# AAT9 — Winners Logger: V‑Trac Winner Report

## Purpose
Generate a per‑state, per‑winner HTML export showing the winner’s V‑Trac index across Midday/Evening/Combined panels:
- Green (solid / dashed): winner permutations detected as strict hits or single-digit gaps.
- Blue (solid / dashed): V-TRAC straights (AABB/BBAA) including value-block runs (e.g., 33 66 44).
- Purple (solid / dashed): index-family combos aligned to the winner's V-TRAC index.

## Where in the App
- Control Center → expand “Winners Logger (V‑Trac winner report)”
- Inputs: State (single), Winning number (3 digits)
- Click “Generate V‑Trac Winner Report”

## Outputs
- Path: `data/outputs/winners/<YYYY‑MM‑DD>/vtrac_reports/<STATE>/<STATE>_vtrac<index>_winner_<timestamp>.html`
- HTML contains three inline panels (Midday/Evening/Combined) with colored tags for combos related to the index and straight permutations.
- Streamlit tile exposes an 'Open report (HTML)' download button to avoid /pages routing errors.

## Implementation Notes
- Renderer: `src/core/winners_vtrac_report.py::build_vtrac_winner_report(state, winner, ...)`
- Matching: two-pass across R2/R4/R6/R8 cells — strict permutations, gap-1 winner hits, and VT-straight detection (AABB + value-block) feeding green / blue / purple overlays.
- Mapping: reuses `modules.vtrac_reference::VTRAC_DISPLAY, get_vtrac_index`
- Does not require state string‑tables; table‑agnostic for robustness.
- Future: overlay table‑driven details once state tables are finalized/mapped.

## Pitfalls
- Winner must be exactly 3 digits.
- State label should match your per‑state conventions.
- Windows path issues: paths resolved via `utils.path_handler` where applicable; HTML uses UTF‑8.
# AAT9 — Winners: V‑Trac Reports

## Overview
Two Winners experiences exist in the integrated app:
- Winners Logger (V‑Trac winner report): compact index panel (table‑agnostic), safe when string‑tables are missing.
- Winners Logger (Analyzer‑style full report): 3‑pane HTML (Midday/Evening/Combined) identical to the analyzer layout; requires combined tables.

## Analyzer‑Style Full Report (new)
- Entry: Control Center → “Winners Logger (Analyzer‑style full report)”
- Inputs:
  - State (e.g., Connecticut4)
  - Midday winner (3 digits) — optional
  - Evening winner (3 digits) — optional
  - Date (implicit in filename; defaults to today)
- Data source: reads `data/outputs/tables/<STATE>/<STATE>_{Midday,Evening,Combined}_combined.csv` (string‑safe loader)
- Rendering:
  - Purple: full index coverage (`modules.vtrac_reference.get_index_set(index)`).
  - Green: winner straights overlay (`modules.vtrac_reference.get_index_straights(winner)`); overrides purple where overlapping.
- Output path:
  - `data/outputs/analysis/winners/<STATE>/<STATE>_<Draw>_<YYYY-MM-DD>_winner_<NNN>_analyzer.html`
  - Path helper: `utils.path_handler.get_analysis_dir("winners", <STATE>)`
- Fallback: if tables are missing, use the compact Winners tile.

### Minimal Flow
1) Ensure combined tables exist for the state (pipeline ran once).
2) Open the full Winners tile and enter winners.
3) Open the generated HTML(s); expect three panes with purple+green highlights.

## Compact Index Panel (existing)
- Entry: “Winners Logger (V‑Trac winner report)”
- Behavior: renders green / blue / purple index panel without reading string‑tables; safe for states without tables.
- Output path: `data/outputs/winners/<YYYY-MM-DD>/vtrac_reports/<STATE>/*.html`

## Developer Notes
- Canonical V‑Trac API: `modules/vtrac_reference.py` provides `get_vtrac_index`, `get_index_set`, `get_index_straights` for non‑Aux pages.
- Aux isolation: Aux still uses a staged `modules.vtrac_reference` under `scripts/auxiliary/working/modules/`; only the Aux page binds to it.
- String‑safe IO: table reads use `dtype=str, keep_default_na=False, na_filter=False` to preserve tokens.
- CLI smoke: `python scripts/smoke/build_winners_full.py <STATE4> <WINNER>` prints the saved full report path.
- Unit guardrails: run pytest tests/test_vtrac_matchers.py (VT-straight spans) and pytest tests/test_winners_renderer.py (legend/classes).
- Smoke: run python scripts/smoke_winners_logger.py to confirm legend tokens (winner, VT-straight, family) render in the analyzer-style report.
