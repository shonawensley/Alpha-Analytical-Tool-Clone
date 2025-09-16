#!/usr/bin/env python
"""
CLI smoke script: build analyzer-style Winners full report without Streamlit.

Usage:
  python scripts/smoke/build_winners_full.py <STATE4> <WINNER>

Example:
  python scripts/smoke/build_winners_full.py Connecticut4 224
"""
from __future__ import annotations

import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    _, state4, winner = argv

    # Ensure project root and src on sys.path
    root = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(root))
    sys.path.insert(0, str(root / 'src'))

    # Fix utils binding to top-level utils, then re-add src for core\n    # Temporarily remove any src entries\n    orig = list(sys.path)\n    sys.path = [p for p in sys.path if not p.endswith('\\src') and not p.endswith('/src')]\n    import importlib as _il\n    try:\n        _il.invalidate_caches()\n        _ph = _il.import_module('utils.path_handler')\n        sys.modules['utils.path_handler'] = _ph\n    except Exception:\n        pass\n    # Restore sys.path with src so core.* imports work\n    sys.path = orig

    try:
        from modules.winner_report_full import write_winner_full_report as build_full
    except Exception as e:
        print(f"Import error: {e}")
        return 1

    try:
        out = build_full(state4, winner)
        print(out)
        return 0
    except Exception as e:
        print(f"Build failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))



