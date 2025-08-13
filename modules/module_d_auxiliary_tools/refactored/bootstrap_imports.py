"""
Minimal bootstrap to resolve legacy imports for Aux tools only.

Responsibilities:
- Ensure legacy directory is on sys.path
- Register rich legacy reference as "modules.vtrac_reference"

Safe: does not touch any other tools or global state outside Aux usage.
"""

from __future__ import annotations

import sys
import importlib.util
from pathlib import Path


def init() -> None:

    legacy_dir = (
        Path(__file__).resolve().parents[1]
        / "core_legacy"
        / "legacy_modules_backup"
    )

    # Make sure legacy code is importable
    legacy_dir_str = str(legacy_dir)
    if legacy_dir_str not in sys.path:
        sys.path.insert(0, legacy_dir_str)

    # Provide the expected legacy module name for old code
    vr_path = legacy_dir / "vtrac_reference.py"
    if "modules.vtrac_reference" not in sys.modules and vr_path.exists():
        spec = importlib.util.spec_from_file_location(
            "modules.vtrac_reference", str(vr_path)
        )
        if spec and spec.loader:
            vr_mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(vr_mod)
            sys.modules["modules.vtrac_reference"] = vr_mod


__all__ = ["init"]


