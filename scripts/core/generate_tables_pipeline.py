#!/usr/bin/env python
"""
generate_tables_pipeline.py

This script runs the core data processing pipeline:
1. Cleans data from the source Excel file.
2. Extracts structured data for each state.
3. Generates the standard set of 6 CSV tables per state.
   (Midday_combined, Evening_combined, Combined_combined,
    Midday_R2_only, Evening_R2_only, Combined_R2_only)
Saves the output tables to data/outputs/tables/[STATE_NAME]/
This provides the baseline data needed for subsequent analysis tools.
"""

import os
import sys
import time
from datetime import datetime

# Add project root to path to allow importing utility modules
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir)) # Go up two levels
sys.path.append(project_root)

# Import necessary functions from the utils directory
try:
    from scripts.utils.path_handler import (
        get_excel_path,
        create_output_directories,
        get_cleaned_data_dir,
        get_tables_output_dir
    )
    from scripts.utils.state_utils import STATES
    from scripts.utils.clean_data import clean_all_states
    from scripts.utils.extract_data import extract_all_states
    from scripts.utils.table_generator import generate_tables
except ImportError as e:
    print(f"Error importing utility modules: {e}")
    print("Please ensure the script is run from the project root or relevant paths are set.")
    sys.exit(1)

def format_time(seconds):
    """Format time in seconds to human-readable string"""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    else:
        minutes = int(seconds // 60)
        sec = seconds % 60
        return f"{minutes} min {sec:.2f} sec"

def main():
    """Executes the full data processing pipeline to generate tables."""
    print("Starting Data Processing Pipeline...")
    pipeline_start_time = time.time()

    # 1. Check for Source Excel File
    print("\nStep 1: Checking for source Excel file...")
    excel_path = get_excel_path()
    if not os.path.exists(excel_path):
        print(f"[ERROR] Source Excel file not found at: {excel_path}")
        print("Please ensure 'Pick3StatsC4.xlsm' is in the 'data/original/' directory.")
        sys.exit(1)
    print(f"Source Excel file found: {os.path.basename(excel_path)}")

    # 2. Create Output Directories
    print("\nStep 2: Ensuring output directories exist...")
    create_output_directories() # Creates cleaned, tables, analysis, etc.
    print("Output directories checked/created.")

    # Define states to process (all states)
    states_to_process = STATES
    print(f"Processing for {len(states_to_process)} states: {', '.join(states_to_process)}")

    # 3. Clean Data
    print("\nStep 3: Cleaning data...")
    clean_start_time = time.time()
    cleaned_dir = get_cleaned_data_dir()
    try:
        cleaning_results = clean_all_states(states_to_process, excel_path, cleaned_dir)
        print(f"Successfully cleaned: {len(cleaning_results['success'])} states.")
        if cleaning_results['failed']:
            print(f"[WARNING] Failed to clean: {', '.join(cleaning_results['failed'])} states.")
    except Exception as e:
        print(f"[ERROR] An error occurred during data cleaning: {e}")
        sys.exit(1)
    print(f"Data cleaning finished in {format_time(time.time() - clean_start_time)}.")

    # 4. Extract Data
    print("\nStep 4: Extracting structured data...")
    extract_start_time = time.time()
    extracted_data = {}
    try:
        extracted_data = extract_all_states(states_to_process, cleaned_dir)
        print(f"Successfully extracted data for: {len(extracted_data)} states.")
    except Exception as e:
        print(f"[ERROR] An error occurred during data extraction: {e}")
        sys.exit(1)
    print(f"Data extraction finished in {format_time(time.time() - extract_start_time)}.")

    # 5. Generate Tables
    print("\nStep 5: Generating CSV tables...")
    generate_start_time = time.time()
    tables_generated_count = 0
    tables_base_dir = get_tables_output_dir()
    # Ensure the base 'tables' directory exists, but generate_tables handles the state subdirs
    os.makedirs(tables_base_dir, exist_ok=True) 

    for state_name, state_data in extracted_data.items():
        try:
            # The generate_tables function saves files to tables_base_dir/state_name/
            print(f"  Generating tables for {state_name}...")
            generate_tables(state_data, state_name, tables_base_dir)
            tables_generated_count += 1
        except Exception as e:
            print(f"[ERROR] Failed to generate tables for {state_name}: {e}")

    print(f"Table generation finished in {format_time(time.time() - generate_start_time)}.")
    print(f"Successfully generated tables for {tables_generated_count} states.")

    # Pipeline Completion Summary
    print("\n------------------------------------")
    print("Data Processing Pipeline Completed!")
    print(f"Total time: {format_time(time.time() - pipeline_start_time)}")
    print(f"Output tables saved in: {tables_base_dir}")
    print("You can now run analysis tools on the generated tables.")
    print("------------------------------------")

if __name__ == "__main__":
    main() 