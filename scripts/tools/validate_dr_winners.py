"""
Validate that Digit Reduction winners appear in the winner_flags/hits for a sharepack.

Usage:
  PYTHONPATH=.:src python3 scripts/tools/validate_dr_winners.py --sharepack sharepacks/2025-06-21/OntarioCanada4/digit_reduction/OntarioCanada4

Checks:
  - Detects latest stamp in analyzer_v2/winners.
  - For Midday/Evening/Combined, confirms that:
      - `*_winner_stamp.json` exists (SSOT for winner + any vs final semantics)
      - winner_flags/hits files exist and have row counts consistent with stamp `counts.items_total`
      - aggregate flag sums match the stamp counts (exact_any/vtrac_any/... and exact_final/vtrac_final/...)
  - IMPORTANT: do NOT treat `winner_hits.csv.final_value` as “the winner”; final_value is per-item output.
"""

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd


def detect_latest_stamp(winners_dir: Path) -> str:
    stamps = sorted({p.name.split("_")[0] for p in winners_dir.glob("*_winner_stamp.json")})
    if not stamps:
        stamps = sorted({p.name.split("_")[0] for p in winners_dir.glob("*_winner_flags.csv")})
    if not stamps:
        raise SystemExit("No winner_flags found in winners/")
    return stamps[-1]


def canonical_of_literal(literal: str) -> str:
    return "".join(sorted(str(literal)))


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _norm_state(label: str) -> str:
    return "".join(ch for ch in (label or "").lower() if ch.isalpha())


def _normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def _parse_results(results_file: Path) -> Dict[str, Dict[str, str]]:
    """Parse data/results/<D>.txt into {norm_state: {"Midday": "123", "Evening": "456"}}."""
    winners: Dict[str, Dict[str, str]] = {}
    if not results_file.exists():
        return winners
    with results_file.open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh, delimiter="\t")
        for row in reader:
            if not row:
                continue
            state_raw = (row[0] or "").strip()
            if not state_raw or state_raw.lower() == "state":
                continue
            if state_raw.lower() in {"midday", "evening"}:
                continue
            if len(row) < 3:
                continue
            midday = _normalize_pick3_literal((row[1] or "").strip())
            evening = _normalize_pick3_literal((row[2] or "").strip())
            entry: Dict[str, str] = {}
            if len(midday) == 3 and midday.isdigit():
                entry["Midday"] = midday
            if len(evening) == 3 and evening.isdigit():
                entry["Evening"] = evening
            if entry:
                winners[_norm_state(state_raw)] = entry
    return winners


def _load_aux_state_label(sharepack: Path) -> str | None:
    """
    Try to load the Aux state label (matches results file labels) from the sibling Aux sharepack summary.
    """
    try:
        state_dir = sharepack.parent.parent
        aux_summary = state_dir / "aux" / sharepack.name / "summary.json"
        if not aux_summary.exists():
            return None
        payload = json.loads(aux_summary.read_text(encoding="utf-8", errors="replace"))
        meta = (payload.get("draw_sources") or {}).get("snapshot_meta") or {}
        label = (meta.get("aux_state_label") or "").strip()
        return label or None
    except Exception:
        return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sharepack", required=True, help="Path to digit_reduction/<STATE>/<STATE>")
    ap.add_argument("--warn-only", action="store_true", help="Print problems but do not exit non-zero")
    args = ap.parse_args()

    sharepack = Path(args.sharepack)
    state = sharepack.name
    winners_dir = sharepack / "analyzer_v2" / "winners"
    date_dir = sharepack.parents[2] if len(sharepack.parents) >= 3 else None
    results_date = date_dir.name if date_dir else None
    results_file = (Path(__file__).resolve().parents[2] / "data" / "results" / f"{results_date}.txt") if results_date else None

    expected_winners: Dict[str, str] | None = None
    aux_state_label = _load_aux_state_label(sharepack) or state
    if results_file and results_file.exists():
        expected_winners = _parse_results(results_file).get(_norm_state(aux_state_label))
        if expected_winners is None:
            print(
                f"Digit Reduction winner validation for {state}: no winners in results file for this state/day; skipping."
            )
            return

    stamp = detect_latest_stamp(winners_dir)

    print(f"Digit Reduction winner validation for {state} (stamp {stamp})")
    problems: List[str] = []
    notes: List[str] = []

    for variant in ["Midday", "Evening", "Combined"]:
        expected_for_variant = expected_winners.get(variant) if expected_winners and variant in {"Midday", "Evening"} else None
        if expected_winners is not None:
            if variant in {"Midday", "Evening"} and not expected_for_variant:
                print(f"- {variant}: no winner in results file; skipping (expected on some days)")
                continue
            if variant == "Combined" and not expected_winners:
                print("- Combined: no winners in results file; skipping (expected)")
                continue

        stamp_variant = variant
        stamp_path = winners_dir / f"{stamp}_{variant}_winner_stamp.json"
        flags_path = winners_dir / f"{stamp}_{variant}_winner_flags.csv"
        hits_path = winners_dir / f"{stamp}_{variant}_winner_hits.csv"

        if not stamp_path.exists():
            # If only one of Midday/Evening exists in results, allow the tool to have written it under the other period bucket.
            aliased = False
            if expected_winners is not None and variant in {"Midday", "Evening"} and expected_for_variant:
                other = "Evening" if variant == "Midday" else "Midday"
                other_expected = expected_winners.get(other) if expected_winners else None
                other_stamp = winners_dir / f"{stamp}_{other}_winner_stamp.json"
                other_flags = winners_dir / f"{stamp}_{other}_winner_flags.csv"
                other_hits = winners_dir / f"{stamp}_{other}_winner_hits.csv"
                if not other_expected and other_stamp.exists() and other_flags.exists() and other_hits.exists():
                    other_data = load_json(other_stamp)
                    other_winner = _normalize_pick3_literal(str(other_data.get("winner") or ""))
                    if other_winner == expected_for_variant:
                        notes.append(
                            f"{variant}: missing {variant} stamp; using {other} artifacts because results has only {variant} winner"
                        )
                        stamp_variant = other
                        stamp_path, flags_path, hits_path = other_stamp, other_flags, other_hits
                        aliased = True
            if not aliased:
                problems.append(f"{variant}: missing stamp JSON ({stamp_path.name})")
                continue
        if not flags_path.exists():
            problems.append(f"{variant}: missing flags CSV ({flags_path.name})")
            continue
        if not hits_path.exists():
            problems.append(f"{variant}: missing hits CSV ({hits_path.name})")
            continue

        stamp_data = load_json(stamp_path)
        counts = stamp_data.get("counts") or {}
        items_total = int(counts.get("items_total") or 0)
        literal = str(stamp_data.get("winner") or "unknown")
        canonical = str(stamp_data.get("winner_canon") or canonical_of_literal(literal))

        flags = pd.read_csv(flags_path)
        hits = pd.read_csv(hits_path)

        if items_total and len(flags) != items_total:
            problems.append(f"{variant}: flags rows={len(flags)} != items_total={items_total}")
        if items_total and len(hits) != items_total:
            problems.append(f"{variant}: hits rows={len(hits)} != items_total={items_total}")

        # Any counts (from flags)
        any_map = {
            "exact_any": "dr_win_exact",
            "vtrac_any": "dr_win_vtrac",
            "drop_exact_any": "dr_win_drop_exact",
            "drop_vtrac_any": "dr_win_drop_vtrac",
            "family_exact_any": "dr_win_family_exact",
            "family_vtrac_any": "dr_win_family_vtrac",
        }
        for k, col in any_map.items():
            if col not in flags.columns:
                problems.append(f"{variant}: flags missing column {col} (needed for {k})")
                continue
            if k in counts:
                got = int(flags[col].fillna(0).sum())
                exp = int(counts.get(k) or 0)
                if got != exp:
                    problems.append(f"{variant}: {k} mismatch (flags {got} vs stamp {exp})")

        # Final counts (from hits)
        final_map = {
            "exact_final": "final_exact_match",
            "vtrac_final": "final_vtrac_match",
            "drop_exact_final": "final_drop_exact_match",
            "drop_vtrac_final": "final_drop_vtrac_match",
            "family_exact_final": "final_family_exact_match",
            "family_vtrac_final": "final_family_vtrac_match",
        }
        for k, col in final_map.items():
            if col not in hits.columns:
                problems.append(f"{variant}: hits missing column {col} (needed for {k})")
                continue
            if k in counts:
                got = int(hits[col].fillna(0).sum())
                exp = int(counts.get(k) or 0)
                if got != exp:
                    problems.append(f"{variant}: {k} mismatch (hits {got} vs stamp {exp})")

        vt_boxed_any = int(flags["dr_win_vt_boxed"].fillna(0).sum()) if "dr_win_vt_boxed" in flags.columns else None
        vt_straight_any = int(flags["dr_win_vt_straight"].fillna(0).sum()) if "dr_win_vt_straight" in flags.columns else None
        vt_boxed_final = int(hits["final_vt_boxed"].fillna(0).sum()) if "final_vt_boxed" in hits.columns else None
        vt_straight_final = int(hits["final_vt_straight"].fillna(0).sum()) if "final_vt_straight" in hits.columns else None

        label = variant
        if stamp_variant != variant:
            label = f"{variant} (using {stamp_variant} artifacts)"
        print(
            f"- {label}: winner {literal} (canon {canonical}) | items_total={items_total} | "
            f"exact_any={counts.get('exact_any')} exact_final={counts.get('exact_final')} | "
            f"vtrac_any={counts.get('vtrac_any')} vtrac_final={counts.get('vtrac_final')} | "
            f"vt_boxed_any={vt_boxed_any} vt_boxed_final={vt_boxed_final} | "
            f"vt_straight_any={vt_straight_any} vt_straight_final={vt_straight_final}"
        )

    if not problems:
        print("\nOK: DR winners artifacts are internally consistent (stamp ↔ flags ↔ hits).")
        for note in notes:
            print(f"NOTE: {note}")
    else:
        print("\nProblems:")
        for p in problems:
            print(f"- {p}")
        for note in notes:
            print(f"NOTE: {note}")
        if args.warn_only:
            print("\nWARN-ONLY mode: not failing.")
            return
        raise SystemExit(1)


if __name__ == "__main__":
    main()
