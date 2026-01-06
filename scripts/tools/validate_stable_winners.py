"""
Validate that Stable winner spotlight artifacts are coherent with metrics.json.

Usage:
  PYTHONPATH=.:src python3 scripts/tools/validate_stable_winners.py --sharepack sharepacks/2025-06-21/OntarioCanada4/stable/OntarioCanada4

Checks:
  - Reads <STATE>_metrics.json for winners (list -> Midday/Evening by position).
  - Validates the spotlight file exists when winners exist.
  - Validates the winner-family IDs from metrics appear in the spotlight (artifact integrity).
  - Only requires an exact-canonical row when metrics indicates an exact hit (analytic outcome).
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


def map_winners(metrics: dict) -> dict:
    winners = metrics.get("winners") or []
    winners = [normalize_pick3_literal(w) for w in winners]
    winners = [w for w in winners if w]
    mapping = {}
    if len(winners) >= 1:
        mapping["Midday"] = winners[0]
    if len(winners) >= 2:
        mapping["Evening"] = winners[1]
    return mapping


def map_winner_family_ids(metrics: dict, winners: dict) -> dict:
    fam_ids = metrics.get("winner_family_ids") or []
    mapping = {}
    labels = list(winners.keys())
    if len(fam_ids) == 1 and len(labels) == 1:
        mapping[labels[0]] = str(fam_ids[0])
        return mapping
    if len(fam_ids) >= 1 and "Midday" in winners:
        mapping["Midday"] = str(fam_ids[0])
    if len(fam_ids) >= 2 and "Evening" in winners:
        mapping["Evening"] = str(fam_ids[1])
    return mapping


def truthy(series: pd.Series) -> pd.Series:
    if series.dtype == bool:
        return series
    if pd.api.types.is_numeric_dtype(series):
        return series.fillna(0).astype(int).astype(bool)
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes", "y"})


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--sharepack",
        required=True,
        help="Path to stable/<STATE>/<STATE> folder inside the sharepack",
    )
    args = p.parse_args()

    sharepack = Path(args.sharepack)
    state = sharepack.name

    metrics_path = sharepack / f"{sharepack.name}_metrics.json"
    spotlight_path = sharepack / f"{sharepack.name}_winner_family_spotlight_raw.csv"

    if not metrics_path.exists():
        raise SystemExit(f"Missing metrics file in sharepack: {metrics_path}")

    metrics = json.loads(metrics_path.read_text())
    results_date = sharepack.parents[2].name if len(sharepack.parents) >= 3 else ""
    winners = load_winners_from_results(results_date, state) or map_winners(metrics)
    if not winners:
        print(f"Stable winner spotlight validation for {state}")
        print("No winners in metrics.json; skipping (expected when results are missing for this state/day).")
        return

    if not spotlight_path.exists():
        raise SystemExit(f"Missing spotlight file in sharepack: {spotlight_path}")

    spotlight = pd.read_csv(
        spotlight_path,
        dtype={
            "Canonical": str,
            "winner_literal_midday": str,
            "winner_literal_evening": str,
        },
    )
    spotlight["Canonical"] = spotlight["Canonical"].astype(str).str.strip()
    for col in ("winner_literal_midday", "winner_literal_evening"):
        if col in spotlight.columns:
            spotlight[col] = spotlight[col].map(normalize_pick3_literal)

    fam_ids = map_winner_family_ids(metrics, winners)
    hits = metrics.get("winner_hits") or {}

    failures: list[str] = []
    notes: list[str] = []

    # Winner literals recorded inside spotlight (informational, but useful to detect drift).
    for label, col in (("Midday", "winner_literal_midday"), ("Evening", "winner_literal_evening")):
        if label in winners and col in spotlight.columns:
            vals = [v for v in spotlight[col].tolist() if str(v).strip()]
            if vals and vals[0] != winners[label]:
                notes.append(f"spotlight.{col}={vals[0]} != metrics.winners[{label}]={winners[label]}")

    for label, literal in winners.items():
        literal = normalize_pick3_literal(literal)
        if not literal:
            continue

        expected_family_id = fam_ids.get(label)
        if expected_family_id and "family_id" in spotlight.columns:
            fam_present = (spotlight["family_id"].astype(str) == expected_family_id).any()
            if not fam_present:
                failures.append(f"{label}: missing family_id {expected_family_id} in spotlight")

        canonical = canonical_of_literal(literal)
        fallback_key = literal.lstrip("0") or "0"
        hit = hits.get(literal) or hits.get(fallback_key) or {}
        expects_exact = bool(hit.get("exact_boxed") or hit.get("exact_straight"))

        canon_rows = spotlight[spotlight["Canonical"] == canonical]
        if expects_exact:
            if canon_rows.empty:
                failures.append(f"{label}: expected exact hit but Canonical={canonical} row missing in spotlight")
            else:
                if hit.get("exact_boxed") and "is_exact_boxed" in canon_rows:
                    if not truthy(canon_rows["is_exact_boxed"]).any():
                        failures.append(f"{label}: metrics says exact_boxed but spotlight rows are not exact_boxed for Canonical={canonical}")
                if hit.get("exact_straight") and "is_exact_straight" in canon_rows:
                    if not truthy(canon_rows["is_exact_straight"]).any():
                        failures.append(
                            f"{label}: metrics says exact_straight but spotlight rows are not exact_straight for Canonical={canonical}"
                        )
        else:
            if canon_rows.empty:
                notes.append(f"{label}: no exact Stable hit (Canonical={canonical} not present) — analytic outcome, not a workflow failure")

    print(f"Stable winner spotlight validation for {state}")
    if not failures:
        print("OK: spotlight artifacts are coherent with metrics")
        for note in notes:
            print(f"NOTE: {note}")
    else:
        print("FAIL:")
        for msg in failures:
            print(f"- {msg}")
        for note in notes:
            print(f"NOTE: {note}")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
