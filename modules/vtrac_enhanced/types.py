"""
Typed data structures shared across the enhanced V-TRAC analyzer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional, Sequence

RINGS: Sequence[str] = ("R2", "R4", "R6", "R8")
COLUMN_LABELS: Sequence[int] = (7, 6, 5, 4, 3, 2, 1)
SECTIONS: Sequence[str] = ("Midday", "Evening", "Combined")
SETS: Sequence[str] = ("Set3", "Set2", "Set1")  # processed oldest -> newest


@dataclass(frozen=True)
class Cell:
    """Single grid cell: raw digits plus hot flags."""

    digits: str
    hot: bool = False
    superhot: bool = False


@dataclass(frozen=True)
class PatternsGrid:
    """Canonical representation of one section/set grid."""

    by_ring: Dict[str, Sequence[Cell]]

    def rings(self) -> Iterable[str]:
        return self.by_ring.keys()

    def columns(self, ring: str) -> Sequence[Cell]:
        return self.by_ring.get(ring, ())


@dataclass(frozen=True)
class SectionData:
    """Snapshot of a section/set pair."""

    section: str
    set_name: str
    patterns: PatternsGrid


@dataclass(frozen=True)
class EngineInput:
    """Normalizer input payload consumed by the scoring engine."""

    sections: Sequence[SectionData]
    recent_draws: Sequence[str] = ()
    winner_hint: Optional[int] = None


@dataclass(frozen=True)
class FeatureScore:
    """Contribution of a single feature to an index score."""

    name: str
    value: float
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class IndexEvidence:
    """Mutable collector for per-index evidence."""

    index: int
    raw: Dict[str, Any] = field(default_factory=dict)
    features: List[FeatureScore] = field(default_factory=list)

    def add(self, name: str, value: float, **details: Any) -> None:
        self.features.append(FeatureScore(name=name, value=value, details=details))


@dataclass(frozen=True)
class StraightCandidate:
    """Ranked straight permutation details."""

    index: int
    straight: str
    score: float
    reasons: Sequence[str] = ()


@dataclass
class IndexScore:
    """Aggregate score and attached evidence for one V-TRAC index."""

    index: int
    score: float
    evidence: IndexEvidence
    straights: List[StraightCandidate]


@dataclass(frozen=True)
class EngineOutput:
    """Structured analyzer output."""

    indices_ranked: List[IndexScore]
    straights_ranked: List[StraightCandidate]
    telemetry: Dict[str, Any]


__all__ = [
    "Cell",
    "PatternsGrid",
    "SectionData",
    "EngineInput",
    "FeatureScore",
    "IndexEvidence",
    "StraightCandidate",
    "IndexScore",
    "EngineOutput",
    "RINGS",
    "COLUMN_LABELS",
    "SECTIONS",
    "SETS",
]
