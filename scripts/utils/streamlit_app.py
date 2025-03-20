#!/usr/bin/env python
"""
streamlit_app.py - Streamlit interface for lottery data processing
"""

import os
import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path
import tempfile

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
from excel_export import export_state_tables, setup_logging_directories

def get_project_root():
    """Get the absolute path to the project root"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(current_dir))

@st.cache_data
def process_excel_file(excel_path, cleaned_dir):
    """Process Excel file and clean all states (cached)"""
    return clean_all_states(STATES, excel_path, cleaned_dir)

@st.cache_data
def load_state_data(state_name, excel_path):
    """Load data for a single state (cached)"""
    try:
        extractor = LotteryDataExtractor(excel_path)
        return extractor.extract_all()
    except Exception as e:
        st.error(f"Error loading {state_name}: {str(e)}")
        return None

@st.cache_data
def build_tables(section_data):
    """Build combined and R2-only tables (cached)"""
    if not section_data:
        return None, None
    return build_section_table(section_data), build_r2_only_table(section_data)

def initialize_session_state():
    """Initialize session state variables"""
    if 'processed_states' not in st.session_state:
        st.session_state.processed_states = {}
    if 'last_upload' not in st.session_state:
        st.session_state.last_upload = None

def get_historical_files():
    """Get list of available historical Excel files."""
    historical_dir = Path("data/historical_files")
    if not historical_dir.exists():
        return []
    return sorted([f for f in historical_dir.glob("*.xlsx") if "Pick3StatsC4" in f.name])

def export_all_tables_to_csv(state_data, state_name):
    """Export all tables (Midday/Evening/Combined) to a single CSV file"""
    import pandas as pd
    import os
    from datetime import datetime
    
    # Create output directory if it doesn't exist
    output_dir = "data/archive"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Initialize list to store all tables
    all_tables = []
    section_names = []
    
    # Process each section
    for section in ["Midday", "Evening", "Combined"]:
        if section not in state_data:
            continue
            
        # Build tables for this section
        combined_df = build_section_table(state_data[section])
        r2_df = build_r2_only_table(state_data[section])
        
        # Add section name as prefix to column names (except Set, Draw, RowType)
        combined_df.columns = [f"{section}_{col}" if col not in ["Set", "Draw", "RowType"] else col 
                             for col in combined_df.columns]
        r2_df.columns = [f"{section}_{col}" if col not in ["Set", "Draw"] else col 
                        for col in r2_df.columns]
        
        # Store tables
        all_tables.extend([combined_df, r2_df])
        section_names.extend([f"{section}_Combined", f"{section}_R2"])
    
    # Create Excel-like format with tables side by side
    max_rows = max(len(df) for df in all_tables)
    padded_tables = []
    
    for df in all_tables:
        # Pad shorter tables with NaN rows
        if len(df) < max_rows:
            padding = pd.DataFrame(index=range(len(df), max_rows), columns=df.columns)
            df = pd.concat([df, padding])
        padded_tables.append(df)
    
    # Combine all tables horizontally
    final_df = pd.concat(padded_tables, axis=1)
    
    # Save to CSV
    output_file = os.path.join(output_dir, f"{state_name}_all_tables_{timestamp}.csv")
    final_df.to_csv(output_file, index=False)
    
    return output_file

def main():
    st.set_page_config(
        page_title="Lottery Data Viewer",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    initialize_session_state()
    
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
    
    # File selection section
    st.header("Data Source Selection")
    upload_col, historical_col = st.columns(2)
    
    with upload_col:
        st.subheader("Upload New File")
        uploaded_file = st.file_uploader("Choose a Pick3StatsC4 Excel file", type=["xlsx", "xlsm"])
    
    with historical_col:
        st.subheader("Historical Files")
        historical_files = get_historical_files()
        if historical_files:
            file_dates = [datetime.strptime(f.stem.split('_')[-1], '%Y%m%d') if '_' in f.stem else None for f in historical_files]
            file_options = [f"{f.name} ({d.strftime('%Y-%m-%d') if d else 'No date'}" for f, d in zip(historical_files, file_dates)]
            selected_file = st.selectbox("Select historical file", file_options, index=None)
            if selected_file:
                file_index = file_options.index(selected_file)
                file_path = historical_files[file_index]
                uploaded_file = file_path
    
    if uploaded_file is None:
        st.warning("Please upload a Pick3StatsC4 Excel file or select one from historical files.")
        return

    # Save uploaded file to historical_files if it's new
    if hasattr(uploaded_file, 'name'):  # It's a new upload
        file_name = uploaded_file.name
        if "Pick3StatsC4" in file_name:
            save_path = Path("data/historical_files") / file_name
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            st.success(f"File saved to historical files: {file_name}")
    
    # State selection
    state = st.selectbox(
        "Select State to View",
        STATES,
        format_func=lambda x: x.replace("4", "")
    )
    
    # Load state data (using session state cache)
    cleaned_file = os.path.join(cleaned_dir, f"{state}_cleaned.xlsx")
    if not os.path.exists(cleaned_file):
        st.error(f"No cleaned data found for {state}")
        return
    
    if state not in st.session_state.processed_states:
        state_data = load_state_data(state, cleaned_file)
        if state_data:
            st.session_state.processed_states[state] = state_data
    
    state_data = st.session_state.processed_states.get(state)
    if not state_data:
        return
    
    # Get related combinations if winners are entered
    winning_combos = set()
    related_combos = set()
    midday_winner = None
    evening_winner = None
    
    if state_data.get("Midday", {}):
        midday_winner = state_data["Midday"].get("winning_combos", "")
        if midday_winner:
            _, winning_perms, related = find_vtrac_index_and_combos(midday_winner)
            winning_combos.update(winning_perms)
            related_combos.update(related)
    
    if state_data.get("Evening", {}):
        evening_winner = state_data["Evening"].get("winning_combos", "")
        if evening_winner:
            _, winning_perms, related = find_vtrac_index_and_combos(evening_winner)
            winning_combos.update(winning_perms)
            related_combos.update(related)
    
    # Add a button to log all tables for this state
    if st.button(f"Log All {state} Tables to Excel"):
        try:
            # Set up archive directory
            archive_dir = setup_logging_directories()
            
            # Get the DataFrames
            midday_df = build_section_table(state_data.get("Midday", {}))
            evening_df = build_section_table(state_data.get("Evening", {}))
            combined_df = build_section_table(state_data.get("Combined", {}))
            
            # Export to Excel
            filepath = export_state_tables(
                state,
                midday_df,
                evening_df,
                combined_df,
                archive_dir
            )
            
            st.success(f"Successfully saved tables to: {filepath}")
        except Exception as e:
            st.error(f"Error saving tables: {str(e)}")

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
                # Build tables (cached)
                combined_df, r2_df = build_tables(section_data)
                
                if combined_df is None or r2_df is None:
                    continue
                
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

                # After displaying tables, add logging button
                if st.button(f"Log {state} Results", key=f"log-{section_name.lower()}"):
                    try:
                        # Prepare data for export
                        tables_data = {
                            'Midday': st.session_state.processed_states[state].get('Midday', {}).get('combined_table'),
                            'Evening': st.session_state.processed_states[state].get('Evening', {}).get('combined_table'),
                            'Combined': st.session_state.processed_states[state].get('Combined', {}).get('combined_table')
                        }
                        
                        # Set up archive directory
                        archive_dir = setup_logging_directories()
                        
                        # Export to Excel
                        filepath = export_state_tables(
                            state,
                            tables_data,
                            winning_combos,
                            related_combos,
                            archive_dir
                        )
                        
                        st.success(f"Successfully logged results to: {filepath}")
                    except Exception as e:
                        st.error(f"Error logging results: {str(e)}")

    # Add export all tables button
    if st.button("Export All Tables (Midday/Evening/Combined)"):
        try:
            output_file = export_all_tables_to_csv(state_data, state)
            st.success(f"All tables exported to: {output_file}")
        except Exception as e:
            st.error(f"Error exporting tables: {str(e)}")

if __name__ == "__main__":
    main() 