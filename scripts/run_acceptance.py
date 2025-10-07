#!/usr/bin/env python
"""Run the acceptance (or smoke) test suite with consistent PYTHONPATH setup."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
AUX = ROOT / "scripts" / "auxiliary" / "working"


def _build_env() -> dict[str, str]:
    env = os.environ.copy()
    paths = [str(ROOT), str(SRC), str(AUX)]
    existing = env.get("PYTHONPATH")
    if existing:
        paths.append(existing)
    env["PYTHONPATH"] = os.pathsep.join(paths)
    return env


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run pytest with the acceptance or smoke marker.")
    parser.add_argument(
        "--with-doubles-health",
        action="store_true",
        help="Run the doubles variant health audit before pytest.",
    )
    parser.add_argument(
        "--marker",
        default="acceptance",
        help="Pytest marker to run (defaults to 'acceptance').",
    )
    parser.add_argument(
        "pytest_args",
        nargs=argparse.REMAINDER,
        help="Additional arguments passed directly to pytest (after '--').",
    )
    args = parser.parse_args(argv)

    pytest_args = args.pytest_args or []
    if pytest_args and pytest_args[0] == "--":
        pytest_args = pytest_args[1:]

    default_targets = ["tests/acceptance"]
    env = _build_env()

    if args.with_doubles_health:
        health_cmd = [sys.executable, "scripts/health/check_doubles_variants.py"]
        health_rc = subprocess.call(health_cmd, cwd=str(ROOT), env=env)
        if health_rc != 0:
            return int(health_rc)

    cmd = [sys.executable, "-m", "pytest", "-m", args.marker] + default_targets + pytest_args
    result = subprocess.call(cmd, cwd=str(ROOT), env=env)
    return int(result)


if __name__ == "__main__":
    sys.exit(main())
