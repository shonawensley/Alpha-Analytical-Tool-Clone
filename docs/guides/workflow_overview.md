# Alpha Analytical Tool: Complete Workflow Guide

## Overview

The Alpha Analytical Tool is a powerful data processing and pattern analysis system that transforms raw data into actionable insights. This document explains the entire workflow from start to finish, showing how all components work together.

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  1. DATA    │     │  2. DATA    │     │  3. TABLE   │     │  4. PATTERN │
│  IMPORT     │────▶│  PROCESSING │────▶│  GENERATION │────▶│  ANALYSIS   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

## The Complete Process

### 1. Data Import

**Input**: Excel file (`Pick3StatsC4.xlsm`)
- Place this file in the `data/original/` directory
- Contains raw data for multiple states

### 2. Data Processing

**Step 1: Data Cleaning**
- Raw data is standardized and formatted
- Each state's data is processed separately
- Output: `data/cleaned/[STATE]_cleaned.xlsx`

**Step 2: Set Extraction**
- System extracts draw sets from cleaned data
- Processes sets into different timeframes (Midday, Evening, Combined)
- Handles R2/R4/R6/R8 transformations
- Creates raw data structure for table generation

### 3. Table Generation

- Formatted tables are created for analysis
- Six table types are generated for each state:
  - Midday Combined
  - Evening Combined
  - Combined Combined
  - Midday R2-only
  - Evening R2-only
  - Combined R2-only
- Tables are stored in date-stamped directories: `data/outputs/tables/[DATE]/[STATE]/`

### 4. Pattern Analysis

**V-TRAC Analysis**
- Tables are analyzed for patterns from all 35 V-TRAC indices
- Patterns are scored based on occurrence frequency
- Additional metrics are calculated:
  - Pattern persistence (across different sets/draws)
  - Pattern stability (consecutive appearances)
  - Straight combinations (exact position matches)
- HTML reports are generated with pattern highlighting
- Reports are stored in: `data/outputs/vtrac/`

## User Interface

The application provides four main functions, all accessible through the Streamlit interface:

### 1. Process Data Tab

- **Purpose**: Run the data pipeline from start to finish
- **Options**:
  - Clean Data
  - Extract Data
  - Generate Tables
- **State Selection**: Process all states or select specific ones
- **Output**: Processed data and tables ready for analysis

### 2. View Results Tab

- **Purpose**: Examine generated tables
- **Features**:
  - Select by date, state, and table type
  - View color-coded tables
  - Download tables as CSV files

### 3. V-TRAC Analyzer Tab

- **Purpose**: Perform pattern analysis across tables
- **Features**:
  - Single state or multi-state analysis
  - Pattern threshold adjustment
  - Ranking of V-TRAC indices by pattern occurrence
  - Interactive HTML reports with pattern highlighting

### 4. About Tab

- **Purpose**: Information about the tool
- **Content**: Overview of features and capabilities

## Running the Application

Two batch files are provided for easy access:

1. **Alpha_Tool.bat** - Runs the standard application
2. **V-TRAC_Analyzer.bat** - Opens directly to the V-TRAC Analyzer tab

## Processing Workflow Example

Here's an example of a complete workflow:

1. **Data Preparation**:
   - Place `Pick3StatsC4.xlsm` in the `data/original/` folder

2. **Initial Processing**:
   - Run `Alpha_Tool.bat`
   - Select "Process Data" tab
   - Ensure all three options are checked (Clean, Extract, Generate)
   - Click "Process Data"
   - Wait for processing to complete

3. **Data Exploration**:
   - Switch to "View Results" tab
   - Select state and table type
   - Examine raw data tables

4. **Pattern Analysis**:
   - Switch to "V-TRAC Analyzer" tab (or run `V-TRAC_Analyzer.bat`)
   - Select states to analyze
   - Set pattern threshold (typically 3)
   - Click "Run V-TRAC Analysis"
   - Review top-ranked indices
   - Examine HTML reports with highlighted patterns

5. **Using Analysis Results**:
   - Open HTML reports in browser for detailed viewing
   - Download reports for further reference
   - Identify strongest pattern clusters

## Relationship to Original Process

The V-TRAC Analyzer builds upon the standard processing pipeline:

```
┌─────────────────────────────────────────────────┐
│              ORIGINAL PROCESS                   │
│                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │  CLEAN   │───▶│  EXTRACT │───▶│ GENERATE │  │
│  │  DATA    │    │  DATA    │    │  TABLES  │  │
│  └──────────┘    └──────────┘    └──────────┘  │
└───────────────────────┬─────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────┐
│              V-TRAC ENHANCEMENT                 │
│                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │ PATTERN  │───▶│  INDEX   │───▶│  HTML    │  │
│  │ ANALYSIS │    │ SCORING  │    │ REPORTS  │  │
│  └──────────┘    └──────────┘    └──────────┘  │
└─────────────────────────────────────────────────┘
```

The V-TRAC Analyzer integrates seamlessly with the original process:
- It uses the same data paths and table structures
- It can be run independently or as part of the full workflow
- It provides enhanced analytical capabilities without disrupting the core process

## Data Management

- Raw Excel: `data/original/`
- Cleaned Data: `data/cleaned/`
- Generated Tables: `data/outputs/tables/[DATE]/[STATE]/`
- V-TRAC Reports: `data/outputs/vtrac/`

## Technical Details

For more detailed technical information, please refer to:
- `documentation/vtrac_analyzer_guide.md` - Technical reference
- `documentation/vtrac_quickstart.md` - Quick start guide 