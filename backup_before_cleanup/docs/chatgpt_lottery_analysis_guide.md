# ChatGPT Lottery Analysis Guide

## Table of Contents
1. [Quick Start](#quick-start)
2. [Data Format](#data-format)
3. [Essential Tools](#essential-tools)
4. [Analysis Examples](#analysis-examples)
5. [Data Visualization](#data-visualization)

## Quick Start

### Step 1: Share Your JSON Data
```
"Here's my lottery data for analysis:
File: [State]4_ai_format_[DATE].json

Here's a small sample of the structure:
{
  "sections": {
    "Combined": {
      "sets": {
        "Set1": {
          "draws": {
            "Draw1": {
              "pattern_variations": {
                "R2": ["99418677", ...],
                ...
              }
            }
          }
        }
      }
    }
  }
}
```

### Step 2: Share Analysis Tools
Share the `pattern_mapper.py` code

### Step 3: Ask for Analysis
```
"Please analyze this data to:
1. Find hot zones in Combined Set1
2. Check for consensus patterns
3. Identify pattern clusters
4. Display the results in a tabular format"
```

## Data Format

Your lottery data is structured as JSON with:
- Sections: Midday, Evening, Combined
- Sets: Set1, Set2, Set3
- Draws: Draw1 through Draw7
- Pattern Types: R2, R4, R6, R8

### Column Structure
- Draw1: 7 columns
- Draw2: 6 columns
- Draw3: 5 columns
- Draw4: 4 columns
- Draw5: 3 columns
- Draw6: 2 columns
- Draw7: 1 column

### Box Structure
Each "box" is a vertical alignment of R2/R4/R6/R8 patterns at a specific draw and column position.

## Essential Tools

### 1. PatternMapper Class
The `pattern_mapper.py` file contains a class that helps navigate and analyze patterns:

```python
# Core functions:
mapper = PatternMapper(json_data)
box = mapper.get_box("Combined", "Set1", "Draw1", 2)
hot_zones = mapper.get_hot_zones("Combined", "Set1")
consensus = mapper.check_consensus("Combined", "Set1", "Draw1", 1)
occurrences = mapper.track_pattern("224", "Combined", "Set1")
```

### 2. Pattern Analysis Guide
The `pattern_analysis_guide.md` explains the table structure, pattern relationships, and analysis strategies.

### 3. TableFormatter Class
For visualizing data in a format similar to Streamlit:

```python
class TableFormatter:
    def __init__(self, json_data):
        self.data = json_data
        self.mapper = PatternMapper(json_data)
        
    def display_table(self, section, style="ascii"):
        """Display a formatted table for a section"""
        # Implementation details in the formatter.py file
        
    def highlight_hot_zones(self, table_data):
        """Add highlighting to hot zones"""
        # Implementation details in the formatter.py file
        
    def highlight_patterns(self, table_data, pattern_to_highlight):
        """Highlight specific patterns in the table"""
        # Implementation details in the formatter.py file
```

## Analysis Examples

### Example 1: Find Hot Zones
```python
mapper = PatternMapper(json_data)
hot_zones = mapper.get_hot_zones("Combined", "Set1")
print("Hot Zones Found:")
for location, data in hot_zones.items():
    print(f"Location: {location}")
    print(f"Hot Zone Count: {data['hot_zone_count']}")
    print("Patterns:")
    for row_type, patterns in data['patterns'].items():
        print(f"  {row_type}: {patterns}")
```

### Example 2: Check for Consensus
```python
consensus_patterns = []
for draw in range(1, 8):
    for col in range(1, 8 - draw + 1):  # Respect staircase structure
        consensus = mapper.check_consensus("Combined", "Set1", f"Draw{draw}", col)
        if consensus:
            consensus_patterns.append(consensus)

print(f"Found {len(consensus_patterns)} consensus patterns")
for c in consensus_patterns:
    print(f"Consensus {c['consensus']} at {c['location']}")
```

### Example 3: Track Patterns
```python
# Track a pattern like "224" across all positions
pattern = "224"
occurrences = mapper.track_pattern(pattern, "Combined", "Set1")
print(f"Pattern '{pattern}' found in {len(occurrences)} locations")
```

## Data Visualization

### ASCII Table Format
```
+---------+--------+--------+--------+--------+--------+--------+--------+
| Draw    | Col 7  | Col 6  | Col 5  | Col 4  | Col 3  | Col 2  | Col 1  |
+---------+--------+--------+--------+--------+--------+--------+--------+
| Draw1   |        |        |        |        |        |        |        |
| R2      | 994186 | 994186 | 994186 | 994186 | 994186 | 994186 | 994186 |
| R4      | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 |
| R6      | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 |
| R8      | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 |
+---------+--------+--------+--------+--------+--------+--------+--------+
| Draw2   |        |        |        |        |        |        |        |
| R2      | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 |        |
| R4      | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 |        |
| R6      | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 |        |
| R8      | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 |        |
+---------+--------+--------+--------+--------+--------+--------+--------+
```

### Asking for Visual Output
When working with ChatGPT, ask:
```
"Please display the Combined Set1 table with hot zones highlighted using ASCII formatting. 
Indicate hot zones with [*] and highlight any patterns containing '224'."
```

### Example Implementation
```python
def format_table_for_chatgpt(section="Combined", set_name="Set1"):
    # Create headers
    header = "| Draw | Col 7 | Col 6 | Col 5 | Col 4 | Col 3 | Col 2 | Col 1 |"
    separator = "|------|------|------|------|------|------|------|------|"
    
    rows = [header, separator]
    
    # For each draw (1-7)
    for draw_num in range(1, 8):
        draw_name = f"Draw{draw_num}"
        
        # Draw header
        rows.append(f"| {draw_name} | | | | | | | |")
        
        # For each row type (R2, R4, R6, R8)
        for row_type in ["R2", "R4", "R6", "R8"]:
            # Get patterns for this draw
            patterns = mapper.get_draw_patterns(section, set_name, draw_name, row_type)
            
            # Format row with proper column count
            cols = []
            for i in range(7):
                if i < len(patterns):
                    # Show first 6 chars of pattern
                    p = patterns[i][:6]
                    # Mark hot zones
                    is_hot = mapper.is_hot_zone(section, set_name, draw_name, 7-i)
                    if is_hot:
                        p = f"*{p}*"
                    cols.append(p)
                else:
                    cols.append("")
            
            # Add to table
            row = f"| {row_type} | {' | '.join(cols)} |"
            rows.append(row)
    
    return "\n".join(rows)
```

## Daily Workflow with ChatGPT

1. Export your state data to JSON using the Streamlit app
2. Share the JSON data with ChatGPT
3. Share the pattern_mapper.py code
4. Ask for specific analyses:
   - "Find hot zones and display them in a table"
   - "Check for consensus patterns in hot zones"
   - "Track pattern X across all positions"
5. Ask for visual outputs to help understand the data

### Example Session
```
User: "I have today's lottery data for Indiana. Here's the JSON file and the PatternMapper class. Please analyze the Combined Set1 data, identify hot zones, and display the results in a table format that resembles the Streamlit view."

ChatGPT: [Analyzes data and displays table with hot zones highlighted]

User: "Can you highlight any consensus patterns in the table? Also track pattern '224' across all positions."

ChatGPT: [Updates table with consensus patterns and shows tracking results]
``` 