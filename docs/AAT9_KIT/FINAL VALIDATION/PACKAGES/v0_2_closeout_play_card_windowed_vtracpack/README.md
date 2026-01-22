# v0.2 Closeout Pack — Play Cards + Windowed Grading + VTRAC Pack Strategy

Goal: give a zero-context reviewer a **tight, pointer-only** entry point for the v0.2→v0.3 “selection-layer alignment” work:
- training-aligned semantics (“lane present” vs “closure” vs “straight”),
- windowed grading (hit within N draw-slots, N=5),
- and the VTRAC boxed-member pack strategy that lifts at B24/B36.

This pack is pointer-only (no duplication). Evidence lives in:
- RUNS (analysis outputs + rollups): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/...`
- Predictive sharepacks (winners-free): `sharepacks/_predictive/<D>/...` (gitignored; local-generated)

## Start here (recommended order)

1) Orientation / navigation:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`

2) The core evidence (training-aligned grading, N=5):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v1__N5__2025-12-30_to_2026-01-04.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__vtracpack_v1__N5__2026-01-05_to_2026-01-09.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__v0_2_default_v1__N5__2025-12-30_to_2026-01-04.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_windowed_rollup__tool_only__v0_2_default_v1__N5__2026-01-05_to_2026-01-09.md`

3) Tooling (what implements the semantics):
- `scripts/tools/create_play_card.py`
- `scripts/tools/grade_play_card.py`
- `scripts/tools/grade_play_card_windowed.py`
- `scripts/tools/create_predictive_portfolio_report.py`
- `scripts/tools/run_v0_3_cycle.py` (daily cadence wrapper; pre + post)

4) VTRAC reference surface (concept anchor):
- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`
- `modules/vtrac_reference.py`

## Manifest

- Exact file list: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/v0_2_closeout_play_card_windowed_vtracpack/MANIFEST.md`
- ChatGPT Pro prompt (copy/paste): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/v0_2_closeout_play_card_windowed_vtracpack/CHATGPT_PRO_DEEP_RESEARCH_PROMPT.md`

