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
    This app will have a tabbed interface to access the different analysis modules.
    """
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox(
        "Choose a module:",
        [
            "V-TRAC Analyzer",
            "Stable Pattern Extractor",
            "Digit Reduction",
            "Hot Zones (Stub)",
            "Control Center",
        ]
    )

    if app_mode == "V-TRAC Analyzer":
        from core import module_c_vtrac  # lazy import
        st.title("V-TRAC Analyzer")
        module_c_vtrac.main()

    elif app_mode == "Stable Pattern Extractor":
        from core import stable_pattern_extractor as stable
        from utils import path_handler as ph

        st.title("Stable Pattern Extractor")

        # --- User inputs ---------------------------------------------------
        state = st.text_input("State name (e.g. Connecticut4)", value="Connecticut4")
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

    elif app_mode == "Digit Reduction":
        show_digit_reduction_page()

    elif app_mode == "Hot Zones (Stub)":
        st.title("Hot Zones")
        st.write("Hot-Zones module is a placeholder.")

    elif app_mode == "Control Center":
        st.title("Control Center")
        st.write("Aggregator / dashboard goes here.")


def show_digit_reduction_page() -> None:
    """Render the Digit-Reduction Streamlit tab."""
    st.header("Digit Reduction")

    tables_root = Path(get_tables_output_dir())
    if not tables_root.exists():
        st.error("No processed tables found. Run the data pipeline first.")
        return

    states = sorted([p.name for p in tables_root.iterdir() if p.is_dir()])
    if not states:
        st.error("No state folders detected in tables directory.")
        return

    state = st.selectbox("Select State", states)

    if st.button("Run Digit Reduction"):
        with st.spinner("Running Digit Reduction …"):
            df, html_path, csv_path = run_digit_reduction(
                state,
                tables_path=tables_root / state,
            )

        if df.empty:
            st.warning("Digit Reduction produced no output – verify tables exist.")
            return

        st.success(f"{len(df)} reductions extracted")
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