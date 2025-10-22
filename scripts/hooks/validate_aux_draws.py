#!/usr/bin/env python
"""Pre-commit helper to ensure Aux loaders/resolvers stay canonical."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def build_env() -> dict[str, str]:
    env = os.environ.copy()
    paths = [
        str(ROOT),
        str(ROOT / "src"),
    ]
    existing = env.get("PYTHONPATH")
    if existing:
        paths.append(existing)
    env["PYTHONPATH"] = os.pathsep.join(paths)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env


def run_command(args: list[str], *, env: dict[str, str]) -> None:
    result = subprocess.run(
        [sys.executable, *args],
        cwd=str(ROOT),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if result.stdout:
        sys.stdout.write(result.stdout)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> int:
    if os.environ.get("AAT9_SKIP_AUX_GUARD"):
        return 0

    env = build_env()

    run_command(["scripts/checks/smoke_positional.py"], env=env)

    core_states = ["Connecticut4", "Florida4"]
    run_command(
        ["scripts/tools/validate_aux_doubles.py", *core_states, "--max-n", "1000"],
        env=env,
    )
    run_command(
        [
            "scripts/tools/validate_aux_repeat.py",
            *core_states,
            "--max-n",
            "1000",
            "--window",
            "150",
            "--shortlist-limit",
            "5",
        ],
        env=env,
    )
    run_command(
        [
            "scripts/tools/validate_aux_vtrac.py",
            "Connecticut4",
            "--max-n",
            "1000",
            "--window",
            "150",
            "--limit",
            "10",
        ],
        env=env,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
