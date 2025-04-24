"""
test_app.py

A test Streamlit app to demonstrate the auxiliary analysis features.
This app is completely separate from the main application and does not
modify any existing functionality.
"""

import os
import sys
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from collections import Counter, defaultdict

# Add parent directory to path to import other modules
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
project_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)
sys.path.append(project_dir)

# Import draw extractor
from auxiliary.draw_extractor import get_state_columns, load_draw_data, extract_state_draws

# Page configuration
st.set_page_config(
    page_title="Lottery Draw Data Extractor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to get Excel file path
def get_excel_path():
    """Find the Pick3StatsC4.xlsm file in the standard data folder."""
    excel_path = os.path.join(project_dir, "data", "original", "Pick3StatsC4.xlsm")
    if not os.path.exists(excel_path):
        return None
    return excel_path

# Function to get Draw Analysis
def analyze_draws(draws_list):
    """Analyze a list of draw numbers to find patterns and statistics."""
    if not draws_list:
        return None
    
    # Extract draw numbers (ignore dates)
    draw_numbers = [draw for _, draw in draws_list]
    
    # Basic statistics
    total_draws = len(draw_numbers)
    unique_draws = len(set(draw_numbers))
    
    # Count frequency of each draw
    draw_counts = Counter(draw_numbers)
    most_common = draw_counts.most_common(5)
    least_common = draw_counts.most_common()[:-6:-1]
    
    # Digit analysis
    first_digits = [int(draw[0]) for draw in draw_numbers]
    second_digits = [int(draw[1]) for draw in draw_numbers]
    third_digits = [int(draw[2]) for draw in draw_numbers]
    
    digit_positions = {
        "First Digit": Counter(first_digits),
        "Second Digit": Counter(second_digits),
        "Third Digit": Counter(third_digits)
    }
    
    # Analyze digit combinations
    pairs = []
    for draw in draw_numbers:
        pairs.append(draw[0:2])  # First two digits
        pairs.append(draw[1:3])  # Last two digits
    pair_counts = Counter(pairs)
    
    # Check for consecutive draws
    consecutive_draws = []
    for i in range(1, len(draw_numbers)):
        if draw_numbers[i] == draw_numbers[i-1]:
            consecutive_draws.append((draw_numbers[i-1], draw_numbers[i]))
    
    return {
        "total_draws": total_draws,
        "unique_draws": unique_draws,
        "draw_counts": draw_counts,
        "most_common": most_common,
        "least_common": least_common,
        "digit_positions": digit_positions,
        "pair_counts": pair_counts,
        "consecutive_draws": consecutive_draws
    }

# Function to generate visualizations
def generate_visualizations(analysis, state_name):
    """Generate visualization charts for draw analysis."""
    if not analysis:
        return
    
    # Frequency distribution of all draws
    st.subheader(f"Draw Frequency Distribution - {state_name}")
    
    # Convert to DataFrame for easier plotting
    draw_counts_df = pd.DataFrame.from_dict(
        analysis["draw_counts"], 
        orient='index',
        columns=['frequency']
    ).reset_index()
    draw_counts_df.columns = ['Draw', 'Frequency']
    
    # Sort by draw number for the chart
    draw_counts_df = draw_counts_df.sort_values('Draw')
    
    # Plot frequency distribution
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=draw_counts_df.sample(min(50, len(draw_counts_df))), x='Draw', y='Frequency', ax=ax)
    ax.set_title(f"Frequency Distribution (Sample of 50 Draws)")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    st.pyplot(fig)
    
    # Digit position analysis
    st.subheader("Digit Frequency by Position")
    
    # Create figure with 3 subplots (one for each position)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for i, (position, counts) in enumerate(analysis["digit_positions"].items()):
        # Convert to DataFrame
        df = pd.DataFrame.from_dict(counts, orient='index', columns=['frequency']).reset_index()
        df.columns = ['Digit', 'Frequency']
        df = df.sort_values('Digit')
        
        # Plot
        sns.barplot(data=df, x='Digit', y='Frequency', ax=axes[i])
        axes[i].set_title(position)
        axes[i].set_xlabel("Digit")
        axes[i].set_ylabel("Frequency")
    
    fig.tight_layout()
    st.pyplot(fig)
    
    # Most common and least common draws
    st.subheader("Most Common and Least Common Draws")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Most Common Draws:")
        most_common_df = pd.DataFrame(analysis["most_common"], columns=["Draw", "Frequency"])
        st.dataframe(most_common_df)
    
    with col2:
        st.write("Least Common Draws:")
        least_common_df = pd.DataFrame(analysis["least_common"], columns=["Draw", "Frequency"])
        st.dataframe(least_common_df)
    
    # Pair frequency analysis
    st.subheader("Most Common Digit Pairs")
    
    # Get top 20 pairs
    top_pairs = pd.DataFrame(analysis["pair_counts"].most_common(20), columns=["Pair", "Frequency"])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=top_pairs, x='Pair', y='Frequency', ax=ax)
    ax.set_title("Top 20 Most Common Digit Pairs")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    st.pyplot(fig)

# Main Application
def main():
    st.title("Lottery Draw Data Extractor and Analyzer")
    
    # Sidebar
    st.sidebar.title("Controls")
    
    # Excel file selection
    excel_path = get_excel_path()
    if not excel_path:
        st.error("Excel file not found in the standard location. Please check the data/original folder.")
        return
        
    st.sidebar.info(f"Using Excel file: {os.path.basename(excel_path)}")
    
    # Load the dataframe first to pass to get_state_columns
    try:
        df = load_draw_data(excel_path)
        if df is None:
            st.error("Failed to load Excel file. Please check that it exists and has the proper format.")
            return
            
        # Get state columns directly from the mapping
        state_cols = get_state_columns(df)
        available_states = list(state_cols.keys())
        
        if not available_states:
            st.error("No states defined in the state mapping.")
            return
        
        selected_state = st.sidebar.selectbox(
            "Select State to Analyze",
            available_states
        )
        
        max_draws = st.sidebar.slider(
            "Maximum Number of Draws to Analyze",
            min_value=50,
            max_value=1000,
            value=200,
            step=50
        )
        
        if st.sidebar.button("Extract and Analyze Data"):
            with st.spinner("Extracting draw data..."):
                state_col = state_cols[selected_state]
                draws = extract_state_draws(df, state_col, max_draws=max_draws)
                
                if not draws:
                    st.error(f"No draw data found for {selected_state}")
                    return
                
                # Display raw data
                st.subheader(f"Raw Draw Data for {selected_state}")
                st.write(f"Total draws extracted: {len(draws)}")
                
                draws_df = pd.DataFrame(draws, columns=["Date", "Draw"])
                st.dataframe(draws_df)
                
                # Analyze the draws
                analysis = analyze_draws(draws)
                
                # Generate visualizations
                generate_visualizations(analysis, selected_state)
                
                # Show some statistics
                st.subheader("Draw Statistics")
                st.write(f"Total Draws: {analysis['total_draws']}")
                st.write(f"Unique Draws: {analysis['unique_draws']}")
                st.write(f"Coverage: {analysis['unique_draws']/1000:.2%} of all possible 3-digit combinations")
                
                if analysis['consecutive_draws']:
                    st.write(f"Number of consecutive repeated draws: {len(analysis['consecutive_draws'])}")
    
    except Exception as e:
        st.error(f"Error processing data: {str(e)}")
        st.exception(e)

if __name__ == "__main__":
    main() 