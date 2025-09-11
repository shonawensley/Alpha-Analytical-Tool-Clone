# AAT9 — Digit Reduction: Stacked Report & Training Exports

## Overview
Adds stacked HTML report (optional embed) and training‑friendly CSV/JSON exports with structural fields, ranks, and export‑only compaction. Analysis algorithms and tabbed HTML remain unchanged.

## Where to Look
- `data/outputs/analysis/digit_reduction/<STATE>/<STATE>digit_reduction_report.html` (tabbed)
- `data/outputs/analysis/digit_reduction/<STATE>/<STATE>digit_reduction_report_stacked.html` (stacked)
- `data/outputs/analysis/digit_reduction/<STATE>/<STATE>digit_reduction_scores.csv` (summary)
- `data/outputs/analysis/digit_reduction/<STATE>/training/<STATE>digit_reduction_steps.csv` (long/tidy steps)
- `data/outputs/analysis/digit_reduction/<STATE>/training/<STATE>digit_reduction_logs.json` (compacted logs + guidance)

## App Wiring (unchanged)
- Page: `src/app.py` → `show_digit_reduction_page(state)`
  - Resolves tables dir via `utils.path_handler.get_tables_output_dir()`
  - Calls `src/core/module_b_digit_reduction.py::run_digit_reduction`
  - Renders summary DataFrame, provides “Download CSV”, and embeds HTML; checkbox toggles stacked embed
- Orchestrator: `src/core/module_b_digit_reduction.py`
  - Builds `big_data` from `*_combined.csv`
  - Applies methods A..T in own/combined
  - Writes tabbed + stacked HTML, summary CSV, and training CSV/JSON
- Engine: `src/core/long_string_reducer_part1.py`

## Export Compaction (exports only)
- Terminal start: first step where length <= 3 or unique_digits <= 2
- Keep steps up to terminal inclusive
- After terminal: allow at most one identical duplicate per distinct value; keep later changes (each with at most one identical duplicate)
- If no terminal: keep up to last_change_step

## Structural Fields (for grouping/pivots)
- area (LS1/LS2), section (Midday/Evening/Combined), set (Set1/2/3), draw (Draw1..7), col (numeric + label)
- Ranks for panel order: `area_rank`, `section_rank (1..3)`, `set_rank (1..3, desc in UI)`, `draw_rank (1..7)`, `col_rank (7/6/5 or 3/1)`
- `grid_position`, `sequence_meta`, `final`, and compacted `steps[{step, value, length, unique_digits, is_3value}]`

## Suggested Sorts
- Recreate UI grid: `area_rank`, `section_rank`, `set_rank desc`, `draw_rank`, `col_rank`, `method`, `mode`
- Own‑table analysis: fix `section`, compare LS1 (`col_rank` 7/6/5) or LS2 (`col_rank` 3/1)
- Cross‑chart: group by `[area, set_rank, draw_rank, col_rank, method, mode]` and pivot `section_rank`

## Pitfalls
- Windows can lock the summary CSV if open (Excel/Preview Pane). Close/delete then re‑run.
- State label must match tables directory exactly.
- Checkbox toggles re‑render; if stacked disappears, press “Run Digit Reduction” or open stacked HTML directly.

## Why This Helps
- Exports embed guidance and structural fields so downstream analysis/aggregation can be reproducible and AI‑friendly without UI coupling.

