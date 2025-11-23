#!/usr/bin/env python
"""
path_handler.py - Centralized path management for lottery data processing

This module:
1. Defines standard paths for all project directories and files
2. Provides functions to resolve paths consistently across modules
3. Creates required directories if they don't exist
4. Handles path operations for input, output, and intermediate files
"""

import os
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_PICK3_FILENAME = "Pick3StatsC4.xlsm"
PICK3_PATTERN = "Pick3StatsC4*.xlsm"

def get_project_root():
    """Get the absolute path to the project root directory"""
    # Start at this file's location
    current_file = os.path.abspath(__file__)
    # Go up to utils, then project root
    utils_dir = os.path.dirname(current_file)
    return os.path.dirname(utils_dir)  # One level up from utils is project root

def get_current_date_str():
    """Get the current date as a string in YYYY-MM-DD format"""
    return datetime.now().strftime("%Y-%m-%d")

def get_data_dir():
    """Get the data directory path"""
    return os.path.join(get_project_root(), "data")

def get_original_data_dir():
    """Get the original data directory path"""
    return os.path.join(get_data_dir(), "original")

def get_cleaned_data_dir():
    """Get the cleaned data directory path"""
    return os.path.join(get_data_dir(), "cleaned")

def get_outputs_dir():
    """Get the outputs directory path"""
    return os.path.join(get_data_dir(), "outputs")

def get_tables_output_dir():
    """Get the tables output directory path"""
    return os.path.join(get_outputs_dir(), "tables")

def get_tables_manifest_path() -> str:
    """Path to the tables manifest file."""
    return os.path.join(get_tables_output_dir(), "tables_manifest.json")

def get_analysis_output_dir() -> str:
    """
    Folder where HTML/CSV/JSON analysis files are written.
    Matches the layout used by vtrac & stable-pattern tools.
    """
    return os.path.join(get_outputs_dir(), "analysis")

def get_analysis_dir(kind: str, state: str) -> str:
    """
    Get the per-tool analysis directory for a given state, ensuring it exists.

    Example: kind="patterns" -> data/outputs/analysis/patterns/<STATE>/
    """
    base = os.path.join(get_analysis_output_dir(), kind)
    path = os.path.join(base, state)
    os.makedirs(path, exist_ok=True)
    return path

def get_winners_output_dir():
    """Get the winners output directory path"""
    date_str = get_current_date_str()
    return os.path.join(get_outputs_dir(), "winners", date_str)

def get_json_tables_dir() -> str:
    """Directory housing JSON mirrors of the per-state tables."""
    return os.path.join(get_outputs_dir(), "json_tables")

def get_pick3_workbook_path(preferred_filename: str | None = None) -> str:
    """
    Resolve the active Pick3StatsC4 workbook path.

    Order of precedence:
      1. Environment variable PICK3_WORKBOOK (absolute path)
      2. Preferred filename within data/original/ (if provided and exists)
      3. data/original/Pick3StatsC4.xlsm (legacy name)
      4. Latest matching Pick3StatsC4_*.xlsm under data/original/

    Raises FileNotFoundError with guidance if no candidate exists.
    """
    env_path = os.getenv("PICK3_WORKBOOK")
    if env_path:
        resolved = Path(env_path).expanduser()
        if resolved.exists():
            return str(resolved)
        raise FileNotFoundError(f"PICK3_WORKBOOK={env_path} was not found.")

    original_dir = Path(get_original_data_dir())

    if preferred_filename:
        candidate = original_dir / preferred_filename
        if candidate.exists():
            return str(candidate)

    legacy = original_dir / DEFAULT_PICK3_FILENAME
    if legacy.exists():
        return str(legacy)

    matches = sorted(original_dir.glob(PICK3_PATTERN))
    if matches:
        return str(matches[-1])

    history_dir = Path(get_data_dir()) / "history"
    message = [
        "No Pick3StatsC4 workbook found.",
        f"Checked {original_dir / DEFAULT_PICK3_FILENAME} and pattern {PICK3_PATTERN}.",
    ]
    if history_dir.exists():
        message.append(
            f"History files exist under {history_dir}; copy the desired file into {original_dir}."
        )
    raise FileNotFoundError(" ".join(message))

def get_excel_path():
    """Backward-compatible alias for get_pick3_workbook_path."""
    return get_pick3_workbook_path()

def get_cleaned_state_path(state_name):
    """
    Get the path to a cleaned state Excel file
    
    Args:
        state_name: The name of the state
        
    Returns:
        Path to the cleaned Excel file for the state
    """
    return os.path.join(get_cleaned_data_dir(), f"{state_name}_cleaned.xlsx")

def get_state_tables_dir(state_name):
    """
    Get the directory path for a state's generated tables
    
    Args:
        state_name: The name of the state
        
    Returns:
        Path to the directory for the state's tables
    """
    return os.path.join(get_tables_output_dir(), state_name)

def get_state_winners_dir(state_name):
    """
    Get the directory path for a state's winners
    
    Args:
        state_name: The name of the state
        
    Returns:
        Path to the directory for the state's winners
    """
    return os.path.join(get_winners_output_dir(), state_name)

def create_output_directories():
    """Create all required output directories if they don't exist"""
    dirs = [
        get_data_dir(),
        get_original_data_dir(),
        get_cleaned_data_dir(),
        get_outputs_dir(),
        get_tables_output_dir(),
        get_winners_output_dir(),
        get_analysis_output_dir(),
        get_json_tables_dir(),
    ]
    
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"Ensured directory exists: {directory}")

if __name__ == "__main__":
    # Display path information when run directly
    print("Lottery Data Processing Path Information:")
    print(f"Project Root: {get_project_root()}")
    print(f"Data Directory: {get_data_dir()}")
    print(f"Original Data: {get_original_data_dir()}")
    print(f"Cleaned Data: {get_cleaned_data_dir()}")
    print(f"Outputs Directory: {get_outputs_dir()}")
    print(f"Tables Output: {get_tables_output_dir()}")
    print(f"Winners Output (Today): {get_winners_output_dir()}")
    print(f"Analysis Output: {get_analysis_output_dir()}")
    print(f"Excel File Path: {get_excel_path()}")
    
    # Create directories
    create_output_directories()
    print("\nAll required directories have been created.") 

def get_cleaned_draws_dir():
    """Get the directory that stores cleaned draw CSVs"""
    draws_dir = os.path.join(get_cleaned_data_dir(), "draws")
    os.makedirs(draws_dir, exist_ok=True)
    return draws_dir
