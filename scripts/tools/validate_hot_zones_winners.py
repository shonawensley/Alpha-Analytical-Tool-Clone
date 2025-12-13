"""
Validate that Hot Zones sharepack contains required outputs and that winners are present in top_lanes.

Usage:
  python3 scripts/tools/validate_hot_zones_winners.py --sharepack sharepacks/2025-06-21/OntarioCanada4/hot_zones/OntarioCanada4

Winners are loaded from sibling Stable metrics.json if available; otherwise pass --winners \"678,517\".
"""

import argparse
import json
from pathlib import Path

import pandas as pd


def canonical_of_literal(literal: str) -> str:
    return "".join(sorted(str(literal)))


def load_winners(date_dir: Path, state: str, winners_arg: str | None) -> dict:
    metrics_path = date_dir / state / "stable" / state / f"{state}_metrics.json"
    if metrics_path.exists():
        metrics = json.loads(metrics_path.read_text())
        winners = [str(w) for w in (metrics.get("winners") or [])]
        out = {}
        if len(winners) >= 1:
            out["Midday"] = winners[0]
        if len(winners) >= 2:
            out["Evening"] = winners[1]
        return out
    if winners_arg:
        parts = [p.strip() for p in winners_arg.split(",") if p.strip()]
        out = {}
        if len(parts) >= 1:
            out["Midday"] = parts[0]
        if len(parts) >= 2:
            out["Evening"] = parts[1]
        return out
    return {}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sharepack", required=True)
    ap.add_argument("--winners")
    args = ap.parse_args()

    sharepack = Path(args.sharepack)
    state = sharepack.parents[1].name if len(sharepack.parents) >= 2 else sharepack.name
    date_dir = sharepack.parents[2] if len(sharepack.parents) >= 3 else None

    required = [
        sharepack / f"{state}_hot_zones_per_lane.csv",
        sharepack / f"{state}_hot_zones_top_lanes.csv",
        sharepack / f"{state}_hot_zones_meta.json",
    ]
    missing_files = [str(p) for p in required if not p.exists()]

    print(f"Hot Zones validation for {state}")
    if missing_files:
        print("Missing required files:")
        for p in missing_files:
            print(f"- {p}")
        return

    top_lanes = pd.read_csv(required[1])
    top_lanes["rank"] = top_lanes["score_mean"].rank(method="min", ascending=False).astype(int)

    winners = load_winners(date_dir, state, args.winners) if date_dir else {}
    if not winners:
        print("No winners available to validate; pass --winners if needed.")
        return

    missing_winners = []
    for label, literal in winners.items():
        canon = canonical_of_literal(literal)
        mask = top_lanes["triad"].astype(str).isin([literal, canon])
        if not mask.any():
            missing_winners.append(f"{label} {literal} (canonical {canon})")

    if not missing_winners:
        print("OK: winners present in top_lanes")
    else:
        print("Missing winners in top_lanes:")
        for m in missing_winners:
            print(f"- {m}")


if __name__ == "__main__":
    main()

