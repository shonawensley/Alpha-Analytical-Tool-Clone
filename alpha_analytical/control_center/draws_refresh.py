"""Utilities to reset Aux draw CSVs before regeneration."""
from __future__ import annotations

from pathlib import Path
from typing import List, Sequence

from modules.module_d_auxiliary_tools.refactored import draws_extractor_p3_columns as _columns

__all__ = ["purge_draw_csvs"]

_SPECIAL_SUFFIXES = {
    "morning": "Morning",
    "noon": "Noon",
    "nite": "Nite",
}


def _canonical_and_stem(state_label: str) -> tuple[str, str]:
    canonical = _columns.canonical_state(state_label) or state_label.replace("4", "")
    stem = (
        canonical.replace(" ", "_")
        .replace("(", "")
        .replace(")", "")
    )
    return canonical, stem


def _expected_paths(canonical: str, stem: str, out_dir: Path, include_combined: bool, include_specials: bool) -> List[Path]:
    paths: List[Path] = []
    if include_combined:
        paths.append(out_dir / f"{stem}_draws.csv")
    if _columns.get_columns_for(canonical, "midday"):
        paths.append(out_dir / f"{stem}_Midday_draws.csv")
    if _columns.get_columns_for(canonical, "evening"):
        paths.append(out_dir / f"{stem}_Evening_draws.csv")
    if include_specials:
        for key, suffix in _SPECIAL_SUFFIXES.items():
            if _columns.get_columns_for(canonical, key):
                paths.append(out_dir / f"{stem}_{suffix}_draws.csv")
    return paths


def purge_draw_csvs(
    states: Sequence[str],
    out_dir: Path | str,
    *,
    include_combined: bool = True,
    include_specials: bool = False,
) -> List[Path]:
    """Delete existing draw CSVs for the given states.

    Returns the list of files that were removed. Missing files are ignored.
    """
    out_path = Path(out_dir)
    removed: List[Path] = []
    if not states or not out_path.exists():
        return removed

    for state in states:
        canonical, stem = _canonical_and_stem(state)
        for candidate in _expected_paths(canonical, stem, out_path, include_combined, include_specials):
            if candidate.exists():
                candidate.unlink()
                removed.append(candidate)
    return removed
