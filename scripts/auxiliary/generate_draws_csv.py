"""Generate Auxiliary draw CSVs from Pick3StatsC4.xlsm.

This script wraps the refactored extractor so operators can rebuild
Combined/Midday/Evening draw files (and optional specials) for the Aux
module in one step. Combined CSVs are emitted by default so the Aux page
continues to work without extra steps.

Usage examples (run from repo root):

  py -3 scripts/auxiliary/generate_draws_csv.py --states Connecticut Delaware
  py -3 scripts/auxiliary/generate_draws_csv.py --skip-combined --include-specials
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable, List


def _ensure_project_root() -> Path:
    script_path = Path(__file__).resolve()
    project_root = script_path.parents[2]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    return project_root


PROJECT_ROOT = _ensure_project_root()
DEFAULT_DRAWS_DIR = PROJECT_ROOT / "data" / "cleaned" / "draws"


from modules.module_d_auxiliary_tools.refactored import (  # noqa: E402
    draws_extractor_p3_columns as column_map,
    extractor as aux_extractor,
)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Aux draw CSVs")
    parser.add_argument(
        "--excel",
        default=str(PROJECT_ROOT / "data" / "original" / "Pick3StatsC4.xlsm"),
        help="Path to Pick3StatsC4.xlsm (default: data/original/Pick3StatsC4.xlsm)",
    )
    parser.add_argument(
        "--outdir",
        default=str(DEFAULT_DRAWS_DIR),
        help="Directory to write draw CSVs (default: data/cleaned/draws)",
    )
    parser.add_argument(
        "--states",
        nargs="*",
        help="Subset of states to process (default: all tracked Aux states)",
    )
    parser.add_argument(
        "--skip-combined",
        action="store_true",
        help="Skip writing <State>_draws.csv (combined) if you only need Midday/Evening",
    )
    parser.add_argument(
        "--include-specials",
        action="store_true",
        help="Generate Morning/Noon/Nite CSVs where available",
    )
    parser.add_argument(
        "--max-draws",
        type=int,
        default=1000,
        help="Number of newest draws to keep (default: 1000)",
    )
    parser.add_argument(
        "--list-states",
        action="store_true",
        help="Print tracked states and exit",
    )
    return parser.parse_args()


def _resolve_states(arg: Iterable[str] | None) -> List[str]:
    if arg:
        return list(arg)
    return column_map.get_tracked_states()


def main() -> None:
    args = _parse_args()

    tracked = column_map.get_tracked_states()
    if args.list_states:
        print("Tracked Aux states:")
        for name in tracked:
            print(f" - {name}")
        return

    states = _resolve_states(args.states)
    invalid = [s for s in states if column_map.canonical_state(s) is None]
    if invalid:
        print("Warning: unknown state labels skipped ->", ", ".join(invalid))
        states = [s for s in states if column_map.canonical_state(s) is not None]

    if not states:
        print("No valid states to process; exiting.")
        return

    try:
        aux_extractor.save_category_csvs(
            excel_path=args.excel,
            states=states,
            outdir=args.outdir,
            include_combined=not args.skip_combined,
            include_specials=args.include_specials,
            max_draws=args.max_draws,
        )
    except PermissionError as exc:
        print(f"Error: {exc}")
        return

    print("Draw exports complete:")
    for label in states:
        canonical = column_map.canonical_state(label) or label
        stem = column_map.state_to_filename(canonical)

        if not args.skip_combined and column_map.get_columns_for(canonical, "combined"):
            print(f" - {stem}_draws.csv")

        if column_map.get_columns_for(canonical, "midday"):
            print(f" - {stem}_Midday_draws.csv")
        if column_map.get_columns_for(canonical, "evening"):
            print(f" - {stem}_Evening_draws.csv")

        if args.include_specials:
            for suffix_key, suffix_name in (("morning", "Morning"), ("noon", "Noon"), ("nite", "Nite")):
                if column_map.get_columns_for(canonical, suffix_key):
                    print(f" - {stem}_{suffix_name}_draws.csv")


if __name__ == "__main__":
    main()
