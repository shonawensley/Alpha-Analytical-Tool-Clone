from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml


CONFIG_PATH = Path(__file__).with_suffix(".yml")
CFG: Dict[str, Any] = {}


def load_config(path: Path | None = None) -> Dict[str, Any]:
    """Load the stable feature configuration YAML."""
    config_path = path or CONFIG_PATH
    with config_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return dict(data)


def reload() -> Dict[str, Any]:
    """Reload CFG in-place and return the updated mapping."""
    global CFG
    CFG = load_config()
    return CFG


# Populate CFG on import so downstream modules can rely on it immediately.
reload()


__all__ = ["CFG", "CONFIG_PATH", "load_config", "reload"]
