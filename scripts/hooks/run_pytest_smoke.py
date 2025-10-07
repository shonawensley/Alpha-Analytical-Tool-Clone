#!/usr/bin/env python
"""Pre-commit helper to execute the smoke subset of acceptance tests."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "run_acceptance.py"


def build_env() -> dict[str, str]:
    env = os.environ.copy()
    paths = [str(ROOT), str(ROOT / "src"), str(ROOT / "scripts" / "auxiliary" / "working")]
    existing = env.get("PYTHONPATH")
    if existing:
        paths.append(existing)
    env["PYTHONPATH"] = os.pathsep.join(paths)
    return env


def main(args: list[str] | None = None) -> int:
    env = build_env()

    if os.environ.get('AAT9_RUN_DOUBLES_HEALTH'):
        cmd = [sys.executable, 'scripts/health/check_doubles_variants.py']
        rc = subprocess.call(cmd, cwd=str(ROOT), env=env)
        if rc != 0:
            return rc
    cmd = [sys.executable, str(SCRIPT), "--marker", "smoke", "--", "--maxfail", "1"]
    return subprocess.call(cmd, cwd=str(ROOT), env=env)


if __name__ == "__main__":
    sys.exit(main())
