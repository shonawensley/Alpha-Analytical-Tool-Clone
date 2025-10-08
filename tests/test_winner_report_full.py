from __future__ import annotations

import importlib
import sys
from pathlib import Path
from types import ModuleType


def test_winner_report_full_import_survives_legacy_utils_shadowing():
    repo_root = Path(__file__).resolve().parents[1]
    src_dir = repo_root / "src"
    modules_dir = repo_root / "modules"
    repo_root_str = repo_root.as_posix()
    src_str = src_dir.as_posix()

    original_sys_path = list(sys.path)
    preserved_modules = {
        name: sys.modules[name]
        for name in list(sys.modules)
        if name == "utils" or name.startswith("utils.") or name.startswith("modules.winner_report_full")
    }
    try:
        new_sys_path = []
        for path_entry in sys.path:
            entry_norm = Path(path_entry).as_posix()
            if repo_root_str in entry_norm or src_str in entry_norm:
                continue
            new_sys_path.append(path_entry)
        new_sys_path.insert(0, str(modules_dir))
        sys.path[:] = new_sys_path

        legacy_utils = ModuleType("utils")
        legacy_utils.__file__ = str(src_dir / "utils" / "__init__.py")
        legacy_path_handler = ModuleType("utils.path_handler")
        legacy_path_handler.__file__ = str(src_dir / "utils" / "path_handler.py")

        sys.modules["utils"] = legacy_utils
        sys.modules["utils.path_handler"] = legacy_path_handler

        sys.modules.pop("modules.winner_report_full", None)
        module = importlib.import_module("modules.winner_report_full")

        assert hasattr(module, "write_winner_full_report")
        utils_module = importlib.import_module("utils")
        utils_path = Path(getattr(utils_module, "__file__", "")).as_posix()
        assert repo_root_str in utils_path and "/src/utils/" not in utils_path

        core_module = importlib.import_module("core.module_c_vtrac")
        assert core_module is not None
    finally:
        sys.path[:] = original_sys_path
        for name in list(sys.modules):
            if name == "utils" or name.startswith("utils.") or name.startswith("modules.winner_report_full"):
                sys.modules.pop(name, None)
        sys.modules.update(preserved_modules)

def test_no_function_local_import_os():
    text = Path("src/app.py").read_text(encoding="utf-8")
    shadow_lines = [line for line in text.splitlines() if line.strip().startswith("import os") and line.strip() != "import os"]
    assert not shadow_lines, f"unexpected function-level os imports: {shadow_lines}"
