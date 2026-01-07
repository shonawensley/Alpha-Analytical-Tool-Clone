#!/usr/bin/env python3
"""
Create a small "dashboard" view over the numeric corpus exports.

This is intentionally reporting-only:
  - It does not change analyzers.
  - It reads:
      - RUNS/corpus_tool_metrics.csv (sharepack-derived tool metrics)
      - RUNS/corpus_summary.csv (run-report derived synthesis fields)

Outputs (small, Git-friendly):
  - __CORPUS_DASHBOARD.md
  - __CONVERGENCE_CASES.md
  - __CONVERGENCE_CASES.csv

Usage:
  python3 scripts/tools/create_corpus_dashboard.py --start 2025-12-30 --end 2026-01-04
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
from collections import Counter
from pathlib import Path
from statistics import mean, median
from typing import Dict, List, Optional, Sequence, Tuple


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


def safe_int(value: str) -> Optional[int]:
    v = (value or "").strip()
    if not v:
        return None
    try:
        return int(float(v))
    except Exception:
        return None


def safe_float(value: str) -> Optional[float]:
    v = (value or "").strip()
    if not v:
        return None
    try:
        return float(v)
    except Exception:
        return None


def pct(n: int, d: int) -> str:
    return "0.0%" if d == 0 else f"{(100.0 * n / d):.1f}%"


def pctl(values: Sequence[float], q: float) -> Optional[float]:
    if not values:
        return None
    xs = sorted(values)
    idx = max(0, min(len(xs) - 1, int(round((len(xs) - 1) * q))))
    return xs[idx]


def load_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(encoding="utf-8", errors="replace", newline="") as f:
        dr = csv.DictReader(f)
        return list(dr)


def fmt_float(v: Optional[float]) -> str:
    return "" if v is None else f"{v:.4f}"


def fmt_int(v: Optional[int]) -> str:
    return "" if v is None else str(v)


def write_csv(path: Path, fieldnames: List[str], rows: List[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        dw = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        dw.writeheader()
        for row in rows:
            dw.writerow(row)


def convergence_score(row: Dict[str, str]) -> Tuple[int, List[str]]:
    reasons: List[str] = []
    score = 0

    stable_present = (row.get("stable_families_present") or "") == "1"
    stable_rf = safe_float(row.get("stable_families_rank_fraction") or "")
    if stable_present and stable_rf is not None and stable_rf <= 0.10:
        score += 1
        reasons.append("stable_top10pct")

    hz_present = (row.get("hz_top_lanes_present") or "") == "1"
    hz_rf = safe_float(row.get("hz_top_lanes_rank_fraction") or "")
    if hz_present and hz_rf is not None and hz_rf <= 0.20:
        score += 1
        reasons.append("hz_top20pct")

    vtrac_top10 = (row.get("vtrac_top10_rank") or "").strip()
    if vtrac_top10:
        score += 1
        reasons.append("vtrac_top10")

    dr_best = safe_int(row.get("dr_best_area_rank_vtrac_any") or "")
    if dr_best is not None and dr_best <= 3:
        score += 1
        reasons.append("dr_best_area<=3")

    return score, reasons


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
        "--summary-csv",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "corpus_summary.csv"),
        help="Path to corpus_summary.csv",
    )
    ap.add_argument(
        "--out-dir",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"),
        help="Output directory",
    )
    args = ap.parse_args()

    dates = set(daterange(args.start, args.end))
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    metrics_path = Path(args.metrics_csv)
    summary_path = Path(args.summary_csv)
    if not metrics_path.exists():
        raise SystemExit(f"metrics file not found: {metrics_path}")
    if not summary_path.exists():
        raise SystemExit(f"summary file not found: {summary_path}")

    metrics_rows = [r for r in load_csv(metrics_path) if r.get("date") in dates and (r.get("winner_literal") or "").strip()]
    total = len(metrics_rows)

    by_period = Counter(r.get("period") or "Unknown" for r in metrics_rows)
    stable_present = sum(1 for r in metrics_rows if (r.get("stable_families_present") or "") == "1")
    stable_exact_boxed = sum(1 for r in metrics_rows if (r.get("stable_exact_boxed") or "") == "1")
    stable_exact_straight = sum(1 for r in metrics_rows if (r.get("stable_exact_straight") or "") == "1")

    stable_sections = Counter((r.get("stable_families_section") or "").strip() or "missing" for r in metrics_rows)

    hz_present = sum(1 for r in metrics_rows if (r.get("hz_top_lanes_present") or "") == "1")
    vtrac_top10 = sum(1 for r in metrics_rows if (r.get("vtrac_top10_rank") or "").strip())
    vtrac_top10_combined = sum(
        1
        for r in metrics_rows
        if (r.get("vtrac_top10_rank") or "").strip() and "Combined" in (r.get("vtrac_top10_sections") or "")
    )
    dr_top_present = sum(1 for r in metrics_rows if (r.get("dr_top_winner_present") or "") == "1")
    ba_contains = sum(1 for r in metrics_rows if (r.get("blackapple_top_contains_winner") or "") == "1")
    mirror_sig_repeat = sum(1 for r in metrics_rows if (r.get("winner_vtrac_signature_has_repeat") or "") == "1")

    stable_rank_fracs: List[float] = []
    hz_rank_fracs: List[float] = []
    vtrac_rank_fracs: List[float] = []
    for r in metrics_rows:
        if (r.get("stable_families_present") or "") == "1":
            x = safe_float(r.get("stable_families_rank_fraction") or "")
            if x is not None:
                stable_rank_fracs.append(x)
        if (r.get("hz_top_lanes_present") or "") == "1":
            x = safe_float(r.get("hz_top_lanes_rank_fraction") or "")
            if x is not None:
                hz_rank_fracs.append(x)
        x = safe_float(r.get("vtrac_index_rank_fraction") or "")
        if x is not None:
            vtrac_rank_fracs.append(x)

    # Run-report corpus (environment verdicts / cross-variant mentions)
    summary_rows = [r for r in load_csv(summary_path) if r.get("date") in dates and (r.get("winner_missing") or "0") != "1"]
    env_verdicts = Counter((r.get("env_verdict") or "").strip() or "missing" for r in summary_rows)
    cross_variant_mentions = sum(1 for r in summary_rows if (r.get("cross_variant_mentioned") or "") == "1")

    # Convergence cases (heuristic scoring for "study these examples")
    case_rows: List[Tuple[int, float, Dict[str, str], List[str]]] = []
    score_counts: Counter[int] = Counter()
    for r in metrics_rows:
        score, reasons = convergence_score(r)
        score_counts[score] += 1
        stable_rf = safe_float(r.get("stable_families_rank_fraction") or "")
        stable_key = stable_rf if stable_rf is not None else 9e9
        case_rows.append((score, stable_key, r, reasons))

    case_rows.sort(key=lambda t: (-t[0], t[1]))
    top_cases = [t for t in case_rows if t[0] >= 3][:100]

    # Write convergence CSV
    cases_csv = out_dir / f"{args.start}_to_{args.end}__CONVERGENCE_CASES.csv"
    cases_csv_rows: List[Dict[str, object]] = []
    for score, _, r, reasons in top_cases:
        cases_csv_rows.append(
            {
                "date": r.get("date"),
                "history_date": r.get("history_date"),
                "state": r.get("state"),
                "period": r.get("period"),
                "winner_literal": r.get("winner_literal"),
                "winner_canonical": r.get("winner_canonical"),
                "winner_vtrac_index": r.get("winner_vtrac_index"),
                "mirror_sig_repeat": r.get("winner_vtrac_signature_has_repeat"),
                "stable_rank_fraction": r.get("stable_families_rank_fraction"),
                "stable_section": r.get("stable_families_section"),
                "hz_rank_fraction": r.get("hz_top_lanes_rank_fraction"),
                "vtrac_top10_rank": r.get("vtrac_top10_rank"),
                "vtrac_top10_sections": r.get("vtrac_top10_sections"),
                "dr_best_area_rank_vtrac_any": r.get("dr_best_area_rank_vtrac_any"),
                "blackapple_top_contains_winner": r.get("blackapple_top_contains_winner"),
                "convergence_score": score,
                "convergence_reasons": "|".join(reasons),
            }
        )
    cases_fields = [
        "date",
        "history_date",
        "state",
        "period",
        "winner_literal",
        "winner_canonical",
        "winner_vtrac_index",
        "mirror_sig_repeat",
        "stable_rank_fraction",
        "stable_section",
        "hz_rank_fraction",
        "vtrac_top10_rank",
        "vtrac_top10_sections",
        "dr_best_area_rank_vtrac_any",
        "blackapple_top_contains_winner",
        "convergence_score",
        "convergence_reasons",
    ]
    write_csv(cases_csv, cases_fields, cases_csv_rows)

    # Write dashboard markdown
    dash_md = out_dir / f"{args.start}_to_{args.end}__CORPUS_DASHBOARD.md"
    lines: List[str] = []
    lines.append(f"# Corpus Dashboard — {args.start} → {args.end}")
    lines.append("")
    try:
        lines.append(f"- tool metrics: `{metrics_path.relative_to(ROOT)}`")
        lines.append(f"- run-report corpus: `{summary_path.relative_to(ROOT)}`")
    except Exception:
        lines.append(f"- tool metrics: `{metrics_path}`")
        lines.append(f"- run-report corpus: `{summary_path}`")
    lines.append("")
    lines.append(f"Total graded outcomes (state×period): **{total}**")
    lines.append("")

    lines.append("## Outcome mix")
    lines.append("")
    lines.append("| period | n | % |")
    lines.append("|---|---:|---:|")
    for p in ["Midday", "Evening", "Combined", "Unknown"]:
        n = by_period.get(p, 0)
        if n:
            lines.append(f"| {p} | {n} | {pct(n, total)} |")
    lines.append("")

    lines.append("## Tool presence / exactness (not performance claims)")
    lines.append("")
    lines.append(f"- Stable families present: **{stable_present}/{total}** ({pct(stable_present, total)})")
    lines.append(f"- Hot Zones top lanes present: **{hz_present}/{total}** ({pct(hz_present, total)})")
    lines.append(f"- VTRAC winner index in top10: **{vtrac_top10}/{total}** ({pct(vtrac_top10, total)})")
    if vtrac_top10:
        lines.append(f"- …with Combined among supporting sections: **{vtrac_top10_combined}/{vtrac_top10}** ({pct(vtrac_top10_combined, vtrac_top10)})")
    lines.append(f"- DR top-candidates contain winner: **{dr_top_present}/{total}** ({pct(dr_top_present, total)})")
    lines.append(f"- Blackapple top list contains winner: **{ba_contains}/{total}** ({pct(ba_contains, total)})")
    lines.append(f"- Winner VTRAC signature has repeat (mirror/double-space): **{mirror_sig_repeat}/{total}** ({pct(mirror_sig_repeat, total)})")
    lines.append("")

    lines.append("## Stable evidence origin (section labels)")
    lines.append("")
    lines.append("| stable_section | n | % |")
    lines.append("|---|---:|---:|")
    for sec, n in stable_sections.most_common():
        lines.append(f"| {sec} | {n} | {pct(n, total)} |")
    lines.append("")

    def _dist(name: str, vals: List[float]) -> None:
        if not vals:
            lines.append(f"- {name}: <none>")
            return
        lines.append(
            f"- {name}: n={len(vals)} median={fmt_float(median(vals))} p10={fmt_float(pctl(vals,0.10))} p25={fmt_float(pctl(vals,0.25))} p75={fmt_float(pctl(vals,0.75))}"
        )

    lines.append("## Rank-fraction distributions (lower is better)")
    lines.append("")
    _dist("Stable family rank_fraction", stable_rank_fracs)
    _dist("Hot Zones top_lanes rank_fraction", hz_rank_fracs)
    _dist("VTRAC index rank_fraction", vtrac_rank_fracs)
    lines.append("")

    lines.append("## Run-report synthesis (from completed RUNS)")
    lines.append("")
    if summary_rows:
        denom = len(summary_rows)
        lines.append(f"- Run-report rows: **{denom}**")
        lines.append(f"- Cross-variant mentioned: **{cross_variant_mentions}/{denom}** ({pct(cross_variant_mentions, denom)})")
        lines.append("")
        lines.append("| env_verdict | n | % |")
        lines.append("|---|---:|---:|")
        for k, n in env_verdicts.most_common():
            lines.append(f"| {k} | {n} | {pct(n, denom)} |")
        lines.append("")
    else:
        lines.append("- No run-report rows found for this date range in corpus_summary.csv.")
        lines.append("")

    lines.append("## Convergence score (heuristic; used to pick study examples)")
    lines.append("")
    lines.append("| score | n | % | meaning |")
    lines.append("|---:|---:|---:|---|")
    for s in sorted(score_counts.keys(), reverse=True):
        n = score_counts[s]
        meaning = {
            4: "Stable(top10%) + HotZones(top20%) + VTRAC top10 + DR best_area<=3",
            3: "3 of the 4 convergence lenses present",
            2: "2 lenses",
            1: "1 lens",
            0: "no convergence lenses",
        }.get(s, "")
        lines.append(f"| {s} | {n} | {pct(n, total)} | {meaning} |")
    lines.append("")
    try:
        lines.append(f"Top convergence cases CSV: `{cases_csv.relative_to(ROOT)}`")
    except Exception:
        lines.append(f"Top convergence cases CSV: `{cases_csv}`")
    lines.append("")
    dash_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Convergence cases markdown (short)
    cases_md = out_dir / f"{args.start}_to_{args.end}__CONVERGENCE_CASES.md"
    cl: List[str] = []
    cl.append(f"# Convergence Cases — {args.start} → {args.end}")
    cl.append("")
    cl.append("These are *study targets* (not rules): outcomes where multiple lenses strongly supported the winner.")
    cl.append("")
    try:
        cl.append(f"CSV: `{cases_csv.relative_to(ROOT)}`")
    except Exception:
        cl.append(f"CSV: `{cases_csv}`")
    cl.append("")
    cl.append("| date | state | period | winner | score | reasons | stable_rf | stable_sec | hz_rf | vtrac_top10 | dr_best_area | BA_contains |")
    cl.append("|---|---|---|---|---:|---|---:|---|---:|---:|---:|---:|")
    for score, _, r, reasons in top_cases[:50]:
        cl.append(
            "| "
            + " | ".join(
                [
                    r.get("date") or "",
                    r.get("state") or "",
                    r.get("period") or "",
                    r.get("winner_literal") or "",
                    str(score),
                    ",".join(reasons),
                    (r.get("stable_families_rank_fraction") or ""),
                    (r.get("stable_families_section") or ""),
                    (r.get("hz_top_lanes_rank_fraction") or ""),
                    (r.get("vtrac_top10_rank") or ""),
                    (r.get("dr_best_area_rank_vtrac_any") or ""),
                    (r.get("blackapple_top_contains_winner") or ""),
                ]
            )
            + " |"
        )
    cl.append("")
    cases_md.write_text("\n".join(cl) + "\n", encoding="utf-8")

    print(f"Wrote: {dash_md}")
    print(f"Wrote: {cases_md}")
    print(f"Wrote: {cases_csv}")


if __name__ == "__main__":
    main()

