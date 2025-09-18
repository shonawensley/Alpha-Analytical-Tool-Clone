"""
Module for parsing Pick3 lottery draw data from Excel files.
"""

import os
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional

# State ID to column mapping
STATE_MAPPING = {
    4: ('Connecticut', 'N'),
    5: ('Delaware', 'O'),
    6: ('Florida', 'P'),
    7: ('Georgia', 'Q'),
    10: ('Indiana', 'T'),
    15: ('Michigan', 'Y'),
    18: ('New Jersey', 'AB'),
    20: ('New York', 'AD'),
    21: ('North Carolina', 'AE'),
    22: ('Ohio', 'AF'),
    23: ('Ontario', 'AG'),
    24: ('Pennsylvania', 'AH'),
    25: ('Puerto Rico', 'AI'),
    26: ('South Carolina', 'AJ'),
    28: ('Texas', 'AL'),
    29: ('Tri-State', 'AM'),
    30: ('Virginia', 'AN'),
    74: ('West Virginia', 'CF')
}

# Draws per day for each state
DRAWS_PER_DAY = {
    'West Virginia': 1,
    'Georgia': 3,
    'Texas': 4
}
# Default is 2 for states not specified


def get_state_column_mapping(df: pd.DataFrame) -> Dict[str, str]:
    """
    Extracts the state ID to column mapping from row 15 of the Excel file.
    
    Args:
        df: DataFrame containing the Excel data
        
    Returns:
        Dict mapping state names to their corresponding Excel columns
    """
    state_cols = {}
    
    # Row 15 (0-indexed) contains state identifiers
    state_row = df.iloc[14]  # 15th row, 0-indexed
    
    print(f"DEBUG: Row 15 content = {state_row.tolist()}")
    
    # Find each state ID in the row
    for state_id, (state_name, expected_col) in STATE_MAPPING.items():
        # Look for the state ID in the row
        for col in df.columns:
            if state_row[col] == state_id:
                state_cols[state_name] = col
                print(f"DEBUG: Found state {state_name} (ID {state_id}) in column {col}")
                break
        else:
            # If we get here, we didn't find the state ID
            print(f"Warning: Could not find column for state ID {state_id} ({state_name})")
    
    return state_cols


def validate_state_columns(state_cols: Dict[str, str]) -> bool:
    """
    Validates that all expected states were found in the Excel file.
    
    Args:
        state_cols: Dict mapping state names to their columns
        
    Returns:
        True if all states were found, False otherwise
    """
    expected_states = set(state_name for _, (state_name, _) in STATE_MAPPING.items())
    found_states = set(state_cols.keys())
    
    missing_states = expected_states - found_states
    if missing_states:
        print(f"Warning: These states were not found in the Excel file: {missing_states}")
        return False
    
    return True


def parse_draw_data(file_path: str, max_draws: int = 1000) -> Dict[str, List[str]]:
    """
    Parses the Pick3 lottery draw data from the Excel file.
    
    Args:
        file_path: Path to the Excel file
        max_draws: Maximum number of draws to extract per state
        
    Returns:
        Dict mapping state names to lists of draw results (3-digit strings)
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Excel file not found: {file_path}")
    
    # Read the Excel file - no header, keep all data as is
    try:
        # First get available sheet names to handle case sensitivity
        sheet_names = pd.ExcelFile(file_path).sheet_names
        print(f"Available sheets: {sheet_names}")
        
        # Look for P3Draws sheet with case-insensitive matching
        target_sheet = "P3Draws"
        sheet_to_use = None
        
        for sheet in sheet_names:
            if sheet.upper() == target_sheet.upper():
                sheet_to_use = sheet
                break
        
        if not sheet_to_use:
            print(f"Warning: Sheet '{target_sheet}' not found. Using first available sheet.")
            sheet_to_use = sheet_names[0]
        
        # Now read the selected sheet
        print(f"Attempting to read Excel file: {file_path}, sheet: {sheet_to_use}")
        df = pd.read_excel(file_path, sheet_name=sheet_to_use, header=None)
        print(f"Successfully read Excel file from sheet '{sheet_to_use}'")
        print(f"DEBUG: Excel shape = {df.shape}")
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        # If all else fails, try the first sheet as a last resort
        try:
            print("Trying to read first sheet as fallback...")
            sheet_names = pd.ExcelFile(file_path).sheet_names
            if len(sheet_names) > 0:
                print(f"Using first sheet: {sheet_names[0]}")
                df = pd.read_excel(file_path, sheet_name=sheet_names[0], header=None)
                print(f"Successfully read from sheet: {sheet_names[0]}")
                print(f"DEBUG: Excel shape = {df.shape}")
            else:
                raise ValueError("No sheets found in the Excel file")
        except Exception as inner_e:
            print(f"Error reading any sheet: {inner_e}")
            raise
    
    # Get state column mapping
    state_cols = get_state_column_mapping(df)
    print(f"DEBUG: Found {len(state_cols)} state columns: {list(state_cols.keys())}")
    
    # Validate that we found all expected states
    if not validate_state_columns(state_cols):
        print("Warning: Not all states were found, continuing with available data")
    
    # Extract draw data for each state
    state_draws = {}
    
    # Draws start from row 20 (0-indexed = 19)
    draw_rows = df.iloc[19:19+max_draws]
    print(f"DEBUG: Processing {len(draw_rows)} draw rows, starting from row 20")
    
    for state_name, col in state_cols.items():
        # Extract draws for this state
        draws = []
        for _, value in draw_rows[col].items():
            # Skip missing values
            if pd.isna(value):
                continue
                
            # Convert to string and pad with leading zeros to 3 digits
            draw = str(int(value)).zfill(3)
            draws.append(draw)
            
        state_draws[state_name] = draws
        print(f"DEBUG: Extracted {len(draws)} draws for {state_name}")
    
    return state_draws


def save_clean_data(state_draws: Dict[str, List[str]], output_dir: str) -> None:
    """
    Saves the cleaned draw data to CSV files.
    
    Args:
        state_draws: Dict mapping state names to lists of draw results
        output_dir: Directory to save the output files
    """
    os.makedirs(output_dir, exist_ok=True)
    
    for state, draws in state_draws.items():
        # Create DataFrame from draws
        df = pd.DataFrame(draws, columns=["Draw"])
        
        # Save to CSV
        output_path = os.path.join(output_dir, f"{state.replace(' ', '_')}_draws.csv")
        df.to_csv(output_path, index=False)
        
        print(f"Saved {len(draws)} draws for {state} to {output_path}")


def process_excel_file(file_path: str, output_dir: str, max_draws: int = 1000) -> Dict[str, List[str]]:
    """
    Main function to process an Excel file, extract draw data, and save it.
    
    Args:
        file_path: Path to the Excel file
        output_dir: Directory to save output files
        max_draws: Maximum number of draws to extract per state
        
    Returns:
        Dict mapping state names to their draw histories
    """
    try:
        # Ensure file_path is using correct path separators
        file_path = os.path.normpath(file_path)
        output_dir = os.path.normpath(output_dir)
        
        print(f"Processing Excel file: {file_path}")
        print(f"Absolute path: {os.path.abspath(file_path)}")
        print(f"Output directory: {output_dir}")
        
        # Parse draw data
        state_draws = parse_draw_data(file_path, max_draws)
        
        if not state_draws:
            print("WARNING: No state draw data was extracted")
            return None
            
        print(f"DEBUG: Extracted data for {len(state_draws)} states: {list(state_draws.keys())}")
        
        # Save cleaned data
        save_clean_data(state_draws, output_dir)
        
        print(f"Successfully processed {file_path}")
        print(f"Extracted data for {len(state_draws)} states")
        
        return state_draws
        
    except Exception as e:
        print(f"Error processing Excel file: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    # Example usage
    import sys
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Default path - use normalized path
        file_path = os.path.normpath("data/original/Pick3StatsC4.xlsm")
    
    output_dir = os.path.normpath("data/cleaned")
    process_excel_file(file_path, output_dir) 