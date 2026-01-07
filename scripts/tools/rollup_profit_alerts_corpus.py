#!/usr/bin/env python3
"""
Roll up Profit Alerts evaluation outputs across a date range.

This is intentionally evaluation/reporting-only:
  - It does not change analyzers.
  - It reads existing sharepack Brain-2 artifacts under sharepacks/<D>/control_center/.

Outputs (small, Git-friendly):
  - __PROFIT_ALERTS_ROLLUP_ROWS.csv   (per AlertId; profit_alerts_eval.csv)
  - __PROFIT_ALERTS_ROLLUP_MERGED.csv (per suggested_kinds + per alert_ids group; profit_alerts_eval_merged.csv)
  - __PROFIT_ALERTS_ROLLUP.md         (human summary)

Usage:
  python3 scripts/tools/rollup_profit_alerts_corpus.py --start 2025-12-30 --end 2026-01-04
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import math
from collections import Counter, defaultdict
from dataclasses import dataclass, field
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


def pct(n: int, d: int) -> str:
    return "0.0%" if d == 0 else f"{(100.0 * n / d):.1f}%"


def rate(n: int, d: int) -> str:
    return "" if d == 0 else f"{(n / d):.4f}"


def p90(values: Sequence[int]) -> Optional[int]:
    if not values:
        return None
    xs = sorted(values)
    idx = max(0, math.ceil(0.9 * len(xs)) - 1)
    return xs[idx]


def ynq_bucket(value: str) -> str:
    v = (value or "").strip().upper()
    if v in {"Y", "N", "?"}:
        return v
    return ""


@dataclass
class HitCounters:
    measured: int = 0
    hits: int = 0
    unknown: int = 0

    def add(self, value: str) -> None:
        b = ynq_bucket(value)
        if b == "Y":
            self.measured += 1
            self.hits += 1
        elif b == "N":
            self.measured += 1
        elif b == "?":
            self.unknown += 1


@dataclass
class RowAgg:
    rows_total: int = 0
    rows_candidates: int = 0
    rows_promoters: int = 0
    status_counts: Counter[str] = field(default_factory=Counter)

    hit_decay: HitCounters = field(default_factory=HitCounters)
    hit_any_decay: HitCounters = field(default_factory=HitCounters)
    hit_7: HitCounters = field(default_factory=HitCounters)
    hit_any_7: HitCounters = field(default_factory=HitCounters)
    hit_14: HitCounters = field(default_factory=HitCounters)
    hit_any_14: HitCounters = field(default_factory=HitCounters)

    time_to_hit_steps: List[int] = field(default_factory=list)
    implied_set_sizes: List[int] = field(default_factory=list)
    strengths: List[int] = field(default_factory=list)

    def add_row(self, row: Dict[str, str]) -> None:
        self.rows_total += 1
        row_type = (row.get("row_type") or "").strip().upper()
        if row_type == "CANDIDATE":
            self.rows_candidates += 1
        elif row_type == "PROMOTER":
            self.rows_promoters += 1

        status = (row.get("status") or "").strip().upper()
        if status:
            self.status_counts[status] += 1

        if row_type == "CANDIDATE":
            self.hit_decay.add(row.get("hit_within_decay", ""))
            self.hit_any_decay.add(row.get("hit_any_within_decay", ""))
            self.hit_7.add(row.get("hit_within_7", ""))
            self.hit_any_7.add(row.get("hit_any_within_7", ""))
            self.hit_14.add(row.get("hit_within_14", ""))
            self.hit_any_14.add(row.get("hit_any_within_14", ""))

            t = safe_int(row.get("time_to_hit_steps") or "")
            if status == "HIT" and t is not None:
                self.time_to_hit_steps.append(t)

            ss = safe_int(row.get("implied_set_size") or "")
            if ss is not None:
                self.implied_set_sizes.append(ss)

            st = safe_int(row.get("strength") or "")
            if st is not None:
                self.strengths.append(st)


@dataclass
class MergedAgg:
    rows_total: int = 0
    status_counts: Counter[str] = field(default_factory=Counter)
    hit_any_decay: HitCounters = field(default_factory=HitCounters)
    hit_any_7: HitCounters = field(default_factory=HitCounters)
    hit_any_14: HitCounters = field(default_factory=HitCounters)
    time_to_hit_steps: List[int] = field(default_factory=list)
    implied_set_sizes: List[int] = field(default_factory=list)

    def add_row(self, row: Dict[str, str]) -> None:
        self.rows_total += 1
        status = (row.get("status") or "").strip().upper()
        if status:
            self.status_counts[status] += 1

        self.hit_any_decay.add(row.get("hit_any_within_decay", ""))
        self.hit_any_7.add(row.get("hit_any_within_7", ""))
        self.hit_any_14.add(row.get("hit_any_within_14", ""))

        t = safe_int(row.get("time_to_hit_steps") or "")
        if status == "HIT" and t is not None:
            self.time_to_hit_steps.append(t)

        ss = safe_int(row.get("implied_set_size") or "")
        if ss is not None:
            self.implied_set_sizes.append(ss)


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


def fmt_float(v: Optional[float]) -> str:
    return "" if v is None else f"{v:.3f}"


def fmt_int(v: Optional[int]) -> str:
    return "" if v is None else str(v)


def hit_summary(h: HitCounters) -> Tuple[int, int, int, str]:
    return (h.hits, h.measured, h.unknown, rate(h.hits, h.measured))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="Start results date D (YYYY-MM-DD)")
    ap.add_argument("--end", required=True, help="End results date D (YYYY-MM-DD)")
    ap.add_argument(
        "--out-dir",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"),
        help="Output directory for rollups",
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

    by_alert: Dict[str, RowAgg] = defaultdict(RowAgg)
    overall_rows = RowAgg()

    merged_by_suggested: Dict[str, MergedAgg] = defaultdict(MergedAgg)
    merged_by_alert_ids: Dict[str, MergedAgg] = defaultdict(MergedAgg)
    overall_merged = MergedAgg()

    missing_eval: List[str] = []
    missing_merged: List[str] = []

    for d in dates:
        eval_path = sharepacks_root / d / "control_center" / "profit_alerts_eval.csv"
        merged_path = sharepacks_root / d / "control_center" / "profit_alerts_eval_merged.csv"

        if eval_path.exists():
            for row in load_csv_rows(eval_path):
                aid = (row.get("alert_id") or "").strip().upper() or "UNKNOWN"
                by_alert[aid].add_row(row)
                overall_rows.add_row(row)
        else:
            missing_eval.append(d)

        if merged_path.exists():
            for row in load_csv_rows(merged_path):
                suggested = (row.get("suggested_kinds") or "").strip() or "UNKNOWN"
                alert_ids = (row.get("alert_ids") or "").strip() or "UNKNOWN"
                merged_by_suggested[suggested].add_row(row)
                merged_by_alert_ids[alert_ids].add_row(row)
                overall_merged.add_row(row)
        else:
            missing_merged.append(d)

    stem = f"{args.start}_to_{args.end}__PROFIT_ALERTS_ROLLUP"
    rows_csv = out_dir / f"{stem}_ROWS.csv"
    merged_csv = out_dir / f"{stem}_MERGED.csv"
    md_path = out_dir / f"{stem}.md"

    # Per-AlertId rows CSV
    rows_out: List[Dict[str, object]] = []
    for aid in sorted(by_alert.keys()):
        agg = by_alert[aid]
        d_hit, d_meas, d_unk, d_rate = hit_summary(agg.hit_decay)
        a_hit, a_meas, a_unk, a_rate = hit_summary(agg.hit_any_decay)
        h7_hit, h7_meas, h7_unk, h7_rate = hit_summary(agg.hit_7)
        a7_hit, a7_meas, a7_unk, a7_rate = hit_summary(agg.hit_any_7)
        h14_hit, h14_meas, h14_unk, h14_rate = hit_summary(agg.hit_14)
        a14_hit, a14_meas, a14_unk, a14_rate = hit_summary(agg.hit_any_14)

        t_mean = mean(agg.time_to_hit_steps) if agg.time_to_hit_steps else None
        t_med = median(agg.time_to_hit_steps) if agg.time_to_hit_steps else None
        t_p90 = p90(agg.time_to_hit_steps)
        ss_mean = mean(agg.implied_set_sizes) if agg.implied_set_sizes else None
        st_mean = mean(agg.strengths) if agg.strengths else None

        rows_out.append(
            {
                "alert_id": aid,
                "rows_total": agg.rows_total,
                "rows_candidates": agg.rows_candidates,
                "rows_promoters": agg.rows_promoters,
                "status_HIT": agg.status_counts.get("HIT", 0),
                "status_EXPIRED": agg.status_counts.get("EXPIRED", 0),
                "status_CENSORED": agg.status_counts.get("CENSORED", 0),
                "status_ACTIVE": agg.status_counts.get("ACTIVE", 0),
                "hit_decay_hits": d_hit,
                "hit_decay_measured": d_meas,
                "hit_decay_unknown": d_unk,
                "hit_decay_rate": d_rate,
                "hit_any_decay_hits": a_hit,
                "hit_any_decay_measured": a_meas,
                "hit_any_decay_unknown": a_unk,
                "hit_any_decay_rate": a_rate,
                "hit_7_hits": h7_hit,
                "hit_7_measured": h7_meas,
                "hit_7_unknown": h7_unk,
                "hit_7_rate": h7_rate,
                "hit_any_7_hits": a7_hit,
                "hit_any_7_measured": a7_meas,
                "hit_any_7_unknown": a7_unk,
                "hit_any_7_rate": a7_rate,
                "hit_14_hits": h14_hit,
                "hit_14_measured": h14_meas,
                "hit_14_unknown": h14_unk,
                "hit_14_rate": h14_rate,
                "hit_any_14_hits": a14_hit,
                "hit_any_14_measured": a14_meas,
                "hit_any_14_unknown": a14_unk,
                "hit_any_14_rate": a14_rate,
                "time_to_hit_mean_steps": fmt_float(t_mean),
                "time_to_hit_median_steps": fmt_float(t_med),
                "time_to_hit_p90_steps": fmt_int(t_p90),
                "implied_set_size_mean": fmt_float(ss_mean),
                "strength_mean": fmt_float(st_mean),
            }
        )

    rows_fields = [
        "alert_id",
        "rows_total",
        "rows_candidates",
        "rows_promoters",
        "status_HIT",
        "status_EXPIRED",
        "status_CENSORED",
        "status_ACTIVE",
        "hit_decay_hits",
        "hit_decay_measured",
        "hit_decay_unknown",
        "hit_decay_rate",
        "hit_any_decay_hits",
        "hit_any_decay_measured",
        "hit_any_decay_unknown",
        "hit_any_decay_rate",
        "hit_7_hits",
        "hit_7_measured",
        "hit_7_unknown",
        "hit_7_rate",
        "hit_any_7_hits",
        "hit_any_7_measured",
        "hit_any_7_unknown",
        "hit_any_7_rate",
        "hit_14_hits",
        "hit_14_measured",
        "hit_14_unknown",
        "hit_14_rate",
        "hit_any_14_hits",
        "hit_any_14_measured",
        "hit_any_14_unknown",
        "hit_any_14_rate",
        "time_to_hit_mean_steps",
        "time_to_hit_median_steps",
        "time_to_hit_p90_steps",
        "implied_set_size_mean",
        "strength_mean",
    ]
    write_csv(rows_csv, rows_fields, rows_out)

    # Merged CSV (two views: suggested_kinds + alert_ids)
    merged_out: List[Dict[str, object]] = []

    def emit_merged(view: str, key: str, agg: MergedAgg) -> None:
        d_hit, d_meas, d_unk, d_rate = hit_summary(agg.hit_any_decay)
        h7_hit, h7_meas, h7_unk, h7_rate = hit_summary(agg.hit_any_7)
        h14_hit, h14_meas, h14_unk, h14_rate = hit_summary(agg.hit_any_14)
        t_mean = mean(agg.time_to_hit_steps) if agg.time_to_hit_steps else None
        t_med = median(agg.time_to_hit_steps) if agg.time_to_hit_steps else None
        t_p90 = p90(agg.time_to_hit_steps)
        ss_mean = mean(agg.implied_set_sizes) if agg.implied_set_sizes else None
        merged_out.append(
            {
                "view": view,
                "key": key,
                "rows_total": agg.rows_total,
                "status_HIT": agg.status_counts.get("HIT", 0),
                "status_EXPIRED": agg.status_counts.get("EXPIRED", 0),
                "status_CENSORED": agg.status_counts.get("CENSORED", 0),
                "status_ACTIVE": agg.status_counts.get("ACTIVE", 0),
                "hit_any_decay_hits": d_hit,
                "hit_any_decay_measured": d_meas,
                "hit_any_decay_unknown": d_unk,
                "hit_any_decay_rate": d_rate,
                "hit_any_7_hits": h7_hit,
                "hit_any_7_measured": h7_meas,
                "hit_any_7_unknown": h7_unk,
                "hit_any_7_rate": h7_rate,
                "hit_any_14_hits": h14_hit,
                "hit_any_14_measured": h14_meas,
                "hit_any_14_unknown": h14_unk,
                "hit_any_14_rate": h14_rate,
                "time_to_hit_mean_steps": fmt_float(t_mean),
                "time_to_hit_median_steps": fmt_float(t_med),
                "time_to_hit_p90_steps": fmt_int(t_p90),
                "implied_set_size_mean": fmt_float(ss_mean),
            }
        )

    for k in sorted(merged_by_suggested.keys()):
        emit_merged("suggested_kinds", k, merged_by_suggested[k])
    for k in sorted(merged_by_alert_ids.keys()):
        emit_merged("alert_ids", k, merged_by_alert_ids[k])

    merged_fields = [
        "view",
        "key",
        "rows_total",
        "status_HIT",
        "status_EXPIRED",
        "status_CENSORED",
        "status_ACTIVE",
        "hit_any_decay_hits",
        "hit_any_decay_measured",
        "hit_any_decay_unknown",
        "hit_any_decay_rate",
        "hit_any_7_hits",
        "hit_any_7_measured",
        "hit_any_7_unknown",
        "hit_any_7_rate",
        "hit_any_14_hits",
        "hit_any_14_measured",
        "hit_any_14_unknown",
        "hit_any_14_rate",
        "time_to_hit_mean_steps",
        "time_to_hit_median_steps",
        "time_to_hit_p90_steps",
        "implied_set_size_mean",
    ]
    write_csv(merged_csv, merged_fields, merged_out)

    # Markdown
    lines: List[str] = []
    lines.append(f"# Profit Alerts Rollup — {args.start} → {args.end}")
    lines.append("")
    lines.append("Small, corpus-level summary of Profit Alerts evaluation outputs (row-level and merged play-sets).")
    lines.append("")
    lines.append("Inputs (per day):")
    lines.append("- `sharepacks/<D>/control_center/profit_alerts_eval.csv`")
    lines.append("- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`")
    lines.append("")
    lines.append("Outputs:")
    try:
        lines.append(f"- `{rows_csv.relative_to(ROOT)}`")
    except Exception:
        lines.append(f"- `{rows_csv}`")
    try:
        lines.append(f"- `{merged_csv.relative_to(ROOT)}`")
    except Exception:
        lines.append(f"- `{merged_csv}`")
    lines.append("")

    if missing_eval or missing_merged:
        lines.append("## Missing inputs (skipped days)")
        lines.append("")
        if missing_eval:
            lines.append(f"- Missing `profit_alerts_eval.csv`: {', '.join(missing_eval)}")
        if missing_merged:
            lines.append(f"- Missing `profit_alerts_eval_merged.csv`: {', '.join(missing_merged)}")
        lines.append("")

    lines.append("## Overall (row-level)")
    lines.append("")
    lines.append(f"- Total alert rows: **{overall_rows.rows_total}**")
    lines.append(f"- Candidate rows: **{overall_rows.rows_candidates}**")
    lines.append(f"- Promoter rows: **{overall_rows.rows_promoters}**")
    lines.append("")
    for st in ["HIT", "EXPIRED", "CENSORED", "ACTIVE"]:
        n = overall_rows.status_counts.get(st, 0)
        if n:
            lines.append(f"- Status {st}: **{n}/{overall_rows.rows_total}** ({pct(n, overall_rows.rows_total)})")
    lines.append("")

    lines.append("## Overall (merged play-sets)")
    lines.append("")
    lines.append(f"- Merged sets: **{overall_merged.rows_total}**")
    for st in ["HIT", "EXPIRED", "CENSORED", "ACTIVE"]:
        n = overall_merged.status_counts.get(st, 0)
        if n:
            lines.append(f"- Status {st}: **{n}/{overall_merged.rows_total}** ({pct(n, overall_merged.rows_total)})")
    lines.append("")

    # Candidate-only table, sorted by cross-variant decay hit-rate
    lines.append("## Candidate rows: hits within window (rollup by AlertId)")
    lines.append("")
    lines.append("| alert_id | rows | hit_decay | hit_any_decay | hit_any<=7 | hit_any<=14 |")
    lines.append("|---|---:|---:|---:|---:|---:|")

    sortable: List[Tuple[float, int, str]] = []
    for aid, agg in by_alert.items():
        denom = agg.hit_any_decay.measured
        r = (agg.hit_any_decay.hits / denom) if denom else -1.0
        sortable.append((r, agg.rows_candidates, aid))
    sortable.sort(reverse=True)
    for _, _, aid in sortable:
        agg = by_alert[aid]
        if agg.rows_candidates == 0:
            continue

        def _fmt(h: HitCounters) -> str:
            return f"{h.hits}/{h.measured}" if h.measured else "-"

        lines.append(
            f"| {aid} | {agg.rows_candidates} | {_fmt(agg.hit_decay)} | {_fmt(agg.hit_any_decay)} | {_fmt(agg.hit_any_7)} | {_fmt(agg.hit_any_14)} |"
        )
    lines.append("")

    lines.append("## Merged play-sets: by suggested kind")
    lines.append("")
    lines.append("| suggested_kinds | sets | hit_any_decay | hit_any<=7 | hit_any<=14 |")
    lines.append("|---|---:|---:|---:|---:|")
    for sk in sorted(merged_by_suggested.keys()):
        agg = merged_by_suggested[sk]
        lines.append(f"| {sk} | {agg.rows_total} | {agg.hit_any_decay.hits}/{agg.hit_any_decay.measured or 0} | {agg.hit_any_7.hits}/{agg.hit_any_7.measured or 0} | {agg.hit_any_14.hits}/{agg.hit_any_14.measured or 0} |")
    lines.append("")

    lines.append("## Notes")
    lines.append("")
    lines.append("- `hit_decay` is variant-faithful (Midday rows grade Midday-only; Evening rows grade Evening-only; Combined rows grade Midday→Evening→…).")
    lines.append("- `hit_any_*` is the cross-variant diagnostic lens (Midday alerts can be credited if the hit lands on Evening within the same time span, etc.).")
    lines.append("- Use `CENSORED` and `?` counts (in the CSVs) to see where results coverage is insufficient for the requested windows.")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote: {rows_csv}")
    print(f"Wrote: {merged_csv}")
    print(f"Wrote: {md_path}")


if __name__ == "__main__":
    main()

