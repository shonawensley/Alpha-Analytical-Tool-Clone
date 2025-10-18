"""
Feature-gated Streamlit wrapper for the enhanced V-TRAC analyzer.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Sequence

import pandas as pd
import streamlit as st

from modules import vtrac_enhanced as ve
from utils import path_handler as ph

SESSION_KEY_RESULTS = "vtrac_enhanced_results"
SESSION_KEY_WEIGHTS = "vtrac_enhanced_weights"


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
    weights = _render_tuning_panel()
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
            output = ve.run_analysis(engine_input, weights=weights, digits_to_mask=mask_set)
            bundle_path = ve.write_prediction_bundle(state, output, engine_input=engine_input)
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

    _render_why_panel(output)


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


# --- Tuning and why panels ---

_WEIGHT_SLIDERS = [
    ("bonus_cross_section", "Cross-section consensus", 0.0, 1.5, 0.05),
    ("bonus_set_echo", "Set echo", 0.0, 1.0, 0.05),
    ("bonus_column_span", "Column span depth", 0.0, 1.0, 0.05),
    ("bonus_first_hit", "First-hit bonus", 0.0, 1.0, 0.05),
    ("bonus_persistence", "Persistence", 0.0, 1.0, 0.05),
    ("bonus_total_hits", "Hit volume", 0.0, 0.5, 0.01),
    ("bonus_hot_support", "Hot support", 0.0, 0.5, 0.01),
    ("bonus_super_hot_support", "Super-hot support", 0.0, 0.5, 0.01),
    ("bonus_mask_drop", "Mask drop", 0.0, 1.0, 0.05),
    ("bonus_reduction", "Reduction hits", 0.0, 1.0, 0.05),
    ("bonus_doubles", "Doubles bias", 0.0, 1.0, 0.05),
    ("bonus_mirror", "Mirror support", 0.0, 1.0, 0.05),
]


def _load_weights_from_session() -> ve.EvidenceWeights:
    stored = st.session_state.get(SESSION_KEY_WEIGHTS)
    if stored:
        try:
            return ve.EvidenceWeights.from_dict(stored if isinstance(stored, dict) else json.loads(stored))
        except Exception:
            pass
    return ve.DEFAULT_WEIGHTS.clone()


def _save_weights(weights: ve.EvidenceWeights) -> None:
    st.session_state[SESSION_KEY_WEIGHTS] = weights.to_dict()


def _render_tuning_panel() -> ve.EvidenceWeights:
    weights = _load_weights_from_session()
    with st.expander("Tuning (weights)", expanded=False):
        st.caption("Adjust evidence weights and rerun analysis to compare.")
        cols = st.columns(3)
        for idx, (field, label, min_val, max_val, step) in enumerate(_WEIGHT_SLIDERS):
            col = cols[idx % 3]
            current = getattr(weights, field)
            new_val = col.slider(label, min_value=float(min_val), max_value=float(max_val), value=float(current), step=float(step))
            setattr(weights, field, new_val)
        toggles = st.columns(3)
        with toggles[0]:
            weights.enable_mirror_assist = st.checkbox("Enable mirror assist", value=weights.enable_mirror_assist)
            weights.enable_reduction_assist = st.checkbox("Enable reduction assist", value=weights.enable_reduction_assist)
        with toggles[1]:
            weights.emit_evidence = st.checkbox("Record feature contributions", value=weights.emit_evidence)
        with toggles[2]:
            if st.button("Reset to defaults"):
                weights = ve.DEFAULT_WEIGHTS.clone()
                _save_weights(weights)
                st.experimental_rerun()
        st.caption("Current weights")
        st.json(weights.to_dict())
    _save_weights(weights)
    return weights


def _render_why_panel(output: ve.EngineOutput) -> None:
    if not output.indices_ranked:
        return
    st.subheader("Why these indices?")
    options = [f"Index {item.index} - score {item.score:.2f}" for item in output.indices_ranked[:12]]
    choice = st.selectbox("Inspect index", options, index=0)
    selected = output.indices_ranked[options.index(choice)]
    with st.expander(f"Evidence for index {selected.index}", expanded=True):
        st.write(f"Score: {selected.score:.2f}")
        st.json(selected.evidence.raw)
        if selected.evidence.features:
            feature_rows = [
                {
                    "feature": feat.name,
                    "value": round(float(feat.value), 4),
                    "details": feat.details,
                }
                for feat in selected.evidence.features
            ]
            st.dataframe(pd.DataFrame(feature_rows))
        else:
            st.caption("Feature contributions not recorded (emit_evidence disabled).")

