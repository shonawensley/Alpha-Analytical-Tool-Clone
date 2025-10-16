"""
Scoring engine for the enhanced V-TRAC analyzer.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Set

from .config import EvidenceWeights, DEFAULT_WEIGHTS
from .features import extract_index_evidence, straight_permutation_candidates
from .types import EngineInput, EngineOutput, IndexEvidence, IndexScore, StraightCandidate


def run_analysis(
    data: EngineInput,
    weights: Optional[EvidenceWeights] = None,
    *,
    digits_to_mask: Optional[Set[str]] = None,
) -> EngineOutput:
    """
    Execute the enhanced V-TRAC scoring pipeline.
    """

    weights = weights or EvidenceWeights()
    evidence_map = extract_index_evidence(
        data,
        weights,
        digits_to_mask=digits_to_mask,
    )

    index_scores: List[IndexScore] = []
    straight_pool: List[StraightCandidate] = []

    for idx, evidence in evidence_map.items():
        raw = evidence.raw
        score = float(raw["presence_score"])
        sections: Sequence[str] = raw["sections"]

        if len(sections) >= 2:
            intensity = min(1.0, (len(sections) - 1) / 2.0 + 0.5)
            bonus = weights.bonus_cross_section * intensity
            score += bonus
            if weights.emit_evidence:
                evidence.add("cross_section", bonus, sections=sections)

        first_col = raw["first_col"]
        if first_col:
            multiplier = max(0.2, 1.0 - (first_col - 1) / 6.0)
            bonus = weights.bonus_first_hit * multiplier
            score += bonus
            if weights.emit_evidence:
                evidence.add("first_hit", bonus, first_column=first_col)

        max_streak = raw["max_streak"]
        if max_streak >= 2:
            bonus = weights.bonus_persistence * min(1.0, max_streak / 4.0)
            score += bonus
            if weights.emit_evidence:
                evidence.add("persistence", bonus, streak=max_streak)

        if raw["mask_drop"]:
            bonus = weights.bonus_mask_drop + (weights.bonus_reduction * raw["reduction_hits"])
            score += bonus
            if weights.emit_evidence:
                evidence.add(
                    "mask_drop",
                    bonus,
                    reduction_hits=raw["reduction_hits"],
                )

        if raw["double_hits"]:
            bonus = weights.bonus_doubles * min(1.0, raw["double_hits"] / 4.0)
            score += bonus
            if weights.emit_evidence:
                evidence.add("doubles_bias", bonus, hits=raw["double_hits"])

        if raw["mirror_supported"] and weights.enable_mirror_assist:
            score += weights.bonus_mirror
            if weights.emit_evidence:
                evidence.add("mirror_support", weights.bonus_mirror, refs=raw["mirror_refs"])

        if data.winner_hint and int(data.winner_hint) == idx:
            score += weights.penalty_recent_winner
            if weights.emit_evidence:
                evidence.add("recent_penalty", weights.penalty_recent_winner, winner=data.winner_hint)

        straights = _score_straights(
            idx,
            evidence,
            weights=weights,
        )
        straight_pool.extend(straights)

        index_scores.append(
            IndexScore(
                index=idx,
                score=score,
                evidence=evidence,
                straights=straights,
            )
        )

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
    }

    return EngineOutput(indices_ranked=index_scores, straights_ranked=straight_pool, telemetry=telemetry)


def _score_straights(
    index: int,
    evidence: IndexEvidence,
    *,
    weights: EvidenceWeights,
) -> List[StraightCandidate]:
    raw = evidence.raw
    order_counts: Dict[str, float] = raw["order_counts"]
    if not order_counts:
        return []

    sections = raw["sections"]
    hot_hits = raw["hot_hits"]

    straights: List[StraightCandidate] = []
    permutations = straight_permutation_candidates(index)

    for perm in permutations:
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
