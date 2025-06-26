"""Alpha Analytical Tool Python package.

This root package exposes submodules such as `alpha_analytical.stable` which
contains the frozen v1.0.0 Stable-Pattern Extractor.
"""

from importlib import import_module as _imp

# Lazily expose analyzer via top-level for convenience
stable = _imp("alpha_analytical.stable")

__all__ = ["stable"] 