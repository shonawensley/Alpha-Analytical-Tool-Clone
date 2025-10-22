#!/usr/bin/env python
"""Pre-commit helper to run stdlib py_compile on changed Python files."""

from __future__ import annotations

import importlib
import sys
import tempfile
from pathlib import Path


sys.dont_write_bytecode = True


def main(paths: list[str]) -> int:
    std_py_compile = importlib.import_module("py_compile")
    had_error = False
    for raw in paths:
        path = Path(raw)
        if path.suffix != ".py" or "cp1252" in path.stem.lower():
            continue
        try:
            tmp_file = tempfile.NamedTemporaryFile(suffix=".pyc", delete=False)
            cache_path = Path(tmp_file.name)
            tmp_file.close()
            std_py_compile.compile(str(path), cfile=str(cache_path), doraise=True)
        except std_py_compile.PyCompileError as exc:  # type: ignore[attr-defined]
            had_error = True
            sys.stderr.write(f"py_compile failed: {path}\n{exc.msg}\n")
        finally:
            try:
                if cache_path.exists():
                    cache_path.unlink()
            except OSError:
                pass
    return 1 if had_error else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
