#!/usr/bin/env python
"""
test_components.py - Test individual components of the lottery data processing system

This script provides testing capabilities for:
1. Path handling and directory setup
2. Data cleaning for specific states
3. Data extraction from cleaned files
4. Table generation with terminal display
5. V-TRAC winner highlighting
6. End-to-end processing tests
"""

import os
import sys
import argparse
import pandas as pd
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
    get_winners_output_dir,
    get_project_root
)
from utils.state_utils import STATES
from utils.clean_data import clean_state_data, clean_all_states
from utils.extract_data import extract_state_data, extract_all_states
from utils.table_generator import generate_tables, print_ascii_table
from utils.vtrac_utils import find_vtrac_index_and_combos
from vtrac.winner_highlighter import highlight_winners, highlight_winners_in_tables

def test_paths():
    """Test path handling and directory creation"""
    print("\n===== TESTING PATH HANDLING =====")
    
    # Display all relevant paths
    paths_to_check = [
        ("Project Root", get_project_root()),
        ("Excel File", get_excel_path()),
        ("Cleaned Data Dir", get_cleaned_data_dir()),
        ("Tables Output Dir", get_tables_output_dir()),
        ("Winners Output Dir", get_winners_output_dir())
    ]
    
    for name, path in paths_to_check:
        exists = os.path.exists(path)
        print(f"{name}: {path} {'✓ EXISTS' if exists else '✗ MISSING'}")
    
    # Create directories if needed
    create_option = input("\nCreate missing directories? (y/n): ")
    if create_option.lower() == 'y':
        create_output_directories()
        print("Directories created!")
    
    # Check Excel file specifically
    excel_path = get_excel_path()
    if not os.path.exists(excel_path):
        print(f"\n⚠️ Excel file not found at: {excel_path}")
        print("Please place Pick3StatsC4.xlsm in the data/original directory before proceeding.")
    else:
        print(f"\n✓ Excel file found: {excel_path}")
    
    return os.path.exists(excel_path)

def test_clean_data(state=None):
    """Test data cleaning for a specific state or all states"""
    print("\n===== TESTING DATA CLEANING =====")
    
    excel_path = get_excel_path()
    if not os.path.exists(excel_path):
        print(f"Error: Excel file not found at {excel_path}")
        return False
    
    output_dir = get_cleaned_data_dir()
    
    if state:
        # Clean a single state
        print(f"Cleaning data for state: {state}")
        result = clean_state_data(excel_path, state, output_dir)
        success = result is not None
        print(f"{'✓ Success' if success else '✗ Failed'}: {state}")
        return success
    else:
        # Clean all states
        print("Cleaning data for all states...")
        results = clean_all_states(STATES, excel_path, output_dir)
        
        print(f"\nSuccessfully cleaned {len(results['success'])} states:")
        for s in results['success']:
            print(f"  ✓ {s}")
        
        if results['failed']:
            print(f"\nFailed to clean {len(results['failed'])} states:")
            for s in results['failed']:
                print(f"  ✗ {s}")
        
        return len(results['success']) > 0

def test_extract_data(state=None):
    """Test data extraction for a specific state or all states"""
    print("\n===== TESTING DATA EXTRACTION =====")
    
    cleaned_dir = get_cleaned_data_dir()
    
    if state:
        # Extract a single state
        state_file = os.path.join(cleaned_dir, f"{state}_cleaned.xlsx")
        if not os.path.exists(state_file):
            print(f"Error: Cleaned file for {state} not found at {state_file}")
            return False
        
        print(f"Extracting data for state: {state}")
        result = extract_state_data(state_file)
        success = bool(result)
        
        print(f"{'✓ Success' if success else '✗ Failed'}: {state}")
        return result
    else:
        # Extract all states
        print("Extracting data for all cleaned states...")
        results = extract_all_states(STATES, cleaned_dir)
        
        print(f"\nSuccessfully extracted {len(results)} states:")
        for s in results:
            print(f"  ✓ {s}")
        
        return results

def test_generate_tables(state_data, state_name):
    """Test table generation for a specific state"""
    print(f"\n===== TESTING TABLE GENERATION FOR {state_name} =====")
    
    if not state_data:
        print(f"Error: No data available for {state_name}")
        return None
    
    # Generate tables but don't save to files
    tables = {}
    
    for section in ["Midday", "Evening", "Combined"]:
        if section not in state_data:
            print(f"  Section {section} not found - skipping")
            continue
        
        print(f"\nGenerating tables for {state_name} {section}...")
        
        # Generate combined table
        combined_df = generate_tables(state_data, state_name)[f"{section}_combined"]
        tables[f"{section}_combined"] = combined_df
        
        # Print ASCII table for preview
        print_ascii_table(combined_df, f"{state_name} {section} Combined Table")
        
        # Generate R2-only table
        r2_df = generate_tables(state_data, state_name)[f"{section}_r2"]
        tables[f"{section}_r2"] = r2_df
        
        # Print ASCII table for preview
        print_ascii_table(r2_df, f"{state_name} {section} R2-Only Table")
    
    return tables

def test_vtrac_highlighting(tables, winning_numbers):
    """Test V-TRAC winner highlighting with specific numbers"""
    if not tables:
        print("Error: No tables available for testing")
        return None
    
    print("\n===== TESTING V-TRAC WINNER HIGHLIGHTING =====")
    
    if not winning_numbers:
        winning_numbers = input("Enter winning numbers separated by spaces: ").strip()
        winning_numbers = [w.strip() for w in winning_numbers.split() if w.strip()]
    
    if not winning_numbers:
        print("No winning numbers provided - skipping test")
        return None
    
    # Display the V-TRAC indices for each winning number
    print("\nV-TRAC Analysis of Winning Numbers:")
    for number in winning_numbers:
        vtrac_idx = find_vtrac_index_and_combos(number)
        pattern = "AAA" if vtrac_idx == 0 else "AAB" if vtrac_idx == 1 else "ABC"
        print(f"  Number {number}: VTRAC{vtrac_idx} ({pattern} pattern)")
    
    # Apply highlighting to one table as an example
    sample_key = next(iter(tables))
    sample_table = tables[sample_key]
    
    print(f"\nHighlighting winners in {sample_key}...")
    
    # Highlight the first winning number as an example
    if winning_numbers:
        highlighted = highlight_winners(sample_table, winning_number=winning_numbers[0])
        print_ascii_table(highlighted, f"Highlighted Table ({winning_numbers[0]})")
    
    return True

def test_full_process(state=None, winners=None):
    """Run a complete process test for a specific state or all states"""
    print("\n===== TESTING FULL PROCESS =====")
    
    # 1. Check paths and create directories
    path_check = test_paths()
    if not path_check:
        print("Path check failed - cannot proceed with full test")
        return False
    
    # 2. Clean data
    clean_success = test_clean_data(state)
    if not clean_success:
        print("Data cleaning failed - cannot proceed with full test")
        return False
    
    # 3. Extract data
    if state:
        extracted_data = test_extract_data(state)
        states_to_process = [state] if extracted_data else []
    else:
        extracted_data = test_extract_data()
        states_to_process = list(extracted_data.keys())
    
    if not states_to_process:
        print("Data extraction failed - cannot proceed with full test")
        return False
    
    # 4. Generate tables
    tables_by_state = {}
    for s in states_to_process:
        if state and s != state:
            continue
        tables = test_generate_tables(extracted_data[s], s)
        if tables:
            tables_by_state[s] = tables
    
    if not tables_by_state:
        print("Table generation failed - cannot proceed with full test")
        return False
    
    # 5. Test highlighting if winners provided
    if winners:
        first_state = next(iter(tables_by_state))
        test_vtrac_highlighting(tables_by_state[first_state], winners)
    
    print("\n===== FULL PROCESS TEST COMPLETED SUCCESSFULLY =====")
    print(f"Processed {len(states_to_process)} states")
    return True

def main():
    """Run test components based on command-line arguments"""
    parser = argparse.ArgumentParser(description="Test lottery data processing components")
    parser.add_argument("--paths", action="store_true", help="Test path handling")
    parser.add_argument("--clean", action="store_true", help="Test data cleaning")
    parser.add_argument("--extract", action="store_true", help="Test data extraction")
    parser.add_argument("--tables", action="store_true", help="Test table generation")
    parser.add_argument("--vtrac", action="store_true", help="Test V-TRAC highlighting")
    parser.add_argument("--full", action="store_true", help="Run full process test")
    parser.add_argument("--state", help="Process a specific state")
    parser.add_argument("--winners", help="Winning numbers for testing (comma-separated)")
    
    args = parser.parse_args()
    
    # Parse winning numbers if provided
    winning_numbers = None
    if args.winners:
        winning_numbers = [w.strip() for w in args.winners.split(",") if w.strip()]
    
    # Run selected test components
    if args.paths or not any([args.paths, args.clean, args.extract, args.tables, args.vtrac, args.full]):
        test_paths()
    
    if args.clean:
        test_clean_data(args.state)
    
    if args.extract:
        extracted = test_extract_data(args.state)
        
        if args.tables and extracted:
            if args.state:
                tables = test_generate_tables(extracted, args.state)
                
                if args.vtrac and tables:
                    test_vtrac_highlighting(tables, winning_numbers)
            else:
                for state, data in extracted.items():
                    tables = test_generate_tables(data, state)
                    
                    if args.vtrac and tables and state == next(iter(extracted)):
                        test_vtrac_highlighting(tables, winning_numbers)
                        break
    
    if args.full:
        test_full_process(args.state, winning_numbers)

if __name__ == "__main__":
    main() 