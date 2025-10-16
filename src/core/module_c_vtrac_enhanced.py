"""
Enhanced V-TRAC analyzer page module.

This mirrors the legacy V-TRAC page but delegates scoring to the
modules.vtrac_enhanced package.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Sequence, Set

import streamlit as st

from modules import vtrac_enhanced as ve


def render(state: str) -> None:
    st.title("V-TRAC Analyzer (Enhanced)")

    try:
        engine_input = ve.build_engine_input_from_tables(state)
    except FileNotFoundError as exc:
        st.error(str(exc))
        return

    mask_digits = ve.suggested_mask_digits(engine_input.recent_draws)
    mask_str = st.text_input(
        "Digits to mask (optional)",
        value="".join(sorted(mask_digits)),
        help="Digits removed while scanning strings to surface masked patterns.",
    )
    mask_set = {ch for ch in mask_str if ch.isdigit()}

    if st.button("Run enhanced analysis", type="primary"):
        with st.spinner("Analyzing V-TRAC indices..."):
            output = ve.run_analysis(engine_input, digits_to_mask=mask_set)
            bundle_path = ve.write_prediction_bundle(state, output)
        st.success("Analysis complete.")
        st.caption(f"Bundle written to {bundle_path}")
        _render_results(output)
    else:
        st.info("Adjust mask digits if needed and click run to generate results.")


def _render_results(output: ve.EngineOutput) -> None:
    top_indices = output.indices_ranked[:12]
    st.subheader("Top V-TRAC indices")
    if not top_indices:
        st.warning("No indices scored. Verify the combined tables contain patterns.")
        return

    rows = [
        {
            "Index": item.index,
            "Score": round(item.score, 2),
            "Sections": ", ".join(item.evidence.raw.get("sections", [])),
            "First Col": item.evidence.raw.get("first_col"),
            "Max Streak": item.evidence.raw.get("max_streak"),
        }
        for item in top_indices
    ]
    st.dataframe(rows, use_container_width=True)

    top_straights = output.straights_ranked[:12]
    st.subheader("Top straight candidates")
    if top_straights:
        s_rows = [
            {
                "Straight": straight.straight,
                "Index": straight.index,
                "Score": round(straight.score, 2),
                "Reasons": ", ".join(straight.reasons),
            }
            for straight in top_straights
        ]
        st.dataframe(s_rows, use_container_width=True)
    else:
        st.caption("No straight candidates triggered the thresholds.")
