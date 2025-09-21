"""
Minimal bootstrap to resolve legacy imports for Aux tools only.

Responsibilities:
- Ensure legacy directory is on sys.path
- Register rich legacy reference as `modules.vtrac_reference` (legacy copy)

Safe: does not touch other tools outside Aux usage.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def _load_module_from_path(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    if not spec or not spec.loader:
        raise ImportError(f"Cannot load module {name!r} from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module

def init() -> None:
    """Make legacy Aux modules importable (boxed VTRAC, analyze_pairs)."""
    existing = sys.modules.get('vtrac_reference')
    if existing and hasattr(existing, 'BOXED_LABEL_LOOKUP'):
        return

    repo_root = Path(__file__).resolve().parents[3]
    candidate_bases = [
        repo_root / 'modules' / 'module_d_auxiliary_tools' / 'core_legacy' / 'legacy_modules_backup',
        repo_root / 'archived' / 'vtrac_refs',
    ]

    for base in candidate_bases:
        if not base.exists():
            continue

        vtrac_candidates = [
            base / 'modules' / 'vtrac_reference.py',
            base / 'vtrac_reference.py',
            base / 'legacy_2_modules_vtrac_reference.py',
            base / 'core_legacy_backup_vtrac_reference.py',
        ]
        vtrac_path = next((p for p in vtrac_candidates if p.exists()), None)
        if not vtrac_path:
            continue

        module = _load_module_from_path('vtrac_reference', vtrac_path)
        sys.modules['vtrac_reference'] = module
        sys.modules['modules.vtrac_reference'] = module

        analyze_candidates = [
            base / 'analyze_pairs.py',
            base / 'modules' / 'analyze_pairs.py',
        ]
        analyze_path = next((p for p in analyze_candidates if p.exists()), None)
        if analyze_path and 'analyze_pairs' not in sys.modules:
            analyze_module = _load_module_from_path('analyze_pairs', analyze_path)
            sys.modules['analyze_pairs'] = analyze_module

        base_str = str(base)
        if base_str not in sys.path:
            sys.path.insert(0, base_str)
        modules_dir = base / 'modules'
        modules_dir_str = str(modules_dir)
        if modules_dir.exists() and modules_dir_str not in sys.path:
            sys.path.insert(0, modules_dir_str)
        return

    raise ImportError('Legacy vtrac_reference.py not found in expected locations')


__all__ = ['init']
