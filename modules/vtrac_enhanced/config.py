"""
Default configuration knobs for the enhanced V-TRAC analyzer.

These weights and toggles are designed to mirror the ratios outlined in the
research briefs while remaining easy to tweak on a per-state basis.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, Mapping, MutableMapping


@dataclass
class EvidenceWeights:
    """
    Tunable weights for index scoring.

    The defaults align with the "FINAL" blueprint: right-column gravity,
    set/section weighting, and conservative boosts for mirror/reduction assists.
    """

    ring_weights: MutableMapping[str, float] = field(
        default_factory=lambda: {"R2": 1.25, "R4": 1.10, "R6": 1.00, "R8": 1.00}
    )
    column_weights: MutableMapping[int, float] = field(
        default_factory=lambda: {7: 0.15, 6: 0.25, 5: 0.40, 4: 0.55, 3: 0.70, 2: 0.85, 1: 1.00}
    )
    set_weights: MutableMapping[str, float] = field(
        default_factory=lambda: {"Set1": 1.00, "Set2": 0.60, "Set3": 0.40}
    )
    section_weights: MutableMapping[str, float] = field(
        default_factory=lambda: {"Combined": 1.15, "Midday": 1.00, "Evening": 1.00}
    )
    hot_boost: float = 0.10
    super_hot_boost: float = 0.20

    # Bonus terms
    bonus_cross_section: float = 0.50
    bonus_first_hit: float = 0.40
    bonus_persistence: float = 0.40
    bonus_reduction: float = 0.25
    bonus_doubles: float = 0.25
    bonus_mask_drop: float = 0.30
    bonus_mirror: float = 0.35

    # Dampers
    penalty_recent_winner: float = -0.35

    # Feature toggles
    enable_mirror_assist: bool = True
    enable_reduction_assist: bool = True
    emit_evidence: bool = True

    straight_order_weight: float = 0.6
    straight_hot_weight: float = 0.2
    straight_consensus_weight: float = 0.2

    def normalize_columns(self) -> None:
        """
        Ensure column weights cover the expected range 1..7. Missing values inherit
        from nearest neighbour (defaults already set).
        """
        for col in (7, 6, 5, 4, 3, 2, 1):
            if col not in self.column_weights:
                self.column_weights[col] = self.column_weights.get(col + 1, 1.0)

    def ring_list(self) -> Iterable[str]:
        return self.ring_weights.keys()


DEFAULT_WEIGHTS = EvidenceWeights()
