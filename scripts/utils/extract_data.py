#!/usr/bin/env python
"""
extract_data.py - Extract lottery data from cleaned Excel files

This module:
1. Reads cleaned Excel files for each state
2. Extracts structured data for Midday, Evening, and Combined sections
3. Handles Set1, Set2, Set3 and their respective draws
"""

import os
import pandas as pd
from .path_handler import get_cleaned_data_dir, get_cleaned_state_path
from .clean_data import STATES

class LotteryDataExtractor:
    def __init__(self, excel_path):
        """
        Initialize extractor with path to cleaned Excel file
        
        Args:
            excel_path: Path to cleaned Excel file for a state
        """
        print(f"Reading cleaned Excel: {os.path.abspath(excel_path)}")
        self.df = pd.read_excel(excel_path, sheet_name=0, header=None, dtype=str)
        print(f"DataFrame loaded with shape {self.df.shape}")
        
        # Rename DataFrame columns to match Excel letters
        col_map = {
            0:'Q',  1:'S',  2:'V',  3:'W',  4:'X',  5:'Y',  6:'Z',  7:'AA', 8:'AB',
            9:'AD', 10:'AF', 11:'AI', 12:'AJ', 13:'AK', 14:'AL', 15:'AM', 16:'AN', 17:'AO',
            18:'BD', 19:'BI', 20:'BJ', 21:'BK', 22:'BL', 23:'BM', 24:'BN', 25:'BO'
        }
        self.df.rename(columns=col_map, inplace=True)

        # For each section, we store:
        #   - The "indicator_col" (Q for Midday, AD for Evening, BD for Combined)
        #   - The 7 data columns to use for that section
        #   - The starting row offsets for each set (Set1 starts at 3, Set2 at 49, Set3 at 95)
        self.sections = {
            'Midday': {
                'indicator_col': 'Q',
                'data_cols': ['V','W','X','Y','Z','AA','AB'],
                'set_offsets': {1: 3, 2: 49, 3: 95}
            },
            'Evening': {
                'indicator_col': 'AD',
                'data_cols': ['AI','AJ','AK','AL','AM','AN','AO'],
                'set_offsets': {1: 3, 2: 49, 3: 95}
            },
            'Combined': {
                'indicator_col': 'BD',
                'data_cols': ['BI','BJ','BK','BL','BM','BN','BO'],
                'set_offsets': {1: 3, 2: 49, 3: 95}
            }
        }
        # Define additional row shift adjustments for Set2 and Set3
        # (shift upward by subtracting rows from the base offset)
        # For all sections: Set2 shifts by 1 row, Set3 shifts by 2 rows.
        self.shift_adjustments = {
            'Midday': {2: 1, 3: 2},
            'Evening': {2: 1, 3: 2},
            'Combined': {2: 1, 3: 2}
        }
    
    def extract_set1(self, section):
        """
        Extract Set1 data for a section (Midday/Evening/Combined)
        
        Set1 has 7 draws. Each draw is 5 lines (draw_data + R2 + R4 + R6 + R8)
        plus 1 blank line => 6 rows per draw.

        We also do the "column slicing" so that Draw1 uses all 7 columns,
        Draw2 uses the last 6 columns, etc.
        """
        config = self.sections[section]
        base_row = config['set_offsets'][1]  # typically 3
        all_draws = {}
        
        for draw_num in range(1, 8):  # 1..7
            row = base_row + (draw_num - 1) * 6
            cols = config['data_cols'][draw_num - 1:]

            try:
                data = {
                    'draw_data': [str(x).strip().zfill(3) for x in self.df.loc[row, cols]],
                    'R2': [str(x).strip() for x in self.df.loc[row + 1, cols]],
                    'R4': [str(x).strip() for x in self.df.loc[row + 2, cols]],
                    'R6': [str(x).strip() for x in self.df.loc[row + 3, cols]],
                    'R8': [str(x).strip() for x in self.df.loc[row + 4, cols]]
                }

                indicator_val = str(self.df.loc[row + 1, config['indicator_col']]).strip()
                if not indicator_val.startswith("R-2"):
                    print(f"Warning: Expected 'R-2' at row {row+1} for {section} Set1 Draw{draw_num}, found '{indicator_val}'")

                print(f"\n{section} Set1 Draw{draw_num}:")
                print(f"  draw_data => {data['draw_data']}")
                print(f"  R2 => {data['R2']}")
                print(f"  R4 => {data['R4']}")
                print(f"  R6 => {data['R6']}")
                print(f"  R8 => {data['R8']}")

                all_draws[f"Draw{draw_num}"] = data
            except Exception as e:
                print(f"Error extracting {section} Set1 Draw{draw_num}: {e}")
        
        return all_draws

    def extract_single_draw(self, section, set_num):
        """
        Extract a single draw from Set2 or Set3
        
        For Set2 and Set3, we only want ONE draw (Draw1).
        We take all 7 columns (no column slicing) and extract:
          - draw_data at base_row,
          - then R2, R4, R6, and R8 from the subsequent rows.
        """
        config = self.sections[section]
        # Get the configured base row for this set (Set2 or Set3)
        base = config['set_offsets'][set_num]
        # Apply the shift adjustment for this section and set
        shift = self.shift_adjustments[section][set_num]
        actual_base = base - shift
        # For single-draw extraction we always use all 7 data columns.
        cols = config['data_cols']
        
        try:
            data = {
                'draw_data': [str(x).strip().zfill(3) for x in self.df.loc[actual_base, cols]],
                'R2': [str(x).strip() for x in self.df.loc[actual_base + 1, cols]],
                'R4': [str(x).strip() for x in self.df.loc[actual_base + 2, cols]],
                'R6': [str(x).strip() for x in self.df.loc[actual_base + 3, cols]],
                'R8': [str(x).strip() for x in self.df.loc[actual_base + 4, cols]]
            }
            
            indicator_val = str(self.df.loc[actual_base + 1, config['indicator_col']]).strip()
            if not indicator_val.startswith("R-2"):
                print(f"Warning: Expected 'R-2' at row {actual_base+1} for {section} Set{set_num} Draw1, found '{indicator_val}'")
            
            print(f"\n{section} Set{set_num} Draw1:")
            print(f"  draw_data => {data['draw_data']}")
            print(f"  R2 => {data['R2']}")
            print(f"  R4 => {data['R4']}")
            print(f"  R6 => {data['R6']}")
            print(f"  R8 => {data['R8']}")
            
            return {"Draw1": data}
            
        except Exception as e:
            print(f"Error extracting {section} Set{set_num} Draw1: {e}")
            return {"Draw1": {}}
    
    def extract_all(self):
        """
        Extract all data from the Excel file
        
        Returns:
            Dictionary with structure:
            {
                "Midday": {
                    "Set3": { "Draw1": {...} },
                    "Set2": { "Draw1": {...} },
                    "Set1": {
                        "Draw1": {...},
                        "Draw2": {...},
                        ...
                        "Draw7": {...}
                    }
                },
                "Evening": {...},
                "Combined": {...}
            }
        """
        all_data = {}
        
        for section in ['Midday', 'Evening', 'Combined']:
            all_data[section] = {}

            # Set1 uses the existing 7-draw extraction with column slicing.
            print(f"\nExtracting {section} Set1...")
            all_data[section]["Set1"] = self.extract_set1(section)

            # Set2 and Set3 each extract only one draw (Draw1) using all 7 columns.
            print(f"\nExtracting {section} Set2...")
            all_data[section]["Set2"] = self.extract_single_draw(section, set_num=2)

            print(f"\nExtracting {section} Set3...")
            all_data[section]["Set3"] = self.extract_single_draw(section, set_num=3)

        return all_data

def process_state(state_name, cleaned_dir):
    """Process a single state's cleaned file"""
    excel_path = os.path.join(cleaned_dir, f"{state_name}_cleaned.xlsx")
    if not os.path.exists(excel_path):
        print(f"Warning: File not found for {state_name}: {excel_path}")
        return None
    
    try:
        print(f"\nProcessing {state_name}...")
        extractor = LotteryDataExtractor(excel_path)
        data = extractor.extract_all()
        print(f"✓ Successfully processed {state_name}")
        return data
    except Exception as e:
        print(f"Error processing {state_name}: {str(e)}")
        return None

def extract_all_states(states_list, cleaned_dir):
    """
    Extract data for all states
    
    Args:
        states_list: List of states to process
        cleaned_dir: Directory containing cleaned Excel files
        
    Returns:
        Dictionary mapping state names to extracted data
    """
    results = {}
    
    for state in states_list:
        state_file = os.path.join(cleaned_dir, f"{state}_cleaned.xlsx")
        if not os.path.exists(state_file):
            print(f"Error: Cleaned file for {state} not found at {state_file}")
            continue
        
        print(f"\nExtracting data for {state}...")
        data = process_state(state, cleaned_dir)
        if data:
            results[state] = data
    
    return results

if __name__ == "__main__":
    # Get paths
    cleaned_dir = get_cleaned_data_dir()
    
    # Process a test state
    test_state = "Connecticut4"
    test_file = get_cleaned_state_path(test_state)
    
    if os.path.exists(test_file):
        print(f"Testing extraction with {test_state}...")
        data = process_state(test_state, cleaned_dir)
        if data:
            print("\nExtraction successful!")
            print("Data structure:")
            for section in data:
                print(f"\n{section}:")
                for set_name in data[section]:
                    print(f"  {set_name}:")
                    for draw in data[section][set_name]:
                        print(f"    {draw}")
    else:
        print(f"Test file not found: {test_file}")
        print("Please run clean_data.py first to generate cleaned files.") 