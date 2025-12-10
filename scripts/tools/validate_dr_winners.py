"""
Validate that Digit Reduction winners appear in the winner_flags/hits for a sharepack.

Usage:
  PYTHONPATH=.:src python3 scripts/tools/validate_dr_winners.py --sharepack sharepacks/2025-06-21/OntarioCanada4/digit_reduction/OntarioCanada4

Checks:
  - Detects latest stamp in analyzer_v2/winners.
  - For Midday/Evening/Combined, confirms that winner_flags rows exist and that winner_hits rows exist for the literal.
  - Canonical-aware: uses literal from flags (winner_literal if present) or final_value from hits; falls back to stamp/date if unknown.
"""

import argparse
from pathlib import Path

import pandas as pd


def detect_latest_stamp(winners_dir: Path) -> str:
    stamps = sorted({p.name.split("_")[0] for p in winners_dir.glob("*_winner_flags.csv")})
    if not stamps:
        raise SystemExit("No winner_flags found in winners/")
    return stamps[-1]


def canonical_of_literal(literal: str) -> str:
    return "".join(sorted(str(literal)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sharepack", required=True, help="Path to digit_reduction/<STATE>/<STATE>")
    args = ap.parse_args()

    sharepack = Path(args.sharepack)
    state = sharepack.parent.name if sharepack.parent else sharepack.name
    winners_dir = sharepack / "analyzer_v2" / "winners"
    stamp = detect_latest_stamp(winners_dir)

    print(f"Digit Reduction winner validation for {state} (stamp {stamp})")
    missing = []

    for variant in ["Midday", "Evening", "Combined"]:
        flags = pd.read_csv(winners_dir / f"{stamp}_{variant}_winner_flags.csv")
        hits = pd.read_csv(winners_dir / f"{stamp}_{variant}_winner_hits.csv")

        literal = None
        if "winner_literal" in flags.columns:
            literal = str(flags["winner_literal"].iloc[0])
        elif "final_value" in hits.columns and len(hits):
            literal = str(hits["final_value"].iloc[0])
        else:
            literal = "unknown"
        canonical = canonical_of_literal(literal)

        flags_rows = len(flags)
        hits_rows = len(hits[hits["final_value"].astype(str) == literal])

        if flags_rows == 0 or hits_rows == 0:
            missing.append({"variant": variant, "literal": literal, "canonical": canonical, "flags_rows": flags_rows, "hits_rows": hits_rows})

    if not missing:
        print("OK: all variants have winner flags/hits")
    else:
        print("Missing winners:")
        for m in missing:
            print(f"- {m['variant']}: literal {m['literal']} (canonical {m['canonical']}), flags_rows={m['flags_rows']}, hits_rows={m['hits_rows']}")


if __name__ == "__main__":
    main()
