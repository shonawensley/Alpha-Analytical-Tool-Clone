#!/usr/bin/env python3
"""
Build Stable sharepacks for a given date.

Copies the lean Stable artifacts (scores/families/compound/metrics/spotlights/report)
and V-TRAC winners HTML into sharepacks/<DATE>/<STATE>/, and writes helper files
(compound_top5.txt, headers.txt, README.md).

Usage:
    python3 scripts/tools/build_stable_sharepacks.py \
        --date 2025-06-23 \
        --workbook Pick3StatsC4_2025-06-22.xlsm \
        --results-file data/results/2025-06-23.txt
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path
from typing import Iterable

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PATTERNS_ROOT = ROOT / "data" / "outputs" / "analysis" / "patterns"
WINNERS_SRC_ROOT = ROOT / "reports" / "stable" / "winners_by_date"
SHAREPACK_ROOT = ROOT / "sharepacks"

LABEL_OVERRIDES = {
    "NewJersey4": "New Jersey",
    "NewYork4": "New York",
    "NorthCarolina4": "North Carolina",
    "OntarioCanada4": "Ontario",
    "PuertoRico4": "Puerto Rico",
    "SouthCarolina4": "South Carolina",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Stable sharepack folders for a given date.")
    parser.add_argument("--date", required=True, help="Results date (e.g., 2025-06-23)")
    parser.add_argument("--states", nargs="*", help="Optional subset of states (default: autodetect from patterns dir)")
    parser.add_argument("--workbook", required=True, help="Workbook filename that fed the pipeline")
    parser.add_argument("--results-file", required=True, help="data/results/<DATE>.txt path used for Stable runs")
    parser.add_argument("--clobber", action="store_true", help="Remove any existing sharepacks/<date>/ directory first")
    return parser.parse_args()


def detect_states(states_arg: Iterable[str] | None) -> list[str]:
    if states_arg:
        return list(states_arg)
    if not PATTERNS_ROOT.exists():
        raise SystemExit(f"{PATTERNS_ROOT} does not exist")
    return sorted(p.name for p in PATTERNS_ROOT.iterdir() if p.is_dir())


def copy_stable_files(state: str, dest: Path) -> None:
    state_root = PATTERNS_ROOT / state
    stable_dir = dest / "stable"
    stable_dir.mkdir(parents=True, exist_ok=True)
    required = [
        f"{state}_stable_patterns_scores.csv",
        f"{state}_stable_patterns_families.csv",
        f"{state}_stable_patterns_compound.csv",
        f"{state}_metrics.json",
        f"{state}_winner_family_spotlight_raw.csv",
        f"{state}_winner_family_spotlight_families.csv",
        f"{state}_stable_patterns_report.html",
    ]
    for filename in required:
        src = state_root / filename
        if src.exists():
            shutil.copy2(src, stable_dir / filename)
        else:
            print(f"[WARN] Missing {src} for {state}")


def copy_winners_html(state: str, date: str, dest: Path) -> None:
    winners_src = WINNERS_SRC_ROOT / date / state
    winners_dest = dest / "winners"
    winners_dest.mkdir(parents=True, exist_ok=True)
    if not winners_src.exists():
        print(f"[WARN] Winners folder missing for {state} at {winners_src}")
        return
    for html_file in winners_src.glob("*.html"):
        shutil.copy2(html_file, winners_dest / html_file.name)


def write_compound_top5(state: str, dest: Path) -> None:
    compound_csv = PATTERNS_ROOT / state / f"{state}_stable_patterns_compound.csv"
    if not compound_csv.exists():
        print(f"[WARN] Compound CSV missing for {state}")
        return
    result = subprocess.run(
        [
            "python3",
            str(ROOT / "scripts" / "tools" / "compound_top5.py"),
            str(compound_csv),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    (dest / "compound_top5.txt").write_text(result.stdout.strip() + "\n", encoding="utf-8")


def write_headers(state: str, dest: Path) -> None:
    sections = [
        ("scores", f"{state}_stable_patterns_scores.csv"),
        ("families", f"{state}_stable_patterns_families.csv"),
        ("compound", f"{state}_stable_patterns_compound.csv"),
    ]
    parts: list[str] = []
    for label, filename in sections:
        path = PATTERNS_ROOT / state / filename
        if not path.exists():
            print(f"[WARN] Cannot list headers for missing {path}")
            continue
        df = pd.read_csv(path, nrows=0)
        columns = list(df.columns)
        parts.append(f"[{label}] {len(columns)} columns")
        parts.append(", ".join(columns))
        parts.append("")
    (dest / "headers.txt").write_text("\n".join(parts).strip() + "\n", encoding="utf-8")


def write_readme(state: str, date: str, workbook: str, results_file: str, dest: Path) -> None:
    label_extra = ""
    label_override = LABEL_OVERRIDES.get(state)
    if label_override:
        label_extra = f' --results-label "{label_override}"'
    content = f"""# Stable Sharepack — {state} ({date} results)

- Workbook: {workbook}
- Results file: {results_file}
- Stable command: python3 scripts/tools/run_stable_from_results.py \\
    --state {state} --results-file {results_file} --min-occ 1{label_extra}
- Winners HTML source: reports/stable/winners_by_date/{date}/{state}/

## Contents
- stable/ — lean Stable artifacts (scores, families, compound, metrics, winner spotlights, report)
- winners/ — analyzer-style V-TRAC winners HTML
- compound_top5.txt — Midday/Evening/Combined Top-5 snapshot
- headers.txt — column lists for scores/families/compound CSVs

## Notes
- Runs use draws through the workbook date ({workbook.split('_')[-1].replace('.xlsm','')}) to target {date} winners.
- See docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md for analysis write-ups.
"""
    (dest / "README.md").write_text(content, encoding="utf-8")


def build_sharepacks(date: str, states: list[str], workbook: str, results_file: str, clobber: bool) -> None:
    dest_root = SHAREPACK_ROOT / date
    if dest_root.exists() and clobber:
        shutil.rmtree(dest_root)
    dest_root.mkdir(parents=True, exist_ok=True)

    for state in states:
        state_dest = dest_root / state
        state_dest.mkdir(parents=True, exist_ok=True)
        copy_stable_files(state, state_dest)
        copy_winners_html(state, date, state_dest)
        write_compound_top5(state, state_dest)
        write_headers(state, state_dest)
        write_readme(state, date, workbook, results_file, state_dest)


def main() -> None:
    args = parse_args()
    states = detect_states(args.states)
    build_sharepacks(args.date, states, args.workbook, args.results_file, args.clobber)
    print(f"Sharepacks written under {SHAREPACK_ROOT / args.date}")


if __name__ == "__main__":
    main()
