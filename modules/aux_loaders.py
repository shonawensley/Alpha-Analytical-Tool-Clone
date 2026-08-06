from __future__ import annotations

from pathlib import Path
from utils.path_handler import get_cleaned_draws_dir, get_cleaned_data_dir
from typing import Dict, List, Optional, Tuple, Literal

import pandas as pd

Variant = Literal["combined", "midday", "evening"]


def _norm(label: str) -> str:
    """Normalize a state label or stem: lowercase alnum only (drops spaces/underscores/digits noise)."""
    s = (label or "").lower()
    return "".join(ch for ch in s if ch.isalnum())


def _strip_trailing_digits(s: str) -> str:
    i = len(s)
    while i > 0 and s[i - 1].isdigit():
        i -= 1
    return s[:i]


_SUFFIX_VARIANT_MAP: Dict[str, str] = {
    "_midday": "midday",
    "_evening": "evening",
    "_morning": "morning",
    "_nite": "nite",
    "_noon": "noon",
}

_STATE_ALIASES = {
    "ontariocanada": "ontario",
}

_DRAWS_ROOT = Path(get_cleaned_draws_dir())
_LEGACY_DRAWS_ROOT = Path(get_cleaned_data_dir())


def _iter_draw_roots(base: Optional[Path]) -> List[Path]:
    """Return candidate directories where draw CSVs might live."""
    if base is not None:
        return [base]

    roots: List[Path] = []
    if _DRAWS_ROOT.exists():
        roots.append(_DRAWS_ROOT)
    # Legacy location (combined draws historically lived here)
    roots.append(_LEGACY_DRAWS_ROOT)
    return roots


def _split_variant_from_stem(stem: str) -> Tuple[str, str]:
    lowered = stem.lower()
    for suffix, variant in _SUFFIX_VARIANT_MAP.items():
        if lowered.endswith(suffix):
            return stem[: -len(suffix)], variant
    return stem, "combined"


def _stem_without_suffix(path: Path) -> str:
    stem = path.stem
    if stem.lower().endswith("_draws"):
        stem = stem[:-6]
    return stem


def _state_norms(label: str) -> set[str]:
    values = {
        _norm(label),
        _norm(_strip_trailing_digits(label)),
    }
    for value in tuple(values):
        alias = _STATE_ALIASES.get(value)
        if alias:
            values.add(alias)
    return {value for value in values if value}


def _pick_draws_csv_for_variant(label: str, base: Path, variant: Variant) -> Optional[Path]:
    """Pick the most likely *_draws.csv for a given UI label/variant combination."""
    if not base.exists():
        return None

    wanted = _state_norms(label)
    candidates = sorted(base.glob("*_draws.csv"))
    if not candidates:
        return None

    for path in candidates:
        stem = _stem_without_suffix(path)
        state_stem, detected_variant = _split_variant_from_stem(stem)
        if detected_variant != variant:
            continue
        if _norm(state_stem) in wanted:
            return path
    return None


def _pick_combined_csv(label: str, base: Path) -> Optional[Path]:
    """Original combined resolver retained for backwards compatibility."""
    if not base.exists():
        return None
    wanted = _state_norms(label)
    candidates = sorted(base.glob("*_draws.csv"))
    if not candidates:
        return None

    for path in candidates:
        stem = _stem_without_suffix(path)
        state_stem, detected_variant = _split_variant_from_stem(stem)
        if detected_variant != "combined":
            continue
        if _norm(state_stem) in wanted:
            return path
    return None


def _resolve_csv_path(state_label: str, variant: Variant, base: Optional[Path]) -> Optional[Path]:
    for root in _iter_draw_roots(base):
        if variant == "combined":
            csv_path = _pick_combined_csv(state_label, root)
        else:
            csv_path = _pick_draws_csv_for_variant(state_label, root, variant)
        if csv_path:
            return csv_path
    return None


def load_state_draws(
    state_label: str,
    variant: Variant = "combined",
    *,
    base: Optional[Path] = None,
    max_n: int = 1000,
) -> Tuple[List[str], Optional[str]]:
    """Load newest-first draws for a state/variant combination.

    Returns (draws, resolved_path). If the file is missing or unreadable, returns ([], None).
    """
    csv_path = _resolve_csv_path(state_label, variant, base)
    if not csv_path:
        return [], None

    try:
        df = pd.read_csv(csv_path)
        col = "Draw" if "Draw" in df.columns else df.columns[0]
        draws = (
            df[col]
            .astype(str)
            .str.replace(r"\\D", "", regex=True)
            .str.zfill(3)
            .tolist()
        )
        if max_n and max_n > 0:
            draws = draws[:max_n]
        return draws, str(csv_path)
    except Exception:
        return [], str(csv_path)


__all__ = ["Variant", "load_state_draws"]
