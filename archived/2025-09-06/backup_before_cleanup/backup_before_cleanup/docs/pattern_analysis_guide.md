# Lottery Pattern Analysis Guide

## Daily Analysis Process

### Purpose
This system is used to analyze daily lottery data and predict next day's draws by:
1. Processing new daily data files
2. Analyzing patterns across Midday/Evening/Combined tables
3. Identifying hot zones and consensus patterns
4. Using historical data (Set3/Set2) to predict Set1 patterns

### Daily Workflow
1. **Data Update**
   - New daily data file is uploaded
   - Data is processed into structured JSON format
   - Contains all sections (Midday/Evening/Combined)

2. **Analysis Process**
   - Start with Combined table for overall patterns
   - Compare with Midday/Evening for specific insights
   - Use Set3/Set2 historical data to validate patterns
   - Focus on Set1 for current day predictions

3. **Pattern Prediction**
   - Identify hot zones in current data
   - Look for consensus patterns across R2/R4/R6/R8
   - Track pattern progression across columns
   - Use V-TRAC relationships for validation

4. **Key Concepts**
   - Hot zones indicate high-probability patterns
   - Consensus patterns (same ending digits) are significant
   - Pattern progression shows digit elimination
   - V-TRAC relationships connect related patterns

## Quick Start Guide for AI Analysis

### 1. Initial Setup
```python
# Load the data and create mapper
import json
from pattern_mapper import PatternMapper

with open("your_state_data.json", "r") as f:
    json_data = json.load(f)
mapper = PatternMapper(json_data)
```

### 2. Common Analysis Tasks

#### Find Hot Zones
```python
# Get all hot zones in Combined Set1
hot_zones = mapper.get_hot_zones("Combined", "Set1")
```

#### Check for Consensus
```python
# Look for consensus in hot zones
for draw in range(1, 8):
    for col in range(1, 8):
        consensus = mapper.check_consensus("Combined", "Set1", f"Draw{draw}", col)
        if consensus:
            print(f"Found consensus: {consensus}")
```

#### Track Pattern Progression
```python
# Track a specific pattern across columns
occurrences = mapper.track_pattern("224", "Combined", "Set1")
```

### 3. Analysis Strategy
1. Start with Combined table for overall patterns
2. Check hot zones in Set1 for current predictions
3. Use Set3/Set2 to validate pattern stability
4. Look for consensus patterns in hot zones
5. Track pattern progression across columns

### 4. Key Indicators
- Hot zones (*) indicate high-probability patterns
- Consensus patterns (same ending digits) are significant
- Pattern progression shows digit elimination
- V-TRAC relationships connect related patterns

## Table Structure Overview

### 1. Basic Navigation
```
Location Format: {section}:{set}:{draw}:{column}:{row_type}
Example: Midday:Set1:Draw1:Column2:R2

Sections: Midday, Evening, Combined
Sets: Set3, Set2, Set1
Draws: Draw1-Draw7
Columns: 7→1 (right to left)
Row Types: R2, R4, R6, R8
```

### 2. Box Structure
Each "box" is defined by its vertical alignment:
```
R2: Top row     (2000x pool)
R4: Second row  (4000x pool)
R6: Third row   (6000x pool)
R8: Bottom row  (8000x pool)
```

### 3. Pattern Indicators
```
*  = Hot zone item
** = Super hot zone item
Empty = Regular item
```

## Pattern Location Mapping

### 1. Vertical Box Analysis
To analyze a specific box, use:
```
{section}:{set}:{draw}:{column}
Example: "Midday:Set1:Draw1:Column2" gives you:
R2: 99418677
R4: 99684771
R6: 68177994
R8: 77199864
```

### 2. Hot Zone Distribution
```
Draw1: Last 5 items (last 3 super hot)
Draw2: Last 4 items (last 2 super hot)
Draw3: Last 3 items (last 2 super hot)
Draw4: Last 2 items (both super hot)
Draw5: Last 2 items (both super hot)
```

### 3. Pattern Progression
```
Set1 Draw1: 7 columns (full pattern)
Set1 Draw2: 6 columns
Set1 Draw3: 5 columns
Set1 Draw4: 4 columns
Set1 Draw5: 3 columns
Set1 Draw6: 2 columns
Set1 Draw7: 1 column
```

## Pattern Analysis Methods

### 1. Vertical Analysis
- Compare patterns within a single box (R2/R4/R6/R8)
- Look for matching digits or sequences
- Check for consensus (same ending digits across all rows)

### 2. Horizontal Analysis
- Track pattern changes across columns (7→1)
- Monitor digit elimination patterns
- Identify persistent digits/sequences

### 3. Cross-Section Analysis
- Compare patterns across sections (Midday/Evening/Combined)
- Look for pattern persistence across sets (Set3→Set2→Set1)
- Identify V-TRAC relationships

## Pattern Types

### 1. Three-Digit Patterns
```
Unique: Three different digits (567, 123, 471)
- Straight order: 613, 613, 613
- Box order: 613, 361, 136
- Extended: 316 → 331116

Doubles: Two unique digits (244, 566, 133)
```

### 2. V-TRAC Patterns
```
Definition: Related stable patterns in strings
Example: 590 = 045 = 54455 (same V-TRAC)
Straight: Patterns in same order (781 and 286)
```

## API for Pattern Location

### 1. Location Format
```python
location = {
    "section": "Midday|Evening|Combined",
    "set": "Set1|Set2|Set3",
    "draw": "Draw1|Draw2|Draw3|Draw4|Draw5|Draw6|Draw7",
    "column": "1|2|3|4|5|6|7",
    "row_type": "R2|R4|R6|R8"
}
```

### 2. Pattern Query Format
```python
pattern_query = {
    "location": location,
    "analysis_type": "vertical|horizontal|cross_section",
    "pattern_type": "three_digit|vtrac|consensus",
    "hot_zone_only": boolean
}
```

## Example Usage

### 1. Querying a Specific Box
```python
query = {
    "location": {
        "section": "Midday",
        "set": "Set1",
        "draw": "Draw1",
        "column": "2",
        "row_type": "ALL"  # Gets all R2/R4/R6/R8
    }
}
```

### 2. Analyzing Hot Zones
```python
hot_zone_query = {
    "location": {
        "section": "Midday",
        "set": "Set1",
        "draw": "Draw1"
    },
    "hot_zone_only": true
}
```

### 3. Pattern Tracking
```python
tracking_query = {
    "location": {
        "section": "Midday",
        "set": "Set1"
    },
    "analysis_type": "horizontal",
    "pattern": "224"  # Track this pattern across columns
}
``` 