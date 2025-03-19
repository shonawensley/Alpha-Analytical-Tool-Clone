#!/usr/bin/env python
"""
run_process.py - Main script to run the lottery data processing pipeline

This script:
1. Cleans lottery data from the original Excel file for all states
2. Extracts structured datasets from cleaned state files
3. Generates formatted tables for each state and section
4. Optionally highlights winners using V-TRAC references
5. Saves all outputs to appropriate directories
"""

import sys
import os
import time
import argparse
from datetime import datetime

# Add the current directory to the path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Import utility modules
from utils.path_handler import (
    get_excel_path, 
    create_output_directories,
    get_cleaned_data_dir,
    get_tables_output_dir,
    get_winners_output_dir
)
from utils.state_utils import STATES
from utils.clean_data import clean_all_states
from utils.extract_data import extract_all_states
from utils.table_generator import generate_tables, print_ascii_table
from vtrac.winner_highlighter import highlight_winners_in_tables

def format_timestamp():
    """Generate a formatted timestamp for display"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main(args=None):
    """
    Run the complete lottery data processing pipeline
    
    Args:
        args: Command line arguments:
            --no-clean: Skip data cleaning step
            --no-extract: Skip data extraction step
            --no-tables: Skip table generation step
            --winners: Optional winners to highlight (comma-separated)
    """
    parser = argparse.ArgumentParser(description="Lottery Data Processing Pipeline")
    parser.add_argument("--no-clean", action="store_true", help="Skip data cleaning step")
    parser.add_argument("--no-extract", action="store_true", help="Skip data extraction step")
    parser.add_argument("--no-tables", action="store_true", help="Skip table generation step")
    parser.add_argument("--midday-winners", help="Midday winners to highlight (comma-separated)")
    parser.add_argument("--evening-winners", help="Evening winners to highlight (comma-separated)")
    
    # Parse arguments
    if args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)
    
    # Setup output directories
    create_output_directories()
    
    # Get paths
    excel_path = get_excel_path()
    cleaned_data_dir = get_cleaned_data_dir()
    tables_output_dir = get_tables_output_dir()
    winners_output_dir = get_winners_output_dir()
    
    print(f"\n{'=' * 60}")
    print(f"LOTTERY DATA PROCESSING PIPELINE - {format_timestamp()}")
    print(f"{'=' * 60}")
    print(f"Input Excel File: {excel_path}")
    print(f"Cleaned Data Dir: {cleaned_data_dir}")
    print(f"Tables Output Dir: {tables_output_dir}")
    print(f"Winners Output Dir: {winners_output_dir}")
    
    # Check if the input Excel file exists
    if not os.path.exists(excel_path):
        print(f"\nERROR: Input Excel file not found at {excel_path}")
        print("Please place the Pick3StatsC4.xlsm file in the data/original directory")
        return False
    
    # STEP 1: Clean data
    if not args.no_clean:
        print(f"\n{'=' * 60}")
        print(f"STEP 1: CLEANING DATA - {format_timestamp()}")
        print(f"{'=' * 60}")
        
        start_time = time.time()
        cleaned_results = clean_all_states(STATES, excel_path, cleaned_data_dir)
        clean_duration = time.time() - start_time
        
        print(f"\nData cleaning completed in {clean_duration:.2f} seconds")
        print(f"Successfully cleaned: {len(cleaned_results['success'])}/{len(STATES)} states")
        
        if cleaned_results['failed']:
            print(f"Failed states: {', '.join(cleaned_results['failed'])}")
    else:
        print("\nSkipping data cleaning step (--no-clean flag set)")
    
    # STEP 2: Extract data
    if not args.no_extract:
        print(f"\n{'=' * 60}")
        print(f"STEP 2: EXTRACTING DATA - {format_timestamp()}")
        print(f"{'=' * 60}")
        
        start_time = time.time()
        extracted_data = extract_all_states(STATES, cleaned_data_dir)
        extract_duration = time.time() - start_time
        
        print(f"\nData extraction completed in {extract_duration:.2f} seconds")
        print(f"Successfully extracted: {len(extracted_data)}/{len(STATES)} states")
    else:
        print("\nSkipping data extraction step (--no-extract flag set)")
        # Load previously extracted data if available
        extracted_data = {}
    
    # STEP 3: Generate tables
    if not args.no_tables:
        print(f"\n{'=' * 60}")
        print(f"STEP 3: GENERATING TABLES - {format_timestamp()}")
        print(f"{'=' * 60}")
        
        tables_by_state = {}
        start_time = time.time()
        
        for state_name, state_data in extracted_data.items():
            print(f"\nGenerating tables for {state_name}...")
            state_tables = generate_tables(
                state_data, 
                state_name, 
                os.path.join(tables_output_dir, state_name)
            )
            tables_by_state[state_name] = state_tables
        
        tables_duration = time.time() - start_time
        print(f"\nTable generation completed in {tables_duration:.2f} seconds")
    else:
        print("\nSkipping table generation step (--no-tables flag set)")
    
    # STEP 4: Highlight winners if specified
    if args.midday_winners or args.evening_winners:
        print(f"\n{'=' * 60}")
        print(f"STEP 4: HIGHLIGHTING WINNERS - {format_timestamp()}")
        print(f"{'=' * 60}")
        
        midday_winners = args.midday_winners.split(",") if args.midday_winners else []
        evening_winners = args.evening_winners.split(",") if args.evening_winners else []
        
        if midday_winners:
            print(f"Midday Winners: {', '.join(midday_winners)}")
        if evening_winners:
            print(f"Evening Winners: {', '.join(evening_winners)}")
        
        start_time = time.time()
        
        for state_name, state_tables in tables_by_state.items():
            output_dir = os.path.join(winners_output_dir, state_name)
            os.makedirs(output_dir, exist_ok=True)
            
            print(f"\nProcessing winners for {state_name}...")
            updated_tables = highlight_winners_in_tables(
                state_tables,
                midday_winners,
                evening_winners
            )
            
            # Save highlighted tables
            for section_key, df in updated_tables.items():
                if df is not None and not df.empty:
                    # Create winner-specific filename
                    winners_suffix = ""
                    if "Midday" in section_key and midday_winners:
                        winners_suffix = f"_win{'_'.join(midday_winners)}"
                    elif "Evening" in section_key and evening_winners:
                        winners_suffix = f"_win{'_'.join(evening_winners)}"
                    elif "Combined" in section_key and (midday_winners or evening_winners):
                        winners_suffix = "_winners"
                    
                    output_file = os.path.join(
                        output_dir, 
                        f"{state_name}_{section_key}{winners_suffix}.csv"
                    )
                    df.to_csv(output_file, index=False)
                    print(f"  - Saved {section_key} with winners to {output_file}")
        
        winners_duration = time.time() - start_time
        print(f"\nWinner highlighting completed in {winners_duration:.2f} seconds")
    
    # Print completion message
    print(f"\n{'=' * 60}")
    print(f"PIPELINE COMPLETED SUCCESSFULLY - {format_timestamp()}")
    print(f"{'=' * 60}")
    return True

if __name__ == "__main__":
    main() 