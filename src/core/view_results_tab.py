import os
import re
import streamlit as st
from utils.path_handler import get_tables_output_dir

STATE_RE = re.compile(r'.*[A-Za-z]4$')   # matches "Florida4" etc.

def view_results_tab():
    st.title("View Results")
    output_dir = get_tables_output_dir()
    available_states = [
        d for d in os.listdir(output_dir)
        if os.path.isdir(os.path.join(output_dir, d))
        and STATE_RE.match(d)
    ]
    if not available_states:
        st.warning("No state data available. Please process data first.")
        return
    selected_state = st.selectbox("Select State", available_states)
    state_dir = os.path.join(output_dir, selected_state)
    if os.path.exists(state_dir):
        files = [f for f in os.listdir(state_dir) if f.endswith('.csv')]
        if not files:
            st.warning(f"No CSV files found for {selected_state}")
            return
        selected_file = st.selectbox("Select File", files)
        file_path = os.path.join(state_dir, selected_file)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                st.text(f.read())
        else:
            st.error(f"File {selected_file} not found.")
    else:
        st.error(f"Directory for {selected_state} not found.") 