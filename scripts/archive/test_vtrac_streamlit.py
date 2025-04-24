#!/usr/bin/env python
"""
Streamlit test page for V-TRAC functionality
"""

import streamlit as st
import pandas as pd
from pathlib import Path
import sys
import os

# Add scripts directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Import utility modules
from utils.vtrac_utils import find_vtrac_index_and_combos
from utils.table_generator import build_section_table, build_r2_only_table
from utils.extract_data import process_state

def highlight_patterns_in_string(string, patterns, color='red'):
    """Highlight patterns in a string with colored brackets"""
    result = string
    # Sort patterns by length (longest first) to avoid overlapping matches
    sorted_patterns = sorted(patterns, key=len, reverse=True)
    
    for pattern in sorted_patterns:
        start = 0
        while True:
            pos = string.find(pattern, start)
            if pos == -1:
                break
            # Replace the pattern with colored version
            result = result[:pos] + f"[{pattern}]" + result[pos + len(pattern):]
            start = pos + len(pattern)
    
    return result

def highlight_patterns_in_table(df, winning_patterns, related_patterns):
    """Highlight patterns in all strings in the table"""
    highlighted_df = df.copy()
    
    # Process each column that contains string data
    for col in df.columns:
        if df[col].dtype == 'object':  # Only process string columns
            highlighted_df[col] = df[col].apply(
                lambda x: highlight_patterns_in_string(str(x), winning_patterns, 'red') if pd.notna(x) else x
            )
            highlighted_df[col] = highlighted_df[col].apply(
                lambda x: highlight_patterns_in_string(str(x), related_patterns, 'blue') if pd.notna(x) else x
            )
    
    return highlighted_df

def main():
    st.title("V-TRAC Pattern Testing")
    
    # Sidebar for controls
    st.sidebar.header("Test Controls")
    
    # State selection
    states = [
        "Connecticut4", "Delaware4", "Florida4", "Indiana4",
        "Michigan4", "NewJersey4", "NewYork4", "NorthCarolina4", "Ohio4",
        "OntarioCanada4", "Pennsylvania4", "PuertoRico4", "SouthCarolina4", 
        "Virginia4"
    ]
    selected_state = st.sidebar.selectbox("Select State", states)
    
    # Section selection
    sections = ["Midday", "Evening", "Combined"]
    selected_section = st.sidebar.selectbox("Select Section", sections)
    
    # Number input
    test_number = st.sidebar.text_input("Enter 3-digit number to test", "123")
    
    if st.sidebar.button("Test V-TRAC"):
        try:
            # Process state data
            data_dir = Path(script_dir).parent / 'data' / 'cleaned'
            state_data = process_state(selected_state, str(data_dir))
            
            if state_data and selected_section in state_data:
                # Generate tables
                combined_df = build_section_table(state_data[selected_section])
                r2_df = build_r2_only_table(state_data[selected_section])
                
                # Show V-TRAC information
                st.subheader("V-TRAC Analysis")
                index, winning_patterns, related_patterns = find_vtrac_index_and_combos(test_number)
                
                if index is not None:
                    st.write(f"V-TRAC Index: {index}")
                    st.write("Winning Patterns:", ", ".join(sorted(winning_patterns)))
                    st.write("Related Patterns:", ", ".join(sorted(related_patterns)))
                    
                    # Highlight patterns in tables
                    st.subheader("Combined Table (Highlighted)")
                    highlighted_combined = highlight_patterns_in_table(combined_df, winning_patterns, related_patterns)
                    st.dataframe(highlighted_combined)
                    
                    st.subheader("R2-Only Table (Highlighted)")
                    highlighted_r2 = highlight_patterns_in_table(r2_df, winning_patterns, related_patterns)
                    st.dataframe(highlighted_r2)
                else:
                    st.warning("Number not found in V-TRAC reference")
            else:
                st.error("No data available for selected state/section")
                
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    # Add help text
    st.sidebar.markdown("""
    ### Instructions
    1. Select a state and section
    2. Enter a 3-digit number
    3. Click "Test V-TRAC" to see results
    """)

if __name__ == "__main__":
    main() 