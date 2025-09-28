"""
Digit-Reduction · Analyzer V2 (AAT9)

Reads reducer training artifacts and writes richer analysis beside them:
  data/outputs/analysis/digit_reduction/<STATE>/training/  (inputs)
  data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/  (outputs)

Do not modify the live reducer/orchestrator used by the app.
"""
__all__ = ["io", "features", "pivot", "score", "writers", "pipeline", "types"]
from .pipeline import run
