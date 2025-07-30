"""
Draw Data Extractor Module

This module provides functions to extract draw data from Excel files,
specifically designed for the Pick3Stats workbook.
"""

import os
import pandas as pd
from datetime import datetime

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

def excel_col_to_index(col_str):
    """Convert Excel column letter to 0-based index"""
    idx = 0
    for char in col_str:
        idx = idx * 26 + (ord(char.upper()) - ord('A') + 1)
    return idx - 1

def load_draw_data(excel_path):
    """Load the raw data from the P3Draws sheet"""
    try:
        # Get sheet names to handle case sensitivity
        xl = pd.ExcelFile(excel_path)
        sheet_names = xl.sheet_names
        
        # Find P3Draws sheet with case-insensitive matching
        target_sheet = "P3Draws"
        sheet_to_use = None
        
        for sheet in sheet_names:
            if sheet.upper() == target_sheet.upper():
                sheet_to_use = sheet
                break
        
        if not sheet_to_use:
            print(f"Warning: Sheet '{target_sheet}' not found. Using first available sheet.")
            sheet_to_use = sheet_names[0]
            
        # Directly load the P3Draws sheet (or fallback)
        df = pd.read_excel(excel_path, sheet_name=sheet_to_use, header=None)
        return df
    except Exception as e:
        print(f"Error loading Excel file: {str(e)}")
        return None

def get_state_columns(df):
    """
    Extract the state ID to column mapping from row 15 of the Excel file.
    
    Args:
        df: DataFrame containing the Excel data
        
    Returns:
        Dict mapping state names to their corresponding Excel columns
    """
    state_columns = {}
    
    if df is None:
        return state_columns
    
    # Row 15 (0-indexed 14) contains state identifiers
    try:
        state_row = df.iloc[14]  # 15th row, 0-indexed
        
        # Find each state ID in the row
        for state_id, (state_name, expected_col) in STATE_MAPPING.items():
            # Look for the state ID in the row
            col_idx = excel_col_to_index(expected_col)
            
            # Check if the column index is valid
            if col_idx < len(state_row):
                # Check if the state ID matches the expected value in the row
                value = state_row[col_idx]
                if value == state_id:
                    state_columns[state_name] = expected_col
                    print(f"Found state {state_name} (ID {state_id}) in column {expected_col}")
        
        if not state_columns:
            # Fallback: use the hard-coded mapping directly
            print("Warning: No states found in row 15. Using hard-coded column mapping.")
            for state_id, (state_name, col) in STATE_MAPPING.items():
                state_columns[state_name] = col
    
    except Exception as e:
        print(f"Error extracting state columns: {str(e)}")
        # Fallback to hard-coded mapping
        for state_id, (state_name, col) in STATE_MAPPING.items():
            state_columns[state_name] = col
    
    return state_columns

def extract_state_draws(df, state_column, max_draws=1000):
    """
    Extract draws for a specific state from the loaded dataframe
    
    Args:
        df: The pandas DataFrame containing the draw data
        state_column: Column letter for the state (e.g., "AH" for Pennsylvania)
        max_draws: Maximum number of draws to return
        
    Returns:
        List of (date, draw) tuples, newest first
    """
    try:
        # Convert column letter to column index
        col_idx = excel_col_to_index(state_column)
        
        # Date column is always column A (0)
        date_col = 0
        
        # Data starts from row 20 (0-indexed: 19)
        start_row = 19
        
        draws = []
        
        # Ensure we don't go past the end of the DataFrame
        max_row = min(start_row + max_draws * 2, len(df))  # Use *2 to ensure we have enough rows to filter from
        
        for i in range(start_row, max_row):
            # Check if the row index is valid
            if i >= len(df):
                break
                
            # Get draw value
            if col_idx < len(df.columns):
                draw_val = df.iloc[i, col_idx]
                
                # Skip empty values
                if pd.isna(draw_val):
                    continue
                
                # Convert draw to 3-digit string
                try:
                    draw_str = str(int(draw_val)).zfill(3)
                    
                    # Get date if available (for display purposes)
                    date_str = "Unknown"
                    if date_col < len(df.columns):
                        date_val = df.iloc[i, date_col]
                        if not pd.isna(date_val):
                            if isinstance(date_val, datetime):
                                date_str = date_val.strftime("%Y-%m-%d")
                            else:
                                date_str = str(date_val)
                    
                    draws.append((date_str, draw_str))
                    
                    # Stop when we have enough draws
                    if len(draws) >= max_draws:
                        break
                        
                except (ValueError, TypeError) as e:
                    # Skip non-numeric values
                    print(f"Skipping invalid draw value at row {i+1}, column {state_column}: {draw_val}")
                    continue
        
        # Reverse the draws so newest are first (index 0)
        draws.reverse()
        
        print(f"Extracted {len(draws)} draws for column {state_column}")
        return draws
    
    except Exception as e:
        print(f"Error extracting draws for column {state_column}: {str(e)}")
        return []

def get_all_state_draws(excel_path, max_draws_per_state=200):
    """
    Get draws for all states
    
    Returns:
        Dictionary of state_name -> list of (date, draw) tuples
    """
    df = load_draw_data(excel_path)
    if df is None:
        return {}
        
    state_cols = get_state_columns(df)
    result = {}
    
    for state, col in state_cols.items():
        draws = extract_state_draws(df, col, max_draws=max_draws_per_state)
        if draws:
            result[state] = draws
    
    return result

def save_draws_to_csv(draws_dict, output_dir):
    """
    Save extracted draws to CSV files, one file per state.
    
    Args:
        draws_dict (dict): Dictionary mapping state names to their draw data
        output_dir (str): Directory to save the CSV files
        
    Returns:
        list: List of paths to the saved CSV files
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    saved_files = []
    for state, draws in draws_dict.items():
        if not draws:
            continue
        
        # Create DataFrame from draw data
        df = pd.DataFrame(draws, columns=["Date", "Draw"])
        
        # Save to CSV
        filename = os.path.join(output_dir, f"{state}_draws.csv")
        df.to_csv(filename, index=False)
        saved_files.append(filename)
    
    return saved_files

if __name__ == "__main__":
    # Example usage
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(current_dir, "../.."))
    data_dir = os.path.join(project_dir, "data")
    
    excel_path = os.path.join(data_dir, "original", "Pick3StatsC4.xlsm")
    output_dir = os.path.join(data_dir, "processed", "draws")
    
    print(f"Extracting draw data from: {excel_path}")
    all_draws = get_all_state_draws(excel_path)
    
    if all_draws:
        saved_files = save_draws_to_csv(all_draws, output_dir)
        print(f"Saved {len(saved_files)} draw files to: {output_dir}")
        for f in saved_files:
            print(f"  - {os.path.basename(f)}")
    else:
        print("No draw data extracted.") 

