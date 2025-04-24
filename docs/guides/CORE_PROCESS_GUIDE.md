# Alpha Analytical Tool - Core Process Guide

This document explains the working data flow and process that all tools should build upon.

## Core Data Processing Flow

```
Excel Data → Cleaning → Extract Sets → Generate Tables → Analysis
```

### 1. Data Input

- Source: `Pick3StatsC4.xlsm` Excel file in `data/original`
- Contains raw lottery data for multiple states

### 2. Data Cleaning 

- Executed by: `clean_all_states()` function in `utils/clean_data.py`
- Output: Cleaned CSV files in `data/cleaned/{STATE_NAME}.csv`
- Normalizes data formats, fixes inconsistencies

### 3. Data Extraction

- Executed by: `extract_all_states()` function in `utils/extract_data.py`
- Extracts sets and draws from the cleaned data
- Prepares structured data for table generation

### 4. Table Generation

- Executed by: `generate_tables()` function in `utils/table_generator.py` 
- Creates 6 tables per state:
  - Midday_combined.csv
  - Evening_combined.csv
  - Combined_combined.csv
  - Midday_R2_only.csv
  - Evening_R2_only.csv
  - Combined_R2_only.csv
- Output: Tables in `data/outputs/tables/{DATE}/{STATE}`

### 5. Analysis Tools

The following analysis tools all build on the generated tables:

1. **V-TRAC Analyzer**
   - Script: `enhanced_analyzer_final.py`
   - Launcher: `run_enhanced_analyzer_final.bat`
   - Analyzes V-TRAC patterns in the Combined Tables
   - Generates HTML reports with pattern highlighting
   
2. **Integrated App with Analyzer**
   - Script: `streamlit_app_with_analyzer.py`
   - Launcher: `run_with_analyzer.bat`
   - Combines data processing and V-TRAC analysis
   - Provides a complete end-to-end workflow

## Directory Structure

```
Alpha Analytical Tool/
├── data/                    # Data storage
│   ├── original/            # Original Excel files
│   ├── cleaned/             # Cleaned CSV files
│   └── outputs/             # Generated output
│       ├── tables/          # Generated tables by date
│       └── analysis/        # Analysis reports
├── scripts/
│   ├── core/                # Production-ready scripts
│   │   ├── streamlit_app_with_analyzer.py
│   │   └── enhanced_analyzer_final.py
│   ├── utils/               # Core utility modules
│   │   ├── clean_data.py
│   │   ├── extract_data.py
│   │   ├── table_generator.py
│   │   └── vtrac_utils.py
│   ├── auxiliary/           # Tools for future modules
│   └── archive/             # Obsolete or experimental scripts
├── batch/                   # Batch launchers
│   ├── run_enhanced_analyzer_final.bat
│   └── run_with_analyzer.bat
└── docs/                    # Documentation
    └── guides/              # Detailed guides
        └── CORE_PROCESS_GUIDE.md
```

## Best Practices

When adding new features or tools:

1. Always build upon the existing data flow
2. Use the Combined Tables as your data source
3. Maintain compatibility with the core utilities
4. Add new batch files to the batch directory
5. Document any changes to the core process

By following these guidelines, all new tools will integrate seamlessly with the existing workflow. 