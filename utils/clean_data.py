#!/usr/bin/env python
"""
clean_data.py - Cleans and normalizes Pick3StatsC4.xlsm sheets for all states
"""
import os
import sys
import pandas as pd

STATES = [
    "Connecticut4", "Delaware4", "Florida4", "Indiana4",
    "Michigan4", "NewJersey4", "NewYork4", "NorthCarolina4", "Ohio4",
    "OntarioCanada4", "Pennsylvania4", "PuertoRico4", "SouthCarolina4", 
    "Virginia4"
]

def clean_excel_file(input_path, output_path, sheet_name):
    """Clean a single state's sheet from the Excel file"""
    print(f"\nProcessing state: {sheet_name}")
    print(f"Reading file: {input_path}")
    
    try:
        df = pd.read_excel(input_path, sheet_name=sheet_name, dtype=str)
        
        # Define columns to keep
        columns_to_keep = [
            'Q', 'S',  # Midday indicators and draws
            'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB',  # Midday data
            'AD', 'AF',  # Evening indicators
            'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO',  # Evening data
            'BD',  # Combined indicators
            'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO'  # Combined data
        ]
        
        # Filter to only existing columns
        existing_columns = [col for col in columns_to_keep if col in df.columns]
        
        if not existing_columns:
            print(f"Error: None of the required columns were found for {sheet_name}")
            return False
            
        print(f"Processing {len(existing_columns)} columns")
        
        # Create cleaned dataframe
        cleaned_df = df[existing_columns]
        
        # Clean the data
        def clean_value(x):
            return str(x).strip() if pd.notnull(x) else ''
        
        cleaned_df = cleaned_df.map(clean_value)
        
        # Save the cleaned file
        cleaned_df.to_excel(output_path, index=False)
        print(f"Cleaned file saved to: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error processing {sheet_name}: {str(e)}")
        return False

def clean_all_states(states_list, excel_path, output_dir):
    """Process all states in the Excel file"""
    os.makedirs(output_dir, exist_ok=True)
    
    successful = []
    failed = []
    
    for state in states_list:
        output_path = os.path.join(output_dir, f"{state}_cleaned.xlsx")
        if clean_excel_file(excel_path, output_path, state):
            successful.append(state)
        else:
            failed.append(state)
            
    return {"success": successful, "failed": failed}

if __name__ == "__main__":
    # Get paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    
    input_path = os.path.join(project_root, 'data', 'original', 'Pick3StatsC4.xlsm')
    cleaned_dir = os.path.join(project_root, 'data', 'cleaned')
    
    if not os.path.exists(input_path):
        print(f"\nError: Input file not found at {input_path}")
        sys.exit(1)
        
    results = clean_all_states(STATES, input_path, cleaned_dir)
    
    # Print summary
    print("\n=== Processing Summary ===")
    print(f"Successfully processed {len(results['success'])} states:")
    for state in results['success']:
        print(f"✓ {state}")
    
    if results['failed']:
        print(f"\nFailed to process {len(results['failed'])} states:")
        for state in results['failed']:
            print(f"✗ {state}") 