#!/usr/bin/env python
"""
streamlit_app.py - Interactive web interface for lottery data processing

This app provides:
1. Data processing interface for cleaning and extracting lottery data
2. Table viewer for examining generated tables by state and section
3. Winner logging interface for highlighting and saving winners
4. V-TRAC analyzer for checking number patterns
"""

import os
import sys
import time
import pandas as pd
import streamlit as st
from datetime import datetime

# Add script directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Import utility modules
from utils.path_handler import (
    get_excel_path,
    create_output_directories,
    get_cleaned_data_dir,
    get_tables_output_dir,
    get_winners_output_dir
)
from utils.state_utils import STATES
from utils.clean_data import clean_all_states
from utils.extract_data import extract_all_states
from utils.table_generator import generate_tables
from vtrac.winner_highlighter import highlight_winners_in_tables
from utils.vtrac_utils import find_vtrac_index_and_combos

# Set page config
st.set_page_config(
    page_title="Lottery Data Processor",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Lottery Data Processor")
st.sidebar.image("https://img.icons8.com/fluency/96/lottery.png", width=80)
st.sidebar.markdown("---")

# Helper functions
def format_time(seconds):
    """Format time in seconds to human-readable string"""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    else:
        minutes = int(seconds // 60)
        sec = seconds % 60
        return f"{minutes} min {sec:.2f} sec"

def check_excel_file():
    """Check if the Excel file exists and return its path"""
    excel_path = get_excel_path()
    excel_exists = os.path.exists(excel_path)
    return excel_path, excel_exists

def load_state_data(state_name):
    """Load generated tables for a specific state"""
    tables_dir = os.path.join(get_tables_output_dir(), state_name)
    result = {}
    
    if os.path.exists(tables_dir):
        for filename in os.listdir(tables_dir):
            if filename.endswith(".csv"):
                filepath = os.path.join(tables_dir, filename)
                key = os.path.splitext(filename)[0].replace(f"{state_name}_", "")
                try:
                    df = pd.read_csv(filepath)
                    result[key] = df
                except Exception as e:
                    st.error(f"Error loading {filename}: {e}")
    
    return result

def process_data_tab():
    """Process Data Tab Content"""
    st.header("Process Lottery Data")
    
    # Check if Excel file exists
    excel_path, excel_exists = check_excel_file()
    
    if not excel_exists:
        st.error(f"Excel file not found at {excel_path}")
        st.warning("Please place the 'Pick3StatsC4.xlsm' file in the data/original directory.")
        return
    
    st.success(f"Found Excel file: {os.path.basename(excel_path)}")
    
    # Create columns for processing options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        clean_data = st.checkbox("Clean Data", value=True)
    with col2:
        extract_data = st.checkbox("Extract Data", value=True)
    with col3:
        generate_tables_option = st.checkbox("Generate Tables", value=True)
    
    # Add multi-select for states
    selected_states = st.multiselect(
        "Select States to Process (leave empty for all states)",
        options=STATES,
        default=[]
    )
    
    # Use all states if none selected
    states_to_process = selected_states if selected_states else STATES
    
    # Process button
    if st.button("Process Data", type="primary"):
        # Create progress bar and status
        progress_bar = st.progress(0)
        status = st.empty()
        results = st.empty()
        
        # Create output directories
        create_output_directories()
        
        # Initialize processing summary
        summary = {
            "cleaned_states": [],
            "failed_clean": [],
            "extracted_states": [],
            "tables_generated": []
        }
        
        with st.spinner("Processing data..."):
            # Step 1: Clean data
            if clean_data:
                status.info("Step 1/3: Cleaning data...")
                start_time = time.time()
                
                cleaning_results = clean_all_states(
                    states_to_process, 
                    excel_path, 
                    get_cleaned_data_dir()
                )
                
                summary["cleaned_states"] = cleaning_results["success"]
                summary["failed_clean"] = cleaning_results["failed"]
                
                progress_bar.progress(33)
                duration = time.time() - start_time
                status.success(f"Data cleaning completed in {format_time(duration)}")
            else:
                progress_bar.progress(33)
                status.info("Skipping data cleaning step")
            
            # Step 2: Extract data
            extracted_data = {}
            if extract_data:
                status.info("Step 2/3: Extracting data...")
                start_time = time.time()
                
                extracted_data = extract_all_states(
                    states_to_process,
                    get_cleaned_data_dir()
                )
                
                summary["extracted_states"] = list(extracted_data.keys())
                
                progress_bar.progress(66)
                duration = time.time() - start_time
                status.success(f"Data extraction completed in {format_time(duration)}")
            else:
                progress_bar.progress(66)
                status.info("Skipping data extraction step")
            
            # Step 3: Generate tables
            if generate_tables_option and extracted_data:
                status.info("Step 3/3: Generating tables...")
                start_time = time.time()
                
                for state_name, state_data in extracted_data.items():
                    generate_tables(
                        state_data,
                        state_name,
                        os.path.join(get_tables_output_dir(), state_name)
                    )
                    summary["tables_generated"].append(state_name)
                
                progress_bar.progress(100)
                duration = time.time() - start_time
                status.success(f"Table generation completed in {format_time(duration)}")
            else:
                progress_bar.progress(100)
                status.info("Skipping table generation step")
        
        # Show processing summary
        results.markdown("### Processing Summary")
        st.write(f"**States Processed:** {len(states_to_process)}")
        
        if clean_data:
            st.write(f"**Successfully Cleaned:** {len(summary['cleaned_states'])}")
            if summary["failed_clean"]:
                st.warning(f"**Failed to Clean:** {', '.join(summary['failed_clean'])}")
        
        if extract_data:
            st.write(f"**Successfully Extracted:** {len(summary['extracted_states'])}")
        
        if generate_tables_option:
            st.write(f"**Tables Generated:** {len(summary['tables_generated'])}")
        
        st.success("Processing completed!")

def view_results_tab():
    """View Results Tab Content"""
    st.header("View Results")
    
    # Select state
    state = st.selectbox("Select State", STATES)
    
    # Load data for selected state
    state_data = load_state_data(state)
    
    if not state_data:
        st.warning(f"No data found for {state}. Please process data first.")
        return
    
    # Create tabs for different sections
    tables_tabs = st.tabs(["Midday", "Evening", "Combined"])
    
    for i, section in enumerate(["Midday", "Evening", "Combined"]):
        with tables_tabs[i]:
            # Combined table
            combined_key = f"{section}_combined"
            r2_key = f"{section}_r2"
            
            st.subheader(f"{section} - Combined Table")
            if combined_key in state_data:
                st.dataframe(
                    state_data[combined_key], 
                    use_container_width=True,
                    height=400
                )
                
                # Download option
                csv = state_data[combined_key].to_csv(index=False)
                st.download_button(
                    f"Download {section} Combined Table",
                    data=csv,
                    file_name=f"{state}_{section}_combined.csv",
                    mime="text/csv",
                )
            else:
                st.info(f"No {section} combined table available")
            
            # R2 table
            st.subheader(f"{section} - R2 Table")
            if r2_key in state_data:
                st.dataframe(
                    state_data[r2_key],
                    use_container_width=True,
                    height=250
                )
                
                # Download option
                csv = state_data[r2_key].to_csv(index=False)
                st.download_button(
                    f"Download {section} R2 Table",
                    data=csv,
                    file_name=f"{state}_{section}_r2.csv",
                    mime="text/csv",
                )
            else:
                st.info(f"No {section} R2 table available")

def log_winners_tab():
    """Log Winners Tab Content"""
    st.header("Log & Highlight Winners")
    
    # Form for winner inputs
    with st.form("winners_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Midday Winners")
            midday_winners = st.text_input(
                "Enter Midday winning numbers (separated by spaces)",
                placeholder="e.g. 123 456 789"
            )
        
        with col2:
            st.subheader("Evening Winners")
            evening_winners = st.text_input(
                "Enter Evening winning numbers (separated by spaces)",
                placeholder="e.g. 123 456 789"
            )
        
        # Select states to process
        selected_states = st.multiselect(
            "Select States to Process (leave empty for all)",
            options=STATES,
            default=[]
        )
        
        submit_button = st.form_submit_button("Highlight Winners", type="primary")
    
    # Process winners when submitted
    if submit_button:
        if not midday_winners and not evening_winners:
            st.warning("Please enter at least one winning number")
            return
        
        # Parse winners
        midday_list = [w.strip() for w in midday_winners.split() if w.strip()]
        evening_list = [w.strip() for w in evening_winners.split() if w.strip()]
        
        # Preview winners
        if midday_list:
            st.write("Midday Winners:", ", ".join(midday_list))
        if evening_list:
            st.write("Evening Winners:", ", ".join(evening_list))
        
        # States to process
        states_to_process = selected_states if selected_states else STATES
        st.write(f"Processing {len(states_to_process)} states...")
        
        # Progress tracking
        progress_bar = st.progress(0)
        status = st.empty()
        
        # Process each state
        for i, state_name in enumerate(states_to_process):
            status.info(f"Processing {state_name}...")
            
            # Load tables for this state
            tables = load_state_data(state_name)
            
            if not tables:
                st.warning(f"No tables found for {state_name}")
                continue
            
            # Highlight winners
            highlighted_tables = highlight_winners_in_tables(
                tables,
                midday_list,
                evening_list
            )
            
            # Save highlighted tables
            output_dir = os.path.join(get_winners_output_dir(), state_name)
            os.makedirs(output_dir, exist_ok=True)
            
            for section_key, df in highlighted_tables.items():
                if df is not None and not df.empty:
                    # Create winner-specific filename
                    winners_suffix = ""
                    if "Midday" in section_key and midday_list:
                        winners_suffix = f"_win{'_'.join(midday_list)}"
                    elif "Evening" in section_key and evening_list:
                        winners_suffix = f"_win{'_'.join(evening_list)}"
                    elif "Combined" in section_key and (midday_list or evening_list):
                        winners_suffix = "_winners"
                    
                    output_file = os.path.join(
                        output_dir, 
                        f"{state_name}_{section_key}{winners_suffix}.csv"
                    )
                    df.to_csv(output_file, index=False)
            
            # Update progress
            progress = (i + 1) / len(states_to_process)
            progress_bar.progress(progress)
        
        # Complete
        status.success("Winner highlighting completed!")
        
        # Show sample results
        if states_to_process:
            st.subheader("Sample Results (First State)")
            first_state = states_to_process[0]
            sample_tables = load_state_data(first_state)
            
            if "Midday_combined" in sample_tables and midday_list:
                st.write("Midday Combined Table (with winners):")
                highlighted = highlight_winners_in_tables(
                    {"Midday_combined": sample_tables["Midday_combined"]},
                    midday_list,
                    []
                )
                st.dataframe(highlighted["Midday_combined"], use_container_width=True)
            
            if "Evening_combined" in sample_tables and evening_list:
                st.write("Evening Combined Table (with winners):")
                highlighted = highlight_winners_in_tables(
                    {"Evening_combined": sample_tables["Evening_combined"]},
                    [],
                    evening_list
                )
                st.dataframe(highlighted["Evening_combined"], use_container_width=True)

def vtrac_analyzer_tab():
    """V-TRAC Analyzer Tab Content"""
    st.header("V-TRAC Analyzer")
    
    # V-TRAC explanation
    with st.expander("What is V-TRAC?"):
        st.markdown("""
        **V-TRAC System** classifies 3-digit numbers based on their digit patterns:
        
        - **VTRAC0**: All three digits are the same (e.g., 111, 222) - 10 combinations
        - **VTRAC1**: Two digits are the same (e.g., 112, 122) - 90 combinations  
        - **VTRAC2**: All three digits are different (e.g., 123, 456) - 720 combinations
        
        This system helps identify potential number patterns and highlight winners.
        """)
    
    # Number input
    number = st.text_input(
        "Enter a 3-digit number to analyze", 
        max_chars=3,
        placeholder="123"
    )
    
    if number:
        # Clean input
        number = ''.join(c for c in number if c.isdigit())
        
        if len(number) > 0:
            # Pad with zeros if less than 3 digits
            if len(number) < 3:
                number = number.zfill(3)
            
            # Find V-TRAC index
            vtrac_idx = find_vtrac_index_and_combos(number)
            
            # Get match information
            match_info = find_vtrac_index_and_combos(number)
            
            # Display result
            st.markdown(f"### Analysis for Number: {number}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**V-TRAC Index**: VTRAC{vtrac_idx}")
                
                if vtrac_idx == 0:
                    st.markdown("**Pattern**: AAA (all digits the same)")
                elif vtrac_idx == 1:
                    st.markdown("**Pattern**: AAB (two digits the same)")
                elif vtrac_idx == 2:
                    st.markdown("**Pattern**: ABC (all digits different)")
            
            with col2:
                st.markdown(f"**Total Matches**: {len(match_info['potential_matches'])}")
                
                # Calculate probability
                total_combs = 10 + 90 + 720  # Total possible 3-digit combinations
                probability = len(match_info['potential_matches']) / total_combs * 100
                
                st.markdown(f"**Probability**: {probability:.2f}%")
            
            # Show exact matches
            if match_info['exact_matches']:
                with st.expander(f"Exact Matches ({len(match_info['exact_matches'])})"):
                    st.write(match_info['exact_matches'])
                    
                    # Create downloadable file of matches
                    matches_df = pd.DataFrame(match_info['exact_matches'], columns=["Number"])
                    csv = matches_df.to_csv(index=False)
                    st.download_button(
                        "Download Exact Matches",
                        data=csv,
                        file_name=f"vtrac_{number}_exact_matches.csv",
                        mime="text/csv"
                    )
            
            # Show all potential matches
            with st.expander(f"All Potential Matches ({len(match_info['potential_matches'])})"):
                # Split into chunks for better display
                chunk_size = 10
                matches = match_info['potential_matches']
                chunks = [matches[i:i+chunk_size] for i in range(0, len(matches), chunk_size)]
                
                for i, chunk in enumerate(chunks):
                    st.write(", ".join(chunk))
                    
                    if i >= 9:  # Limit display to first 10 chunks
                        st.write("... and more")
                        break
                
                # Create downloadable file of all matches
                matches_df = pd.DataFrame(match_info['potential_matches'], columns=["Number"])
                csv = matches_df.to_csv(index=False)
                st.download_button(
                    "Download All Potential Matches",
                    data=csv,
                    file_name=f"vtrac_{number}_all_matches.csv",
                    mime="text/csv"
                )

def main():
    """Main function to run the Streamlit app"""
    # Show app title
    st.title("Lottery Data Processing System")
    
    # Create tabs
    tabs = st.tabs([
        "📊 Process Data", 
        "👁️ View Results", 
        "🏆 Log Winners",
        "🧩 V-TRAC Analyzer"
    ])
    
    # Process Data tab
    with tabs[0]:
        process_data_tab()
    
    # View Results tab
    with tabs[1]:
        view_results_tab()
    
    # Log Winners tab
    with tabs[2]:
        log_winners_tab()
    
    # V-TRAC Analyzer tab
    with tabs[3]:
        vtrac_analyzer_tab()
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.info(
        "This application processes lottery data from Pick3StatsC4.xlsm file. "
        "Place the file in the data/original directory to get started."
    )
    
    # Display date and time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.text(f"Last Updated: {now}")

if __name__ == "__main__":
    main() 