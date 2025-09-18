from __future__ import annotations

from pathlib import Path
from typing import List, Tuple
import pandas as pd


def _norm(label: str) -> str:
    """Normalize a state label or stem: lowercase alnum only (drops spaces/underscores/digits noise)."""
    s = (label or "").lower()
    return "".join(ch for ch in s if ch.isalnum())


def _strip_trailing_digits(s: str) -> str:
    i = len(s)
    while i > 0 and s[i - 1].isdigit():
        i -= 1
    return s[:i]


_CATEGORY_SUFFIXES_NORM = ("midday", "evening", "morning", "nite", "noon")

_DRAWS_ROOT = Path("data") / "cleaned" / "draws"
_LEGACY_DRAWS_ROOT = Path("data") / "cleaned"


def _iter_draw_roots(base: Path | None) -> List[Path]:
    """Return candidate directories where draw CSVs might live."""
    if base is not None:
        return [base]

    roots: List[Path] = []
    if _DRAWS_ROOT.exists():
        roots.append(_DRAWS_ROOT)
    # Legacy location (combined draws historically lived here)
    roots.append(_LEGACY_DRAWS_ROOT)
    return roots


def _pick_draws_csv_for(label: str, base: Path) -> Path | None:
    """Pick the most likely *_draws.csv for a given UI label, tolerant to naming differences.

    When multiple draw categories are present (e.g., Midday/Evening), prefer the canonical
    combined file whose normalized stem exactly matches the state label.
    """
    if not base.exists():
        return None
    want = _norm(label)
    want_no4 = _norm(_strip_trailing_digits(label))

    candidates = list(base.glob("*_draws.csv"))
    if not candidates:
        return None

    def stem_norm(p: Path) -> str:
        stem = p.stem.replace("_draws", "")
        return _norm(stem)

    # 1) exact norm match
    for p in candidates:
        sn = stem_norm(p)
        if sn == want or sn == want_no4:
            return p

    # Filter out known category suffixes (Midday/Evening/etc.) before falling back to
    # relaxed matching. This keeps the default lookup pinned to combined draws.
    filtered: List[Tuple[Path, str]] = []
    for p in candidates:
        sn = stem_norm(p)
        if any(sn.endswith(sfx) for sfx in _CATEGORY_SUFFIXES_NORM):
            continue
        filtered.append((p, sn))

    # 2) contains relationship (e.g., ontario vs ontariocanada)
    for p, sn in filtered:
        if want in sn or want_no4 in sn or sn in want or sn in want_no4:
            return p
    # 3) fallback: None
    return None


def load_state_draws(state_label: str, base: Path | None = None, max_n: int = 1000) -> Tuple[List[str], str]:
    """
    Load newest-first draws for a state from data/cleaned/draws/*_draws.csv (fallback to legacy path).
    Returns (draws, source_path_str). If not found, returns ([], '').
    """
    candidate_roots = _iter_draw_roots(base)
    for root in candidate_roots:
        csv_path = _pick_draws_csv_for(state_label, root)
        if not csv_path:
            continue
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

    return [], ""
