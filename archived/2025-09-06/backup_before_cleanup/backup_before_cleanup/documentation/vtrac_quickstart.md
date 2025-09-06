# V-TRAC Analyzer Quick-Start Guide

## What is the V-TRAC Analyzer?

The V-TRAC Analyzer is a specialized tool that identifies stable pattern clusters in lottery data. It works by analyzing data tables for recurring 3-digit patterns and ranking the V-TRAC indices based on pattern occurrence frequency.

## Quick Setup

1. **Install Prerequisites**
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare Data**
   - Place your `Pick3StatsC4.xlsm` Excel file in the `data/original/` folder

3. **Start the Application**
   ```bash
   streamlit run scripts/streamlit_app_with_analyzer.py
   ```

## Processing Data (First-Time Setup)

1. Select the **Process Data** tab
2. Ensure all three options are checked:
   - Clean Data
   - Extract Data
   - Generate Tables
3. Click **Process Data**
4. Wait for processing to complete

## Running V-TRAC Analysis

1. Select the **V-TRAC Analyzer** tab
2. Choose analysis mode:
   - **Single State**: Analyze one state at a time
   - **All States**: Analyze multiple states at once
3. Set the **Minimum Pattern Count** (recommended: 3)
4. Click **Run V-TRAC Analysis**
5. Review the results:
   - Top indices ranked by pattern occurrence
   - HTML reports with highlighted patterns

## Viewing and Using Reports

1. Click on the tabs to view each ranked index report
2. Use the **Open in Browser** button for a full-screen view
3. Use the **Download HTML** button to save the report
4. The HTML reports show:
   - Midday, Evening, and Combined tables side-by-side
   - Patterns highlighted in purple
   - Statistics on pattern frequency and distribution

## Tips for Best Results

- **Pattern Threshold**: Set between 2-4 for optimal results
- **Multiple States**: When analyzing all states, the rankings will show the best indices across all states
- **Regular Updates**: Re-run the analysis after processing new data for updated results

## Batch Operation

For automated batch processing, use the included `run_with_analyzer.bat` file:

```
@echo off
echo ================================
echo = V-TRAC Analyzer (Test Version) =
echo ================================
echo.

cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run scripts/streamlit_app_with_analyzer.py

pause
```

This quick-start guide should help you get up and running with the V-TRAC Analyzer tool quickly and effectively. 