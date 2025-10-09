"""Compat shim exposing the project-level `utils.path_handler` to src.* modules."""
from __future__ import annotations

import importlib.util
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_ORIGINAL_PATH_HANDLER = _PROJECT_ROOT / "utils" / "path_handler.py"

_spec = importlib.util.spec_from_file_location("_aat9_path_handler", _ORIGINAL_PATH_HANDLER)
if _spec is None or _spec.loader is None:
    raise ImportError(f"Unable to load canonical path_handler from {_ORIGINAL_PATH_HANDLER}")

_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

__all__ = [name for name in dir(_module) if not name.startswith('_')]
for name in __all__:
    globals()[name] = getattr(_module, name)
