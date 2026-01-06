#!/usr/bin/env python3
"""
Run the Stable Pattern Extractor for a state and automatically supply winners
based on a data/results/<date>.txt file.

Usage:
    python3 scripts/tools/run_stable_from_results.py --state Connecticut4 --results-file data/results/2025-06-24.txt
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utils import path_handler as ph
from src.core.stable_pattern_extractor import run_stable_pattern_extraction


def _detect_winners(results_file: Path, label: str) -> List[str]:
    label = label.strip()
    label_lower = label.lower()
    winners: List[str] = []
    if not results_file.exists():
        raise FileNotFoundError(results_file)

    def _triads_from_token(token: str) -> List[str]:
        if not token:
            return []
        direct = re.findall(r"\d{3}", token)
        if direct:
            return direct
        digits = "".join(ch for ch in str(token) if ch.isdigit())
        if len(digits) < 3 or len(digits) % 3 != 0:
            return []
        return [digits[i : i + 3] for i in range(0, len(digits), 3)]

    for raw_line in results_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or not line.lower().startswith(label_lower):
            continue
        remainder = line[len(label):].strip()
        remainder = remainder.replace("\t", " ")
        parts = [p for p in remainder.split(" ") if p]
        for part in parts:
            winners.extend(_triads_from_token(part))
        break
    return winners[:2]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Stable extractor with winners pulled from a results file.")
    parser.add_argument("--state", required=True, help="State identifier (e.g., Connecticut4)")
    parser.add_argument(
        "--results-file",
        required=True,
        help="Path to data/results/<date>.txt containing the Midday/Evening winners.",
    )
    parser.add_argument(
        "--results-label",
        help="Label inside the results file (default: state name without trailing digits).",
    )
    parser.add_argument(
        "--min-occ",
        type=int,
        default=3,
        help="Minimum occurrences per canonical before it is kept (default: 3).",
    )
    parser.add_argument(
        "--write-bundle",
        action="store_true",
        help="Whether to write a training bundle for this run.",
    )
    parser.add_argument(
        "--bundle-stamp",
        help="Optional training bundle stamp (defaults to timestamp when writing).",
    )
    args = parser.parse_args()

    state = args.state.strip()
    if not state:
        raise SystemExit("State must be provided.")

    label = args.results_label.strip() if args.results_label else state.rstrip("0123456789")
    winners = _detect_winners(Path(args.results_file), label)
    if not winners:
        raise SystemExit(f"No winners found for label '{label}' in {args.results_file}")

    tables_dir = ph.get_state_tables_dir(state)
    out_dir = ph.get_analysis_dir("patterns", state)

    df, html_path, csv_path = run_stable_pattern_extraction(
        state=state,
        tables_path=tables_dir,
        out_path=out_dir,
        min_occ=args.min_occ,
        winners=winners,
        bundle_stamp=args.bundle_stamp,
        write_bundle=args.write_bundle,
    )

    print(f"Stable run complete for {state}")
    print(f"Patterns: {len(df)}")
    print(f"HTML: {html_path}")
    print(f"CSV: {csv_path}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(__doc__)
        raise SystemExit(1)
    main()
