"""Canonical module bootstrap helpers."""
from __future__ import annotations

import importlib
import sys
from pathlib import Path
from typing import Dict

_CANONICAL_ALIASES = {
    "modules.vtrac_reference": "vtrac_reference",
    "modules.analyze_pairs": "analyze_pairs",
}


def _same_file(mod_a, mod_b) -> bool:
    try:
        return Path(mod_a.__file__).resolve() == Path(mod_b.__file__).resolve()
    except Exception:
        return False


def ensure_ssot() -> Dict[str, str]:
    """Ensure canonical modules are loaded and alias legacy names."""
    loaded: Dict[str, str] = {}
    for canonical, alias in _CANONICAL_ALIASES.items():
        module = importlib.import_module(canonical)
        loaded[canonical] = getattr(module, "__file__", "")
        sys.modules[canonical] = module
        if alias in sys.modules and not _same_file(sys.modules[alias], module):
            # Overwrite any staged copy with the canonical module.
            sys.modules[alias] = module
        else:
            sys.modules[alias] = module
    return loaded


__all__ = ["ensure_ssot"]
