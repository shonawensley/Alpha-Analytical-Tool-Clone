# Alpha Analytical Tool

A Python-based tool for analyzing lottery data with pattern recognition and V-TRAC analysis.

## Features

- Process Pick3StatsC4 Excel files
- Clean and organize data by state
- Generate combined and R2-only tables
- V-TRAC pattern analysis and highlighting
- Interactive Streamlit interface

## Getting Started

### Quick Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd lottery-analysis-tool
```

2. Set up environment (using included batch file):
```
install_packages.bat
```

3. Place your Pick3StatsC4 Excel file in the `data/original` directory

### Running the Application

Two batch files are provided for easy access:

1. **run_app.bat** - Runs the standard table generator app
2. **run_with_analyzer.bat** - Runs the enhanced app with V-TRAC analyzer

## Project Structure

The project has been organized for clarity and maintainability:

```
Alpha Analytical Tool/
├── scripts/
│   ├── core/                # Main application scripts
│   │   ├── streamlit_app_with_analyzer.py  # Enhanced app with V-TRAC
│   │   ├── streamlit_app.py               # Basic table generator
│   │   └── run_process.py                 # Core processing script
│   └── utils/               # Core utilities
│       ├── clean_data.py    # Data cleaning
│       ├── extract_data.py  # Data extraction
│       ├── table_generator.py # Table creation
│       └── vtrac_utils.py   # V-TRAC utilities
├── data/                    # Data storage
│   ├── original/            # Original Excel files
│   ├── cleaned/             # Cleaned CSV files
│   └── outputs/             # Generated output
└── docs/                    # Documentation
    ├── guides/              # Comprehensive guides
    ├── technical/           # Technical documentation
    └── quickstart/          # Getting started guides
```

## Documentation

Comprehensive documentation is available in the `docs` directory:

- For quick start guides: [docs/quickstart/](docs/quickstart/)
- For user guides: [docs/guides/](docs/guides/)
- For technical reference: [docs/technical/](docs/technical/)

See [docs/README.md](docs/README.md) for a complete guide to all documentation.

## Using the Application

### 1. Process Data
- Upload or select Pick3StatsC4 Excel file
- Process data for all states or selected states
- Generate tables for analysis

### 2. View Results
- Select state and table type
- View combined and R2-only tables
- Export tables to CSV if needed

### 3. V-TRAC Analysis
- Analyze tables for pattern clusters
- View ranked V-TRAC indices
- Generate HTML reports with pattern highlighting

## Data Privacy

This application is designed for local use only:
- Keep your data files private
- Do not commit data files to version control
- Use `.gitignore` to exclude sensitive data

## Need Help?

- Check the documentation in the docs/ directory
- Review error messages in the terminal
- See the Troubleshooting section in the docs 