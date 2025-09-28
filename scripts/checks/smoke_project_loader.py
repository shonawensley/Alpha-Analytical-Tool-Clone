"""Smoke check that _load_project_module registers modules correctly.

Usage:
    python scripts/checks/smoke_project_loader.py

The script imports src.app._load_project_module and verifies that the
positional tool module is registered in sys.modules and exposes its
public API after being loaded dynamically.
"""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    # Ensure project root and src directory are on sys.path
    root = Path(__file__).resolve().parents[2]
    sys_path_inserts = [str(root), str(root / "src")]
    for entry in reversed(sys_path_inserts):
        if entry not in sys.path:
            sys.path.insert(0, entry)

    from src.app import _load_project_module  # type: ignore

    dotted_name = "project_positional_tool_smoke"
    target_rel_path = "modules/module_d_auxiliary_tools/refactored/positional_tool.py"

    # Ensure we start from a clean state for this dotted name.
    sys.modules.pop(dotted_name, None)

    module_obj = _load_project_module(dotted_name, target_rel_path)

    if sys.modules.get(dotted_name) is not module_obj:
        raise SystemExit("loader did not register module in sys.modules")

    if not hasattr(module_obj, "analyze_state_variants"):
        raise SystemExit("positional tool missing analyze_state_variants")

    print("loader smoke: OK")


if __name__ == "__main__":
    main()
