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

def get_analysis_output_dir() -> str:
    """
    Folder where HTML/CSV/JSON analysis files are written.
    Matches the layout used by vtrac & stable-pattern tools.
    """
    return os.path.join(get_outputs_dir(), "analysis")

def get_winners_output_dir():
    """Get the winners output directory path"""
    date_str = get_current_date_str()
    return os.path.join(get_outputs_dir(), "winners", date_str)

def get_excel_path():
    """Get the path to the original Excel file"""
    return os.path.join(get_original_data_dir(), "Pick3StatsC4.xlsm")

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
        get_analysis_output_dir()
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