"""
Debug script to identify and fix issues in the lottery project pipeline.
"""
import os
import sys
import time
from typing import Dict, List, Set

# Import required modules
from modules.parse_excel import process_excel_file
from modules.analyze_pairs import (
    calculate_overdue_pairs,
    get_top_overdue_repeating_pairs,
    get_vtrac_statuses,
    combos_appeared_in_1000
)
from modules.vtrac_reference import get_vtrac_index, VTRAC_LOOKUP, BOXED_VTRAC_REFERENCE, BOXED_LABEL_LOOKUP

def check_excel_structure():
    """Check if the Excel file has the expected structure."""
    excel_path = os.path.normpath("data/original/Pick3StatsC4.xlsm")
    
    if not os.path.exists(excel_path):
        print(f"ERROR: Excel file not found at {excel_path}")
        return False
    
    print(f"Excel file exists at {excel_path}")
    
    try:
        import pandas as pd
        # Try to read the Excel file
        xls = pd.ExcelFile(excel_path)
        sheet_names = xls.sheet_names
        print(f"Available sheets: {sheet_names}")
        
        # Check if the P3Draws sheet exists
        if "P3Draws" not in sheet_names:
            print("WARNING: 'P3Draws' sheet not found! Available sheets:", sheet_names)
            sheet_to_use = sheet_names[0]
        else:
            sheet_to_use = "P3Draws"
        
        # Read the first 20 rows to check structure
        df = pd.read_excel(excel_path, sheet_name=sheet_to_use, header=None, nrows=20)
        print(f"Excel shape: {df.shape}")
        
        # Check row 15 (0-indexed 14) for state IDs
        state_row = df.iloc[14]
        print(f"Row 15 content: {state_row.tolist()}")
        
        # Check if any state IDs are present
        state_ids = [4, 5, 6, 7, 10, 15, 18, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 74]
        found_states = []
        
        for col in df.columns:
            if state_row[col] in state_ids:
                found_states.append(state_row[col])
        
        print(f"Found {len(found_states)} state IDs in row 15: {found_states}")
        
        if not found_states:
            print("ERROR: No state IDs found in row 15! Excel has wrong structure.")
            return False
        
        return True
    
    except Exception as e:
        print(f"ERROR reading Excel: {e}")
        import traceback
        traceback.print_exc()
        return False


def check_vtrac_lookup():
    """Check if VTRAC_LOOKUP is initialized correctly."""
    print(f"VTRAC_LOOKUP contains {len(VTRAC_LOOKUP)} entries")
    
    # Check a few sample draws
    sample_draws = ["123", "456", "789", "012", "501", "999"]
    for draw in sample_draws:
        idx = get_vtrac_index(draw)
        print(f"Draw {draw} maps to V-Trac index: {idx}")
    
    # Check how many distinct indices there are
    indices = set(VTRAC_LOOKUP.values())
    print(f"VTRAC_LOOKUP has {len(indices)} distinct indices")
    
    # Verify boxed reference matches lookup
    boxes_count = 0
    for entry in BOXED_VTRAC_REFERENCE:
        boxes_count += len(entry["Singles"]) + len(entry["Doubles"])
    
    print(f"BOXED_VTRAC_REFERENCE has {boxes_count} total combos")
    if boxes_count != len(VTRAC_LOOKUP):
        print("WARNING: Mismatch between BOXED_VTRAC_REFERENCE and VTRAC_LOOKUP counts")


def test_combos_appeared():
    """Test the combos_appeared_in_1000 function with sample data."""
    # Create a sample draw history with known combos
    sample_draws = ["123", "456", "789", "234", "567", "890"]
    
    found = combos_appeared_in_1000(sample_draws)
    print(f"Found {len(found)} combos from sample draws")
    
    # Check if a specific draw was recognized
    if "123" in found:
        print("Draw 123 was correctly recognized")
    else:
        print("WARNING: Draw 123 was not recognized")
    
    # Check if our boxed label lookup is working
    if "123" in BOXED_LABEL_LOOKUP:
        print(f"Draw 123 maps to boxed label: {BOXED_LABEL_LOOKUP['123']}")
    
    # Check how many total boxed labels we have
    unique_labels = set(BOXED_LABEL_LOOKUP.values())
    print(f"Total unique boxed labels: {len(unique_labels)}")
    
    
def test_process_excel(max_draws=1000, analysis_draws=50):
    """Test the process_excel_file function with reduced analysis window."""
    excel_path = os.path.normpath("data/original/Pick3StatsC4.xlsm")
    output_dir = os.path.normpath("data/cleaned")
    
    print(f"Testing process_excel_file with {excel_path}")
    start_time = time.time()
    
    state_draws = process_excel_file(excel_path, output_dir)
    
    if not state_draws:
        print("ERROR: process_excel_file returned None or empty dict")
        return
    
    print(f"Processed {len(state_draws)} states in {time.time() - start_time:.2f} seconds")
    
    # Check a few states
    for state in list(state_draws.keys())[:1]:  # Just test the first state
        draws = state_draws[state]
        print(f"{state}: {len(draws)} draws, first 5: {draws[:5]}")
    
        # Test the combos_appeared_in_1000 with real draw data
        if state_draws:
            draws_1000 = draws[:1000] if len(draws) >= 1000 else draws
            
            print(f"Testing combos_appeared_in_1000 with {len(draws_1000)} draws from {state}")
            found_combos = combos_appeared_in_1000(draws_1000)
            print(f"Found {len(found_combos)} specific combos that appeared in real data")
            
            # Test with smaller analysis window
            draws_analysis = draws[:analysis_draws] if len(draws) >= analysis_draws else draws
            print(f"Using {len(draws_analysis)} draws for overdue analysis")
            
            # Calculate overdue pairs with the reduced window
            non_repeating_overdue, repeating_overdue, pair_status = calculate_overdue_pairs(draws_analysis)
            
            # Count colored pairs
            red_pairs = [pair for pair, color in pair_status.items() if color == 'red']
            blue_pairs = [pair for pair, color in pair_status.items() if color == 'blue']
            purple_pairs = [pair for pair, color in pair_status.items() if color == 'purple']
            
            print(f"RED pairs: {len(red_pairs)}, BLUE pairs: {len(blue_pairs)}, PURPLE pairs: {len(purple_pairs)}")
            
            # Get V-Trac statuses
            vtrac_statuses = get_vtrac_statuses(draws_analysis, draws_1000)
            
            # Count underlined combos
            underlined = 0
            for idx_data in vtrac_statuses.values():
                for status in idx_data.get("singles_status", {}).values():
                    if status.get("underline", False):
                        underlined += 1
                for status in idx_data.get("doubles_status", {}).values():
                    if status.get("underline", False):
                        underlined += 1
            
            print(f"Found {underlined} combos that should be underlined (never appeared in draws_1000)")
            
            # Test the colored pairs function
            from modules.analyze_pairs import get_colored_pairs
            colored_pairs = get_colored_pairs(draws_analysis)
            print(f"RED pairs: {len(colored_pairs['red'])}")
            print(f"BLUE pairs: {len(colored_pairs['blue'])}")
            print(f"PURPLE pairs: {len(colored_pairs['purple'])}")


def main():
    """Main debug function."""
    print("=== Lottery Project Debug Tool ===")
    
    print("\n1. Checking Excel structure...")
    if not check_excel_structure():
        print("Excel structure check failed, fixing file structure may be required.")
    else:
        print("Excel structure check passed!")
    
    print("\n2. Checking VTRAC lookup functionality...")
    check_vtrac_lookup()
    
    print("\n3. Testing combo recognition...")
    test_combos_appeared()
    
    print("\n4. Testing full Excel processing with reduced analysis window...")
    test_process_excel(max_draws=1000, analysis_draws=50)  # Use only 50 draws for analysis
    
    print("\nDebugging complete!")


if __name__ == "__main__":
    main() 