import streamlit as st
import json
import os
import re
from collections import defaultdict

# Set page title and layout
st.set_page_config(page_title="Lottery Stable Pattern Analyzer", layout="wide")

st.title("Lottery Stable Pattern Analyzer")
st.write("This app automatically detects and highlights stable patterns in lottery data tables")

# Simple pattern detection function
def find_stable_patterns(data, min_cluster_size=2, min_pattern_length=3):
    """
    Find all stable patterns (sequences appearing in multiple rows) in the data
    """
    stable_patterns = {}
    
    try:
        # For each section
        for section_name in ["Midday", "Evening", "Combined"]:
            if section_name not in data.get("sections", {}):
                continue
                
            section = data["sections"][section_name]
            
            # For each set
            for set_name in ["Set1", "Set2", "Set3"]:
                if set_name not in section.get("sets", {}):
                    continue
                    
                set_data = section["sets"][set_name]
                
                # For each draw
                for draw_name, draw_data in set_data.get("draws", {}).items():
                    # Get pattern variations
                    variations = draw_data.get("pattern_variations", {})
                    
                    # Get the number of columns
                    column_count = 0
                    for row_type in ["R2", "R4", "R6", "R8"]:
                        if row_type in variations:
                            column_count = max(column_count, len(variations[row_type]))
                    
                    # For each column
                    for col_idx in range(column_count):
                        # Get patterns from each row
                        column_patterns = {}
                        
                        for row_type in ["R2", "R4", "R6", "R8"]:
                            if row_type not in variations:
                                continue
                                
                            row_patterns = variations[row_type]
                            if col_idx < len(row_patterns):
                                pattern = row_patterns[col_idx]
                                
                                # Extract substrings of min_pattern_length or longer
                                for i in range(len(pattern) - min_pattern_length + 1):
                                    for j in range(i + min_pattern_length, min(i + 7, len(pattern) + 1)):
                                        substr = pattern[i:j]
                                        if substr not in column_patterns:
                                            column_patterns[substr] = set()
                                        column_patterns[substr].add(row_type)
                        
                        # Find patterns that meet the cluster criteria
                        location = f"{section_name}:{set_name}:{draw_name}:Column{col_idx+1}"
                        stable_patterns[location] = []
                        
                        for pattern, rows in column_patterns.items():
                            if len(rows) >= min_cluster_size:
                                is_hot = draw_data.get("metadata", {}).get("is_hot_zone", False)
                                stable_patterns[location].append({
                                    "pattern": pattern,
                                    "rows": list(rows),
                                    "row_count": len(rows),
                                    "is_hot_zone": is_hot
                                })
                        
                        # Remove empty locations
                        if not stable_patterns[location]:
                            del stable_patterns[location]
                            
        return stable_patterns
        
    except Exception as e:
        st.error(f"Error analyzing patterns: {str(e)}")
        return {}

# Simple ASCII table function
def generate_table_ascii(data, section_name, set_name):
    """Generate ASCII table for the given section and set"""
    try:
        # Check if section and set exist
        if section_name not in data.get("sections", {}) or set_name not in data["sections"][section_name].get("sets", {}):
            return f"No data found for {section_name}:{set_name}"
            
        section = data["sections"][section_name]
        set_data = section["sets"][set_name]
        
        rows = []
        
        # Add header
        header = "+--------+"
        header_row = "| Draw   |"
        for i in range(7, 0, -1):  # Columns from 7 to 1
            header += "---------+"
            header_row += f" Col {i}  |"
        
        rows.append(header)
        rows.append(header_row)
        rows.append(header)
        
        # For each draw (1-7)
        for draw_num in range(1, 8):
            draw_name = f"Draw{draw_num}"
            
            # Skip if draw doesn't exist
            if draw_name not in set_data.get("draws", {}):
                continue
                
            draw_data = set_data["draws"][draw_name]
            
            # Add draw header
            rows.append(f"| {draw_name:<6} |" + " " * 9 * 7 + "|")
            
            # Get pattern variations
            variations = draw_data.get("pattern_variations", {})
            
            # Generate rows for R2, R4, R6, R8
            for row_type in ["R2", "R4", "R6", "R8"]:
                if row_type not in variations:
                    continue
                    
                # Get patterns for this row
                patterns = variations[row_type]
                
                # Calculate the number of columns based on draw number
                # In a staircase pattern, Draw1 has 7 columns, Draw7 has 1
                col_count = 8 - draw_num
                
                # Generate row data
                row_data = f"| {row_type:<6} |"
                
                # Add empty cells for missing columns
                for i in range(7 - col_count):
                    row_data += " " * 8 + "|"
                
                # Add pattern data
                for i in range(col_count):
                    # Get pattern at reverse index (last element is column 1)
                    pattern_idx = col_count - i - 1
                    
                    if pattern_idx < len(patterns):
                        pattern = patterns[pattern_idx]
                        # Limit to 7 chars to fit in cell
                        pattern = pattern[:7]
                        row_data += f" {pattern:<7} |"
                    else:
                        row_data += " " * 8 + "|"
                
                rows.append(row_data)
            
            rows.append(header)
        
        return "\n".join(rows)
        
    except Exception as e:
        return f"Error generating table: {str(e)}"

# HTML table with patterns highlighted
def generate_html_table(data, section_name, set_name, stable_patterns):
    """Generate HTML table with patterns highlighted"""
    try:
        # Get ASCII table first
        ascii_table = generate_table_ascii(data, section_name, set_name)
        
        # Convert to HTML with highlighting
        lines = ascii_table.split("\n")
        html_rows = []
        
        current_draw = None
        col_indices = {}  # Maps column numbers to indices in the table row
        
        # First pass: find column indices and structure
        for i, line in enumerate(lines):
            if "| Draw" in line and "Col" not in line:
                # This is a draw header
                match = re.search(r'\| (Draw\d+)', line)
                if match:
                    current_draw = match.group(1)
            
            if "| Draw   |" in line:
                # This is the column header row
                parts = line.split("|")
                for j, part in enumerate(parts):
                    if "Col" in part:
                        col_num = int(re.search(r'Col (\d+)', part).group(1))
                        col_indices[col_num] = j
        
        # Second pass: create HTML with highlighting
        in_table = False
        for i, line in enumerate(lines):
            # Skip horizontal lines
            if line.startswith("+--"):
                continue
                
            # Draw header
            if "| Draw" in line and "Col" not in line:
                match = re.search(r'\| (Draw\d+)', line)
                if match:
                    current_draw = match.group(1)
                    html_rows.append(f"<tr><th colspan='100'>{current_draw}</th></tr>")
                    continue
            
            # Column header
            if "| Draw   |" in line:
                parts = line.split("|")
                html_row = "<tr>"
                for part in parts:
                    if part.strip():
                        html_row += f"<th>{part.strip()}</th>"
                html_row += "</tr>"
                html_rows.append(html_row)
                in_table = True
                continue
            
            # Data rows
            if in_table and line.startswith("|"):
                parts = line.split("|")
                
                # Skip empty rows
                if len(parts) <= 2:
                    continue
                    
                # Get row type
                row_type = parts[1].strip() if len(parts) > 1 else ""
                
                if row_type in ["R2", "R4", "R6", "R8"]:
                    html_row = "<tr>"
                    
                    # Add row type
                    html_row += f"<td class='{row_type}'>{row_type}</td>"
                    
                    # Add each cell
                    for j in range(2, len(parts)):
                        cell_content = parts[j].strip()
                        cell_class = row_type
                        
                        # Find which column this is
                        col_num = None
                        for num, idx in col_indices.items():
                            if idx + 1 == j:  # +1 because split creates empty first element
                                col_num = num
                                break
                        
                        # Check if this cell has a stable pattern
                        if current_draw and col_num:
                            location = f"{section_name}:{set_name}:{current_draw}:Column{col_num}"
                            
                            if location in stable_patterns:
                                patterns_here = stable_patterns[location]
                                
                                # Check if any patterns apply to this row
                                highlighted_content = cell_content
                                has_pattern = False
                                
                                for pattern_info in patterns_here:
                                    pattern = pattern_info["pattern"]
                                    if row_type in pattern_info["rows"] and pattern in cell_content:
                                        # Highlight this pattern
                                        highlighted_content = highlighted_content.replace(
                                            pattern, 
                                            f"<span class='highlight'>{pattern}</span>"
                                        )
                                        has_pattern = True
                                
                                if has_pattern:
                                    cell_content = highlighted_content
                                    cell_class += " has-pattern"
                        
                        # Add the cell
                        html_row += f"<td class='{cell_class}'>{cell_content}</td>"
                    
                    html_row += "</tr>"
                    html_rows.append(html_row)
        
        # Create final HTML
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
        
    except Exception as e:
        return f"<p>Error generating HTML table: {str(e)}</p>"

# Main app logic
with st.sidebar:
    st.header("Input Data")
    
    # Find available JSON files
    json_files = []
    ai_exports_dir = os.path.join('data', 'ai_exports')
    if os.path.exists(ai_exports_dir):
        json_files = [f for f in os.listdir(ai_exports_dir) if f.endswith('.json')]
    
    if json_files:
        selected_file = st.selectbox(
            "Choose a lottery data file",
            json_files,
            index=0
        )
        file_path = os.path.join(ai_exports_dir, selected_file)
    else:
        st.warning("No JSON files found in data/ai_exports directory")
        file_path = None
    
    # Parameters for stable pattern detection
    st.header("Pattern Detection Parameters")
    
    min_cluster_size = st.slider(
        "Minimum Cluster Size", 
        min_value=2, 
        max_value=4, 
        value=2,
        help="Minimum number of rows (R2/R4/R6/R8) a pattern must appear in"
    )
    
    min_pattern_length = st.slider(
        "Minimum Pattern Length", 
        min_value=3, 
        max_value=6, 
        value=3,
        help="Minimum number of digits in a pattern"
    )
    
    # Run button
    run_analysis = st.button("Run Pattern Analysis")

# Main content area
if file_path and run_analysis:
    try:
        # Load data
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        state_name = data.get("state_name", "Unknown State")
        st.subheader(f"Analyzing stable patterns for {state_name}")
        
        # Find all stable patterns
        with st.spinner("Detecting stable patterns..."):
            stable_patterns = find_stable_patterns(
                data, 
                min_cluster_size=min_cluster_size,
                min_pattern_length=min_pattern_length
            )
            
            # Count total patterns found
            total_patterns = sum(len(patterns) for patterns in stable_patterns.values())
            
            if total_patterns == 0:
                st.warning("No stable patterns found with current settings. Try adjusting the parameters.")
            else:
                st.success(f"Found {total_patterns} stable patterns across {len(stable_patterns)} locations!")
        
        # Create tabs for Midday, Evening, Combined
        sections = ["Midday", "Evening", "Combined"]
        section_tabs = st.tabs(sections)
        
        for i, section_name in enumerate(sections):
            with section_tabs[i]:
                # Check if this section exists
                if section_name not in data.get("sections", {}):
                    st.info(f"No data found for {section_name} section")
                    continue
                
                # Create tabs for sets
                sets = ["Set1", "Set2", "Set3"]
                sets_tabs = st.tabs(sets)
                
                for j, set_name in enumerate(sets):
                    with sets_tabs[j]:
                        if set_name not in data["sections"][section_name].get("sets", {}):
                            st.info(f"No data found for {set_name}")
                            continue
                        
                        # Generate HTML table with patterns highlighted
                        html_table = generate_html_table(data, section_name, set_name, stable_patterns)
                        
                        # Display the table
                        st.markdown(html_table, unsafe_allow_html=True)
                        
                        # Show pattern details for this section/set
                        section_patterns = {
                            loc: pats for loc, pats in stable_patterns.items() 
                            if loc.startswith(f"{section_name}:{set_name}:")
                        }
                        
                        if section_patterns:
                            with st.expander(f"Pattern Details for {section_name}:{set_name}"):
                                for location, patterns in section_patterns.items():
                                    st.markdown(f"**{location}**")
                                    
                                    # Create a list for display
                                    pattern_list = []
                                    for pattern_info in patterns:
                                        pattern_list.append({
                                            "Pattern": pattern_info["pattern"],
                                            "Rows": ", ".join(pattern_info["rows"]),
                                            "Row Count": pattern_info["row_count"],
                                            "In Hot Zone": "Yes" if pattern_info["is_hot_zone"] else "No"
                                        })
                                    
                                    # Display as a table
                                    st.table(pattern_list)
                        else:
                            st.info(f"No stable patterns found in {section_name}:{set_name}")
                    
    except Exception as e:
        st.error(f"Error: {str(e)}")
        
else:
    if not file_path:
        st.info("Please select a lottery data file from the sidebar")
    elif not run_analysis:
        st.info("Click 'Run Pattern Analysis' to detect and highlight stable patterns")
    
    # Display explanation
    with st.expander("What are Stable Patterns?"):
        st.markdown("""
        ### Stable Patterns in Lottery Data
        
        **Stable patterns** are sequences of digits that appear in multiple rows (R2/R4/R6/R8) within the same column.
        These patterns may have special significance for lottery prediction.
        
        ### How this tool works:
        
        1. The tool automatically scans the entire lottery data table
        2. It identifies sequences of digits that appear in multiple rows of the same column
        3. These stable patterns are highlighted in green in the tables
        
        ### Reading the highlighted tables:
        
        - **Green background**: Cells containing stable patterns
        - **Bright green**: The specific stable pattern within the cell
        - **Multiple rows**: A pattern that appears in 2 or more of R2/R4/R6/R8 is considered "stable"
        
        The more rows a pattern appears in, the more stable it is considered. Patterns in "hot zones" 
        may be especially important.
        """)

# Add version and debug info at the bottom
st.sidebar.markdown("---")
st.sidebar.caption("Simple Pattern Highlighter v1.0") 