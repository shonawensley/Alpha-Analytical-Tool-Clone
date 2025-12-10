"""
Validate per-state table naming patterns (generic vs state-prefixed) and report missing variants.

Usage:
  python3 scripts/tools/validate_tables_naming.py

Outputs a report to stdout summarizing:
  - Which states have prefixed tables present
  - Which states fell back to generic names
  - Missing variant files
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List

from utils import path_handler as ph


def scan_states(states: List[str]) -> Dict[str, Dict]:
    results = {}
    for state in states:
        info = ph.resolve_state_table_paths(state)
        combined = info.get("Combined")
        midday = info.get("Midday")
        evening = info.get("Evening")
        missing = [k for k, v in [("Combined", combined), ("Midday", midday), ("Evening", evening)] if v is None]
        warnings = info.get("warnings", [])
        results[state] = {
            "combined": combined,
            "midday": midday,
            "evening": evening,
            "missing": missing,
            "warnings": warnings,
        }
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--states",
        nargs="*",
        help="States to check (default: all known states from cleaned data dir)",
    )
    parser.add_argument("--json-out", help="Optional JSON output file")
    args = parser.parse_args()

    if args.states:
        states = args.states
    else:
        # infer from tables directory
        tables_root = Path(ph.get_tables_output_dir())
        states = [p.name for p in tables_root.iterdir() if p.is_dir()]

    results = scan_states(states)

    # Print summary
    print("Table naming validation:")
    for state, info in sorted(results.items()):
        missing = info["missing"]
        warn = info["warnings"]
        status = "OK"
        if missing:
            status = f"Missing: {','.join(missing)}"
        elif warn:
            status = f"Fallback: {len(warn)} warning(s)"
        print(f"- {state}: {status}")
        if warn:
            for w in warn:
                print(f"    warn: {w}")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
