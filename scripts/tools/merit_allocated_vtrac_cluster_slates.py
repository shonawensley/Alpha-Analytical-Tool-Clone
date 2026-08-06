#!/usr/bin/env python3
"""Winner-blind merit allocation across lingering VTRAC clusters.

This module reads frozen predictive pattern tables directly. It deliberately
keeps pattern rows, Arena evidence, and Aux confirmation in separate score
components. Draw-data rows are never scanned.
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Set,
    Tuple,
)

from modules.vtrac_reference import get_vtrac_index
from modules.vtrac_straight_map import ordered_vcode_for_combo, vstraight_lane_for_vcode
from scripts.tools.compact_candidate_slates import (
    EXPERIMENTAL_STATUS,
    assess_input_safety,
    canonicalize,
    input_receipt,
    normalize_pick3,
    now_iso,
    straight_equivalent_cost,
    validate_artifact_alignment,
    write_json,
)


SCHEMA_VERSION = "merit_allocated_vtrac_cluster_slate_v1"
ARTIFACT_TYPE = "merit_allocated_vtrac_cluster_slate"
PATTERN_ROWS = ("R2", "R4", "R6", "R8")
COLUMN_ORDER = ("C7", "C6", "C5", "C4", "C3", "C2", "C1")
AUX_SOURCE_TYPES = {"positional", "blackapple", "due_double", "profit_alert"}

STRUCTURAL_WEIGHTS: Dict[str, float] = {
    "strict_cell_count": 12.0,
    "strict_occurrences": 3.0,
    "vertical_boxes_2plus": 8.0,
    "vertical_boxes_3plus": 8.0,
    "vertical_boxes_4rows": 9.0,
    "horizontal_multi_column_groups": 10.0,
    "set1_cells": 8.0,
    "c1_c2_cells": 7.0,
    "short_cell_hits": 5.0,
    "long_string_cell_hits": 5.0,
    "variant_count": 4.0,
    "set_count": 3.0,
    "row_count": 3.0,
    "top_canonical_cell_count": 8.0,
    "repeated_canonical_count": 7.0,
}

BOX_SOURCE_BONUS: Dict[str, float] = {
    "arena_dominant": 2.5,
    "arena_context_reinforced": 2.0,
    "arena_watchlist": 3.0,
    "arena_example": 1.5,
    "sandbox_primary": 2.5,
    "sandbox_secondary": 1.0,
    "sandbox_survivor": 2.8,
    "sandbox_boxed_seed": 3.0,
    "candidate_universe": 1.0,
    "positional": 1.5,
    "blackapple": 1.2,
    "due_double": 1.4,
    "profit_alert": 1.4,
}

STRAIGHT_SOURCE_BONUS: Dict[str, float] = {
    "arena_example": 1.5,
    "sandbox_straight_seed": 3.5,
    "candidate_universe": 1.0,
    "positional": 3.0,
    "blackapple": 0.8,
    "due_double": 1.0,
    "profit_alert": 1.0,
}


def _digits_only(value: Any) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _triples(value: Any) -> List[str]:
    digits = _digits_only(value)
    return [digits[index : index + 3] for index in range(max(0, len(digits) - 2))]


def _value_stats() -> Dict[str, Any]:
    return {
        "cells": set(),
        "occurrences": 0,
        "variants": set(),
        "sets": set(),
        "rows": set(),
        "columns": set(),
        "set1_cells": set(),
        "c1_c2_cells": set(),
        "short_cells": set(),
        "long_cells": set(),
    }


def _profile(index: int) -> Dict[str, Any]:
    return {
        "vtrac_index": int(index),
        "cells": set(),
        "occurrences": 0,
        "variants": set(),
        "sets": set(),
        "rows": set(),
        "columns": set(),
        "set1_cells": set(),
        "c1_c2_cells": set(),
        "short_cells": set(),
        "terminal_short_cells": set(),
        "long_cells": set(),
        "vertical_groups": defaultdict(set),
        "horizontal_groups": defaultdict(set),
        "canonicals": defaultdict(_value_stats),
        "literals": defaultdict(_value_stats),
        "vcodes": defaultdict(_value_stats),
        "examples": [],
    }


def _external_row(index: int) -> Dict[str, Any]:
    return {
        "vtrac_index": int(index),
        "arena_rank": None,
        "arena_support_count": 0,
        "arena_string_source_count": 0,
        "arena_context_source_count": 0,
        "arena_score_total": 0.0,
        "arena_watchlist_rank": None,
        "sandbox_vtrac_support": 0,
        "cluster_sources": set(),
        "aux_types": set(),
        "box_candidates": defaultdict(lambda: {"sources": set(), "strength": 0.0}),
        "straight_candidates": defaultdict(lambda: {"sources": set(), "strength": 0.0}),
    }


def iter_pattern_cells(
    tables: Mapping[str, Any],
    *,
    target_period: str = "Day",
) -> Iterator[Dict[str, str]]:
    """Yield only R2/R4/R6/R8 cells from raw predictive table JSON."""

    sections = tables.get("sections") if isinstance(tables.get("sections"), Mapping) else {}
    period = str(target_period or "Day")
    variants = ("Midday", "Evening", "Combined") if period == "Day" else (period,)
    for variant in variants:
        section = sections.get(variant)
        if not isinstance(section, Mapping):
            continue
        sets = section.get("sets") if isinstance(section.get("sets"), Mapping) else {}
        for set_name, draws in sets.items():
            if not isinstance(draws, Mapping):
                continue
            for draw_name, draw_payload in draws.items():
                if not isinstance(draw_payload, Mapping):
                    continue
                rows = (
                    draw_payload.get("pattern_variations")
                    if isinstance(draw_payload.get("pattern_variations"), Mapping)
                    else {}
                )
                for row_name in PATTERN_ROWS:
                    values = rows.get(row_name)
                    if not isinstance(values, Sequence) or isinstance(values, (str, bytes)):
                        continue
                    for offset, raw_value in enumerate(values[: len(COLUMN_ORDER)]):
                        column = COLUMN_ORDER[offset]
                        yield {
                            "variant": str(variant),
                            "set": str(set_name),
                            "draw": str(draw_name),
                            "row": str(row_name),
                            "column": column,
                            "text": str(raw_value or ""),
                            "cell_id": (
                                f"{variant}|{set_name}|{draw_name}|{row_name}|{column}"
                            ),
                        }


def scan_pattern_tables(
    tables: Mapping[str, Any],
    *,
    target_period: str = "Day",
) -> Dict[int, Dict[str, Any]]:
    """Build raw, winner-independent VTRAC cluster profiles."""

    profiles: Dict[int, Dict[str, Any]] = {}
    for cell in iter_pattern_cells(tables, target_period=target_period):
        literals = [literal for literal in _triples(cell["text"]) if normalize_pick3(literal)]
        if not literals:
            continue
        by_index: Dict[int, List[str]] = defaultdict(list)
        for literal in literals:
            index = get_vtrac_index(literal)
            if index is not None:
                by_index[int(index)].append(literal)

        digits_length = len(_digits_only(cell["text"]))
        # Six-or-fewer digits corresponds to the reduced survivor/near-survivor
        # band used by the existing string-table review notes.
        is_short = digits_length <= 6
        is_long = digits_length >= 8
        for index, index_literals in by_index.items():
            row = profiles.setdefault(index, _profile(index))
            cell_id = cell["cell_id"]
            row["cells"].add(cell_id)
            row["occurrences"] += len(index_literals)
            row["variants"].add(cell["variant"])
            row["sets"].add(cell["set"])
            row["rows"].add(cell["row"])
            row["columns"].add(cell["column"])
            if cell["set"] == "Set1":
                row["set1_cells"].add(cell_id)
            if cell["column"] in {"C1", "C2"}:
                row["c1_c2_cells"].add(cell_id)
            if is_short:
                row["short_cells"].add(cell_id)
                if cell["column"] in {"C1", "C2"}:
                    row["terminal_short_cells"].add(cell_id)
            if is_long:
                row["long_cells"].add(cell_id)

            vertical_key = (
                cell["variant"],
                cell["set"],
                cell["draw"],
                cell["column"],
            )
            horizontal_key = (
                cell["variant"],
                cell["set"],
                cell["draw"],
                cell["row"],
            )
            row["vertical_groups"][vertical_key].add(cell["row"])
            row["horizontal_groups"][horizontal_key].add(cell["column"])

            literal_counts = Counter(index_literals)
            for literal, count in literal_counts.items():
                _update_value_stats(
                    row["literals"][literal],
                    cell=cell,
                    cell_id=cell_id,
                    occurrences=count,
                    is_short=is_short,
                    is_long=is_long,
                )
                canonical = canonicalize(literal)
                _update_value_stats(
                    row["canonicals"][canonical],
                    cell=cell,
                    cell_id=cell_id,
                    occurrences=count,
                    is_short=is_short,
                    is_long=is_long,
                )
                vcode = ordered_vcode_for_combo(literal)
                if vcode:
                    _update_value_stats(
                        row["vcodes"][vcode],
                        cell=cell,
                        cell_id=cell_id,
                        occurrences=count,
                        is_short=is_short,
                        is_long=is_long,
                    )

            if len(row["examples"]) < 12:
                row["examples"].append(
                    {
                        "variant": cell["variant"],
                        "set": cell["set"],
                        "draw": cell["draw"],
                        "row": cell["row"],
                        "column": cell["column"],
                        "text": cell["text"],
                        "literals": sorted(literal_counts),
                    }
                )
    return profiles


def _update_value_stats(
    stats: MutableMapping[str, Any],
    *,
    cell: Mapping[str, str],
    cell_id: str,
    occurrences: int,
    is_short: bool,
    is_long: bool,
) -> None:
    stats["cells"].add(cell_id)
    stats["occurrences"] += int(occurrences)
    stats["variants"].add(cell["variant"])
    stats["sets"].add(cell["set"])
    stats["rows"].add(cell["row"])
    stats["columns"].add(cell["column"])
    if cell["set"] == "Set1":
        stats["set1_cells"].add(cell_id)
    if cell["column"] in {"C1", "C2"}:
        stats["c1_c2_cells"].add(cell_id)
    if is_short:
        stats["short_cells"].add(cell_id)
    if is_long:
        stats["long_cells"].add(cell_id)


def _external(
    external: MutableMapping[int, Dict[str, Any]],
    index: Any,
) -> Optional[Dict[str, Any]]:
    try:
        numeric = int(index)
    except (TypeError, ValueError):
        return None
    if numeric <= 0:
        return None
    return external.setdefault(numeric, _external_row(numeric))


def _add_box_external(
    external: MutableMapping[int, Dict[str, Any]],
    value: Any,
    *,
    source: str,
    strength: float = 1.0,
    aux_type: str = "",
) -> None:
    canonical = canonicalize(value)
    index = get_vtrac_index(canonical)
    row = _external(external, index)
    if row is None or not canonical:
        return
    candidate = row["box_candidates"][canonical]
    candidate["sources"].add(str(source))
    candidate["strength"] = max(float(candidate["strength"]), float(strength))
    row["cluster_sources"].add(str(source))
    if aux_type in AUX_SOURCE_TYPES:
        row["aux_types"].add(aux_type)


def _add_straight_external(
    external: MutableMapping[int, Dict[str, Any]],
    value: Any,
    *,
    source: str,
    strength: float = 1.0,
    aux_type: str = "",
) -> None:
    literal = normalize_pick3(value)
    index = get_vtrac_index(literal)
    row = _external(external, index)
    if row is None or not literal:
        return
    candidate = row["straight_candidates"][literal]
    candidate["sources"].add(str(source))
    candidate["strength"] = max(float(candidate["strength"]), float(strength))
    row["cluster_sources"].add(str(source))
    if aux_type in AUX_SOURCE_TYPES:
        row["aux_types"].add(aux_type)
    _add_box_external(
        external,
        literal,
        source=source,
        strength=strength,
        aux_type=aux_type,
    )


def collect_external_evidence(
    *,
    candidate_universe: Mapping[str, Any],
    aggregated_arena: Optional[Mapping[str, Any]] = None,
    translation_sandbox: Optional[Mapping[str, Any]] = None,
    aux_summary: Optional[Mapping[str, Any]] = None,
) -> Dict[int, Dict[str, Any]]:
    """Collect bounded Arena, Sandbox, CU, and Aux receipts by VTRAC index."""

    external: Dict[int, Dict[str, Any]] = {}
    arena = aggregated_arena if isinstance(aggregated_arena, Mapping) else {}
    synthesis = (
        arena.get("arena_synthesis")
        if isinstance(arena.get("arena_synthesis"), Mapping)
        else {}
    )

    for rank, item in enumerate(synthesis.get("dominant_vtrac_indices") or [], start=1):
        if not isinstance(item, Mapping):
            continue
        row = _external(external, item.get("value"))
        if row is None:
            continue
        row["arena_rank"] = rank
        row["arena_support_count"] = int(item.get("support_count") or 0)
        row["arena_string_source_count"] = int(item.get("string_source_count") or 0)
        row["arena_context_source_count"] = int(item.get("context_source_count") or 0)
        row["arena_score_total"] = float(item.get("score_total") or 0.0)
        row["cluster_sources"].add(f"arena_vtrac_rank:{rank}")
        for literal in item.get("example_literals") or []:
            _add_straight_external(
                external,
                literal,
                source="arena_example",
                strength=1.0,
            )

    for rank, item in enumerate(synthesis.get("vtrac_literal_watchlist") or [], start=1):
        if not isinstance(item, Mapping):
            continue
        row = _external(external, item.get("vtrac_index"))
        if row is None:
            continue
        row["arena_watchlist_rank"] = rank
        row["cluster_sources"].add(f"arena_watchlist_rank:{rank}")
        for value in item.get("candidate_canonicals") or []:
            _add_box_external(
                external,
                value,
                source="arena_watchlist",
                strength=max(0.5, 2.0 - ((rank - 1) * 0.15)),
            )
        for literal in item.get("example_literals") or []:
            _add_straight_external(
                external,
                literal,
                source="arena_example",
                strength=1.0,
            )

    for key, source in (
        ("dominant_canonicals", "arena_dominant"),
        ("context_reinforced_canonicals", "arena_context_reinforced"),
    ):
        for rank, item in enumerate(synthesis.get(key) or [], start=1):
            value = item.get("value") if isinstance(item, Mapping) else item
            _add_box_external(
                external,
                value,
                source=source,
                strength=max(0.5, 2.0 - ((rank - 1) * 0.1)),
            )
            if isinstance(item, Mapping):
                for literal in item.get("example_literals") or []:
                    _add_straight_external(
                        external,
                        literal,
                        source="arena_example",
                        strength=1.0,
                    )

    sandbox = translation_sandbox if isinstance(translation_sandbox, Mapping) else {}
    brain1 = sandbox.get("brain1_core") if isinstance(sandbox.get("brain1_core"), Mapping) else {}
    hypotheses = (
        sandbox.get("sandbox_hypotheses")
        if isinstance(sandbox.get("sandbox_hypotheses"), Mapping)
        else {}
    )
    brain2 = (
        sandbox.get("brain2_context")
        if isinstance(sandbox.get("brain2_context"), Mapping)
        else {}
    )

    for key, source in (
        ("dominant_canonicals", "sandbox_primary"),
        ("context_reinforced_canonicals", "sandbox_primary"),
        ("secondary_canonicals", "sandbox_secondary"),
        ("survivor_frontier_canonicals", "sandbox_survivor"),
        ("survivor_last_remaining_canonicals", "sandbox_survivor"),
    ):
        for rank, value in enumerate(brain1.get(key) or [], start=1):
            _add_box_external(
                external,
                value,
                source=source,
                strength=max(0.5, 2.0 - ((rank - 1) * 0.08)),
            )

    for item in hypotheses.get("diagnostic_vt_box_seed") or []:
        if not isinstance(item, Mapping):
            continue
        row = _external(external, item.get("value"))
        if row is None:
            continue
        row["sandbox_vtrac_support"] = max(
            int(row["sandbox_vtrac_support"]),
            int(item.get("support_count") or 0),
        )
        row["cluster_sources"].add("sandbox_vtrac_seed")

    for item in hypotheses.get("diagnostic_boxed_seed") or []:
        if not isinstance(item, Mapping):
            continue
        _add_box_external(
            external,
            item.get("value"),
            source="sandbox_boxed_seed",
            strength=float(item.get("support_count") or 0.0),
        )

    for item in hypotheses.get("diagnostic_straight_seed") or []:
        if not isinstance(item, Mapping):
            continue
        _add_straight_external(
            external,
            item.get("value"),
            source="sandbox_straight_seed",
            strength=float(item.get("support_count") or 0.0),
        )

    _collect_brain2_aux(external, brain2)
    _collect_candidate_universe(external, candidate_universe)
    _collect_direct_aux(external, aux_summary)
    return external


def _collect_brain2_aux(
    external: MutableMapping[int, Dict[str, Any]],
    brain2: Mapping[str, Any],
) -> None:
    for item in brain2.get("positional_shortlist_top") or []:
        if not isinstance(item, Mapping):
            continue
        _add_straight_external(
            external,
            item.get("combo"),
            source="positional",
            strength=float(item.get("score") or 0.0),
            aux_type="positional",
        )
    for key, source, aux_type in (
        ("blackapple_recommended_canonicals", "blackapple", "blackapple"),
        ("due_double_example_canonicals", "due_double", "due_double"),
        ("profit_alert_implied_canonicals", "profit_alert", "profit_alert"),
    ):
        for value in brain2.get(key) or []:
            _add_box_external(
                external,
                value,
                source=source,
                strength=1.0,
                aux_type=aux_type,
            )


def _collect_candidate_universe(
    external: MutableMapping[int, Dict[str, Any]],
    candidate_universe: Mapping[str, Any],
) -> None:
    for pack in candidate_universe.get("packs") or []:
        if not isinstance(pack, Mapping):
            continue
        for value in pack.get("canonicals") or []:
            _add_box_external(
                external,
                value,
                source="candidate_universe",
                strength=1.0,
            )
        for value in pack.get("combos") or []:
            _add_straight_external(
                external,
                value,
                source="candidate_universe",
                strength=1.0,
            )


def _collect_direct_aux(
    external: MutableMapping[int, Dict[str, Any]],
    aux_summary: Optional[Mapping[str, Any]],
) -> None:
    if not isinstance(aux_summary, Mapping):
        return
    positional = (
        aux_summary.get("positional")
        if isinstance(aux_summary.get("positional"), Mapping)
        else {}
    )
    shortlist = (
        positional.get("shortlist_report")
        if isinstance(positional.get("shortlist_report"), Mapping)
        else {}
    )
    for item in shortlist.get("candidates") or []:
        if not isinstance(item, Mapping):
            continue
        _add_straight_external(
            external,
            item.get("combo"),
            source="positional",
            strength=float(item.get("score") or 0.0),
            aux_type="positional",
        )

    blackapple = (
        aux_summary.get("blackapple")
        if isinstance(aux_summary.get("blackapple"), Mapping)
        else {}
    )
    top_by_variant = (
        blackapple.get("top_by_variant")
        if isinstance(blackapple.get("top_by_variant"), Mapping)
        else {}
    )
    for rows in top_by_variant.values():
        for item in rows or []:
            if not isinstance(item, Mapping):
                continue
            _add_box_external(
                external,
                item.get("combo"),
                source="blackapple",
                strength=float(item.get("score") or 0.0),
                aux_type="blackapple",
            )


def _count_vertical_groups(groups: Mapping[Any, Set[str]], minimum: int) -> int:
    return sum(1 for values in groups.values() if len(values) >= minimum)


def _count_horizontal_groups(groups: Mapping[Any, Set[str]]) -> int:
    return sum(1 for values in groups.values() if len(values) >= 2)


def _raw_metrics(profile: Mapping[str, Any]) -> Dict[str, int]:
    canonical_cells = [len(stats["cells"]) for stats in profile["canonicals"].values()]
    return {
        "strict_cell_count": len(profile["cells"]),
        "strict_occurrences": int(profile["occurrences"]),
        "variant_count": len(profile["variants"]),
        "set_count": len(profile["sets"]),
        "row_count": len(profile["rows"]),
        "column_count": len(profile["columns"]),
        "set1_cells": len(profile["set1_cells"]),
        "c1_c2_cells": len(profile["c1_c2_cells"]),
        "short_cell_hits": len(profile["short_cells"]),
        "terminal_short_cell_hits": len(profile["terminal_short_cells"]),
        "long_string_cell_hits": len(profile["long_cells"]),
        "vertical_boxes_2plus": _count_vertical_groups(profile["vertical_groups"], 2),
        "vertical_boxes_3plus": _count_vertical_groups(profile["vertical_groups"], 3),
        "vertical_boxes_4rows": _count_vertical_groups(profile["vertical_groups"], 4),
        "horizontal_multi_column_groups": _count_horizontal_groups(profile["horizontal_groups"]),
        "canonical_count": len(profile["canonicals"]),
        "top_canonical_cell_count": max(canonical_cells, default=0),
        "repeated_canonical_count": sum(1 for value in canonical_cells if value >= 3),
    }


def _normalized(value: float, maximum: float) -> float:
    if maximum <= 0:
        return 0.0
    return max(0.0, min(1.0, float(value) / float(maximum)))


def score_clusters(
    profiles: Mapping[int, Mapping[str, Any]],
    external: Mapping[int, Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    """Score clusters while retaining a fully auditable component vector."""

    metrics_by_index = {int(index): _raw_metrics(profile) for index, profile in profiles.items()}
    maxima = {
        metric: max((values.get(metric, 0) for values in metrics_by_index.values()), default=0)
        for metric in STRUCTURAL_WEIGHTS
    }
    arena_maxima = {
        key: max(
            (
                float((external.get(index) or {}).get(key) or 0.0)
                for index in profiles
            ),
            default=0.0,
        )
        for key in (
            "arena_support_count",
            "arena_string_source_count",
            "arena_context_source_count",
            "sandbox_vtrac_support",
        )
    }

    rows: List[Dict[str, Any]] = []
    for index in sorted(profiles):
        metrics = metrics_by_index[index]
        structural_components = {
            metric: round(
                weight * _normalized(metrics.get(metric, 0), maxima.get(metric, 0)),
                6,
            )
            for metric, weight in STRUCTURAL_WEIGHTS.items()
        }
        structural_score = sum(structural_components.values())
        ext = external.get(index) or {}
        arena_rank = ext.get("arena_rank") or ext.get("arena_watchlist_rank")
        arena_components = {
            "rank": round(6.0 / math.sqrt(float(arena_rank)), 6) if arena_rank else 0.0,
            "support": round(
                4.0
                * _normalized(
                    ext.get("arena_support_count") or 0,
                    arena_maxima["arena_support_count"],
                ),
                6,
            ),
            "string_sources": round(
                4.0
                * _normalized(
                    ext.get("arena_string_source_count") or 0,
                    arena_maxima["arena_string_source_count"],
                ),
                6,
            ),
            "context_sources": round(
                2.0
                * _normalized(
                    ext.get("arena_context_source_count") or 0,
                    arena_maxima["arena_context_source_count"],
                ),
                6,
            ),
            "watchlist": 2.0 if ext.get("arena_watchlist_rank") else 0.0,
            "sandbox_vtrac": round(
                2.0
                * _normalized(
                    ext.get("sandbox_vtrac_support") or 0,
                    arena_maxima["sandbox_vtrac_support"],
                ),
                6,
            ),
        }
        arena_score = sum(arena_components.values())
        aux_types = sorted(str(value) for value in (ext.get("aux_types") or set()))
        aux_score = min(10.0, 2.5 * len(aux_types))
        dimensions = {
            "vertical": metrics["vertical_boxes_2plus"] >= 2,
            "horizontal": metrics["horizontal_multi_column_groups"] >= 2,
            "survivor_short": metrics["short_cell_hits"] >= 3,
            "long_string": metrics["long_string_cell_hits"] >= 3,
            "current_progression": (
                metrics["set1_cells"] >= 5 and metrics["c1_c2_cells"] >= 2
            ),
        }
        breadth = bool(
            metrics["variant_count"] >= 2
            or metrics["set_count"] >= 2
            or int(ext.get("arena_string_source_count") or 0) >= 2
        )
        absolute_eligible = bool(
            metrics["strict_cell_count"] >= 8
            and sum(1 for value in dimensions.values() if value) >= 2
            and breadth
        )
        rows.append(
            {
                "vtrac_index": index,
                "metrics": metrics,
                "structural_components": structural_components,
                "structural_score": round(structural_score, 6),
                "arena_components": arena_components,
                "arena_score": round(arena_score, 6),
                "aux_types": aux_types,
                "aux_score": round(aux_score, 6),
                "total_merit": round(structural_score + arena_score + aux_score, 6),
                "structural_dimensions": dimensions,
                "structural_dimension_count": sum(
                    1 for value in dimensions.values() if value
                ),
                "breadth_gate": breadth,
                "absolute_eligible": absolute_eligible,
                "eligible": False,
                "eligibility_reasons": [],
                "arena_rank": ext.get("arena_rank"),
                "arena_watchlist_rank": ext.get("arena_watchlist_rank"),
                "arena_support_count": int(ext.get("arena_support_count") or 0),
                "arena_string_source_count": int(
                    ext.get("arena_string_source_count") or 0
                ),
                "arena_context_source_count": int(
                    ext.get("arena_context_source_count") or 0
                ),
                "sandbox_vtrac_support": int(
                    ext.get("sandbox_vtrac_support") or 0
                ),
                "cluster_sources": sorted(
                    str(value) for value in (ext.get("cluster_sources") or set())
                ),
            }
        )

    leader_structural = max((row["structural_score"] for row in rows), default=0.0)
    leader_total = max((row["total_merit"] for row in rows), default=0.0)
    for row in rows:
        reasons: List[str] = []
        if not row["absolute_eligible"]:
            reasons.append("absolute_structural_gate_failed")
        if row["structural_score"] < (leader_structural * 0.25):
            reasons.append("relative_structural_floor_failed")
        if row["total_merit"] < (leader_total * 0.35):
            reasons.append("relative_total_merit_floor_failed")
        row["eligible"] = not reasons
        row["eligibility_reasons"] = reasons or ["eligible"]

    rows.sort(key=lambda row: (-float(row["total_merit"]), int(row["vtrac_index"])))
    for rank, row in enumerate(rows, start=1):
        row["merit_rank"] = rank
    return rows


def select_clusters(
    cluster_rows: Sequence[Mapping[str, Any]],
    *,
    maximum_clusters: int = 4,
) -> List[int]:
    eligible = [dict(row) for row in cluster_rows if row.get("eligible")]
    if not eligible or maximum_clusters <= 0:
        return []

    selected: List[int] = []

    def add(index: int) -> None:
        if index not in selected and len(selected) < maximum_clusters:
            selected.append(index)

    add(int(eligible[0]["vtrac_index"]))
    arena_protected = sorted(
        (
            row
            for row in eligible
            if row.get("arena_rank") is not None and int(row["arena_rank"]) <= 3
        ),
        key=lambda row: (int(row["arena_rank"]), -float(row["total_merit"])),
    )
    for row in arena_protected:
        add(int(row["vtrac_index"]))
    for row in eligible:
        add(int(row["vtrac_index"]))
    return selected


def _stats_receipt(stats: Optional[Mapping[str, Any]]) -> Dict[str, Any]:
    stats = stats or {}
    return {
        "pattern_cell_count": len(stats.get("cells") or set()),
        "pattern_occurrences": int(stats.get("occurrences") or 0),
        "variant_count": len(stats.get("variants") or set()),
        "set_count": len(stats.get("sets") or set()),
        "row_count": len(stats.get("rows") or set()),
        "column_count": len(stats.get("columns") or set()),
        "set1_cell_count": len(stats.get("set1_cells") or set()),
        "c1_c2_cell_count": len(stats.get("c1_c2_cells") or set()),
        "short_cell_count": len(stats.get("short_cells") or set()),
        "long_cell_count": len(stats.get("long_cells") or set()),
    }


def build_box_candidate_pools(
    profiles: Mapping[int, Mapping[str, Any]],
    external: Mapping[int, Mapping[str, Any]],
    selected_indices: Sequence[int],
    cluster_lookup: Mapping[int, Mapping[str, Any]],
) -> Dict[int, List[Dict[str, Any]]]:
    pools: Dict[int, List[Dict[str, Any]]] = {}
    for index in selected_indices:
        profile = profiles[index]
        ext = external.get(index) or {}
        direct = profile["canonicals"]
        external_candidates = ext.get("box_candidates") or {}
        values = set(direct) | set(external_candidates)
        max_cells = max((len(stats["cells"]) for stats in direct.values()), default=0)
        max_occurrences = max(
            (int(stats["occurrences"]) for stats in direct.values()),
            default=0,
        )
        max_set1 = max(
            (len(stats["set1_cells"]) for stats in direct.values()),
            default=0,
        )
        max_c12 = max(
            (len(stats["c1_c2_cells"]) for stats in direct.values()),
            default=0,
        )
        rows: List[Dict[str, Any]] = []
        for canonical in sorted(values):
            if get_vtrac_index(canonical) != index:
                continue
            stats = direct.get(canonical)
            receipt = _stats_receipt(stats)
            external_row = external_candidates.get(canonical) or {}
            sources = sorted(str(value) for value in (external_row.get("sources") or set()))
            external_bonus = min(
                8.0,
                sum(BOX_SOURCE_BONUS.get(source, 0.5) for source in set(sources)),
            )
            score = (
                12.0 * _normalized(receipt["pattern_cell_count"], max_cells)
                + 4.0
                * _normalized(receipt["pattern_occurrences"], max_occurrences)
                + 3.0 * _normalized(receipt["variant_count"], 3)
                + 3.0 * _normalized(receipt["set1_cell_count"], max_set1)
                + 3.0 * _normalized(receipt["c1_c2_cell_count"], max_c12)
                + external_bonus
            )
            is_direct = receipt["pattern_cell_count"] > 0
            if not is_direct and not sources:
                continue
            rows.append(
                {
                    "canonical": canonical,
                    "vtrac_index": index,
                    "score": round(score, 6),
                    "cluster_merit": float(cluster_lookup[index]["total_merit"]),
                    "is_direct_pattern": is_direct,
                    "pattern_receipt": receipt,
                    "external_sources": sources,
                    "external_strength": round(
                        float(external_row.get("strength") or 0.0),
                        6,
                    ),
                    "straight_equivalent_cost": straight_equivalent_cost(canonical),
                }
            )
        rows.sort(key=lambda row: (-float(row["score"]), str(row["canonical"])))
        pools[index] = rows
    return pools


def _next_unselected(
    rows: Sequence[Mapping[str, Any]],
    selected_values: Set[str],
    *,
    direct_only: bool,
    value_key: str,
) -> Optional[Dict[str, Any]]:
    for row in rows:
        value = str(row.get(value_key) or "")
        if not value or value in selected_values:
            continue
        if direct_only and not bool(
            row.get("is_direct_pattern") or row.get("has_strong_external_order")
        ):
            continue
        return dict(row)
    return None


def allocate_candidates(
    pools: Mapping[int, Sequence[Mapping[str, Any]]],
    selected_indices: Sequence[int],
    cluster_lookup: Mapping[int, Mapping[str, Any]],
    *,
    width_cap: int,
    per_cluster_cap: int = 6,
    base_slots: int = 2,
    minimum_marginal_score: float = 3.0,
    value_key: str,
) -> Tuple[List[Dict[str, Any]], Dict[int, Dict[str, Any]]]:
    selected_rows: List[Dict[str, Any]] = []
    selected_values: Set[str] = set()
    counts: Counter[int] = Counter()
    leader_merit = max(
        (float(cluster_lookup[index]["total_merit"]) for index in selected_indices),
        default=0.0,
    )

    def append(row: Dict[str, Any], stage: str) -> None:
        index = int(row["vtrac_index"])
        value = str(row[value_key])
        if value in selected_values or counts[index] >= per_cluster_cap:
            return
        row["slot"] = len(selected_rows) + 1
        row["allocation_stage"] = stage
        selected_rows.append(row)
        selected_values.add(value)
        counts[index] += 1

    for _ in range(base_slots):
        for index in selected_indices:
            if len(selected_rows) >= width_cap or counts[index] >= per_cluster_cap:
                continue
            row = _next_unselected(
                pools.get(index) or [],
                selected_values,
                direct_only=True,
                value_key=value_key,
            )
            if row is not None:
                append(row, "protected_cluster_base")

    while len(selected_rows) < width_cap:
        options: List[Tuple[float, int, Dict[str, Any]]] = []
        for index in selected_indices:
            if counts[index] >= per_cluster_cap:
                continue
            row = _next_unselected(
                pools.get(index) or [],
                selected_values,
                direct_only=False,
                value_key=value_key,
            )
            if row is None:
                continue
            cluster_factor = (
                0.65
                + 0.35
                * _normalized(
                    float(cluster_lookup[index]["total_merit"]),
                    leader_merit,
                )
            )
            marginal = float(row.get("score") or 0.0) * cluster_factor
            if marginal >= minimum_marginal_score:
                options.append((marginal, index, row))
        if not options:
            break
        options.sort(
            key=lambda item: (
                -item[0],
                int(selected_indices.index(item[1])),
                str(item[2].get(value_key) or ""),
            )
        )
        append(options[0][2], "marginal_merit")

    allocation = {
        index: {
            "vtrac_index": index,
            "allocated_count": counts[index],
            "unused_cluster_capacity": max(0, per_cluster_cap - counts[index]),
            "cluster_merit": float(cluster_lookup[index]["total_merit"]),
        }
        for index in selected_indices
    }
    return selected_rows, allocation


def build_straight_candidate_pools(
    profiles: Mapping[int, Mapping[str, Any]],
    external: Mapping[int, Mapping[str, Any]],
    selected_indices: Sequence[int],
    cluster_lookup: Mapping[int, Mapping[str, Any]],
    boxed_candidates: Sequence[Mapping[str, Any]],
) -> Dict[int, List[Dict[str, Any]]]:
    selected_boxes: Dict[int, Set[str]] = defaultdict(set)
    box_score: Dict[Tuple[int, str], float] = {}
    for row in boxed_candidates:
        index = int(row["vtrac_index"])
        canonical = canonicalize(row.get("canonical"))
        selected_boxes[index].add(canonical)
        box_score[(index, canonical)] = float(row.get("score") or 0.0)

    pools: Dict[int, List[Dict[str, Any]]] = {}
    for index in selected_indices:
        profile = profiles[index]
        ext = external.get(index) or {}
        raw_literals = profile["literals"]
        raw_vcodes = profile["vcodes"]
        ext_literals = ext.get("straight_candidates") or {}
        candidates: Dict[str, Dict[str, Any]] = {}

        def ensure(literal: str) -> Dict[str, Any]:
            return candidates.setdefault(
                literal,
                {
                    "literal": literal,
                    "canonical": canonicalize(literal),
                    "vtrac_index": index,
                    "ordered_vcode": ordered_vcode_for_combo(literal) or "",
                    "generation_types": set(),
                    "external_sources": set(),
                },
            )

        for literal in raw_literals:
            if canonicalize(literal) not in selected_boxes[index]:
                continue
            ensure(literal)["generation_types"].add("strict_pattern_literal")
        for literal, source_row in ext_literals.items():
            if canonicalize(literal) not in selected_boxes[index]:
                continue
            row = ensure(literal)
            row["generation_types"].add("external_ordered_seed")
            row["external_sources"].update(source_row.get("sources") or set())

        top_vcodes = sorted(
            raw_vcodes.items(),
            key=lambda item: (
                -len(item[1]["cells"]),
                -int(item[1]["occurrences"]),
                str(item[0]),
            ),
        )[:6]
        for canonical in selected_boxes[index]:
            for vcode, _ in top_vcodes:
                for literal in vstraight_lane_for_vcode(vcode):
                    if canonicalize(literal) != canonical:
                        continue
                    row = ensure(literal)
                    row["generation_types"].add("ordered_lane_mate")
                    row.setdefault("lane_parent_vcodes", set()).add(vcode)

        max_literal_cells = max(
            (len(stats["cells"]) for stats in raw_literals.values()),
            default=0,
        )
        max_literal_occ = max(
            (int(stats["occurrences"]) for stats in raw_literals.values()),
            default=0,
        )
        max_vcode_cells = max(
            (len(stats["cells"]) for stats in raw_vcodes.values()),
            default=0,
        )
        max_box_score = max(
            (box_score.get((index, value), 0.0) for value in selected_boxes[index]),
            default=0.0,
        )

        rows: List[Dict[str, Any]] = []
        for literal, candidate in candidates.items():
            stats = raw_literals.get(literal)
            receipt = _stats_receipt(stats)
            vcode = candidate["ordered_vcode"]
            vcode_stats = raw_vcodes.get(vcode)
            vcode_receipt = _stats_receipt(vcode_stats)
            source_row = ext_literals.get(literal) or {}
            candidate["external_sources"].update(source_row.get("sources") or set())
            sources = sorted(str(value) for value in candidate["external_sources"])
            external_bonus = min(
                7.0,
                sum(STRAIGHT_SOURCE_BONUS.get(source, 0.5) for source in set(sources)),
            )
            direct = receipt["pattern_cell_count"] > 0
            score = (
                12.0
                * _normalized(receipt["pattern_cell_count"], max_literal_cells)
                + 4.0
                * _normalized(receipt["pattern_occurrences"], max_literal_occ)
                + 2.0 * _normalized(receipt["variant_count"], 3)
                + 2.0
                * _normalized(
                    receipt["set1_cell_count"],
                    max(
                        (
                            len(value["set1_cells"])
                            for value in raw_literals.values()
                        ),
                        default=0,
                    ),
                )
                + 2.0
                * _normalized(
                    receipt["c1_c2_cell_count"],
                    max(
                        (
                            len(value["c1_c2_cells"])
                            for value in raw_literals.values()
                        ),
                        default=0,
                    ),
                )
                + 6.0
                * _normalized(
                    vcode_receipt["pattern_cell_count"],
                    max_vcode_cells,
                )
                + 5.0
                * _normalized(
                    box_score.get((index, candidate["canonical"]), 0.0),
                    max_box_score,
                )
                + external_bonus
                + (2.0 if direct else -1.0)
            )
            has_strong_external = bool(
                set(sources) & {"sandbox_straight_seed", "positional"}
            )
            rows.append(
                {
                    "literal": literal,
                    "canonical": candidate["canonical"],
                    "vtrac_index": index,
                    "ordered_vcode": vcode,
                    "score": round(max(0.0, score), 6),
                    "cluster_merit": float(cluster_lookup[index]["total_merit"]),
                    "is_direct_pattern": direct,
                    "has_strong_external_order": has_strong_external,
                    "pattern_receipt": receipt,
                    "ordered_vcode_receipt": vcode_receipt,
                    "generation_types": sorted(candidate["generation_types"]),
                    "lane_parent_vcodes": sorted(
                        candidate.get("lane_parent_vcodes") or set()
                    ),
                    "external_sources": sources,
                }
            )
        rows.sort(
            key=lambda row: (
                -float(row["score"]),
                str(row["literal"]),
            )
        )
        pools[index] = rows
    return pools


def _serialize_pattern_cluster(
    profile: Mapping[str, Any],
    cluster_row: Mapping[str, Any],
    *,
    selected: bool,
    selection_reason: str,
) -> Dict[str, Any]:
    top_canonicals = sorted(
        (
            {
                "canonical": canonical,
                **_stats_receipt(stats),
            }
            for canonical, stats in profile["canonicals"].items()
        ),
        key=lambda row: (
            -int(row["pattern_cell_count"]),
            -int(row["pattern_occurrences"]),
            str(row["canonical"]),
        ),
    )[:12]
    top_literals = sorted(
        (
            {
                "literal": literal,
                "canonical": canonicalize(literal),
                "ordered_vcode": ordered_vcode_for_combo(literal),
                **_stats_receipt(stats),
            }
            for literal, stats in profile["literals"].items()
        ),
        key=lambda row: (
            -int(row["pattern_cell_count"]),
            -int(row["pattern_occurrences"]),
            str(row["literal"]),
        ),
    )[:12]
    top_vcodes = sorted(
        (
            {
                "ordered_vcode": vcode,
                **_stats_receipt(stats),
            }
            for vcode, stats in profile["vcodes"].items()
        ),
        key=lambda row: (
            -int(row["pattern_cell_count"]),
            -int(row["pattern_occurrences"]),
            str(row["ordered_vcode"]),
        ),
    )[:12]
    return {
        **dict(cluster_row),
        "selected": selected,
        "selection_reason": selection_reason,
        "top_pattern_canonicals": top_canonicals,
        "top_pattern_literals": top_literals,
        "top_ordered_vcodes": top_vcodes,
        "examples": list(profile.get("examples") or []),
    }


def validate_tables_input(
    *,
    pattern_tables: Mapping[str, Any],
    candidate_universe: Mapping[str, Any],
    tables_path: Optional[Path],
    aux_summary: Optional[Mapping[str, Any]],
    run_mode: str,
) -> None:
    state_name = str(pattern_tables.get("state_name") or "")
    state_key = str(candidate_universe.get("state_key") or "")
    if not state_name or state_name != state_key:
        raise ValueError(
            f"Pattern tables state mismatch: expected {state_key!r}, got {state_name!r}"
        )
    if not isinstance(pattern_tables.get("sections"), Mapping):
        raise ValueError("Pattern tables must contain a sections object")
    if isinstance(aux_summary, Mapping):
        aux_state = str(aux_summary.get("state") or "")
        if aux_state and aux_state != state_key:
            raise ValueError(
                f"Aux summary state mismatch: expected {state_key!r}, got {aux_state!r}"
            )
    if str(run_mode or "").lower() == "shadow" and tables_path is not None:
        lowered_parts = [part.lower() for part in tables_path.resolve().parts]
        if any("winner" in part for part in lowered_parts):
            raise ValueError("Shadow generation rejected winner-side pattern tables")
        if "_predictive" not in tables_path.resolve().parts:
            raise ValueError(
                "Shadow generation requires pattern tables under a _predictive root"
            )


def build_merit_allocated_slate(
    *,
    pattern_tables: Mapping[str, Any],
    candidate_universe: Mapping[str, Any],
    aggregated_arena: Optional[Mapping[str, Any]] = None,
    translation_sandbox: Optional[Mapping[str, Any]] = None,
    aux_summary: Optional[Mapping[str, Any]] = None,
    tables_path: Optional[Path] = None,
    candidate_path: Optional[Path] = None,
    arena_path: Optional[Path] = None,
    sandbox_path: Optional[Path] = None,
    aux_path: Optional[Path] = None,
    repo_root: Optional[Path] = None,
    target_period: str = "Day",
    run_mode: str = "shadow",
    freeze_receipt: str = "",
    maximum_clusters: int = 4,
    width_cap: int = 12,
) -> Dict[str, Any]:
    if not 1 <= int(maximum_clusters) <= 4:
        raise ValueError("maximum_clusters must be between 1 and 4")
    if not 1 <= int(width_cap) <= 12:
        raise ValueError("width_cap must be between 1 and 12")
    validate_artifact_alignment(
        candidate_universe=candidate_universe,
        aggregated_arena=aggregated_arena,
        translation_sandbox=translation_sandbox,
    )
    validate_tables_input(
        pattern_tables=pattern_tables,
        candidate_universe=candidate_universe,
        tables_path=tables_path,
        aux_summary=aux_summary,
        run_mode=run_mode,
    )
    safety = assess_input_safety(
        candidate_universe=candidate_universe,
        aggregated_arena=aggregated_arena,
        translation_sandbox=translation_sandbox,
        candidate_path=candidate_path,
        run_mode=run_mode,
        freeze_receipt=freeze_receipt,
        additional_paths=(tables_path, arena_path, sandbox_path, aux_path),
    )

    profiles = scan_pattern_tables(pattern_tables, target_period=target_period)
    external = collect_external_evidence(
        candidate_universe=candidate_universe,
        aggregated_arena=aggregated_arena,
        translation_sandbox=translation_sandbox,
        aux_summary=aux_summary,
    )
    cluster_rows = score_clusters(profiles, external)
    selected_indices = select_clusters(
        cluster_rows,
        maximum_clusters=int(maximum_clusters),
    )
    cluster_lookup = {
        int(row["vtrac_index"]): row
        for row in cluster_rows
    }
    box_pools = build_box_candidate_pools(
        profiles,
        external,
        selected_indices,
        cluster_lookup,
    )
    boxed, boxed_allocation = allocate_candidates(
        box_pools,
        selected_indices,
        cluster_lookup,
        width_cap=int(width_cap),
        per_cluster_cap=6,
        base_slots=2,
        minimum_marginal_score=3.0,
        value_key="canonical",
    )
    straight_pools = build_straight_candidate_pools(
        profiles,
        external,
        selected_indices,
        cluster_lookup,
        boxed,
    )
    straights, straight_allocation = allocate_candidates(
        straight_pools,
        selected_indices,
        cluster_lookup,
        width_cap=int(width_cap),
        per_cluster_cap=6,
        base_slots=2,
        minimum_marginal_score=3.0,
        value_key="literal",
    )

    selection_reason = {
        index: (
            "arena_top3_structurally_qualified"
            if cluster_lookup[index].get("arena_rank")
            and int(cluster_lookup[index]["arena_rank"]) <= 3
            else "highest_remaining_cluster_merit"
        )
        for index in selected_indices
    }
    cluster_ledger = [
        _serialize_pattern_cluster(
            profiles[int(row["vtrac_index"])],
            row,
            selected=int(row["vtrac_index"]) in selected_indices,
            selection_reason=selection_reason.get(
                int(row["vtrac_index"]),
                "not_selected",
            ),
        )
        for row in cluster_rows
    ]
    state_key = str(candidate_universe.get("state_key") or "")
    results_date = str(candidate_universe.get("results_date") or "")
    return {
        "schema_version": SCHEMA_VERSION,
        "artifact_type": ARTIFACT_TYPE,
        "status": EXPERIMENTAL_STATUS,
        "metadata": {
            "state_key": state_key,
            "results_date": results_date,
            "history_date": str(candidate_universe.get("history_date") or ""),
            "profile": str(candidate_universe.get("profile") or ""),
            "target_period": str(target_period),
            "generated_at": now_iso(),
        },
        "evidence_safety": {
            **safety,
            "pattern_rows_only": True,
            "draw_data_scanned": False,
            "winner_input_accepted": False,
        },
        "source_artifacts": [
            input_receipt(tables_path, "predictive_pattern_tables", repo_root),
            input_receipt(candidate_path, "candidate_universe", repo_root),
            input_receipt(arena_path, "aggregated_arena", repo_root),
            input_receipt(sandbox_path, "translation_sandbox", repo_root),
            input_receipt(aux_path, "aux_summary", repo_root),
        ],
        "allocation_contract": {
            "maximum_clusters": int(maximum_clusters),
            "surface_width_cap": int(width_cap),
            "per_cluster_cap": 6,
            "protected_base_slots_per_cluster": 2,
            "structural_gate_required": True,
            "arena_top3_protection_requires_structural_gate": True,
            "aux_can_create_cluster_eligibility": False,
            "draw_data_used": False,
            "force_fill": False,
            "static_scoreboard_rank_used": False,
            "selected_or_funded": False,
            "structural_weights": dict(STRUCTURAL_WEIGHTS),
        },
        "pattern_scan_receipt": {
            "pattern_cell_count": sum(
                1 for _ in iter_pattern_cells(pattern_tables, target_period=target_period)
            ),
            "cluster_count": len(cluster_rows),
            "eligible_cluster_count": sum(1 for row in cluster_rows if row["eligible"]),
            "selected_cluster_count": len(selected_indices),
            "selected_vtrac_indices": list(selected_indices),
        },
        "cluster_ledger": cluster_ledger,
        "surfaces": {
            "BOXED12": {
                "surface_type": "BOXED_CANONICAL",
                "width_cap": int(width_cap),
                "candidate_count": len(boxed),
                "unused_slots": max(0, int(width_cap) - len(boxed)),
                "straight_equivalent_lines": sum(
                    int(row["straight_equivalent_cost"]) for row in boxed
                ),
                "allocation_by_cluster": [
                    boxed_allocation[index] for index in selected_indices
                ],
                "candidates": boxed,
            },
            "STRAIGHT12": {
                "surface_type": "ORDERED_LITERAL",
                "width_cap": int(width_cap),
                "candidate_count": len(straights),
                "unused_slots": max(0, int(width_cap) - len(straights)),
                "allocation_by_cluster": [
                    straight_allocation[index] for index in selected_indices
                ],
                "candidates": straights,
            },
        },
        "deep_review_mapping": {
            "shared_cluster_ledger_locator": "cluster_ledger",
            "surface_routes": {
                "BOXED12": {
                    "route_family": "BOX_DIVERSIFIED",
                    "generator_identity": (
                        f"{SCHEMA_VERSION}:BOXED12"
                    ),
                    "play_mode": "BOX",
                    "members_locator": "surfaces.BOXED12.candidates[*].canonical",
                    "count_locator": "surfaces.BOXED12.candidate_count",
                    "cost_locator": (
                        "surfaces.BOXED12.straight_equivalent_lines"
                    ),
                    "template_sections": [
                        "D5",
                        "D7",
                        "D7.1",
                        "D10",
                        "E1",
                        "E3",
                        "E4-E5",
                    ],
                },
                "STRAIGHT12": {
                    "route_family": "STR_DIVERSIFIED",
                    "generator_identity": (
                        f"{SCHEMA_VERSION}:STRAIGHT12"
                    ),
                    "play_mode": "STRAIGHT",
                    "members_locator": "surfaces.STRAIGHT12.candidates[*].literal",
                    "count_locator": "surfaces.STRAIGHT12.candidate_count",
                    "template_sections": [
                        "D6",
                        "D7",
                        "D7.1",
                        "D10",
                        "E1",
                        "E3",
                        "E4-E5",
                    ],
                },
            },
            "claim_class_source": "evidence_safety",
            "result_grading_artifact_type": (
                "merit_allocated_vtrac_cluster_slate_grade"
            ),
        },
        "claim_boundary": (
            "Winner-blind experimental shadow source only. It is not selected, "
            "funded, or realized without a separate frozen decision receipt."
        ),
    }


def render_merit_slate_markdown(payload: Mapping[str, Any]) -> str:
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), Mapping) else {}
    safety = (
        payload.get("evidence_safety")
        if isinstance(payload.get("evidence_safety"), Mapping)
        else {}
    )
    receipt = (
        payload.get("pattern_scan_receipt")
        if isinstance(payload.get("pattern_scan_receipt"), Mapping)
        else {}
    )
    selected_text = ", ".join(
        str(value) for value in (receipt.get("selected_vtrac_indices") or [])
    )
    lines: List[str] = [
        "# Merit-Allocated VTRAC Cluster Slate",
        "",
        f"- Status: `{payload.get('status')}`",
        f"- State: `{metadata.get('state_key') or '-'}`",
        f"- Results date: `{metadata.get('results_date') or '-'}`",
        f"- Target period: `{metadata.get('target_period') or '-'}`",
        f"- Timing status: `{safety.get('timing_status') or '-'}`",
        f"- Winner-free input: `{safety.get('winner_free_input')}`",
        f"- Pattern rows only: `{safety.get('pattern_rows_only')}`",
        f"- Draw data scanned: `{safety.get('draw_data_scanned')}`",
        "",
        "> Experimental shadow source only. It is not a selected or funded ticket.",
        "",
        "## Cluster Selection",
        "",
        f"- Clusters scanned: `{receipt.get('cluster_count') or 0}`",
        f"- Eligible clusters: `{receipt.get('eligible_cluster_count') or 0}`",
        f"- Selected indices: `{selected_text or '-'}`",
        "",
        (
            "| Merit rank | VTRAC | Selected | Structural | Arena | Aux | "
            "Total | Cells | Vertical 4 | Horizontal |"
        ),
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in payload.get("cluster_ledger") or []:
        if not isinstance(row, Mapping):
            continue
        metrics = row.get("metrics") if isinstance(row.get("metrics"), Mapping) else {}
        lines.append(
            f"| {row.get('merit_rank')} | {row.get('vtrac_index')} | "
            f"{int(bool(row.get('selected')))} | "
            f"{float(row.get('structural_score') or 0.0):.3f} | "
            f"{float(row.get('arena_score') or 0.0):.3f} | "
            f"{float(row.get('aux_score') or 0.0):.3f} | "
            f"{float(row.get('total_merit') or 0.0):.3f} | "
            f"{metrics.get('strict_cell_count') or 0} | "
            f"{metrics.get('vertical_boxes_4rows') or 0} | "
            f"{metrics.get('horizontal_multi_column_groups') or 0} |"
        )

    surfaces = payload.get("surfaces") if isinstance(payload.get("surfaces"), Mapping) else {}
    for surface_name in ("BOXED12", "STRAIGHT12"):
        surface = (
            surfaces.get(surface_name)
            if isinstance(surfaces.get(surface_name), Mapping)
            else {}
        )
        lines.extend(
            [
                "",
                f"## {surface_name}",
                "",
                f"- Candidate count: `{surface.get('candidate_count') or 0}`",
                f"- Unused slots: `{surface.get('unused_slots') or 0}`",
            ]
        )
        if surface_name == "BOXED12":
            lines.append(
                f"- Straight-equivalent lines: `{surface.get('straight_equivalent_lines') or 0}`"
            )
            lines.extend(
                [
                    "",
                    (
                        "| Slot | Canonical | VTRAC | Score | Cluster merit | "
                        "Direct pattern | Cost | Stage |"
                    ),
                    "|---:|---|---:|---:|---:|---:|---:|---|",
                ]
            )
            for row in surface.get("candidates") or []:
                lines.append(
                    f"| {row.get('slot')} | `{row.get('canonical')}` | "
                    f"{row.get('vtrac_index')} | {float(row.get('score') or 0.0):.3f} | "
                    f"{float(row.get('cluster_merit') or 0.0):.3f} | "
                    f"{int(bool(row.get('is_direct_pattern')))} | "
                    f"{row.get('straight_equivalent_cost') or 0} | "
                    f"{row.get('allocation_stage')} |"
                )
        else:
            lines.extend(
                [
                    "",
                    (
                        "| Slot | Literal | Canonical | Vcode | VTRAC | Score | "
                        "Direct pattern | Origin | Stage |"
                    ),
                    "|---:|---|---|---|---:|---:|---:|---|---|",
                ]
            )
            for row in surface.get("candidates") or []:
                lines.append(
                    f"| {row.get('slot')} | `{row.get('literal')}` | "
                    f"`{row.get('canonical')}` | `{row.get('ordered_vcode')}` | "
                    f"{row.get('vtrac_index')} | {float(row.get('score') or 0.0):.3f} | "
                    f"{int(bool(row.get('is_direct_pattern')))} | "
                    f"{','.join(row.get('generation_types') or []) or '-'} | "
                    f"{row.get('allocation_stage')} |"
                )
    mapping = (
        payload.get("deep_review_mapping")
        if isinstance(payload.get("deep_review_mapping"), Mapping)
        else {}
    )
    route_mapping = (
        mapping.get("surface_routes")
        if isinstance(mapping.get("surface_routes"), Mapping)
        else {}
    )
    lines.extend(
        [
            "",
            "## Deep Review Mapping",
            "",
            "| Surface | Route family | Play mode | Members locator |",
            "|---|---|---|---|",
        ]
    )
    for surface_name in ("BOXED12", "STRAIGHT12"):
        row = (
            route_mapping.get(surface_name)
            if isinstance(route_mapping.get(surface_name), Mapping)
            else {}
        )
        lines.append(
            f"| `{surface_name}` | `{row.get('route_family') or '-'}` | "
            f"`{row.get('play_mode') or '-'}` | "
            f"`{row.get('members_locator') or '-'}` |"
        )
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_merit_slate_files(
    json_path: Path,
    payload: Mapping[str, Any],
) -> Tuple[Path, Path]:
    write_json(json_path, payload)
    markdown_path = json_path.with_suffix(".md")
    markdown_path.write_text(render_merit_slate_markdown(payload), encoding="utf-8")
    return json_path, markdown_path


def discover_merit_inputs(
    candidate_path: Path,
) -> Tuple[Optional[Path], Optional[Path], Optional[Path], Optional[Path]]:
    state_dir = candidate_path.parent
    state_key = state_dir.name
    suffix = candidate_path.name.removeprefix("candidate_universe").removesuffix(".json")
    tables_path = state_dir / "json" / f"{state_key}_tables.json"
    arena_path = state_dir / "analysis" / f"aggregated_analysis_arena{suffix}.json"
    sandbox_path = state_dir / "analysis" / f"translation_sandbox_seed{suffix}.json"
    aux_path = state_dir / "aux" / state_key / "summary.json"
    return (
        tables_path if tables_path.exists() else None,
        arena_path if arena_path.exists() else None,
        sandbox_path if sandbox_path.exists() else None,
        aux_path if aux_path.exists() else None,
    )


def default_merit_output_path(candidate_path: Path) -> Path:
    suffix = candidate_path.name.removeprefix("candidate_universe").removesuffix(".json")
    return (
        candidate_path.parent
        / "analysis"
        / f"merit_allocated_vtrac_cluster_slate{suffix}.json"
    )


__all__ = [
    "ARTIFACT_TYPE",
    "SCHEMA_VERSION",
    "allocate_candidates",
    "build_merit_allocated_slate",
    "collect_external_evidence",
    "default_merit_output_path",
    "discover_merit_inputs",
    "iter_pattern_cells",
    "render_merit_slate_markdown",
    "scan_pattern_tables",
    "score_clusters",
    "select_clusters",
    "validate_tables_input",
    "write_merit_slate_files",
]
