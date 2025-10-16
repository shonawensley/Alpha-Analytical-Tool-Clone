"""
Adapters for loading combined tables and writing enhanced analyzer outputs.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Set, Tuple

import pandas as pd

from utils.path_handler import get_analysis_output_dir, get_tables_output_dir

from .types import Cell, EngineInput, EngineOutput, PatternsGrid, SectionData

SECTIONS: Tuple[str, ...] = ("Midday", "Evening", "Combined")
RINGS: Tuple[str, ...] = ("R2", "R4", "R6", "R8")
COLUMN_ORDER: Tuple[str, ...] = ("7", "6", "5", "4", "3", "2", "1")
SET_ORDER: Tuple[str, ...] = ("Set1", "Set2", "Set3")
HOT_WINDOWS = {
    "Draw1": (5, 3),
    "Draw2": (4, 2),
    "Draw3": (3, 2),
    "Draw4": (2, 1),
    "Draw5": (2, 1),
}


def build_engine_input_from_tables(
    state: str,
    *,
    tables_root: Optional[Path] = None,
    recent_draws: Optional[Sequence[str]] = None,
) -> EngineInput:
    """
    Load the canonical combined tables for a state and build the EngineInput.
    """

    tables_root = tables_root or Path(get_tables_output_dir())
    state_dir = tables_root / state
    if not state_dir.exists():
        raise FileNotFoundError(f"Tables directory not found for state {state}: {state_dir}")

    sections: List[SectionData] = []

    for set_name in SET_ORDER:
        for section in SECTIONS:
            csv_path = state_dir / f"{state}_{section}_combined.csv"
            if not csv_path.exists():
                continue
            df = pd.read_csv(csv_path, dtype=str, keep_default_na=False)
            subset = df[df["Set"].str.lower() == set_name.lower()]
            if subset.empty:
                continue

            ring_map = {}
            for ring in RINGS:
                ring_rows = subset[subset["RowType"].str.upper() == ring]
                if ring_rows.empty:
                    ring_map[ring] = tuple(Cell(digits="") for _ in COLUMN_ORDER)
                    continue
                row = _select_draw_row(ring_rows)
                ring_map[ring] = _cells_from_row(row)

            patterns = PatternsGrid(by_r=ring_map)
            sections.append(SectionData(section=section, set_name=set_name, patterns=patterns))

    return EngineInput(sections=sections, recent_draws=recent_draws or ())


def _select_draw_row(rows: pd.DataFrame) -> pd.Series:
    """
    Choose the row with the most recent draw (Draw1 preferred) for a ring.
    """

    if "Draw" not in rows.columns:
        return rows.iloc[0]
    rows = rows.copy()
    rows["__rank"] = rows["Draw"].str.extract(r"(\d+)").fillna("9").astype(int)
    rows = rows.sort_values("__rank")
    return rows.iloc[0]


def _cells_from_row(row: pd.Series) -> Tuple[Cell, ...]:
    draw_name = str(row.get("Draw", "")).strip()
    hot_window, super_window = HOT_WINDOWS.get(draw_name, (0, 0))
    cells: List[Cell] = []
    for idx, column in enumerate(COLUMN_ORDER, start=1):
        col_number = int(column)
        value = _clean_digits(row.get(column, ""))
        hot = bool(hot_window and col_number <= hot_window)
        superhot = bool(super_window and col_number <= super_window)
        cells.append(Cell(digits=value, hot=hot, superhot=superhot))
    return tuple(cells)


def _clean_digits(value: object) -> str:
    digits = str(value).strip()
    if not digits or digits.lower() in {"nan", "none"}:
        return ""
    if digits.endswith(".0"):
        digits = digits[:-2]
    return digits.replace(".", "")


def suggested_mask_digits(recent_draws: Sequence[str]) -> Set[str]:
    """
    Suggest the digits to mask (typically the most recent draw).
    """

    if not recent_draws:
        return set()
    return set(str(recent_draws[0]))


def write_prediction_bundle(
    state: str,
    output: EngineOutput,
    *,
    analysis_root: Optional[Path] = None,
) -> Path:
    """
    Persist the engine output as JSON in the canonical analysis folder.
    """

    analysis_root = analysis_root or Path(get_analysis_output_dir())
    target_dir = analysis_root / "vtrac_enhanced" / state
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
                "raw": score.evidence.raw,
                "features": [
                    {"name": feat.name, "value": feat.value, "details": feat.details}
                    for feat in score.evidence.features
                ],
                "straights": [
                    {
                        "straight": candidate.straight,
                        "score": candidate.score,
                        "reasons": candidate.reasons,
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
                "reasons": candidate.reasons,
            }
            for candidate in output.straights_ranked
        ],
        "telemetry": output.telemetry,
    }

    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return out_path
