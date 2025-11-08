#!/usr/bin/env python3
"""
Quick sanity checker for Digit-Reduction Analyzer V2 outputs.
Ensures newly-added scoring columns exist and basic ordering holds.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd


def _load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing expected analyzer file: {path}")
    return pd.read_csv(path)


def run_check(state: str) -> None:
    root = Path("data/outputs/analysis/digit_reduction") / state / "analyzer_v2"
    per_item = _load_csv(root / f"{state}_analyzer_v2_per_item.csv")
    top = _load_csv(root / f"{state}_analyzer_v2_top_candidates.csv")

    required_cols = {"final_linear", "final_prob", "lock_decision"}
    missing = sorted(col for col in required_cols if col not in per_item.columns)
    if missing:
        raise AssertionError(f"per_item missing columns: {', '.join(missing)}")

    if "score" in top.columns and not top["score"].is_monotonic_decreasing:
        raise AssertionError("top_candidates score must be sorted descending")

    summary = {
        "state": state,
        "rows": int(len(per_item)),
        "top_rows": int(len(top)),
        "locks": int((per_item["lock_decision"] == "lock").sum()),
        "holds": int((per_item["lock_decision"] == "hold").sum()),
    }
    print(json.dumps(summary, indent=2))


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: dr_quickcheck.py <StateLabel>")
        sys.exit(2)
    run_check(sys.argv[1])


if __name__ == "__main__":
    main()
