"""Test bootstrap: ensure staged modules resolve during pytest runs."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
STAGED_MODULES = ROOT / "scripts" / "auxiliary" / "working"


def _norm(path: str) -> str:
    try:
        return str(Path(path).resolve())
    except Exception:
        return path

norm_paths = [_norm(p) for p in sys.path]
staged_norm = _norm(str(STAGED_MODULES))

sys.path = [p for p, n in zip(sys.path, norm_paths) if n != staged_norm]
norm_paths = [_norm(p) for p in sys.path]

for candidate in (SRC, ROOT):
    candidate_norm = _norm(str(candidate))
    if candidate_norm not in norm_paths:
        sys.path.insert(0, str(candidate))
        norm_paths.insert(0, candidate_norm)

if STAGED_MODULES.exists() and staged_norm not in norm_paths:
    sys.path.append(str(STAGED_MODULES))
    norm_paths.append(staged_norm)