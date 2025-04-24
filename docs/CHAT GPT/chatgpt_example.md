# ChatGPT Example: Analyzing Lottery Patterns

This example shows how to use our analysis tools with ChatGPT.

## Step 1: Share Your JSON Data

```
I have today's lottery data for Indiana. Here's the JSON file structure:

{
  "sections": {
    "Combined": {
      "sets": {
        "Set1": {
          "draws": {
            "Draw1": {
              "pattern_variations": {
                "R2": ["99418677", "99418677", "99418677", "99418677", "99418677", "99418677", "99418677"],
                "R4": ["99684771", "99684771", "99684771", "99684771", "99684771", "99684771", "99684771"],
                "R6": ["99684771", "99684771", "99684771", "99684771", "99684771", "99684771", "99684771"],
                "R8": ["99684771", "99684771", "99684771", "99684771", "99684771", "99684771", "99684771"]
              },
              "metadata": {
                "is_hot_zone": true,
                "hot_zone_count": 3,
                "hot_zone_indicators": {
                  "R2": [true, true, false, false, false, false, false],
                  "R4": [true, true, false, false, false, false, false],
                  "R6": [true, false, false, false, false, false, false],
                  "R8": [false, false, false, false, false, false, false]
                }
              }
            }
          }
        }
      }
    }
  }
}
```

## Step 2: Share Analysis Tools

```python
# PatternMapper.py
class PatternMapper:
    def __init__(self, json_data):
        """Initialize with lottery JSON data"""
        self.data = json_data
        self.sections = ["Midday", "Evening", "Combined"]
        self.sets = ["Set3", "Set2", "Set1"]
        self.draws = [f"Draw{i}" for i in range(1, 8)]
        self.row_types = ["R2", "R4", "R6", "R8"]
        
    def get_box(self, section, set_name, draw_name, column):
        """Get all patterns in a specific box (vertical R2/R4/R6/R8 alignment)"""
        # ... rest of code ...
```

```python
# TableFormatter.py (snippet)
class TableFormatter:
    def __init__(self, json_data):
        """Initialize with lottery JSON data"""
        self.data = json_data
        self.mapper = PatternMapper(json_data)
        
    def display_table(self, section, set_name, style="ascii", highlight_pattern=None):
        """Display a formatted table for a section"""
        # ... rest of code ...
```

## Step 3: Ask for Analysis

```
Using the PatternMapper and TableFormatter tools, please:

1. Show me the Combined Set1 data in a table format similar to the Streamlit app
2. Highlight any hot zones with asterisks (*pattern*)
3. Find patterns containing "224" and highlight them with exclamation marks (!pattern!)
4. Find any clusters where the same pattern fragment appears in at least 2 row types in the same column
5. Check for consensus patterns (where R2/R4/R6/R8 have same ending digits)

Please format the output in ASCII tables to make it easy to read.
```

## Example Response from ChatGPT

ChatGPT would analyze your data and respond with:

1. A formatted table showing the Combined Set1 data with hot zones marked
2. Highlighted patterns containing "224" 
3. A table showing pattern clusters
4. Consensus patterns identified

The output might look like:

```
Combined Set1 Table:

+---------+--------+--------+--------+--------+--------+--------+--------+
| Draw    | Col 7  | Col 6  | Col 5  | Col 4  | Col 3  | Col 2  | Col 1  |
+---------+--------+--------+--------+--------+--------+--------+--------+
| Draw1   |        |        |        |        |        |        |        |
| R2      | *994186* | *994186* | 994186 | 994186 | 994186 | 994186 | 994186 |
| R4      | *996847* | *996847* | 996847 | 996847 | 996847 | 996847 | 996847 |
| R6      | *996847* | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 |
| R8      | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 | 996847 |
+---------+--------+--------+--------+--------+--------+--------+--------+
```

## Follow-up Questions

After reviewing the initial analysis, you can ask follow-up questions:

```
Thanks! Now can you:

1. Show me only Draw1 and Draw2 from the Midday section
2. Check if there are any patterns that appear in both Midday and Evening sections
3. Track the pattern "847" across all positions
```

## Using for Daily Analysis

When you get new data each day:

1. Export JSON data using the Streamlit app
2. Share with ChatGPT along with the tools
3. Ask for specific analyses based on what you're looking for
4. Have ChatGPT compare with previous days' patterns (if you've shared those)
5. Look for hot zones and consensus patterns that might indicate winning numbers

The beauty of this approach is that ChatGPT can quickly analyze complex patterns and present them in a readable format, helping you identify potential winning numbers more efficiently. 