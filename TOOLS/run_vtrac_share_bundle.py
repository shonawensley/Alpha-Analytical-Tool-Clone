#!/usr/bin/env python3
"""
One-click helper to rebuild all shareable V-TRAC artifacts.

Runs, in order:
    1. make_pro_payload.py           → summary.md / summary.csv
    2. vtrac_score_and_export.py     → vtrac_compact_report.json / .csv
    3. make_vtrac_full_payload.py    → optional bulk ZIP

Usage:
    python TOOLS/run_vtrac_share_bundle.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATION_DIR = ROOT / "data/outputs/analysis/vtrac_validation"


def run_step(description: str, argv: list[str]) -> None:
    print(f"\n🚀 {description}")
    print("   $" + " ".join(argv))
    try:
        subprocess.run(argv, check=True, cwd=ROOT)
    except subprocess.CalledProcessError as exc:
        print(f"❌ {description} failed with code {exc.returncode}", file=sys.stderr)
        raise


def main() -> int:
    if not VALIDATION_DIR.exists():
        print(
            "⚠️  Validation folder is missing. Run the enhanced validator first.\n"
            f"Expected: {VALIDATION_DIR}",
            file=sys.stderr,
        )
        return 1

    run_step(
        "Building summary.md / summary.csv",
        [sys.executable, "TOOLS/make_pro_payload.py"],
    )
    run_step(
        "Scoring sections → vtrac_compact_report.*",
        [
            sys.executable,
            "TOOLS/vtrac_score_and_export.py",
            "data/outputs/analysis/vtrac",
            str(VALIDATION_DIR),
            "--output",
            str(VALIDATION_DIR),
        ],
    )
    run_step(
        "Packaging optional full payload ZIP",
        [sys.executable, "TOOLS/make_vtrac_full_payload.py"],
    )

    print(
        "\n✅ Done. Publish (commit/push) these artifacts if you need to share:\n"
        "  - data/outputs/analysis/vtrac_validation/summary.md\n"
        "  - data/outputs/analysis/vtrac_validation/summary.csv\n"
        "  - data/outputs/analysis/vtrac_validation/vtrac_compact_report.json\n"
        "  - data/outputs/analysis/vtrac_validation/vtrac_compact_report.csv\n"
        "  - data/outputs/analysis/vtrac_validation/vtrac_validation_full_payload.zip (optional)\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
