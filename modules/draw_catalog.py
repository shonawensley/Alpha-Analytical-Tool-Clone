"""Utilities for scanning draw CSVs and double-tracking helpers."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, List, Tuple

Snapshot = Dict[str, Tuple[int, int]]

_DEF_SUFFIXES = ("_Midday", "_Evening", "_Morning", "_Nite", "_Noon")


def draws_since_last_double(draws: Iterable[str]) -> Tuple[int, str | None]:
    """Return (draws_since, combo) for the most recent double in a newest-first list."""
    draw_list = [str(value) for value in draws]
    for idx, combo in enumerate(draw_list):
        if len(combo) != 3:
            continue
        a, b, c = combo[0], combo[1], combo[2]
        if a == b or b == c or a == c:
            return idx, combo
    return len(draw_list), None


def scan_draw_files(
    directories: Iterable[Path],
    *,
    category_suffixes: Iterable[str] | None = None,
) -> Tuple[Snapshot, List[str]]:
    """Scan draw directories and return (snapshot, sorted state labels).

    The snapshot maps absolute CSV paths to an (mtime_ns, size) tuple so callers can
    invalidate caches when the underlying data changes.
    """
    suffixes = tuple(category_suffixes) if category_suffixes else _DEF_SUFFIXES
    snapshot: Snapshot = {}
    state_labels: set[str] = set()

    for directory in directories:
        path = Path(directory)
        if not path.exists():
            continue
        for csv_path in path.glob("*_draws.csv"):
            try:
                stat = csv_path.stat()
            except OSError:
                continue
            snapshot[str(csv_path.resolve())] = (stat.st_mtime_ns, stat.st_size)

            stem = csv_path.stem
            lower = stem.lower()
            if lower.endswith("_draws"):
                stem = stem[:-6]
                lower = stem.lower()

            base_stem = stem
            for suffix in suffixes:
                if lower.endswith(suffix.lower()):
                    base_stem = stem[: -len(suffix)]
                    break
            state_labels.add(base_stem.replace("_", " "))

    return snapshot, sorted(state_labels)


__all__ = ["draws_since_last_double", "scan_draw_files", "Snapshot"]
