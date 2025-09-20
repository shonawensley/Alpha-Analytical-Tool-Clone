"""Draw list extractor and helpers for auxiliary tools."""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd

from .draws_extractor_p3_columns import (
    canonical_state,
    get_columns_for,
    state_to_filename,
)

logger = logging.getLogger(__name__)

_P3_SHEET_NAME = "P3Draws"
_P3_START_ROW = 19  # zero-indexed row 20 in Excel
_MAX_DRAWS_DEFAULT = 1000
DEFAULT_DRAWS_DIR = Path("data") / "cleaned" / "draws"
LEGACY_DRAWS_DIR = Path("data") / "cleaned"

_P3_CACHE: Optional[pd.DataFrame] = None
_P3_CACHE_PATH: Optional[Path] = None


def _load_p3_draws(excel_path: Path) -> pd.DataFrame:
    global _P3_CACHE, _P3_CACHE_PATH
    excel_path = excel_path.resolve()
    if _P3_CACHE is None or _P3_CACHE_PATH != excel_path:
        _P3_CACHE = pd.read_excel(excel_path, sheet_name=_P3_SHEET_NAME, header=None)
        _P3_CACHE_PATH = excel_path
    return _P3_CACHE


def _excel_col_to_index(col_letter: str) -> int:
    idx = 0
    for char in col_letter:
        idx = idx * 26 + (ord(char.upper()) - ord("A") + 1)
    return idx - 1


def _extract_column_draws(df: pd.DataFrame, col_letter: str, *, max_draws: int) -> List[str]:
    if not col_letter:
        return []
    col_idx = _excel_col_to_index(col_letter)
    draws: List[str] = []
    upper = min(_P3_START_ROW + max_draws * 2, len(df))
    for row in range(_P3_START_ROW, upper):
        if col_idx >= len(df.columns):
            break
        value = df.iat[row, col_idx]
        if pd.isna(value):
            continue
        try:
            draw_str = str(int(value)).zfill(3)
        except (ValueError, TypeError):
            continue
        draws.append(draw_str)
        if len(draws) >= max_draws:
            break
    return draws


def extract_draws_from_columns(
    df: pd.DataFrame,
    column_letters: List[str],
    *,
    max_draws: int = _MAX_DRAWS_DEFAULT,
) -> List[str]:
    aggregated: List[str] = []
    for letter in column_letters:
        aggregated.extend(_extract_column_draws(df, letter, max_draws=max_draws))
    if len(aggregated) > max_draws:
        aggregated = aggregated[:max_draws]
    return aggregated


def _write_draw_csv(path: Path, draws: List[str]) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame({"Draw": draws}).to_csv(path, index=False)
    except PermissionError as exc:
        raise PermissionError(
            f"Permission denied while writing {path}. Close the file if it is open and retry."
        ) from exc


def save_category_csvs(
    excel_path: os.PathLike[str] | str,
    states: List[str],
    outdir: os.PathLike[str] | str,
    *,
    include_combined: bool = True,
    include_specials: bool = True,
    max_draws: int = _MAX_DRAWS_DEFAULT,
) -> None:
    excel_file = Path(excel_path)
    if not excel_file.exists():
        raise FileNotFoundError(f"Excel path not found: {excel_file}")

    df = _load_p3_draws(excel_file)
    out_path = Path(outdir)
    out_path.mkdir(parents=True, exist_ok=True)

    for label in states:
        canonical = canonical_state(label)
        if not canonical:
            logger.warning("Unknown state label '%s' skipped", label)
            continue

        stem = state_to_filename(canonical)

        cols_combined = get_columns_for(canonical, "combined")
        if include_combined and cols_combined:
            draws_combined = extract_draws_from_columns(df, cols_combined, max_draws=max_draws)
            if draws_combined:
                target = out_path / f"{stem}_draws.csv"
                _write_draw_csv(target, draws_combined)

        midday_cols = get_columns_for(canonical, "midday")
        if midday_cols:
            draws_mid = extract_draws_from_columns(df, midday_cols, max_draws=max_draws)
            if draws_mid:
                _write_draw_csv(out_path / f"{stem}_Midday_draws.csv", draws_mid)

        evening_cols = get_columns_for(canonical, "evening")
        if evening_cols:
            draws_eve = extract_draws_from_columns(df, evening_cols, max_draws=max_draws)
            if draws_eve:
                _write_draw_csv(out_path / f"{stem}_Evening_draws.csv", draws_eve)

        if include_specials:
            for category in ("morning", "noon", "nite"):
                spec_cols = get_columns_for(canonical, category)
                if not spec_cols:
                    continue
                draws_spec = extract_draws_from_columns(df, spec_cols, max_draws=max_draws)
                if not draws_spec:
                    continue
                suffix = category.capitalize()
                _write_draw_csv(out_path / f"{stem}_{suffix}_draws.csv", draws_spec)


def _iter_draw_roots(base: Optional[Path]) -> List[Path]:
    if base is not None:
        return [base]

    roots: List[Path] = []
    if DEFAULT_DRAWS_DIR.exists():
        roots.append(DEFAULT_DRAWS_DIR)
    roots.append(LEGACY_DRAWS_DIR)
    return roots


def _load_draws_from_csv(csv_path: Path, *, max_n: int) -> List[str]:
    df = pd.read_csv(csv_path)
    col = "Draw" if "Draw" in df.columns else df.columns[0]
    draws = (
        df[col]
        .astype(str)
        .str.replace(r"\D", "", regex=True)
        .str.zfill(3)
        .tolist()
    )
    if max_n and max_n > 0:
        draws = draws[:max_n]
    return draws


def extract_draw_list(state: str, data_dir: Optional[Path] = None) -> List[str]:
    canonical = canonical_state(state) or state.replace("4", "")

    for root in _iter_draw_roots(data_dir):
        csv_path = root / f"{state_to_filename(canonical)}_draws.csv"
        if csv_path.exists():
            try:
                return _load_draws_from_csv(csv_path, max_n=_MAX_DRAWS_DEFAULT)
            except Exception as exc:
                logger.warning("Failed to read %s: %s", csv_path, exc)
                break

    logger.info("CSV not found for %s, extracting from master Excel", state)
    return _extract_from_master_excel(canonical)


def _extract_from_master_excel(state: str) -> List[str]:
    combined_cols = get_columns_for(state, "combined")
    if not combined_cols:
        raise ValueError(f"No combined mapping available for {state}")

    master_file = Path("data/original/Pick3StatsC4.xlsm")
    if not master_file.exists():
        raise FileNotFoundError(f"Master data file not found at {master_file}")

    df = _load_p3_draws(master_file)
    draws = extract_draws_from_columns(df, combined_cols, max_draws=_MAX_DRAWS_DEFAULT)
    if not draws:
        raise ValueError(f"No valid draws found for {state}")
    return draws


def get_state_info(state: str) -> Dict[str, Any]:
    state_mapping = {
        "Connecticut4": {"id": 4, "draws_per_day": 2},
        "Delaware4": {"id": 5, "draws_per_day": 2},
        "Florida4": {"id": 6, "draws_per_day": 2},
        "Georgia4": {"id": 7, "draws_per_day": 3},
        "Indiana4": {"id": 10, "draws_per_day": 2},
        "Michigan4": {"id": 15, "draws_per_day": 2},
        "NewJersey4": {"id": 18, "draws_per_day": 2},
        "NewYork4": {"id": 20, "draws_per_day": 2},
        "NorthCarolina4": {"id": 21, "draws_per_day": 2},
        "Ohio4": {"id": 22, "draws_per_day": 2},
        "Ontario4": {"id": 23, "draws_per_day": 2},
        "Pennsylvania4": {"id": 24, "draws_per_day": 2},
        "Texas4": {"id": 28, "draws_per_day": 4},
        "Virginia4": {"id": 30, "draws_per_day": 2},
        "WestVirginia4": {"id": 74, "draws_per_day": 1},
    }
    return state_mapping.get(state, {"id": 0, "draws_per_day": 2})


def validate_draw_data(draws: List[str]) -> List[str]:
    validated = []
    for draw in draws:
        draw_str = str(draw).zfill(3)
        if len(draw_str) == 3 and draw_str.isdigit():
            validated.append(draw_str)
        else:
            logger.warning(f"Invalid draw skipped: {draw}")
    return validated
