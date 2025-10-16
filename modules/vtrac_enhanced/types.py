"""
Typed data structures for the enhanced V-TRAC analyzer.

These dataclasses encapsulate the evidence grid extracted from the
combined tables as well as the scoring outputs returned by the engine.
They are intentionally lightweight and JSON-friendly so the same payloads
can be logged for training or consumed by the Streamlit UI.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional, Sequence

# --------------------------------------------------------------------------------------
# Input structures
# --------------------------------------------------------------------------------------


@dataclass(frozen=True)
class Cell:
    """Single grid cell: the digits string plus hot-zone flags."""

    digits: str
    hot: bool = False
    superhot: bool = False


@dataclass(frozen=True)
class PatternsGrid:
    """
    Canonical pattern grid for one section (Midday / Evening / Combined).

    Layout:
        - by_r maps ring ("R2", "R4", "R6", "R8") to a list of 7 cells.
        - The list is left-to-right (col7 -> col1) with index -1 representing col1.
    """

    by_r: Dict[str, Sequence[Cell]]

    def rings(self) -> Iterable[str]:
        return self.by_r.keys()

    def columns(self, ring: str) -> Sequence[Cell]:
        return self.by_r.get(ring, ())


@dataclass(frozen=True)
class SectionData:
    """
    Wrapper for one Set (Set1/Set2/Set3) inside a section (Midday/Evening/Combined).
    """

    section: str
    set_name: str
    patterns: PatternsGrid


@dataclass(frozen=True)
class EngineInput:
    """
    Normalised input for the enhanced analyzer.

    Attributes:
        sections: Ordered list of section/set grids in recency order (Set1 first).
        recent_draws: Optional latest draws for reduction assists (newest first).
        winner_hint: Optional prior winner V-TRAC index (supports recency damping).
    """

    sections: Sequence[SectionData]
    recent_draws: Sequence[str] = ()
    winner_hint: Optional[int] = None


# --------------------------------------------------------------------------------------
# Evidence and scoring payloads
# --------------------------------------------------------------------------------------


@dataclass(frozen=True)
class FeatureScore:
    """Single feature contribution for audit trails."""

    name: str
    value: float
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class IndexEvidence:
    """Mutable accumulator of per-index evidence."""

    index: int
    raw: Dict[str, Any] = field(default_factory=dict)
    features: List[FeatureScore] = field(default_factory=list)

    def add(self, name: str, value: float, **details: Any) -> None:
        self.features.append(FeatureScore(name=name, value=value, details=details))


@dataclass
class StraightCandidate:
    index: int
    straight: str
    score: float
    reasons: List[str] = field(default_factory=list)


@dataclass
class IndexScore:
    index: int
    score: float
    evidence: IndexEvidence
    straights: List[StraightCandidate]


@dataclass
class EngineOutput:
    indices_ranked: List[IndexScore]
    straights_ranked: List[StraightCandidate]
    telemetry: Dict[str, Any] = field(default_factory=dict)
