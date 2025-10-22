"""
Scoring engine orchestrating the enhanced V-TRAC analysis.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Set

from modules.vtrac_reference import get_index_set

from .config import EvidenceWeights, DEFAULT_WEIGHTS
from .features import extract_index_evidence
from .types import EngineInput, EngineOutput, IndexEvidence, IndexScore, StraightCandidate


def run_analysis(
    data: EngineInput,
    weights: Optional[EvidenceWeights] = None,
    *,
    digits_to_mask: Optional[Set[str]] = None,
) -> EngineOutput:
    """
    Execute the enhanced analyzer and return ranked indices and straights.
    """

    weights = weights.clone() if weights else DEFAULT_WEIGHTS.clone()
    evidence_map = extract_index_evidence(data, weights, digits_to_mask=digits_to_mask)

    index_scores: List[IndexScore] = []
    straight_pool: List[StraightCandidate] = []

    for idx, evidence in evidence_map.items():
        raw = evidence.raw
        presence = float(raw.get("presence_score", 0.0))
        sections: Sequence[str] = raw.get("sections", [])
        set_presence: Sequence[str] = raw.get("set_presence", [])
        columns_by_ring: Dict[str, Sequence[int]] = raw.get("columns_by_ring", {})
        first_col = raw.get("first_col")
        max_streak = raw.get("max_streak", 0)
        total_hits = raw.get("total_hits", 0)
        hot_hits = raw.get("hot_hits", 0)
        super_hot_hits = raw.get("super_hot_hits", 0)

        score = 0.0
        if presence:
            score += presence
            if weights.emit_evidence:
                evidence.add("presence", presence, total_hits=total_hits)

        if len(sections) >= 2:
            intensity = min(1.0, (len(sections) - 1) / 2.0 + 0.5)
            bonus = weights.bonus_cross_section * intensity
            score += bonus
            if weights.emit_evidence:
                evidence.add("cross_section", bonus, sections=sections, intensity=intensity)

        unique_sets = sorted({s for s in set_presence})
        if len(unique_sets) >= 2:
            bonus = weights.bonus_set_echo * min(len(unique_sets) - 1, 2)
            score += bonus
            if weights.emit_evidence:
                evidence.add("set_echo", bonus, sets=unique_sets)

        if first_col:
            # closer to column 1 earns the full bonus
            multiplier = max(0.2, 1.0 - (first_col - 1) / 6.0)
            bonus = weights.bonus_first_hit * multiplier
            score += bonus
            if weights.emit_evidence:
                evidence.add("first_hit", bonus, first_column=first_col, multiplier=multiplier)

        columns: Set[int] = set()
        for cols in columns_by_ring.values():
            columns.update(cols)
        if columns:
            near = sum(1 for col in columns if col <= 3)
            far = len(columns) - near
            coverage = 0.0
            if near:
                coverage += near / 3.0
            if far:
                coverage += 0.35 * min(far, 4) / 4.0
            bonus = weights.bonus_column_span * min(coverage, 1.6)
            if bonus:
                score += bonus
                if weights.emit_evidence:
                    evidence.add("column_span", bonus, columns=sorted(columns))

        if max_streak and max_streak >= 2:
            bonus = weights.bonus_persistence * min(1.0, max_streak / 4.0)
            score += bonus
            if weights.emit_evidence:
                evidence.add("persistence", bonus, streak=max_streak)

        if total_hits:
            bonus = weights.bonus_total_hits * min(total_hits, 12)
            score += bonus
            if weights.emit_evidence:
                evidence.add("hit_volume", bonus, total_hits=total_hits)

        if hot_hits:
            bonus = weights.bonus_hot_support * hot_hits
            score += bonus
            if weights.emit_evidence:
                evidence.add("hot_support", bonus, hot_hits=hot_hits)

        if super_hot_hits:
            bonus = weights.bonus_super_hot_support * super_hot_hits
            score += bonus
            if weights.emit_evidence:
                evidence.add("super_hot_support", bonus, super_hot_hits=super_hot_hits)

        if raw.get("mask_drop") and weights.enable_reduction_assist:
            bonus = weights.bonus_mask_drop + (weights.bonus_reduction * raw.get("reduction_hits", 0))
            score += bonus
            if weights.emit_evidence:
                evidence.add(
                    "mask_drop",
                    bonus,
                    reduction_hits=raw.get("reduction_hits", 0),
                )

        if raw.get("double_hits", 0):
            bonus = weights.bonus_doubles * min(1.0, raw["double_hits"] / 4.0)
            score += bonus
            if weights.emit_evidence:
                evidence.add("doubles_bias", bonus, hits=raw["double_hits"])

        if raw.get("mirror_supported") and weights.enable_mirror_assist:
            score += weights.bonus_mirror
            if weights.emit_evidence:
                evidence.add("mirror_support", weights.bonus_mirror, refs=raw.get("mirror_refs", []))

        if data.winner_hint and int(data.winner_hint) == idx:
            score += weights.penalty_recent_winner
            if weights.emit_evidence:
                evidence.add("recent_penalty", weights.penalty_recent_winner, winner=data.winner_hint)

        straights = _score_straights(idx, evidence, weights=weights)
        straight_pool.extend(straights)

        index_scores.append(IndexScore(index=idx, score=score, evidence=evidence, straights=straights))

        if weights.emit_evidence and not total_hits:
            evidence.add("no_hits", 0.0)

    index_scores.sort(key=lambda item: item.score, reverse=True)
    straight_pool.sort(key=lambda item: item.score, reverse=True)

    telemetry = {
        "weights": {
            "ring": dict(weights.ring_weights),
            "column": dict(weights.column_weights),
            "set": dict(weights.set_weights),
            "section": dict(weights.section_weights),
        },
        "winner_hint": data.winner_hint,
        "mask_digits": sorted(digits_to_mask) if digits_to_mask else [],
    }

    return EngineOutput(indices_ranked=index_scores, straights_ranked=straight_pool, telemetry=telemetry)


def _score_straights(
    index: int,
    evidence: IndexEvidence,
    *,
    weights: EvidenceWeights,
) -> List[StraightCandidate]:
    raw = evidence.raw
    order_counts: Dict[str, float] = raw.get("order_counts", {})
    if not order_counts:
        return []

    sections = raw.get("sections", [])
    hot_hits = raw.get("hot_hits", 0)
    straights: List[StraightCandidate] = []

    permutations: Set[str] = set()
    for combo in get_index_set(index):
        cleaned = "".join(ch for ch in combo if ch.isdigit())
        if len(cleaned) != 3 or len(set(cleaned)) != 3:
            continue
        permutations.add(cleaned)

    for perm in sorted(permutations):
        base_score = order_counts.get(perm, 0.0)
        if base_score <= 0:
            continue

        hot_bonus = weights.straight_hot_weight * hot_hits
        consensus_bonus = weights.straight_consensus_weight * max(0, len(sections) - 1)
        final_score = base_score + hot_bonus + consensus_bonus

        reasons: List[str] = []
        if base_score:
            reasons.append("order echoes")
        if hot_hits:
            reasons.append("hot zone support")
        if len(sections) >= 2:
            reasons.append("cross-section echo")

        straights.append(
            StraightCandidate(
                index=index,
                straight=perm,
                score=final_score,
                reasons=reasons,
            )
        )

    return straights


__all__ = ["run_analysis"]
