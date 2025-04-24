# Ideal Workflow Guide: Generating Tables & Running Analysis

## Overview

This guide explains the recommended **two-step workflow** for using the Alpha Analytical Tool efficiently. This approach separates the **data generation** step from the **data analysis** step, making the process clearer, faster for analysis, and easier to extend with new tools.

This workflow runs in parallel to the existing integrated applications, providing a safe way to test and build.

**The Core Idea:**

1.  **Generate Tables ONCE:** Run a dedicated script to process the raw Excel data and create all the standard CSV analysis tables (Midday Combined, Evening R2-only, etc.). This creates your stable "Combined Tables Environment".
2.  **Run Analysis Tools MANY TIMES:** Use separate tools (like the Standalone V-TRAC Analyzer or your own custom tools) that *load* the tables generated in Step 1 to perform their analysis.

```mermaid
graph LR
    A[Raw Excel Data (.xlsm)] --> B(Step 1: generate_tables_pipeline.bat);
    B --> C{Combined Tables Environment};
    C --> D(Step 2: run_vtrac_analyzer_standalone.bat);
    C --> E(Step 2: run_pattern_extractor.bat);
    C --> F(Step 2: run_my_new_analyzer.bat);

    subgraph "Data Generation"
        B
    end

    subgraph "Combined Tables Storage"
        C[data/outputs/tables/STATE/*.csv]
    end

    subgraph "Analysis Tools (Load Existing Tables)"
        D
        E
        F
    end

    style C fill:#f9f,stroke:#333,stroke-width:2px
```

## Step 1: Generating the Combined Tables Environment

*   **What:** This step takes the raw `Pick3StatsC4.xlsm` file, cleans the data, extracts sets, and generates the 6 standard CSV tables for *all* states.
*   **Script:** `scripts/core/generate_tables_pipeline.py` (This script performs the work).
*   **How to Run:** Double-click the `generate_tables_pipeline.bat` file in the project's main directory.
*   **Output:** Creates/updates the CSV files inside `data/outputs/tables/[STATE_NAME]/` (e.g., `data/outputs/tables/Florida4/Florida4_Midday_combined.csv`).
*   **When to Run:** Run this *once* whenever you have new raw data in the Excel file that needs to be processed.

## Step 2: Running Analysis Tools

Once the tables are generated in Step 1, you can run any analysis tool that is designed to load these tables.

### Example: Running the Standalone V-TRAC Analyzer

*   **What:** This tool performs the V-TRAC index analysis based on the tables generated in Step 1. It *only* loads data; it does not regenerate it.
*   **Script:** `scripts/core/vtrac_analyzer_standalone.py` (This script contains the Streamlit app and analysis logic).
*   **How to Run:** Double-click the `run_vtrac_analyzer_standalone.bat` file in the project's main directory.
*   **Input:** Reads the necessary CSV tables from `data/outputs/tables/[SELECTED_STATE]/`.
*   **Output:** Displays the V-TRAC rankings and generates detailed HTML reports in `data/outputs/analysis/`.
*   **When to Run:** Run this anytime you want to perform V-TRAC analysis on the existing generated tables. You can run it multiple times without re-running Step 1.

## Building Your Own Analysis Tool (e.g., Pattern Extractor)

This two-step workflow makes adding your own tools much easier:

1.  **Create Your Script:**
    *   Make a new Python file, for example: `scripts/core/pattern_extractor.py`.
    *   **Import necessary utilities:** You'll likely need `pandas` and potentially functions from `scripts.utils.path_handler` and `scripts.utils.state_utils`.
    *   **Load Data:** Use a function similar to `load_state_data` found in `vtrac_analyzer_standalone.py`. This function reads the required CSV tables for a specific state from `data/outputs/tables/[STATE_NAME]/` into Pandas DataFrames.
        ```python
        # Example inside your pattern_extractor.py
        import pandas as pd
        import os
        from scripts.utils.path_handler import get_tables_output_dir
        from scripts.utils.state_utils import STATES # To get state list if needed

        def load_analysis_data(state_name):
            state_tables_dir = os.path.join(get_tables_output_dir(), state_name)
            tables = {}
            if not os.path.exists(state_tables_dir):
                print(f"ERROR: Directory not found: {state_tables_dir}")
                return None # Or raise error

            # Load the specific tables you need, e.g., Combined_combined
            table_path = os.path.join(state_tables_dir, f"{state_name}_Combined_combined.csv")
            if os.path.exists(table_path):
                 try:
                     tables['Combined_combined'] = pd.read_csv(table_path)
                 except Exception as e:
                     print(f"Error loading {table_path}: {e}")
            # Load other tables as needed...
            
            if not tables:
                 print(f"ERROR: No required tables loaded for {state_name}")
                 return None

            return tables

        # --- Your main analysis logic ---
        selected_state = "Florida4" # Or get from user input/Streamlit widget
        state_tables = load_analysis_data(selected_state)

        if state_tables:
            combined_df = state_tables.get("Combined_combined")
            if combined_df is not None:
                print(f"Loaded Combined table for {selected_state}. Shape: {combined_df.shape}")
                # --- START YOUR PATTERN ANALYSIS HERE ---
                # Example: Find frequent patterns in column '1'
                # patterns = combined_df['1'].astype(str).value_counts()
                # print(patterns.head())
                # --- END YOUR PATTERN ANALYSIS HERE ---
            else:
                 print("Combined_combined table not loaded.")
        ```
    *   **Perform Analysis:** Write your Python code to analyze the patterns within the loaded DataFrame(s).
    *   **Output Results:** You can print results, save them to a file (e.g., in `data/outputs/analysis/`), or build a Streamlit interface like the V-TRAC analyzer.

2.  **Create a Batch File:**
    *   Make a new `.bat` file, for example: `run_pattern_extractor.bat`.
    *   Copy the structure from `run_vtrac_analyzer_standalone.bat`.
    *   Change the `streamlit run` or `python` command to execute *your* new script (`scripts/core/pattern_extractor.py`).

3.  **Run:**
    *   Make sure you've run `generate_tables_pipeline.bat` at least once (Step 1).
    *   Double-click your new `run_pattern_extractor.bat` to run your analysis (Step 2).

## Fallback Option

Your original batch files (`run_app.bat`, `run_enhanced_analyzer_final.bat`, `run_with_analyzer.bat`) are still available and unchanged. If you encounter issues with the new workflow, you can always revert to using the previous methods.

This separation makes the whole process more robust, efficient, and much easier to understand and build upon. 