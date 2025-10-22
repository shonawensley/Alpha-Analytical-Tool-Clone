"""
Public API surface for the enhanced V-TRAC analyzer package.
"""

from .config import EvidenceWeights, DEFAULT_WEIGHTS
from .engine import run_analysis
from .adapters import (
    build_engine_input_from_tables,
    suggested_mask_digits,
    write_prediction_bundle,
)
from .types import EngineInput, EngineOutput

__all__ = [
    "EvidenceWeights",
    "DEFAULT_WEIGHTS",
    "EngineInput",
    "EngineOutput",
    "run_analysis",
    "build_engine_input_from_tables",
    "suggested_mask_digits",
    "write_prediction_bundle",
]
