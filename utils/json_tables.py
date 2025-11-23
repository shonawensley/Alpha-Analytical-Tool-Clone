from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

import pandas as pd

SECTION_FILES = {
    "Midday": "Midday_Combined.csv",
    "Evening": "Evening_Combined.csv",
    "Combined": "Combined_Combined.csv",
}

COLUMNS = ["7", "6", "5", "4", "3", "2", "1"]
PATTERN_ROWS = ("R2", "R4", "R6", "R8")


def _empty_draw_entry() -> Dict[str, object]:
    return {
        "draw_data": [],
        "pattern_variations": {row: [] for row in PATTERN_ROWS},
        "metadata": {"hot_zone_count": 0, "is_hot_zone": False},
    }


def _process_section(state: str, section: str, tables_dir: Path) -> Dict[str, Dict[str, dict]]:
    csv_path = tables_dir / SECTION_FILES[section]
    if not csv_path.exists():
        raise FileNotFoundError(f"{csv_path} missing for {state}")
    df = pd.read_csv(csv_path, dtype=str).fillna("")
    sets: Dict[str, Dict[str, dict]] = {}
    for _, row in df.iterrows():
        set_name = str(row["Set"])
        draw_name = str(row["Draw"])
        rowtype = str(row["RowType"])
        entry = sets.setdefault(set_name, {}).setdefault(draw_name, _empty_draw_entry())
        values = [str(row[col]) for col in COLUMNS]
        if rowtype == "draw_data":
            entry["draw_data"] = values
        elif rowtype in PATTERN_ROWS:
            entry["pattern_variations"][rowtype] = values
            hz_count = sum(1 for v in values if "*" in v)
            entry["metadata"]["hot_zone_count"] += hz_count
        entry["metadata"]["is_hot_zone"] = entry["metadata"]["hot_zone_count"] > 0
    return sets


def build_json_tables_from_csv(state: str, tables_dir: str, out_dir: str) -> str:
    """
    Build the JSON mirror (Midday/Evening/Combined) for the given state.
    Returns the path to the JSON file.
    """
    tables_path = Path(tables_dir)
    out_root = Path(out_dir)
    sections: Dict[str, Dict[str, dict]] = {}
    for section in SECTION_FILES:
        sections[section] = {"sets": _process_section(state, section, tables_path)}

    payload = {
        "state_name": state,
        "sections": sections,
    }
    out_root.mkdir(parents=True, exist_ok=True)
    json_path = out_root / f"{state}_tables.json"
    json_path.write_text(json.dumps(payload, indent=2))
    return str(json_path)
