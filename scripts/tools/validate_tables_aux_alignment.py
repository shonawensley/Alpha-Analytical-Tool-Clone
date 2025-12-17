#!/usr/bin/env python3
"""
Validate that string tables and Aux draw CSVs describe the SAME "world snapshot".

Why this matters
----------------
When swapping workbooks (Pick3StatsC4), it's possible for:
- string tables to reflect one workbook snapshot (D-1), while
- Aux draw CSVs reflect another (or "today's live" draws after a later swap).

That mismatch can silently invalidate Master Validation Part 3 and any
tool/aux cross-analysis.

This validator compares the newest draws:
- Aux: newest 5 draws per variant (Combined/Midday/Evening)
- Tables: Set1/Draw1 draw_data row newest 5 (reverse of last 5 columns)

Modes
-----
1) Live (no sharepack):
   python3 scripts/tools/validate_tables_aux_alignment.py --state OntarioCanada4

2) Sharepack (recommended for Master Validation):
   python3 scripts/tools/validate_tables_aux_alignment.py --date 2025-06-21 --state OntarioCanada4
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if SRC.exists() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from modules.aux_loaders import load_state_draws  # noqa: E402

VARIANTS: Tuple[str, ...] = ("combined", "midday", "evening")
TABLE_FILES = {
    "combined": "Combined_Combined.csv",
    "midday": "Midday_Combined.csv",
    "evening": "Evening_Combined.csv",
}


def read_table_set1_draw1_latest5(path: Path) -> List[str]:
    if not path.exists():
        raise FileNotFoundError(str(path))
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 4:
                continue
            if row[0] == "Set1" and row[1] == "Draw1" and row[2] == "draw_data":
                values = [v.strip() for v in row[3:] if v is not None and str(v).strip() != ""]
                if len(values) < 5:
                    raise ValueError(f"Not enough draw_data values in {path} (got {len(values)})")
                return list(reversed(values[-5:]))
    raise ValueError(f"Set1,Draw1,draw_data row not found in {path}")


def resolve_table_dir(*, date: str | None, state: str) -> Path:
    if date:
        return ROOT / "sharepacks" / date / state / "tables"
    return ROOT / "data" / "outputs" / "tables" / state


def resolve_aux_base(*, date: str | None, state: str) -> Path | None:
    if date:
        base = ROOT / "sharepacks" / date / state / "aux" / "draws"
        return base if base.exists() else None
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", required=True, help="State key (e.g., OntarioCanada4)")
    ap.add_argument("--date", help="Sharepack results date D (YYYY-MM-DD); when set, validates sharepack tables vs sharepack aux snapshot")
    ap.add_argument("--max-n", type=int, default=1000, help="Max draws to load for Aux (default: 1000)")
    ap.add_argument("--strict", action="store_true", help="Fail if sharepack aux snapshot dir is missing (sharepack mode only)")
    args = ap.parse_args()

    state: str = args.state
    date: str | None = args.date
    max_n: int = args.max_n

    table_dir = resolve_table_dir(date=date, state=state)
    aux_base = resolve_aux_base(date=date, state=state)

    if date and args.strict and aux_base is None:
        raise SystemExit(
            f"[FAIL] Sharepack aux snapshot missing: sharepacks/{date}/{state}/aux/draws/ "
            f"(run aux_sharepack_summary.py --date {date} --state {state} --excel <D-1 workbook>)"
        )

    failures: List[str] = []
    details: Dict[str, Dict[str, List[str]]] = {}

    for variant in VARIANTS:
        table_path = table_dir / TABLE_FILES[variant]
        try:
            table_latest5 = read_table_set1_draw1_latest5(table_path)
        except Exception as exc:
            failures.append(f"{variant}: table read failed ({exc})")
            continue

        draws, resolved = load_state_draws(state, variant=variant, base=aux_base, max_n=max_n)
        aux_latest5 = draws[:5]
        details[variant] = {
            "table_latest5": table_latest5,
            "aux_latest5": aux_latest5,
        }
        if table_latest5 != aux_latest5:
            where = f"sharepacks/{date}/{state}" if date else f"data/outputs/tables/{state}"
            failures.append(
                f"{variant}: mismatch at {where} | table={table_latest5} | aux={aux_latest5} | aux_path={resolved}"
            )

    if failures:
        print("[FAIL] Tables vs Aux alignment check failed:\n")
        for line in failures:
            print("-", line)
        raise SystemExit(1)

    where = f"sharepacks/{date}/{state}" if date else f"data/outputs/tables/{state}"
    print(f"[OK] Tables vs Aux alignment: {state} ({where})")
    if date and aux_base is None:
        print("     Note: sharepack aux snapshot dir missing; Aux compared against live draws (non-strict mode).")


if __name__ == "__main__":
    main()

