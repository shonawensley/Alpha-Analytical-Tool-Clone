from __future__ import annotations

import importlib
import sys
from pathlib import Path
from types import ModuleType


def test_winner_report_full_import_survives_legacy_utils_shadowing():
    root = Path(__file__).resolve().parents[1]
    src = root / "src"

    original_sys_path = list(sys.path)
    preserved_modules = {
        name: sys.modules[name]
        for name in list(sys.modules)
        if name == "utils" or name.startswith("utils.") or name.startswith("modules.winner_report_full")
    }
    try:
        if str(src) not in sys.path:
            sys.path.insert(0, str(src))
        if str(root) not in sys.path:
            sys.path.insert(1, str(root))

        # Create stub legacy modules that look like the shim.
        legacy_utils = ModuleType("utils")
        legacy_utils.__file__ = str(src / "utils" / "__init__.py")
        legacy_path_handler = ModuleType("utils.path_handler")
        legacy_path_handler.__file__ = str(src / "utils" / "path_handler.py")

        sys.modules["utils"] = legacy_utils
        sys.modules["utils.path_handler"] = legacy_path_handler

        sys.modules.pop("modules.winner_report_full", None)
        module = importlib.import_module("modules.winner_report_full")

        assert hasattr(module, "write_winner_full_report")
        utils_module = importlib.import_module("utils")
        utils_path = str(getattr(utils_module, "__file__", "")).replace("\\", "/")
        assert "/src/utils/" not in utils_path
    finally:
        sys.path[:] = original_sys_path
        for name in list(sys.modules):
            if name == "utils" or name.startswith("utils.") or name.startswith("modules.winner_report_full"):
                sys.modules.pop(name, None)
        sys.modules.update(preserved_modules)
