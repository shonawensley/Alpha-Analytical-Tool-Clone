import streamlit as st
import json
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Add the scripts directory to the path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Import our modules
try:
    from table_formatter import TableFormatter
    from pattern_mapper import PatternMapper
    from auto_pattern_analyzer import AutoPatternAnalyzer
except ImportError as e:
    st.error(f"Error importing modules: {e}")
    st.stop()

st.set_page_config(page_title="Lottery Pattern Analyzer", layout="wide")

st.title("Automatic Lottery Pattern Analyzer")
st.write("This app automatically finds and highlights significant patterns in lottery data")

# Sidebar for file selection and options
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
    
    st.header("Analysis Options")
    
    # Pattern analysis options
    min_cluster_size = st.slider(
        "Minimum Cluster Size", 
        min_value=2, 
        max_value=4, 
        value=2,
        help="Minimum number of rows a pattern must appear in to be considered a cluster"
    )
    
    min_frequency = st.slider(
        "Minimum Pattern Frequency", 
        min_value=2, 
        max_value=10, 
        value=3,
        help="Minimum number of times a pattern must appear to be considered significant"
    )
    
    top_n = st.slider(
        "Number of Top Patterns", 
        min_value=5, 
        max_value=30, 
        value=10,
        help="Number of top patterns to display"
    )
    
    # Run analysis button
    run_analysis = st.button("Run Analysis")

# Main content area
if file_path and run_analysis:
    # Load data
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            lottery_data = json.load(f)
        except json.JSONDecodeError:
            st.error("Error decoding JSON file. Please ensure it's valid JSON.")
            st.stop()
    
    state_name = lottery_data.get("state_name", "Unknown State")
    st.subheader(f"Analyzing data for {state_name}")
    
    # Create analyzer and run analysis
    with st.spinner("Analyzing patterns... This may take a moment"):
        analyzer = AutoPatternAnalyzer(lottery_data)
        top_patterns = analyzer.get_top_patterns(count=top_n)
    
    if not top_patterns:
        st.warning("No significant patterns found with the current settings. Try adjusting the minimum cluster size or frequency.")
        st.stop()
    
    # Display top patterns
    st.subheader(f"Top {len(top_patterns)} Significant Patterns")
    
    # Convert to DataFrame for better display
    patterns_data = []
    for pattern, info in top_patterns:
        patterns_data.append({
            "Pattern": pattern,
            "Score": info["score"],
            "Frequency": info["frequency"],
            "Hot Zone Count": info["hot_zone_count"],
            "Cluster Size Total": info["cluster_size_total"],
            "Section Count": info["section_count"]
        })
    
    df = pd.DataFrame(patterns_data)
    st.dataframe(df)
    
    # Visualize top patterns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top Patterns by Score")
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Get top 10 for visualization
        viz_data = df.head(min(10, len(df)))
        ax.barh(
            viz_data["Pattern"],
            viz_data["Score"],
            color="skyblue"
        )
        ax.invert_yaxis()  # Highest at the top
        plt.xlabel("Score")
        plt.ylabel("Pattern")
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        st.subheader("Score Components")
        # Create stacked bar chart of score components
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        
        # Get top 5 patterns for components visualization
        viz_data = df.head(min(5, len(df)))
        
        # Create the stacked bar
        ax2.bar(
            viz_data["Pattern"],
            viz_data["Frequency"],
            label="Frequency"
        )
        ax2.bar(
            viz_data["Pattern"],
            viz_data["Hot Zone Count"],
            bottom=viz_data["Frequency"],
            label="Hot Zone Bonus"
        )
        
        # Calculate remaining score (cluster size + section bonus)
        remaining = viz_data["Score"] - viz_data["Frequency"] - viz_data["Hot Zone Count"]
        ax2.bar(
            viz_data["Pattern"],
            remaining,
            bottom=viz_data["Frequency"] + viz_data["Hot Zone Count"],
            label="Other Bonuses"
        )
        
        plt.ylabel("Score Components")
        plt.xlabel("Pattern")
        plt.legend()
        plt.tight_layout()
        st.pyplot(fig2)
    
    # Pattern detail explorer
    st.subheader("Pattern Detail Explorer")
    
    # Select pattern to explore
    selected_pattern = st.selectbox(
        "Select a pattern to explore",
        [p[0] for p in top_patterns]
    )
    
    # Get the selected pattern info
    selected_pattern_info = next((info for pat, info in top_patterns if pat == selected_pattern), None)
    
    if selected_pattern_info:
        # Display pattern details
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f"### Pattern: {selected_pattern}")
            st.markdown(f"**Total Score:** {selected_pattern_info['score']}")
            st.markdown(f"**Frequency:** {selected_pattern_info['frequency']}")
            st.markdown(f"**Hot Zone Count:** {selected_pattern_info['hot_zone_count']}")
            st.markdown(f"**Cluster Size Total:** {selected_pattern_info['cluster_size_total']}")
            st.markdown(f"**Appears in {selected_pattern_info['section_count']} sections**")
        
        with col2:
            # Show locations in a table
            locations_data = []
            for loc in selected_pattern_info["locations"]:
                locations_data.append({
                    "Section": loc["section"],
                    "Set": loc["set"],
                    "Draw": loc["draw"],
                    "Column": loc["column"],
                    "Rows": ", ".join(loc["rows"]),
                    "Hot Zone": "Yes" if loc["is_hot_zone"] else "No"
                })
            
            locations_df = pd.DataFrame(locations_data)
            st.markdown("### Pattern Locations")
            st.dataframe(locations_df)
        
        # Select a location to display the table
        if selected_pattern_info["locations"]:
            st.subheader(f"View Table with Highlighted Pattern '{selected_pattern}'")
            
            # Create a selection for section/set
            sections = sorted(set(loc["section"] for loc in selected_pattern_info["locations"]))
            selected_section = st.selectbox("Select Section", sections)
            
            # Filter locations by selected section
            section_locations = [loc for loc in selected_pattern_info["locations"] if loc["section"] == selected_section]
            sets = sorted(set(loc["set"] for loc in section_locations))
            selected_set = st.selectbox("Select Set", sets)
            
            # Generate and display the table
            table = analyzer.highlight_pattern_in_table(selected_section, selected_set, selected_pattern)
            st.markdown("```\n" + table + "\n```")

else:
    if not file_path:
        st.info("Please select a JSON file from the sidebar")
    elif not run_analysis:
        st.info("Click 'Run Analysis' in the sidebar to start")

# Explanation of the analysis
with st.expander("What is this analysis doing?"):
    st.markdown("""
    ### Automatic Pattern Analysis
    
    This tool automatically searches for significant patterns in the lottery data by:
    
    1. **Finding Clusters**: Identifying patterns that appear in multiple rows (R2, R4, R6, R8) within a column
    2. **Scoring Patterns**: Evaluating patterns based on:
       - Frequency (how often the pattern appears)
       - Hot Zone presence (patterns in hot zones receive bonus points)
       - Cluster size (larger clusters receive more points)
       - Section coverage (patterns that appear in multiple sections receive bonus points)
    3. **Highlighting Top Patterns**: The highest-scoring patterns are likely the most significant for prediction
    
    ### How to Use This Analysis
    
    1. Look for patterns with high scores that appear in hot zones
    2. Pay attention to patterns that appear across multiple sections (Midday, Evening, Combined)
    3. Use the pattern explorer to see where each pattern appears in the tables
    4. Focus on stable patterns (appear in multiple rows) in hot zones for potential predictions
    """) 