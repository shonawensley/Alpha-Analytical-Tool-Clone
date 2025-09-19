#!/usr/bin/env python
"""
clustering_app_2.py - Enhanced V-TRAC analyzer with advanced clustering analysis

This app provides:
1. Data processing interface for cleaning and extracting lottery data
2. Table viewer for examining generated tables by state and section
3. Winner logging interface for highlighting and saving winners
4. Enhanced V-TRAC analyzer for identifying clusters across states
"""

import os
import sys
import time
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import seaborn as sns
import numpy as np
from datetime import datetime
import webbrowser
from pathlib import Path
import io
import base64
import shutil
from bs4 import BeautifulSoup

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
from utils.vtrac_utils import (
    find_vtrac_index_and_combos,
    BOXED_VTRAC_REFERENCE
)

def main():
    """Main application layout and execution"""
    # Page title
    st.title("Alpha Analytical Tool")
    
    # Create tabs
    tabs = st.tabs([
        "📊 Process Data", 
        "👁 View Results", 
        "🏆 Log Winners", 
        "📈 V-TRAC Analyzer"
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
    
    # Display date and time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.text(f"Last Updated: {now}")
    st.sidebar.title("Alpha Analytical Tool")

if __name__ == "__main__":
    main() 