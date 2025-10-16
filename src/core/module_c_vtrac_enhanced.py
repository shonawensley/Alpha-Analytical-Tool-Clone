"""
Feature-gated Streamlit wrapper for the enhanced V-TRAC analyzer.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Sequence

import pandas as pd
import streamlit as st

from modules import vtrac_enhanced as ve
from utils import path_handler as ph

SESSION_KEY_RESULTS = "vtrac_enhanced_results"


def render(state: str) -> None:
    st.title("V-TRAC Analyzer · Enhanced")

    tables_root = Path(ph.get_tables_output_dir())
    state_dir = tables_root / state
    bundle_dir = Path(ph.get_analysis_output_dir()) / "vtrac" / state

    _render_preflight(state, tables_root, state_dir, bundle_dir)

    if not state_dir.exists():
        st.warning("No combined tables found for this state. Run the tables pipeline first.")
        return

    engine_input = ve.build_engine_input_from_tables(state)
    mask_default = "".join(sorted(ve.suggested_mask_digits(engine_input.recent_draws)))
    mask_digits = st.text_input(
        "Digits to mask (optional)",
        value=mask_default,
        help="Digits removed before scanning strings. Defaults to the latest draw.",
    )
    mask_set = {ch for ch in mask_digits if ch.isdigit()}

    run_label = "Run enhanced analysis"
    if st.button(run_label, type="primary"):
        with st.spinner("Analyzing V-TRAC indices..."):
            output = ve.run_analysis(engine_input, digits_to_mask=mask_set)
            bundle_path = ve.write_prediction_bundle(state, output)
        _store_session(state, output, bundle_path)
        st.success("Enhanced analysis complete.")
        st.caption(f"Bundle written to {bundle_path}")

    stored = st.session_state.get(SESSION_KEY_RESULTS, {}).get(state)
    if not stored:
        st.info("Run the enhanced analyzer to view ranked indices and straights.")
        return

    output: ve.EngineOutput = stored["output"]
    bundle_path: Path = stored["bundle"]

    st.subheader("Top V-TRAC indices")
    rows: List[dict] = []
    for score in output.indices_ranked[:12]:
        rows.append(
            {
                "Index": score.index,
                "Score": round(score.score, 2),
                "Sections": ", ".join(score.evidence.raw.get("sections", [])),
                "Hits": score.evidence.raw.get("total_hits", 0),
                "First Col": score.evidence.raw.get("first_col"),
                "Max Streak": score.evidence.raw.get("max_streak"),
            }
        )
    st.dataframe(pd.DataFrame(rows), use_container_width=True)

    st.subheader("Top straight candidates")
    straight_rows: List[dict] = []
    for straight in output.straights_ranked[:12]:
        straight_rows.append(
            {
                "Straight": straight.straight,
                "Index": straight.index,
                "Score": round(straight.score, 2),
                "Reasons": ", ".join(straight.reasons),
            }
        )
    st.dataframe(pd.DataFrame(straight_rows), use_container_width=True)

    with st.expander("Bundle details", expanded=False):
        st.caption(str(bundle_path))
        st.json(output.telemetry)


def _render_preflight(state: str, tables_root: Path, state_dir: Path, bundle_dir: Path) -> None:
    st.subheader("Preflight checks")
    checks = [
        ("Tables root", tables_root.exists(), str(tables_root)),
        (f"State directory ({state})", state_dir.exists(), str(state_dir)),
        ("Existing bundles", bundle_dir.exists(), str(bundle_dir)),
    ]
    for label, ok, detail in checks:
        icon = "✅" if ok else "⚠️"
        st.write(f"{icon} {label}: {detail}")

    dev_health = st.sidebar.checkbox("Show Dev Health (enhanced V-TRAC)", value=False, key=f"dev_health_vtrac_enh_{state}")
    if dev_health:
        with st.expander("Dev health (tables)", expanded=False):
            available = sorted(state_dir.glob("*_combined.csv")) if state_dir.exists() else []
            if not available:
                st.write("No combined tables located.")
            else:
                for path in available:
                    try:
                        size = path.stat().st_size
                    except OSError:
                        size = 0
                    st.write(f"{path.name} · {size:,} bytes")


def _store_session(state: str, output: ve.EngineOutput, bundle_path: Path) -> None:
    st.session_state.setdefault(SESSION_KEY_RESULTS, {})
    st.session_state[SESSION_KEY_RESULTS][state] = {"output": output, "bundle": bundle_path}
