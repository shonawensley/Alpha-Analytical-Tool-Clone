import streamlit as st
import json
import os
import pandas as pd
import sys

# Add the scripts directory to the path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Import our modules
try:
    from table_formatter import TableFormatter
    from pattern_mapper import PatternMapper
except ImportError as e:
    st.error(f"Error importing modules: {e}")
    st.stop()

st.set_page_config(page_title="Lottery Data Viewer", layout="wide")

st.title("Lottery Pattern Table Viewer")
st.write("View lottery data in tabular format and search for pattern clusters")

# Sidebar for selecting JSON file and options
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
    
    st.header("Display Options")
    
    # Section selection
    section = st.selectbox(
        "Select Section",
        ["Midday", "Evening", "Combined"],
        index=0
    )
    
    # Set selection
    set_name = st.selectbox(
        "Select Set",
        ["Set1", "Set2", "Set3"],
        index=0
    )
    
    # Pattern search
    pattern_search = st.text_input("Search for Pattern", value="", help="Enter a pattern to highlight in the table")
    
    # Find clusters
    with st.expander("Cluster Search Options"):
        cluster_pattern = st.text_input("Find Clusters Containing", value="455")
        min_cluster_size = st.slider("Minimum Cluster Size", 1, 4, 2)
        
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
    
    # Create formatter
    formatter = TableFormatter(lottery_data)
    
    # Display the table as ASCII art in a monospace font
    st.subheader(f"Pattern Table for {section} : {set_name}")
    table = formatter.display_table(section, set_name, style="ascii", highlight_pattern=pattern_search if pattern_search else None)
    
    st.markdown("```\n" + table + "\n```")
    
    # Find and display clusters
    if cluster_pattern:
        st.subheader(f"Clusters containing '{cluster_pattern}'")
        
        clusters = formatter.find_clusters(section, set_name, cluster_pattern, min_cluster=min_cluster_size)
        
        if clusters:
            # Convert clusters to a DataFrame for better display
            cluster_data = []
            for location, data in clusters.items():
                loc_parts = location.split(":")
                section_name = loc_parts[0] if len(loc_parts) > 0 else ""
                set_id = loc_parts[1] if len(loc_parts) > 1 else ""
                draw_name = loc_parts[2] if len(loc_parts) > 2 else ""
                column = loc_parts[3].replace("Column", "") if len(loc_parts) > 3 else ""
                
                patterns_str = ", ".join([f"{p['row_type']}:{p['pattern'][:6]}" for p in data["matching_patterns"]])
                
                cluster_data.append({
                    "Section": section_name,
                    "Set": set_id,
                    "Draw": draw_name,
                    "Column": column,
                    "Count": data["count"],
                    "Patterns": patterns_str,
                    "Hot Zone": "Yes" if data["is_hot_zone"] else "No"
                })
            
            df = pd.DataFrame(cluster_data)
            st.dataframe(df)
            
            # Display ASCII table as well
            with st.expander("View as ASCII Table"):
                cluster_table = formatter.display_clusters(clusters, style="ascii")
                st.markdown("```\n" + cluster_table + "\n```")
        else:
            st.info(f"No clusters containing '{cluster_pattern}' found with minimum size {min_cluster_size}")
    
    # Provide explanations and guides
    with st.expander("Understanding the Pattern Table"):
        st.markdown("""
        ### Table Format Explanation
        
        The pattern table is organized in a "staircase" structure:
        
        - **Rows**: Each Draw has 4 rows (R2, R4, R6, R8), representing different row types in the lottery data
        - **Columns**: Columns are numbered from right to left, with Column 1 being the rightmost column
        - **Staircase**: Each Draw shows progressively fewer columns:
          - Draw1 shows 7 columns
          - Draw2 shows 6 columns
          - ... and so on
        
        ### Pattern Markings
        
        - **Hot Zones**: Patterns in hot zones are marked with `*asterisks*`
        - **Highlighted Patterns**: Patterns matching your search term are marked with `!exclamation marks!`
        
        ### Clusters
        
        A cluster occurs when a pattern appears in multiple rows of the same column, indicating a stable pattern that may have significance for prediction.
        """)

else:
    if not file_path:
        st.info("Please select a JSON file from the sidebar")
    elif not run_analysis:
        st.info("Click 'Run Analysis' in the sidebar to start") 