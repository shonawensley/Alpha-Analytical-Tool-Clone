import sys
import pathlib
import streamlit as st

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
        from scripts.core import stable_pattern_analyzer_standalone as stable
        st.title("Stable Pattern Extractor")
        stable.main()

    elif app_mode == "Digit Reduction":
        from core import module_b_digit_reduction as reducer
        st.title("Digit Reduction")
        reducer.main()

    elif app_mode == "Hot Zones (Stub)":
        st.title("Hot Zones")
        st.write("Hot-Zones module is a placeholder.")

    elif app_mode == "Control Center":
        st.title("Control Center")
        st.write("Aggregator / dashboard goes here.")


if __name__ == "__main__":
    main() 