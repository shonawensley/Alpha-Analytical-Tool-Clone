from __future__ import annotations

import hashlib
import io
import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from utils import path_handler as ph
from utils.json_tables import build_json_tables_from_csv


MANIFEST_PATH = Path(ph.get_tables_manifest_path())


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


def _purge_state_tables(state_dir: str) -> None:
    """Remove existing CSV tables for a state before writing refreshed versions."""
    if not os.path.isdir(state_dir):
        return
    for entry in Path(state_dir).glob("*.csv"):
        try:
            entry.unlink()
        except OSError:
            continue


def _hash_file(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    digest = hashlib.md5()
    try:
        with path.open("rb") as fh:
            for chunk in iter(lambda: fh.read(8192), b""):
                digest.update(chunk)
    except OSError:
        return None
    return digest.hexdigest()


def _load_manifest() -> Dict[str, Any]:
    if not MANIFEST_PATH.exists():
        return {}
    try:
        return json.loads(MANIFEST_PATH.read_text())
    except (OSError, json.JSONDecodeError):
        return {}


def _write_manifest(manifest: Dict[str, Any]) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, sort_keys=True))


def _describe_workbook(excel_path: str) -> Dict[str, Any]:
    excel = Path(excel_path)
    info: Dict[str, Any] = {
        "path": str(excel.resolve()) if excel.exists() else str(excel),
        "exists": excel.exists(),
    }
    if excel.exists():
        stat = excel.stat()
        info.update(
            {
                "mtime": stat.st_mtime,
                "size": stat.st_size,
            }
        )
    return info


def _summarize_checksums(state_dirs: Dict[str, str]) -> Dict[str, Any]:
    states_summary: Dict[str, Any] = {}
    for state, state_dir in state_dirs.items():
        combined_file = Path(state_dir) / "Combined_Combined.csv"
        checksum = _hash_file(combined_file)
        states_summary[state] = {
            "combined_checksum": checksum,
            "updated": datetime.utcnow().isoformat(),
        }
    return states_summary


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
    state_dirs: Dict[str, str] = {}
    for state, data in extracted.items():
        state_dir = os.path.join(tables_root, state)
        os.makedirs(state_dir, exist_ok=True)
        _purge_state_tables(state_dir)
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
        state_dirs[state] = state_dir

    json_root = ph.get_json_tables_dir()
    for state, state_dir in state_dirs.items():
        try:
            build_json_tables_from_csv(state, state_dir, json_root)
        except Exception:
            continue

    summary = {
        "clean_success": len(res_clean.get("success", [])),
        "clean_failed": res_clean.get("failed", []),
        "states_extracted": len(extracted),
        "tables_root": tables_root,
        "written_states": written_states,
        "state_dirs": state_dirs,
    }
    summary["json_root"] = json_root
    return summary


def run_pipeline_from_bytes(excel_bytes: bytes) -> Dict[str, Any]:
    """
    Save uploaded Excel to data/original/, archive previous copy, then run pipeline.
    Returns a summary dict.
    """
    dest = ph.get_excel_path()
    _archive_original(dest)
    _write_original_excel(excel_bytes, dest)
    summary = run_pipeline_from_original_path(dest)
    workbook_info = _describe_workbook(dest)
    state_dirs = summary.get("state_dirs") or {}
    manifest = {
        "generated_at": datetime.utcnow().isoformat(),
        "workbook": workbook_info,
        "states": _summarize_checksums(state_dirs),
    }
    _write_manifest(manifest)
    return summary


def run_tables_with_guard(excel_path: str) -> Dict[str, Any]:
    """
    Regenerate tables only when the workbook changed.
    Returns the pipeline summary (and skips work otherwise).
    """
    workbook_info = _describe_workbook(excel_path)
    manifest = _load_manifest()
    workbook_matches = manifest.get("workbook") == workbook_info if manifest else False
    if workbook_matches and MANIFEST_PATH.exists():
        return {
            "skipped": True,
            "reason": "tables up-to-date",
            "manifest": manifest,
        }

    summary = run_pipeline_from_original_path(excel_path)
    state_dirs = summary.get("state_dirs") or {}
    manifest = {
        "generated_at": datetime.utcnow().isoformat(),
        "workbook": workbook_info,
        "states": _summarize_checksums(state_dirs),
    }
    _write_manifest(manifest)
    summary["manifest"] = manifest
    return summary
