"""
Evidence extraction utilities for the enhanced V-TRAC analyzer.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable, Mapping, MutableMapping, Optional, Sequence, Set, Tuple

from modules.vtrac_reference import BOXED_VTRAC_REFERENCE, get_index_set, get_vtrac_index

from .config import EvidenceWeights
from .types import COLUMN_LABELS, RINGS, EngineInput, IndexEvidence

ALL_INDICES: Tuple[int, ...] = tuple(int(entry["Index"]) for entry in BOXED_VTRAC_REFERENCE)
INDEX_COMBOS: Mapping[int, Set[str]] = {idx: {combo for combo in get_index_set(idx)} for idx in ALL_INDICES}
COMBO_TO_INDICES: Mapping[str, Set[int]] = defaultdict(set)
for idx, combos in INDEX_COMBOS.items():
    for combo in combos:
        COMBO_TO_INDICES.setdefault(combo, set()).add(idx)

MIRROR_MAP = {
    "0": "9",
    "1": "8",
    "2": "7",
    "3": "6",
    "4": "5",
    "5": "4",
    "6": "3",
    "7": "2",
    "8": "1",
    "9": "0",
}


def _digits_only(value: str) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _apply_mask(value: str, digits_to_mask: Set[str]) -> str:
    if not digits_to_mask:
        return value
    return "".join(ch for ch in value if ch not in digits_to_mask)


def _mirror_combo(combo: str) -> Optional[str]:
    if not combo:
        return None
    mirrored: list[str] = []
    for ch in combo:
        mapped = MIRROR_MAP.get(ch)
        if mapped is None:
            return None
        mirrored.append(mapped)
    return "".join(mirrored)


def extract_index_evidence(
    data: EngineInput,
    weights: EvidenceWeights,
    *,
    digits_to_mask: Optional[Set[str]] = None,
) -> Dict[int, IndexEvidence]:
    """
    Scan the combined tables and collect structured evidence for each index.
    """

    weights.normalise()
    digits_to_mask = set(digits_to_mask or ())

    evidence_map: Dict[int, IndexEvidence] = {idx: IndexEvidence(index=idx) for idx in ALL_INDICES}
    stats: Dict[int, MutableMapping[str, object]] = {
        idx: {
            "presence_score": 0.0,
            "sections": set(),
            "set_presence": set(),
            "hot_hits": 0,
            "super_hot_hits": 0,
            "first_col": None,
            "max_streak": 0,
            "streak_current": {ring: 0 for ring in RINGS},
            "double_hits": 0,
            "mask_drop": False,
            "reduction_hits": 0,
            "total_hits": 0,
            "columns_by_ring": {ring: set() for ring in RINGS},
            "mirror_refs": set(),
            "order_counts": defaultdict(float),
        }
        for idx in ALL_INDICES
    }

    for section_data in data.sections:
        section_weight = weights.section_weights.get(section_data.section, 1.0)
        set_weight = weights.set_weights.get(section_data.set_name, 1.0)

        for ring in section_data.patterns.rings():
            ring_weight = weights.ring_weights.get(ring, 1.0)
            cells = section_data.patterns.columns(ring)
            if not cells:
                continue

            for col_number, cell in zip(COLUMN_LABELS, cells):
                matched_indices: Set[int] = set()
                base_digits = _digits_only(cell.digits)
                masked_digits = _apply_mask(base_digits, digits_to_mask)

                if len(masked_digits) < 3 and len(base_digits) < 3:
                    continue

                masked_hits: Set[str] = set()
                base_hits: Set[str] = set()

                if len(masked_digits) >= 3:
                    for combo in COMBO_TO_INDICES:
                        if combo in masked_digits:
                            masked_hits.add(combo)
                        if digits_to_mask and combo in base_digits:
                            base_hits.add(combo)
                elif digits_to_mask and len(base_digits) >= 3:
                    for combo in COMBO_TO_INDICES:
                        if combo in base_digits:
                            base_hits.add(combo)

                if not masked_hits:
                    continue

                column_weight = weights.column_weights.get(col_number, 1.0)
                for combo in masked_hits:
                    owners = COMBO_TO_INDICES.get(combo, ())
                    if not owners:
                        continue
                    for idx in owners:
                        matched_indices.add(idx)
                        meta = stats[idx]

                        base = ring_weight * section_weight * set_weight * column_weight
                        boost = 0.0
                        if cell.hot:
                            boost += weights.hot_boost
                            meta["hot_hits"] = int(meta["hot_hits"]) + 1
                        if cell.superhot:
                            boost += weights.super_hot_boost
                            meta["super_hot_hits"] = int(meta["super_hot_hits"]) + 1
                        contribution = base * (1.0 + boost)

                        meta["presence_score"] = float(meta["presence_score"]) + contribution
                        meta["total_hits"] = int(meta["total_hits"]) + 1
                        meta["sections"].add(section_data.section)
                        meta["set_presence"].add(section_data.set_name)
                        meta["columns_by_ring"][ring].add(col_number)
                        meta["order_counts"][combo] += contribution

                        first_col = meta["first_col"]
                        if first_col is None or col_number < first_col:
                            meta["first_col"] = col_number

                        if len(set(combo)) <= 2:
                            meta["double_hits"] = int(meta["double_hits"]) + 1

                        if weights.enable_reduction_assist and digits_to_mask:
                            base_present = combo in base_hits
                            if not base_present:
                                meta["mask_drop"] = True
                                meta["reduction_hits"] = int(meta["reduction_hits"]) + 1

                        if weights.enable_mirror_assist:
                            mirror_combo = _mirror_combo(combo)
                            if mirror_combo:
                                mirror_idx = get_vtrac_index(mirror_combo)
                                if mirror_idx:
                                    meta["mirror_refs"].add(int(mirror_idx))

                # update streaks
                for idx, meta in stats.items():
                    streaks = meta["streak_current"]
                    if idx in matched_indices:
                        streaks[ring] = streaks[ring] + 1
                        meta["max_streak"] = max(int(meta["max_streak"]), streaks[ring])
                    else:
                        streaks[ring] = 0

    # evaluate mirror support and transfer stats into evidence objects
    for idx, meta in stats.items():
        evidence = evidence_map[idx]
        mirror_refs: Set[int] = meta["mirror_refs"]
        mirror_supported = any(stats.get(ref, {}).get("total_hits") for ref in mirror_refs)

        evidence.raw.update(
            {
                "presence_score": float(meta["presence_score"]),
                "sections": sorted(meta["sections"]),
                "set_presence": sorted(meta["set_presence"]),
                "hot_hits": int(meta["hot_hits"]),
                "super_hot_hits": int(meta["super_hot_hits"]),
                "first_col": meta["first_col"],
                "max_streak": int(meta["max_streak"]),
                "double_hits": int(meta["double_hits"]),
                "mask_drop": bool(meta["mask_drop"]),
                "reduction_hits": int(meta["reduction_hits"]),
                "total_hits": int(meta["total_hits"]),
                "columns_by_ring": {ring: sorted(cols) for ring, cols in meta["columns_by_ring"].items()},
                "mirror_refs": sorted(mirror_refs),
                "mirror_supported": mirror_supported,
                "order_counts": dict(meta["order_counts"]),
            }
        )

    return evidence_map


__all__ = ["extract_index_evidence"]
