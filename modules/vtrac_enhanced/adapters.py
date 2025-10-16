"""
Adapters for building engine inputs from combined tables and writing outputs.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple, Set

import pandas as pd

from utils.path_handler import get_analysis_output_dir, get_tables_output_dir

from .types import COLUMN_LABELS, EngineInput, PatternsGrid, SectionData, Cell, RINGS, SECTIONS, SETS

HOT_WINDOWS: dict[str, Tuple[int, int]] = {
    "DRAW1": (5, 3),
    "DRAW2": (4, 2),
    "DRAW3": (3, 2),
    "DRAW4": (2, 1),
    "DRAW5": (2, 1),
}


def build_engine_input_from_tables(
    state: str,
    *,
    tables_root: Optional[Path] = None,
    recent_draws: Optional[Sequence[str]] = None,
) -> EngineInput:
    """
    Read the canonical combined tables for a state and build EngineInput.
    """

    root = Path(tables_root or get_tables_output_dir())
    state_dir = root / state
    if not state_dir.exists():
        raise FileNotFoundError(f"Tables directory not found for state {state}: {state_dir}")

    sections: List[SectionData] = []
    collected_draws: List[str] = list(recent_draws or [])

    for set_name in SETS:
        for section in SECTIONS:
            csv_path = _resolve_section_path(state_dir, state, section)
            if not csv_path:
                continue
            df = pd.read_csv(csv_path, dtype=str, keep_default_na=False)
            subset = df[df["Set"].str.strip().str.lower() == set_name.lower()]
            if subset.empty:
                continue

            if not collected_draws:
                draw_digits = _extract_draw_digits(subset)
                if draw_digits:
                    collected_draws.extend(draw_digits)

            ring_map = {}
            for ring in RINGS:
                ring_rows = subset[subset["RowType"].str.upper() == ring]
                if ring_rows.empty:
                    ring_map[ring] = tuple(Cell(digits="") for _ in COLUMN_LABELS)
                    continue
                row = _select_draw_row(ring_rows)
                ring_map[ring] = _cells_from_row(row)

            sections.append(SectionData(section=section, set_name=set_name, patterns=PatternsGrid(by_ring=ring_map)))

    if not sections:
        raise ValueError(f"No combined table data found for state {state}")

    return EngineInput(sections=sections, recent_draws=tuple(collected_draws))


def _resolve_section_path(state_dir: Path, state: str, section: str) -> Optional[Path]:
    candidates = [
        state_dir / f"{state}_{section}_combined.csv",
        state_dir / f"{section}_Combined.csv",
        state_dir / f"{section}_combined.csv",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def _extract_draw_digits(df: pd.DataFrame) -> Sequence[str]:
    draw_rows = df[df["RowType"].str.upper() == "DRAW_DATA"]
    if draw_rows.empty:
        return ()
    row = _select_draw_row(draw_rows)
    text = str(row.get("1", "")).strip()
    digits = "".join(ch for ch in text if ch.isdigit())
    return (digits,) if digits else ()


def _select_draw_row(rows: pd.DataFrame) -> pd.Series:
    if "Draw" not in rows.columns:
        return rows.iloc[0]
    rows = rows.copy()
    rows["__rank"] = rows["Draw"].str.extract(r"(\d+)").fillna("9").astype(int)
    rows = rows.sort_values("__rank")
    return rows.iloc[0]


def _cells_from_row(row: pd.Series) -> Tuple[Cell, ...]:
    draw_name = str(row.get("Draw", "")).strip().upper()
    hot_window, super_window = HOT_WINDOWS.get(draw_name, (0, 0))
    cells: List[Cell] = []
    total_cols = len(COLUMN_LABELS)
    for idx, col in enumerate(COLUMN_LABELS):
        value = str(row.get(str(col), "")).strip()
        digits = "".join(ch for ch in value if ch.isdigit())
        if value.endswith(".0") and not digits:
            digits = value[:-2]
        position_from_right = total_cols - idx
        hot = bool(hot_window and position_from_right <= hot_window)
        superhot = bool(super_window and position_from_right <= super_window)
        cells.append(Cell(digits=digits, hot=hot, superhot=superhot))
    return tuple(cells)


def suggested_mask_digits(recent_draws: Sequence[str]) -> Set[str]:
    """
    Suggest digits to mask using the most recent draw.
    """

    if not recent_draws:
        return set()
    return {ch for ch in str(recent_draws[0]) if ch.isdigit()}


def write_prediction_bundle(
    state: str,
    output: EngineOutput,
    *,
    analysis_root: Optional[Path] = None,
) -> Path:
    """
    Persist analyzer output under data/outputs/analysis/vtrac/<STATE>/.
    """

    root = Path(analysis_root or get_analysis_output_dir())
    target_dir = root / "vtrac" / state
    target_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = target_dir / f"{state}_vtrac_enhanced_{timestamp}.json"

    payload = {
        "state": state,
        "timestamp": timestamp,
        "indices_ranked": [
            {
                "index": score.index,
                "score": score.score,
                "evidence": {
                    "raw": score.evidence.raw,
                    "features": [
                        {"name": feat.name, "value": feat.value, "details": feat.details}
                        for feat in score.evidence.features
                    ],
                },
                "straights": [
                    {
                        "straight": candidate.straight,
                        "score": candidate.score,
                        "reasons": list(candidate.reasons),
                    }
                    for candidate in score.straights
                ],
            }
            for score in output.indices_ranked
        ],
        "straights_ranked": [
            {
                "index": candidate.index,
                "straight": candidate.straight,
                "score": candidate.score,
                "reasons": list(candidate.reasons),
            }
            for candidate in output.straights_ranked
        ],
        "telemetry": output.telemetry,
    }

    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return out_path


__all__ = [
    "build_engine_input_from_tables",
    "suggested_mask_digits",
    "write_prediction_bundle",
]
