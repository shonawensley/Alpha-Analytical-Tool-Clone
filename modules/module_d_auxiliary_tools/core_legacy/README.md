# Lottery Data Analysis Tool

A Python-based lottery analysis application for analyzing Pick3 draw data with V-Trac analysis.

## Features

- Reads daily Pick3 draw data from Excel files
- Maps draws to V-Trac indices for analysis
- Tracks overdue pairs and combinations
- Analyzes due pairs based on configurable thresholds
- Color-codes data based on lateness criteria
- Provides state-by-state and combined analytics 
- Streamlit-based user interface

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Place Excel data file in `data/original` folder
3. Run the application:
   ```
   streamlit run app.py
   ```

## Project Structure

- `app.py`: Main Streamlit application
- `modules/`: Code modules for data processing and analysis
- `data/`: Data directory
  - `original/`: Raw Excel files
  - `cleaned/`: Processed data
  - `outputs/`: Analysis results 