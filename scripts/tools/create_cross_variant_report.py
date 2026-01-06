#!/usr/bin/env python3
"""
Create a cross-variant / Combined influence report from corpus_tool_metrics.csv.

This is intentionally reporting-only:
  - It does not change analyzers.
  - It quantifies how often the strongest evidence appears to come from:
      - the same period (Midday/Evening),
      - the opposite period (bounce),
      - or Combined (lens),
    using Stable and VTRAC evidence fields exported in corpus_tool_metrics.csv.

Usage:
  python3 scripts/tools/create_cross_variant_report.py --start 2025-12-30 --end 2026-01-04
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[2]


def parse_date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def daterange(start: str, end: str) -> List[str]:
    s = parse_date(start)
    e = parse_date(end)
    if e < s:
        raise SystemExit("--end must be >= --start")
    out: List[str] = []
    cur = s
    while cur <= e:
        out.append(cur.isoformat())
        cur += dt.timedelta(days=1)
    return out


def load_rows(path: Path, *, dates: set[str]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    with path.open(encoding="utf-8", errors="replace", newline="") as f:
        dr = csv.DictReader(f)
        for row in dr:
            if row.get("date") in dates:
                rows.append(row)
    return rows


def pct(n: int, d: int) -> str:
    return "0.0%" if d == 0 else f"{(100.0 * n / d):.1f}%"


def stable_origin_bucket(period: str, origin: str) -> str:
    if not origin:
        return "missing"
    if origin == period:
        return "same_period"
    if origin == "Combined":
        return "combined"
    if origin in {"Midday", "Evening"}:
        return "other_period"
    return "other"


def parse_vtrac_sections(value: str) -> List[str]:
    parts = [p.strip() for p in (value or "").split("|") if p.strip()]
    return parts


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="Start results date D (YYYY-MM-DD)")
    ap.add_argument("--end", required=True, help="End results date D (YYYY-MM-DD)")
    ap.add_argument(
        "--metrics-csv",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "corpus_tool_metrics.csv"),
        help="Path to corpus_tool_metrics.csv",
    )
    ap.add_argument(
        "--out",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "2025-12-30_to_2026-01-04__CROSS_VARIANT_REPORT.md"),
        help="Output markdown path",
    )
    args = ap.parse_args()

    dates = set(daterange(args.start, args.end))
    metrics_path = Path(args.metrics_csv)
    if not metrics_path.exists():
        raise SystemExit(f"metrics file not found: {metrics_path}")
    try:
        metrics_display = str(metrics_path.relative_to(ROOT))
    except Exception:
        metrics_display = str(metrics_path)

    rows = load_rows(metrics_path, dates=dates)
    rows = [r for r in rows if r.get("winner_literal")]  # ignore missing winners

    total = len(rows)

    # Stable origin buckets
    stable_bucket_counts: Counter[str] = Counter()
    stable_bucket_by_period: Dict[str, Counter[str]] = defaultdict(Counter)
    bounce_examples: List[Tuple[float, Dict[str, str]]] = []
    combined_examples: List[Tuple[float, Dict[str, str]]] = []

    for r in rows:
        period = r.get("period", "")
        origin = r.get("stable_families_section", "")
        bucket = stable_origin_bucket(period, origin)
        stable_bucket_counts[bucket] += 1
        stable_bucket_by_period[period][bucket] += 1

        rank_frac = None
        try:
            rank_frac = float(r.get("stable_families_rank_fraction") or "")
        except Exception:
            rank_frac = None
        score = rank_frac if rank_frac is not None else 9e9

        if bucket == "other_period":
            bounce_examples.append((score, r))
        if bucket == "combined":
            combined_examples.append((score, r))

    bounce_examples.sort(key=lambda t: t[0])
    combined_examples.sort(key=lambda t: t[0])

    # VTRAC winner-index sections
    vtrac_in_top10 = [r for r in rows if r.get("vtrac_top10_rank")]
    vtrac_top10_total = len(vtrac_in_top10)
    vtrac_combined_support = 0
    vtrac_midday_support = 0
    vtrac_evening_support = 0
    for r in vtrac_in_top10:
        secs = set(parse_vtrac_sections(r.get("vtrac_top10_sections", "")))
        if "Combined" in secs:
            vtrac_combined_support += 1
        if "Midday" in secs:
            vtrac_midday_support += 1
        if "Evening" in secs:
            vtrac_evening_support += 1

    # Write report
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines: List[str] = []
    lines.append(f"# Cross‑Variant / Combined Report — {args.start} → {args.end}")
    lines.append("")
    lines.append("This report quantifies how often the strongest evidence appears to come from Combined or cross‑variant sources.")
    lines.append("")
    lines.append("Data sources:")
    lines.append(f"- metrics: `{metrics_display}`")
    lines.append("- Stable cross‑variant proxy: `stable_families_section` in Stable sharepack summaries")
    lines.append("- VTRAC Combined proxy: whether the winner’s index appears in the day’s `top_indices` and which sections support it (`vtrac_top10_sections`).")
    lines.append("")
    lines.append(f"Total graded outcomes (state×period rows): **{total}**")
    lines.append("")

    lines.append("## Stable origin (where the winner’s best Stable family evidence came from)")
    lines.append("")
    lines.append("| Bucket | Count | % | Meaning |")
    lines.append("|---|---:|---:|---|")
    for bucket in ["same_period", "other_period", "combined", "missing", "other"]:
        n = stable_bucket_counts.get(bucket, 0)
        if n == 0:
            continue
        meaning = {
            "same_period": "Stable’s strongest family evidence came from the same period section",
            "other_period": "Cross‑variant bounce: strongest evidence came from the opposite period section",
            "combined": "Combined lens: strongest evidence came from Combined section",
            "missing": "No Stable family evidence captured",
            "other": "Unexpected/unknown section label",
        }[bucket]
        lines.append(f"| {bucket} | {n} | {pct(n, total)} | {meaning} |")
    lines.append("")

    for period in ["Midday", "Evening"]:
        if period not in stable_bucket_by_period:
            continue
        c = stable_bucket_by_period[period]
        denom = sum(c.values())
        lines.append(f"### {period} breakdown (n={denom})")
        lines.append("")
        lines.append("| Bucket | Count | % |")
        lines.append("|---|---:|---:|")
        for bucket in ["same_period", "other_period", "combined", "missing", "other"]:
            n = c.get(bucket, 0)
            if n == 0:
                continue
            lines.append(f"| {bucket} | {n} | {pct(n, denom)} |")
        lines.append("")

    lines.append("## VTRAC Combined support (winner index appears in top indices)")
    lines.append("")
    lines.append(f"- Winner index appears in VTRAC top indices: **{vtrac_top10_total}/{total}** ({pct(vtrac_top10_total, total)})")
    if vtrac_top10_total:
        lines.append(f"- Of those top-index appearances: Combined supports **{vtrac_combined_support}/{vtrac_top10_total}** ({pct(vtrac_combined_support, vtrac_top10_total)})")
        lines.append(f"- Midday supports **{vtrac_midday_support}/{vtrac_top10_total}** ({pct(vtrac_midday_support, vtrac_top10_total)})")
        lines.append(f"- Evening supports **{vtrac_evening_support}/{vtrac_top10_total}** ({pct(vtrac_evening_support, vtrac_top10_total)})")
    lines.append("")

    def _example_block(title: str, items: List[Tuple[float, Dict[str, str]]]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not items:
            lines.append("- <none>")
            lines.append("")
            return
        lines.append("| date | state | period | winner | stable_section | stable_rank_frac | stable_best_rank |")
        lines.append("|---|---|---|---|---|---:|---:|")
        for _, r in items[:20]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        r.get("date", ""),
                        r.get("state", ""),
                        r.get("period", ""),
                        r.get("winner_literal", ""),
                        r.get("stable_families_section", ""),
                        r.get("stable_families_rank_fraction", ""),
                        r.get("stable_families_best_rank", ""),
                    ]
                )
                + " |"
            )
        lines.append("")

    _example_block("Strongest cross‑variant bounce examples (Stable evidence came from opposite period)", bounce_examples)
    _example_block("Strongest Combined‑driven examples (Stable evidence came from Combined section)", combined_examples)

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
