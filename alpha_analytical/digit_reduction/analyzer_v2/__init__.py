"""
Digit-Reduction Analyzer V2 (AAT9)

Reads reducer training artifacts and writes richer analysis beside them:
  data/outputs/analysis/digit_reduction/<STATE>/training/  (inputs)
  data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/  (outputs)

Do not modify the live reducer/orchestrator used by the app.
"""
from . import io, features, pivot, score, writers, vtrac_index, types
from .pipeline import run
from .winners_overlay import run_winner_overlay, run_winner_overlay_batch

__all__ = [
    "run",
    "run_winner_overlay",
    "run_winner_overlay_batch",
    "io",
    "features",
    "pivot",
    "score",
    "writers",
    "vtrac_index",
    "types",
]
