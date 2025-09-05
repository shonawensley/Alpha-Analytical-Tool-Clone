import sys
import os
import pathlib
import streamlit as st
from contextlib import contextmanager
from pathlib import Path
from core.module_b_digit_reduction import run_digit_reduction
from utils.path_handler import get_tables_output_dir

# --- path hook ---------------------------------------------------------
SRC_DIR = pathlib.Path(__file__).resolve().parent     # .../src
PROJECT_ROOT = SRC_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
# ----------------------------------------------------------------------
 

# --- AUX working modules path (staged, isolated) -----------------------
from pathlib import Path
_AUX_WORKING_ROOT = os.path.normpath(os.path.join(Path(__file__).resolve().parent.parent, "scripts", "auxiliary", "working"))
if os.path.isdir(_AUX_WORKING_ROOT) and _AUX_WORKING_ROOT not in sys.path:
    # Insert the parent folder so absolute imports like `modules.parse_excel` work
    sys.path.insert(0, _AUX_WORKING_ROOT)
# ----------------------------------------------------------------------
from importlib.util import spec_from_file_location, module_from_spec

def _load_project_module(dotted_name: str, rel_file: str):
    """Load a module by absolute file path from the project root.
    This bypasses any top-level package name collisions on sys.path.
    """
    file_path = Path(PROJECT_ROOT) / rel_file
    if not file_path.exists():
        raise FileNotFoundError(f"Expected module at {file_path}")
    spec = spec_from_file_location(dotted_name, str(file_path))
    mod = module_from_spec(spec)  # type: ignore[arg-type]
    assert spec and spec.loader, f"Could not load spec for {file_path}"
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _load_blackapple_real():
    return _load_project_module("project_blackapple", "modules/blackapple.py")


def _load_aux_loaders_real():
    return _load_project_module("project_aux_loaders", "modules/aux_loaders.py")

# Helpers for rendering working Vâ€‘TRAC output (used only on Aux page)
def _severity(cls: str) -> int:
    return {"blue": 3, "red": 2, "purple": 1}.get(cls or "", 0)


def _color_digit_pairs(combo: str, pair_status: dict) -> str:
    if not combo or len(combo) != 3:
        return combo
    d1, d2, d3 = combo[0], combo[1], combo[2]
    p12 = ''.join(sorted(d1 + d2))
    p23 = ''.join(sorted(d2 + d3))
    p13 = ''.join(sorted(d1 + d3))
    c1 = pair_status.get(p12, "")
    if _severity(pair_status.get(p13, "")) > _severity(c1):
        c1 = pair_status.get(p13, "")
    c2 = pair_status.get(p12, "")
    if _severity(pair_status.get(p23, "")) > _severity(c2):
        c2 = pair_status.get(p23, "")
    c3 = pair_status.get(p13, "")
    if _severity(pair_status.get(p23, "")) > _severity(c3):
        c3 = pair_status.get(p23, "")
    s1 = f'<span class="digit {c1}">{d1}</span>' if c1 else f'<span class="digit">{d1}</span>'
    s2 = f'<span class="digit {c2}">{d2}</span>' if c2 else f'<span class="digit">{d2}</span>'
    s3 = f'<span class="digit {c3}">{d3}</span>' if c3 else f'<span class="digit">{d3}</span>'
    return s1 + s2 + s3


def _format_combo(combo: str, status_dict: dict, pair_status: dict) -> str:
    if combo not in status_dict:
        return _color_digit_pairs(combo, pair_status)
    combo_status = status_dict[combo]
    classes = []
    if combo_status.get("shape_red_circle"):
        classes.append("shape-red-circle")
    elif combo_status.get("shape_blue_square"):
        classes.append("shape-blue-square")
    inner = _color_digit_pairs(combo, pair_status)
    if not classes:
        return inner
    return f'<span class="{" ".join(classes)}">{inner}</span>'

# --- Helpers: robust draw loading without touching other tools ----------
def _normalize_state_name(state_name: str) -> str:
    import re
    # Drop trailing digits like "Connecticut4" -> "Connecticut"
    return re.sub(r"\d+$", "", state_name or "").strip().replace("_", " ")


def _load_draws_from_csv_candidates(state_name: str):
    import pandas as _pd
    base = _normalize_state_name(state_name)
    fn = f"{base.replace(' ', '_')}_draws.csv"
    candidates = [
        os.path.normpath("data/cleaned"),
        os.path.normpath("data/processed/draws"),  # auxiliary extractor output
    ]
    for d in candidates:
        path = os.path.join(d, fn)
        if os.path.exists(path):
            try:
                df = _pd.read_csv(path)
                draws = [str(x).zfill(3) for x in df["Draw"].dropna().astype(int).astype(str).tolist()]
                if draws:
                    return draws
            except Exception:
                continue
    return []

# --- Project-first import context and local sums helpers ----------------
@contextmanager
def _project_first_imports():
    """Temporarily place PROJECT_ROOT at the front of sys.path so imports
    prefer the project's `modules` tree over the staged working copy.
    """
    _old = list(sys.path)
    try:
        if str(PROJECT_ROOT) in sys.path:
            try:
                sys.path.remove(str(PROJECT_ROOT))
            except ValueError:
                pass
        sys.path.insert(0, str(PROJECT_ROOT))
        yield
    finally:
        sys.path[:] = _old

# Prefer PROJECT_ROOT/modules for non-colliding imports of Sums package
MODULES_DIR = os.path.join(PROJECT_ROOT, "modules")

@contextmanager
def _project_modules_first():
    old = list(sys.path)
    try:
        if MODULES_DIR in sys.path:
            try:
                sys.path.remove(MODULES_DIR)
            except ValueError:
                pass
        sys.path.insert(0, MODULES_DIR)
        yield
    finally:
        sys.path[:] = old

@contextmanager
def _project_blackapple_ctx():
    """Ensure project modules resolve first for Blackapple and avoid staged 'modules' shadow.
    Temporarily prepend PROJECT_ROOT to sys.path and evict any existing 'modules' binding
    so imports of 'modules.blackapple' resolve to the project's modules package.
    """
    old_path = list(sys.path)
    old_modules = sys.modules.get('modules')
    try:
        if str(PROJECT_ROOT) not in sys.path:
            sys.path.insert(0, str(PROJECT_ROOT))
        try:
            sys.modules.pop('modules')
        except KeyError:
            pass
        yield
    finally:
        # Restore prior 'modules' binding
        if old_modules is not None:
            sys.modules['modules'] = old_modules
        else:
            try:
                sys.modules.pop('modules')
            except KeyError:
                pass
        sys.path[:] = old_path
def _sum3(d: str) -> int:
    return sum(int(ch) for ch in d) if d and len(d) == 3 and d.isdigit() else 0

def _root(n: int) -> int:
    return 0 if n <= 0 else 1 + ((n - 1) % 9)

def _root_sum3(d: str) -> int:
    return _root(_sum3(d))

# --- Sums badge helpers (local-only; no imports) -----------------------
def _sums_badge_for(combo: str, sums_stats: dict) -> str:
    try:
        if not combo or len(combo) != 3 or not combo.isdigit():
            return ""
        s = _sum3(combo)
        r = _root_sum3(combo)
        by_sum = sums_stats.get("by_sum", {}) if isinstance(sums_stats, dict) else {}
        by_root = sums_stats.get("by_root_sum", {}) if isinstance(sums_stats, dict) else {}
        sflags = (by_sum.get(s) or {}).get("flags", {})
        rflags = (by_root.get(r) or {}).get("flags", {})

        def tag(label: str, flags: dict) -> str:
            parts = []
            if flags.get("blue"):
                parts.append(f'<span class="blue">{label}</span>')
            if flags.get("red"):
                parts.append(f'<span class="red">{label}</span>')
            if flags.get("purple"):
                parts.append('<span class="purple">â€¢</span>')
            return " ".join(parts)

        s_tag = tag(f"S{s}", sflags)
        r_tag = tag(f"R{r}", rflags)
        if not s_tag and not r_tag:
            return ""
        both = " ".join(x for x in (s_tag, r_tag) if x)
        return f' <span style="font-size:0.85em;opacity:.85">[{both}]</span>'
    except Exception:
        return ""

# â¶ Page config FIRST (before every other st.*)
st.set_page_config(page_title="Alpha-Final Analytical Tool",
                   page_icon="ðŸš€", layout="wide")

# Debug: show which file is running (safe to remove later)
def main():
    """
    Main function to run the Alpha-Final Streamlit app.
    This app will have a two-level navigation: State selection and Tool selection.
    """
    st.sidebar.title("Navigation")
    # Debug sidebar info after context is ready
    try:
        st.sidebar.caption(f"ENTRY: {os.path.relpath(__file__)}")
    except Exception:
        pass
    
    # First level: State selector
    states_list = [
        "Connecticut4", "Delaware4", "Florida4", "Georgia4", "Indiana4",
        "Michigan4", "NewJersey4", "NewYork4", "NorthCarolina4", "Ohio4",
        "Ontario4", "Pennsylvania4", "Texas4", "Virginia4", "WestVirginia4"
    ]
    
    selected_state = st.sidebar.selectbox(
        "State â–¼",
        states_list,
        index=0
    )
    
    # Second level: Tool selector  
    selected_tool = st.sidebar.selectbox(
        "Tool â–¼",
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
    # Dev: System Health (V-TRAC)
    try:
        show_dev_v = st.sidebar.checkbox("Show Dev Health", value=False, key="dev_health_vtrac")
    except Exception:
        show_dev_v = False
    if show_dev_v:
        import os, sys as _sys
        with st.expander("System Health (V-TRAC)"):
            st.caption("cwd: " + os.getcwd())
            st.caption("python: " + _sys.executable)
            try:
                import core.module_c_vtrac as _v
                st.caption("V-TRAC module: " + str(getattr(_v, "__file__", "unknown")))
            except Exception as _se:
                st.caption("V-TRAC module: unavailable: " + str(_se))


def show_stable_pattern_page(state: str) -> None:
    """Render the Stable Pattern Extractor page."""
    from core import stable_pattern_extractor as stable
    from utils import path_handler as ph

    st.title(f"Stable Pattern Extractor - {state}")

    # Dev: System Health (Stable Pattern)
    try:
        show_dev_s = st.sidebar.checkbox("Show Dev Health", value=False, key="dev_health_stable")
    except Exception:
        show_dev_s = False
    if show_dev_s:
        import os, sys as _sys
        from utils import path_handler as ph
        from pathlib import Path as _P
        with st.expander("System Health (Stable)"):
            st.caption("cwd: " + os.getcwd())
            st.caption("python: " + _sys.executable)
            try:
                from core import stable_pattern_extractor as _stable
                st.caption("Stable module: " + str(getattr(_stable, "__file__", "unknown")))
            except Exception as _se:
                st.caption("Stable module: unavailable: " + str(_se))
            try:
                tdir = ph.get_state_tables_dir(state)
                st.caption("tables_dir: " + str(tdir) + " (exists=" + str(_P(tdir).exists()) + ")")
            except Exception:
                pass
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
            st.warning("No patterns found â€“ verify tables or adjust parameters.")
        else:
            st.success(f"{len(df)} patterns extracted.")
            st.dataframe(df.head(50), height=360)

            if csv_f:
                st.markdown(f"[â¬‡ Download CSV]({csv_f})")

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
    
    try:
        from modules.analyze_pairs import get_doubles_history
        import pandas as _pd
        from pathlib import Path as _Path

        cleaned_dir = _Path("data/cleaned")
        if not cleaned_dir.exists():
            st.warning("No cleaned data found in data/cleaned.")
            return

            try:
                show_dev_d = st.sidebar.checkbox("Show Dev Health", value=False, key="dev_health_dr")
            except Exception:
                show_dev_d = False
            if show_dev_d:
                import os, sys as _sys
                with st.expander("System Health (Digit Reduction)"):
                    st.caption("cwd: " + os.getcwd())
                    st.caption("python: " + _sys.executable)
                    try:
                        from core.module_b_digit_reduction import run_digit_reduction as _rdr
                        import inspect as _insp
                        st.caption("DR module: " + str(getattr(_rdr, "__module__", "unknown")))
                    except Exception as _se:
                        st.caption("DR module: unavailable: " + str(_se))
                    try:
                        st.caption("tables_root: " + str(tables_root) + " (exists=" + str(tables_root.exists()) + ")")
                    except Exception:
                        pass
                st.error("No processed tables found. Run the data pipeline first.")
                return
        
            # Check if the specific state directory exists
            state_path = tables_root / state
            if not state_path.exists():
                st.error(f"No tables found for {state}. Available states: {[p.name for p in tables_root.iterdir() if p.is_dir()]}")
                return
        
        def _compute_combined():
            state_to_draws = {}
            for csv_path in cleaned_dir.glob("*_draws.csv"):
                try:
                    df = _pd.read_csv(csv_path)
                    draws = [str(x).zfill(3) for x in df["Draw"].dropna().astype(int).astype(str).tolist()]
                    state_name = csv_path.stem.replace("_draws", "").replace("_", " ")
                    if draws:
                        state_to_draws[state_name] = draws
                except Exception:
                    continue
            if not state_to_draws:
                return _pd.DataFrame()
            doubles = get_doubles_history(state_to_draws)
            rows = []
            for state, draws in state_to_draws.items():
                ds = int(doubles.get(state, 0)) if state in doubles else 0
                latest_double = draws[ds] if 0 <= ds < len(draws) else "None"
                rows.append({
                    "State": state,
                    "Draws Since Last Double": ds,
                    "Latest Double": latest_double,
                    "Total Draws": len(draws),
                })
            df = _pd.DataFrame(rows)
            if not df.empty:
                df = df.sort_values(["Draws Since Last Double", "State"], ascending=[False, True])
            return df

        if st.button("Refresh Combined Table"):
            st.session_state.pop("combined_doubles_df", None)

        df = st.session_state.get("combined_doubles_df")
        if df is None or df.empty:
            df = _compute_combined()
            if df is not None and not df.empty:
                st.session_state["combined_doubles_df"] = df
        if df is None or df.empty:
            st.warning("No state draw files found in data/cleaned.")
            return

        st.subheader("States Ranked by Draws Since Last Double")
        st.dataframe(df, use_container_width=True)

        # --- Blackapple Alerts (All States) ---
        try:
            _ba = _load_blackapple_real()
            analyze_blackapple = _ba.analyze_blackapple
            ba_status_label = _ba.ba_status_label
            _aux = _load_aux_loaders_real()
            load_state_draws = _aux.load_state_draws

            rows_ba = []
            for csv_path in cleaned_dir.glob("*_draws.csv"):
                try:
                    state_label = csv_path.stem.replace("_draws", "").replace("_", " ")
                    dr, src = load_state_draws(state_label)
                    if not dr:
                        continue
                    ba = analyze_blackapple(dr)
                    status = ba_status_label(ba.get("score", 0))
                    tr = ba.get("triggers", {})
                    tparts = []
                    if tr.get("mirror"):
                        tparts.append("Mirror")
                    roots = tr.get("root_due", [])
                    if roots:
                        tparts.append("Root " + "/".join(map(str, roots)))
                    pat = tr.get("pattern", {})
                    if pat.get("extreme_due"):
                        tparts.append("SSS/TTT")
                    if pat.get("mixed_due"):
                        tparts.append("SST/STS/TSS")
                    flt = tr.get("floating", [])
                    if flt:
                        tparts.append("Float " + "".join(flt))
                    rows_ba.append({
                        "State": state_label,
                        "BA-Score": ba.get("score", 0),
                        "Status": status,
                        "Triggers": ", ".join(tparts),
                        "#Candidates": len(ba.get("candidates", [])),
                        "Examples": " ".join([c.get("combo", "") for c in ba.get("candidates", [])[:3]]),
                    })
                except Exception:
                    continue

            if rows_ba:
                df_ba = _pd.DataFrame(rows_ba).sort_values(["BA-Score", "#Candidates"], ascending=[False, False]).reset_index(drop=True)
                st.subheader("Blackapple Alerts (All States)")
                st.dataframe(df_ba, use_container_width=True)
        except Exception as _e:
            st.caption(f"Combined BA table unavailable: {_e}")
        # Optional: per-state full candidates view with tags
        try:
            for row in rows_ba:
                state_label = row.get("State") or row.get("state")
                if not state_label:
                    continue
                with st.expander(f"{state_label} — View all candidates"):
                    # Re-run BA for this state to list all candidates
                    dr, _src = load_state_draws(state_label)
                    if not dr:
                        st.caption("No draws available.")
                        continue
                    ba_full = analyze_blackapple(dr)
                    cands = ba_full.get("candidates", [])
                    if not cands:
                        st.caption("No candidates found.")
                        continue
                    import pandas as _pd
                    rows_detail = []
                    for c in cands:
                        tags = c.get("tags", [])
                        if isinstance(tags, set):
                            tags = sorted(tags)
                        rows_detail.append({
                            "Combo": c.get("combo", ""),
                            "Score": c.get("score", 0),
                            "Tags": " ".join(tags),
                        })
                    st.dataframe(_pd.DataFrame(rows_detail), use_container_width=True)
        except Exception:
            pass
            st.caption(f"Combined BA table unavailable: {_e}")
    except Exception as e:
        # System Health (development)
        try:
            import os, sys as _sys
            with st.expander("System Health"):
                st.caption(f"cwd: {os.getcwd()}")
                st.caption(f"python: {_sys.executable}")
                try:
                    _ba = _load_blackapple_real()
                    st.caption(f"BA module: {getattr(_ba, '__file__', 'unknown')}")
                except Exception as _se:
                    st.caption(f"BA module: unavailable: {_se}")
        except Exception:
            pass
        st.warning(f"Combined view unavailable: {e}")
def show_aux_page(state: str) -> None:
    """Render the Auxiliary Tools page."""
    import streamlit as st
    import pandas as pd
    # Loader from legacy extractor (safe to reuse just for CSV reads)
    try:
        from modules.module_d_auxiliary_tools.refactored.extractor import extract_draw_list
    except Exception:
        extract_draw_list = None

    # Working modules (staged copy) â€“ used only inside Aux page
    _AUX_WORKING_AVAILABLE = False
    try:
        from modules.analyze_pairs import (
            calculate_overdue_pairs,
            get_top_overdue_repeating_pairs,
            get_vtrac_statuses,
            get_doubles_history,
            COLOR_LATE, COLOR_VERY_LATE, COLOR_PENDING,
        )
        from modules.vtrac_reference import VTRAC_DISPLAY, get_vtrac_index
        _AUX_WORKING_AVAILABLE = True
    except Exception:
        _AUX_WORKING_AVAILABLE = False
    
    st.title(f"Auxiliary Tools - {state}")
    st.write(f"Advanced lottery analysis tools for {state}")
    
    # Dev: System Health (toggle in sidebar)
    try:
        show_dev = st.sidebar.checkbox("Show Dev Health", value=False, key="dev_health_aux")
    except Exception:
        show_dev = False
    if show_dev:
        import os, sys as _sys
        with st.expander("System Health (Aux)"):
            st.caption("cwd: " + os.getcwd())
            st.caption("python: " + _sys.executable)
            try:
                _ba = _load_blackapple_real()
                st.caption("BA module: " + str(getattr(_ba, "__file__", "unknown")))
            except Exception as _se:
                st.caption("BA module: unavailable: " + str(_se))
            try:
                _aux = _load_aux_loaders_real()
                load_state_draws = getattr(_aux, "load_state_draws", None)
                if callable(load_state_draws):
                    dr, src = load_state_draws(state)
                    st.caption("draws CSV: " + str(src) + " (" + str(len(dr) if isinstance(dr, list) else 0) + ")")
            except Exception:
                pass
    # Basic styles for working renderer
    st.markdown("""
    <style>
        .red { color: red; font-weight: bold; }
        .blue { color: blue; font-weight: bold; }
        .purple { color: purple; font-weight: bold; }
        .shape-red-circle { border: 2px solid red; border-radius: 8px; padding: 1px 3px; }
        .shape-blue-square { border: 2px solid blue; padding: 1px 3px; }
        .digit { padding: 0 1px; font-weight: 600; }
        .row-green { background-color: rgba(0, 200, 0, 0.08); display: block; padding: 2px 4px; min-height: 1.2em; }
        .row-red { background-color: rgba(255, 0, 0, 0.08); display: block; padding: 2px 4px; min-height: 1.2em; }
        .rank-badge { font-size: 0.8em; float: right; opacity: 0.7; }
    </style>
    """, unsafe_allow_html=True)

    # Add caching for performance (working logic)
    @st.cache_data(ttl=30 * 60)
    def cached_aux_analysis(state_name: str):
        if not (_AUX_WORKING_AVAILABLE):
            return None
        # 1) Try CSVs first (selfâ€‘contained; does not touch other tools)
        draws = _load_draws_from_csv_candidates(state_name)
        # 2) Fallback to extractor (readâ€‘only) if available
        if not draws and extract_draw_list is not None:
            draws = extract_draw_list(state_name, None)
        # If no draws, attempt to generate cleaned CSVs once from local Excel
        if not draws:
            try:
                local_excel_path = os.path.normpath("data/original/Pick3StatsC4.xlsm")
                if os.path.exists(local_excel_path):
                    # Use staged runner; writes only to data/cleaned
                    from modules.run_process import run_process
                    _ = run_process(local_excel_path, max_draws=1000, analysis_draws=100)
                    # re-try CSV read to avoid extractor conflicts
                    draws = _load_draws_from_csv_candidates(state_name)
            except Exception:
                pass
        if not draws:
            return None
        draws_100 = draws[:100] if len(draws) >= 100 else draws
        draws_1000 = draws[:1000] if len(draws) >= 1000 else draws
        nonrep, rep, pair_status = calculate_overdue_pairs(draws_100)
        vstat = get_vtrac_statuses(draws_100, draws_1000)
        top5 = get_top_overdue_repeating_pairs(draws_100, 5)
        doubles = get_doubles_history({state_name: draws})
        return {
            "draws": draws,
            "draws_100": draws_100,
            "draws_1000": draws_1000,
            "nonrep": nonrep,
            "rep": rep,
            "pair_status": pair_status,
            "vstat": vstat,
            "top5": top5,
            "doubles": doubles,
        }
    
    if st.button("Run Auxiliary Tools Analysis", type="primary"):
        with st.spinner(f"Running auxiliary analysis for {state}..."):
            try:
                results = cached_aux_analysis(state)
                if not results:
                    st.error("Working modules unavailable or no draws found.")
                    return

                draws = results["draws"]
                draws_100 = results["draws_100"]
                pair_status = results["pair_status"]
                vstat = results["vstat"]
                # Compute sums stats (window matches analysis_draws) using a non-colliding import root
                _calc_sums = None
                _build_sums_df = None
                with _project_modules_first():
                    try:
                        from module_d_auxiliary_tools.refactored.sums_analysis import (
                            calculate_sums_stats as _calc_sums,
                        )
                        from module_d_auxiliary_tools.refactored.sums_ui import (
                            build_sums_dataframe as _build_sums_df,
                        )
                        # Debug caption to verify import source; safe to remove later
                        st.sidebar.caption(f"SUMS â¦¿ {_calc_sums.__module__}")
                    except Exception as _e:
                        st.sidebar.caption(f"SUMS import failed: {_e}")

                analysis_draws = st.session_state.get("analysis_draws", 100)
                if callable(_calc_sums):
                    try:
                        sums_stats = _calc_sums(draws, window=analysis_draws)
                    except Exception:
                        sums_stats = {"window": 0, "by_sum": {}, "by_root_sum": {}}
                else:
                    sums_stats = {"window": 0, "by_sum": {}, "by_root_sum": {}}
                results["sums_stats"] = sums_stats

                # --- Vâ€‘Trac Table (Working logic) ---
                st.subheader("ðŸ“Š Vâ€‘Trac Analysis (Working logic)")
                import pandas as _pd
                rows = []
                rows_plain = []
                for entry in VTRAC_DISPLAY:
                    idx = entry["Index"]
                    singles = entry["Singles"].split() if entry["Singles"] else []
                    doubles = entry["Doubles"].split() if entry["Doubles"] else []
                    sdict = vstat.get(idx, {}).get("singles_status", {})
                    ddict = vstat.get(idx, {}).get("doubles_status", {})
                    # Build html content
                    # Build html content + sums badges
                    s_html = " ".join([
                        (_format_combo(c, sdict, pair_status) + _sums_badge_for(c, results.get("sums_stats", {})))
                        for c in singles
                    ]) if singles else "&nbsp;"
                    d_html = " ".join([
                        (_format_combo(c, ddict, pair_status) + _sums_badge_for(c, results.get("sums_stats", {})))
                        for c in doubles
                    ]) if doubles else "&nbsp;"
                    # Row tint + rank badge
                    idx_style = vstat.get(idx, {}).get("index_style", {})
                    row_class = ""
                    if idx_style.get("bg") == "green":
                        row_class = "row-green"
                    elif idx_style.get("bg") == "red":
                        row_class = "row-red"
                    badge = f'<sup class="rank-badge">{idx_style.get("rank")}</sup>' if idx_style.get("rank") else ""
                    index_cell = f'<div class="{row_class}">{idx}{badge}</div>' if row_class else f'{idx}{badge}'
                    singles_cell = f'<div class="{row_class}">{s_html}{badge}</div>' if row_class else f'{s_html}{badge}'
                    doubles_cell = f'<div class="{row_class}">{d_html}{badge}</div>' if row_class else f'{d_html}{badge}'
                    rows.append({"Index": index_cell, "Singles": singles_cell, "Doubles": doubles_cell})
                    # Plain (for CSV download)
                    rows_plain.append({"Index": idx, "Singles": " ".join(singles), "Doubles": " ".join(doubles)})
                df_v = _pd.DataFrame(rows)
                st.markdown(df_v.to_html(escape=False, index=False), unsafe_allow_html=True)
                # Download (plain)
                df_plain = _pd.DataFrame(rows_plain)
                st.download_button(
                    "Download Vâ€‘Trac Table (Working) CSV",
                    df_plain.to_csv(index=False).encode("utf-8"),
                    file_name=f"{state}_vtrac_working.csv",
                    mime="text/csv",
                )

                # --- Overdue Pairs (Working logic) ---
                st.subheader("ðŸ”¥ Overdue Pairs Analysis (Working logic)")
                THR_NR_RED, THR_R_RED = 37, 71
                THR_NR_BLUE, THR_R_BLUE = 56, 107
                THR_PENDING = 25
                nonrep = results["nonrep"]
                rep = results["rep"]
                rep_red = sorted([p for p, ds in rep.items() if ds >= THR_R_RED])
                rep_blue = sorted([p for p, ds in rep.items() if ds >= THR_R_BLUE])
                rep_purple = sorted([p for p, ds in rep.items() if THR_PENDING <= ds < THR_R_RED])
                nr_red = sorted([p for p, ds in nonrep.items() if ds >= THR_NR_RED])
                nr_blue = sorted([p for p, ds in nonrep.items() if ds >= THR_NR_BLUE])
                nr_purple = sorted([p for p, ds in nonrep.items() if THR_PENDING <= ds < THR_NR_RED])

                # Thresholds info like the working app
                st.info(f"""
                **Overdue Thresholds:**
                - Repeating pairs (00, 11, etc): RED={THR_R_RED}+, BLUE={THR_R_BLUE}+, PURPLE={THR_PENDING}+
                - Non-repeating pairs (01, 23, etc): RED={THR_NR_RED}+, BLUE={THR_NR_BLUE}+, PURPLE={THR_PENDING}+
                """)

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("<b>Repeating Pairs (Doubles)</b>", unsafe_allow_html=True)
                    st.markdown(f"<span class='red'>Red (â‰¥{THR_R_RED}):</span> " + (", ".join(rep_red) if rep_red else "None"), unsafe_allow_html=True)
                    st.markdown(f"<span class='blue'>Blue (â‰¥{THR_R_BLUE}):</span> " + (", ".join(rep_blue) if rep_blue else "None"), unsafe_allow_html=True)
                    st.markdown(f"<span class='purple'>Purple (â‰¥{THR_PENDING}):</span> " + (", ".join(rep_purple) if rep_purple else "None"), unsafe_allow_html=True)
                with c2:
                    st.markdown("<b>Nonâ€‘Repeating Pairs</b>", unsafe_allow_html=True)
                    st.markdown(f"<span class='red'>Red (â‰¥{THR_NR_RED}):</span> " + (", ".join(nr_red) if nr_red else "None"), unsafe_allow_html=True)
                    st.markdown(f"<span class='blue'>Blue (â‰¥{THR_NR_BLUE}):</span> " + (", ".join(nr_blue) if nr_blue else "None"), unsafe_allow_html=True)
                    st.markdown(f"<span class='purple'>Purple (â‰¥{THR_PENDING}):</span> " + (", ".join(nr_purple) if nr_purple else "None"), unsafe_allow_html=True)

                # --- Top 5 Repeating Pairs ---
                st.subheader("Top 5 Most Overdue Repeating Pairs (Working logic)")
                for pair, overdue in results["top5"]:
                    if overdue >= 107:
                        color = "blue"
                    elif overdue >= 71:
                        color = "red"
                    elif overdue >= 25:
                        color = "purple"
                    else:
                        color = ""

                    line = f"{pair} - {overdue} draws overdue"
                    if color:
                        st.markdown(f'<span class="{color}">{line}</span>', unsafe_allow_html=True)
                    else:
                        st.write(line)

                # --- Four-panels row (parity with working app) ---
                c1, c2, c3, c4 = st.columns(4, gap="small")
                # Latest Draws
                with c1:
                    st.subheader("Latest Draws")
                    import pandas as _pd
                    df_latest = _pd.DataFrame({"Draw": draws[:5]})
                    st.dataframe(df_latest, use_container_width=True)
                # Pairs Analysis Results (tabular)
                with c2:
                    st.subheader("Pairs Analysis Results")
                    times_drawn = {}
                    for i, d in enumerate(draws[:150]):
                        if not isinstance(d, str) or len(d) != 3:
                            continue
                        d1, d2, d3 = d[0], d[1], d[2]
                        for raw in (d1+d2, d2+d3, d1+d3):
                            p = ''.join(sorted(raw))
                            times_drawn[p] = times_drawn.get(p, 0) + 1
                    # merge overdue values
                    all_pairs = sorted(set(list(nonrep.keys()) + list(rep.keys())))
                    rows_pairs = []
                    for p in all_pairs:
                        is_rep = (p[0] == p[1])
                        overdue = rep.get(p, 0) if is_rep else nonrep.get(p, 0)
                        rows_pairs.append({"Pair": p, "Times Drawn": times_drawn.get(p, 0), "Draws Since": overdue})
                    df_pairs = _pd.DataFrame(rows_pairs)
                    if not df_pairs.empty:
                        df_pairs = df_pairs.sort_values("Draws Since", ascending=False)
                    st.dataframe(df_pairs, use_container_width=True)
                # Combinations Analysis (Draws Since) with shapes
                with c3:
                    st.subheader("Combinations Analysis (Draws Since)")
                    combo_ds = vstat.get(0, {})
                    singles_ds = combo_ds.get("singles_ds", {})
                    doubles_ds = combo_ds.get("doubles_ds", {})
                    S_RED, S_BLUE, D_RED, D_BLUE = 501, 334, 1000, 667
                    safe_rows = []
                    # Build status to reuse shape rendering
                    for base, ds in singles_ds.items():
                        status = {}
                        if ds >= S_RED:
                            status[base] = {"shape_red_circle": True}
                        elif ds >= S_BLUE:
                            status[base] = {"shape_blue_square": True}
                        html_combo = _format_combo(str(base).zfill(3), status, pair_status)
                        safe_rows.append({"Combo": html_combo, "Type": "Single", "Draws Since": int(ds)})
                    for base, ds in doubles_ds.items():
                        status = {}
                        if ds >= D_RED:
                            status[base] = {"shape_red_circle": True}
                        elif ds >= D_BLUE:
                            status[base] = {"shape_blue_square": True}
                        html_combo = _format_combo(str(base).zfill(3), status, pair_status)
                        safe_rows.append({"Combo": html_combo, "Type": "Double", "Draws Since": int(ds)})
                    if safe_rows:
                        safe_rows.sort(key=lambda x: x["Draws Since"], reverse=True)
                        dfc_html = _pd.DataFrame(safe_rows)
                        html_table = dfc_html.to_html(escape=False, index=False)
                        st.markdown(f'<div style="max-height: 420px; overflow-y: auto; border: 1px solid #eee; padding: 6px;">{html_table}</div>', unsafe_allow_html=True)
                    else:
                        st.write("No data")
                with c4:
                    st.subheader("Top 5 Most Overdue Repeating Pairs (Working logic)")
                    for pair, overdue in results["top5"]:
                        if overdue >= 107:
                            color = "blue"
                        elif overdue >= 71:
                            color = "red"
                        elif overdue >= 25:
                            color = "purple"
                        else:
                            color = ""
                        style = "font-size: 1.05rem; font-weight: 600;"
                        line = f"{pair} - {overdue} draws overdue"
                        if color:
                            st.markdown(f"<span class='{color}' style='{style}'>{line}</span>", unsafe_allow_html=True)
                        else:
                            st.markdown(f"<span style='{style}'>{line}</span>", unsafe_allow_html=True)

                # Sums Tracking (table)
                if callable(_build_sums_df) and isinstance(sums_stats, dict) and sums_stats.get("by_sum"):
                    try:
                        df_sums = _build_sums_df(sums_stats)  # type: ignore[misc]
                        html_sums = df_sums.to_html(escape=False, index=False)
                        st.subheader("Sums Tracking")
                        st.markdown(f'<div style="max-height: 420px; overflow-y: auto; border: 1px solid #eee; padding: 6px;">{html_sums}</div>', unsafe_allow_html=True)
                    except Exception:
                        pass
                # --- Blackapple Alert (MVP) ---
                try:
                    _ba = _load_blackapple_real()
                    analyze_blackapple = _ba.analyze_blackapple
                    ba_status_label = _ba.ba_status_label
                    sum_tags = getattr(_ba, "sum_tags", None)
                    if sum_tags is None:
                        def sum_tags(combo: str):
                            s = sum(int(c) for c in combo) if combo and combo.isdigit() else 0
                            r = s
                            while r > 9:
                                r = sum(int(x) for x in str(r))
                            return {"Sigma": s, "sD": s % 10, "RS": r}

                    _aux = _load_aux_loaders_real()
                    load_state_draws = getattr(_aux, "load_state_draws", None)
                    if callable(load_state_draws):
                        ba_draws, ba_src = load_state_draws(state)
                    else:
                        ba_draws, ba_src = [], ""

                    ba = analyze_blackapple(ba_draws or draws)
                    status = ba_status_label(ba.get("score", 0))
                    st.subheader("Blackapple Alert")
                    if ba_src:
                        st.caption(f"BA draws: {ba_src} ({len(ba_draws)})")
                    parts = []
                    tr = ba.get("triggers", {})
                    if tr.get("mirror"):
                        parts.append("Mirror")
                    roots = tr.get("root_due", [])
                    if roots:
                        parts.append("Root due: " + ", ".join(map(str, roots)))
                    pat = tr.get("pattern", {})
                    if pat.get("extreme_due"):
                        parts.append("SSS/TTT due")
                    if pat.get("mixed_due"):
                        parts.append("SST/STS/TSS due")
                    flt = tr.get("floating", [])
                    if flt:
                        parts.append("Floating: " + "".join(flt))
                    rc = (tr.get("pairs", {}) or {}).get("remaining_count")
                    if rc is not None:
                        parts.append(f"Remaining Pairs: {rc}")
                    st.markdown(f"**Status:** {status} (BAScore {ba.get('score',0)}/5)")
                    st.write("Triggers: " + (", ".join(parts) if parts else "None"))
                    rows = []
                    for c in ba.get("candidates", []):
                        t = sum_tags(c.get("combo", ""))
                        rows.append({
                            "Combo": c.get("combo", ""),
                            "MatchScore": c.get("score", 0),
                            "Tags": " ".join(sorted(c.get("tags", []))),
                            "Sums": f"IΣ{t['Sigma']} sD{t['sD']} RS{t['RS']}"
                        })
                    if rows:
                        import pandas as _pd
                        st.dataframe(_pd.DataFrame(rows), use_container_width=True)
                    else:
                        st.caption("No candidate list (insufficient overlap) — still watching triggers.")
                except Exception as _e:
                    st.caption(f"Blackapple panel unavailable: {_e}")
                # Legend / Feature Guide
                with st.expander("Legend / Feature Guide"):
                    st.markdown("""
                    - Vâ€‘Trac index row tints: light green = last 5 hit (rank 1..5), light red = 5 most overdue (rank 1..5).
                    - Combination shapes:
                      - Red circle: Singles â‰¥ 501 draws since; Doubles â‰¥ 1000
                      - Blue square: Singles â‰¥ 334; Doubles â‰¥ 667
                      - Boxed combos: permutations are treated as the same combo
                    - Pairs colors (analysis window based):
                      - Red (Late): nonâ€‘repeating â‰¥ 37, repeating â‰¥ 71
                      - Blue (Very Late): nonâ€‘repeating â‰¥ 56, repeating â‰¥ 107
                      - Purple (Pending): â‰¥ 25
                    """)

                # --- Vâ€‘Trac Index Hits (Working logic) ---
                import pandas as _pd
                idx_rows = []
                # Build draws_since map for all indices
                recent_ranks = vstat.get(0, {}).get("recent_index_ranks", {}) if isinstance(vstat.get(0, {}), dict) else {}
                overdue_ranks = vstat.get(0, {}).get("overdue_index_ranks", {}) if isinstance(vstat.get(0, {}), dict) else {}
                # If not present under 0-key, reconstruct minimal maps from per-index style
                if not recent_ranks and not overdue_ranks:
                    for entry in VTRAC_DISPLAY:
                        idx = entry["Index"]
                        ist = vstat.get(idx, {}).get("index_style", {})
                        if ist.get("bg") == "green" and ist.get("rank"):
                            recent_ranks[idx] = ist.get("rank")
                        elif ist.get("bg") == "red" and ist.get("rank"):
                            overdue_ranks[idx] = ist.get("rank")
                # derive draws_since by scanning the first-seen positions over draws_1000
                draws_1000 = results.get("draws_1000", draws)
                total_len = len(draws_1000)
                index_first_seen = {}
                for i, d in enumerate(draws_1000):
                    if not isinstance(d, str) or len(d) != 3 or len(set(d)) == 1:
                        continue
                    idx = get_vtrac_index(d)
                    if idx and idx not in index_first_seen:
                        index_first_seen[idx] = i
                index_draws_since = {i: index_first_seen.get(i, total_len) for i in range(1, 36)}

                for idx, ds in index_draws_since.items():
                    status = "None"
                    rank = ""
                    if idx in overdue_ranks:
                        status = "Overdue"
                        rank = overdue_ranks[idx]
                    elif idx in recent_ranks:
                        status = "Recent"
                        rank = recent_ranks[idx]
                    idx_rows.append({"Index": idx, "Draws Since": ds, "Status": status, "Rank": rank})
                # Sort: Overdue desc, then Recent by rank, then others
                df_idx = _pd.DataFrame(idx_rows)
                if not df_idx.empty:
                    df_idx["_overdue_sort"] = df_idx["Status"].apply(lambda s: 2 if s == "Overdue" else (1 if s == "Recent" else 0))
                    df_idx["_rank_fill"] = df_idx["Rank"].apply(lambda r: int(r) if str(r).isdigit() else 0)
                    df_idx = df_idx.sort_values(["_overdue_sort", "Draws Since", "_rank_fill"], ascending=[False, False, True])[ ["Index", "Draws Since", "Status", "Rank"] ]
                    html_idx = df_idx.to_html(index=False, escape=False)
                    st.subheader("Vâ€‘Trac Index Hits (Working logic)")
                    st.markdown(f'<div style="max-height: 320px; overflow-y: auto; border: 1px solid #eee; padding: 6px;">{html_idx}</div>', unsafe_allow_html=True)

                st.success(f"âœ… Auxiliary tools (working logic) completed for {state}")
                
            except Exception as e:
                st.error(f"Error running auxiliary analysis: {str(e)}")
                st.info("Please ensure the state data files are available in data/cleaned/")
    
    else:
        st.info("Click the button above to run auxiliary tools analysis.")
        
        # Show available states info (from legacy helper if present)
        try:
            from modules.module_d_auxiliary_tools.integration import get_available_states
            available_states = get_available_states()
        except Exception:
            available_states = []
        else:
            st.warning("No state data files found. Please ensure cleaned data is available.")


def show_digit_reduction_page(state: str) -> None:
    """Render the Digit-Reduction Streamlit tab."""
    st.title(f"Digit Reduction - {state}")

    tables_root = Path(get_tables_output_dir())
    if not tables_root.exists():
        # Dev: System Health (Digit Reduction)
        try:
            show_dev_d = st.sidebar.checkbox("Show Dev Health", value=False, key="dev_health_dr")
        except Exception:
            show_dev_d = False
        if show_dev_d:
            import os, sys as _sys
            with st.expander("System Health (Digit Reduction)"):
                st.caption("cwd: " + os.getcwd())
                st.caption("python: " + _sys.executable)
                try:
                    from core.module_b_digit_reduction import run_digit_reduction as _rdr
                    import inspect as _insp
                    st.caption("DR module: " + str(getattr(_rdr, "__module__", "unknown")))
                except Exception as _se:
                    st.caption("DR module: unavailable: " + str(_se))
                try:
                    st.caption("tables_root: " + str(tables_root) + " (exists=" + str(tables_root.exists()) + ")")
                except Exception:
                    pass
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
            st.warning("Digit Reduction produced no output â€“ verify tables exist.")
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




























