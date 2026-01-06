#!/usr/bin/env python3
"""
Create a per-day cross-state synthesis stub for Master Validation.

This is intentionally "analysis layer" only:
- reads already-filled per-state run reports via `RUNS/corpus_summary.csv`
- writes `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__DAY_SYNTHESIS.md`

It does NOT rebuild sharepacks or run analyzers.
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from datetime import date as _date
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class StateDay:
    state: str
    env_verdict: str | None
    pack_midday: str | None
    pack_evening: str | None
    midday_missing: bool
    evening_missing: bool


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        return list(csv.DictReader(f))


def _iter_state_days(*, date: str, rows: list[dict[str, str]]) -> Iterable[StateDay]:
    by_state: dict[str, dict[str, dict[str, str]]] = {}
    for r in rows:
        if r.get("date") != date:
            continue
        state = r.get("state", "")
        period = r.get("period", "")
        by_state.setdefault(state, {})[period] = r

    for state, periods in sorted(by_state.items()):
        if state in {"CONTROL_CENTER", "DAY_SYNTHESIS"}:
            continue

        midday = periods.get("Midday", {})
        evening = periods.get("Evening", {})

        yield StateDay(
            state=state,
            env_verdict=(midday.get("env_verdict") or evening.get("env_verdict") or None),
            pack_midday=midday.get("pack") or None,
            pack_evening=evening.get("pack") or None,
            midday_missing=(midday.get("winner_missing") == "1"),
            evening_missing=(evening.get("winner_missing") == "1"),
        )


def _bucket_verdict(verdict: str | None) -> str:
    if not verdict:
        return "Unknown"
    v = verdict.lower()
    if "strong" in v:
        return "Strong"
    if "support" in v:
        return "Support"
    if "weak" in v or "noisy" in v:
        return "Weak/Noisy"
    return "Mixed/Other"


def _pack_short(line: str | None, *, label: str) -> str:
    if not line:
        return f"{label}: N/A"
    m = re.search(r"winner\s+(\d{3})", line, re.IGNORECASE)
    winner = m.group(1) if m else None
    box = None
    m2 = re.search(r"box\s+`(\d{3})`", line)
    if m2:
        box = m2.group(1)
    if winner and box:
        return f"{label} {winner} → BOX `{box}`"
    return f"{label}: {line}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="Results/sharepack date D (YYYY-MM-DD)")
    ap.add_argument(
        "--out",
        help="Output Markdown path (default: RUNS/<D>__DAY_SYNTHESIS.md)",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing synthesis file (default: refuse to overwrite).",
    )
    args = ap.parse_args()

    d = parse_iso_date(args.date)
    results_date = d.isoformat()

    runs_dir = _runs_dir()
    corpus_csv = runs_dir / "corpus_summary.csv"
    if not corpus_csv.exists():
        raise SystemExit(f"Missing corpus summary CSV: {corpus_csv} (run export_master_validation_corpus.py first)")

    rows = _read_csv_rows(corpus_csv)
    states = list(_iter_state_days(date=results_date, rows=rows))
    if not states:
        raise SystemExit(f"No corpus rows found for D={results_date}.")

    # Provenance from sharepack Control Center meta (preferred for H)
    meta_path = REPO_ROOT / "sharepacks" / results_date / "control_center" / "meta.json"
    history_date = "unknown"
    if meta_path.exists():
        import json

        meta = json.loads(meta_path.read_text(encoding="utf-8", errors="replace"))
        history_date = meta.get("history_date") or history_date

    default_out = runs_dir / f"{results_date}__DAY_SYNTHESIS.md"
    out_path = Path(args.out) if args.out else default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.force:
        raise SystemExit(
            f"Day synthesis already exists: {out_path}. Refusing to overwrite. Use --force to overwrite."
        )

    buckets: dict[str, list[str]] = {"Strong": [], "Support": [], "Mixed/Other": [], "Weak/Noisy": [], "Unknown": []}
    for sd in states:
        buckets[_bucket_verdict(sd.env_verdict)].append(sd.state)

    lines: list[str] = []
    lines.append(f"# Day Synthesis — D={results_date} (H={history_date})")
    lines.append("")
    lines.append("Scope")
    lines.append(f"- Results date (D): `{results_date}`")
    lines.append(f"- History workbook date (H): `{history_date}` (usually D-1)")
    lines.append(f"- States ({len(states)}): " + ", ".join(sd.state for sd in states))
    lines.append("- Outcomes: Midday + Evening (Combined is a lens only; used for cross-variant structure and tags)")
    lines.append("")
    lines.append("Sources")
    lines.append(f"- Sharepack day root: `sharepacks/{results_date}/README.md`")
    lines.append(f"- Control Center portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/{results_date}__CONTROL_CENTER.md`")
    lines.append(f"- Run reports (per-state): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/{results_date}__<STATE>.md`")
    lines.append(f"- Results file: `data/results/{results_date}.txt`")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append("- Day-level synthesis is intentionally conservative (avoid overfitting).")
    lines.append("- Use this doc to classify environment types and log cross-state patterns you notice during review.")
    lines.append("")
    lines.append("## Verdict Distribution (Part A “Environment verdict”, distilled)")
    lines.append("")
    for key in ["Strong", "Support", "Mixed/Other", "Weak/Noisy", "Unknown"]:
        if not buckets[key]:
            continue
        lines.append(f"- {key}: " + ", ".join(f"`{s}`" for s in buckets[key]))
    lines.append("")
    lines.append("## Pack Translation Snapshot (Part 5 “Pack vs winners”, quick map)")
    lines.append("")
    for sd in states:
        mid = _pack_short(sd.pack_midday, label="Midday")
        eve = _pack_short(sd.pack_evening, label="Evening")
        lines.append(f"- `{sd.state}`: {mid}; {eve}.")
    lines.append("")
    lines.append("## Fix-later / anomalies (day-specific)")
    lines.append("")
    lines.append("- (Add anything that looks repeatable or suspicious, with links to the state run reports.)")
    lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
