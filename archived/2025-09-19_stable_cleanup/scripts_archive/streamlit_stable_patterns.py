import streamlit as st
import json
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict, Counter
import re

# Add the parent directory to the path so we can import from the stable_pattern_analysis_demo
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Import the functions from stable_pattern_analysis_demo.py
from stable_pattern_analysis_demo import (
    canonical_form, to_vtrac, is_three_value_pattern, has_mirror_digits,
    long_cluster_bonus, evaluate_boxed_vs_straight, extract_patterns_per_column,
    evaluate_horizontal_persistence, detect_lingering_patterns_in_draw,
    run_stable_extraction_on_json
)

# Set page title and layout
st.set_page_config(page_title="Lottery Stable Pattern Analysis", layout="wide")

st.title("Lottery Stable Pattern Analysis")
st.write("Analyze stable patterns in lottery data using V-Trac methodology")

# Sidebar for file selection
with st.sidebar:
    st.header("Input Data")
    json_files = []
    ai_exports_dir = os.path.join('data', 'ai_exports')
    
    if os.path.exists(ai_exports_dir):
        json_files = [f for f in os.listdir(ai_exports_dir) if f.endswith('.json')]
    
    if json_files:
        selected_file = st.selectbox(
            "Choose a JSON file to analyze",
            json_files,
            index=0
        )
        file_path = os.path.join(ai_exports_dir, selected_file)
    else:
        st.warning("No JSON files found in data/ai_exports directory")
        file_path = None
        
    # Analysis options
    st.header("Analysis Options")
    top_n = st.slider("Number of top patterns to display", 5, 50, 15)
    
    # Section filter
    section_filter = st.multiselect(
        "Filter by Section",
        ["Midday", "Evening", "Combined"],
        default=["Midday", "Evening", "Combined"]
    )
    
    # Run analysis button
    run_analysis = st.button("Run Analysis")

# Main content area
if file_path and run_analysis:
    # Load data
    with open(file_path, "r", encoding="utf-8") as f:
        lottery_data = json.load(f)
    
    state_name = lottery_data.get("state_name", "Unknown State")
    st.subheader(f"Analyzing data for {state_name}")
    
    # Run stable pattern extraction
    with st.spinner("Extracting stable patterns..."):
        full_analysis = run_stable_extraction_on_json(lottery_data)
    
    # Collect all patterns across entire dataset
    all_patterns = []
    for section_name, sets_dict in full_analysis.items():
        if section_name not in section_filter:
            continue
            
        for set_name, draws_dict in sets_dict.items():
            for draw_name, draw_data in draws_dict.items():
                col_list = draw_data["columns"]  # list of dicts
                for col_idx, col_dict in enumerate(col_list):
                    for can_pat, details in col_dict.items():
                        # We'll gather into a single list
                        # We'll keep track of location & total_score
                        row_info = {
                            "section": section_name,
                            "set": set_name,
                            "draw": draw_name,
                            "column_index": col_idx,
                            "pattern": can_pat,
                            "vertical_coverage": details["vertical_coverage"],
                            "hot_zone_bonus": details.get("hot_zone_bonus", 0),
                            "straight_bonus": details.get("straight_bonus", 0),
                            "box_bonus": details.get("box_permutation_bonus", 0),
                            "lingering_bonus": details.get("lingering_pattern_bonus", 0),
                            "horizontal_bonus": details.get("horizontal_persistence_score", 0),
                            "score": details["total_score"]
                        }
                        all_patterns.append(row_info)
    
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(all_patterns)
    
    # Sort by score descending
    df_sorted = df.sort_values('score', ascending=False)
    
    # Display top patterns table
    st.subheader(f"Top {top_n} Stable Patterns (By Total Score)")
    st.dataframe(
        df_sorted.head(top_n),
        column_config={
            "section": "Section",
            "set": "Set",
            "draw": "Draw",
            "column_index": st.column_config.NumberColumn("Column", format="%d"),
            "pattern": "Pattern",
            "vertical_coverage": st.column_config.NumberColumn("Vertical Coverage", format="%d"),
            "hot_zone_bonus": st.column_config.NumberColumn("Hot Zone Bonus", format="%d"),
            "straight_bonus": st.column_config.NumberColumn("Straight Bonus", format="%d"),
            "box_bonus": st.column_config.NumberColumn("Box Bonus", format="%d"),
            "lingering_bonus": st.column_config.NumberColumn("Lingering Bonus", format="%d"),
            "horizontal_bonus": st.column_config.NumberColumn("Horizontal Bonus", format="%d"),
            "score": st.column_config.NumberColumn("Total Score", format="%d"),
        },
        hide_index=True,
    )
    
    # Split the page into two columns for charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Bar chart of top scoring patterns
        st.subheader("Top 10 Patterns by Score")
        top10 = df_sorted.head(10)
        
        fig, ax = plt.figure(figsize=(10, 6)), plt.axes()
        ax.barh(
            [f"{r['pattern']}@{r['draw']}" for _, r in top10.iterrows()],
            top10['score'],
            color='skyblue'
        )
        ax.invert_yaxis()  # highest at the top
        plt.title("Top 10 Stable Patterns by Score")
        plt.xlabel("Score")
        plt.ylabel("Pattern@Draw")
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        # Score distribution by section
        st.subheader("Score Distribution by Section")
        section_avg = df.groupby('section')['score'].mean().reset_index()
        
        fig2, ax2 = plt.figure(figsize=(10, 6)), plt.axes()
        ax2.bar(
            section_avg['section'],
            section_avg['score'],
            color=['#ff9999', '#66b3ff', '#99ff99']
        )
        plt.title("Average Pattern Score by Section")
        plt.xlabel("Section")
        plt.ylabel("Average Score")
        plt.tight_layout()
        st.pyplot(fig2)
    
    # Pattern details
    st.subheader("Explore Pattern Details")
    pattern_to_explore = st.selectbox(
        "Select a pattern to explore details", 
        df_sorted['pattern'].unique()
    )
    
    if pattern_to_explore:
        pattern_data = df[df['pattern'] == pattern_to_explore]
        st.write(f"**Pattern '{pattern_to_explore}' appears in {len(pattern_data)} locations:**")
        
        # Display all occurrences of the selected pattern
        st.dataframe(
            pattern_data.sort_values('score', ascending=False),
            hide_index=True
        )
        
        # Show distribution across sections/draws
        fig3, ax3 = plt.figure(figsize=(10, 5)), plt.axes()
        pattern_sections = pattern_data.groupby(['section', 'draw']).size().reset_index(name='count')
        section_colors = {'Midday': '#ff9999', 'Evening': '#66b3ff', 'Combined': '#99ff99'}
        
        for section in pattern_sections['section'].unique():
            section_data = pattern_sections[pattern_sections['section'] == section]
            ax3.scatter(
                section_data['draw'], 
                section_data['count'],
                label=section,
                color=section_colors.get(section, 'gray'),
                s=100
            )
        
        plt.title(f"Pattern '{pattern_to_explore}' Distribution")
        plt.xlabel("Draw")
        plt.ylabel("Occurrences")
        plt.legend()
        plt.tight_layout()
        st.pyplot(fig3)

else:
    if not file_path:
        st.info("Please select a JSON file from the sidebar")
    elif not run_analysis:
        st.info("Click 'Run Analysis' in the sidebar to start")

# Add information about how to interpret the results
with st.expander("How to Interpret the Results"):
    st.markdown("""
    ### Understanding Stable Patterns
    
    **Stable patterns** are digit clusters that appear with consistency across multiple rows
    (R2, R4, R6, R8) and potentially across multiple columns. The analysis assigns scores to
    patterns based on several factors:
    
    - **Vertical Coverage**: How many different rows (R2/R4/R6/R8) the pattern appears in
    - **Hot Zone Bonus**: Extra points for patterns in "hot zones" (marked with * or **)
    - **Straight Bonus**: Points for exact same digit order appearing multiple times
    - **Box Bonus**: Points for different arrangements of the same digits
    - **Lingering Bonus**: When a pattern appears in multiple columns of a draw
    - **Horizontal Bonus**: When a pattern continues from one column to the next
    
    Higher scoring patterns are generally more significant and may be worth closer study.
    
    ### V-Trac Methodology
    
    V-Trac groups mirror digits:
    - 0, 5 → 1
    - 1, 6 → 2  
    - 2, 7 → 3
    - 3, 8 → 4
    - 4, 9 → 5
    
    This allows us to detect patterns even when mirror digits are substituted.
    """) 