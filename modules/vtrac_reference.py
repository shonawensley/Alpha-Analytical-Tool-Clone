"""
Canonical V-TRAC reference API for non-Aux pages.

Exports:
- get_vtrac_index(winner: str) -> int
- get_index_set(index: int) -> set[str]
- get_index_straights(winner: str) -> set[str]

Implementation notes:
- Uses analyzer utilities already present in the project so this module
  does not depend on the staged Aux package.
"""
from __future__ import annotations

from typing import Set


def _norm_winner(w: str) -> str:
    w = "".join(ch for ch in str(w or "") if ch.isdigit())
    if len(w) != 3:
        raise ValueError(f"winner must be 3 digits, got {w!r}")
    return w


def get_vtrac_index(winner: str) -> int:
    """Return the V-TRAC index for a 3-digit winner using analyzer utilities."""
    from utils.vtrac_utils import find_vtrac_index_and_combos  # lazy import

    w = _norm_winner(winner)
    idx, _perms, _related = find_vtrac_index_and_combos(w)
    return int(idx) if idx is not None else 0


def get_index_set(index: int) -> Set[str]:
    """Return the full pattern set (singles + doubles) for the index.
    Uses analyzer helper to gather combinations.
    """
    from src.core.module_c_vtrac import get_all_combinations_for_index  # lazy

    combos = set(get_all_combinations_for_index(int(index)) or [])
    # Ensure all as strings of length 3
    return {str(c) for c in combos}


def get_index_straights(winner: str) -> Set[str]:
    """Return unique straights (permutations) for the winner (3-digit)."""
    w = _norm_winner(winner)
    a, b, c = w[0], w[1], w[2]
    return {
        a + b + c,
        a + c + b,
        b + a + c,
        b + c + a,
        c + a + b,
        c + b + a,
    }


__all__ = [
    "get_vtrac_index",
    "get_index_set",
    "get_index_straights",
]
