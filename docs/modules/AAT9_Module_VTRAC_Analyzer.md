# AAT9 ▸ Module D: V-TRAC Analyzer

This document provides a comprehensive overview of the V-TRAC Analyzer module, which includes V-TRAC pattern analysis, winner logging, and the creation of data bundles for future machine learning.

## 1. Purpose & Role in AAT9

The V-TRAC Analyzer is a cornerstone of the AAT9 suite. Its primary functions are:

1.  **Analyze Data Tables**: It systematically processes the generated CSV tables (`Midday_combined`, `Evening_combined`, `Combined_combined`) for each state.
2.  **Rank V-TRAC Indices**: It evaluates all 35 V-TRAC indices to identify and rank which ones have the strongest, most persistent pattern clusters within the data.
3.  **Log Winners**: It provides a user interface to log the daily Midday and Evening winning numbers.
4.  **Generate Learning Payloads**: It creates machine-readable JSON "bundles" that correlate the tool's predictions with the actual winners, forming the basis for a machine learning feedback loop.
5.  **Produce Human-Readable Reports**: It generates detailed HTML reports with color-coded highlights for visual analysis, debugging, and demonstration.

In the overall AAT9 architecture, the V-TRAC Analyzer is a primary analysis module that produces feature-rich outputs for the final `Aggregator / ML brain`.

```
[Tables] → [V-TRAC Analyzer] → [HTML Reports (for humans)] + [JSON Bundles (for machine learning)]
```

## 2. Core Components & Key Files

| File | Location | Purpose |
| :--- | :--- | :--- |
| **Streamlit App** | `scripts/streamlit_app_with_analyzer.py` | The main user interface. The **V-TRAC Analyzer** and **Log & Highlight Winners** tabs contain all the logic for this module. |
| **V-TRAC Utilities**| `utils/vtrac_utils.py` | Contains the core V-TRAC logic, including the `BOXED_VTRAC_REFERENCE` table and helper functions for pattern matching and scoring. |
| **Bundler** | `utils/bundler.py` | Contains the crucial `bundle_day` function, which merges the V-TRAC predictions and the logged winners into a single, machine-readable JSON file. |

## 3. Data Flow: Understanding the Outputs

The distinction between HTML, CSV, and JSON files is critical. Each serves a different purpose.

| File Type | Path | Purpose |
| :--- | :--- | :--- |
| **Prediction JSON** | `data/outputs/predictions/` | **Machine-Readable**. Contains the raw output of the V-TRAC analysis, including the top-ranked indices, their scores, and the patterns they represent. |
| **Winners JSON** | `data/outputs/winners_json/` | **Machine-Readable**. Contains the winning numbers for a specific state and date, as entered by you in the UI. |
| **Bundle JSON** | `data/outputs/bundles/` | **CRITICAL FOR ML**. This is the most important machine-readable output. It combines the `predictions` and `winners` JSON into a single file, creating a complete record of "what the tool predicted" vs. "what actually won". **This is what the ML model will learn from.** |
| **Analysis HTML** | `data/outputs/analysis/` | **Human-Readable**. Detailed, color-coded reports for visually inspecting the top-ranked V-TRAC indices and their patterns in the data tables. Used for QA and demos, **not for ML**. |
| **Winners HTML/CSV**| `data/outputs/winners/` | **Human-Readable**. Highlighted versions of the data tables showing where the winning numbers appeared. Used for visual confirmation. |

### How the System "Learns"

The system does **not** learn from the colorful HTML files. The learning process is designed to happen in a separate, future ML step and works like this:

1.  **Data Capture (Current Step)**: The Streamlit app runs the analysis and you log winners. This generates the raw CSV tables and the essential JSON bundle (`{state}_{date}_bundle.json`), which contains the predictions and the actual winning numbers.
2.  **Feature Engineering & Training (Future ML Step)**: A training script (e.g., a Python notebook) will load the `bundle.json`. For each entry, it will:
    *   Read the prediction and the actual winner.
    *   Load the corresponding raw CSV tables for that day.
    *   Use the same helper functions (e.g., `count_patterns_in_table`) to re-calculate the pattern features from the raw data.
    *   Train a model to find correlations between the features it calculates and the winning outcomes.

This ensures the model is learning from the raw data, guided by the predictions and results captured in the JSON bundles.

## 4. Actionable Roadmap & Cleanup

Here is a concrete plan based on the "checkpoint" document to finalize this module and prepare for the next steps.

### A. Folder & File Cleanup (Immediate)

These actions will tidy the repository without breaking any code.

- **Archive Old Scripts**: Move any duplicate scripts from the root `scripts/` directory into `scripts/archive/`. The canonical, "live" scripts are the ones in `scripts/core/` and `scripts/utils/`.
- **Remove Legacy Tables**: The `_R2_only.csv` tables are no longer used by the main analysis modules. They can be safely deleted from any existing `data/outputs/tables/` directories to reduce clutter.
- **Archive Old HTML**: If the `data/outputs/analysis/` or `data/outputs/winners/` folders are cluttered with old reports, move them to a new `html_archive/` folder to start fresh.

### B. Code & Pipeline (Next Steps)

- **Drop R2-Only Table Generation**: In `utils/table_generator.py` (or the `generate_tables` function), comment out the lines that save the `_R2_only` DataFrames. This will stop them from being generated going forward.
- **Integrate into a Single App**: The long-term goal is to have one unified AAT9 Streamlit application. The current `streamlit_app_with_analyzer.py` is an excellent foundation. The next step is to create a central `src/app.py` and migrate the functionality of the standalone tools (like Stable-Pattern Extractor, Digit Reducer) into it as separate tabs or modules.

### C. What to Commit to GitHub

When you are ready to save the current progress, here is a recommended set of files to commit under a feature branch (e.g., `feat/vtrac-analyzer-mvp`):

-   `scripts/streamlit_app_with_analyzer.py`
-   `utils/vtrac_utils.py`
-   `utils/bundler.py`
-   `utils/path_handler.py`
-   `docs/modules/AAT9_Module_VTRAC_Analyzer.md` (this file)
-   An updated `docs/README_AAT9.md`

This captures the entire V-TRAC module as a stable, working component of AAT9. 