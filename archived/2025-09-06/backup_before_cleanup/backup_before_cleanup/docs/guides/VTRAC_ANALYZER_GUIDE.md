# V-TRAC Analyzer Guide

This document explains how the V-TRAC analyzer works, how to use it, and how to extend it.

## Overview

The V-TRAC analyzer is a specialized pattern analysis tool that:

1. Analyzes lottery data tables for specific patterns
2. Ranks V-TRAC indexes (1-35) based on pattern occurrence
3. Generates detailed HTML reports with pattern highlighting
4. Visualizes pattern distribution and scores

## Two Implementation Options

### 1. Enhanced V-TRAC Analyzer (Standalone)

- **Script**: `enhanced_analyzer_final.py`
- **Launcher**: `run_enhanced_analyzer_final.bat`

This standalone app provides comprehensive V-TRAC pattern analysis with a user-friendly interface:

- Select any state from a dropdown
- Set analysis parameters (number of top indexes, reports to generate)
- Run analysis with a simple button click
- View ranked indexes with scores
- Generate downloadable HTML reports with pattern highlighting
- Visualize top index distribution with a chart

### 2. Integrated App with Analyzer

- **Script**: `streamlit_app_with_analyzer.py`
- **Launcher**: `run_with_analyzer.bat`

This full-featured app combines the entire process:
- Data cleaning
- Table generation
- V-TRAC analysis
- Report viewing

All in a streamlined interface with separate tabs for each function.

## How V-TRAC Analysis Works

1. **Data Loading**: Loads the combined tables for a state
2. **Pattern Collection**: For each V-TRAC index (1-35), collects the associated patterns
3. **Pattern Counting**: Counts pattern occurrences across all tables
4. **Scoring**: Ranks indexes based on pattern occurrence frequency
5. **Report Generation**: Creates HTML reports with highlighted patterns
6. **Visualization**: Charts the distribution of top indexes

## Key Functions

```python
# Load state data
tables = load_state_data(state_name)

# Analyze all indexes
results = analyze_all_indexes(state_name)

# Generate HTML reports
reports = generate_top_reports(state_name, results, top_n_reports)

# Generate score visualization
chart_image = generate_summary_chart(results, top_n_indices)
```

## HTML Report Structure

The generated HTML reports have a consistent structure:

1. **Three-Column Layout**:
   - Midday data (left)
   - Evening data (center)
   - Combined data (right)

2. **Pattern Highlighting**:
   - Patterns in the data are highlighted in purple
   - Clear visual identification of where patterns occur

3. **Statistical Analysis**:
   - Pattern occurrence counts
   - Pattern persistence scores
   - Pattern stability scores
   - Straight combination occurrences

## Extending the Analyzer

When extending the V-TRAC analyzer, maintain these key aspects:

1. Keep the three-column layout for easy data comparison
2. Ensure pattern highlighting uses consistent styling
3. Generate unique download button keys for each report
4. Maintain the detailed statistics sections
5. Preserve the clean, organized HTML structure

## Best Practices

1. Always run the V-TRAC analyzer on properly generated tables
2. Start with the enhanced analyzer for focused pattern analysis
3. Use the integrated app for end-to-end workflow
4. Download HTML reports for detailed offline analysis
5. Focus on the top 3-5 ranked indexes for best results 