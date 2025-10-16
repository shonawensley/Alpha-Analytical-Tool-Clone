"""
Feature extraction helpers for the enhanced V-TRAC analyzer.

This module inspects the combined tables grid and produces structured
evidence per V-TRAC index. The evidence is kept intentionally rich so the
scoring layer can remain simple and explainable.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable, Mapping, MutableMapping, Optional, Sequence, Set

from modules.vtrac_reference import BOXED_VTRAC_REFERENCE, get_index_set, get_vtrac_index

from .config import EvidenceWeights
from .types import EngineInput, IndexEvidence

# --------------------------------------------------------------------------------------
# Precomputed reference tables
# --------------------------------------------------------------------------------------

INDEX_IDS: Sequence[int] = tuple(int(entry["Index"]) for entry in BOXED_VTRAC_REFERENCE)
INDEX_COMBOS: Mapping[int, Set[str]] = {
    idx: get_index_set(idx) for idx in INDEX_IDS
}


def _digits_only(text: str) -> str:
    return "".join(ch for ch in text if ch.isdigit())


def _apply_mask(text: str, digits_to_mask: Optional[Set[str]]) -> str:
    if not digits_to_mask:
        return text
    return "".join(ch for ch in text if ch not in digits_to_mask)


def _match_combos(text: str, combos: Iterable[str]) -> Set[str]:
    return {combo for combo in combos if combo and combo in text}


def extract_index_evidence(
    data: EngineInput,
    weights: EvidenceWeights,
    *,
    digits_to_mask: Optional[Set[str]] = None,
) -> Dict[int, IndexEvidence]:
    """
    Produce raw evidence for every index.

    The resulting dictionary contains IndexEvidence objects with both raw stats
    (in .raw) and a list of FeatureScore entries (.features) suitable for logging.
    """

    weights.normalize_columns()
    evidence_map: Dict[int, IndexEvidence] = {idx: IndexEvidence(index=idx) for idx in INDEX_IDS}

    stats: Dict[int, MutableMapping[str, object]] = {
        idx: {
            "presence_score": 0.0,
            "sections": set(),
            "hot_hits": 0,
            "super_hot_hits": 0,
            "first_col": None,
            "max_streak": 0,
            "streak_current": {"R2": 0, "R4": 0, "R6": 0, "R8": 0},
            "double_hits": 0,
            "mask_drop": False,
            "total_hits": 0,
            "order_counts": defaultdict(float),
            "hot_weight": 0.0,
            "columns_by_ring": {"R2": set(), "R4": set(), "R6": set(), "R8": set()},
            "mirror_refs": set(),
            "reduction_hits": 0,
        }
        for idx in INDEX_IDS
    }

    digits_to_mask = digits_to_mask or set()

    for section in data.sections:
        section_weight = weights.section_weights.get(section.section, 1.0)
        set_weight = weights.set_weights.get(section.set_name, 1.0)

        for ring in section.patterns.rings():
            ring_weight = weights.ring_weights.get(ring, 1.0)
            cells = section.patterns.columns(ring)
            if not cells:
                continue

            for col_idx, cell in enumerate(cells):
                col_number = 7 - col_idx
                col_weight = weights.column_weights.get(col_number, 1.0)

                base_digits = _digits_only(cell.digits)
                masked_digits = _apply_mask(base_digits, digits_to_mask)
                if not masked_digits:
                    continue

                base_matches: Dict[int, Set[str]] = {}
                masked_matches: Dict[int, Set[str]] = {}
                for idx in INDEX_IDS:
                    combos = INDEX_COMBOS[idx]
                    matched_masked = _match_combos(masked_digits, combos)
                    if matched_masked:
                        masked_matches[idx] = matched_masked
                        matched_base = _match_combos(base_digits, combos)
                        if matched_base:
                            base_matches[idx] = matched_base

                if not masked_matches:
                    # reset streaks for indexes that had ongoing runs
                    for idx in INDEX_IDS:
                        streaks = stats[idx]["streak_current"]
                        if streaks[ring]:
                            streaks[ring] = 0
                    continue

                matched_indices = set(masked_matches.keys())
                for idx in INDEX_IDS:
                    streaks = stats[idx]["streak_current"]
                    if idx in matched_indices:
                        streaks[ring] += 1
                        stats[idx]["max_streak"] = max(
                            stats[idx]["max_streak"], streaks[ring]
                        )
                    else:
                        streaks[ring] = 0

                for idx, combos in masked_matches.items():
                    ev_stats = stats[idx]
                    score_weight = ring_weight * col_weight * section_weight * set_weight
                    if cell.hot:
                        score_weight += weights.hot_boost
                    if cell.superhot:
                        score_weight += weights.super_hot_boost

                    ev_stats["presence_score"] += score_weight
                    ev_stats["sections"].add(section.section)
                    if cell.hot:
                        ev_stats["hot_hits"] += 1
                    if cell.superhot:
                        ev_stats["super_hot_hits"] += 1
                    ev_stats["hot_weight"] += max(0.0, score_weight - (ring_weight * col_weight * section_weight * set_weight))
                    ev_stats["total_hits"] += len(combos)
                    ev_stats["columns_by_ring"][ring].add(col_number)

                    first_col = ev_stats["first_col"]
                    if first_col is None or col_number < first_col:
                        ev_stats["first_col"] = col_number

                    base_matched = base_matches.get(idx, set())
                    if weights.enable_reduction_assist and combos - base_matched:
                        ev_stats["mask_drop"] = True
                        ev_stats["reduction_hits"] += len(combos - base_matched)

                    for combo in combos:
                        ev_stats["order_counts"][combo] += score_weight
                        if len(set(combo)) <= 2:
                            ev_stats["double_hits"] += 1
                        if weights.enable_mirror_assist:
                            mirror = _mirror_combo(combo)
                            if mirror:
                                mirror_idx = get_vtrac_index(mirror)
                                if mirror_idx and mirror_idx != idx:
                                    ev_stats["mirror_refs"].add(mirror_idx)

    # Second pass: populate IndexEvidence objects
    mirror_supported: Dict[int, bool] = {}
    for idx, meta in stats.items():
        mirror_refs: Set[int] = meta["mirror_refs"]
        mirror_supported[idx] = any(
            stats.get(ref, {}).get("total_hits", 0) for ref in mirror_refs
        )

    for idx, meta in stats.items():
        evidence = evidence_map[idx]
        evidence.raw.update(
            {
                "presence_score": meta["presence_score"],
                "sections": sorted(meta["sections"]),
                "hot_hits": meta["hot_hits"],
                "super_hot_hits": meta["super_hot_hits"],
                "first_col": meta["first_col"],
                "max_streak": meta["max_streak"],
                "double_hits": meta["double_hits"],
                "mask_drop": meta["mask_drop"],
                "total_hits": meta["total_hits"],
                "order_counts": dict(meta["order_counts"]),
                "columns_by_ring": {
                    ring: sorted(cols) for ring, cols in meta["columns_by_ring"].items()
                },
                "mirror_refs": sorted(meta["mirror_refs"]),
                "mirror_supported": mirror_supported[idx],
                "reduction_hits": meta["reduction_hits"],
            }
        )
        if weights.emit_evidence:
            evidence.add(
                "presence",
                meta["presence_score"],
                sections=evidence.raw["sections"],
                hot_hits=meta["hot_hits"],
            )

    return evidence_map


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


def _mirror_combo(combo: str) -> Optional[str]:
    if not combo:
        return None
    try:
        return "".join(MIRROR_MAP[d] for d in combo)
    except KeyError:
        return None


def straight_permutation_candidates(index: int) -> Set[str]:
    """
    Return the unique 3-digit straight permutations associated with an index.
    """

    combos = INDEX_COMBOS.get(index, set())
    return {combo for combo in combos if len(combo) == 3 and len(set(combo)) == 3}
