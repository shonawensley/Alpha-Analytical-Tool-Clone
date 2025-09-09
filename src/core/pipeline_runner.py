from __future__ import annotations

import os
import io
import shutil
from datetime import datetime
from typing import Dict, Any

from utils import path_handler as ph


def _archive_original(excel_path: str) -> None:
    if os.path.exists(excel_path):
        root = ph.get_original_data_dir()
        archive_dir = os.path.join(root, "archive", datetime.now().strftime("%Y%m%d_%H%M%S"))
        os.makedirs(archive_dir, exist_ok=True)
        shutil.move(excel_path, os.path.join(archive_dir, os.path.basename(excel_path)))


def _write_original_excel(bytes_data: bytes, dest_path: str) -> None:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "wb") as fh:
        fh.write(bytes_data)


def run_pipeline_from_original_path(excel_path: str) -> Dict[str, Any]:
    """
    Run the tables pipeline using an existing Pick3StatsC4.xlsm on disk.
    Returns a summary dict with counts and destinations.
    """
    from src.utils.clean_data import clean_all_states, STATES  # type: ignore
    from src.utils.extract_data import extract_all_states      # type: ignore
    from src.utils.table_generator import build_combined_table # type: ignore
    import pandas as pd

    cleaned_dir = ph.get_cleaned_data_dir()
    tables_root = ph.get_tables_output_dir()

    # 1) Clean all states -> *_cleaned.xlsx
    res_clean = clean_all_states(STATES, excel_path, cleaned_dir)

    # 2) Extract all states
    extracted = extract_all_states(STATES, cleaned_dir)

    # 3) Build per-state combined tables and write CSVs
    os.makedirs(tables_root, exist_ok=True)
    written_states = 0
    for state, data in extracted.items():
        state_dir = os.path.join(tables_root, state)
        os.makedirs(state_dir, exist_ok=True)
        # Build combined tables for each section
        for section in ("Midday", "Evening", "Combined"):
            try:
                section_data = data.get(section) or {}
                df = build_combined_table(section_data)
                # Match Stable extractor glob pattern *Combined*.csv
                out_name = f"{section}_Combined.csv"
                df.to_csv(os.path.join(state_dir, out_name), index=False)
            except Exception:
                continue
        written_states += 1

    return {
        "clean_success": len(res_clean.get("success", [])),
        "clean_failed": res_clean.get("failed", []),
        "states_extracted": len(extracted),
        "tables_root": tables_root,
        "written_states": written_states,
    }


def run_pipeline_from_bytes(excel_bytes: bytes) -> Dict[str, Any]:
    """
    Save uploaded Excel to data/original/, archive previous copy, then run pipeline.
    Returns a summary dict.
    """
    dest = ph.get_excel_path()
    _archive_original(dest)
    _write_original_excel(excel_bytes, dest)
    return run_pipeline_from_original_path(dest)
