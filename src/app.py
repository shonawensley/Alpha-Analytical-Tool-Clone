import sys
import pathlib
import streamlit as st
from pathlib import Path
from core.module_b_digit_reduction import run_digit_reduction
from utils.path_handler import get_tables_output_dir

# --- path hook ---------------------------------------------------------
SRC_DIR = pathlib.Path(__file__).resolve().parent     # .../src
PROJECT_ROOT = SRC_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
# ----------------------------------------------------------------------

# ❶ Page config FIRST (before every other st.*)
st.set_page_config(page_title="Alpha-Final Analytical Tool",
                   page_icon="🚀", layout="wide")


def main():
    """
    Main function to run the Alpha-Final Streamlit app.
    This app will have a two-level navigation: State selection and Tool selection.
    """
    st.sidebar.title("Navigation")
    
    # First level: State selector
    states_list = [
        "Connecticut4", "Delaware4", "Florida4", "Georgia4", "Indiana4",
        "Michigan4", "NewJersey4", "NewYork4", "NorthCarolina4", "Ohio4",
        "Ontario4", "Pennsylvania4", "Texas4", "Virginia4", "WestVirginia4"
    ]
    
    selected_state = st.sidebar.selectbox(
        "State ▼",
        states_list,
        index=0
    )
    
    # Second level: Tool selector  
    selected_tool = st.sidebar.selectbox(
        "Tool ▼",
        [
            "V-TRAC Analyzer",
            "Stable Pattern Extractor", 
            "Digit Reduction",
            "Auxiliary Tools",
            "Hot Zones (Stub)",
            "Control Center",
        ],
        index=0
    )

    if selected_tool == "V-TRAC Analyzer":
        show_vtrac_page(selected_state)
        
    elif selected_tool == "Stable Pattern Extractor":
        show_stable_pattern_page(selected_state)
        
    elif selected_tool == "Digit Reduction":
        show_digit_reduction_page(selected_state)
        
    elif selected_tool == "Auxiliary Tools":
        show_aux_page(selected_state)
        
    elif selected_tool == "Hot Zones (Stub)":
        show_hot_zones_page(selected_state)
        
    elif selected_tool == "Control Center":
        show_control_center_page()


def show_vtrac_page(state: str) -> None:
    """Render the V-TRAC Analyzer page."""
    from core import module_c_vtrac  # lazy import
    st.title(f"V-TRAC Analyzer - {state}")
    st.info(f"Running V-TRAC analysis for {state}")
    module_c_vtrac.main()


def show_stable_pattern_page(state: str) -> None:
    """Render the Stable Pattern Extractor page."""
    from core import stable_pattern_extractor as stable
    from utils import path_handler as ph

    st.title(f"Stable Pattern Extractor - {state}")

    # --- User inputs ---------------------------------------------------
    min_occ = st.number_input("Minimum occurrences (min_occ)", min_value=1, max_value=10, value=3, step=1)

    if st.button("Run Stable Pattern Extraction"):
        tables_dir = ph.get_state_tables_dir(state)
        out_dir    = ph.get_analysis_dir("patterns", state)

        df, html_f, csv_f = stable.run_stable_pattern_extraction(
            state=state,
            tables_path=tables_dir,
            out_path=out_dir,
            min_occ=min_occ,
        )

        if df.empty:
            st.warning("No patterns found – verify tables or adjust parameters.")
        else:
            st.success(f"{len(df)} patterns extracted.")
            st.dataframe(df.head(50), height=360)

            if csv_f:
                st.markdown(f"[⬇ Download CSV]({csv_f})")

            if html_f and Path(html_f).exists():
                with open(html_f, "r", encoding="utf-8") as fh:
                    st.components.v1.html(fh.read(), height=600, scrolling=True)


def show_hot_zones_page(state: str) -> None:
    """Render the Hot Zones Stub page."""
    st.title(f"Hot Zones - {state}")
    st.write("Hot-Zones module is a placeholder.")


def show_control_center_page() -> None:
    """Render the Control Center page."""
    st.title("Control Center")
    st.write("Cross-State Analysis Dashboard")
    
    # Add cross-state doubles table from legacy combined_view.py functionality
    try:
        from scripts.auxiliary.combined_view import generate_combined_analysis
        st.info("Loading cross-state analysis...")
        
        # Show combined analysis across all states
        st.subheader("Cross-State Doubles Analysis")
        st.write("This shows doubles patterns across all available states.")
        
        # Placeholder for actual combined view functionality
        st.warning("Combined view functionality to be implemented.")
        
    except ImportError:
        st.warning("Combined view module not available. Cross-state analysis disabled.")


def show_aux_page(state: str) -> None:
    """Render the Auxiliary Tools page."""
    import streamlit as st
    import pandas as pd
    from modules.module_d_auxiliary_tools.integration import run_aux_tools
    from modules.module_d_auxiliary_tools.refactored.boxed_vtrac import render_boxed_vtrac_html
    
    st.title(f"Auxiliary Tools - {state}")
    st.write(f"Advanced lottery analysis tools for {state}")
    
    # Add caching for performance
    @st.cache_data(ttl=1 * 60 * 60)  # Cache for 1 hour
    def cached_aux_analysis(state_name: str):
        return run_aux_tools(state_name)
    
    if st.button("Run Auxiliary Tools Analysis", type="primary"):
        with st.spinner(f"Running auxiliary analysis for {state}..."):
            try:
                results = cached_aux_analysis(state)
                
                # Display Boxed V-TRAC Table (HTML render for colors/underlines)
                st.subheader("📊 Boxed V-TRAC Table")
                boxed_vtrac = results["boxed_vtrac"]
                if not boxed_vtrac.empty:
                    st.write("35x8 V‑TRAC index table with legacy color/underline styling")
                    # Render via HTML component to preserve <span> styling
                    st.components.v1.html(render_boxed_vtrac_html(boxed_vtrac), height=650, scrolling=True)
                    # Add download option (CSV from the underlying DataFrame)
                    st.download_button(
                        "Download V-TRAC Table CSV",
                        boxed_vtrac.to_csv(index=False),
                        f"{state}_boxed_vtrac.csv",
                        "text/csv"
                    )
                else:
                    st.warning("No V-TRAC data available for this state.")
                
                # Display Overdue Pairs Analysis
                st.subheader("🔥 Overdue Pairs Analysis")
                overdue_pairs = results["overdue_pairs"]
                
                if not overdue_pairs.empty:
                    # Compact top-5 repeating pairs (like legacy)
                    st.caption("Top 5 Most Overdue Repeating Pairs")
                    top5 = (
                        overdue_pairs[overdue_pairs['Type'] == 'Repeating']
                        .sort_values('Draws_Overdue', ascending=False)
                        .head(5)
                    )
                    for _, row in top5.iterrows():
                        color = row.get('Color', '')
                        pair = row['Pair']
                        overdue = row['Draws_Overdue']
                        if color == 'red':
                            st.markdown(f'<span style="color: red; font-weight: bold">{pair} - {overdue} draws overdue</span>', unsafe_allow_html=True)
                        elif color == 'blue':
                            st.markdown(f'<span style="color: blue; font-weight: bold">{pair} - {overdue} draws overdue</span>', unsafe_allow_html=True)
                        elif color == 'purple':
                            st.markdown(f'<span style="color: purple; font-weight: bold">{pair} - {overdue} draws overdue</span>', unsafe_allow_html=True)
                        else:
                            st.write(f"{pair} - {overdue} draws overdue")
                    # Detailed table below for reference
                    st.dataframe(overdue_pairs, use_container_width=True)
                else:
                    st.info("No overdue pairs data available.")

                # Doubles tracking (per-state) will be part of Control Center aggregation
                st.subheader("🎯 Doubles Tracker")
                st.info("Cross-state doubles (combos) ranking will appear in Control Center.")
                
                # Display Compound Indicators (Placeholder)
                if "compound_indicators" in results:
                    compound_indicators = results["compound_indicators"]
                    if not compound_indicators.empty:
                        st.subheader("📈 Compound Indicators (Preview)")
                        st.write("Future compound scoring indicators:")
                        st.dataframe(compound_indicators, use_container_width=True)
                
                st.success(f"✅ Auxiliary tools analysis completed for {state}")
                
            except Exception as e:
                st.error(f"Error running auxiliary analysis: {str(e)}")
                st.info("Please ensure the state data files are available in data/cleaned/")
    
    else:
        st.info("Click the button above to run auxiliary tools analysis.")
        
        # Show available states info
        from modules.module_d_auxiliary_tools.integration import get_available_states
        available_states = get_available_states()
        
        if available_states:
            st.subheader("Available States")
            st.write(f"Data available for {len(available_states)} states:")
            cols = st.columns(3)
            for i, state_name in enumerate(available_states):
                with cols[i % 3]:
                    st.write(f"• {state_name}")
        else:
            st.warning("No state data files found. Please ensure cleaned data is available.")


def show_digit_reduction_page(state: str) -> None:
    """Render the Digit-Reduction Streamlit tab."""
    st.title(f"Digit Reduction - {state}")

    tables_root = Path(get_tables_output_dir())
    if not tables_root.exists():
        st.error("No processed tables found. Run the data pipeline first.")
        return

    # Check if the specific state directory exists
    state_path = tables_root / state
    if not state_path.exists():
        st.error(f"No tables found for {state}. Available states: {[p.name for p in tables_root.iterdir() if p.is_dir()]}")
        return

    if st.button("Run Digit Reduction"):
        with st.spinner(f"Running Digit Reduction for {state}..."):
            df, html_path, csv_path = run_digit_reduction(
                state,
                tables_path=state_path,
            )

        if df.empty:
            st.warning("Digit Reduction produced no output – verify tables exist.")
            return

        st.success(f"{len(df)} reductions extracted for {state}")
        st.dataframe(df, use_container_width=True)

        if csv_path:
            st.download_button(
                "Download CSV",
                Path(csv_path).read_bytes(),
                file_name=Path(csv_path).name,
            )

        if html_path and Path(html_path).exists():
            with open(html_path, "r", encoding="utf-8") as fh:
                st.components.v1.html(fh.read(), height=800, scrolling=True)


if __name__ == "__main__":
    main() 