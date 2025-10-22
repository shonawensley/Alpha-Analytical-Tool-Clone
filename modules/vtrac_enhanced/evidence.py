"""
Shared evidence layer for V-TRAC string tables.

This module normalises the Midday/Evening/Combined tables into a grid,
lets callers evaluate a winner/index family against every cell, and
produces per-box summaries (earliest step, persistence, echoes, etc.).

Both the Streamlit winners logger and the enhanced analyzer can consume
these objects so they reason about the exact same evidence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property
import math
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Mapping, MutableMapping, Optional, Sequence, Tuple

import pandas as pd

from modules.vtrac_matchers import WinnerTargets, collect_spans, digits_only

__all__ = [
    "COL_LABELS",
    "CellKey",
    "CellEvidence",
    "BoxKey",
    "BoxEvidence",
    "VtracGrid",
    "load_state_tables",
    "build_grid",
]

# ---------------------------------------------------------------------------
# Constants & helpers
# ---------------------------------------------------------------------------

COL_LABELS: Tuple[str, ...] = ("7", "6", "5", "4", "3", "2", "1")

ROWTYPE_ORDER_CACHE: MutableMapping[str, int] = {}

HIGHLIGHT_PRIORITY: Dict[str, int] = {
    "family_gap": 1,
    "family_strict": 2,
    "vt_straight_gap": 3,
    "vt_straight_strict": 4,
    "winner_gap": 5,
    "winner_strict": 6,
}

HIGHLIGHT_CLASS: Dict[str, str] = {
    "winner_strict": "hit-winner",
    "winner_gap": "hit-winner-gap",
    "vt_straight_strict": "hit-vt-straight",
    "vt_straight_gap": "hit-vt-straight-gap",
    "family_strict": "hit-family",
    "family_gap": "hit-family-gap",
}

CATEGORY_MAP: Dict[str, str] = {
    "winner_strict": "exact",
    "winner_gap": "drop_exact",
    "vt_straight_strict": "vt_straight",
    "vt_straight_gap": "drop_vt_straight",
    "family_strict": "family_exact",
    "family_gap": "family_drop",
}

TRACKED_CATEGORIES: Tuple[str, ...] = tuple(CATEGORY_MAP.values())


def _normalise_variant(label: str) -> str:
    base = str(label or "").strip()
    if base.endswith("_combined"):
        base = base[:-9]
    return base.capitalize()


def _row_order(row_type: str) -> int:
    if row_type in ROWTYPE_ORDER_CACHE:
        return ROWTYPE_ORDER_CACHE[row_type]
    raw = row_type.strip().upper()
    if raw.startswith("R"):
        try:
            value = int(raw[1:])
        except ValueError:
            value = 0
    else:
        value = 0
    ROWTYPE_ORDER_CACHE[row_type] = value
    return value


def _is_reduction_row(row_type: str) -> bool:
    raw = row_type.strip().upper()
    return raw.startswith("R") and raw[1:].isdigit()


# ---------------------------------------------------------------------------
# Dataclasses representing cells and boxes
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CellKey:
    variant: str
    set_name: str
    draw: str
    column: int
    row_type: str

    @property
    def is_reduction(self) -> bool:
        return _is_reduction_row(self.row_type)

    @property
    def step(self) -> int:
        return _row_order(self.row_type)


@dataclass
class CellEvidence:
    key: CellKey
    raw: str
    digits: str
    hot_level: int
    spans: Dict[str, List[Tuple[int, int]]] = field(default_factory=dict)

    @property
    def flags(self) -> Dict[str, bool]:
        return {name: bool(spans) for name, spans in self.spans.items()}

    def render_highlighted(self) -> str:
        if not self.spans:
            return self.raw
        chars = list(self.raw)
        labels: List[Optional[str]] = [None] * len(chars)
        for category in ("family_gap", "family_strict", "vt_straight_gap", "vt_straight_strict", "winner_gap", "winner_strict"):
            priority = HIGHLIGHT_PRIORITY.get(category, 0)
            for start, end in self.spans.get(category, []):
                for idx in range(start, min(end, len(labels))):
                    current = labels[idx]
                    if current is None or HIGHLIGHT_PRIORITY.get(current, 0) < priority:
                        labels[idx] = category
        result: List[str] = []
        idx = 0
        while idx < len(chars):
            label = labels[idx]
            if label is None:
                result.append(chars[idx])
                idx += 1
            else:
                cls = HIGHLIGHT_CLASS[label]
                j = idx
                while j < len(chars) and labels[j] == label:
                    j += 1
                segment = "".join(chars[idx:j])
                result.append(f'<span class="{cls}">{segment}</span>')
                idx = j
        return "".join(result)


@dataclass(frozen=True)
class BoxKey:
    variant: str
    set_name: str
    draw: str
    column: int


@dataclass
class MatchSummary:
    present: bool = False
    first_row: Optional[str] = None
    first_step: Optional[int] = None
    rows: List[str] = field(default_factory=list)
    final_row: Optional[str] = None

    @property
    def count(self) -> int:
        return len(self.rows)


@dataclass
class BoxEvidence:
    key: BoxKey
    cells: Dict[str, CellEvidence] = field(default_factory=dict)
    row_order: List[str] = field(default_factory=list)
    summary: Dict[str, MatchSummary] = field(default_factory=dict)

    @cached_property
    def set_index(self) -> int:
        name = self.key.set_name.strip().lower()
        if name.startswith("set"):
            try:
                value = int(name[3:])
                if value >= 1:
                    return value - 1
            except ValueError:
                pass
        return math.inf

    def iter_cells(self) -> Iterator[CellEvidence]:
        for row in self.row_order:
            cell = self.cells.get(row)
            if cell:
                yield cell


@dataclass
class VtracGrid:
    boxes: Dict[BoxKey, BoxEvidence]
    raw_tables: Dict[str, pd.DataFrame]

    def evaluate(self, targets: WinnerTargets) -> "VtracGrid":
        for box in self.boxes.values():
            summary_map: Dict[str, MatchSummary] = {cat: MatchSummary() for cat in TRACKED_CATEGORIES}
            updated_cells: Dict[str, CellEvidence] = {}
            for row_type in box.row_order:
                cell = box.cells[row_type]
                spans = collect_spans(cell.raw, targets)
                cell.spans = spans
                updated_cells[row_type] = cell
                for source_cat, mapped in CATEGORY_MAP.items():
                    if spans.get(source_cat):
                        summary = summary_map[mapped]
                        if not summary.present:
                            summary.present = True
                            summary.first_row = row_type
                            summary.first_step = cell.key.step
                        summary.rows.append(row_type)
                        summary.final_row = row_type
            box.cells = updated_cells
            box.summary = summary_map
        return self


# ---------------------------------------------------------------------------
# Loading & grid construction
# ---------------------------------------------------------------------------


def load_state_tables(state: str, *, tables_root: Optional[Path] = None) -> Dict[str, pd.DataFrame]:
    root = Path(tables_root) if tables_root else Path("data") / "outputs" / "tables"
    state_dir = root / state
    if not state_dir.exists():
        raise FileNotFoundError(f"Tables directory not found for state {state}: {state_dir}")

    def _resolve(section: str) -> Path:
        candidates = [
            state_dir / f"{state}_{section}_combined.csv",
            state_dir / f"{section}_Combined.csv",
            state_dir / f"{section}_combined.csv",
        ]
        for candidate in candidates:
            if candidate.exists():
                return candidate
        raise FileNotFoundError(f"Combined table missing for section '{section}' (state {state})")

    tables: Dict[str, pd.DataFrame] = {}
    for section in ("Midday", "Evening", "Combined"):
        path = _resolve(section)
        df = pd.read_csv(path, dtype=str).fillna("")
        tables[f"{section}_combined"] = df
    return tables


def build_grid(tables: Mapping[str, pd.DataFrame]) -> VtracGrid:
    boxes: Dict[BoxKey, BoxEvidence] = {}
    for variant_key, df in tables.items():
        variant = _normalise_variant(variant_key)
        for _, row in df.iterrows():
            set_name = str(row.get("Set", "") or "").strip()
            draw = str(row.get("Draw", "") or "").strip()
            row_type = str(row.get("RowType", "") or "").strip()
            if not set_name or not draw:
                continue
            for col_label in COL_LABELS:
                if col_label not in df.columns:
                    continue
                raw_value = str(row.get(col_label, "") or "")
                digits = digits_only(raw_value)
                hot_level = raw_value.count("*")
                column = int(col_label)
                cell_key = CellKey(
                    variant=variant,
                    set_name=set_name,
                    draw=draw,
                    column=column,
                    row_type=row_type,
                )
                box_key = BoxKey(
                    variant=variant,
                    set_name=set_name,
                    draw=draw,
                    column=column,
                )
                cell = CellEvidence(
                    key=cell_key,
                    raw=raw_value,
                    digits=digits,
                    hot_level=hot_level,
                )
                box = boxes.get(box_key)
                if not box:
                    box = BoxEvidence(key=box_key)
                    boxes[box_key] = box
                box.cells[row_type] = cell

    for box in boxes.values():
        rows = sorted(box.cells.keys(), key=_row_order)
        # Keep DRAW_DATA (if present) at the front but do not treat as reduction row.
        reduction_rows = [r for r in rows if _is_reduction_row(r)]
        non_reduction = [r for r in rows if not _is_reduction_row(r)]
        box.row_order = non_reduction + reduction_rows

    return VtracGrid(boxes=boxes, raw_tables=dict(tables))
