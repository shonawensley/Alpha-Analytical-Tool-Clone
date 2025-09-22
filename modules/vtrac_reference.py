"""
Canonical V-TRAC reference API for non-Aux pages.

Exports:
- get_vtrac_index(winner: str) -> int
- get_index_set(index: int) -> set[str]
- get_index_straights(winner: str) -> set[str]
- VTRAC_DISPLAY, BOXED_VTRAC_REFERENCE, BOXED_LABEL_LOOKUP (legacy compat)

Implementation notes:
- Uses analyzer utilities already present in the project so this module
  does not depend on the staged Aux package for helpers, but we lazily
  re-export the legacy constants so existing tooling remains stable.
"""
from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Set


def _load_staged_reference():
    """Best-effort loader for the legacy staged V-TRAC reference."""
    try:
        staged_path = (
            Path(__file__).resolve().parent.parent
            / "scripts"
            / "auxiliary"
            / "working"
            / "modules"
            / "vtrac_reference.py"
        )
        if not staged_path.exists():
            return None
        spec = spec_from_file_location("_staged_vtrac_reference", str(staged_path))
        if not spec or not spec.loader:
            return None
        module = module_from_spec(spec)
        spec.loader.exec_module(module)  # type: ignore[union-attr]
        return module
    except Exception:
        return None


_STAGED = _load_staged_reference()
if _STAGED is not None:
    VTRAC_DISPLAY = getattr(_STAGED, "VTRAC_DISPLAY", [])
    BOXED_VTRAC_REFERENCE = getattr(_STAGED, "BOXED_VTRAC_REFERENCE", [])
    BOXED_LABEL_LOOKUP = getattr(_STAGED, "BOXED_LABEL_LOOKUP", {})
else:
    VTRAC_DISPLAY = []
    BOXED_VTRAC_REFERENCE = []
    BOXED_LABEL_LOOKUP = {}


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
    "VTRAC_DISPLAY",
    "BOXED_VTRAC_REFERENCE",
    "BOXED_LABEL_LOOKUP",
]
