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