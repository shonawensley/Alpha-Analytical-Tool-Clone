"""Hot Zones engine — JSON ingestion, scanning, scoring, and writers."""

from .models import (
    PatternBox,
    DrawEntry,
    SetEntry,
    SectionEntry,
    TableEnv,
    HotScanConfig,
    load_table_env_from_json,
)
from .scanner import HotZoneScanner, PerItemRow, TopCandidateRow, HotZoneWeights
from .writer import (
    HotZonesArtifacts,
    write_hotzones_artifacts,
    write_winner_map,
)

__all__ = [
    "PatternBox",
    "DrawEntry",
    "SetEntry",
    "SectionEntry",
    "TableEnv",
    "HotScanConfig",
    "HotZoneScanner",
    "PerItemRow",
    "TopCandidateRow",
    "HotZoneWeights",
    "load_table_env_from_json",
    "HotZonesArtifacts",
    "write_hotzones_artifacts",
    "write_winner_map",
]
