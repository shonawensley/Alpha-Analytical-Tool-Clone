# AAT9 — Winners Logger: V‑Trac Winner Report

## Purpose
Generate a per‑state, per‑winner HTML export showing the winner’s V‑Trac index across Midday/Evening/Combined panels:
- Purple: stable‑pattern combos for the index
- Green: straight permutations of the winning number

## Where in the App
- Control Center → expand “Winners Logger (V‑Trac winner report)”
- Inputs: State (single), Winning number (3 digits)
- Click “Generate V‑Trac Winner Report”

## Outputs
- Path: `data/outputs/winners/<YYYY‑MM‑DD>/vtrac_reports/<STATE>/<STATE>_vtrac<index>_winner_<timestamp>.html`
- HTML contains three inline panels (Midday/Evening/Combined) with colored tags for combos related to the index and straight permutations.

## Implementation Notes
- Renderer: `src/core/winners_vtrac_report.py::build_vtrac_winner_report(state, winner, ...)`
- Mapping: reuses `modules.vtrac_reference::VTRAC_DISPLAY, get_vtrac_index`
- Does not require state string‑tables; table‑agnostic for robustness.
- Future: overlay table‑driven details once state tables are finalized/mapped.

## Pitfalls
- Winner must be exactly 3 digits.
- State label should match your per‑state conventions.
- Windows path issues: paths resolved via `utils.path_handler` where applicable; HTML uses UTF‑8.

