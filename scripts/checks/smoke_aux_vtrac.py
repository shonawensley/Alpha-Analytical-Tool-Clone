#!/usr/bin/env python
"""Quick smoke test to ensure staged Aux modules expose boxed VTRAC data."""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parents[2]
aux_root = repo_root / 'scripts' / 'auxiliary' / 'working'
if not aux_root.exists():
    raise SystemExit(f'Aux staging path not found: {aux_root}')

sys.path.insert(0, str(aux_root))
# Evict any existing `modules` package so we bind to the staged copy
for key in list(sys.modules):
    if key == 'modules' or key.startswith('modules.'):
        del sys.modules[key]

analyze_pairs = importlib.import_module('modules.analyze_pairs')
vtrac_reference = importlib.import_module('modules.vtrac_reference')

print(f"analyze_pairs: {getattr(analyze_pairs, '__file__', 'unknown')}")
print(f"vtrac_reference: {getattr(vtrac_reference, '__file__', 'unknown')}")

missing = []
for attr in ('VTRAC_DISPLAY', 'BOXED_LABEL_LOOKUP'):
    if not hasattr(vtrac_reference, attr):
        missing.append(attr)
    print(f"has {attr}: {hasattr(vtrac_reference, attr)}")

if missing:
    raise SystemExit(f'Missing boxed attributes: {", ".join(missing)}')

# Auxiliary VTRAC staging smoke test

