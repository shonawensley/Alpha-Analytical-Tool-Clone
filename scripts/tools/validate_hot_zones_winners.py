"""
Validate that Hot Zones sharepack contains required outputs and that winners are present in top_lanes.

Usage:
  python3 scripts/tools/validate_hot_zones_winners.py --sharepack sharepacks/2025-06-21/OntarioCanada4/hot_zones/OntarioCanada4

Winners are loaded from sibling Stable metrics.json if available; otherwise pass --winners \"678,517\".
"""

import argparse
import json
import re
from pathlib import Path

import pandas as pd


def canonical_of_literal(literal: str) -> str:
    return "".join(sorted(str(literal)))


def normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def _results_label_from_state(state_name: str) -> str:
    base = re.sub(r"\d+$", "", state_name or "")
    if base.lower().startswith("ontariocanada"):
        return "Ontario"
    words = re.findall(r"[A-Z][a-z]*|[A-Z]+(?![a-z])", base) or [base]
    return " ".join(words).strip()


def load_winners_from_results(results_date: str, state_name: str) -> dict | None:
    results_path = Path("data/results") / f"{results_date}.txt"
    if not results_path.exists():
        return None
    target = _results_label_from_state(state_name)

    def norm(label: str) -> str:
        return re.sub(r"[^a-z0-9]+", "", (label or "").lower())

    def first_tri(token: str) -> str | None:
        if not token:
            return None
        direct = re.findall(r"\d{3}", token)
        if direct:
            return direct[0]
        digits = "".join(ch for ch in str(token) if ch.isdigit())
        if len(digits) < 3:
            return None
        if len(digits) == 3:
            return digits
        if len(digits) % 3 != 0:
            return None
        return digits[:3]

    for raw in results_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line:
            continue
        header = line.lower()
        if header.startswith(("state", "pick", "midday", "evening")):
            continue
        parts = line.split("\t")
        if not parts:
            continue
        label = parts[0].strip()
        if norm(label) != norm(target):
            continue
        midday = first_tri(parts[1]) if len(parts) >= 2 else None
        evening = first_tri(parts[2]) if len(parts) >= 3 else None
        mapping: dict[str, str] = {}
        if midday:
            mapping["Midday"] = midday
        if evening:
            mapping["Evening"] = evening
        return mapping or None
    return None


def load_winners(date_dir: Path, state: str, winners_arg: str | None) -> dict:
    results_winners = load_winners_from_results(date_dir.name, state)
    if results_winners:
        return results_winners

    metrics_path = date_dir / state / "stable" / state / f"{state}_metrics.json"
    if metrics_path.exists():
        metrics = json.loads(metrics_path.read_text())
        winners = [normalize_pick3_literal(w) for w in (metrics.get("winners") or [])]
        winners = [w for w in winners if w]
        out = {}
        if len(winners) >= 1:
            out["Midday"] = winners[0]
        if len(winners) >= 2:
            out["Evening"] = winners[1]
        return out
    if winners_arg:
        parts = [p.strip() for p in winners_arg.split(",") if p.strip()]
        parts = [normalize_pick3_literal(p) for p in parts]
        parts = [p for p in parts if p]
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

    top_lanes = pd.read_csv(required[1], dtype={"triad": str})
    top_lanes["triad"] = top_lanes["triad"].map(normalize_pick3_literal)
    top_lanes["rank"] = top_lanes["score_mean"].rank(method="min", ascending=False).astype(int)

    winners = load_winners(date_dir, state, args.winners) if date_dir else {}
    if not winners:
        print("No winners available to validate; pass --winners if needed.")
        return

    missing_winners = []
    for label, literal in winners.items():
        literal = normalize_pick3_literal(literal)
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
