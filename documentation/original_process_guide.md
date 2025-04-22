# Complete Lottery Data Processing Pipeline

## Overview

This documentation covers the complete process of transforming raw Excel files into formatted state tables, including data cleaning, extraction, and visualization.

## 1. Project Structure

```
python
new_test_lottery/
├── data/
│   ├── original/ # Raw Excel files
│   │   └── Pick3StatsC4.xlsm
│   └── cleaned/ # Cleaned state files
│       ├── Connecticut4_cleaned.xlsx
│       ├── Delaware4_cleaned.xlsx
│       └── ... (17 state files)
├── scripts/
│   ├── utils/
│   │   ├── clean_all_states.py
│   │   ├── extract_datasets_5.py
│   │   ├── final_simplified.py
│   │   ├── print_highlighted_states.py
│   │   └── streamlit_viewer.py
│   └── run_clean_and_view.sh
└── docs/
    └── COMPLETE_PROCESS_DOCUMENTATION.md
```

## 2. Process Flow

### Step 1: Data Cleaning
- Script: `clean_all_states.py`
- Purpose: Clean raw Excel data for all 17 states
- Process:
  1. Reads Pick3StatsC4.xlsm
  2. Processes each state sheet
  3. Removes unnecessary columns
  4. Normalizes data formats
  5. Saves individual cleaned files

### Step 2: Data Extraction
- Script: `extract_datasets_5.py`
- Purpose: Extract structured data from cleaned files
- Process:
  1. Reads cleaned state Excel files
  2. Extracts sections (Midday/Evening/Combined)
  3. Processes sets (Set1/Set2/Set3)
  4. Extracts row types (DRAW_DATA, R2, R4, R6, R8)

### Step 3: Table Generation
- Script: `final_simplified.py`
- Purpose: Generate formatted tables
- Output:
  1. Combined Tables (all data)
  2. R2-only Tables (with custom slicing)
- Features:
  - Left-aligned data
  - Custom R2 slicing rules
  - Proper row ordering

### Step 4: Visualization
- Script: `streamlit_viewer.py`
- Purpose: Interactive table viewing
- Features:
  - State selection
  - Table type selection
  - Pattern highlighting

## 3. Essential Code Files

### clean_all_states.py
```python
#!/usr/bin/env python
"""
Clean and normalize data for all state sheets from Pick3StatsC4.xlsm
"""
[Code content...]
```

### extract_datasets_5.py
```python
#!/usr/bin/env python
"""
Extract structured datasets from cleaned Excel files
"""
[Code content...]
```

## Running the Process

1. Place the raw Excel file (Pick3StatsC4.xlsm) in the data/original directory
2. Run the cleaning script to generate cleaned state files
3. Run the extraction script to process the cleaned data
4. Generate formatted tables using the final script
5. View results through the Streamlit interface

## Data Flow

```
Raw Excel ──▶ Cleaned Files ──▶ Extracted Sets ──▶ Formatted Tables
(original)     (by state)       (with row types)   (combined & R2)
```

## Important Notes

1. All scripts assume the correct directory structure
2. Files must be processed in order (clean → extract → generate)
3. Each step depends on the successful completion of previous steps
4. The Streamlit viewer provides an easy way to verify results

This documentation serves as a reference for the original working process and can be used alongside the newer V-TRAC enhanced system. 