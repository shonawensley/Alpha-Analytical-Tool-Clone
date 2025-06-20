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

# PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # -> project root
DATA_DIR      = PROJECT_ROOT / "data"
ORIGINAL_DIR  = DATA_DIR / "original"

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
    return DATA_DIR

def get_original_data_dir():
    """Get the original data directory path"""
    return ORIGINAL_DIR

def get_cleaned_data_dir():
    """Get the cleaned data directory path"""
    return DATA_DIR / "cleaned"

def get_outputs_dir():
    """Get the outputs directory path"""
    return DATA_DIR / "outputs"

def get_tables_output_dir():
    """Get the tables output directory path"""
    return DATA_DIR / "outputs" / "tables"

def get_analysis_output_dir() -> str:
    """
    Folder where HTML/CSV/JSON analysis files are written.
    Matches the layout used by vtrac & stable-pattern tools.
    """
    return DATA_DIR / "outputs" / "analysis"

def get_winners_output_dir():
    """Get the winners output directory path"""
    date_str = get_current_date_str()
    return DATA_DIR / "outputs" / "winners" / date_str

def get_excel_path(filename: str = "Pick3StatsC4.xlsm") -> str:
    return str(ORIGINAL_DIR / filename)

def get_cleaned_state_path(state_name):
    """
    Get the path to a cleaned state Excel file
    
    Args:
        state_name: The name of the state
        
    Returns:
        Path to the cleaned Excel file for the state
    """
    return DATA_DIR / f"{state_name}_cleaned.xlsx"

def get_state_tables_dir(state_name):
    """
    Get the directory path for a state's generated tables
    
    Args:
        state_name: The name of the state
        
    Returns:
        Path to the directory for the state's tables
    """
    return DATA_DIR / "outputs" / "tables" / state_name

def get_state_winners_dir(state_name):
    """
    Get the directory path for a state's winners
    
    Args:
        state_name: The name of the state
        
    Returns:
        Path to the directory for the state's winners
    """
    return DATA_DIR / "outputs" / "winners" / state_name

def create_output_directories():
    """Create all required output directories if they don't exist"""
    dirs = [
        DATA_DIR,
        ORIGINAL_DIR,
        DATA_DIR / "cleaned",
        DATA_DIR / "outputs",
        DATA_DIR / "outputs" / "tables",
        DATA_DIR / "outputs" / "winners",
        DATA_DIR / "outputs" / "analysis"
    ]
    
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
        print(f"Ensured directory exists: {directory}")

def get_analysis_dir(kind: str, state: str) -> Path:
    """Return analysis subfolder path, creating it if needed.

    Args:
        kind: sub-folder under data/outputs/analysis (e.g. 'patterns', 'vtrac').
        state: state name, e.g. 'Connecticut4'.

    Returns:
        pathlib.Path pointing to the directory data/outputs/analysis/<kind>/<state>/
    """
    base = get_outputs_dir() / "analysis" / kind / state
    base.mkdir(parents=True, exist_ok=True)
    return base

if __name__ == "__main__":
    # Display path information when run directly
    print("Lottery Data Processing Path Information:")
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Data Directory: {DATA_DIR}")
    print(f"Original Data: {ORIGINAL_DIR}")
    print(f"Cleaned Data: {DATA_DIR / 'cleaned'}")
    print(f"Outputs Directory: {DATA_DIR / 'outputs'}")
    print(f"Tables Output: {DATA_DIR / 'outputs' / 'tables'}")
    print(f"Winners Output (Today): {DATA_DIR / 'outputs' / 'winners' / get_current_date_str()}")
    print(f"Analysis Output: {DATA_DIR / 'outputs' / 'analysis'}")
    print(f"Excel File Path: {get_excel_path()}")
    
    # Create directories
    create_output_directories()
    print("\nAll required directories have been created.") 