#!/usr/bin/env python3
"""
Build a shareable ZIP that bundles the entire V-TRAC validation outputs plus
the rendered winners HTML artifacts. Deploy this when a reviewer wants the
full dataset instead of just summary.md/summary.csv.

Sources:
    data/outputs/analysis/vtrac_validation/**
    data/outputs/analysis/winners/**

Destination:
    data/outputs/analysis/vtrac_validation/vtrac_validation_full_payload.zip
"""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
VALIDATION_DIR = ROOT / "data/outputs/analysis/vtrac_validation"
WINNERS_DIR = ROOT / "data/outputs/analysis/winners"
OUTPUT_ZIP = VALIDATION_DIR / "vtrac_validation_full_payload.zip"


def iter_files(base: Path) -> Iterable[Path]:
    if not base.exists():
        return []
    return [path for path in base.rglob("*") if path.is_file()]


def add_tree(zf: zipfile.ZipFile, base: Path, count: int) -> int:
    for file_path in iter_files(base):
        arcname = file_path.relative_to(ROOT).as_posix()
        zf.write(file_path, arcname)
        count += 1
    return count


def build_zip() -> None:
    OUTPUT_ZIP.parent.mkdir(parents=True, exist_ok=True)
    file_count = 0
    with zipfile.ZipFile(OUTPUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for source in (VALIDATION_DIR, WINNERS_DIR):
            if source.exists():
                file_count = add_tree(zf, source, file_count)
    size_bytes = OUTPUT_ZIP.stat().st_size if OUTPUT_ZIP.exists() else 0
    print(f"Wrote {OUTPUT_ZIP} ({file_count} files, {size_bytes/1024:.1f} KiB)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    missing = [str(p) for p in (VALIDATION_DIR, WINNERS_DIR) if not p.exists()]
    if missing:
        print("Warning: missing sources -> " + ", ".join(missing), file=sys.stderr)
    build_zip()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
