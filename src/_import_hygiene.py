from __future__ import annotations

import os
import sys
from pathlib import Path
from contextlib import contextmanager


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def ensure_project_root_on_syspath() -> None:
    rp = str(PROJECT_ROOT)
    if rp in sys.path:
        try:
            sys.path.remove(rp)
        except ValueError:
            pass
    sys.path.insert(0, rp)


def evict_staged_modules_for_non_aux() -> None:
    m = sys.modules.get('modules')
    if not m:
        return
    path_norm = ('%s' % getattr(m, '__file__', '')).replace('\\', '/').lower()
    if '/scripts/auxiliary/working/modules/' in path_norm:
        sys.modules.pop('modules', None)


def evict_legacy_utils_shim() -> None:
    mod = sys.modules.get('utils')
    if not mod:
        return
    mod_path = str(getattr(mod, '__file__', '')).replace('\\', '/').lower()
    if '/src/utils/' not in mod_path:
        return
    targets = [name for name in list(sys.modules) if name == 'utils' or name.startswith('utils.')]
    for name in targets:
        sys.modules.pop(name, None)


@contextmanager
def project_modules_first():
    """Temporarily prioritize project modules/ for imports."""
    rp = str(PROJECT_ROOT / 'modules')
    old = list(sys.path)
    try:
        ensure_project_root_on_syspath()
        evict_legacy_utils_shim()
        if rp in sys.path:
            try:
                sys.path.remove(rp)
            except ValueError:
                pass
        sys.path.insert(0, rp)
        yield
    finally:
        sys.path[:] = old

