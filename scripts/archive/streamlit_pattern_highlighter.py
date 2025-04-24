import streamlit as st
import json
import os
import sys
import pandas as pd
import re
from collections import defaultdict, Counter

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

st.set_page_config(page_title="Lottery Stable Pattern Analyzer", layout="wide")

st.title("Lottery Stable Pattern Analyzer")
st.write("This app identifies and highlights stable patterns in lottery data tables")

# Helper function to find stable patterns in a table
def find_stable_patterns(json_data, section, set_name, min_cluster_size=2, min_length=3):
    """
    Find stable patterns in a specific section and set
    
    Args:
        json_data: The JSON lottery data
        section: Midday/Evening/Combined
        set_name: Set1/Set2/Set3
        min_cluster_size: Minimum number of rows to be considered a cluster
        min_length: Minimum pattern length
        
    Returns:
        dict: Dictionary mapping draw_name+column to a list of stable patterns
    """
    try:
        # Make sure the section and set exist
        if section not in json_data["sections"] or set_name not in json_data["sections"][section]["sets"]:
            return {}
            
        # Initialize pattern mapper for convenient access
        mapper = PatternMapper(json_data)
        
        # Store stable patterns by location
        stable_patterns = {}
        
        # For each draw in the set
        for draw_num in range(1, 8):  # Draws 1-7
            draw_name = f"Draw{draw_num}"
            
            # Skip if draw doesn't exist
            if draw_name not in json_data["sections"][section]["sets"][set_name]["draws"]:
                continue
                
            # Calculate number of columns for this draw (staircase structure)
            column_count = 8 - draw_num  # Draw1 has 7 columns, Draw7 has 1
            
            # For each column in the draw
            for col in range(1, column_count + 1):
                # Get the box data
                box = mapper.get_box(section, set_name, draw_name, col)
                if not box:
                    continue
                
                # Extract all substring patterns of length min_length or more from each row
                row_patterns = defaultdict(set)  # Maps pattern to set of rows it appears in
                
                for row_type in ["R2", "R4", "R6", "R8"]:
                    if row_type not in box:
                        continue
                        
                    # Get pattern string for this row
                    pattern = box[row_type]
                    
                    # Find all substrings of min_length or longer (up to 6 digits)
                    for i in range(len(pattern) - min_length + 1):
                        for j in range(i + min_length, min(i + 7, len(pattern) + 1)):
                            substr = pattern[i:j]
                            row_patterns[substr].add(row_type)
                
                # Filter patterns that appear in at least min_cluster_size rows
                stable_patterns_in_box = []
                for pattern, rows in row_patterns.items():
                    if len(rows) >= min_cluster_size:
                        is_hot = box["metadata"].get("is_hot_zone", False)
                        stable_patterns_in_box.append({
                            "pattern": pattern,
                            "rows": list(rows),
                            "row_count": len(rows),
                            "is_hot_zone": is_hot
                        })
                
                # If we found stable patterns, store them
                if stable_patterns_in_box:
                    location = f"{draw_name}_Column{col}"
                    stable_patterns[location] = stable_patterns_in_box
        
        return stable_patterns
        
    except Exception as e:
        st.error(f"Error analyzing patterns: {str(e)}")
        return {}

# Helper function to display tables with highlighted patterns
def display_tables_with_patterns(json_data, section, set_name, stable_patterns):
    """
    Display tables with stable patterns highlighted
    
    Args:
        json_data: The JSON lottery data
        section: Midday/Evening/Combined
        set_name: Set1/Set2/Set3
        stable_patterns: Dictionary of stable patterns by location
    """
    # Use TableFormatter to generate base table
    formatter = TableFormatter(json_data)
    table_text = formatter.display_table(section, set_name, style="ascii")
    
    # Convert the ASCII table to HTML with pattern highlighting
    rows = table_text.strip().split('\n')
    html_rows = []
    
    # Process each row
    current_draw = None
    current_col = None
    draw_col_indices = {}  # Maps draw+column to column indices in the table
    
    # First pass: identify the structure and positions
    for i, row in enumerate(rows):
        # Track current draw
        if "| Draw" in row and "Col" not in row:
            draw_match = re.search(r'\| (Draw\d+)', row)
            if draw_match:
                current_draw = draw_match.group(1)
        
        # Track column positions
        if "| Draw    |" in row:
            # This is the header row with column indices
            parts = row.split('|')
            for j, part in enumerate(parts):
                if "Col" in part:
                    col_num = int(re.search(r'Col (\d+)', part).group(1))
                    if current_draw:
                        draw_col_indices[f"{current_draw}_Column{col_num}"] = j
    
    # Second pass: create HTML with highlighting
    in_table_data = False
    for i, row in enumerate(rows):
        # Check if this is a draw header
        if "| Draw" in row and "Col" not in row:
            draw_match = re.search(r'\| (Draw\d+)', row)
            if draw_match:
                current_draw = draw_match.group(1)
                html_rows.append(f"<tr><th colspan='100%'>{current_draw}</th></tr>")
                continue
        
        # Check if this is a column header
        if "| Draw    |" in row:
            parts = row.split('|')
            html_row = "<tr>"
            for part in parts:
                if part.strip():
                    html_row += f"<th>{part.strip()}</th>"
            html_row += "</tr>"
            html_rows.append(html_row)
            in_table_data = True
            continue
        
        # Check if this is a divider row
        if row.startswith("+-") or row.startswith("|--"):
            continue
        
        # Process data rows
        if in_table_data and row.startswith("|"):
            parts = row.split('|')
            row_type = None
            
            # Extract row type (R2, R4, R6, R8)
            if len(parts) > 1:
                row_type = parts[1].strip()
            
            html_row = "<tr>"
            for j, part in enumerate(parts):
                cell_content = part.strip()
                cell_class = ""
                
                # Skip empty cells
                if not cell_content:
                    continue
                
                # Determine if this cell contains a stable pattern
                if current_draw and row_type in ["R2", "R4", "R6", "R8"]:
                    # Check each column
                    for col_num in range(1, 8):
                        location = f"{current_draw}_Column{col_num}"
                        if location in stable_patterns and j == draw_col_indices.get(location, -1):
                            # This cell is in a location with stable patterns
                            patterns_here = stable_patterns[location]
                            
                            # Check if any of the patterns apply to this row
                            applicable_patterns = []
                            for pattern_info in patterns_here:
                                if row_type in pattern_info["rows"]:
                                    applicable_patterns.append(pattern_info["pattern"])
                            
                            # Highlight the cell if it has applicable patterns
                            if applicable_patterns:
                                cell_content_highlighted = cell_content
                                for pattern in applicable_patterns:
                                    # Add highlighting spans for each pattern
                                    cell_content_highlighted = cell_content_highlighted.replace(
                                        pattern, 
                                        f"<span class='highlight'>{pattern}</span>"
                                    )
                                cell_content = cell_content_highlighted
                                cell_class = "has-pattern"
                
                # Add the cell to the HTML row
                if row_type in ["R2", "R4", "R6", "R8"]:
                    html_row += f"<td class='{row_type} {cell_class}'>{cell_content}</td>"
                else:
                    html_row += f"<td>{cell_content}</td>"
            
            html_row += "</tr>"
            html_rows.append(html_row)
    
    # Join the HTML rows into a table
    html_table = f"""
    <style>
    table {{
        border-collapse: collapse;
        width: 100%;
        font-family: monospace;
    }}
    th, td {{
        border: 1px solid #ddd;
        padding: 5px;
        text-align: left;
    }}
    th {{
        background-color: #f2f2f2;
        font-weight: bold;
    }}
    tr:nth-child(even) {{
        background-color: #f9f9f9;
    }}
    .R2 {{ background-color: #f8f8ff; }}
    .R4 {{ background-color: #fff8f8; }}
    .R6 {{ background-color: #f8fff8; }}
    .R8 {{ background-color: #fff8ff; }}
    .has-pattern {{ background-color: #dfd; }}
    .highlight {{ 
        background-color: #afa; 
        font-weight: bold;
        color: #060;
    }}
    </style>
    <table>
    {"".join(html_rows)}
    </table>
    """
    
    return html_table

# Helper function to summarize all patterns across the data
def summarize_all_patterns(json_data, sections, sets, min_cluster_size=2, min_length=3):
    """Summarize all stable patterns found in the data"""
    all_patterns = []
    pattern_frequency = Counter()
    
    for section in sections:
        for set_name in sets:
            patterns = find_stable_patterns(
                json_data, section, set_name, 
                min_cluster_size=min_cluster_size, 
                min_length=min_length
            )
            
            # Process each location's patterns
            for location, pattern_list in patterns.items():
                for pattern_info in pattern_list:
                    pattern = pattern_info["pattern"]
                    is_hot = pattern_info["is_hot_zone"]
                    row_count = pattern_info["row_count"]
                    
                    # Update frequency counter
                    pattern_frequency[pattern] += 1
                    
                    # Add to all patterns list
                    all_patterns.append({
                        "section": section,
                        "set": set_name,
                        "location": location,
                        "pattern": pattern,
                        "row_count": row_count,
                        "is_hot_zone": is_hot
                    })
    
    # Add frequency to each pattern
    for pattern in all_patterns:
        pattern["frequency"] = pattern_frequency[pattern["pattern"]]
    
    return all_patterns

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
    
    min_pattern_length = st.slider(
        "Minimum Pattern Length", 
        min_value=3, 
        max_value=6, 
        value=3,
        help="Minimum number of digits in a pattern"
    )
    
    # Section selection
    sections = st.multiselect(
        "Sections to Analyze",
        ["Midday", "Evening", "Combined"],
        default=["Midday", "Evening", "Combined"]
    )
    
    sets = st.multiselect(
        "Sets to Analyze",
        ["Set1", "Set2", "Set3"],
        default=["Set1"]
    )
    
    # Run analysis button
    run_analysis = st.button("Run Stable Pattern Analysis")

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
    
    # Run stable pattern analysis across all selected sections/sets
    with st.spinner("Analyzing stable patterns... This may take a moment"):
        # Gather all stable patterns
        all_patterns = summarize_all_patterns(
            lottery_data, sections, sets, 
            min_cluster_size=min_cluster_size, 
            min_length=min_pattern_length
        )
        
        # Create pattern frequency table
        pattern_counts = Counter()
        for pattern in all_patterns:
            pattern_counts[pattern["pattern"]] += 1
        
        # Get top patterns 
        top_patterns = pattern_counts.most_common(15)
        
        if top_patterns:
            # Show summary of top patterns
            st.subheader("Top Stable Patterns")
            
            # Create DataFrame for display
            top_pattern_data = []
            for pattern, count in top_patterns:
                # Get all instances of this pattern
                instances = [p for p in all_patterns if p["pattern"] == pattern]
                
                # Calculate stats
                hot_zone_count = sum(1 for p in instances if p["is_hot_zone"])
                max_row_count = max(p["row_count"] for p in instances)
                sections_present = set(p["section"] for p in instances)
                
                top_pattern_data.append({
                    "Pattern": pattern,
                    "Frequency": count,
                    "Hot Zone Count": hot_zone_count,
                    "Max Row Count": max_row_count,
                    "Sections": ", ".join(sections_present)
                })
            
            # Display as table
            top_df = pd.DataFrame(top_pattern_data)
            st.dataframe(top_df)
            
            # Display tables with highlighted patterns for each section/set
            st.subheader("Tables with Highlighted Stable Patterns")
            st.write("Green highlighting shows stable patterns that appear in multiple rows")
            
            # Create tabs for each section
            section_tabs = st.tabs(sections)
            
            for i, section in enumerate(sections):
                with section_tabs[i]:
                    # Create tabs for each set
                    set_tabs = st.tabs(sets)
                    
                    for j, set_name in enumerate(sets):
                        with set_tabs[j]:
                            # Find stable patterns for this section/set
                            stable_patterns = find_stable_patterns(
                                lottery_data, section, set_name, 
                                min_cluster_size=min_cluster_size, 
                                min_length=min_pattern_length
                            )
                            
                            if stable_patterns:
                                # Generate HTML table with highlighted patterns
                                html_table = display_tables_with_patterns(
                                    lottery_data, section, set_name, stable_patterns
                                )
                                
                                # Display the HTML table
                                st.markdown(html_table, unsafe_allow_html=True)
                                
                                # Show pattern details
                                st.subheader(f"Stable Pattern Details for {section}:{set_name}")
                                
                                # Create a detailed list of patterns by location
                                for location, patterns in stable_patterns.items():
                                    st.markdown(f"**{location}**")
                                    
                                    pattern_details = []
                                    for pattern_info in patterns:
                                        pattern_details.append({
                                            "Pattern": pattern_info["pattern"],
                                            "Rows": ", ".join(pattern_info["rows"]),
                                            "Row Count": pattern_info["row_count"],
                                            "Hot Zone": "Yes" if pattern_info["is_hot_zone"] else "No"
                                        })
                                    
                                    st.dataframe(pd.DataFrame(pattern_details))
                            else:
                                st.info(f"No stable patterns found in {section}:{set_name} with current settings")
        else:
            st.warning("No stable patterns found with the current settings. Try adjusting the minimum cluster size or pattern length.")

else:
    if not file_path:
        st.info("Please select a JSON file from the sidebar")
    elif not run_analysis:
        st.info("Click 'Run Stable Pattern Analysis' in the sidebar to start")

# Explanation of the analysis
with st.expander("What are Stable Patterns?"):
    st.markdown("""
    ### Stable Patterns in Lottery Data
    
    **Stable patterns** are sequences of digits that appear consistently across multiple rows (R2, R4, R6, R8) 
    within the same column of a lottery table. These patterns may indicate significant structures in the data.
    
    ### How This Analysis Works
    
    1. **Finding Clusters**: The tool identifies digit sequences that appear in multiple rows of the same column
    2. **Highlighting Patterns**: Patterns that meet the cluster criteria are highlighted in green
    3. **Scoring by Frequency**: Patterns are ranked by how frequently they appear across the dataset
    
    ### How to Interpret Results
    
    - **Green Highlighting**: Indicates stable patterns that appear in multiple rows
    - **Higher Frequency**: Patterns that appear more frequently may be more significant
    - **Hot Zones**: Patterns in hot zones (marked with * in the original data) may be especially important
    - **Cross-Section Appearance**: Patterns that appear in multiple sections (Midday/Evening/Combined) may have special significance
    
    Use these indicators to identify potential significant patterns for lottery prediction.
    """) 