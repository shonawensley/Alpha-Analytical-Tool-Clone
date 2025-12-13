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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sharepack", required=True, help="Path to digit_reduction/<STATE>/<STATE>")
    ap.add_argument("--warn-only", action="store_true", help="Print problems but do not exit non-zero")
    args = ap.parse_args()

    sharepack = Path(args.sharepack)
    state = sharepack.name
    winners_dir = sharepack / "analyzer_v2" / "winners"
    stamp = detect_latest_stamp(winners_dir)

    print(f"Digit Reduction winner validation for {state} (stamp {stamp})")
    problems: List[str] = []

    for variant in ["Midday", "Evening", "Combined"]:
        stamp_path = winners_dir / f"{stamp}_{variant}_winner_stamp.json"
        flags_path = winners_dir / f"{stamp}_{variant}_winner_flags.csv"
        hits_path = winners_dir / f"{stamp}_{variant}_winner_hits.csv"

        if not stamp_path.exists():
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

        print(
            f"- {variant}: winner {literal} (canon {canonical}) | items_total={items_total} | "
            f"exact_any={counts.get('exact_any')} exact_final={counts.get('exact_final')} | "
            f"vtrac_any={counts.get('vtrac_any')} vtrac_final={counts.get('vtrac_final')} | "
            f"vt_boxed_any={vt_boxed_any} vt_boxed_final={vt_boxed_final} | "
            f"vt_straight_any={vt_straight_any} vt_straight_final={vt_straight_final}"
        )

    if not problems:
        print("\nOK: DR winners artifacts are internally consistent (stamp ↔ flags ↔ hits).")
    else:
        print("\nProblems:")
        for p in problems:
            print(f"- {p}")
        if args.warn_only:
            print("\nWARN-ONLY mode: not failing.")
            return
        raise SystemExit(1)


if __name__ == "__main__":
    main()
