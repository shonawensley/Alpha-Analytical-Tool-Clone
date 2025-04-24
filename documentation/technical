# V-TRAC Analyzer Documentation

## System Overview

The V-TRAC Analyzer is an advanced pattern recognition tool integrated into the Lottery Data Processor application. It identifies and ranks stable pattern clusters in lottery data across different states. The analyzer evaluates all 35 V-TRAC indices to determine which have the strongest pattern clustering properties within the lottery data tables.

## Data Flow Architecture

```
[Excel Data] → [Cleaning] → [Extraction] → [Table Generation] → [V-TRAC Analysis]
```

The system follows a sequential workflow:
1. Raw lottery data is loaded from Excel files
2. Data is cleaned and standardized 
3. Draw sets are extracted from cleaned data
4. Structured tables are generated (Midday, Evening, Combined)
5. V-TRAC pattern analysis is performed on the tables

## Core Components

### 1. Main Application (`streamlit_app_with_analyzer.py`)
- Provides a Streamlit web interface with four tabs:
  - Process Data: Clean and extract lottery data from Excel
  - View Results: Display generated tables
  - V-TRAC Analyzer: Analyze and rank pattern clusters
  - About: Information about the tool

### 2. Data Processing Pipeline
- `clean_data.py`: Standardizes raw Excel data
- `extract_data.py`: Extracts draw sets and R2/R4/R6/R8 transforms
- `table_generator.py`: Creates combined and R2-only tables

### 3. V-TRAC Analysis Engine
- `vtrac_utils.py`: Contains the V-TRAC reference table and pattern matching functions
- `vtrac_analyzer_tab()`: The main integration point for V-TRAC analysis in the Streamlit app

## Key Functions and Their Purpose

### Data Loading Functions
- `get_combined_table(state, time_of_day)`: Loads the most recent combined table for a state/time period
- `get_r2_table(state, time_of_day)`: Loads the most recent R2-only table for a state/time period

### Pattern Analysis Functions
- `get_patterns_for_index(index)`: Retrieves all patterns associated with a specific V-TRAC index
- `count_patterns_in_table(df, patterns)`: Counts occurrences of each pattern in a table
- `analyze_pattern_persistence(df, patterns)`: Measures how patterns persist across different sets/draws
- `analyze_pattern_stability(df, patterns)`: Measures how stable patterns are within the same set/draw
- `detect_straight_combinations(df, pattern)`: Detects when patterns appear in the exact same position

### Scoring and Reporting Functions
- `calculate_index_score(df, patterns)`: Calculates an overall score for a V-TRAC index
- `generate_index_html_report(state_name, index, patterns, tables, score, rank)`: Creates an HTML report with pattern highlighting

## V-TRAC Analysis Logic

### 1. Index Evaluation Process
The system evaluates all 35 V-TRAC indices independently:
1. Retrieves all patterns (Singles and Doubles) associated with each index
2. Counts pattern occurrences across all tables
3. Filters out patterns below a minimum threshold
4. Calculates a score based on pattern occurrence count
5. Ranks indices by their score (higher is better)

### 2. Scoring System
The core scoring is based on pattern occurrence frequency:
- Each pattern occurrence adds to the index score
- Higher frequency patterns contribute more to the final score
- Only patterns that meet the minimum threshold are considered

Additional metrics (calculated but not used for ranking):
- Pattern persistence (appearance across different sets/draws)
- Pattern stability (consistent appearance within the same set/draw)
- Straight combinations (patterns appearing in the exact same position)

### 3. HTML Report Generation
For each analyzed index, the system generates an HTML report that:
1. Displays the tables side-by-side (Midday, Evening, Combined)
2. Highlights the patterns within the data
3. Provides detailed statistics on pattern occurrences
4. Ranks the index based on its score

## Integration with Main Process

The V-TRAC Analyzer seamlessly integrates with the main lottery data processing workflow:

1. **Data Preparation**:
   - The main data processing pipeline generates cleaned data and tables
   - Tables are stored in date-stamped folders under `data/outputs/tables/[DATE]/[STATE]/`

2. **Analysis Triggering**:
   - Analysis can be triggered through the "V-TRAC Analyzer" tab in the Streamlit app
   - Users can analyze a single state or multiple states simultaneously

3. **Report Storage**:
   - Generated HTML reports are saved to `data/outputs/vtrac/[TIMESTAMP]_[STATE]_Index[N].html`
   - Reports can be viewed directly in the app or opened in a browser

## Implementation Details

### File Structure
```
scripts/
├── streamlit_app_with_analyzer.py  # Main application
├── utils/
│   ├── clean_data.py               # Data cleaning utilities
│   ├── extract_data.py             # Data extraction utilities
│   ├── table_generator.py          # Table generation utilities
│   ├── vtrac_utils.py              # V-TRAC utilities and reference table
│   └── path_handler.py             # File path management
data/
├── original/                       # Raw Excel data
├── cleaned/                        # Cleaned data
└── outputs/
    ├── tables/                     # Generated tables
    └── vtrac/                      # V-TRAC analysis reports
```

### BOXED_VTRAC_REFERENCE Structure
The V-TRAC reference table contains 35 indices, each with:
- Index number (1-35)
- Singles: Patterns that occur once in the permutation groups
- Doubles: Patterns that occur twice in the permutation groups

Each pattern is a 3-digit string, representing a specific number combination that might appear in lottery data.

### HTML Report Structure
The HTML reports are structured with:
1. A horizontal layout showing Midday, Evening, and Combined tables side by side
2. Pattern highlighting in the tables (purple for matching patterns)
3. V-TRAC information and ranking
4. Detailed statistics section with:
   - Pattern occurrence counts
   - Pattern persistence scores
   - Pattern stability scores
   - Straight combination occurrences

## Running the Application

1. Ensure Excel data is in `data/original/Pick3StatsC4.xlsm`
2. Launch the application: `streamlit run scripts/streamlit_app_with_analyzer.py`
3. Process data in the "Process Data" tab if not already done
4. Navigate to the "V-TRAC Analyzer" tab
5. Select analysis mode (Single State or All States)
6. Set minimum pattern count threshold
7. Click "Run V-TRAC Analysis"
8. View ranked results and HTML reports

## Technical Notes

- The analyzer calculates pattern occurrences by checking each cell in the tables
- Only patterns that meet the minimum threshold are considered for scoring
- The HTML reports use inline CSS styling for pattern highlighting
- The Streamlit interface is fully responsive and adapts to different screen sizes

This documentation provides a comprehensive overview of how the V-TRAC Analyzer works and integrates with the main lottery data processing system. 