#!/usr/bin/env python
"""
Streamlit test page for V-TRAC functionality
"""

import streamlit as st
import pandas as pd
from pathlib import Path
import sys
import os

# Add scripts to path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

from utils.vtrac_utils import find_vtrac_index_and_combos
from vtrac.winner_highlighter import highlight_winners
from utils.table_generator import build_section_table, build_r2_only_table
from utils.extract_data import process_state

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
                index, winning_perms, related_combos = find_vtrac_index_and_combos(test_number)
                
                if index is not None:
                    st.write(f"V-TRAC Index: {index}")
                    st.write("Winning Permutations:", ", ".join(sorted(winning_perms)))
                    st.write("Related Combinations:", ", ".join(sorted(related_combos)))
                else:
                    st.warning("Number not found in V-TRAC reference")
                
                # Show highlighted tables
                st.subheader("Combined Table (Highlighted)")
                highlighted_combined = highlight_winners(combined_df, test_number)
                st.dataframe(highlighted_combined)
                
                st.subheader("R2-Only Table (Highlighted)")
                highlighted_r2 = highlight_winners(r2_df, test_number)
                st.dataframe(highlighted_r2)
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