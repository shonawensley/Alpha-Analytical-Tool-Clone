#!/usr/bin/env python
"""
streamlit_app.py - Streamlit interface for lottery data processing
"""

import os
import streamlit as st
import pandas as pd
from datetime import datetime

# Add the project root to Python path
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_root)

# Import from local modules
from clean_data import clean_all_states, STATES
from extract_data import LotteryDataExtractor
from table_generator import build_section_table, build_r2_only_table
from vtrac_utils import highlight_winners_in_table, find_vtrac_index_and_combos

def get_project_root():
    """Get the absolute path to the project root"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(current_dir))

def load_state_data(state_name, excel_path):
    """Load data for a single state"""
    try:
        extractor = LotteryDataExtractor(excel_path)
        return extractor.extract_all()
    except Exception as e:
        st.error(f"Error loading {state_name}: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="Lottery Data Viewer",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Enhanced CSS for better table display
    st.markdown("""
        <style>
        .stDataFrame table {
            width: 100% !important;
        }
        .stDataFrame td {
            min-width: 150px !important;
            max-width: none !important;
            white-space: nowrap !important;
            font-family: monospace !important;
            padding: 8px !important;
            border: 1px solid #e1e4e8 !important;
        }
        div[data-testid="stDataFrame"] div[data-testid="stTable"] {
            width: 100% !important;
        }
        /* Section styling */
        .section-border-set3 {
            border: 2px solid #1f77b4 !important;
            background-color: rgba(31, 119, 180, 0.1) !important;
        }
        .section-border-set2 {
            border: 2px solid #2ca02c !important;
            background-color: rgba(44, 160, 44, 0.1) !important;
        }
        .section-border-set1-draw1 {
            border: 2px solid #ff7f0e !important;
            background-color: rgba(255, 127, 14, 0.1) !important;
        }
        /* Winner highlighting */
        .winner {
            color: red !important;
            font-weight: bold !important;
        }
        .related {
            color: blue !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Get project paths
    project_root = get_project_root()
    original_dir = os.path.join(project_root, "data", "original")
    cleaned_dir = os.path.join(project_root, "data", "cleaned")
    
    # File upload in sidebar
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload Pick3StatsC4 Excel file", type=["xlsm", "xlsx"])
        
        if uploaded_file:
            # Create directories if they don't exist
            os.makedirs(original_dir, exist_ok=True)
            os.makedirs(cleaned_dir, exist_ok=True)
            
            # Save uploaded file
            excel_path = os.path.join(original_dir, uploaded_file.name)
            with open(excel_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            
            # Process the file
            with st.spinner("Processing Excel file..."):
                results = clean_all_states(STATES, excel_path, cleaned_dir)
                
                if results["success"]:
                    st.success(f"Processed {len(results['success'])} states successfully")
                if results["failed"]:
                    st.error(f"Failed to process {len(results['failed'])} states")
        
        # Winner inputs
        st.markdown("### Enter Winners")
        midday_winner = st.text_input("Midday Winner (3 digits):", placeholder="Enter 3 digits")
        evening_winner = st.text_input("Evening Winner (3 digits):", placeholder="Enter 3 digits")
    
    # Main content area
    if not uploaded_file:
        st.info("Please upload an Excel file to begin")
        return
    
    # State selection
    state = st.selectbox(
        "Select State to View",
        STATES,
        format_func=lambda x: x.replace("4", "")
    )
    
    # Load state data
    cleaned_file = os.path.join(cleaned_dir, f"{state}_cleaned.xlsx")
    if not os.path.exists(cleaned_file):
        st.error(f"No cleaned data found for {state}")
        return
        
    state_data = load_state_data(state, cleaned_file)
    if not state_data:
        return
    
    # Get related combinations if winners are entered
    winning_combos = set()
    related_combos = set()
    if midday_winner and len(midday_winner) == 3:
        _, winning_perms, related = find_vtrac_index_and_combos(midday_winner)
        winning_combos.update(winning_perms)
        related_combos.update(related)
    if evening_winner and len(evening_winner) == 3:
        _, winning_perms, related = find_vtrac_index_and_combos(evening_winner)
        winning_combos.update(winning_perms)
        related_combos.update(related)
    
    # Create three columns for Midday/Evening/Combined
    midday_col, evening_col, combined_col = st.columns(3)
    
    sections = {
        "Midday": (midday_col, state_data.get("Midday", {}), midday_winner),
        "Evening": (evening_col, state_data.get("Evening", {}), evening_winner),
        "Combined": (combined_col, state_data.get("Combined", {}), None)
    }
    
    for section_name, (column, section_data, winner) in sections.items():
        with column:
            st.markdown(f"### {section_name}")
            
            if section_data:
                # Build tables
                combined_df = build_section_table(section_data)
                r2_df = build_r2_only_table(section_data)
                
                # Style function for highlighting
                def style_function(val):
                    if not isinstance(val, str) or val in ['N/A', 'nan']:
                        return ''
                    if any(combo in val for combo in winning_combos):
                        return 'color: red; font-weight: bold'
                    if any(combo in val for combo in related_combos):
                        return 'color: blue'
                    return ''
                
                # Apply section styling and highlighting
                def style_df(df):
                    styled = df.style
                    
                    # Section background colors
                    styled = styled.apply(lambda x: [
                        'background-color: rgba(31, 119, 180, 0.1)' if x['Set'] == 'Set3'
                        else 'background-color: rgba(44, 160, 44, 0.1)' if x['Set'] == 'Set2'
                        else 'background-color: rgba(255, 127, 14, 0.1)' if (x['Set'] == 'Set1' and x['Draw'] == 'Draw1')
                        else '' for _ in range(len(x))
                    ], axis=1)
                    
                    # Winner highlighting
                    if winning_combos:
                        for col in df.columns:
                            if col not in ["Set", "Draw", "RowType"]:
                                styled = styled.applymap(style_function, subset=[col])
                    
                    return styled.set_properties(**{
                        'text-align': 'center',
                        'font-family': 'monospace',
                        'white-space': 'nowrap',
                        'padding': '8px'
                    })
                
                # Style and display tables
                combined_df_styled = style_df(combined_df)
                r2_df_styled = style_df(r2_df)
                
                st.markdown("#### Combined Table")
                st.dataframe(
                    combined_df_styled,
                    height=1800,  # Show all 38 rows
                    use_container_width=True
                )
                
                st.markdown("#### R2-only Table")
                st.dataframe(
                    r2_df_styled,
                    height=400,
                    use_container_width=True
                )
                
                # Download buttons
                csv_combined = combined_df.to_csv(index=False)
                csv_r2 = r2_df.to_csv(index=False)
                
                st.download_button(
                    f"Download {section_name} Combined Table",
                    csv_combined,
                    f"{state}_{section_name}_combined.csv",
                    "text/csv",
                    key=f'download-combined-{section_name.lower()}'
                )
                st.download_button(
                    f"Download {section_name} R2-only Table",
                    csv_r2,
                    f"{state}_{section_name}_r2.csv",
                    "text/csv",
                    key=f'download-r2-{section_name.lower()}'
                )

if __name__ == "__main__":
    main() 