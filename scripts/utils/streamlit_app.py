#!/usr/bin/env python
"""
streamlit_app.py - Streamlit interface for lottery data processing
"""

import os
import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path
import tempfile
import json
import sys
import shutil

# Add parent directory to path so we can import from utils
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(script_dir)

from utils.extract_data import LotteryDataExtractor
from utils.table_generator import build_section_table, build_r2_only_table
from utils.path_handler import get_cleaned_data_dir, get_cleaned_state_path
from utils.clean_data import STATES
from vtrac_utils import highlight_winners_in_table, find_vtrac_index_and_combos
from excel_export import export_state_tables, setup_logging_directories

def get_project_root():
    """Get the absolute path to the project root"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(current_dir))

@st.cache_data
def process_excel_file(excel_path, cleaned_dir):
    """Process Excel file and clean all states (cached)"""
    return clean_all_states(STATES, excel_path, cleaned_dir)

@st.cache_data
def load_state_data(state_name, excel_path):
    """Load data for a single state (cached)"""
    try:
        extractor = LotteryDataExtractor(excel_path)
        return extractor.extract_all()
    except Exception as e:
        st.error(f"Error loading {state_name}: {str(e)}")
        return None

@st.cache_data
def build_tables(section_data):
    """Build combined and R2-only tables (cached)"""
    if not section_data:
        return None, None
    return build_section_table(section_data), build_r2_only_table(section_data)

def initialize_session_state():
    """Initialize session state variables"""
    if 'processed_states' not in st.session_state:
        st.session_state.processed_states = {}
    if 'last_upload' not in st.session_state:
        st.session_state.last_upload = None

def get_historical_files():
    """Get list of available historical Excel files."""
    historical_dir = Path("data/historical_files")
    if not historical_dir.exists():
        return []
    return sorted([f for f in historical_dir.glob("*.xlsx") if "Pick3StatsC4" in f.name])

def export_all_tables_to_csv(state_data, state_name):
    """Export all tables (Midday/Evening/Combined) vertically to a single CSV file"""
    import pandas as pd
    import os
    from datetime import datetime
    
    # Create output directory if it doesn't exist
    output_dir = "data/archive"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Initialize list to store all tables
    all_dfs = []
    
    # Process each section
    for section in ["Midday", "Evening", "Combined"]:
        if section not in state_data:
            continue
            
        # Build tables for this section
        combined_df = build_section_table(state_data[section])
        r2_df = build_r2_only_table(state_data[section])
        
        # Add section headers
        section_header = pd.DataFrame([
            [f"=== {section} Combined Table ==="] + [""] * (len(combined_df.columns) - 1)
        ], columns=combined_df.columns)
        
        r2_header = pd.DataFrame([
            [f"=== {section} R2-only Table ==="] + [""] * (len(r2_df.columns) - 1)
        ], columns=r2_df.columns)
        
        # Add empty row for spacing
        empty_row = pd.DataFrame([[""] * len(combined_df.columns)], columns=combined_df.columns)
        
        # Combine section tables with headers
        all_dfs.extend([
            section_header,
            combined_df,
            empty_row,
            r2_header,
            r2_df,
            empty_row,
            empty_row  # Extra spacing between sections
        ])
    
    # Combine all tables vertically
    final_df = pd.concat(all_dfs, ignore_index=True)
    
    # Save to CSV
    output_file = os.path.join(output_dir, f"{state_name}_all_tables_{timestamp}.csv")
    final_df.to_csv(output_file, index=False)
    
    return output_file

def export_to_json(state_data, state_name):
    """Export state data to AI-friendly JSON format with enhanced pattern analysis rules"""
    import json
    import os
    from datetime import datetime
    
    # Create AI exports directory
    output_dir = "data/ai_exports"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Structure the data for AI understanding
    ai_friendly_data = {
        "state_name": state_name,
        "sections": {
            section_name: {
                "sets": {
                    set_name: {
                        "draws": {
                            draw_name: {
                                "draw_data": data.get("draw_data", []),
                                "pattern_variations": {
                                    "R2": data.get("R2", []),  # 2000x pool size variation
                                    "R4": data.get("R4", []),  # 4000x pool size variation
                                    "R6": data.get("R6", []),  # 6000x pool size variation
                                    "R8": data.get("R8", [])   # 8000x pool size variation
                                },
                                "metadata": {
                                    "is_hot_zone": set_name == "Set1" and draw_name in ["Draw1", "Draw2", "Draw3", "Draw4", "Draw5"],
                                    "hot_zone_count": {
                                        "Draw1": 5, "Draw2": 5, "Draw3": 5, 
                                        "Draw4": 4, "Draw5": 2
                                    }.get(draw_name, 0) if set_name == "Set1" else 0
                                }
                            }
                            for draw_name, data in draws.items()
                        }
                    }
                    for set_name, draws in section_data.items()
                }
            }
            for section_name, section_data in state_data.items()
        },
        "analysis_guide": {
            "table_structure": {
                "combined_table": {
                    "description": "Each section (Midday/Evening/Combined) has identical combined table structure",
                    "layout": [
                        "Set3 Draw1 and Set2 Draw1 represent previous 2 days' patterns",
                        "Set1 Draw1 represents current day patterns",
                        "Set1 Draw1-7 show different progressions of current day patterns",
                        "Each Set1 structure reduces columns progressively (7→1 columns)"
                    ],
                    "progression": {
                        "Set1 Draw1": "7 columns (last 7 draws)",
                        "Set1 Draw2": "6 columns (last 6 draws)",
                        "Set1 Draw3": "5 columns (last 5 draws)",
                        "Set1 Draw4": "4 columns (last 3 draws)",
                        "Set1 Draw5": "3 columns (last 3 draws)",
                        "Set1 Draw6": "2 columns (last 2 draws)",
                        "Set1 Draw7": "1 column (last draw)"
                    }
                },
                "r2_table": {
                    "description": "Alternative pattern category from longer strings in outer columns",
                    "analysis": [
                        "Evaluate longer strings for persistent patterns",
                        "Look for V-TRAC relationships",
                        "Consider digit reduction using past draws and mirrors",
                        "Diversify pattern selections between R2 and R2/R4/R6/R8 methods"
                    ]
                }
            },
            "pattern_types": {
                "three_digit": {
                    "unique": {
                        "description": "Three unique digits (e.g., 567, 123, 471)",
                        "variations": [
                            "Straight order (613, 613, 613)",
                            "Box order (613, 361, 136)",
                            "Extended digits (316 → 331116)"
                        ]
                    },
                    "doubles": {
                        "description": "Two unique digits forming doubles (e.g., 244, 566, 133)"
                    }
                },
                "vtrac_patterns": {
                    "description": "V-TRAC related stable patterns in strings",
                    "examples": ["590 = 045 = 54455 (same V-TRAC)"],
                    "importance": "Very strong indicator for upcoming winning pattern",
                    "straight": "Patterns in same order (781 and 286 are same order V-TRAC)"
                }
            },
            "analysis_methods": {
                "vertical_analysis": {
                    "description": "Evaluate patterns vertically within R2/R4/R6/R8 boxes",
                    "focus": [
                        "Stable patterns (straight and box)",
                        "V-TRAC relationships",
                        "Pattern persistence"
                    ]
                },
                "horizontal_analysis": {
                    "description": "Track pattern progression across columns",
                    "focus": [
                        "Pattern survival as digits eliminate",
                        "End-string indicators (columns 3/2/1)",
                        "Three-digit pattern survival"
                    ]
                },
                "cross_section_analysis": {
                    "description": "Evaluate patterns across Midday/Evening/Combined",
                    "focus": [
                        "V-TRAC relationships",
                        "Pattern connections",
                        "Hot zone patterns"
                    ]
                }
            },
            "pattern_strength_indicators": [
                "Pattern stability in straight/box format",
                "V-TRAC relationships across sections",
                "Survival in end-string positions",
                "Repetition across multiple draws",
                "Presence in hot zones",
                "Cross-section relationships"
            ]
        }
    }
    
    # Save to JSON file
    output_file = os.path.join(output_dir, f"{state_name}_ai_format_{timestamp}.json")
    with open(output_file, "w") as f:
        json.dump(ai_friendly_data, f, indent=2)
    
    return output_file

def get_timestamp():
    """Generate timestamp for file naming"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def archive_data():
    """Archive current data with timestamp"""
    timestamp = get_timestamp()
    archive_dir = Path("data/archive")
    cleaned_dir = Path("data/cleaned")
    outputs_dir = Path("data/outputs")
    
    # Create archive subdirectory with timestamp
    archive_subdir = archive_dir / f"archive_{timestamp}"
    archive_subdir.mkdir(parents=True, exist_ok=True)
    
    # Archive cleaned data
    if cleaned_dir.exists():
        cleaned_archive = archive_subdir / "cleaned"
        shutil.copytree(cleaned_dir, cleaned_archive, dirs_exist_ok=True)
    
    # Archive outputs
    if outputs_dir.exists():
        outputs_archive = archive_subdir / "outputs"
        shutil.copytree(outputs_dir, outputs_archive, dirs_exist_ok=True)
    
    # Clear current data (but keep .gitkeep)
    for dir_path in [cleaned_dir, outputs_dir]:
        if dir_path.exists():
            for item in dir_path.glob("*"):
                if item.name != ".gitkeep":
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item)
    
    return archive_subdir

def export_data(state_data, state_name, section):
    """Export data with timestamps"""
    timestamp = get_timestamp()
    
    # Export to CSV
    csv_path = f"data/outputs/{state_name}_{section}_{timestamp}.csv"
    state_data.to_csv(csv_path, index=False)
    
    # Export to JSON
    json_path = f"data/ai_exports/{state_name}_ai_format_{timestamp}.json"
    state_data.to_json(json_path, orient='records')
    
    return csv_path, json_path

def main():
    st.set_page_config(
        page_title="Lottery Data Viewer",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Enhanced CSS for better table display
    st.markdown("""
        <style>
        .stDataFrame table {
            width: 100% !important;
        }
        .stDataFrame td {
            min-width: 150px !important;
            max-width: none !important;
            white-space: nowrap !important;
            font-family: monospace !important;
            padding: 8px !important;
            border: 1px solid #e1e4e8 !important;
        }
        div[data-testid="stDataFrame"] div[data-testid="stTable"] {
            width: 100% !important;
        }
        /* Section styling */
        .section-border-set3 {
            border: 2px solid #1f77b4 !important;
            background-color: rgba(31, 119, 180, 0.1) !important;
        }
        .section-border-set2 {
            border: 2px solid #2ca02c !important;
            background-color: rgba(44, 160, 44, 0.1) !important;
        }
        .section-border-set1-draw1 {
            border: 2px solid #ff7f0e !important;
            background-color: rgba(255, 127, 14, 0.1) !important;
        }
        /* Winner highlighting */
        .winner {
            color: red !important;
            font-weight: bold !important;
        }
        .related {
            color: blue !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Get project paths
    project_root = get_project_root()
    original_dir = os.path.join(project_root, "data", "original")
    cleaned_dir = os.path.join(project_root, "data", "cleaned")
    
    # File selection section
    st.header("Data Source Selection")
    upload_col, historical_col = st.columns(2)
    
    with upload_col:
        st.subheader("Upload New File")
        uploaded_file = st.file_uploader("Choose a Pick3StatsC4 Excel file", type=["xlsx", "xlsm"])
    
    with historical_col:
        st.subheader("Historical Files")
        historical_files = get_historical_files()
        if historical_files:
            file_dates = [datetime.strptime(f.stem.split('_')[-1], '%Y%m%d') if '_' in f.stem else None for f in historical_files]
            file_options = [f"{f.name} ({d.strftime('%Y-%m-%d') if d else 'No date'}" for f, d in zip(historical_files, file_dates)]
            selected_file = st.selectbox("Select historical file", file_options, index=None)
            if selected_file:
                file_index = file_options.index(selected_file)
                file_path = historical_files[file_index]
                uploaded_file = file_path
    
    if uploaded_file is None:
        st.warning("Please upload a Pick3StatsC4 Excel file or select one from historical files.")
        return

    # Save uploaded file to historical_files if it's new
    if hasattr(uploaded_file, 'name'):  # It's a new upload
        file_name = uploaded_file.name
        if "Pick3StatsC4" in file_name:
            save_path = Path("data/historical_files") / file_name
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            st.success(f"File saved to historical files: {file_name}")
    
    # State selection
    state = st.selectbox(
        "Select State to View",
        STATES,
        format_func=lambda x: x.replace("4", "")
    )
    
    # Load state data (using session state cache)
    cleaned_file = os.path.join(cleaned_dir, f"{state}_cleaned.xlsx")
    if not os.path.exists(cleaned_file):
        st.error(f"No cleaned data found for {state}")
        return
    
    if state not in st.session_state.processed_states:
        state_data = load_state_data(state, cleaned_file)
        if state_data:
            st.session_state.processed_states[state] = state_data
    
    state_data = st.session_state.processed_states.get(state)
    if not state_data:
        return
    
    # Get related combinations if winners are entered
    winning_combos = set()
    related_combos = set()
    midday_winner = None
    evening_winner = None
    
    if state_data.get("Midday", {}):
        midday_winner = state_data["Midday"].get("winning_combos", "")
        if midday_winner:
            _, winning_perms, related = find_vtrac_index_and_combos(midday_winner)
            winning_combos.update(winning_perms)
            related_combos.update(related)
    
    if state_data.get("Evening", {}):
        evening_winner = state_data["Evening"].get("winning_combos", "")
        if evening_winner:
            _, winning_perms, related = find_vtrac_index_and_combos(evening_winner)
            winning_combos.update(winning_perms)
            related_combos.update(related)
    
    # Add a button to log all tables for this state
    if st.button(f"Log All {state} Tables to Excel"):
        try:
            # Set up archive directory
            archive_dir = setup_logging_directories()
            
            # Get the DataFrames
            midday_df = build_section_table(state_data.get("Midday", {}))
            evening_df = build_section_table(state_data.get("Evening", {}))
            combined_df = build_section_table(state_data.get("Combined", {}))
            
            # Export to Excel
            filepath = export_state_tables(
                state,
                midday_df,
                evening_df,
                combined_df,
                archive_dir
            )
            
            st.success(f"Successfully saved tables to: {filepath}")
        except Exception as e:
            st.error(f"Error saving tables: {str(e)}")

    # Create three columns for Midday/Evening/Combined
    midday_col, evening_col, combined_col = st.columns(3)
    
    sections = {
        "Midday": (midday_col, state_data.get("Midday", {}), midday_winner),
        "Evening": (evening_col, state_data.get("Evening", {}), evening_winner),
        "Combined": (combined_col, state_data.get("Combined", {}), None)
    }
    
    for section_name, (column, section_data, winner) in sections.items():
        with column:
            st.markdown(f"### {section_name}")
            
            if section_data:
                # Build tables (cached)
                combined_df, r2_df = build_tables(section_data)
                
                if combined_df is None or r2_df is None:
                    continue
                
                # Style function for highlighting
                def style_function(val):
                    if not isinstance(val, str) or val in ['N/A', 'nan']:
                        return ''
                    if any(combo in val for combo in winning_combos):
                        return 'color: red; font-weight: bold'
                    if any(combo in val for combo in related_combos):
                        return 'color: blue'
                    return ''
                
                # Apply section styling and highlighting
                def style_df(df):
                    styled = df.style
                    
                    # Section background colors
                    styled = styled.apply(lambda x: [
                        'background-color: rgba(31, 119, 180, 0.1)' if x['Set'] == 'Set3'
                        else 'background-color: rgba(44, 160, 44, 0.1)' if x['Set'] == 'Set2'
                        else 'background-color: rgba(255, 127, 14, 0.1)' if (x['Set'] == 'Set1' and x['Draw'] == 'Draw1')
                        else '' for _ in range(len(x))
                    ], axis=1)
                    
                    # Winner highlighting
                    if winning_combos:
                        for col in df.columns:
                            if col not in ["Set", "Draw", "RowType"]:
                                styled = styled.applymap(style_function, subset=[col])
                    
                    return styled.set_properties(**{
                        'text-align': 'center',
                        'font-family': 'monospace',
                        'white-space': 'nowrap',
                        'padding': '8px'
                    })
                
                # Style and display tables
                combined_df_styled = style_df(combined_df)
                r2_df_styled = style_df(r2_df)
                
                st.markdown("#### Combined Table")
                st.dataframe(
                    combined_df_styled,
                    height=1800,  # Show all 38 rows
                    use_container_width=True
                )
                
                st.markdown("#### R2-only Table")
                st.dataframe(
                    r2_df_styled,
                    height=400,
                    use_container_width=True
                )
                
                # Download buttons
                csv_combined = combined_df.to_csv(index=False)
                csv_r2 = r2_df.to_csv(index=False)
                
                st.download_button(
                    f"Download {section_name} Combined Table",
                    csv_combined,
                    f"{state}_{section_name}_combined.csv",
                    "text/csv",
                    key=f'download-combined-{section_name.lower()}'
                )
                st.download_button(
                    f"Download {section_name} R2-only Table",
                    csv_r2,
                    f"{state}_{section_name}_r2.csv",
                    "text/csv",
                    key=f'download-r2-{section_name.lower()}'
                )

                # After displaying tables, add logging button
                if st.button(f"Log {state} Results", key=f"log-{section_name.lower()}"):
                    try:
                        # Prepare data for export
                        tables_data = {
                            'Midday': st.session_state.processed_states[state].get('Midday', {}).get('combined_table'),
                            'Evening': st.session_state.processed_states[state].get('Evening', {}).get('combined_table'),
                            'Combined': st.session_state.processed_states[state].get('Combined', {}).get('combined_table')
                        }
                        
                        # Set up archive directory
                        archive_dir = setup_logging_directories()
                        
                        # Export to Excel
                        filepath = export_state_tables(
                            state,
                            tables_data,
                            winning_combos,
                            related_combos,
                            archive_dir
                        )
                        
                        st.success(f"Successfully logged results to: {filepath}")
                    except Exception as e:
                        st.error(f"Error logging results: {str(e)}")

    # Add export all tables button
    if st.button("Export All Tables (Midday/Evening/Combined)"):
        try:
            output_file = export_all_tables_to_csv(state_data, state)
            st.success(f"All tables exported to: {output_file}")
        except Exception as e:
            st.error(f"Error exporting tables: {str(e)}")

    # Add export for AI analysis button
    if st.button("Export for AI Analysis (JSON)"):
        try:
            output_file = export_to_json(state_data, state)
            st.success(f"AI-friendly JSON exported to: {output_file}")
        except Exception as e:
            st.error(f"Error exporting JSON: {str(e)}")

    # Add Log All button in sidebar
    with st.sidebar:
        st.header("Data Management")
        if st.button("Log All Data"):
            try:
                archive_path = archive_data()
                st.success(f"All data archived to: {archive_path}")
                st.info("Data folders cleared for new processing")
            except Exception as e:
                st.error(f"Error archiving data: {str(e)}")

if __name__ == "__main__":
    main() 