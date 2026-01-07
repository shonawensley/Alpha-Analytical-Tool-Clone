#!/usr/bin/env python3
"""
Roll up Brain-2 Control Center "boards" across a date range.

This is intentionally reporting-only:
  - It does not change analyzers.
  - It reads existing sharepack Brain-2 artifacts under sharepacks/<D>/control_center/.

Boards:
  - blackapple_alerts.csv
  - due_doubles.csv
  - vtrac_repeat_watch.csv

Outputs (small, Git-friendly):
  - __CONTROL_CENTER_ROLLUP.csv  (per-day metrics)
  - __CONTROL_CENTER_ROLLUP.md   (human summary)

Usage:
  python3 scripts/tools/rollup_control_center_boards.py --start 2025-12-30 --end 2026-01-04
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
from collections import Counter
from pathlib import Path
from statistics import mean
from typing import Dict, List, Optional


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


def load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open(encoding="utf-8", errors="replace", newline="") as f:
        dr = csv.DictReader(f)
        return list(dr)


def write_csv(path: Path, fieldnames: List[str], rows: List[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        dw = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        dw.writeheader()
        for row in rows:
            dw.writerow(row)


def pct(n: int, d: int) -> str:
    return "0.0%" if d == 0 else f"{(100.0 * n / d):.1f}%"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="Start results date D (YYYY-MM-DD)")
    ap.add_argument("--end", required=True, help="End results date D (YYYY-MM-DD)")
    ap.add_argument(
        "--out-dir",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"),
        help="Output directory",
    )
    ap.add_argument(
        "--sharepacks-dir",
        default=str(ROOT / "sharepacks"),
        help="Sharepacks root directory",
    )
    args = ap.parse_args()

    dates = daterange(args.start, args.end)
    sharepacks_root = Path(args.sharepacks_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    per_day_rows: List[Dict[str, object]] = []

    # Aggregate summaries
    ba_status_counts: Counter[str] = Counter()
    ba_midday_hits_total = 0
    ba_evening_hits_total = 0
    ba_rows_total = 0
    ba_scores: List[int] = []

    dd_midday_in_family_total = 0
    dd_evening_in_family_total = 0
    dd_rows_total = 0
    dd_draws_since: List[int] = []

    rw_eq_winner_total = 0
    rw_rows_total = 0
    rw_streaks: List[int] = []

    missing_days: List[str] = []

    for d in dates:
        cc_dir = sharepacks_root / d / "control_center"
        ba_path = cc_dir / "blackapple_alerts.csv"
        dd_path = cc_dir / "due_doubles.csv"
        rw_path = cc_dir / "vtrac_repeat_watch.csv"

        if not (ba_path.exists() and dd_path.exists() and rw_path.exists()):
            missing_days.append(d)
            continue

        # Blackapple
        ba_rows = load_csv_rows(ba_path)
        ba_rows_total += len(ba_rows)
        per_status = Counter((r.get("Status") or "").strip() or "missing" for r in ba_rows)
        ba_status_counts.update(per_status)
        ba_midday_hits = sum(1 for r in ba_rows if (r.get("Midday Hits") or "").strip() not in {"", "-"})
        ba_evening_hits = sum(1 for r in ba_rows if (r.get("Evening Hits") or "").strip() not in {"", "-"})
        ba_midday_hits_total += ba_midday_hits
        ba_evening_hits_total += ba_evening_hits
        for r in ba_rows:
            s = safe_int(r.get("BA-Score") or "")
            if s is not None:
                ba_scores.append(s)

        # Due doubles
        dd_rows = load_csv_rows(dd_path)
        dd_rows_total += len(dd_rows)
        dd_midday_in = sum(1 for r in dd_rows if (r.get("Midday Winner In Family") or "").strip() == "True")
        dd_evening_in = sum(1 for r in dd_rows if (r.get("Evening Winner In Family") or "").strip() == "True")
        dd_midday_in_family_total += dd_midday_in
        dd_evening_in_family_total += dd_evening_in
        for r in dd_rows:
            x = safe_int(r.get("Draws Since Double") or "")
            if x is not None:
                dd_draws_since.append(x)

        # VTRAC repeat watch
        rw_rows = load_csv_rows(rw_path)
        rw_rows_total += len(rw_rows)
        rw_eq = sum(1 for r in rw_rows if (r.get("Current==WinnerVTRAC") or "").strip() == "True")
        rw_eq_winner_total += rw_eq
        for r in rw_rows:
            x = safe_int(r.get("Current Streak") or "")
            if x is not None:
                rw_streaks.append(x)

        per_day_rows.append(
            {
                "date": d,
                "blackapple_rows": len(ba_rows),
                "blackapple_ALERT": per_status.get("ALERT", 0),
                "blackapple_WATCH": per_status.get("WATCH", 0),
                "blackapple_OFF": per_status.get("OFF", 0),
                "blackapple_midday_hits": ba_midday_hits,
                "blackapple_evening_hits": ba_evening_hits,
                "due_doubles_rows": len(dd_rows),
                "due_doubles_midday_in_family": dd_midday_in,
                "due_doubles_evening_in_family": dd_evening_in,
                "repeat_watch_rows": len(rw_rows),
                "repeat_watch_current_eq_winner": rw_eq,
            }
        )

    stem = f"{args.start}_to_{args.end}__CONTROL_CENTER_ROLLUP"
    csv_path = out_dir / f"{stem}.csv"
    md_path = out_dir / f"{stem}.md"

    fields = [
        "date",
        "blackapple_rows",
        "blackapple_ALERT",
        "blackapple_WATCH",
        "blackapple_OFF",
        "blackapple_midday_hits",
        "blackapple_evening_hits",
        "due_doubles_rows",
        "due_doubles_midday_in_family",
        "due_doubles_evening_in_family",
        "repeat_watch_rows",
        "repeat_watch_current_eq_winner",
    ]
    write_csv(csv_path, fields, per_day_rows)

    lines: List[str] = []
    lines.append(f"# Control Center Boards Rollup — {args.start} → {args.end}")
    lines.append("")
    lines.append("This summarizes the Brain-2 Control Center board exports across a date range.")
    lines.append("")
    lines.append("Inputs (per day):")
    lines.append("- `sharepacks/<D>/control_center/blackapple_alerts.csv`")
    lines.append("- `sharepacks/<D>/control_center/due_doubles.csv`")
    lines.append("- `sharepacks/<D>/control_center/vtrac_repeat_watch.csv`")
    lines.append("")
    try:
        lines.append(f"Per-day CSV: `{csv_path.relative_to(ROOT)}`")
    except Exception:
        lines.append(f"Per-day CSV: `{csv_path}`")
    lines.append("")

    if missing_days:
        lines.append("## Missing days (skipped)")
        lines.append("")
        lines.append("- " + ", ".join(missing_days))
        lines.append("")

    lines.append("## Blackapple Alerts (board-level)")
    lines.append("")
    lines.append(f"- Rows: **{ba_rows_total}**")
    for k in ["ALERT", "WATCH", "OFF", "missing"]:
        n = ba_status_counts.get(k, 0)
        if n:
            lines.append(f"- Status {k}: **{n}/{ba_rows_total}** ({pct(n, ba_rows_total)})")
    lines.append(f"- Midday hits (any non-'-' tag): **{ba_midday_hits_total}/{ba_rows_total}** ({pct(ba_midday_hits_total, ba_rows_total)})")
    lines.append(f"- Evening hits (any non-'-' tag): **{ba_evening_hits_total}/{ba_rows_total}** ({pct(ba_evening_hits_total, ba_rows_total)})")
    if ba_scores:
        lines.append(f"- BA-Score mean: **{mean(ba_scores):.2f}** (n={len(ba_scores)})")
    lines.append("")

    lines.append("## Due Doubles (board-level)")
    lines.append("")
    lines.append(f"- Rows: **{dd_rows_total}**")
    lines.append(f"- Midday winner in any family: **{dd_midday_in_family_total}/{dd_rows_total}** ({pct(dd_midday_in_family_total, dd_rows_total)})")
    lines.append(f"- Evening winner in any family: **{dd_evening_in_family_total}/{dd_rows_total}** ({pct(dd_evening_in_family_total, dd_rows_total)})")
    if dd_draws_since:
        lines.append(f"- Draws-since-double mean: **{mean(dd_draws_since):.2f}** (n={len(dd_draws_since)})")
    lines.append("")

    lines.append("## VTRAC Repeat Watch (board-level)")
    lines.append("")
    lines.append(f"- Rows: **{rw_rows_total}**")
    lines.append(f"- Current index == winner VTRAC: **{rw_eq_winner_total}/{rw_rows_total}** ({pct(rw_eq_winner_total, rw_rows_total)})")
    if rw_streaks:
        lines.append(f"- Current streak mean: **{mean(rw_streaks):.2f}** (n={len(rw_streaks)})")
    lines.append("")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote: {csv_path}")
    print(f"Wrote: {md_path}")


if __name__ == "__main__":
    main()

