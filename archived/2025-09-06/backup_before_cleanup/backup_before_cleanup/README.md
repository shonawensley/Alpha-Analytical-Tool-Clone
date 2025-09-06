# Lottery Analysis Tool

A Python-based tool for analyzing lottery data with pattern recognition and V-TRAC analysis.

## Features

- Process Pick3StatsC4 Excel files
- Clean and organize data by state
- Generate combined and R2-only tables
- V-TRAC pattern analysis and highlighting
- Interactive Streamlit interface
- Data export capabilities (CSV, Excel, JSON)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd lottery-analysis-tool
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Unix/MacOS:
```bash
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create required data directories:
```bash
mkdir -p data/{original,cleaned,outputs,archive,historical_files,ai_exports}
```

## Usage

1. Place your Pick3StatsC4 Excel file in the `data/original` directory

2. Run the Streamlit app:
```bash
streamlit run scripts/utils/streamlit_app.py
```

3. Use the interface to:
   - Upload Pick3StatsC4 files
   - Select states for analysis
   - View combined and R2-only tables
   - Highlight winning patterns
   - Export results

## Project Structure

```
lottery-analysis-tool/
├── data/
│   ├── original/      # Original Excel files
│   ├── cleaned/       # Cleaned state data
│   ├── outputs/       # Generated outputs
│   ├── archive/       # Archived results
│   ├── historical_files/ # Historical Excel files
│   └── ai_exports/    # AI-friendly JSON exports
├── scripts/
│   ├── utils/
│   │   ├── clean_data.py
│   │   ├── extract_data.py
│   │   ├── table_generator.py
│   │   ├── vtrac_utils.py
│   │   └── streamlit_app.py
│   └── test_vtrac_streamlit.py
└── requirements.txt
```

## Data Privacy

- Keep your Pick3StatsC4 files private
- Do not commit data files to version control
- Use `.gitignore` to exclude sensitive data

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Advanced Features

### V-TRAC System
- Pattern matching system for identifying winning combinations
- Supports multiple pattern types (R2, R4, R6, R8)
- Highlights winning patterns in tables
- Interactive testing through test_vtrac_streamlit.py

### Data Processing
- Supports multiple states:
  - Connecticut4
  - Delaware4
  - Florida4
  - Indiana4
  - Michigan4
  - NewJersey4
  - NewYork4
  - NorthCarolina4
  - Ohio4
  - OntarioCanada4
  - Pennsylvania4
  - PuertoRico4
  - SouthCarolina4
  - Virginia4

### Table Features
- Hot zone marking for specific draws
- Combined table views (Midday/Evening/Combined)
- R2-only table generation
- Excel export with proper formatting
- JSON export for data analysis

### Data Management
- Historical file tracking
- Automated data cleaning
- State-specific data processing
- Backup and archive system

## Troubleshooting

### Common Issues
1. Import Errors
   - Ensure you're running from the project root
   - Check virtual environment activation
   - Verify all dependencies are installed

2. Excel File Issues
   - Use correct Pick3StatsC4 format
   - Place files in data/original directory
   - Check file permissions

3. Streamlit Interface
   - Port conflicts: Close other Streamlit instances
   - Display issues: Clear browser cache
   - State switching: Allow time for processing

### Getting Help
- Check the documentation in the docs/ directory
- Review error messages in the console
- Contact repository maintainers

## Documentation
Detailed documentation available in docs/:
- Alpha -Comprehensive Combination Methods
- Alpha -Digit Reduction
- Features Advanced Design
- Initial Program Design Theory
- And more... 