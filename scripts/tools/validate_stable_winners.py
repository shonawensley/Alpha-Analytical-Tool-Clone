"""
Validate that Stable winners listed in metrics.json are present in the spotlight CSV.

Usage:
  PYTHONPATH=.:src python3 scripts/tools/validate_stable_winners.py --sharepack sharepacks/2025-06-21/OntarioCanada4/stable/OntarioCanada4

Checks:
  - Reads <STATE>_metrics.json for winners (list -> Midday/Evening by position).
  - Verifies each winner's canonical is present in <STATE>_winner_family_spotlight_raw.csv.
  - Reports any missing winners.
"""

import argparse
import json
from pathlib import Path

import pandas as pd


def canonical_of_literal(literal: str) -> str:
    return "".join(sorted(str(literal)))


def map_winners(metrics: dict) -> dict:
    winners = metrics.get("winners") or []
    winners = [str(w) for w in winners]
    mapping = {}
    if len(winners) >= 1:
        mapping["Midday"] = winners[0]
    if len(winners) >= 2:
        mapping["Evening"] = winners[1]
    return mapping


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--sharepack",
        required=True,
        help="Path to stable/<STATE>/<STATE> folder inside the sharepack",
    )
    args = p.parse_args()

    sharepack = Path(args.sharepack)
    state = sharepack.parent.name if sharepack.parent else sharepack.name

    metrics_path = sharepack / f"{sharepack.name}_metrics.json"
    spotlight_path = sharepack / f"{sharepack.name}_winner_family_spotlight_raw.csv"

    if not metrics_path.exists() or not spotlight_path.exists():
        raise SystemExit("Missing metrics or spotlight file in sharepack")

    metrics = json.loads(metrics_path.read_text())
    winners = map_winners(metrics)
    spotlight = pd.read_csv(spotlight_path)

    missing = []
    for label, literal in winners.items():
        canonical = canonical_of_literal(literal)
        mask = spotlight["Canonical"].astype(str) == canonical
        if not mask.any():
            missing.append({"label": label, "literal": literal, "canonical": canonical})

    print(f"Stable winner spotlight validation for {state}")
    if not missing:
        print("OK: all winners present in spotlight")
    else:
        print("Missing winners in spotlight:")
        for m in missing:
            print(f"- {m['label']}: literal {m['literal']} (canonical {m['canonical']})")


if __name__ == "__main__":
    main()
