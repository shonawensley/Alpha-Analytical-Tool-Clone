#!/usr/bin/env python
"""
Headless entrypoint for the enhanced V-TRAC analyzer.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Sequence

import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from modules import vtrac_enhanced as ve  # noqa: E402  (import after sys.path tweak)


def run_cli(
    state: str,
    *,
    tables_root: Optional[Path] = None,
    analysis_root: Optional[Path] = None,
    mask_digits: Optional[str] = None,
) -> Path:
    engine_input = ve.build_engine_input_from_tables(state, tables_root=tables_root)
    digits_to_mask = set(mask_digits) if mask_digits else ve.suggested_mask_digits(engine_input.recent_draws)
    output = ve.run_analysis(engine_input, digits_to_mask=digits_to_mask)
    bundle_path = ve.write_prediction_bundle(state, output, analysis_root=analysis_root)
    _print_summary(output, digits_to_mask)
    return bundle_path


def _print_summary(output: ve.EngineOutput, digits_to_mask: Sequence[str]) -> None:
    mask_display = "".join(sorted(digits_to_mask)) if digits_to_mask else "(none)"
    print(f"Mask digits: {mask_display}")
    print("\nTop V-TRAC indices:")
    for score in output.indices_ranked[:10]:
        sections = ", ".join(score.evidence.raw.get("sections", []))
        print(f"  #{score.index:<2} -> {score.score:6.2f}   sections=[{sections}]")

    print("\nTop straight candidates:")
    for straight in output.straights_ranked[:10]:
        reasons = ", ".join(straight.reasons)
        print(f"  {straight.straight} (idx {straight.index}) -> {straight.score:6.2f} [{reasons}]")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the enhanced V-TRAC analyzer headlessly.")
    parser.add_argument("--state", required=True, help="State identifier (e.g., Connecticut4)")
    parser.add_argument("--tables-root", type=Path, help="Override tables root directory")
    parser.add_argument("--analysis-root", type=Path, help="Override analysis output directory")
    parser.add_argument("--mask", help="Digits to mask (defaults to most recent draw)")
    args = parser.parse_args()

    bundle_path = run_cli(
        state=args.state,
        tables_root=args.tables_root,
        analysis_root=args.analysis_root,
        mask_digits=args.mask,
    )
    print(f"\nBundle written to {bundle_path}")


if __name__ == "__main__":
    main()
