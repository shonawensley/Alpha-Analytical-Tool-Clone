#!/usr/bin/env python3
"""
Create a results-horizon report for a corpus window.

Purpose:
  - Profit Alerts and other episode-based evaluations look forward across results dates.
  - Missing future results files produce CENSORED episodes (unknown outcomes).
  - This report makes the horizon explicit so "low performance" isn't misread as corruption.

Scope:
  - Reporting only. Does not change analyzers or sharepacks.

Usage:
  python3 scripts/tools/create_results_horizon_report.py --start 2025-12-30 --end 2026-01-04
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from typing import List, Optional, Tuple


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


def list_results_dates(root: Path) -> List[str]:
    results_dir = root / "data" / "results"
    out: List[str] = []
    if not results_dir.exists():
        return out
    for p in results_dir.glob("*.txt"):
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.txt", p.name):
            out.append(p.stem)
    return sorted(out)


def consecutive_horizon_days(*, available: set[str], start_date: str) -> int:
    """
    Number of consecutive results dates available starting at start_date (inclusive).
    """
    cur = parse_date(start_date)
    n = 0
    while True:
        d = cur.isoformat()
        if d not in available:
            break
        n += 1
        cur += dt.timedelta(days=1)
    return n


def safe_tail(values: List[str], n: int) -> List[str]:
    return values[-n:] if len(values) > n else values


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="Start results date D (YYYY-MM-DD)")
    ap.add_argument("--end", required=True, help="End results date D (YYYY-MM-DD)")
    ap.add_argument(
        "--out",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "2025-12-30_to_2026-01-04__RESULTS_HORIZON.md"),
        help="Output markdown path",
    )
    args = ap.parse_args()

    window_dates = daterange(args.start, args.end)
    all_dates = list_results_dates(ROOT)
    available = set(all_dates)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    max_date = all_dates[-1] if all_dates else None

    lines: List[str] = []
    lines.append(f"# Results Horizon — {args.start} → {args.end}")
    lines.append("")
    lines.append("This report answers: **for each results date D in the corpus window, how much future results data exists?**")
    lines.append("")
    lines.append("Why it matters:")
    lines.append("- Episode-based evaluators (Profit Alerts, cross-variant windows, etc.) require future results dates.")
    lines.append("- Missing future results files produce **CENSORED** episodes (unknown, not failed).")
    lines.append("")
    if max_date:
        lines.append(f"- Latest results file present in `data/results/`: **{max_date}.txt**")
    else:
        lines.append("- No results files found under `data/results/`.")
    lines.append("")

    lines.append("## Window coverage")
    lines.append("")
    lines.append("| D | results file exists | consecutive days available from D | approx max steps (Combined) | approx max steps (Midday/Evening) |")
    lines.append("|---|---:|---:|---:|---:|")
    for d in window_dates:
        exists = d in available
        consec = consecutive_horizon_days(available=available, start_date=d) if exists else 0
        # Approximate upper bounds (actual gradeable steps can be lower if a state has blank Midday/Evening).
        max_steps_combined = 2 * consec
        max_steps_single = consec
        lines.append(f"| {d} | {'yes' if exists else 'no'} | {consec} | {max_steps_combined} | {max_steps_single} |")
    lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append("- `consecutive days` counts include D itself.")
    lines.append("- `max steps (Combined)` assumes two outcomes per day (Midday+Evening). Some states/days have blanks, which reduces actual gradeable steps.")
    lines.append("- `max steps (Midday/Evening)` is a conservative bound for period-faithful grading (one outcome per day).")
    lines.append("")

    if all_dates:
        lines.append("## Latest results dates (tail)")
        lines.append("")
        lines.extend([f"- `{d}.txt`" for d in safe_tail(all_dates, 14)])
        lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

