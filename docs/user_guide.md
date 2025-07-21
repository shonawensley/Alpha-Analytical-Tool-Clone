## Using the Application

### Features

- Process Pick3StatsC4 Excel files
- Clean and organize data by state
- Generate combined and R2-only tables
- V-TRAC pattern analysis and highlighting
- Interactive Streamlit interface

### Getting Started & Quick Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd lottery-analysis-tool
    ```

2.  **Set up environment (using included batch file):**
    ```
    install_packages.bat
    ```

3.  **Place your Pick3StatsC4 Excel file in the `data/original` directory.**

### Running the Application

Two batch files are provided for easy access:

1.  `run_app.bat` - Runs the standard table generator app
2.  `run_with_analyzer.bat` - Runs the enhanced app with V-TRAC analyzer

---

## Processing and Analysis

### 1. Process Data
- Upload or select Pick3StatsC4 Excel file.
- Process data for all states or selected states.
- Generate tables for analysis.

### 2. View Results
- Select state and table type.
- View combined and R2-only tables.
- Export tables to CSV if needed.

### 3. V-TRAC Analysis
- Analyze tables for pattern clusters.
- View ranked V-TRAC indices.
- Generate HTML reports with pattern highlighting.

---

## Data Privacy

This application is designed for local use only:
- Keep your data files private.
- Do not commit data files to version control.
- Use `.gitignore` to exclude sensitive data.

## Need Help?

- Check the documentation in the `docs/` directory.
- Review error messages in the terminal.
- See the Troubleshooting section in the docs. 