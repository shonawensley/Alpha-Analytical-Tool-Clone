# Lottery Data Analysis Tool Documentation

## 1. Overview
The Lottery Data Analysis Tool is a Python-based application that analyzes Pick3 lottery draw data across multiple states. It provides detailed analysis of draw patterns, overdue pairs, and combinations using various metrics and visualization techniques.

## 2. Data Source and Processing

### 2.1 Excel File Structure
- Reads from `Pick3StatsC4.xlsx/xlsm` files
- Expects data in the "P3Draws" sheet
- State identifiers are located in row 15 (0-indexed: 14)
- Draw data starts from row 20 (0-indexed: 19)

### 2.2 State ID to Column Mapping
The application maps state IDs to specific columns in the Excel file:

| State ID | State Name       | Expected Column |
|----------|------------------|-----------------|
| 4        | Connecticut      | N               |
| 5        | Delaware         | O               |
| 6        | Florida          | P               |
| 7        | Georgia          | Q               |
| 10       | Indiana          | T               |
| 15       | Michigan         | Y               |
| 18       | New Jersey       | AB              |
| 20       | New York         | AD              |
| 21       | North Carolina   | AE              |
| 22       | Ohio             | AF              |
| 23       | Ontario          | AG              |
| 24       | Pennsylvania     | AH              |
| 25       | Puerto Rico      | AI              |
| 26       | South Carolina   | AJ              |
| 28       | Texas            | AL              |
| 29       | Tri-State        | AM              |
| 30       | Virginia         | AN              |
| 74       | West Virginia    | CF              |

### 2.3 Draws Per Day
Most states have 2 draws per day by default, with these exceptions:
- West Virginia: 1 draw per day
- Georgia: 3 draws per day
- Texas: 4 draws per day

### 2.4 Data Processing Pipeline
1. Reads Excel file and extracts draw data for each state
2. Cleans and validates the data
3. Saves processed data to `data/cleaned/` directory (as CSV files)
4. Performs analysis on the cleaned data
5. Saves analysis results to `data/outputs/` (as JSON files)

## 3. Analysis Features

### 3.1 Pair Analysis
The application tracks two types of pairs:
1. **Non-repeating pairs**: Different digits (e.g., "01", "23")
2. **Repeating pairs (doubles)**: Same digits (e.g., "00", "11")

#### 3.1.1 Pair Extraction Logic
From each 3-digit draw (e.g., "123"), the following pairs are extracted:
- (digit1, digit2) → "12"
- (digit2, digit3) → "23"
- (digit1, digit3) → "13"

All pairs are stored in canonical form (digits sorted) to avoid duplicates.

#### 3.1.2 Overdue Categories and Thresholds
1. **Non-repeating Pairs**:
   - RED (Late): ≥ 37 draws
   - BLUE (Very Late): ≥ 56 draws
   - PURPLE (Pending): ≥ 25 draws

2. **Repeating Pairs**:
   - RED (Late): ≥ 71 draws
   - BLUE (Very Late): ≥ 107 draws
   - PURPLE (Pending): ≥ 25 draws

### 3.2 V-Trac Analysis
- V-Trac is a system for categorizing Pick3 draws into 30 different indices
- Each index contains specific "singles" and "doubles" combinations
- The application maps draws to their corresponding V-Trac indices
- Tracks combinations that haven't appeared in 1000 draws
- Underlines combinations that haven't appeared
- Color-codes combinations based on their constituent pairs

#### 3.2.1 V-Trac Indices
The V-Trac system divides all possible 3-digit combinations into 30 distinct indices:
- Each index contains specific "singles" and "doubles" combinations
- Singles: Combinations where all three digits are different
- Doubles: Combinations where at least two digits are the same

### 3.3 Doubles History
- Tracks the number of draws since the last double for each state
- Ranks states by draws since last double
- Shows the latest double that appeared for each state
- A "double" is defined as any draw containing at least one pair of identical digits

## 4. User Interface Features

### 4.1 State Analysis View
For each state, displays:
1. Latest Draws
2. Overdue Pairs Analysis:
   - Separated by repeating and non-repeating pairs
   - Color-coded based on overdue thresholds
3. Pairs Analysis Results Table:
   - Times drawn
   - Last seen date
   - Draws since last appearance
4. V-Trac Analysis Table:
   - Singles and doubles for each index
   - Color-coded combinations
   - Underlined combinations (not seen in 1000 draws)
5. Top 5 Most Overdue Repeating Pairs

### 4.2 Combined Analysis View
Shows:
1. States ranked by draws since last double
2. Latest double for each state
3. Total draws analyzed per state
4. Special indicators for states with no doubles found

### 4.3 Analysis Settings
- Adjustable analysis window size (50-500 draws)
- Default analysis window: 100 draws
- Larger windows show fewer overdue pairs
- Smaller windows show more overdue pairs

## 5. File Structure
```
project/
├── app.py                  # Main Streamlit application
├── run_process.py          # Data processing pipeline
├── run.py                  # Script to run the application
├── debug_lottery.py        # Debug utilities
├── modules/
│   ├── parse_excel.py      # Excel file processing
│   ├── analyze_pairs.py    # Pair analysis logic
│   └── vtrac_reference.py  # V-Trac mapping and reference data
├── data/
│   ├── original/           # Raw Excel files (Place Pick3StatsC4.xlsm here)
│   ├── cleaned/            # Processed data (CSVs)
│   └── outputs/            # Analysis results (JSONs)
├── v-trac table boxed/     # V-Trac reference tables
└── v-trac full permutations/ # Additional V-Trac data
```

## 6. How to Run the Application

### 6.1 Prerequisites
- Python 3.6 or higher
- Required Python packages: pandas, numpy, openpyxl, streamlit, matplotlib

### 6.2 Setup
1. Place your `Pick3StatsC4.xlsm` file in the `data/original/` directory
2. Install required packages: `pip install -r requirements.txt`

### 6.3 Running the Application
You can run the application in two ways:

1. **Streamlit Web Interface** (Recommended):
   ```bash
   streamlit run app.py
   ```
   This will start a web server and open the application in your browser.

2. **Command Line Interface**:
   ```bash
   python run_process.py
   ```
   This will process the data and save results without launching the web UI.

3. **Batch File** (Windows only):
   Double-click the `start_lottery_app.bat` file to launch the application.

### 6.4 Using the Application
1. Use the sidebar to navigate between different states and the combined view
2. Adjust the analysis window size as needed (50-500 draws)
3. Upload a new Excel file if you want to refresh the data

## 7. Future Enhancements (Based on User Request)
1. Enhanced State Ranking Display:
   - Add combinations with overdue pairs beside state rankings
   - Include combinations with due double pairs not seen in 1000 draws
   - Show all qualifying combinations based on pair criteria

2. Improved Documentation:
   - Regular updates to reflect new features
   - Detailed troubleshooting guides
   - Clear explanation of analysis criteria

## 8. Troubleshooting
1. **Excel File Not Found**:
   - Make sure `Pick3StatsC4.xlsm` is placed in the `data/original/` directory
   - Check if the file name is exactly as expected (case-sensitive)

2. **Sheet Not Found**:
   - Ensure your Excel file has a sheet named "P3Draws"
   - If not, the program will try to use the first available sheet

3. **State Data Not Found**:
   - Check row 15 of your Excel file for state IDs
   - Verify that state IDs match the expected values listed in Section 2.2

4. **Application Won't Start**:
   - Check that all required packages are installed
   - Verify that you're running the command from the project root directory

This documentation provides a comprehensive overview of the application's functionality, data processing, analysis features, and user interface. It can be used as a reference for understanding the system and troubleshooting issues. 