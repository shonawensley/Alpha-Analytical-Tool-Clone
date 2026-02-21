#!/usr/bin/env python3
"""
Create a small, deterministic casebook package for manual auditing Profit Alerts.

This is evaluation/reporting-only:
  - It does not change analyzers.
  - It reads existing sharepack Brain-2 artifacts under sharepacks/<D>/control_center/.

Inputs (per day):
  - sharepacks/<D>/control_center/profit_alerts.csv
  - sharepacks/<D>/control_center/profit_alerts_eval.csv
  - sharepacks/<D>/control_center/profit_alerts_eval_merged.csv

Outputs (package):
  - docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_revamp__<A>_to_<B>__<STAMP>__<LABEL>/CASEBOOK.md
  - docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/profit_alerts_revamp__<A>_to_<B>__<STAMP>__<LABEL>/MANIFEST.md

Usage:
  python3 scripts/tools/create_profit_alerts_casebook.py --start 2025-12-30 --end 2026-01-09 --stamp 2026-02-21 --label revamp_2026-02-21
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
from collections import defaultdict
from dataclasses import dataclass
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


def clean_label(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw.replace(" ", "_")).strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid --label: {value!r} (must contain A-Z/a-z/0-9/_/-)")
    return cleaned[:60]


def safe_float(value: str) -> float:
    v = (value or "").strip()
    if not v:
        return 0.0
    try:
        return float(v)
    except Exception:
        return 0.0


def load_csv_rows(path: Path) -> Iterable[Dict[str, str]]:
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {k: (v or "") for k, v in row.items()}


def write_md(path: Path, lines: List[str]) -> None:
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


@dataclass(frozen=True)
class Case:
    kind: str
    results_date: str
    state_key: str
    variant: str
    alert_id: str
    row_num: str
    canonical: str
    suggested: str
    implied_set_size: str
    strength: float
    decay_draws: str
    badges: str
    status: str
    strict_hit: str
    hit_within_decay: str
    hit_any_within_decay: str
    hit_within_7: str
    hit_within_14: str
    hit_type: str
    hit_any_type: str


def row_tier(row: Dict[str, str]) -> int:
    # Lower is better.
    if (row.get("strict_hit") or "").strip().upper() == "Y":
        return 0
    if (row.get("hit_within_decay") or "").strip().upper() == "Y":
        return 1
    if (row.get("hit_any_within_decay") or "").strip().upper() == "Y":
        return 2
    if (row.get("hit_any_within_7") or "").strip().upper() == "Y":
        return 3
    if (row.get("hit_any_within_14") or "").strip().upper() == "Y":
        return 4
    if (row.get("status") or "").strip().upper() == "EXPIRED":
        return 8
    return 9


def pick_best(rows: List[Dict[str, str]], want_expired: bool) -> Optional[Dict[str, str]]:
    candidates = []
    for r in rows:
        if want_expired:
            if (r.get("status") or "").strip().upper() != "EXPIRED":
                continue
        candidates.append(r)
    if not candidates:
        return None

    # Deterministic: tier -> strength desc -> date/state/variant/row_num
    def key(r: Dict[str, str]) -> Tuple[int, float, str, str, str, int]:
        strength = safe_float(r.get("strength") or "")
        row_num = int(float(r.get("row_num") or "0") or 0)
        return (row_tier(r), -strength, r.get("results_date") or "", r.get("state_key") or "", r.get("variant") or "", row_num)

    return sorted(candidates, key=key)[0]


def to_case(kind: str, row: Dict[str, str]) -> Case:
    return Case(
        kind=kind,
        results_date=(row.get("results_date") or "").strip(),
        state_key=(row.get("state_key") or "").strip(),
        variant=(row.get("variant") or "").strip(),
        alert_id=(row.get("alert_id") or "").strip().upper(),
        row_num=(row.get("row_num") or "").strip(),
        canonical=(row.get("canonical") or "").strip(),
        suggested=(row.get("suggested") or "").strip(),
        implied_set_size=(row.get("implied_set_size") or "").strip(),
        strength=safe_float(row.get("strength") or ""),
        decay_draws=(row.get("decay_draws") or "").strip(),
        badges=(row.get("badges") or "").strip(),
        status=(row.get("status") or "").strip(),
        strict_hit=(row.get("strict_hit") or "").strip(),
        hit_within_decay=(row.get("hit_within_decay") or "").strip(),
        hit_any_within_decay=(row.get("hit_any_within_decay") or "").strip(),
        hit_within_7=(row.get("hit_within_7") or "").strip(),
        hit_within_14=(row.get("hit_within_14") or "").strip(),
        hit_type=(row.get("hit_type") or "").strip(),
        hit_any_type=(row.get("hit_any_type") or "").strip(),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Profit Alerts casebook package across a date range.")
    parser.add_argument("--start", required=True, help="Start results date D (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End results date D (YYYY-MM-DD)")
    parser.add_argument("--stamp", default=dt.date.today().isoformat(), help="Stamp used in output folder name")
    parser.add_argument("--label", default="", help="Optional label appended to output folder name (safe for reruns)")
    parser.add_argument("--sharepacks-dir", default=str(ROOT / "sharepacks"), help="Sharepacks root directory")
    parser.add_argument(
        "--packages-dir",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "PACKAGES"),
        help="Packages output directory",
    )
    args = parser.parse_args()

    label = clean_label(args.label)
    stamp = (args.stamp or "").strip()
    if not stamp:
        raise SystemExit("--stamp must be non-empty")

    sharepacks_root = Path(args.sharepacks_dir)
    packages_root = Path(args.packages_dir)
    packages_root.mkdir(parents=True, exist_ok=True)

    label_suffix = f"__{label}" if label else ""
    package_dir = packages_root / f"profit_alerts_revamp__{args.start}_to_{args.end}__{stamp}{label_suffix}"
    package_dir.mkdir(parents=True, exist_ok=True)

    dates = daterange(args.start, args.end)

    all_rows: List[Dict[str, str]] = []
    missing_eval: List[str] = []
    for d in dates:
        eval_path = sharepacks_root / d / "control_center" / "profit_alerts_eval.csv"
        if not eval_path.exists():
            missing_eval.append(d)
            continue
        all_rows.extend(load_csv_rows(eval_path))

    # Group by alert_id (keep PROMOTER vs CANDIDATE separate)
    by_alert_candidate: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    by_alert_promoter: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in all_rows:
        aid = (row.get("alert_id") or "").strip().upper() or "UNKNOWN"
        rt = (row.get("row_type") or "").strip().upper()
        if rt == "CANDIDATE":
            by_alert_candidate[aid].append(row)
        elif rt == "PROMOTER":
            by_alert_promoter[aid].append(row)

    picked: List[Case] = []

    for aid in sorted(by_alert_candidate.keys()):
        rows = by_alert_candidate[aid]
        best = pick_best(rows, want_expired=False)
        if best:
            picked.append(to_case("BEST", best))
        expired = pick_best(rows, want_expired=True)
        if expired and (not best or expired.get("row_num") != best.get("row_num") or expired.get("results_date") != best.get("results_date")):
            picked.append(to_case("EXPIRED", expired))

    for aid in sorted(by_alert_promoter.keys()):
        rows = by_alert_promoter[aid]
        best = pick_best(rows, want_expired=False)
        if best:
            picked.append(to_case("PROMOTER", best))

    # Write MANIFEST.md
    manifest: List[str] = []
    manifest.append(f"# Profit Alerts Revamp Casebook — {args.start} → {args.end}")
    manifest.append("")
    manifest.append(f"Stamp: `{stamp}`")
    if label:
        manifest.append(f"Label: `{label}`")
    manifest.append("")
    manifest.append("This package is a manual-audit companion to the Profit Alerts rollups/integrity reports.")
    manifest.append("")
    manifest.append("Primary inputs (per day):")
    manifest.append("- `sharepacks/<D>/control_center/profit_alerts.csv`")
    manifest.append("- `sharepacks/<D>/control_center/profit_alerts.md`")
    manifest.append("- `sharepacks/<D>/control_center/profit_alerts_eval.csv`")
    manifest.append("- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`")
    manifest.append("")
    manifest.append("Selected cases are listed in `CASEBOOK.md` with clickable file pointers.")
    manifest.append("")
    if missing_eval:
        manifest.append("Missing eval dates (skipped):")
        manifest.append("")
        for d in missing_eval:
            manifest.append(f"- `{d}`")
        manifest.append("")

    write_md(package_dir / "MANIFEST.md", manifest)

    # Write CASEBOOK.md
    casebook: List[str] = []
    casebook.append(f"# Profit Alerts Casebook — {args.start} → {args.end}")
    casebook.append("")
    casebook.append("How to use this casebook (fast path):")
    casebook.append("- Open the `profit_alerts_eval.csv` row referenced below (by `results_date` + `row_num`).")
    casebook.append("- Open the corresponding `profit_alerts.md` board and locate the same `AlertId`/`StateKey`/`Variant`/`Canonical` row.")
    casebook.append("- Cross-check against the winners digest + HTML under `sharepacks/<D>/<StateKey>/winners/...`.")
    casebook.append("- If you want to audit “why the alert fired”, open Stable scores and search for the canonical / evidence tags.")
    casebook.append("")
    casebook.append("## Cases")
    casebook.append("")

    def fmt_path(p: Path) -> str:
        try:
            return p.relative_to(ROOT).as_posix()
        except Exception:
            return p.as_posix()

    for idx, c in enumerate(picked, start=1):
        d = c.results_date
        state_key = c.state_key

        cc_dir = sharepacks_root / d / "control_center"
        eval_path = cc_dir / "profit_alerts_eval.csv"
        board_md = cc_dir / "profit_alerts.md"
        board_csv = cc_dir / "profit_alerts.csv"
        merged_path = cc_dir / "profit_alerts_eval_merged.csv"

        winners_digest = sharepacks_root / d / state_key / "winners" / state_key / "digest.md"
        winners_dir = winners_digest.parent
        stable_scores = sharepacks_root / d / state_key / "stable" / state_key / f"{state_key}_stable_patterns_scores.csv"
        json_tables = sharepacks_root / d / state_key / "json" / f"{state_key}_tables.json"

        casebook.append(f"### Case {idx} — {c.kind} — {c.alert_id} — {state_key} — {c.variant} — D=`{d}`")
        casebook.append("")
        casebook.append(f"- Status: `{c.status}` | Strength: `{c.strength:g}` | Suggested: `{c.suggested}` | Canonical: `{c.canonical or '-'}` | DecayDraws: `{c.decay_draws}` | Badges: `{c.badges}`")
        casebook.append(f"- Eval: strict_hit=`{c.strict_hit}` hit_decay=`{c.hit_within_decay}` hit_any_decay=`{c.hit_any_within_decay}` hit_any<=7=`{c.hit_within_7}` hit_any<=14=`{c.hit_within_14}`")
        if c.hit_type or c.hit_any_type:
            casebook.append(f"- Hit typing: hit_type=`{c.hit_type or '-'}` hit_any_type=`{c.hit_any_type or '-'}`")
        casebook.append("")
        casebook.append("Files:")
        casebook.append(f"- Eval row source: `{fmt_path(eval_path)}` (row_num={c.row_num})")
        casebook.append(f"- Profit board (md): `{fmt_path(board_md)}`")
        casebook.append(f"- Profit board (csv): `{fmt_path(board_csv)}`")
        casebook.append(f"- Eval merged sets: `{fmt_path(merged_path)}`")
        if winners_digest.exists():
            casebook.append(f"- Winners digest: `{fmt_path(winners_digest)}`")
            casebook.append(f"- Winners HTML/JSON dir: `{fmt_path(winners_dir)}`")
        else:
            casebook.append(f"- Winners digest: `{fmt_path(winners_digest)}` (missing)")
        casebook.append(f"- Stable scores: `{fmt_path(stable_scores)}`")
        casebook.append(f"- JSON tables: `{fmt_path(json_tables)}`")
        casebook.append("")

    write_md(package_dir / "CASEBOOK.md", casebook)

    print(f"Wrote: {package_dir / 'MANIFEST.md'}")
    print(f"Wrote: {package_dir / 'CASEBOOK.md'}")


if __name__ == "__main__":
    main()
