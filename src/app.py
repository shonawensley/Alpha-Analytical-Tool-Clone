import sys
import os
import pathlib
import subprocess
import streamlit as st
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List, Optional

render_dr_winner_overlay_dev = None
DEV_OVERLAY_IMPORT_ERROR = None

# --- Canonical imports bootstrap (ensure top-level utils wins) ---------
SRC_DIR = pathlib.Path(__file__).resolve().parent     # .../src
PROJECT_ROOT = SRC_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
try:
    u = sys.modules.get('utils')
    if u and getattr(u, '__file__', '') and ('%s' % u.__file__).replace('\\', '/').find('/src/utils/') != -1:
        sys.modules.pop('utils', None)
        sys.modules.pop('utils.path_handler', None)
        sys.modules.pop('src.utils', None)
        sys.modules.pop('src.utils.path_handler', None)
except Exception:
    pass
# Ensure 'modules' resolves to project modules for non-Aux pages
try:
    m = sys.modules.get('modules')
    if m and getattr(m, '__file__', ''):
        path_norm = ('%s' % m.__file__).replace('\\', '/').lower()
        if '/scripts/auxiliary/working/modules/' in path_norm:
            # Evict staged binding so imports resolve to project modules
            sys.modules.pop('modules', None)
except Exception:
    pass

# Standardize import hygiene via helper (safe no-op if already applied)
try:
    from _import_hygiene import ensure_project_root_on_syspath, evict_staged_modules_for_non_aux
    ensure_project_root_on_syspath()
    evict_staged_modules_for_non_aux()
except Exception:
    pass
try:
    import importlib as _importlib
    _uph = _importlib.import_module('utils.path_handler')
    sys.modules['utils.path_handler'] = _uph
except Exception:
    pass

try:
    from modules.module_d_auxiliary_tools.refactored import draws_extractor_p3_columns as _aux_columns
    from modules.module_d_auxiliary_tools.refactored import extractor as _aux_extractor
except Exception:
    _aux_columns = None
    _aux_extractor = None
# ----------------------------------------------------------------------

from core.module_b_digit_reduction import run_digit_reduction
from utils.path_handler import get_tables_output_dir
from core.aux_config import (
    PAIRS_WINDOW,
    POSITIONAL_WINDOW,
    SUMS_WINDOW,
    VTRAC_INDEX_WINDOW,
    COMBINATION_WINDOW,
    REPEATING_LATE,
    REPEATING_VERY_LATE,
    NONREPEATING_LATE,
    NONREPEATING_VERY_LATE,
    PAIR_PENDING,
    COMBO_SINGLE_LATE,
    COMBO_SINGLE_VERY_LATE,
    COMBO_DOUBLE_LATE,
    COMBO_DOUBLE_VERY_LATE,
    WINDOW_CAPTIONS,
)

# --- path hook (kept; bootstrap above already inserted PROJECT_ROOT) ---
# ----------------------------------------------------------------------
 

# --- AUX working modules path (staged, isolated) -----------------------
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
    sys.modules[dotted_name] = mod
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _load_blackapple_real():
    return _load_project_module("project_blackapple", "modules/blackapple.py")


def _load_aux_loaders_real():
    return _load_project_module("project_aux_loaders", "modules/aux_loaders.py")

def _load_positional_tool_real():
    try:
        from modules.module_d_auxiliary_tools.refactored import positional_tool as _pt

        return _pt
    except Exception:
        return _load_project_module(
            "project_positional_tool",
            "modules/module_d_auxiliary_tools/refactored/positional_tool.py",
        )

# Digit-Reduction path helpers

def _digit_reduction_dirs(state: str, analysis_root: Path) -> tuple[Path, Path, Path]:
    base = analysis_root / "digit_reduction" / state
    training = base / "training"
    analyzer = base / "analyzer_v2"
    return base, training, analyzer


def _open_path_in_explorer(path: Path) -> bool:
    target = path if path.exists() else path.parent
    if not target.exists():
        return False
    try:
        if os.name == "nt":
            os.startfile(str(target))  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.run(["open", str(target)], check=False)
        else:
            subprocess.run(["xdg-open", str(target)], check=False)
        return True
    except Exception:
        return False


# Helpers for rendering working V-TRAC output (used only on Aux page)
def _severity(cls: str) -> int:
    # Priority: red > blue > purple (display-only severity)
    return {"red": 3, "blue": 2, "purple": 1}.get(cls or "", 0)


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



def _resolve_vtrac_index(draw: str, resolver) -> str | None:
    """Return canonical V-TRAC index for a draw, skipping invalid inputs."""
    if not isinstance(draw, str) or len(draw) != 3:
        return None
    if len(set(draw)) == 1:
        return None
    try:
        idx = resolver(draw)
    except Exception:
        return None
    return idx


def _build_vtrac_overlay(draws: list[str], resolver, window: int = VTRAC_INDEX_WINDOW) -> dict:
    """Compute draws-since overlay data for all 35 V-TRAC indexes."""
    trimmed = list(draws[:window]) if window else list(draws)
    total_len = len(trimmed)
    index_first_seen: dict[int, int] = {}
    for offset, draw in enumerate(trimmed):
        idx = _resolve_vtrac_index(draw, resolver)
        if idx and isinstance(idx, int) and 1 <= idx <= 35 and idx not in index_first_seen:
            index_first_seen[idx] = offset
    draws_since = {idx: index_first_seen.get(idx, total_len) for idx in range(1, 36)}
    sorted_overdue = sorted(draws_since.items(), key=lambda item: item[1], reverse=True)
    return {
        "draws_since": draws_since,
        "sorted_overdue": sorted_overdue,
        "top_overdue": [idx for idx, _ in sorted_overdue[:10]],
        "window": total_len,
    }


def _summarize_vtrac_repeats(draws: list[str], resolver, window: int = VTRAC_INDEX_WINDOW) -> dict:
    """Summarize repeat streak stats for a sequence of draws."""
    trimmed = list(draws[:window]) if window else list(draws)
    valid_stream: list[int] = []
    for draw in trimmed:
        idx = _resolve_vtrac_index(draw, resolver)
        if idx is not None:
            valid_stream.append(idx)
        else:
            valid_stream.append(None)  # keep placeholders for offset math
    # Determine current streak from the head of the stream
    current_index = None
    current_streak = 0
    for value in valid_stream:
        if value is None:
            if current_index is None:
                continue
            break
        if current_index is None:
            current_index = value
            current_streak = 1
        elif value == current_index:
            current_streak += 1
        else:
            break
    # Walk the stream again to capture last repeat and max streak
    last_repeat_gap = None
    last_repeat_index = None
    max_streak = 0
    prev_idx = None
    streak = 0
    for offset, value in enumerate(valid_stream):
        if value is None:
            prev_idx = None
            streak = 0
            continue
        if value == prev_idx:
            streak += 1
        else:
            streak = 1
            prev_idx = value
        if streak > max_streak:
            max_streak = streak
        if streak >= 2 and last_repeat_gap is None:
            last_repeat_gap = offset
            last_repeat_index = value
    if max_streak < current_streak:
        max_streak = current_streak
    return {
        "current_index": current_index,
        "current_streak": current_streak,
        "last_repeat_gap": last_repeat_gap,
        "last_repeat_index": last_repeat_index,
        "max_streak": max_streak,
        "window": len(trimmed),
    }
# --- Helpers: robust draw loading without touching other tools ----------
def _normalize_state_name(state_name: str) -> str:
    import re
    # Drop trailing digits like "Connecticut4" -> "Connecticut"
    return re.sub(r"\d+$", "", state_name or "").strip().replace("_", " ")


def _load_draws_from_csv_candidates(state_name: str, variant: str = "combined"):
    """Fallback loader used by Aux page; prefers the canonical aux_loaders helper."""
    try:
        _aux = _load_aux_loaders_real()
        load_state_draws = getattr(_aux, "load_state_draws", None)
        if callable(load_state_draws):
            draws, _src = load_state_draws(state_name, variant=variant)
            if draws:
                return draws
    except Exception:
        pass

    if variant != "combined":
        return []

    import pandas as _pd

    base = _normalize_state_name(state_name)
    fn = f"{base.replace(' ', '_')}_draws.csv"
    candidates = [
        os.path.normpath("data/cleaned/draws"),
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
def _aux_working_first():
    """Temporarily prefer staged Aux modules and restore project bindings afterwards."""
    prev_modules = sys.modules.get("modules")
    prev_children = {
        name: sys.modules.get(name)
        for name in (
            "modules.analyze_pairs",
            "modules.vtrac_reference",
            "modules.run_process",
        )
    }
    old_sys_path = list(sys.path)
    try:
        # Ensure the staged working root is first on sys.path so that
        # imports of `modules.*` resolve to scripts/auxiliary/working/modules.
        if _AUX_WORKING_ROOT in sys.path:
            try:
                sys.path.remove(_AUX_WORKING_ROOT)
            except ValueError:
                pass
        sys.path.insert(0, _AUX_WORKING_ROOT)

        # Evict any existing bindings so we get a fresh import from the staged copy
        sys.modules.pop("modules", None)
        for name in prev_children:
            sys.modules.pop(name, None)
        yield
    finally:
        # Restore original sys.path
        sys.path[:] = old_sys_path
        if prev_modules is not None:
            sys.modules["modules"] = prev_modules
        else:
            sys.modules.pop("modules", None)
        for name, mod in prev_children.items():
            if mod is not None:
                sys.modules[name] = mod
            else:
                sys.modules.pop(name, None)

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
                parts.append('<span class="purple">&#8226;</span>')
            return " ".join(parts)

        s_tag = tag(f"S{s}", sflags)
        r_tag = tag(f"R{r}", rflags)
        if not s_tag and not r_tag:
            return ""
        both = " ".join(x for x in (s_tag, r_tag) if x)
        return f' <span style="font-size:0.85em;opacity:.85">[{both}]</span>'
    except Exception:
        return ""

# Page config FIRST (before every other st.*)

# --- Aux thresholds (single source of truth via aux_config) ---
REPEATING_LATE_THRESHOLD = REPEATING_LATE
REPEATING_VERY_LATE_THRESHOLD = REPEATING_VERY_LATE
NONREPEATING_LATE_THRESHOLD = NONREPEATING_LATE
NONREPEATING_VERY_LATE_THRESHOLD = NONREPEATING_VERY_LATE
PAIR_PENDING_THRESHOLD = PAIR_PENDING

COMBO_SINGLE_LATE_THRESHOLD = COMBO_SINGLE_LATE
COMBO_SINGLE_VERY_LATE_THRESHOLD = COMBO_SINGLE_VERY_LATE
COMBO_DOUBLE_LATE_THRESHOLD = COMBO_DOUBLE_LATE
COMBO_DOUBLE_VERY_LATE_THRESHOLD = COMBO_DOUBLE_VERY_LATE

assert REPEATING_VERY_LATE_THRESHOLD >= REPEATING_LATE_THRESHOLD, "Repeating: red must be >= blue"
assert NONREPEATING_VERY_LATE_THRESHOLD >= NONREPEATING_LATE_THRESHOLD, "Non-repeating: red must be >= blue"

PAIRS_ANALYSIS_WINDOW = PAIRS_WINDOW

try:
    show_purple

except NameError:
    show_purple = True
def _assert_threshold_alignment():
    assert REPEATING_VERY_LATE_THRESHOLD >= REPEATING_LATE_THRESHOLD, "Repeating: red must be >= blue"
    assert NONREPEATING_VERY_LATE_THRESHOLD >= NONREPEATING_LATE_THRESHOLD, "Non-repeating: red must be >= blue"


def _assert_no_mojibake():
    src = Path(__file__).read_text(encoding='utf-8', errors='ignore')
    if any(ord(ch) > 127 for ch in src):
        try:
            st.warning('Mojibake detected in UI strings - sanitize src/app.py')
        except Exception:
            pass


_assert_threshold_alignment()

st.set_page_config(page_title="Alpha-Final Analytical Tool",
                   page_icon=":bar_chart:", layout="wide")

# Debug: show which file is running (safe to remove later)
def main():
    """
    Main function to run the Alpha-Final Streamlit app.
    This app will have a two-level navigation: State selection and Tool selection.
    """
    try:
        _assert_no_mojibake()
    except Exception:
        pass

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
        "State",
        states_list,
        index=0
    )
    
    # Second level: Tool selector  
    selected_tool = st.sidebar.selectbox(
        "Tool",
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
    """Render the integrated V-TRAC analyzer page."""
    from core import module_c_vtrac  # lazy import
    module_c_vtrac.render(state)


def _parse_winners_input(raw: str) -> list[str]:
    """Normalize a comma/newline separated winners string into 3-digit tokens."""
    winners: list[str] = []
    if not raw:
        return winners
    for token in raw.replace("\n", ",").split(","):
        cleaned = ''.join(ch for ch in token if ch.isdigit())
        if not cleaned:
            continue
        if len(cleaned) == 3:
            winners.append(cleaned)
    return winners


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
        import os, sys as _sys, importlib as _il
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
                from core import stable_pattern_extractor as _stable_ex
                engine_path = getattr(getattr(_stable_ex, "_ex", None), "__file__", None)
                if engine_path:
                    st.caption("Engine: " + str(engine_path))
                cfg_path = getattr(getattr(_stable_ex, "_ex", None), "CFG_PATH", None)
                if cfg_path:
                    st.caption("feature_config.yml: " + str(cfg_path))
            except Exception:
                pass
            try:
                _vref = _il.import_module('modules.vtrac_reference')
                st.caption("vtrac_reference: " + getattr(_vref, '__file__', 'unknown'))
            except Exception:
                pass
            try:
                tdir = ph.get_state_tables_dir(state)
                st.caption("tables_dir: " + str(tdir) + " (exists=" + str(_P(tdir).exists()) + ")")
            except Exception:
                pass
    # --- User inputs ---------------------------------------------------
    min_occ = st.number_input("Minimum occurrences (min_occ)", min_value=1, max_value=10, value=3, step=1)

    winners_raw = st.text_input(
        "Optional winners (comma-separated 3-digit numbers)",
        value="",
        key=f"stable_winners_input_{state}",
        help="Provide winners if you want the extractor to generate spotlight CSVs. Leave blank to skip."
    )
    winners_list = _parse_winners_input(winners_raw)

    if st.button("Run Stable Pattern Extraction"):
        tables_dir = ph.get_state_tables_dir(state)
        out_dir    = ph.get_analysis_dir("patterns", state)

        df, html_f, csv_f = stable.run_stable_pattern_extraction(
            state=state,
            tables_path=tables_dir,
            out_path=out_dir,
            min_occ=min_occ,
            winners=winners_list if winners_list else None,
        )

        if df.empty:
            st.warning("No patterns found - verify tables or adjust parameters.")
        else:
            st.success(f"{len(df)} patterns extracted.")
            st.dataframe(df.head(50), height=360)

            if csv_f:
                st.markdown(f"[Download CSV]({csv_f})")

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

    _CATEGORY_SUFFIXES = ("_Midday", "_Evening", "_Morning", "_Nite", "_Noon")

    def _is_combined_csv(path: Path) -> bool:
        stem = path.stem
        if stem.endswith("_draws"):
            prefix = stem[: -len("_draws")]
        else:
            prefix = stem
        return not any(prefix.endswith(sfx) for sfx in _CATEGORY_SUFFIXES)

    _VARIANT_BADGES = {"combined": "C", "midday": "M", "evening": "E"}
    _RED_COMBO_THRESHOLD = 1000

    def _generate_double_combos() -> tuple[str, ...]:
        combos = set()
        digits = "0123456789"
        for repeated in digits:
            for other in digits:
                if other == repeated:
                    continue
                combos.add(repeated * 2 + other)
                combos.add(repeated + other + repeated)
                combos.add(other + repeated * 2)
        return tuple(sorted(combos))

    _DOUBLE_COMBOS = _generate_double_combos()
    _COMBO_SEPARATOR = " - "

    def _double_combo_gaps(draws: List[str]) -> Dict[str, int]:
        if not draws:
            return {combo: 0 for combo in _DOUBLE_COMBOS}
        default_gap = len(draws)
        gaps = {combo: default_gap for combo in _DOUBLE_COMBOS}
        for idx, draw in enumerate(draws):
            value = (draw or "").strip()
            if len(value) != 3:
                continue
            if value in gaps and gaps[value] == default_gap:
                gaps[value] = idx
        return gaps

    def _combo_matches_pair(combo: str, pair: str) -> bool:
        if not combo or not pair or len(pair) != 2:
            return False
        if pair[0] != pair[1]:
            return False
        value = combo.strip()
        if len(value) != 3:
            return False
        return value.count(pair[0]) == 2 and len(set(value)) == 2

    def _collect_combo_entries(pair: str, badge_maps: Dict[str, Dict[str, int]]) -> List[str]:
        hits: Dict[str, set[str]] = {}
        for badge, gap_map in badge_maps.items():
            for combo, gap in gap_map.items():
                if gap >= _RED_COMBO_THRESHOLD and _combo_matches_pair(combo, pair):
                    hits.setdefault(combo, set()).add(badge)
        formatted: List[str] = []
        for combo in sorted(hits):
            badges = "/".join(sorted(hits[combo]))
            formatted.append(f"{combo} {badges}" if badges else combo)
        return formatted

    def _format_pair_value(entry: Optional[tuple[str, int]]) -> str:
        if not entry:
            return "-"
        pair, gap = entry
        try:
            gap_int = int(gap)
        except (TypeError, ValueError):
            return f"{pair} - {gap}"
        return f"{pair} - {gap_int}"

    def _format_combo_cell(entries: List[str]) -> str:
        if not entries:
            return "-"
        return _COMBO_SEPARATOR.join(entries)


    # Dev: System Health (Control Center)
    try:
        show_dev_cc = st.checkbox("Show Dev Health (Control Center)", value=False, key="dev_health_cc")
    except Exception:
        show_dev_cc = False
    if show_dev_cc:
        import os, sys as _sys, importlib as _il
        from pathlib import Path as _P
        from utils import path_handler as _ph
        with st.expander("System Health (Control Center)", expanded=False):
            st.caption("cwd: " + os.getcwd())
            st.caption("python: " + _sys.executable)
            # Key modules bound
            for name in [
                'utils.path_handler',
                'modules.vtrac_reference',
                'modules.winner_report_full',
                'modules.blackapple',
                'modules.aux_loaders',
                'core.pipeline_runner',
            ]:
                try:
                    mod = _il.import_module(name)
                    st.caption(f"{name}: " + getattr(mod, '__file__', '<package>'))
                except Exception as _se:
                    st.caption(f"{name}: unavailable: {_se}")
            # Tables root + quick inventory
            try:
                _root = _P(_ph.get_tables_output_dir())
                states = sorted([p.name for p in _root.iterdir() if p.is_dir()]) if _root.exists() else []
                st.caption(f"tables_root: {_root} (exists={_root.exists()}; states={len(states)})")
                if states:
                    st.caption("sample states: " + ", ".join(states[:10]) + (" ..." if len(states) > 10 else ""))
            except Exception:
                pass
            try:
                _draw_root = _P("data/cleaned/draws")
                st.caption(f"draws_root: {_draw_root} (exists={_draw_root.exists()})")
            except Exception:
                pass

    # Optional: Tables Pipeline runner (upload Pick3StatsC4.xlsm and generate per-state tables)
    with st.expander("Tables Pipeline (optional)"):
        # Dev Health for pipeline
        try:
            show_dev_pipe = st.checkbox("Show Dev Health (Pipeline)", value=False, key="dev_health_pipeline")
        except Exception:
            show_dev_pipe = False
        if show_dev_pipe:
            import os, sys as _sys, importlib as _il
            from pathlib import Path as _P
            from utils import path_handler as _ph
            with st.expander("System Health (Pipeline)", expanded=False):
                st.caption("cwd: " + os.getcwd())
                st.caption("python: " + _sys.executable)
                try:
                    _pr = _il.import_module('core.pipeline_runner')
                    st.caption("core.pipeline_runner: " + getattr(_pr, '__file__', 'unknown'))
                except Exception as _se:
                    st.caption("core.pipeline_runner: unavailable: " + str(_se))
                try:
                    _tables_root = _P(_ph.get_tables_output_dir())
                    st.caption(f"tables_root: {_tables_root} (exists={_tables_root.exists()})")
                except Exception:
                    pass
        upl = st.file_uploader("Upload Pick3StatsC4.xlsm", type=["xlsm"], accept_multiple_files=False)
        if upl is not None and st.button("Generate Tables"):
            try:
                from core.pipeline_runner import run_pipeline_from_bytes
                with st.spinner("Running tables pipeline (clean -> extract -> generate)..."):
                    summary = run_pipeline_from_bytes(upl.getvalue())
                st.success(
                    f"Cleaned: {summary.get('clean_success',0)} states; "
                    f"Extracted: {summary.get('states_extracted',0)}; "
                    f"Wrote tables for ~{summary.get('written_states',0)} states."
                )
                st.caption("Tables root: " + str(summary.get("tables_root", "")))
                fails = summary.get("clean_failed") or []
                if fails:
                    st.warning("Cleaning failed for: " + ", ".join(fails))
            except Exception as e:
                st.error("Pipeline failed: " + str(e))

    with st.expander("Aux Draws Pipeline (Midday/Evening)"):
        if _aux_columns is None or _aux_extractor is None:
            st.caption("Aux draw extractor unavailable. Ensure refactored modules are present.")
        else:
            all_states = _aux_columns.get_tracked_states()
            selected_states = st.multiselect(
                "States",
                options=all_states,
                default=all_states,
                help="Choose which states to export.",
            )

            include_combined = st.checkbox(
                "Regenerate combined draw CSVs",
                value=True,
                help="Keep on to refresh <State>_draws.csv alongside Midday/Evening.",
            )
            include_specials = st.checkbox(
                "Include specials (Morning/Noon/Nite where available)",
                value=False,
            )

            excel_default = Path("data/original/Pick3StatsC4.xlsm")
            excel_path = st.text_input(
                "Excel source",
                value=str(excel_default),
            )
            out_default = Path("data/cleaned/draws")
            out_path = st.text_input(
                "Output directory",
                value=str(out_default),
            )

            if st.button("Generate Aux Draw CSVs", key="generate_aux_draws"):
                if not selected_states:
                    st.warning("Select at least one state to export.")
                else:
                    try:
                        excel_file = Path(excel_path)
                        out_dir = Path(out_path)
                        with st.spinner("Generating draw CSVs..."):
                            _aux_extractor.save_category_csvs(
                                excel_path=excel_file,
                                states=selected_states,
                                outdir=out_dir,
                                include_combined=include_combined,
                                include_specials=include_specials,
                            )
                        st.success("Aux draw export complete.")
                        preview_lines = []
                        for label in selected_states:
                            canonical = _aux_columns.canonical_state(label) or label
                            stem = _aux_columns.state_to_filename(canonical)
                            if include_combined and _aux_columns.get_columns_for(canonical, "combined"):
                                preview_lines.append(f"{stem}_draws.csv")
                            if _aux_columns.get_columns_for(canonical, "midday"):
                                preview_lines.append(f"{stem}_Midday_draws.csv")
                            if _aux_columns.get_columns_for(canonical, "evening"):
                                preview_lines.append(f"{stem}_Evening_draws.csv")
                            if include_specials:
                                for key, suffix in (("morning", "Morning"), ("noon", "Noon"), ("nite", "Nite")):
                                    if _aux_columns.get_columns_for(canonical, key):
                                        preview_lines.append(f"{stem}_{suffix}_draws.csv")
                        if preview_lines:
                            st.caption("Files written:")
                            st.code("\n".join(preview_lines), language="text")
                    except Exception as _aux_err:
                        st.error(f"Aux draw export failed: {_aux_err}")

    # Winners Logger: V-Trac winner report
    with st.expander("Winners Logger (V-Trac winner report)"):
        try:
            states_list = [
                "Connecticut4", "Delaware4", "Florida4", "Georgia4", "Indiana4",
                "Michigan4", "NewJersey4", "NewYork4", "NorthCarolina4", "Ohio4",
                "Ontario4", "Pennsylvania4", "Texas4", "Virginia4", "WestVirginia4"
            ]
        except Exception:
            states_list = []
        w_state = st.selectbox("State", states_list, key="winners_state")
        w_number = st.text_input("Winning number (3 digits)", max_chars=3, key="winners_number")
        if st.button("Generate V-Trac Winner Report", key="btn_gen_winner_vtrac"):
            try:
                from core.winners_vtrac_report import build_vtrac_winner_report
                if not (w_number and len(w_number) == 3 and w_number.isdigit()):
                    st.warning("Enter a 3-digit winning number.")
                else:
                    with st.spinner("Building winner report..."):
                        out_path = build_vtrac_winner_report(w_state, w_number)
                    rel = os.path.relpath(out_path)
                    st.success("Winner report generated.")
                    st.markdown(f"[Open report]({rel})")
            except Exception as e:
                st.error(f"Winners Logger failed: {e}")

    # Winners Logger (Analyzer-style full report)
    with st.expander("Winners Logger (Analyzer-style full report)"):
        w_state2 = st.selectbox("State", [
            "Connecticut4", "Delaware4", "Florida4", "Georgia4", "Indiana4",
            "Michigan4", "NewJersey4", "NewYork4", "NorthCarolina4", "Ohio4",
            "Ontario4", "Pennsylvania4", "Texas4", "Virginia4", "WestVirginia4"
        ], key="winners_state_full")
        col_a, col_b = st.columns(2)
        with col_a:
            mid_win = st.text_input("Midday winner (3 digits)", max_chars=3, key="winners_mid_full")
        with col_b:
            eve_win = st.text_input("Evening winner (3 digits)", max_chars=3, key="winners_eve_full")
        # Dev Health (diagnostics only; does not affect processing)
        try:
            show_dev_full = st.checkbox("Show Dev Health (Winners Full)", value=False, key="winners_full_dev")
        except Exception:
            show_dev_full = False
        if show_dev_full:
            import sys as _sys, os as _os
            import importlib as _il
            from pathlib import Path as _P
            health_box = st.container()
            health_box.markdown("**System Health (Winners Full)**")
            health_box.caption(f"cwd: {_os.getcwd()}")
            health_box.caption(f"python: {_sys.executable}")
            try:
                _modpkg = _sys.modules.get('modules')
                health_box.caption("modules bound: " + (getattr(_modpkg, '__file__', '<package>') or '<package>'))
            except Exception as _se:
                health_box.caption("modules bound: unavailable: " + str(_se))
            try:
                with _project_modules_first():
                    _vref = _il.import_module('modules.vtrac_reference')
                    health_box.caption("vtrac_reference: " + getattr(_vref, '__file__', 'unknown'))
            except Exception as _se:
                health_box.caption("vtrac_reference: unavailable: " + str(_se))
            try:
                _wrp = _P(PROJECT_ROOT) / 'modules' / 'winner_report_full.py'
                health_box.caption("winner_report_full: " + (str(_wrp) if _wrp.exists() else 'missing'))
            except Exception:
                pass
            try:
                if w_state2:
                    _td = _P('data') / 'outputs' / 'tables' / w_state2
                    health_box.caption(f"tables_dir: {_td} (exists={_td.exists()})")
                    for _sec in ("Midday", "Evening", "Combined"):
                        _f = _td / f"{w_state2}_{_sec}_combined.csv"
                        health_box.caption(f"{_sec}: {_f.name} exists={_f.exists()}")
            except Exception:
                pass
        if st.button("Generate Analyzer-style Report", key="btn_gen_winner_full"):
            try:
                # Ensure imports resolve to project modules, not staged Aux
                import sys as _sys, os as _os, importlib.util as _iu
                from _import_hygiene import project_modules_first as _pmf
                with _pmf():
                    try:
                        _sys.modules.pop('modules')
                        _sys.modules.pop('modules.winner_report_full')
                    except KeyError:
                        pass
                    try:
                        from modules.winner_report_full import write_winner_full_report
                    except Exception as _ie:
                        # Fallback: import the builder directly from file path
                        _wr_path = _os.path.join(str(PROJECT_ROOT), 'modules', 'winner_report_full.py')
                        if _os.path.exists(_wr_path):
                            _spec = _iu.spec_from_file_location('modules.winner_report_full_fallback', _wr_path)
                            if _spec and _spec.loader:
                                _mod = _iu.module_from_spec(_spec)
                                _spec.loader.exec_module(_mod)
                                write_winner_full_report = getattr(_mod, 'write_winner_full_report', None)
                        if not callable(locals().get('write_winner_full_report', None)):
                            # provide debugging breadcrumbs
                            _mod_pkg = _sys.modules.get('modules')
                            _mf = getattr(_mod_pkg, '__file__', 'unknown') if _mod_pkg else 'unbound'
                            raise ImportError(f"winner_report_full import failed: {_ie}; modules.__file__={_mf}")
                generated = []
                if mid_win and len(mid_win) == 3 and mid_win.isdigit():
                    with st.spinner("Building full report (Midday)..."):
                        p_mid = write_winner_full_report(w_state2, mid_win)
                    generated.append(("Midday", p_mid))
                if eve_win and len(eve_win) == 3 and eve_win.isdigit():
                    with st.spinner("Building full report (Evening)..."):
                        p_eve = write_winner_full_report(w_state2, eve_win)
                    generated.append(("Evening", p_eve))
                if not generated:
                    st.warning("Enter at least one 3-digit winner (Midday or Evening).")
                else:
                    for label, path_out in generated:
                        rel_full = os.path.relpath(path_out)
                        st.success(f"{label} winner report generated.")
                        st.markdown(f"[Open report]({rel_full})")
            except Exception as e:
                st.warning("Full report unavailable (missing tables or renderer). Use compact index report above.")
                st.caption(str(e))

    try:
        import pandas as _pd
        from pathlib import Path as _Path

        cache_key = "cc_variant_cache"
        if st.button("Refresh Draw Tables", key="refresh_variant_tables"):
            st.session_state.pop(cache_key, None)

        cache = st.session_state.get(cache_key)

        if cache is None:
            variant_specs = [
                ("Combined", "combined"),
                ("Midday", "midday"),
                ("Evening", "evening"),
            ]
            variant_order = {spec[1]: idx for idx, spec in enumerate(variant_specs)}
            variant_display = {spec[1]: spec[0] for spec in variant_specs}

            try:
                _aux_loader = _load_aux_loaders_real()
                load_state_draws = getattr(_aux_loader, "load_state_draws", None)
            except Exception:
                load_state_draws = None

            if not callable(load_state_draws):
                raise RuntimeError("aux_loaders.load_state_draws unavailable")

            try:
                with _project_modules_first():
                    from modules.vtrac_reference import get_vtrac_index as _cc_get_vtrac_index
            except Exception:
                _cc_get_vtrac_index = None

            draws_root = _Path("data/cleaned/draws")
            if not draws_root.exists():
                draws_root = _Path("data/cleaned")

            cleaned_dir = draws_root
            if not cleaned_dir.exists():
                st.warning("No cleaned data found in data/cleaned.")
                return

            state_candidates = set()
            for csv_path in cleaned_dir.glob("*_draws.csv"):
                stem = csv_path.stem
                if stem.lower().endswith("_draws"):
                    stem = stem[:-6]
                lower = stem.lower()
                base_stem = stem
                for suffix in _CATEGORY_SUFFIXES:
                    if lower.endswith(suffix.lower()):
                        base_stem = stem[: -len(suffix)]
                        break
                state_candidates.add(base_stem.replace("_", " "))

            states = sorted(state_candidates)
            if not states:
                st.warning("No draw CSVs detected in data/cleaned/draws.")
                return

            def _is_double(value: str) -> bool:
                return len(value) == 3 and (
                    value[0] == value[1]
                    or value[1] == value[2]
                    or value[0] == value[2]
                )

            def _draws_since_last_double(draws: list[str]) -> tuple[int, str | None]:
                for idx, combo in enumerate(draws):
                    if _is_double(combo):
                        return idx, combo
                return len(draws), None

            variant_rows: list[dict] = []
            variant_sources: dict[tuple[str, str], str] = {}
            variant_draws: dict[tuple[str, str], list[str]] = {}

            for state_label in states:
                for title, variant_key in variant_specs:
                    draws, src = load_state_draws(state_label, variant=variant_key)
                    if not draws:
                        continue
                    key = (state_label, variant_key)
                    variant_draws[key] = draws
                    if src:
                        variant_sources[key] = src
                    ds, latest = _draws_since_last_double(draws)
                    variant_rows.append(
                        {
                            "State": state_label,
                            "Variant": title,
                            "VariantKey": variant_key,
                            "Draws Since Double": ds,
                        }
                    )

            if not variant_rows:
                st.warning("No draw data available for the selected variants.")
                return

            positional_heat: Dict[tuple[str, str], str] = {}
            positional_notes: Dict[str, str] = {}
            try:
                with _project_modules_first():
                    positional_tool = _load_positional_tool_real()
            except Exception:
                positional_tool = None
            if positional_tool:
                state_variant_draws: Dict[str, Dict[str, List[str]]] = {}
                state_double_flags: Dict[str, bool] = {}
                for row in variant_rows:
                    if row.get("VariantKey") == "combined":
                        ds_val = row.get("Draws Since Double")
                        flag = False
                        try:
                            if ds_val is not None:
                                flag = float(ds_val) >= 71
                        except (TypeError, ValueError):
                            flag = False
                        state_double_flags[row["State"]] = flag
                for (state_label, variant_key), draws in variant_draws.items():
                    if draws:
                        state_variant_draws.setdefault(state_label, {})[variant_key] = draws
                for state_label, variant_map in state_variant_draws.items():
                    if not variant_map:
                        continue
                    due_flag = state_double_flags.get(state_label, False)
                    try:
                        report = positional_tool.analyze_state_variants(
                            variant_map, window=150, topk=3, due_doubles_active=due_flag
                        )
                    except Exception:
                        continue
                    for variant_key, variant_result in report.variant_results.items():
                        if not variant_result or not variant_result.draws_used:
                            continue
                        parts = []
                        for pos_idx in (0, 1, 2):
                            pos_summary = variant_result.position_summaries.get(pos_idx)
                            if not pos_summary or not pos_summary.top_digits:
                                continue
                            top_entry = pos_summary.top_digits[0]
                            parts.append(f"P{pos_idx + 1}:{top_entry.digit}({top_entry.gap})")
                        if parts:
                            positional_heat[(state_label, variant_key)] = " ".join(parts)
                    note_set = sorted({note for note in report.consensus_notes if note})
                    if note_set:
                        positional_notes[state_label] = " | ".join(note_set)
            for row in variant_rows:
                key = (row["State"], row["VariantKey"])
                row["Positional Heat"] = positional_heat.get(key, "")
                row["Positional Notes"] = positional_notes.get(row.get("State"), "") if row.get("VariantKey") == "combined" else ""

            try:
                with _project_modules_first():
                    from analyze_pairs import calculate_overdue_pairs
            except Exception:
                calculate_overdue_pairs = None

            combo_gap_maps: Dict[str, Dict[str, Dict[str, int]]] = {}
            for (state_label, variant_key), draws in variant_draws.items():
                badge = _VARIANT_BADGES.get(variant_key)
                if not badge or not draws:
                    continue
                combo_gap_maps.setdefault(state_label, {})[badge] = _double_combo_gaps(draws)

            pair_display_by_state: Dict[str, List[str]] = {}
            combo_display_by_state: Dict[str, List[str]] = {}
            for state_label in states:
                combined_draws = variant_draws.get((state_label, "combined"))
                top_pairs: List[tuple[str, int]] = []
                if calculate_overdue_pairs and combined_draws:
                    try:
                        _, repeating_overdue, _ = calculate_overdue_pairs(combined_draws[:PAIRS_WINDOW])
                        candidates = [
                            (pair, gap)
                            for pair, gap in repeating_overdue.items()
                            if pair and len(pair) == 2 and pair[0] == pair[1]
                        ]
                        candidates.sort(key=lambda item: item[1], reverse=True)
                        top_pairs = candidates[:4]
                    except Exception:
                        top_pairs = []
                pair_cells: List[str] = []
                combo_cells: List[str] = []
                badge_maps = combo_gap_maps.get(state_label, {})
                for idx in range(4):
                    if idx < len(top_pairs):
                        pair_entry = top_pairs[idx]
                        pair_cells.append(_format_pair_value(pair_entry))
                        combos = _collect_combo_entries(pair_entry[0], badge_maps)
                        combo_cells.append(_format_combo_cell(combos))
                    else:
                        pair_cells.append("-")
                        combo_cells.append("-")
                pair_display_by_state[state_label] = pair_cells
                combo_display_by_state[state_label] = combo_cells

            for row in variant_rows:
                state_label = row.get("State")
                pair_cells = pair_display_by_state.get(state_label, ["-"] * 4)
                combo_cells = combo_display_by_state.get(state_label, ["-"] * 4)
                row["Most Due Pair"] = pair_cells[0]
                row["2nd Most Due Pair"] = pair_cells[1]
                row["3rd Most Due Pair"] = pair_cells[2]
                row["4th Most Due Pair"] = pair_cells[3]
                row["Combos (Most Due Pair)"] = combo_cells[0]
                row["Combos (2nd Pair)"] = combo_cells[1]
                row["Combos (3rd Pair)"] = combo_cells[2]
                row["Combos (4th Pair)"] = combo_cells[3]

            df_doubles = _pd.DataFrame(variant_rows)
            df_doubles["VariantOrder"] = df_doubles["VariantKey"].map(lambda key: variant_order.get(key, 99))
            df_doubles.sort_values(
                ["Draws Since Double", "VariantOrder", "State"],
                ascending=[False, True, True],
                inplace=True,
            )
            drop_cols = [col for col in ("VariantKey", "VariantOrder") if col in df_doubles.columns]
            df_display = df_doubles.drop(columns=drop_cols)
            ordered_cols = [
                "State",
                "Variant",
                "Draws Since Double",
                "Positional Heat",
                "Positional Notes",
                "Most Due Pair",
                "2nd Most Due Pair",
                "3rd Most Due Pair",
                "4th Most Due Pair",
                "Combos (Most Due Pair)",
                "Combos (2nd Pair)",
                "Combos (3rd Pair)",
                "Combos (4th Pair)",
            ]
            remaining = [col for col in df_display.columns if col not in ordered_cols]
            df_display = df_display.loc[:, [col for col in ordered_cols if col in df_display.columns] + remaining]

            missing_variants = [
                f"{state_label} {variant_display[variant_key]}"
                for state_label in states
                for _, variant_key in variant_specs
                if variant_key != "combined" and (state_label, variant_key) not in variant_draws
            ]

            cache = {
                "df": df_display,
                "variant_draws": variant_draws,
                "variant_sources": variant_sources,
                "variant_order": variant_order,
                "variant_display": variant_display,
                "missing": missing_variants,
            }
            st.session_state[cache_key] = cache

        variant_order = cache["variant_order"]
        variant_display = cache["variant_display"]
        df_display = cache["df"]
        variant_draws = cache["variant_draws"]
        variant_sources = cache["variant_sources"]
        missing_variants = cache["missing"]

        st.subheader("States Ranked by Draws Since Double (Combined / Midday / Evening)")
        st.dataframe(df_display, use_container_width=True)
        if _cc_get_vtrac_index:
            repeat_rows: list[dict] = []
            for (state_label, variant_key), draws in variant_draws.items():
                if not draws:
                    continue
                overlay = _build_vtrac_overlay(draws, _cc_get_vtrac_index)
                repeat_summary = _summarize_vtrac_repeats(draws, _cc_get_vtrac_index)
                repeat_rows.append({
                    "State": state_label,
                    "Variant": variant_display.get(variant_key, variant_key.title()),
                    "VariantKey": variant_key,
                    "Current Index": repeat_summary.get("current_index") or "-",
                    "Current Streak": repeat_summary.get("current_streak", 0),
                    "Last Repeat (draws)": repeat_summary.get("last_repeat_gap"),
                    "Last Repeat Index": repeat_summary.get("last_repeat_index") or "-",
                    "Max Streak": repeat_summary.get("max_streak", 0),
                    "Window": overlay.get("window", len(draws)),
                })
            if repeat_rows:
                df_repeats = _pd.DataFrame(repeat_rows)
                df_repeats["VariantOrder"] = df_repeats["VariantKey"].map(lambda key: variant_order.get(key, 99))
                df_repeats.sort_values(
                    ["Current Streak", "Last Repeat (draws)", "VariantOrder", "State"],
                    ascending=[False, True, True, True],
                    inplace=True,
                )
                repeat_display = df_repeats[[
                    "State",
                    "Variant",
                    "Current Index",
                    "Current Streak",
                    "Last Repeat (draws)",
                    "Last Repeat Index",
                    "Max Streak",
                    "Window",
                ]]
                st.subheader(f"V-TRAC Repeat Watch (window {VTRAC_INDEX_WINDOW} draws)")
                repeat_display = repeat_display.fillna("-")
                st.dataframe(repeat_display, use_container_width=True)
                st.caption("Last repeat counts from the most recent draw (0 = immediate repeat).")
        else:
            st.caption("V-TRAC repeat watch unavailable (resolver missing).")


        if variant_sources:
            sample_sources = sorted(_Path(src).name for src in variant_sources.values())
            preview = ", ".join(sample_sources[:6])
            if len(sample_sources) > 6:
                preview += " ..."
            st.caption(f"Draw sources ({len(variant_sources)} files): {preview}")
        if missing_variants:
            st.caption("No draws for: " + ", ".join(missing_variants))

        rows_ba: list[dict] = []
        ba_source_sets: dict[str, set[str]] = {}
        ba_results_cache: dict[tuple[str, str], dict] = {}

        try:
            _ba = _load_blackapple_real()
            analyze_blackapple = _ba.analyze_blackapple
            ba_status_label = _ba.ba_status_label

            for (state_label, variant_key), draws in variant_draws.items():
                ba_input = [d for d in draws if not (isinstance(d, str) and set(d) == {'0'})]
                if not ba_input:
                    ba_input = draws
                ba_result = analyze_blackapple(ba_input)
                ba_results_cache[(state_label, variant_key)] = ba_result
                status = ba_status_label(ba_result.get("score", 0))
                trig = ba_result.get("triggers", {})
                triggers: list[str] = []
                if trig.get("mirror"):
                    triggers.append("Mirror")
                roots = trig.get("root_due", [])
                if roots:
                    triggers.append("Root " + "/".join(map(str, roots)))
                pattern = trig.get("pattern", {})
                if pattern.get("extreme_due"):
                    triggers.append("SSS/TTT")
                if pattern.get("mixed_due"):
                    triggers.append("SST/STS/TSS")
                floats = trig.get("floating", [])
                if floats:
                    triggers.append("Float " + "".join(floats))
                candidates = ba_result.get("candidates", [])
                examples = " ".join(c.get("combo", "") for c in candidates[:3])
                rows_ba.append(
                    {
                        "State": state_label,
                        "Variant": variant_display.get(variant_key, variant_key.title()),
                        "VariantKey": variant_key,
                        "BA-Score": ba_result.get("score", 0),
                        "Status": status,
                        "Triggers": ", ".join(triggers),
                        "#Candidates": len(candidates),
                        "Examples": examples,
                    }
                )
                src = variant_sources.get((state_label, variant_key))
                if src:
                    ba_source_sets.setdefault(variant_key, set()).add(_Path(src).name)

            if rows_ba:
                df_ba = _pd.DataFrame(rows_ba)
                df_ba["VariantOrder"] = df_ba["VariantKey"].map(lambda key: variant_order.get(key, 99))
                df_ba.sort_values(
                    ["BA-Score", "#Candidates", "VariantOrder", "State"],
                    ascending=[False, False, True, True],
                    inplace=True,
                )
                df_ba_display = df_ba.drop(columns=["VariantKey", "VariantOrder"])
                st.subheader("Blackapple Alerts (All States / Variants)")
                st.dataframe(df_ba_display, use_container_width=True)
                if ba_source_sets:
                    pieces = []
                    for variant_key in variant_order:
                        names = ba_source_sets.get(variant_key)
                        if not names:
                            continue
                        sample = ", ".join(sorted(names)[:3])
                        if len(names) > 3:
                            sample += " ..."
                        pieces.append(f"{variant_display.get(variant_key, variant_key.title())}: {sample}")
                    if pieces:
                        st.caption("Blackapple draw sources: " + " | ".join(pieces))
            else:
                st.caption("Blackapple alerts unavailable for current variants.")

            for (state_label, variant_key), ba_result in ba_results_cache.items():
                variant_label = variant_display.get(variant_key, variant_key.title())
                exp_label = f"{state_label} ? {variant_label} candidates"
                with st.expander(exp_label):
                    src = variant_sources.get((state_label, variant_key))
                    if src:
                        st.caption(f"Draw source: {src} ({len(variant_draws[(state_label, variant_key)])})")
                    candidates = ba_result.get("candidates", [])
                    if not candidates:
                        st.caption("No candidates found.")
                        continue
                    import pandas as _pd  # local import for rendering
                    rows_detail = []
                    for cand in candidates:
                        tags = cand.get("tags", [])
                        if isinstance(tags, set):
                            tags = sorted(tags)
                        rows_detail.append(
                            {
                                "Combo": cand.get("combo", ""),
                                "Score": cand.get("score", 0),
                                "Tags": " ".join(tags),
                            }
                        )
                    st.dataframe(_pd.DataFrame(rows_detail), use_container_width=True)
        except Exception as _e:
            st.caption(f"Blackapple table unavailable: {_e}")
    except Exception as e:
        try:
            import sys as _sys
            with st.expander("System Health (Draws View)"):
                st.caption(f"cwd: {os.getcwd()}")
                st.caption(f"python: {_sys.executable}")
                try:
                    _ba = _load_blackapple_real()
                    st.caption(f"BA module: {getattr(_ba, '__file__', 'unknown')}")
                except Exception as _se:
                    st.caption(f"BA module: unavailable: {_se}")
            st.caption(f"windows: pairs={PAIRS_WINDOW}, positional={POSITIONAL_WINDOW}, sums={SUMS_WINDOW}, vtrac_index={VTRAC_INDEX_WINDOW}, combinations={COMBINATION_WINDOW}")
        except Exception:
            pass
        st.warning(f"Control Center draws view unavailable: {e}")
def show_aux_page(state: str) -> None:
    """Render the Auxiliary Tools page."""
    import streamlit as st
    import pandas as pd
    # Loader from legacy extractor (safe to reuse just for CSV reads)
    try:
        from modules.module_d_auxiliary_tools.refactored.extractor import extract_draw_list
    except Exception:
        extract_draw_list = None

    # Working modules (staged copy) - used only inside Aux page
    _AUX_WORKING_AVAILABLE = False
    try:
        with _aux_working_first():
            from modules.analyze_pairs import (
                calculate_overdue_pairs,
                get_top_overdue_repeating_pairs,
                get_vtrac_statuses,
                get_doubles_history,
                COLOR_LATE,
                COLOR_VERY_LATE,
                COLOR_PENDING,
                PAIRS_WINDOW,
            )
            from modules.vtrac_reference import VTRAC_DISPLAY, get_vtrac_index
        _AUX_WORKING_AVAILABLE = True
    except Exception:
        _AUX_WORKING_AVAILABLE = False
    
    st.title(f"Auxiliary Tools - {state}")
    st.write(f"Advanced lottery analysis tools for {state}")

    state_key = ''.join(ch if ch.isalnum() else '_' for ch in state) or 'state'

    variant_options = [
        ("Combined", "combined"),
        ("Midday", "midday"),
        ("Evening", "evening"),
    ]
    variant_labels = [label for label, _ in variant_options]
    variant_label_map = {key: label for label, key in variant_options}
    selected_variant_label = st.radio("Draw variant", variant_labels, index=0, key="aux_variant")
    selected_variant_key = dict(variant_options)[selected_variant_label]
    show_purple = selected_variant_key == "combined"

    
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
            st.caption("windows: pairs={PAIRS_WINDOW}, positional={POSITIONAL_WINDOW}, sums={SUMS_WINDOW}, vtrac_index={VTRAC_INDEX_WINDOW}, combinations={COMBINATION_WINDOW}")
            try:
                _aux = _load_aux_loaders_real()
                load_state_draws = getattr(_aux, "load_state_draws", None)
                if callable(load_state_draws):
                    for label, variant_key in (("Combined", "combined"), ("Midday", "midday"), ("Evening", "evening")):
                        dr, src = load_state_draws(state, variant=variant_key)
                        if src:
                            count = len(dr) if isinstance(dr, list) else 0
                            st.caption(f"{label} draws: {src} ({count})")
                        else:
                            st.caption(f"{label} draws: missing")
            except Exception:
                pass
            # Show which staged modules are actually bound (debug-only)
            try:
                with _aux_working_first():
                    import modules.analyze_pairs as _ap  # type: ignore
                    import modules.vtrac_reference as _vr  # type: ignore
                st.caption("ap: " + str(getattr(_ap, "__file__", "unknown")))
                st.caption("vr: " + str(getattr(_vr, "__file__", "unknown")))
                try:
                    st.caption("vr has VTRAC_DISPLAY: " + str(hasattr(_vr, "VTRAC_DISPLAY")))
                except Exception:
                    pass
            except Exception as _e_dbg:
                st.caption("aux staged bindings: unavailable: " + str(_e_dbg))
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
    def cached_aux_analysis(state_name: str, variant: str):
        if not (_AUX_WORKING_AVAILABLE):
            return None
        with _aux_working_first():
            draws = []
            source = None
            try:
                _aux_loader = _load_aux_loaders_real()
                load_state_draws = getattr(_aux_loader, "load_state_draws", None)
            except Exception:
                load_state_draws = None

            if callable(load_state_draws):
                try:
                    draws, source = load_state_draws(state_name, variant=variant)
                except Exception:
                    draws, source = [], None

            if not draws:
                draws = _load_draws_from_csv_candidates(state_name, variant=variant)

            if not draws and variant == "combined" and extract_draw_list is not None:
                try:
                    draws = extract_draw_list(state_name, None)
                except Exception:
                    draws = []

            if not draws and variant == "combined":
                try:
                    local_excel_path = os.path.normpath("data/original/Pick3StatsC4.xlsm")
                    if os.path.exists(local_excel_path):
                        from modules.run_process import run_process

                        _ = run_process(local_excel_path, max_draws=1000, analysis_draws=100)
                        if callable(load_state_draws):
                            try:
                                draws, source = load_state_draws(state_name, variant=variant)
                            except Exception:
                                draws, source = [], None
                        if not draws:
                            draws = _load_draws_from_csv_candidates(state_name, variant=variant)
                except Exception:
                    pass

            if not draws:
                return None

            draws_100 = draws[:PAIRS_WINDOW] if len(draws) >= PAIRS_WINDOW else draws
            draws_1000 = draws[:VTRAC_INDEX_WINDOW] if len(draws) >= VTRAC_INDEX_WINDOW else draws
            draws_pair_window = draws[:PAIRS_WINDOW] if len(draws) >= PAIRS_WINDOW else draws
            nonrep, rep, pair_status = calculate_overdue_pairs(draws, window=PAIRS_WINDOW)
            vstat = get_vtrac_statuses(draws_100, draws_1000)
            top5 = get_top_overdue_repeating_pairs(draws_pair_window, 5)
            doubles = get_doubles_history({state_name: draws})

            overlay = _build_vtrac_overlay(draws_1000, get_vtrac_index)
            repeat_summary = _summarize_vtrac_repeats(draws_1000, get_vtrac_index)

            return {
                "variant": variant,
                "source": source,
                "draws": draws,
                "draws_100": draws_100,
                "draws_1000": draws_1000,
                "nonrep": nonrep,
                "rep": rep,
                "pair_status": pair_status,
                "vstat": vstat,
                "top5": top5,
                "doubles": doubles,
                "vtrac_overlay": overlay,
                "repeat_summary": repeat_summary,
            }
    if st.button("Run Auxiliary Tools Analysis", type="primary"):
        with st.spinner(f"Running {selected_variant_label} auxiliary analysis for {state}..."):
            try:
                results = cached_aux_analysis(state, selected_variant_key)
                if not results:
                    st.error("Working modules unavailable or no draws found.")
                    return

                variant_label = selected_variant_label
                st.caption(f"Variant: {variant_label}")
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
                        st.sidebar.caption(f"[{variant_label}] SUMS | {_calc_sums.__module__}")
                    except Exception as _e:
                        st.sidebar.caption(f"[{variant_label}] SUMS import failed: {_e}")

                analysis_draws = st.session_state.get("analysis_draws", SUMS_WINDOW)
                if callable(_calc_sums):
                    try:
                        sums_stats = _calc_sums(draws, window=analysis_draws)
                    except Exception:
                        sums_stats = {"window": 0, "by_sum": {}, "by_root_sum": {}}
                else:
                    sums_stats = {"window": 0, "by_sum": {}, "by_root_sum": {}}
                results["sums_stats"] = sums_stats
                with st.expander("Positional Tracker (Combined / Midday / Evening)", expanded=True):
                    pos_window = POSITIONAL_WINDOW
                    pos_topk = 3
                    st.caption(f"Window: {POSITIONAL_WINDOW} draws (Top-K per position: {pos_topk})")
                    try:
                        with _project_modules_first():
                            positional_tool = _load_positional_tool_real()
                    except Exception as _pos_load_err:
                        positional_tool = None
                        st.caption(f"Positional module unavailable: {_pos_load_err}")
                    else:
                        variant_cache: dict[str, Optional[dict]] = {}
                        draws_by_variant: dict[str, List[str]] = {}
                        try:
                            _aux_loader = _load_aux_loaders_real()
                            load_state_draws = getattr(_aux_loader, "load_state_draws", None)
                        except Exception:
                            load_state_draws = None
                        for option_label, option_key in variant_options:
                            cached_variant = cached_aux_analysis(state, option_key)
                            payload = {}
                            if isinstance(cached_variant, dict):
                                payload = dict(cached_variant)
                            variant_draws = payload.get("draws")
                            if not variant_draws and callable(load_state_draws):
                                try:
                                    fallback_draws, fallback_source = load_state_draws(state, variant=option_key)
                                except Exception:
                                    fallback_draws, fallback_source = [], None
                                if fallback_draws:
                                    variant_draws = fallback_draws
                                    payload["draws"] = variant_draws
                                    if fallback_source:
                                        payload.setdefault("source", fallback_source)
                            variant_cache[option_key] = payload if payload else cached_variant
                            if variant_draws:
                                draws_by_variant[option_key] = variant_draws
                        if not draws_by_variant:
                            st.caption("No positional draws available across variants.")
                        else:
                            due_doubles_flag = any(ds >= REPEATING_LATE_THRESHOLD for ds in results.get("rep", {}).values())
                            try:
                                report = positional_tool.analyze_state_variants(
                                    draws_by_variant,
                                    window=pos_window,
                                    topk=pos_topk,
                                    due_doubles_active=due_doubles_flag,
                                )
                            except Exception as _pos_err:
                                st.warning(f"Positional analysis unavailable: {_pos_err}")
                            else:
                                available_variants = [
                                    (label, key)
                                    for label, key in variant_options
                                    if report.variant_results.get(key)
                                    and report.variant_results[key].draws_used
                                ]
                                if not available_variants:
                                    st.caption("Positional metrics unavailable for selected draws.")
                                else:
                                    css_injected = False

                                    def _render_tracker_table(title: str, variant_result, source_path: Optional[str]) -> None:
                                        nonlocal css_injected
                                        if not variant_result or not getattr(variant_result, "tracker_grid", None):
                                            st.markdown(f"**{title}**")
                                            st.caption("No positional tracker data.")
                                            return
                                        grid = variant_result.tracker_grid
                                        if not css_injected:
                                            st.markdown(
                                                "<style>.pos-tracker-table{border-collapse:separate;border-spacing:0;width:100%;margin-bottom:12px;}"
                                                ".pos-tracker-table th{border:2px solid #c7c7c7;padding:6px;text-align:center;font-size:13px;font-weight:700;background-color:#f5f5f5;}.pos-tracker-table td{border:2px solid #e0e0e0;padding:6px;text-align:center;font-size:14px;font-weight:600;}"
                                                ".pos-tracker-table caption{caption-side:top;text-align:left;font-weight:700;margin-bottom:6px;font-size:15px;}"
                                                "</style>",
                                                unsafe_allow_html=True,
                                            )
                                            css_injected = True
                                        ds_header = ["P1 DS", "P1 DIG", "P2 DS", "P2 DIG", "P3 DS", "P3 DIG"]
                                        header_html = "<tr><th>Rank</th>" + "".join(f"<th>{h}</th>" for h in ds_header) + "</tr>"
                                        max_rows = pos_topk
                                        rows_html = []
                                        for rank in range(max_rows):
                                            cells_html = [f"<td>{rank + 1}</td>"]
                                            for pos_idx in (0, 1, 2):
                                                tracker_cells = grid.get(pos_idx, [])
                                                if rank < len(tracker_cells):
                                                    cell = tracker_cells[rank]
                                                    ds_val = cell.draws_since
                                                    style = "background-color:#ffea70;padding:2px 8px;border-radius:6px;font-weight:700;font-size:1.15em;display:inline-block;"
                                                    if getattr(cell, "hard_due", False):
                                                        style += "color:#d60000;"
                                                    digit_html = f"<span style='{style}'>{cell.digit}</span>"
                                                else:
                                                    ds_val = ""
                                                    digit_html = ""
                                                cells_html.append(f"<td>{ds_val}</td>")
                                                cells_html.append(f"<td>{digit_html}</td>")
                                            rows_html.append("<tr>" + "".join(cells_html) + "</tr>")
                                        table_html = (
                                            f"<table class='pos-tracker-table'><thead>{header_html}</thead><tbody>"
                                            + "".join(rows_html)
                                            + "</tbody></table>"
                                        )
                                        st.markdown(f"**{title}**", unsafe_allow_html=True)
                                        if source_path:
                                            st.caption(f"Draw source: {source_path} ({variant_result.draws_used})")
                                        st.markdown(table_html, unsafe_allow_html=True)

                                    for label, key in available_variants:
                                        variant_result = report.variant_results.get(key)
                                        cached_variant = variant_cache.get(key) or {}
                                        source_path = cached_variant.get("source") if isinstance(cached_variant, dict) else None
                                        source_label = ""
                                        if source_path:
                                            try:
                                                source_label = Path(source_path).name
                                            except Exception:
                                                source_label = source_path
                                        _render_tracker_table(f"{state}_{label}", variant_result, source_label)

                                    note_set = sorted({note for note in report.consensus_notes if note})
                                    if note_set:
                                        st.caption(" | ".join(note_set))
                                    double_notes = [note for note in getattr(report, 'double_pressure_notes', []) if note]
                                    if double_notes:
                                        st.caption("Double pressure: " + " | ".join(double_notes))
                                    st.caption("Hard-due: Combined >= 55, Midday/Evening >= 40. Tags: XVAR-Cons = aligned variants, Mirror-Echo = mirror support, Double-Pressure = digit/mirror pressing two positions.")
                                    css_style = (
                                        "<style>"
                                        ".pos-summary-table,.pos-shortlist-table{border-collapse:separate;border-spacing:0;width:100%;margin-bottom:10px;}"
                                        ".pos-summary-table th,.pos-shortlist-table th{border:2px solid #c7c7c7;padding:6px 8px;text-align:center;font-size:13px;font-weight:700;background-color:#f8f8f8;}"
                                        ".pos-summary-table td,.pos-shortlist-table td{border:2px solid #e0e0e0;padding:6px 8px;text-align:center;font-size:13px;font-weight:600;}"
                                        ".pos-shortlist-table td:first-child{font-weight:700;}"
                                        "</style>"
                                    )
                                    st.markdown("**Cross-variant pressure summary**")
                                    import pandas as pd
                                    summary_cols = st.columns(3)
                                    meta_css_injected = False
                                    for pos_idx, column in enumerate(summary_cols):
                                        with column:
                                            st.markdown(f"P{pos_idx + 1}")
                                            agg_items = report.aggregated_digits.get(pos_idx, [])
                                            if not agg_items:
                                                st.caption("--")
                                                continue
                                            if not meta_css_injected:
                                                st.markdown(css_style, unsafe_allow_html=True)
                                                meta_css_injected = True
                                            rows = []
                                            for agg in agg_items[:5]:
                                                hits = ", ".join(f"{variant[:1].upper()}#{rank}" for variant, rank in agg.occurrences)
                                                rows.append({
                                                    "Digit": agg.digit,
                                                    "Score": round(agg.score, 2),
                                                    "Hits": hits,
                                                    "Tags": " ".join(sorted(agg.tags)),
                                                })
                                            summary_html = pd.DataFrame(rows).to_html(classes="pos-summary-table", index=False, escape=False)
                                            st.markdown(summary_html, unsafe_allow_html=True)
                                    if report.candidates:
                                        if not meta_css_injected:
                                            st.markdown(css_style, unsafe_allow_html=True)
                                            meta_css_injected = True
                                        st.markdown("**Positional shortlist**")
                                        candidate_rows = []
                                        for cand in report.candidates:
                                            candidate_rows.append({
                                                "Combo": cand.combo,
                                                "Score": round(cand.score, 2),
                                                "Ranks": "-".join(str(r) for r in cand.ranks if r),
                                                "Root": cand.digital_root,
                                                "VTRAC": "" if cand.vtrac_index is None else cand.vtrac_index,
                                                "Tags": " ".join(sorted(cand.tags)),
                                            })
                                        shortlist_html = pd.DataFrame(candidate_rows).to_html(classes="pos-shortlist-table", index=False, escape=False)
                                        st.markdown(shortlist_html, unsafe_allow_html=True)
                # --- V-TRAC Table (Working logic) ---
                st.subheader("V-TRAC Analysis (Working logic)")
                import pandas as _pd
                rows = []
                rows_plain = []
                overlay = results.get("vtrac_overlay")
                if not overlay:
                    draws_1000 = results.get("draws_1000", draws)
                    overlay = _build_vtrac_overlay(draws_1000, get_vtrac_index)
                    results["vtrac_overlay"] = overlay
                repeat_summary = results.get("repeat_summary")
                if not repeat_summary:
                    draws_1000 = results.get("draws_1000", draws)
                    repeat_summary = _summarize_vtrac_repeats(draws_1000, get_vtrac_index)
                    results["repeat_summary"] = repeat_summary
                index_draws_since_overlay = overlay.get("draws_since", {})
                top10_overdue_overlay = overlay.get("top_overdue", [])
                for entry in VTRAC_DISPLAY:
                    idx = entry["Index"]
                    singles = entry["Singles"].split() if entry["Singles"] else []
                    doubles = entry["Doubles"].split() if entry["Doubles"] else []
                    sdict = vstat.get(idx, {}).get("singles_status", {})
                    ddict = vstat.get(idx, {}).get("doubles_status", {})
                    s_html = " ".join([
                        (_format_combo(c, sdict, pair_status) + _sums_badge_for(c, results.get("sums_stats", {})))
                        for c in singles
                    ]) if singles else "&nbsp;"
                    d_html = " ".join([
                        (_format_combo(c, ddict, pair_status) + _sums_badge_for(c, results.get("sums_stats", {})))
                        for c in doubles
                    ]) if doubles else "&nbsp;"
                    idx_style = vstat.get(idx, {}).get("index_style", {})
                    row_class = ""
                    badge = ""
                    if idx_style.get("bg") == "green":
                        row_class = "row-green"
                        badge = f'<sup class="rank-badge">{idx_style.get("rank")}</sup>' if idx_style.get("rank") else ""
                    else:
                        if idx in top10_overdue_overlay:
                            row_class = "row-red"
                            rank_num = top10_overdue_overlay.index(idx) + 1
                            ds_disp = index_draws_since_overlay.get(idx, "")
                            badge = f'<sup class="rank-badge">{rank_num} ({ds_disp})</sup>'
                        elif idx_style.get("bg") == "red":
                            row_class = "row-red"
                            badge = f'<sup class="rank-badge">{idx_style.get("rank")}</sup>' if idx_style.get("rank") else ""
                    index_cell = f'<div class="{row_class}">{idx}{badge}</div>' if row_class else f'{idx}{badge}'
                    singles_cell = f'<div class="{row_class}">{s_html}{badge}</div>' if row_class else f'{s_html}{badge}'
                    doubles_cell = f'<div class="{row_class}">{d_html}{badge}</div>' if row_class else f'{d_html}{badge}'
                    rows.append({"Index": index_cell, "Singles": singles_cell, "Doubles": doubles_cell})
                    rows_plain.append({"Index": idx, "Singles": " ".join(singles), "Doubles": " ".join(doubles)})
                df_v = _pd.DataFrame(rows)
                st.markdown(df_v.to_html(escape=False, index=False), unsafe_allow_html=True)
                df_plain = _pd.DataFrame(rows_plain)
                st.download_button(
                    "Download V-TRAC Table (Working) CSV",
                    df_plain.to_csv(index=False).encode("utf-8"),
                    file_name=f"{state}_vtrac_working.csv",
                    mime="text/csv",
                )

                # --- Overdue Pairs (Working logic) ---

                st.subheader("Overdue Pairs Analysis (Working logic)")
                rep = results.get("rep", {})
                nonrep = results.get("nonrep", {})
                rep_red = sorted([pair for pair, ds in rep.items() if ds >= REPEATING_VERY_LATE_THRESHOLD])
                rep_blue = sorted([
                    pair for pair, ds in rep.items()
                    if REPEATING_LATE_THRESHOLD <= ds < REPEATING_VERY_LATE_THRESHOLD
                ])
                rep_purple = sorted([
                    pair for pair, ds in rep.items()
                    if PAIR_PENDING_THRESHOLD <= ds < REPEATING_LATE_THRESHOLD
                ])
                nr_red = sorted([pair for pair, ds in nonrep.items() if ds >= NONREPEATING_VERY_LATE_THRESHOLD])
                nr_blue = sorted([
                    pair for pair, ds in nonrep.items()
                    if NONREPEATING_LATE_THRESHOLD <= ds < NONREPEATING_VERY_LATE_THRESHOLD
                ])
                nr_purple = sorted([
                    pair for pair, ds in nonrep.items()
                    if PAIR_PENDING_THRESHOLD <= ds < NONREPEATING_LATE_THRESHOLD
                ])

                st.info(
                    ("**Overdue thresholds**\n"
                     f"- Window: {PAIRS_WINDOW} draws\n"
                     f"- Repeating pairs (00, 11, etc): red >= {REPEATING_VERY_LATE_THRESHOLD}, blue >= {REPEATING_LATE_THRESHOLD}, purple >= {PAIR_PENDING_THRESHOLD}\n"
                     f"- Non-repeating pairs (01, 23, etc): red >= {NONREPEATING_VERY_LATE_THRESHOLD}, blue >= {NONREPEATING_LATE_THRESHOLD}, purple >= {PAIR_PENDING_THRESHOLD}")
                )
                st.caption("Color priority (digits/pairs overlap): red > blue > purple")

                rep_col, nonrep_col = st.columns(2)
                with rep_col:
                    st.markdown("<b>Repeating Pairs (Doubles)</b>", unsafe_allow_html=True)
                    st.markdown(
                        f"<span class='red'>Red (>= {REPEATING_VERY_LATE_THRESHOLD}):</span> "
                        + (", ".join(rep_red) if rep_red else "None"),
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f"<span class='blue'>Blue (>= {REPEATING_LATE_THRESHOLD}):</span> "
                        + (", ".join(rep_blue) if rep_blue else "None"),
                        unsafe_allow_html=True,
                    )
                    if show_purple:
                        st.markdown(
                            f"<span class='purple'>Purple (>= {PAIR_PENDING_THRESHOLD}):</span> "
                            + (", ".join(rep_purple) if rep_purple else "None"),
                            unsafe_allow_html=True,
                        )
                with nonrep_col:
                    st.markdown("<b>Non-Repeating Pairs</b>", unsafe_allow_html=True)
                    st.markdown(
                        f"<span class='red'>Red (>= {NONREPEATING_VERY_LATE_THRESHOLD}):</span> "
                        + (", ".join(nr_red) if nr_red else "None"),
                        unsafe_allow_html=True,
                    )
                    st.markdown(
                        f"<span class='blue'>Blue (>= {NONREPEATING_LATE_THRESHOLD}):</span> "
                        + (", ".join(nr_blue) if nr_blue else "None"),
                        unsafe_allow_html=True,
                    )
                    if show_purple:
                        st.markdown(
                            f"<span class='purple'>Purple (>= {PAIR_PENDING_THRESHOLD}):</span> "
                            + (", ".join(nr_purple) if nr_purple else "None"),
                            unsafe_allow_html=True,
                        )

                # --- Four-panels row
                latest_col, pairs_col, combos_col, top5_col = st.columns(4, gap="small")
                with latest_col:
                    st.subheader("Latest Draws")
                    import pandas as _pd
                    df_latest = _pd.DataFrame({"Draw": draws[:5]})
                    st.dataframe(df_latest, use_container_width=True)
                with pairs_col:
                    st.subheader("Pairs Analysis Results")
                    times_drawn = {}
                    for draw_value in draws[:150]:
                        if not isinstance(draw_value, str) or len(draw_value) != 3:
                            continue
                        d1, d2, d3 = draw_value[0], draw_value[1], draw_value[2]
                        for raw_pair in (d1 + d2, d2 + d3, d1 + d3):
                            pair = "".join(sorted(raw_pair))
                            times_drawn[pair] = times_drawn.get(pair, 0) + 1
                    all_pairs = sorted(set(list(nonrep.keys()) + list(rep.keys())))
                    rows_pairs = []
                    for pair in all_pairs:
                        is_repeating = pair[0] == pair[1]
                        overdue = rep.get(pair, 0) if is_repeating else nonrep.get(pair, 0)
                        rows_pairs.append({"Pair": pair, "Times Drawn": times_drawn.get(pair, 0), "Draws Since": overdue})
                    df_pairs = _pd.DataFrame(rows_pairs)
                    if not df_pairs.empty:
                        df_pairs = df_pairs.sort_values("Draws Since", ascending=False)
                    st.dataframe(df_pairs, use_container_width=True)
                with combos_col:
                    st.subheader("Combinations Analysis (Draws Since)")
                    combo_ds = vstat.get(0, {})
                    singles_ds = combo_ds.get("singles_ds", {})
                    doubles_ds = combo_ds.get("doubles_ds", {})
                    safe_rows = []
                    for base, ds in singles_ds.items():
                        status = {}
                        if ds >= COMBO_SINGLE_VERY_LATE_THRESHOLD:
                            status[base] = {"shape_red_circle": True}
                        elif ds >= COMBO_SINGLE_LATE_THRESHOLD:
                            status[base] = {"shape_blue_square": True}
                        html_combo = _format_combo(str(base).zfill(3), status, pair_status)
                        safe_rows.append({"Combo": html_combo, "Type": "Single", "Draws Since": int(ds)})
                    for base, ds in doubles_ds.items():
                        status = {}
                        if ds >= COMBO_DOUBLE_VERY_LATE_THRESHOLD:
                            status[base] = {"shape_red_circle": True}
                        elif ds >= COMBO_DOUBLE_LATE_THRESHOLD:
                            status[base] = {"shape_blue_square": True}
                        html_combo = _format_combo(str(base).zfill(3), status, pair_status)
                        safe_rows.append({"Combo": html_combo, "Type": "Double", "Draws Since": int(ds)})
                    if safe_rows:
                        safe_rows.sort(key=lambda row: row["Draws Since"], reverse=True)
                        dfc_html = _pd.DataFrame(safe_rows)
                        html_table = dfc_html.to_html(escape=False, index=False)
                        st.markdown(
                            f'<div style="max-height: 420px; overflow-y: auto; border: 1px solid #eee; padding: 6px;">{html_table}</div>',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.write("No data")

                with top5_col:
                    st.subheader("Top 5 Most Overdue Repeating Pairs (Working logic)")
                    for pair, overdue in results.get("top5", []):
                        if overdue >= REPEATING_VERY_LATE_THRESHOLD:
                            color = "red"
                        elif overdue >= REPEATING_LATE_THRESHOLD:
                            color = "blue"
                        elif overdue >= PAIR_PENDING_THRESHOLD:
                            color = "purple"
                        else:
                            color = ""
                        line = f"{pair} - {overdue} draws overdue"
                        if color:
                            st.markdown(f"<span class='{color}'>{line}</span>", unsafe_allow_html=True)
                        else:
                            st.write(line)

# Sums Tracking (table)
                if callable(_build_sums_df) and isinstance(sums_stats, dict) and sums_stats.get("by_sum"):
                    try:
                        df_sums = _build_sums_df(sums_stats)
                        html_sums = df_sums.to_html(escape=False, index=False)
                        st.subheader("Sums Tracking")
                        st.caption(f"Window: {SUMS_WINDOW} draws")
                        st.markdown(
                            f'<div style="max-height: 420px; overflow-y: auto; border: 1px solid #eee; padding: 6px;">{html_sums}</div>',
                            unsafe_allow_html=True,
                        )
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
                        ba_draws, ba_src = load_state_draws(state, variant=selected_variant_key)
                    else:
                        ba_draws, ba_src = [], ""

                    ba_input = [d for d in (ba_draws or draws) if not (isinstance(d, str) and set(d) == {'0'})]
                    if not ba_input:
                        ba_input = ba_draws or draws
                    ba = analyze_blackapple(ba_input)
                    status = ba_status_label(ba.get("score", 0))
                    st.subheader("Blackapple Alert")
                    if ba_src:
                        st.caption(f"{variant_label} BA draws: {ba_src} ({len(ba_draws)})")
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
                            "Sums": f"Sigma{t['Sigma']} sD{t['sD']} RS{t['RS']}"
                        })
                    if rows:
                        import pandas as _pd
                        st.dataframe(_pd.DataFrame(rows), use_container_width=True)
                    else:
                        st.caption("No candidate list (insufficient overlap) - still watching triggers.")
                except Exception as _e:
                    st.caption(f"Blackapple panel unavailable: {_e}")
                # Legend / Feature Guide
                with st.expander("Legend / Feature Guide"):
                    st.markdown("""
                    - V-Trac index row tints: light green = last 5 hit (rank 1..5), light red = 5 most overdue (rank 1..5).
                    - Combination shapes:
                      - Red circle: Singles >= 501 draws since; Doubles >= 1000
                      - Blue square: Singles >= 334; Doubles >= 667
                      - Boxed combos: permutations are treated as the same combo
                    - Pairs colors (analysis window based):
                      - Red (Late): non-repeating >= 37, repeating >= 71
                      - Blue (Very Late): non-repeating >= 56, repeating >= 107
                      - Purple (Pending): >= 25
                    """)

                # --- V-Trac Index Hits (Working logic) ---
                import pandas as _pd
                recent_ranks = vstat.get(0, {}).get("recent_index_ranks", {}) if isinstance(vstat.get(0, {}), dict) else {}
                overdue_ranks = vstat.get(0, {}).get("overdue_index_ranks", {}) if isinstance(vstat.get(0, {}), dict) else {}
                if not recent_ranks and not overdue_ranks:
                    for entry in VTRAC_DISPLAY:
                        idx = entry["Index"]
                        ist = vstat.get(idx, {}).get("index_style", {})
                        if ist.get("bg") == "green" and ist.get("rank"):
                            recent_ranks[idx] = ist.get("rank")
                        elif ist.get("bg") == "red" and ist.get("rank"):
                            overdue_ranks[idx] = ist.get("rank")

                overlay = results.get("vtrac_overlay")
                if not overlay:
                    draws_1000 = results.get("draws_1000", draws)
                    overlay = _build_vtrac_overlay(draws_1000, get_vtrac_index)
                    results["vtrac_overlay"] = overlay
                total_len = overlay.get("window", len(results.get("draws_1000", draws)))
                index_draws_since_overlay = overlay.get("draws_since", {})
                top10_overdue_overlay = overlay.get("top_overdue", [])
                recent_rank_values = {}
                for idx, rank_val in recent_ranks.items():
                    try:
                        recent_rank_values[idx] = int(str(rank_val))
                    except Exception:
                        continue
                rows_hits = []
                for idx in range(1, 36):
                    ds = index_draws_since_overlay.get(idx, total_len)
                    if idx in top10_overdue_overlay:
                        rank_num = top10_overdue_overlay.index(idx) + 1
                        status = "Overdue"
                        rank_display = f"{rank_num} ({ds})"
                    elif idx in recent_rank_values:
                        status = "Recent"
                        rank_val = recent_rank_values[idx]
                        rank_display = f"{rank_val} ({ds})" if rank_val > 0 else f"({ds})"
                    else:
                        status = "None"
                        rank_display = ""
                    rows_hits.append({
                        "Index": idx,
                        "Draws Since": ds,
                        "Status": status,
                        "RankDisplay": rank_display,
                    })
                df_hits = _pd.DataFrame(rows_hits)
                if not df_hits.empty:
                    df_hits = df_hits.sort_values("Index")
                st.subheader("V-Trac Index Hits (Working logic)")
                st.dataframe(df_hits, use_container_width=True, hide_index=True)
                st.success(f"{variant_label} auxiliary tools (working logic) completed for {state}")

                variant_payloads = {selected_variant_key: results}
                for variant_label_entry, variant_key in variant_options:
                    if variant_key not in variant_payloads:
                        try:
                            extra_payload = cached_aux_analysis(state, variant_key)
                        except Exception:
                            extra_payload = None
                        if extra_payload:
                            variant_payloads[variant_key] = extra_payload

                with st.expander("Unified Aux View (DEV)", expanded=False):
                    available_keys = [vk for _, vk in variant_options if variant_payloads.get(vk)]
                    if len(available_keys) <= 1:
                        st.caption("Run additional variants to enable the unified view.")
                    else:
                        import pandas as _pd
                        st.caption("Compact summary for Combined/Midday/Evening.")
                        summary_cols = st.columns(len(variant_options))
                        for col, (variant_label_entry, variant_key) in zip(summary_cols, variant_options):
                            payload = variant_payloads.get(variant_key)
                            with col:
                                st.markdown(f"**{variant_label_entry}**")
                                if not payload:
                                    st.caption("No data available.")
                                    continue
                                top_pairs = payload.get("top5") or []
                                if top_pairs:
                                    df_pairs = _pd.DataFrame(top_pairs, columns=["Pair", "Draws Since"])
                                    st.markdown("Top overdue pairs")
                                    st.dataframe(df_pairs, hide_index=True, use_container_width=True)
                                else:
                                    st.caption("No overdue pair data.")
                                doubles_ds = (payload.get("vstat") or {}).get(0, {}).get("doubles_ds", {})
                                if doubles_ds:
                                    rows = sorted(((str(combo).zfill(3), int(ds)) for combo, ds in doubles_ds.items()), key=lambda kv: kv[1], reverse=True)[:6]
                                    df_combos = _pd.DataFrame(rows, columns=["Combo", "Draws Since"])
                                    st.markdown("Longest-miss doubles")
                                    st.dataframe(df_combos, hide_index=True, use_container_width=True)
                                else:
                                    st.caption("No double combo data.")
                                draws_1000 = payload.get("draws_1000") or payload.get("draws") or []
                                if isinstance(draws_1000, list) and draws_1000:
                                    index_first_seen = {}
                                    for i, draw_value in enumerate(draws_1000):
                                        if isinstance(draw_value, str) and len(draw_value) == 3 and len(set(draw_value)) != 1:
                                            idx_val = get_vtrac_index(draw_value)
                                            if idx_val and idx_val not in index_first_seen:
                                                index_first_seen[idx_val] = i
                                    total_len = len(draws_1000)
                                    index_draws = {i: index_first_seen.get(i, total_len) for i in range(1, 36)}
                                    top_overdue = sorted(index_draws.items(), key=lambda kv: kv[1], reverse=True)[:6]
                                    df_vtrac = _pd.DataFrame(top_overdue, columns=["V-TRAC Index", "Draws Since"])
                                    st.markdown("Overdue V-TRAC indexes")
                                    st.dataframe(df_vtrac, hide_index=True, use_container_width=True)
                                else:
                                    st.caption("No V-TRAC summary.")
                
            except Exception as e:
                st.error(f"{variant_label} analysis failed: {e}")
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
        try:
            show_dev_d = st.sidebar.checkbox("Show Dev Health", value=False, key="dev_health_dr")
        except Exception:
            show_dev_d = False
        if show_dev_d:
            import sys as _sys
            with st.expander("System Health (Digit Reduction)"):
                st.caption("cwd: " + os.getcwd())
                st.caption("python: " + _sys.executable)
                try:
                    from core.module_b_digit_reduction import run_digit_reduction as _rdr
                    st.caption("DR module: " + str(getattr(_rdr, "__module__", "unknown")))
                except Exception as _se:
                    st.caption("DR module: unavailable: " + str(_se))
                st.caption("tables_root: " + str(tables_root) + " (exists=" + str(tables_root.exists()) + ")")
        st.error("No processed tables found. Run the data pipeline first.")
        return

    state_tables_dir = tables_root / state
    if not state_tables_dir.exists():
        available = [p.name for p in tables_root.iterdir() if p.is_dir()]
        st.error(f"No tables found for {state}. Available states: {available}")
        return

    base_analysis_dir = Path(get_analysis_output_dir())
    base_dir, training_dir, analyzer_dir = _digit_reduction_dirs(state, base_analysis_dir)

    def _scan_training_logs() -> list[Path]:
        patterns = [
            f"{state}_digit_reduction_log*.json",
            f"*{state}*digit_reduction_log*.json",
            f"*{state}*digit_reduction_logs*.json",
        ]
        candidates: list[Path] = []
        if training_dir.exists():
            for pattern in patterns:
                candidates.extend(training_dir.glob(pattern))
        candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        unique: list[Path] = []
        seen = set()
        for cand in candidates:
            resolved = cand.resolve()
            if resolved in seen:
                continue
            unique.append(cand)
            seen.add(resolved)
        return unique

    def _scan_analyzer_artifacts() -> list[Path]:
        if not analyzer_dir.exists():
            return []
        return sorted(
            analyzer_dir.glob(f"{state}_analyzer_v2_*"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )

    training_logs = _scan_training_logs()
    analyzer_files = _scan_analyzer_artifacts()
    has_tables = any(state_tables_dir.glob("*.csv"))

    st.subheader("Preflight Checks")
    status_entries = [
        ("Tables CSVs", has_tables, state_tables_dir),
        ("Training JSON", bool(training_logs), training_dir),
        ("Analyzer outputs", bool(analyzer_files), analyzer_dir),
    ]
    for idx, (label, ok, path_obj) in enumerate(status_entries):
        cols = st.columns([4, 1])
        status_text = "[OK]" if ok else "[TODO]"
        with cols[0]:
            st.write(f"{status_text} {label}: {path_obj}")
        with cols[1]:
            if st.button("Open", key=f"open_{label.replace(' ', '_')}_{state}"):
                if not _open_path_in_explorer(path_obj):
                    st.warning(f"Unable to open {path_obj}")

    run_digit_reduction_requested = st.button("Run Digit Reduction", key=f"run_digit_reduction_{state}")
    reducer_result = None

    if not has_tables:
        st.warning("No tables detected. Run the data pipeline before digit reduction.")
    elif not training_logs:
        cols = st.columns([3, 1, 1])
        with cols[0]:
            st.info("Training JSON not found for this state. Run digit reduction to generate it.")
        with cols[1]:
            if st.button("Open training folder", key=f"open_training_dir_{state}"):
                if not _open_path_in_explorer(training_dir):
                    st.warning("Training folder is not available yet.")
        with cols[2]:
            if st.button("Run reducer now", key=f"run_digit_reduction_shortcut_{state}"):
                run_digit_reduction_requested = True
    else:
        if st.button("Open training folder", key=f"open_training_dir_existing_{state}"):
            if not _open_path_in_explorer(training_dir):
                st.warning("Training folder is not available yet.")

    if run_digit_reduction_requested and has_tables:
        with st.spinner(f"Running Digit Reduction for {state}..."):
            df, html_path, csv_path = run_digit_reduction(
                state,
                tables_path=state_tables_dir,
            )
        if df.empty:
            st.warning("Digit Reduction produced no output - verify tables exist.")
            return
        reducer_result = (df, html_path, csv_path)
        training_logs = _scan_training_logs()
        analyzer_files = _scan_analyzer_artifacts()

    if reducer_result:
        df, html_path, csv_path = reducer_result
        st.success(f"{len(df)} reductions extracted for {state}")
        st.dataframe(df, use_container_width=True)
        if csv_path:
            st.download_button(
                "Download CSV",
                Path(csv_path).read_bytes(),
                file_name=Path(csv_path).name,
            )
        if html_path and Path(html_path).exists():
            stacked = st.checkbox("Stacked view (show all methods)", value=False)
            primary_path = Path(html_path)
            target_html = primary_path
            if stacked:
                stacked_path = primary_path.with_name(
                    primary_path.name.replace("_digit_reduction_report.html", "_digit_reduction_report_stacked.html")
                )
                if stacked_path.exists():
                    target_html = stacked_path
            with open(target_html, "r", encoding="utf-8") as fh:
                height = 3200 if stacked else 900
                st.components.v1.html(fh.read(), height=height, scrolling=True)

    with st.expander("Analyzer V2 (DEV)", expanded=False):
        st.caption("Runs the unified analyzer and writes CSV/JSON beside the reducer outputs.")
        latest_training = training_logs[0] if training_logs else None
        if latest_training:
            st.caption(f"Using training log: {latest_training.name}")
        else:
            st.warning("Training JSON not found. Run Digit Reduction first.")
        if st.button("Open analyzer folder", key=f"open_analyzer_dir_{state}"):
            if not _open_path_in_explorer(analyzer_dir):
                st.warning("Analyzer folder is not available yet.")
        disabled = latest_training is None
        if st.button("Run Analyzer V2 for this state", type="primary", key=f"run_analyzer_v2_{state}", disabled=disabled):
            try:
                from alpha_analytical.digit_reduction.analyzer_v2 import run as run_v2
                info = run_v2(state, analysis_root=base_analysis_dir)
            except Exception as exc:
                st.error(f"Analyzer V2 failed: {exc}")
            else:
                out_dir = Path(info.get("out_dir", analyzer_dir))
                st.success(f"Wrote {info.get('rows', 0)} rows - {out_dir}")
                analyzer_files = _scan_analyzer_artifacts()
                artifacts = info.get("artifacts") or [
                    f"{state}_analyzer_v2_per_item.csv",
                    f"{state}_analyzer_v2_own_vs_combined_delta.csv",
                    f"{state}_analyzer_v2_top_candidates.csv",
                    f"{state}_analyzer_v2_meta.json",
                ]
                for name in artifacts:
                    artifact_path = out_dir / name
                    if artifact_path.exists():
                        st.markdown(f"- [{artifact_path.name}]({artifact_path.as_posix()})")
                if not artifacts:
                    st.caption("Analyzer completed without artifacts list.")
        if analyzer_files:
            st.caption("Latest Analyzer V2 outputs for this state:")
            for artifact_path in analyzer_files:
                st.markdown(f"- [{artifact_path.name}]({artifact_path.as_posix()})")

    if callable(render_dr_winner_overlay_dev):
        render_dr_winner_overlay_dev(state)
    elif DEV_OVERLAY_IMPORT_ERROR:
        st.caption(f"Digit Reduction DEV overlay unavailable: {DEV_OVERLAY_IMPORT_ERROR}")

try:
    from alpha_analytical.digit_reduction.analyzer_v2.ui_dev import render_dr_winner_overlay_dev as _render_dr_overlay
except Exception as _import_exc:
    DEV_OVERLAY_IMPORT_ERROR = _import_exc
    render_dr_winner_overlay_dev = None
else:
    DEV_OVERLAY_IMPORT_ERROR = None
    render_dr_winner_overlay_dev = _render_dr_overlay


def _rescue_boot() -> None:
    st.title("Alpha Analytical Tool")
    st.write("Rescue boot path active. main() did not render.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        _rescue_boot()
        st.error(f"main() raised: {exc}")
