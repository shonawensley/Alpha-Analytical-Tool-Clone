#!/usr/bin/env python3
"""
Create a small, deterministic integrity report for Profit Alerts evaluation artifacts.

This is evaluation/reporting-only:
  - It does not change analyzers.
  - It reads existing sharepack Brain-2 artifacts under sharepacks/<D>/control_center/.

Primary input (per day):
  - sharepacks/<D>/control_center/profit_alerts_eval.csv

Output (windowed):
  - docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PROFIT_ALERTS__INTEGRITY__<A>_to_<B>__<STAMP>__<LABEL>.md

Usage:
  python3 scripts/tools/create_profit_alerts_integrity_report.py --start 2025-12-30 --end 2026-01-09 --stamp 2026-02-21 --label revamp_2026-02-21
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[2]


EXPECTED_SET_SIZES: Dict[str, int] = {
    "STR8_8": 8,
    "STR8_4OF8": 4,
    "OVERLAY": 0,
    "SKIP": 0,
}

CANONICAL_OPTIONAL_ALERT_IDS = {"A09"}  # lane-set plays (canonical may be blank/"-")


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


def clean_label(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw.replace(" ", "_")).strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid --label: {value!r} (must contain A-Z/a-z/0-9/_/-)")
    return cleaned[:60]


def safe_int(value: str) -> Optional[int]:
    v = (value or "").strip()
    if not v:
        return None
    try:
        return int(float(v))
    except Exception:
        return None


def yn_bucket(value: str) -> str:
    v = (value or "").strip().upper()
    if v in {"Y", "N", "?"}:
        return v
    return ""


def stable_bucket(value: str) -> str:
    v = (value or "").strip().upper()
    if v in {"Y", "N", "?", "-"}:
        return v
    return ""


def is_canonical(value: str) -> bool:
    return bool(re.fullmatch(r"\d{3}", (value or "").strip()))


def perm_count_in_box(canonical: str) -> Optional[int]:
    c = (canonical or "").strip()
    if not is_canonical(c):
        return None
    uniq = len(set(c))
    if uniq == 1:
        return 1
    if uniq == 2:
        return 3
    return 6


def expected_implied_set_size(suggested: str, canonical: str) -> Optional[int]:
    k = (suggested or "").strip().upper()
    if not k:
        return None
    if k in {"OVERLAY", "SKIP"}:
        return 0
    if k == "STR8_8":
        return 8
    if k == "STR8_4OF8":
        return 4
    if k == "STR8_3":
        # "3-line straight": for triples it can legitimately be 1.
        pc = perm_count_in_box(canonical)
        return None if pc is None else min(3, pc)
    if k == "BOX":
        # Full perms: 6 for ABC, 3 for AAB, 1 for AAA.
        return perm_count_in_box(canonical)
    return EXPECTED_SET_SIZES.get(k)


def pct(n: int, d: int) -> str:
    return "0.0%" if d == 0 else f"{(100.0 * n / d):.1f}%"


def load_csv_rows(path: Path) -> Iterable[Dict[str, str]]:
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {k: (v or "") for k, v in row.items()}


@dataclass
class CandidateSanity:
    rows: int = 0
    canonical_required_rows: int = 0
    canonical_invalid: int = 0
    implied_size_missing: int = 0
    implied_size_mismatch: int = 0
    implied_size_mismatch_by_suggested: Counter = field(default_factory=Counter)
    implied_size_mismatch_by_alert: Counter = field(default_factory=Counter)
    evidence_ok: Counter = field(default_factory=Counter)
    stable_contains: Counter = field(default_factory=Counter)
    evidence_errors: Counter = field(default_factory=Counter)

    def add_row(self, row: Dict[str, str]) -> None:
        self.rows += 1

        suggested = (row.get("suggested") or "").strip()
        alert_id = (row.get("alert_id") or "").strip().upper() or "UNKNOWN"

        canonical = (row.get("canonical") or "").strip()
        if alert_id not in CANONICAL_OPTIONAL_ALERT_IDS:
            self.canonical_required_rows += 1
            if not is_canonical(canonical):
                self.canonical_invalid += 1

        implied_size = safe_int(row.get("implied_set_size") or "")
        if implied_size is None:
            self.implied_size_missing += 1
        else:
            expected = expected_implied_set_size(suggested, canonical)
            if expected is not None and implied_size != expected:
                self.implied_size_mismatch += 1
                self.implied_size_mismatch_by_suggested[suggested] += 1
                self.implied_size_mismatch_by_alert[alert_id] += 1

        eok = yn_bucket(row.get("evidence_ok") or "")
        if eok:
            self.evidence_ok[eok] += 1
        if eok == "N":
            err = (row.get("evidence_error") or "").strip() or "(missing evidence_error)"
            self.evidence_errors[err] += 1

        sc = stable_bucket(row.get("stable_contains_canonical") or "")
        if sc:
            self.stable_contains[sc] += 1


@dataclass
class IntegrityAgg:
    dates_total: int = 0
    dates_with_eval: int = 0
    missing_eval: List[str] = field(default_factory=list)

    rows_total: int = 0
    row_type_counts: Counter = field(default_factory=Counter)
    alert_id_counts: Counter = field(default_factory=Counter)
    suggested_counts: Counter = field(default_factory=Counter)

    evidence_ok: Counter = field(default_factory=Counter)
    evidence_errors: Counter = field(default_factory=Counter)

    candidate: CandidateSanity = field(default_factory=CandidateSanity)

    # Per-day quick stats
    per_day: List[Dict[str, object]] = field(default_factory=list)

    def add_day(self, d: str, rows: List[Dict[str, str]]) -> None:
        self.dates_with_eval += 1

        day_rows = len(rows)
        day_candidates = 0
        day_promoters = 0
        day_eok_y = 0
        day_eok_n = 0
        day_sc_y = 0
        day_sc_n = 0
        day_sc_meas = 0

        for row in rows:
            self.rows_total += 1
            rt = (row.get("row_type") or "").strip().upper() or "UNKNOWN"
            self.row_type_counts[rt] += 1
            aid = (row.get("alert_id") or "").strip().upper() or "UNKNOWN"
            self.alert_id_counts[aid] += 1
            sug = (row.get("suggested") or "").strip() or "UNKNOWN"
            self.suggested_counts[sug] += 1

            eok = yn_bucket(row.get("evidence_ok") or "")
            if eok:
                self.evidence_ok[eok] += 1
            if eok == "N":
                err = (row.get("evidence_error") or "").strip() or "(missing evidence_error)"
                self.evidence_errors[err] += 1
            if eok == "Y":
                day_eok_y += 1
            elif eok == "N":
                day_eok_n += 1

            if rt == "CANDIDATE":
                day_candidates += 1
                self.candidate.add_row(row)
                sc = stable_bucket(row.get("stable_contains_canonical") or "")
                if sc in {"Y", "N"}:
                    day_sc_meas += 1
                    if sc == "Y":
                        day_sc_y += 1
                    else:
                        day_sc_n += 1
            elif rt == "PROMOTER":
                day_promoters += 1

        self.per_day.append(
            {
                "date": d,
                "rows": day_rows,
                "candidates": day_candidates,
                "promoters": day_promoters,
                "evidence_ok_Y": day_eok_y,
                "evidence_ok_N": day_eok_n,
                "stable_contains_Y": day_sc_y,
                "stable_contains_N": day_sc_n,
                "stable_contains_measured": day_sc_meas,
            }
        )


def format_top(counter: Counter, limit: int = 10) -> List[Tuple[str, int]]:
    return [(k, int(v)) for k, v in counter.most_common(limit)]


def write_md(path: Path, lines: List[str]) -> None:
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Profit Alerts integrity report across a date range.")
    parser.add_argument("--start", required=True, help="Start results date D (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End results date D (YYYY-MM-DD)")
    parser.add_argument("--stamp", default=dt.date.today().isoformat(), help="Stamp used in output filename")
    parser.add_argument("--label", default="", help="Optional label appended to output filename (safe for reruns)")
    parser.add_argument("--out-dir", default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"))
    parser.add_argument("--sharepacks-dir", default=str(ROOT / "sharepacks"), help="Sharepacks root directory")
    args = parser.parse_args()

    label = clean_label(args.label)
    stamp = (args.stamp or "").strip()
    if not stamp:
        raise SystemExit("--stamp must be non-empty")

    dates = daterange(args.start, args.end)
    sharepacks_root = Path(args.sharepacks_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    agg = IntegrityAgg(dates_total=len(dates))

    for d in dates:
        eval_path = sharepacks_root / d / "control_center" / "profit_alerts_eval.csv"
        if not eval_path.exists():
            agg.missing_eval.append(d)
            continue
        rows = list(load_csv_rows(eval_path))
        agg.add_day(d, rows)

    label_suffix = f"__{label}" if label else ""
    out_path = out_dir / f"V0_3__PROFIT_ALERTS__INTEGRITY__{args.start}_to_{args.end}__{stamp}{label_suffix}.md"

    total_candidates = int(agg.row_type_counts.get("CANDIDATE", 0))
    total_promoters = int(agg.row_type_counts.get("PROMOTER", 0))
    eok_y = int(agg.evidence_ok.get("Y", 0))
    eok_n = int(agg.evidence_ok.get("N", 0))
    sc_y = int(agg.candidate.stable_contains.get("Y", 0))
    sc_n = int(agg.candidate.stable_contains.get("N", 0))
    sc_q = int(agg.candidate.stable_contains.get("?", 0))
    sc_dash = int(agg.candidate.stable_contains.get("-", 0))
    sc_meas = sc_y + sc_n
    sc_unmeasured = agg.candidate.rows - sc_meas

    lines: List[str] = []
    lines.append(f"# Profit Alerts Integrity — {args.start} → {args.end}")
    lines.append("")
    if label:
        lines.append(f"Label: `{label}`")
        lines.append("")
    lines.append("Purpose: summarize evaluation integrity signals (coverage + evidence wiring) before any tuning.")
    lines.append("")
    lines.append("## Coverage")
    lines.append("")
    lines.append(f"- Dates in range: **{agg.dates_total}**")
    lines.append(f"- Dates with `profit_alerts_eval.csv`: **{agg.dates_with_eval}**")
    if agg.missing_eval:
        lines.append(f"- Missing eval dates: **{len(agg.missing_eval)}**")
        lines.append("")
        lines.append("Missing dates:")
        lines.append("")
        for d in agg.missing_eval:
            lines.append(f"- `{d}`")
    else:
        lines.append("- Missing eval dates: **0**")
    lines.append("")
    lines.append("## Totals")
    lines.append("")
    lines.append(f"- Total rows: **{agg.rows_total}**")
    lines.append(f"- Candidate rows: **{total_candidates}**")
    lines.append(f"- Promoter rows: **{total_promoters}**")
    lines.append("")
    lines.append(f"- Evidence OK (all rows): Y={eok_y}, N={eok_n} (Y rate: {pct(eok_y, eok_y + eok_n)})")
    lines.append(
        f"- Stable contains canonical (candidates): Y={sc_y}, N={sc_n}, ?={sc_q}, -={sc_dash} (measured: {sc_meas}/{agg.candidate.rows}, Y rate: {pct(sc_y, sc_meas)})"
    )
    lines.append(
        f"- Candidate canonical invalid (canonical-required alerts only): **{agg.candidate.canonical_invalid}/{agg.candidate.canonical_required_rows}** ({pct(agg.candidate.canonical_invalid, agg.candidate.canonical_required_rows)})"
    )
    lines.append(f"- Candidate implied_set_size missing: **{agg.candidate.implied_size_missing}/{agg.candidate.rows}** ({pct(agg.candidate.implied_size_missing, agg.candidate.rows)})")
    lines.append(
        f"- Candidate implied_set_size mismatches (vs expected for suggested kind): **{agg.candidate.implied_size_mismatch}/{agg.candidate.rows}** ({pct(agg.candidate.implied_size_mismatch, agg.candidate.rows)})"
    )
    lines.append("")

    lines.append("## Per-day quick stats")
    lines.append("")
    lines.append("| date | rows | candidates | promoters | evidence_ok_Y | evidence_ok_N | stable_contains_Y | stable_contains_N |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for row in agg.per_day:
        lines.append(
            f"| {row['date']} | {row['rows']} | {row['candidates']} | {row['promoters']} | {row['evidence_ok_Y']} | {row['evidence_ok_N']} | {row['stable_contains_Y']} | {row['stable_contains_N']} |"
        )
    lines.append("")

    lines.append("## Evidence errors (top)")
    lines.append("")
    if not agg.evidence_errors:
        lines.append("- None.")
    else:
        lines.append("| evidence_error | count |")
        lines.append("|---|---:|")
        for msg, count in format_top(agg.evidence_errors, limit=12):
            safe_msg = msg.replace("|", "\\|")
            lines.append(f"| {safe_msg} | {count} |")
    lines.append("")

    lines.append("## Candidate set-size mismatches (by suggested kind)")
    lines.append("")
    if not agg.candidate.implied_size_mismatch_by_suggested:
        lines.append("- None.")
    else:
        lines.append("| suggested | mismatches |")
        lines.append("|---|---:|")
        for suggested, count in format_top(agg.candidate.implied_size_mismatch_by_suggested, limit=20):
            lines.append(f"| {suggested} | {count} |")
    lines.append("")

    lines.append("## Stable containment misses (by alert_id)")
    lines.append("")
    by_alert_sc_y: Counter = Counter()
    by_alert_sc_n: Counter = Counter()

    # Build per-alert stable_contains counts by reusing per-day read (lightweight second pass).
    for row in agg.per_day:
        d = str(row["date"])
        eval_path = Path(args.sharepacks_dir) / d / "control_center" / "profit_alerts_eval.csv"
        if not eval_path.exists():
            continue
        for r in load_csv_rows(eval_path):
            if (r.get("row_type") or "").strip().upper() != "CANDIDATE":
                continue
            aid = (r.get("alert_id") or "").strip().upper() or "UNKNOWN"
            sc = stable_bucket(r.get("stable_contains_canonical") or "")
            if sc == "Y":
                by_alert_sc_y[aid] += 1
            elif sc == "N":
                by_alert_sc_n[aid] += 1

    lines.append("| alert_id | stable_contains_Y | stable_contains_N | N_rate |")
    lines.append("|---|---:|---:|---:|")
    for aid in sorted(set(by_alert_sc_y.keys()) | set(by_alert_sc_n.keys())):
        y = int(by_alert_sc_y.get(aid, 0))
        n = int(by_alert_sc_n.get(aid, 0))
        denom = y + n
        n_rate = "" if denom == 0 else f"{(100.0 * n / denom):.1f}%"
        lines.append(f"| {aid} | {y} | {n} | {n_rate} |")

    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- `evidence_ok=N` means the evaluator could not load the required evidence row(s) to grade the alert row; inspect `evidence_error` for the reason.")
    lines.append("- `stable_contains_canonical=N` means the canonical 3-digit did not appear in Stable’s exported scored rows for that state/day/variant; this can be legitimate (signal disagreement) or a wiring issue.")
    lines.append("- `implied_set_size` is sanity-checked against suggested kinds:")
    lines.append("  - BOX expects full perms (6/3/1 depending on unique digits in canonical).")
    lines.append("  - STR8_3 expects min(3, perms) (so triples can legitimately be 1).")
    lines.append("  - STR8_8 expects 8, STR8_4of8 expects 4, OVERLAY/SKIP expect 0.")

    write_md(out_path, lines)
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
