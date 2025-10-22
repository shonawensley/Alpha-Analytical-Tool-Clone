"""
Adapters for building engine inputs from combined tables and writing outputs.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple, Set

import pandas as pd

from utils.path_handler import get_analysis_output_dir, get_tables_output_dir

from .types import COLUMN_LABELS, EngineInput, EngineOutput, IndexScore, PatternsGrid, SectionData, Cell, RINGS, SECTIONS, SETS

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


_VTRAC_CLASS_MAP = {
    "0": "1",
    "5": "1",
    "1": "2",
    "6": "2",
    "2": "3",
    "7": "3",
    "3": "4",
    "8": "4",
    "4": "5",
    "9": "5",
}


def _is_three_value_candidate(digits: str) -> bool:
    digits = "".join(ch for ch in str(digits or "") if ch.isdigit())
    if len(digits) < 3:
        return False
    if len(set(digits)) <= 3:
        return True
    classes = {_VTRAC_CLASS_MAP.get(ch) for ch in digits}
    classes.discard(None)
    return len(classes) <= 3


def _vtrac_box_signature(digits: str) -> str:
    digits = "".join(ch for ch in str(digits or "") if ch.isdigit())
    if len(digits) < 3:
        return ""
    counts = Counter(_VTRAC_CLASS_MAP.get(ch) for ch in digits if _VTRAC_CLASS_MAP.get(ch))
    if not counts:
        return ""
    top = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]
    return "V" + "_".join(f"{cls}x{cnt}" for cls, cnt in top)


def _summarise_section(engine_input: EngineInput, section: str) -> dict:
    summary = {
        "hot_count": 0,
        "superhot_count": 0,
        "consensus_col1": False,
        "consensus_col2": False,
        "stable_columns": [],
        "top_box_signatures": [],
        "ring_votes": {},
    }

    target: Optional[SectionData] = None
    for sec in engine_input.sections:
        if sec.section.lower() == section.lower() and sec.set_name.strip().lower() == "set1":
            target = sec
            break
    if not target:
        return summary

    grid: PatternsGrid = target.patterns
    signature_counter: Counter[str] = Counter()
    stable_columns: List[str] = []
    ring_signature_counts = {ring: Counter() for ring in RINGS}

    for ring in RINGS:
        cells = tuple(grid.columns(ring))
        summary["hot_count"] += sum(1 for cell in cells if cell.hot)
        summary["superhot_count"] += sum(1 for cell in cells if cell.superhot)

    for idx, column in enumerate(COLUMN_LABELS):
        column_signatures: List[str] = []
        ring_digits: List[str] = []
        for ring in RINGS:
            cells = tuple(grid.columns(ring))
            cell = cells[idx] if idx < len(cells) else None
            digits = cell.digits if cell else ""
            ring_digits.append(digits)
            if _is_three_value_candidate(digits):
                signature = _vtrac_box_signature(digits)
                if signature:
                    column_signatures.append(signature)
                    ring_signature_counts[ring][signature] += 1
                    signature_counter.update([signature])

        if column == 1:
            summary["consensus_col1"] = all(0 < len(d) < 3 for d in ring_digits)
        if column == 2:
            summary["consensus_col2"] = all(0 < len(d) < 3 for d in ring_digits)

        if column_signatures:
            sig, count = Counter(column_signatures).most_common(1)[0]
            if count >= 3:
                stable_columns.append(str(column))

    summary["stable_columns"] = stable_columns
    summary["top_box_signatures"] = [sig for sig, _ in signature_counter.most_common(12)]
    summary["ring_votes"] = {
        ring: dict(counter.most_common())
        for ring, counter in ring_signature_counts.items()
        if counter
    }
    return summary


def _collect_analyzer_section_metrics(output: Optional[EngineOutput]) -> Dict[str, dict]:
    metrics: Dict[str, dict] = {
        section: {
            "indices_considered": 0,
            "mask_drop_count": 0,
            "reduction_hits": 0,
            "mirror_supported": 0,
            "double_hits": 0,
            "top_straights": [],  # populated later with list[dict]
        }
        for section in SECTIONS
    }
    if not output:
        return metrics

    index_sections: Dict[int, Sequence[str]] = {}
    for score in output.indices_ranked:
        sections = [
            sec for sec in score.evidence.raw.get("sections", []) if sec in SECTIONS
        ]
        index_sections[score.index] = sections
        mask_drop = bool(score.evidence.raw.get("mask_drop"))
        reduction_hits = int(score.evidence.raw.get("reduction_hits", 0))
        mirror_supported = bool(score.evidence.raw.get("mirror_supported"))
        double_hits = int(score.evidence.raw.get("double_hits", 0))

        for section in sections:
            entry = metrics.setdefault(section, {
                "indices_considered": 0,
                "mask_drop_count": 0,
                "reduction_hits": 0,
                "mirror_supported": 0,
                "double_hits": 0,
                "top_straights": [],
            })
            entry["indices_considered"] += 1
            if mask_drop:
                entry["mask_drop_count"] += 1
            entry["reduction_hits"] += reduction_hits
            if mirror_supported:
                entry["mirror_supported"] += 1
            entry["double_hits"] += double_hits

    for candidate in output.straights_ranked:
        sections = index_sections.get(candidate.index, [])
        for section in sections:
            entry = metrics.setdefault(section, {
                "indices_considered": 0,
                "mask_drop_count": 0,
                "reduction_hits": 0,
                "mirror_supported": 0,
                "double_hits": 0,
                "top_straights": [],
            })
            if len(entry["top_straights"]) >= 12:
                continue
            entry["top_straights"].append(
                {
                    "straight": candidate.straight,
                    "score": candidate.score,
                    "index": candidate.index,
                }
            )

    return metrics


def _build_section_summaries(
    engine_input: Optional[EngineInput],
    output: Optional[EngineOutput],
) -> dict:
    summaries: Dict[str, dict] = {
        section: _summarise_section(engine_input, section)
        for section in SECTIONS
    } if engine_input else {section: {} for section in SECTIONS}

    analyzer_metrics = _collect_analyzer_section_metrics(output)
    for section, metrics in analyzer_metrics.items():
        summaries.setdefault(section, {})
        summaries[section]["analyzer_metrics"] = {
            "indices_considered": metrics["indices_considered"],
            "mask_drop_count": metrics["mask_drop_count"],
            "reduction_hits": metrics["reduction_hits"],
            "mirror_supported": metrics["mirror_supported"],
            "double_hits": metrics["double_hits"],
            "top_straights": metrics["top_straights"],
        }
    return summaries


def write_prediction_bundle(
    state: str,
    output: EngineOutput,
    *,
    analysis_root: Optional[Path] = None,
    engine_input: Optional[EngineInput] = None,
) -> Path:
    """
    Persist analyzer output under data/outputs/analysis/vtrac/<STATE>/.
    """

    root = Path(analysis_root or get_analysis_output_dir())
    target_dir = root / "vtrac" / state
    target_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = target_dir / f"{state}_vtrac_enhanced_{timestamp}.json"

    if engine_input is None:
        try:
            engine_input = build_engine_input_from_tables(state)
        except Exception:
            engine_input = None

    section_summaries = _build_section_summaries(engine_input, output)

    top_straights: List[str] = []
    seen_straights: Set[str] = set()
    for candidate in output.straights_ranked:
        if candidate.straight not in seen_straights:
            seen_straights.add(candidate.straight)
            top_straights.append(candidate.straight)
        if len(top_straights) >= 24:
            break

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
        "section_summaries": section_summaries,
        "top_straights": top_straights,
    }

    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return out_path


__all__ = [
    "build_engine_input_from_tables",
    "suggested_mask_digits",
    "write_prediction_bundle",
]
