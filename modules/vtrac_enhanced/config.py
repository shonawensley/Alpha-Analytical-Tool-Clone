"""
Scoring weights and toggles for the enhanced V-TRAC analyzer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, Mapping, MutableMapping

from .types import COLUMN_LABELS, RINGS, SECTIONS, SETS


@dataclass
class EvidenceWeights:
    """Tunable knobs aligned with the redesign specification."""

    ring_weights: MutableMapping[str, float] = field(
        default_factory=lambda: {ring: weight for ring, weight in zip(RINGS, (1.25, 1.10, 1.00, 1.00))}
    )
    column_weights: MutableMapping[int, float] = field(
        default_factory=lambda: {col: weight for col, weight in zip(COLUMN_LABELS, (0.15, 0.25, 0.40, 0.55, 0.70, 0.85, 1.00))}
    )
    set_weights: MutableMapping[str, float] = field(
        default_factory=lambda: {"Set1": 1.00, "Set2": 0.60, "Set3": 0.40}
    )
    section_weights: MutableMapping[str, float] = field(
        default_factory=lambda: {"Combined": 1.15, "Midday": 1.00, "Evening": 1.00}
    )

    hot_boost: float = 0.10
    super_hot_boost: float = 0.20

    bonus_cross_section: float = 0.50
    bonus_set_echo: float = 0.30
    bonus_column_span: float = 0.25
    bonus_first_hit: float = 0.40
    bonus_persistence: float = 0.40
    bonus_mask_drop: float = 0.30
    bonus_reduction: float = 0.25
    bonus_doubles: float = 0.25
    bonus_mirror: float = 0.35
    bonus_total_hits: float = 0.05
    bonus_hot_support: float = 0.12
    bonus_super_hot_support: float = 0.18

    penalty_recent_winner: float = -0.35

    straight_hot_weight: float = 0.20
    straight_consensus_weight: float = 0.20

    enable_mirror_assist: bool = True
    enable_reduction_assist: bool = True
    emit_evidence: bool = True

    def to_dict(self) -> dict:
        return {
            "ring_weights": dict(self.ring_weights),
            "column_weights": dict(self.column_weights),
            "set_weights": dict(self.set_weights),
            "section_weights": dict(self.section_weights),
            "hot_boost": self.hot_boost,
            "super_hot_boost": self.super_hot_boost,
            "bonus_cross_section": self.bonus_cross_section,
            "bonus_set_echo": self.bonus_set_echo,
            "bonus_column_span": self.bonus_column_span,
            "bonus_first_hit": self.bonus_first_hit,
            "bonus_persistence": self.bonus_persistence,
            "bonus_mask_drop": self.bonus_mask_drop,
            "bonus_reduction": self.bonus_reduction,
            "bonus_doubles": self.bonus_doubles,
            "bonus_mirror": self.bonus_mirror,
            "bonus_total_hits": self.bonus_total_hits,
            "bonus_hot_support": self.bonus_hot_support,
            "bonus_super_hot_support": self.bonus_super_hot_support,
            "penalty_recent_winner": self.penalty_recent_winner,
            "straight_hot_weight": self.straight_hot_weight,
            "straight_consensus_weight": self.straight_consensus_weight,
            "enable_mirror_assist": self.enable_mirror_assist,
            "enable_reduction_assist": self.enable_reduction_assist,
            "emit_evidence": self.emit_evidence,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "EvidenceWeights":
        base = cls()
        clean = dict(data or {})
        return cls(
            ring_weights=clean.get("ring_weights", base.ring_weights),
            column_weights=clean.get("column_weights", base.column_weights),
            set_weights=clean.get("set_weights", base.set_weights),
            section_weights=clean.get("section_weights", base.section_weights),
            hot_boost=clean.get("hot_boost", base.hot_boost),
            super_hot_boost=clean.get("super_hot_boost", base.super_hot_boost),
            bonus_cross_section=clean.get("bonus_cross_section", base.bonus_cross_section),
            bonus_set_echo=clean.get("bonus_set_echo", base.bonus_set_echo),
            bonus_column_span=clean.get("bonus_column_span", base.bonus_column_span),
            bonus_first_hit=clean.get("bonus_first_hit", base.bonus_first_hit),
            bonus_persistence=clean.get("bonus_persistence", base.bonus_persistence),
            bonus_mask_drop=clean.get("bonus_mask_drop", base.bonus_mask_drop),
            bonus_reduction=clean.get("bonus_reduction", base.bonus_reduction),
            bonus_doubles=clean.get("bonus_doubles", base.bonus_doubles),
            bonus_mirror=clean.get("bonus_mirror", base.bonus_mirror),
            bonus_total_hits=clean.get("bonus_total_hits", base.bonus_total_hits),
            bonus_hot_support=clean.get("bonus_hot_support", base.bonus_hot_support),
            bonus_super_hot_support=clean.get("bonus_super_hot_support", base.bonus_super_hot_support),
            penalty_recent_winner=clean.get("penalty_recent_winner", base.penalty_recent_winner),
            straight_hot_weight=clean.get("straight_hot_weight", base.straight_hot_weight),
            straight_consensus_weight=clean.get("straight_consensus_weight", base.straight_consensus_weight),
            enable_mirror_assist=clean.get("enable_mirror_assist", base.enable_mirror_assist),
            enable_reduction_assist=clean.get("enable_reduction_assist", base.enable_reduction_assist),
            emit_evidence=clean.get("emit_evidence", base.emit_evidence),
        )

    def normalise(self) -> None:
        """Ensure weight dictionaries contain all expected keys."""
        for ring in RINGS:
            self.ring_weights.setdefault(ring, 1.0)
        for column in COLUMN_LABELS:
            self.column_weights.setdefault(column, 1.0)
        for set_name in SETS:
            self.set_weights.setdefault(set_name, 1.0)
        for section in SECTIONS:
            self.section_weights.setdefault(section, 1.0)

    def clone(self) -> "EvidenceWeights":
        """Return a detached copy."""
        return EvidenceWeights(
            ring_weights=dict(self.ring_weights),
            column_weights=dict(self.column_weights),
            set_weights=dict(self.set_weights),
            section_weights=dict(self.section_weights),
            hot_boost=self.hot_boost,
            super_hot_boost=self.super_hot_boost,
            bonus_cross_section=self.bonus_cross_section,
            bonus_set_echo=self.bonus_set_echo,
            bonus_column_span=self.bonus_column_span,
            bonus_first_hit=self.bonus_first_hit,
            bonus_persistence=self.bonus_persistence,
            bonus_mask_drop=self.bonus_mask_drop,
            bonus_reduction=self.bonus_reduction,
            bonus_doubles=self.bonus_doubles,
            bonus_mirror=self.bonus_mirror,
            bonus_total_hits=self.bonus_total_hits,
            bonus_hot_support=self.bonus_hot_support,
            bonus_super_hot_support=self.bonus_super_hot_support,
            penalty_recent_winner=self.penalty_recent_winner,
            straight_hot_weight=self.straight_hot_weight,
            straight_consensus_weight=self.straight_consensus_weight,
            enable_mirror_assist=self.enable_mirror_assist,
            enable_reduction_assist=self.enable_reduction_assist,
            emit_evidence=self.emit_evidence,
        )


DEFAULT_WEIGHTS = EvidenceWeights()


__all__ = ["EvidenceWeights", "DEFAULT_WEIGHTS"]
