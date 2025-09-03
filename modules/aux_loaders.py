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


def _pick_draws_csv_for(label: str, base: Path) -> Path | None:
    """Pick the most likely *_draws.csv for a given UI label, tolerant to naming differences."""
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
    # 2) contains relationship (e.g., ontario vs ontariocanada)
    for p in candidates:
        sn = stem_norm(p)
        if want in sn or want_no4 in sn or sn in want or sn in want_no4:
            return p
    # 3) fallback: None
    return None


def load_state_draws(state_label: str, base: Path | None = None, max_n: int = 1000) -> Tuple[List[str], str]:
    """
    Load newest-first draws for a state from data/cleaned/*_draws.csv.
    Returns (draws, source_path_str). If not found, returns ([], '').
    """
    base = base or Path("data") / "cleaned"
    csv_path = _pick_draws_csv_for(state_label, base)
    if not csv_path:
        return [], ""
    try:
        df = pd.read_csv(csv_path)
        # Prefer a column literally named Draw; otherwise take the first column
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
