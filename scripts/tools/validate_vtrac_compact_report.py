"""
Validate that the VTRAC compact report exists and is non-empty for a sharepack date.

Why:
  `sharepacks/<DATE>/vtrac_compact_report.json` is the global “aggregator feed” artifact.
  It can exist but still be effectively empty (e.g., `states=[]`, `sections=[]`), which
  silently breaks downstream joins/scoring.

Usage:
  python3 scripts/tools/validate_vtrac_compact_report.py --date 2025-06-21
  python3 scripts/tools/validate_vtrac_compact_report.py --path sharepacks/2025-06-21/vtrac_compact_report.json

Exit codes:
  0 = OK (non-empty)
  1 = missing/empty (or invalid JSON)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]


def load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON: {path} ({exc})") from exc


def summarize(data: Dict[str, Any]) -> Tuple[int, int, str]:
    states: List[Any] = data.get("states") or []
    sections: List[Any] = data.get("sections") or []
    version = str(data.get("scorer_version") or "")
    return len(states), len(sections), version


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="Sharepack date folder (YYYY-MM-DD), e.g. 2025-06-21")
    ap.add_argument("--path", help="Explicit path to vtrac_compact_report.json")
    ap.add_argument("--warn-only", action="store_true", help="Print warnings but return exit code 0")
    args = ap.parse_args()

    if not args.path and not args.date:
        raise SystemExit("Provide either --date or --path")

    report_path = Path(args.path) if args.path else (REPO_ROOT / "sharepacks" / args.date / "vtrac_compact_report.json")

    problems: List[str] = []
    if not report_path.exists():
        problems.append(f"missing file: {report_path}")
        states_n = sections_n = 0
        version = ""
    else:
        data = load_json(report_path)
        states_n, sections_n, version = summarize(data)
        if states_n == 0:
            problems.append("compact report has no states (states=[])")
        if sections_n == 0:
            problems.append("compact report has no sections (sections=[])")

    print(f"VTRAC compact report: {report_path}")
    if version:
        print(f"- scorer_version: {version}")
    print(f"- states: {states_n}")
    print(f"- sections: {sections_n}")

    if problems:
        print("\nProblems:")
        for p in problems:
            print(f"- {p}")
        print("\nSuggested fix:")
        print("- Rebuild VTRAC share artifacts, then regenerate/copy into the sharepack date.")
        print(f"- Try: {sys.executable} TOOLS/run_vtrac_share_bundle.py")
        if args.warn_only:
            print("\nWARN-ONLY mode: not failing.")
            return 0
        return 1

    print("\nOK: compact report is present and non-empty.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

