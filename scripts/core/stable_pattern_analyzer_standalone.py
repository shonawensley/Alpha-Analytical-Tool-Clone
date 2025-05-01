#!/usr/bin/env python
"""
stable_pattern_analyzer_standalone.py

Streamlit-based UI that:
 1) Loads pre-generated CSV tables for a selected state (similar to how vtrac_analyzer_standalone does).
 2) Converts the CSV table data into the JSON-like structure expected by stable_pattern_extractor_full.
 3) Calls the advanced stable pattern extraction script (stable_pattern_extractor_full.py) to find stable patterns.
 4) Displays a summary of top stable patterns in Streamlit, allows downloading results as CSV/JSON, and offers the generated HTML report for download.

This integrates the core logic (Part 1) with a UI and CSV loading mechanism (Part 2).
"""

import os
import sys
import traceback  # For detailed error logging
import json
import time
from datetime import datetime
from collections import defaultdict, Counter
from functools import lru_cache

import streamlit as st
import pandas as pd
import numpy as np

# Adjust path to import from project root
# -----------------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))  # up 2 levels
sys.path.append(project_root)

# 1) Import the PART 1 stable extractor.
# -----------------------------------------------------------------
try:
    from scripts.core.stable_pattern_extractor_full import (
        run_stable_pattern_extraction,
        build_html_report  # Also import the HTML report builder
    )
except ImportError as e:
    st.error("FATAL ERROR: Cannot import stable_pattern_extractor_full.py.")
    st.error(f"Details: {e}")
    st.error("Please ensure 'scripts/core/stable_pattern_extractor_full.py' exists and is accessible.")
    st.stop()

# 2) Import project utilities for path handling and state list.
# -----------------------------------------------------------------
try:
    from scripts.utils.path_handler import get_tables_output_dir, get_analysis_output_dir
    from scripts.utils.state_utils import STATES
except ImportError as e:
    st.error("FATAL ERROR: Cannot import path_handler or state_utils.")
    st.error(f"Details: {e}")
    st.error("Please ensure 'scripts/utils/' directory and its contents are correct.")
    st.stop()


###############################################################################
# Data Loading (Adapted from vtrac_analyzer_standalone.py)
###############################################################################

@lru_cache(maxsize=16)  # Cache loaded tables for performance
def load_state_data_cached(state_name: str) -> dict:
    """
    Cached loader for a state's CSV tables from the output/tables/[STATE_NAME] folder.
    Returns a dictionary of DataFrames {table_key: df}.
    """
    tables_root = get_tables_output_dir()
    state_tables_dir = os.path.join(tables_root, state_name)

    if not os.path.exists(state_tables_dir):
        print(f"[ERROR] State directory not found: {state_tables_dir}")
        st.error(
            f"Directory not found: {state_tables_dir}. "
            "Please generate tables first using generate_tables_pipeline.bat."
        )
        return {}

    print(f"Loading tables for {state_name} from: {state_tables_dir}")
    result = {}
    loaded_files = 0

    for filename in os.listdir(state_tables_dir):
        if filename.endswith(".csv"):
            filepath = os.path.join(state_tables_dir, filename)
            # Key uses filename without state prefix and extension
            key_parts = os.path.splitext(filename)[0].split(f"{state_name}_")
            key = key_parts[1] if len(key_parts) > 1 else os.path.splitext(filename)[0]
            try:
                # Load as string, fill NaNs with 'N/A' for consistency
                df = pd.read_csv(filepath, dtype=str).fillna('N/A')
                result[key] = df
                loaded_files += 1
            except Exception as e:
                print(f"[ERROR] Error loading {filename}: {e}")
                st.warning(f"Could not load table: {filename}")

    if not result:
        print(f"[ERROR] No CSV tables successfully loaded from {state_tables_dir}")
        st.error(
            f"No CSV tables found or loaded from {state_tables_dir}. "
            "Please check the directory and file integrity."
        )
        return {}

    print(f"Successfully loaded {loaded_files} tables for {state_name}.")
    return result


def load_state_data(state_name: str) -> dict:
    """
    Load generated tables for a specific state using session-state caching.
    """
    if "stable_pattern_loaded_tables" not in st.session_state:
        st.session_state.stable_pattern_loaded_tables = {}

    if state_name not in st.session_state.stable_pattern_loaded_tables:
        st.session_state.stable_pattern_loaded_tables[state_name] = load_state_data_cached(state_name)

    return st.session_state.stable_pattern_loaded_tables[state_name]


###############################################################################
# Convert CSV DataFrames -> 'JSON-like' structure for the stable extractor
###############################################################################

def convert_csv_to_json_structure(tables_dict: dict) -> dict:
    """
    Converts the dictionary of loaded CSV DataFrames into the nested JSON
    structure expected by `run_stable_pattern_extraction`.
    Focuses on *_combined tables.
    """
    sections_data = defaultdict(
        lambda: {
            "sets": defaultdict(
                lambda: {
                    "draws": defaultdict(
                        lambda: {"pattern_variations": defaultdict(list), "metadata": {}}
                    )
                }
            )
        }
    )
    section_keys = {
        "Midday": "Midday_combined",
        "Evening": "Evening_combined",
        "Combined": "Combined_combined",
    }
    # Row types expected by the extractor logic
    row_types = ["R2", "R4", "R6", "R8", "DRAW_DATA"]
    # Columns expected by the extractor logic (7 down to 1)
    col_indices = [str(i) for i in range(7, 0, -1)]

    conversion_successful = False

    for section_name, table_key in section_keys.items():
        if table_key not in tables_dict or tables_dict[table_key].empty:
            print(f"[Warning] Skipping section '{section_name}': Table '{table_key}' not found or empty.")
            continue

        df = tables_dict[table_key].copy()
        required_csv_cols = ["Set", "Draw", "RowType"] + col_indices
        if not all(col in df.columns for col in required_csv_cols):
            print(
                f"[Error] Table '{table_key}' is missing required columns. "
                f"Needs: {required_csv_cols}. Found: {df.columns.tolist()}"
            )
            st.warning(
                f"Table '{table_key}' structure is incorrect. "
                f"Skipping conversion for section '{section_name}'."
            )
            continue

        conversion_successful = True

        # Sort & group by Set and Draw
        try:
            df["Draw_Num"] = pd.to_numeric(df["Draw"], errors="coerce")
            grouped = df.sort_values(by=["Set", "Draw_Num", "Draw"]).groupby(["Set", "Draw"])
        except Exception:
            # fallback if numeric conversion fails
            grouped = df.groupby(["Set", "Draw"])

        for (set_name, draw_id), group in grouped:
            draw_label = f"Draw{draw_id}"
            current_draw_data = {
                "pattern_variations": defaultdict(list),
                "metadata": {"is_hot_zone": False, "hot_zone_indicators": {}},
            }

            for rt in row_types:
                rt_rows = group[group["RowType"] == rt]
                if not rt_rows.empty:
                    row = rt_rows.iloc[0]
                    pattern_list = [str(row[col]) if pd.notna(row[col]) else "" for col in col_indices]
                    current_draw_data["pattern_variations"][rt] = pattern_list
                # else:
                #   current_draw_data["pattern_variations"][rt] = [''] * len(col_indices)

            sections_data[section_name]["sets"][str(set_name)]["draws"][str(draw_label)] = current_draw_data

    if not conversion_successful:
        st.error("Conversion failed: No valid *_combined tables found or processed.")
        return None

    # Convert defaultdicts to normal dicts
    final_data = json.loads(json.dumps(sections_data))
    return {"sections": final_data}


###############################################################################
# Results Processing & Saving
###############################################################################

def flatten_results(results_dict) -> list:
    """
    Flatten the nested results dictionary into a list of records for DataFrame/CSV.
    """
    all_patterns = []
    if not isinstance(results_dict, dict):
        print("[Error] Invalid results format passed to flatten_results: Expected dict.")
        return []

    try:
        # Iterate through sections (e.g., Midday, Evening)
        for section_name, setsdict in results_dict.items():
            if not isinstance(setsdict, dict):
                continue
            # Iterate through sets (e.g., Set1, Set2)
            for set_name, draw_list in setsdict.items():
                if not isinstance(draw_list, list):
                    continue
                # Iterate through draws (list of column-lists)
                for d_idx, col_list in enumerate(draw_list):
                    draw_label = f"Draw{d_idx + 1}"  # we label them Draw1, Draw2, ...
                    if not isinstance(col_list, list):
                        continue
                    # Iterate through columns (list of pattern dicts)
                    for col_i, cdict in enumerate(col_list):
                        if not isinstance(cdict, dict):
                            continue
                        # Iterate through patterns in this column
                        for pat, info in cdict.items():
                            if not isinstance(info, dict):
                                continue
                            record = {
                                "Section": section_name,
                                "Set": set_name,
                                "Draw": draw_label,
                                "Column": col_i + 1,  # 1-based
                                "Pattern": pat,
                                "Score": info.get("score", 0),
                            }
                            # Add debug_info if available
                            debug_info = info.get("debug_info", {})
                            if isinstance(debug_info, dict):
                                for k, v in debug_info.items():
                                    record[f"dbg_{k}"] = v

                            all_patterns.append(record)
    except Exception as e:
        print(f"[Error] Unexpected error during results flattening: {e}")
        return []

    return all_patterns


def save_results_to_files(
    state_name: str,
    results_dict: dict,
    flat_results_df: pd.DataFrame,
    html_report: str
) -> dict:
    """
    Saves the analysis results to JSON, CSV, and HTML.
    Files are saved in data/outputs/analysis/stable_pattern/[STATE]/.
    """
    try:
        output_dir_base = os.path.join(get_analysis_output_dir(), "stable_pattern")
        state_output_dir = os.path.join(output_dir_base, state_name)
        os.makedirs(state_output_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"{state_name}_stable_patterns_{timestamp}"

        # Paths for the files
        json_filepath = os.path.join(state_output_dir, f"{base_filename}_raw.json")
        csv_filepath = os.path.join(state_output_dir, f"{base_filename}_summary.csv")
        html_filepath = os.path.join(state_output_dir, f"{base_filename}_report.html")

        # 1. Save raw results to JSON
        with open(json_filepath, 'w', encoding='utf-8') as f:
            json.dump(results_dict, f, indent=2)
        print(f"Raw results saved to: {json_filepath}")

        # 2. Save flattened results DataFrame to CSV
        if flat_results_df is not None and not flat_results_df.empty:
            flat_results_df.to_csv(csv_filepath, index=False, encoding='utf-8')
            print(f"Summary results saved to: {csv_filepath}")
        else:
            print("Skipping CSV save: DataFrame is empty.")
            csv_filepath = None

        # 3. Save HTML report
        with open(html_filepath, 'w', encoding='utf-8') as f:
            f.write(html_report)
        print(f"HTML report saved to: {html_filepath}")

        st.success(f"Results saved successfully in '{state_output_dir}'")
        return {"json": json_filepath, "csv": csv_filepath, "html": html_filepath}

    except Exception as e:
        print(f"[ERROR] Failed to save results for {state_name}: {e}")
        st.error(f"Error saving results: {e}")
        traceback.print_exc()
        return {}


###############################################################################
# MAIN STREAMLIT APP
###############################################################################

def main():
    st.set_page_config(page_title="Stable Pattern Analyzer", layout="wide")
    st.title("🎯 Stable Pattern Analyzer (Standalone)")
    st.markdown(
        "Loads standard CSV tables, runs the `stable_pattern_extractor_full.py` logic, and displays results."
    )
    st.markdown("--- ")

    # Initialize session state
    if "stable_pattern_results" not in st.session_state:
        st.session_state.stable_pattern_results = {}
    if "stable_pattern_last_state" not in st.session_state:
        st.session_state.stable_pattern_last_state = None
    if "stable_pattern_saved_files" not in st.session_state:
        st.session_state.stable_pattern_saved_files = {}

    # --- Sidebar Controls ---
    st.sidebar.header("Controls")
    selected_state = st.sidebar.selectbox(
        "Select State",
        STATES,
        index=STATES.index(st.session_state.stable_pattern_last_state)
        if st.session_state.stable_pattern_last_state in STATES
        else 0,
    )
    st.session_state.stable_pattern_last_state = selected_state  # Remember selection

    top_n_display = st.sidebar.slider("Number of Top Patterns to Display", 10, 100, 25)
    auto_save = st.sidebar.checkbox("Automatically Save Results?", value=True)
    run_button = st.sidebar.button("Run Stable Pattern Analysis", type="primary")

    # --- Main Analysis Area ---
    if run_button:
        if not selected_state:
            st.warning("Please select a state first.")
            st.stop()

        # Clear previous results for this state
        st.session_state.stable_pattern_results.pop(selected_state, None)
        st.session_state.stable_pattern_saved_files.pop(selected_state, None)

        st.info(f"Starting analysis for {selected_state}...")
        progress_bar = st.progress(0, text="Loading data...")
        start_time = time.time()

        # 1. Load Data
        tables = load_state_data(selected_state)
        if not tables:
            progress_bar.empty()
            st.stop()

        progress_bar.progress(25, text="Converting data structure...")

        # 2. Convert to JSON structure
        json_data = convert_csv_to_json_structure(tables)
        if not json_data:
            progress_bar.empty()
            st.stop()

        progress_bar.progress(50, text="Extracting stable patterns...")

        # 3. Run Extraction
        results_dict = None
        try:
            results_dict = run_stable_pattern_extraction(json_data)
        except Exception as e:
            st.error(f"Error during pattern extraction: {e}")
            st.error(traceback.format_exc())

        if not results_dict:
            st.error("Pattern extraction failed or returned no results.")
            progress_bar.empty()
            st.stop()

        progress_bar.progress(75, text="Processing results...")

        # 4. Process Results
        flat_results_list = flatten_results(results_dict)
        if flat_results_list:
            flat_results_df = pd.DataFrame(flat_results_list)
            if "Score" in flat_results_df.columns:
                flat_results_df["Score"] = pd.to_numeric(
                    flat_results_df["Score"], errors="coerce"
                ).fillna(0)
                flat_results_df = flat_results_df.sort_values(
                    by="Score", ascending=False
                ).reset_index(drop=True)
            else:
                st.warning("Score column missing, cannot sort results.")
        else:
            flat_results_df = pd.DataFrame()
            st.warning("No patterns found after processing results.")

        # Generate HTML report
        try:
            html_report = build_html_report(results_dict)
        except Exception as e:
            st.error(f"Failed to build HTML report: {e}")
            html_report = "<html><body>No report generated due to error.</body></html>"

        # Store results in session state
        st.session_state.stable_pattern_results[selected_state] = {
            "raw": results_dict,
            "dataframe": flat_results_df,
            "html": html_report,
        }

        # 5. Save if requested
        saved_paths = None
        if auto_save:
            progress_bar.progress(90, text="Saving results...")
            saved_paths = save_results_to_files(
                selected_state, results_dict, flat_results_df, html_report
            )
            st.session_state.stable_pattern_saved_files[selected_state] = saved_paths

        end_time = time.time()
        progress_bar.progress(100, text="Analysis complete!")
        st.success(
            f"Analysis for {selected_state} completed in {end_time - start_time:.2f} seconds."
        )
        time.sleep(2)
        progress_bar.empty()

    # --- Display Area ---
    st.markdown("--- ")
    if selected_state in st.session_state.stable_pattern_results:
        st.header(f"Results for: {selected_state}")
        results_data = st.session_state.stable_pattern_results[selected_state]
        results_df = results_data.get("dataframe", pd.DataFrame())
        html_report = results_data.get("html", "")
        raw_results = results_data.get("raw", {})

        if results_df.empty:
            st.info("No stable patterns were found for this state based on the last run.")
        else:
            st.subheader(f"Top {min(top_n_display, len(results_df))} Stable Patterns")
            st.dataframe(results_df.head(top_n_display), use_container_width=True)

            # Download Buttons
            st.subheader("Downloads")
            col1, col2, col3 = st.columns(3)
            with col1:
                try:
                    csv_data = results_df.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        label="Download Results (CSV)",
                        data=csv_data,
                        file_name=(
                            f"{selected_state}_stable_patterns_summary_"
                            f"{datetime.now().strftime('%Y%m%d')}.csv"
                        ),
                        mime="text/csv",
                        key=f"csv_dl_{selected_state}",
                    )
                except Exception as e:
                    st.error(f"CSV DL Error: {e}")

            with col2:
                try:
                    json_data_str = json.dumps(raw_results, indent=2)
                    st.download_button(
                        label="Download Raw Results (JSON)",
                        data=json_data_str,
                        file_name=(
                            f"{selected_state}_stable_patterns_raw_"
                            f"{datetime.now().strftime('%Y%m%d')}.json"
                        ),
                        mime="application/json",
                        key=f"json_dl_{selected_state}",
                    )
                except Exception as e:
                    st.error(f"JSON DL Error: {e}")

            with col3:
                try:
                    st.download_button(
                        label="Download HTML Report",
                        data=html_report.encode("utf-8"),
                        file_name=(
                            f"{selected_state}_stable_patterns_report_"
                            f"{datetime.now().strftime('%Y%m%d')}.html"
                        ),
                        mime="text/html",
                        key=f"html_dl_{selected_state}",
                    )
                except Exception as e:
                    st.error(f"HTML DL Error: {e}")

            # Display saved file paths if available
            if (
                selected_state in st.session_state.stable_pattern_saved_files
                and st.session_state.stable_pattern_saved_files[selected_state]
            ):
                st.markdown("--- ")
                st.subheader("Saved File Locations (auto-save)")
                saved_info = {
                    k: os.path.basename(v) if v else "Not Saved"
                    for k, v in st.session_state.stable_pattern_saved_files[
                        selected_state
                    ].items()
                }
                st.json(saved_info, expanded=False)

            # Inline HTML Expander
            with st.expander("View HTML Report Inline", expanded=False):
                if html_report:
                    st.components.v1.html(html_report, height=600, scrolling=True)
                else:
                    st.warning("HTML report was not generated or available.")
    else:
        st.info("Select a state and click 'Run Stable Pattern Analysis' in the sidebar to begin.")


if __name__ == "__main__":
    main()
