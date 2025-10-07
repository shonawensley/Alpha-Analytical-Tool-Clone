#!/usr/bin/env python
"""Pre-commit helper to py_compile changed Python files."""

from __future__ import annotations

import py_compile
import sys
from pathlib import Path


def main(paths: list[str]) -> int:
    had_error = False
    for raw in paths:
        path = Path(raw)
        if path.suffix != ".py":
            continue
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as exc:
            had_error = True
            sys.stderr.write(f"py_compile failed: {path}\n{exc.msg}\n")
    return 1 if had_error else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
