# Lottery Data Processing System - Quick Start Guide

This guide will help you quickly set up, test, and run the Lottery Data Processing System.

## Prerequisites

1. Python 3.7+ installed
2. Required Python packages:
   - pandas
   - numpy
   - streamlit (for the web interface)
   - openpyxl (for Excel file handling)

Install required packages:
```bash
pip install pandas numpy streamlit openpyxl
```

## Project Structure Setup

1. Ensure your project has the following directory structure:
```
Lottery Data Processing System/
├── data/
│   ├── original/
│   │   └── Pick3StatsC4.xlsm  # Place your Excel file here
│   ├── cleaned/               # Will store cleaned data
│   └── outputs/               # Will store generated tables
├── scripts/
│   ├── utils/
│   ├── vtrac/
│   ├── run_process.py
│   ├── streamlit_app.py
│   └── test_components.py
└── QUICKSTART.md
```

2. Place your `Pick3StatsC4.xlsm` file in the `data/original/` directory

## Testing Components

The `test_components.py` script allows you to test individual components of the system without running the full pipeline.

### Basic Path Testing

Test and create project directories:
```bash
python scripts/test_components.py --paths
```

### Test Data Cleaning

Clean data for a specific state:
```bash
python scripts/test_components.py --clean --state Connecticut
```

Clean data for all states:
```bash
python scripts/test_components.py --clean
```

### Test Data Extraction

Extract data for a specific state (requires cleaned data):
```bash
python scripts/test_components.py --extract --state Connecticut
```

### Test Table Generation

Generate and display tables for a specific state (requires extracted data):
```bash
python scripts/test_components.py --extract --tables --state Connecticut
```

### Test V-TRAC Winner Highlighting

Test winner highlighting with specific numbers:
```bash
python scripts/test_components.py --extract --tables --vtrac --state Connecticut --winners 123,456,789
```

### Run Full Process Test

Test the complete pipeline for a specific state:
```bash
python scripts/test_components.py --full --state Connecticut
```

### Run Full Process Test with Winners

Test the complete pipeline with winner highlighting:
```bash
python scripts/test_components.py --full --state Connecticut --winners 123,456,789
```

## Running the Full System

### Command Line Processing

Process all states from the command line:
```bash
python scripts/run_process.py
```

Skip specific steps if needed:
```bash
python scripts/run_process.py --no-clean --no-extract
```

Process with winners:
```bash
python scripts/run_process.py --midday-winners 123,456 --evening-winners 789,012
```

### Streamlit Web Interface

Run the Streamlit app for an interactive interface:
```bash
streamlit run scripts/streamlit_app.py
```

The Streamlit app provides a user-friendly interface to:
- Process data for all or selected states
- View generated tables
- Log and highlight winners
- Analyze numbers using the V-TRAC system

## Troubleshooting

### Common Issues

1. **Excel File Not Found**:
   - Ensure `Pick3StatsC4.xlsm` is in the `data/original/` directory
   - Check that the filename matches exactly (case-sensitive)

2. **Path Issues**:
   - Run `python scripts/test_components.py --paths` to verify paths
   - Create missing directories when prompted

3. **State Not Found**:
   - Verify the state name in `utils/state_utils.py`
   - Check that the state sheet exists in your Excel file

4. **Missing Dependencies**:
   - Install required packages: `pip install pandas numpy streamlit openpyxl`

5. **Table Format Issues**:
   - For terminal table printing, install tabulate: `pip install tabulate`

## Advanced Usage

### Creating Sample Data

If you don't have real data but want to test the system:

1. Create a sample Excel file with sheets named after states in `STATES`
2. Include required columns with example data
3. Place the file in `data/original/` as `Pick3StatsC4.xlsm`

### Customizing the Process

Edit configuration settings in:
- `scripts/utils/path_handler.py` for path customization
- `scripts/utils/state_utils.py` for state list modification
- `scripts/utils/vtrac_utils.py` for V-TRAC system reference and pattern matching 