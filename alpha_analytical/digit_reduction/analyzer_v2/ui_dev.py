"""Streamlit helpers for Analyzer V2 dev controls."""
from __future__ import annotations

from pathlib import Path
from typing import Dict

import streamlit as st

from utils.path_handler import get_analysis_output_dir
from .winners_overlay import run_winner_overlay_batch


def _collect_winners(combined: str, midday: str, evening: str) -> Dict[str, str]:
    winners: Dict[str, str] = {}
    ordered = [
        ("Combined", combined),
        ("Midday", midday),
        ("Evening", evening),
    ]
    for label, value in ordered:
        trimmed = value.strip()
        if trimmed:
            winners[label] = trimmed
    if "Combined" not in winners:
        for fallback in ("Midday", "Evening"):
            if fallback in winners:
                winners["Combined"] = winners[fallback]
                break
    return winners


def _format_step(value) -> str:
    try:
        ivalue = int(value)
    except (TypeError, ValueError):
        return "n/a"
    return "n/a" if ivalue < 0 else str(ivalue)


def render_dr_winner_overlay_dev(state: str) -> None:
    """Render the dev-only winner overlay batch expander."""
    with st.expander("Analyzer V2 Winners overlay (DEV) - batch", expanded=False):
        st.caption("Build overlays, flags, and winner stamps for any variants you populate below.")

        base_analysis_dir = Path(get_analysis_output_dir())
        combined = st.text_input("Combined winner", value="", max_chars=3)
        midday = st.text_input("Midday winner", value="", max_chars=3)
        evening = st.text_input("Evening winner", value="", max_chars=3)
        mirror = st.checkbox("Mirror stamp into Winners logger", value=True)

        if st.button(f"Build winners overlays for {state}"):
            winners = _collect_winners(combined, midday, evening)
            auto_combined = (not combined.strip()) and "Combined" in winners and any(label in winners for label in ("Midday", "Evening"))
            if not winners:
                st.warning("Enter at least one winner before running the overlay batch.")
                return

            try:
                payload = run_winner_overlay_batch(
                    state,
                    winners,
                    analysis_root=base_analysis_dir,
                    when=None,
                    mirror_to_winners=mirror,
                )
            except Exception as exc:
                st.error(f"Winners overlay batch failed: {exc}")
                return

            st.success("Digit Reduction winners overlays completed.")
            if auto_combined:
                st.caption("Combined overlay reused the Midday/Evening winner input.")
            for variant, details in (payload.get("results") or {}).items():
                winner = details.get("winner", "")
                hits = int(details.get("hits", 0) or 0)
                st.markdown(f"**{variant}** - winner `{winner}` (hits={hits})")

                if details.get("overlay_html"):
                    st.markdown(f"- [Annotated overlay]({details['overlay_html']})")

                st.markdown(
                    "- [Winner map JSON]({}) - [Hits CSV]({}) - [Flags CSV]({})".format(
                        details.get("map_json", ""),
                        details.get("hits_csv", ""),
                        details.get("flags_csv", ""),
                    )
                )

                stamp_url = details.get("stamp_json_winners")
                if stamp_url:
                    st.markdown(f"- Mirrored stamp: `{stamp_url}`")

                summary = details.get("summary") or {}
                counts = summary.get("counts") or {}
                earliest_exact = _format_step(summary.get("earliest_exact_step"))
                earliest_vtrac = _format_step(summary.get("earliest_vtrac_step"))
                total_hits = int(counts.get("items_total", hits) or 0)
                final_exact = int(counts.get("final_exact", 0) or 0)
                final_vtrac = int(counts.get("final_vtrac", 0) or 0)
                st.caption(
                    f"Earliest exact step: {earliest_exact} | Earliest V-TRAC step: {earliest_vtrac} | Final exact hits: {final_exact} | Final V-TRAC hits: {final_vtrac} | Items logged: {total_hits}"
                )

