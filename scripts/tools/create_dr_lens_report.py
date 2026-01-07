#!/usr/bin/env python3
"""
Create a Digit Reduction (DR) "long-string lens" corpus report from corpus_tool_metrics.csv.

Scope:
  - Reporting/instrumentation only. Does NOT change any analyzer behavior.
  - Intended to answer: "Is DR activating (items_total>0)? When is it empty (items_total=0)?"
    and "When it activates, how often does it score/flag the winner within its own outputs?"

Usage:
  python3 scripts/tools/create_dr_lens_report.py --start 2025-12-30 --end 2026-01-04
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List


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


def safe_int(value: str) -> int | None:
    try:
        if value is None or value == "":
            return None
        return int(value)
    except Exception:
        return None


def safe_float(value: str) -> float | None:
    try:
        if value is None or value == "":
            return None
        return float(value)
    except Exception:
        return None


def pct(n: int, d: int) -> str:
    return "0.0%" if d == 0 else f"{(100.0 * n / d):.1f}%"


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
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "2025-12-30_to_2026-01-04__DR_LENS_REPORT.md"),
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

    by_period: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for r in rows:
        by_period[r.get("period", "")].append(r)

    # Activation buckets
    activation_counts = Counter()
    activation_by_period: Dict[str, Counter[str]] = defaultdict(Counter)

    def activation_bucket(r: Dict[str, str]) -> str:
        if r.get("dr_skipped") == "1":
            return "skipped"
        items_total = safe_int(r.get("dr_stamp_items_total", "")) if r.get("dr_stamp_items_total") is not None else None
        if items_total is None:
            return "missing"
        if items_total == 0:
            return "empty"
        return "active"

    for r in rows:
        b = activation_bucket(r)
        activation_counts[b] += 1
        activation_by_period[r.get("period", "")][b] += 1

    # Winner-flag/hit aggregates (only when active)
    active_rows = [r for r in rows if activation_bucket(r) == "active"]
    active_total = len(active_rows)

    def sum_int(field: str, *, rows: List[Dict[str, str]]) -> int:
        out = 0
        for r in rows:
            v = safe_int(r.get(field, ""))
            if v is None:
                continue
            out += v
        return out

    def count_any(field: str, *, rows: List[Dict[str, str]]) -> int:
        out = 0
        for r in rows:
            v = safe_int(r.get(field, ""))
            if v is None:
                continue
            if v > 0:
                out += 1
        return out

    # Note: many DR fields are counts across overlay rows, not booleans.
    top_present_any = count_any("dr_top_winner_present", rows=active_rows)
    flags_vt_boxed_any = count_any("dr_flags_dr_win_vt_boxed", rows=active_rows)
    flags_vt_straight_any = count_any("dr_flags_dr_win_vt_straight", rows=active_rows)
    hits_vt_boxed_any = count_any("dr_hits_final_vt_boxed", rows=active_rows)
    hits_vt_straight_any = count_any("dr_hits_final_vt_straight", rows=active_rows)

    flags_vt_boxed_total = sum_int("dr_flags_dr_win_vt_boxed", rows=active_rows)
    flags_vt_straight_total = sum_int("dr_flags_dr_win_vt_straight", rows=active_rows)
    hits_vt_boxed_total = sum_int("dr_hits_final_vt_boxed", rows=active_rows)
    hits_vt_straight_total = sum_int("dr_hits_final_vt_straight", rows=active_rows)

    # Items_total distribution (active only)
    items_totals = sorted([safe_int(r.get("dr_stamp_items_total", "")) for r in active_rows if safe_int(r.get("dr_stamp_items_total", "")) is not None])
    items_min = items_totals[0] if items_totals else None
    items_max = items_totals[-1] if items_totals else None
    items_mean = (sum(items_totals) / len(items_totals)) if items_totals else None

    # Top rank fraction distribution (active only)
    rank_fracs = sorted([safe_float(r.get("dr_top_winner_rank_fraction", "")) for r in active_rows if safe_float(r.get("dr_top_winner_rank_fraction", "")) is not None])
    rank_frac_mean = (sum(rank_fracs) / len(rank_fracs)) if rank_fracs else None

    # Collect small example tables (for human spot-check)
    empty_examples: List[Dict[str, str]] = [r for r in rows if activation_bucket(r) == "empty"][:20]
    skipped_examples: List[Dict[str, str]] = [r for r in rows if activation_bucket(r) == "skipped"][:20]
    active_examples = sorted(
        [r for r in active_rows],
        key=lambda r: safe_int(r.get("dr_stamp_items_total", "")) or 0,
        reverse=True,
    )[:20]

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines: List[str] = []
    lines.append(f"# Digit Reduction Lens Report — {args.start} → {args.end}")
    lines.append("")
    lines.append("This report focuses on the **DR long‑string lens** (the yellow‑box / long‑string activation) and its basic outcome tags.")
    lines.append("")
    lines.append("Data sources:")
    lines.append(f"- metrics: `{metrics_display}`")
    lines.append("- DR activation proxy: `dr_stamp_items_total` (active if >0, empty if 0)")
    lines.append("- DR winner tags: `dr_flags_dr_win_*` + `dr_hits_final_*` (when active)")
    lines.append("")
    lines.append(f"Total graded outcomes (state×period rows): **{total}**")
    lines.append("")

    lines.append("## DR lens activation (does DR produce long‑string items?)")
    lines.append("")
    lines.append("| Bucket | Count | % | Meaning |")
    lines.append("|---|---:|---:|---|")
    for bucket in ["active", "empty", "skipped", "missing"]:
        n = activation_counts.get(bucket, 0)
        if n == 0:
            continue
        meaning = {
            "active": "DR long‑string lens produced items (items_total>0)",
            "empty": "DR ran but produced no items (items_total=0)",
            "skipped": "State/period missing in results (expected on some days, e.g., Puerto Rico)",
            "missing": "DR summary missing or schema missing for that row",
        }[bucket]
        lines.append(f"| {bucket} | {n} | {pct(n, total)} | {meaning} |")
    lines.append("")

    for period in ["Midday", "Evening"]:
        if period not in activation_by_period:
            continue
        c = activation_by_period[period]
        denom = sum(c.values())
        lines.append(f"### {period} breakdown (n={denom})")
        lines.append("")
        lines.append("| Bucket | Count | % |")
        lines.append("|---|---:|---:|")
        for bucket in ["active", "empty", "skipped", "missing"]:
            n = c.get(bucket, 0)
            if n == 0:
                continue
            lines.append(f"| {bucket} | {n} | {pct(n, denom)} |")
        lines.append("")

    lines.append("## When DR is active: outcome tags (winner‑aligned)")
    lines.append("")
    lines.append(f"Active rows: **{active_total}/{total}** ({pct(active_total, total)})")
    lines.append("")
    lines.append("| Tag | Count | % of active |")
    lines.append("|---|---:|---:|")
    if active_total:
        lines.append(f"| top.winner_present (any) | {top_present_any} | {pct(top_present_any, active_total)} |")
        lines.append(f"| flags.dr_win_vt_boxed (any) | {flags_vt_boxed_any} | {pct(flags_vt_boxed_any, active_total)} |")
        lines.append(f"| flags.dr_win_vt_straight (any) | {flags_vt_straight_any} | {pct(flags_vt_straight_any, active_total)} |")
        lines.append(f"| hits.final_vt_boxed (any) | {hits_vt_boxed_any} | {pct(hits_vt_boxed_any, active_total)} |")
        lines.append(f"| hits.final_vt_straight (any) | {hits_vt_straight_any} | {pct(hits_vt_straight_any, active_total)} |")
    lines.append("")
    if active_total:
        lines.append("Counts note: the `flags.*` and `hits.*` fields are **row counts** inside the DR overlay (not booleans).")
        lines.append("")
        lines.append("| Counter | Total (sum across active rows) |")
        lines.append("|---|---:|")
        lines.append(f"| flags.dr_win_vt_boxed total | {flags_vt_boxed_total} |")
        lines.append(f"| flags.dr_win_vt_straight total | {flags_vt_straight_total} |")
        lines.append(f"| hits.final_vt_boxed total | {hits_vt_boxed_total} |")
        lines.append(f"| hits.final_vt_straight total | {hits_vt_straight_total} |")
        lines.append("")

    lines.append("## Long‑string volume (items_total distribution when active)")
    lines.append("")
    if items_totals:
        lines.append(f"- min: **{items_min}**, max: **{items_max}**, mean: **{items_mean:.1f}** (n={len(items_totals)})")
    else:
        lines.append("- <no active rows>")
    lines.append("")

    lines.append("## DR top-candidate strength (rank_fraction when active)")
    lines.append("")
    if rank_fracs:
        lines.append(f"- mean winner_rank_fraction: **{rank_frac_mean:.3f}** (lower is better; n={len(rank_fracs)})")
    else:
        lines.append("- <no rank_fraction values>")
    lines.append("")

    def render_examples(title: str, ex_rows: List[Dict[str, str]], *, include_skip: bool = False) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not ex_rows:
            lines.append("- <none>")
            lines.append("")
            return
        if include_skip:
            lines.append("| date | state | period | winner | skip_reason |")
            lines.append("|---|---|---|---|---|")
            for r in ex_rows:
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            r.get("date", ""),
                            r.get("state", ""),
                            r.get("period", ""),
                            r.get("winner_literal", ""),
                            (r.get("dr_skip_reason") or "").replace("|", "\\|"),
                        ]
                    )
                    + " |"
                )
        else:
            lines.append("| date | state | period | winner | items_total | top_present | top_best_rank | rank_frac |")
            lines.append("|---|---|---|---|---:|---:|---:|---:|")
            for r in ex_rows:
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            r.get("date", ""),
                            r.get("state", ""),
                            r.get("period", ""),
                            r.get("winner_literal", ""),
                            r.get("dr_stamp_items_total", ""),
                            r.get("dr_top_winner_present", ""),
                            r.get("dr_top_winner_best_rank", ""),
                            r.get("dr_top_winner_rank_fraction", ""),
                        ]
                    )
                    + " |"
                )
        lines.append("")

    render_examples("Active examples (highest items_total first)", active_examples)
    render_examples("Empty examples (items_total=0)", empty_examples)
    render_examples("Skipped examples (missing period/state in results)", skipped_examples, include_skip=True)

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
