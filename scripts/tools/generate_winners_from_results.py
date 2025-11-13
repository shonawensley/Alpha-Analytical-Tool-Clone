#!/usr/bin/env python3
"""Generate analyzer-style winners HTML for all states listed in a results file.

Usage:
    python3 scripts/tools/generate_winners_from_results.py \
        --results-file data/results/2025-06-22.txt \
        --out-dir reports/stable/winners_by_date/2025-06-22
"""
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import Dict, List

import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from modules.winner_report_full import write_winner_full_report

STATE_OVERRIDES: Dict[str, str] = {
    "connecticut": "Connecticut4",
    "delaware": "Delaware4",
    "florida": "Florida4",
    "georgia": "Georgia4",
    "idaho": "Idaho4",
    "illinois": "Illinois4",
    "indiana": "Indiana4",
    "iowa": "Iowa4",
    "kansas": "Kansas4",
    "kentucky": "Kentucky4",
    "maryland": "Maryland4",
    "michigan": "Michigan4",
    "minnesota": "Minnesota4",
    "mississippi": "Mississippi4",
    "missouri": "Missouri4",
    "newjersey": "NewJersey4",
    "newmexico": "NewMexico4",
    "newyork": "NewYork4",
    "northcarolina": "NorthCarolina4",
    "ohio": "Ohio4",
    "ontario": "OntarioCanada4",
    "pennsylvania": "Pennsylvania4",
    "puertorico": "PuertoRico4",
    "southcarolina": "SouthCarolina4",
    "tennessee": "Tennessee4",
    "texas": "Texas4",
    "virginia": "Virginia4",
    "washingtondc": "DistrictOfColumbia4",
    "washington": "Washington4",
    "westvirginia": "WestVirginia4",
    "wisconsin": "Wisconsin4",
}


def normalize_state(label: str) -> str | None:
    key = re.sub(r"[^A-Za-z]", "", label).lower()
    return STATE_OVERRIDES.get(key)


def parse_results(results_path: Path) -> Dict[str, List[str]]:
    winners: Dict[str, List[str]] = {}
    pattern = re.compile(r"\d{3}")
    for raw_line in results_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.lower().startswith("pick") or line.lower().startswith("midday"):
            continue
        nums = pattern.findall(line)
        if not nums:
            continue
        state_part = line
        for num in nums:
            state_part = state_part.replace(num, " ")
        state_part = re.sub(r"\s+", " ", state_part).strip(" -")
        state_code = normalize_state(state_part)
        if not state_code:
            continue
        winners[state_code] = nums[:2]
    return winners


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate winners HTML from a results file")
    parser.add_argument("--results-file", required=True)
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()

    results_path = Path(args.results_file)
    out_root = Path(args.out_dir)
    winners_map = parse_results(results_path)
    out_root.mkdir(parents=True, exist_ok=True)

    tables_root = Path("data/outputs/tables")
    for state, nums in winners_map.items():
        state_tables = tables_root / state
        if not state_tables.exists():
            continue
        state_dir = out_root / state
        os.makedirs(state_dir, exist_ok=True)
        for num in nums:
            if not num or not num.isdigit() or len(num) != 3:
                continue
            try:
                write_winner_full_report(state, num, out_dir=str(state_dir))
            except RuntimeError:
                continue


if __name__ == "__main__":
    main()
