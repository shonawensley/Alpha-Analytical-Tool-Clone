# AAT9 — Auxiliary Tools Integration Checkpoint (Part 2) — 2025‑09‑01

This document records the concrete wiring and successful behaviors added for Auxiliary Tools in `src/app.py`, with a deep focus on Sums availability and UI integration. It is written so another AI/operator can continue without rediscovery.

## Overview

- Edited file: `src/app.py` only.
- Working modules consumed from staged path: `scripts/auxiliary/working/modules/…` (exposed as `modules.*` via `_AUX_WORKING_ROOT`).
- No changes to `src/core` or `src/utils` packages.
- Data read/write remains confined to `data/cleaned/` for CSVs produced by the staged runner if needed.

## Navigation & Entry Points

- Sidebar tool selection contains: `Auxiliary Tools` and `Control Center` among other pages.
- When `Auxiliary Tools` is selected → `show_aux_page(state)`.
- When `Control Center` is selected → doubles aggregation UI using cleaned CSVs.

## Isolated Working Modules Path

- Declared near top of app:
  - `_AUX_WORKING_ROOT = <PROJECT>/scripts/auxiliary/working`
  - If exists, it is `sys.path.insert(0, _AUX_WORKING_ROOT)`, enabling absolute imports like `from modules.analyze_pairs import …` to resolve to the staged copies only for Aux usage.

## Draws Acquisition (Non‑destructive)

Inside `cached_aux_analysis(state_name)`:
- `_load_draws_from_csv_candidates(state_name)` tries the following in order:
  1) `data/cleaned/<State>_draws.csv`
  2) `data/processed/draws/<State>_draws.csv`
- If both missing and extractor is importable: calls `extract_draw_list(state, None)` read‑only.
- If still missing and `data/original/Pick3StatsC4.xlsm` exists: calls staged `modules.run_process()` once to produce `data/cleaned/*_draws.csv`; re‑reads.

This sequence avoids mutating other tools’ data while guaranteeing the Aux page can proceed.

## Working Logic Imports (staged)

- In `show_aux_page` guarded by try/except:
  - `from modules.analyze_pairs import calculate_overdue_pairs, get_top_overdue_repeating_pairs, get_vtrac_statuses, get_doubles_history, COLOR_LATE, COLOR_VERY_LATE, COLOR_PENDING`
  - `from modules.vtrac_reference import VTRAC_DISPLAY, get_vtrac_index`
- Flag `_AUX_WORKING_AVAILABLE` gates the page functionality.

## Caching Strategy

- `@st.cache_data(ttl=30 * 60)` on `cached_aux_analysis(state_name)` caches the full result dict per state for 30 minutes.
- For Control Center, `st.session_state["combined_doubles_df"]` caches the aggregated doubles table. A button clears it.

## Result Model (cached_aux_analysis)

Returned dictionary keys:
- `draws`, `draws_100`, `draws_1000`
- `nonrep`, `rep`, `pair_status`
- `vstat` (per‑index status, row styles, draws‑since maps)
- `top5` list of `(pair, overdue)`
- `doubles` mapping produced by `get_doubles_history({state: draws})`
- `sums_stats` (added in the render phase; see Sums section)

## Sums Integration (Local helpers + optional package)

Local helpers in `src/app.py`:
- `_sum3(d: str) -> int` — sum of three digits (guards invalid input)
- `_root(n: int) -> int` — digit root
- `_root_sum3(d: str) -> int` — composition of the above
- `_sums_badge_for(combo: str, sums_stats: dict) -> str` — returns inline badge string like `[Sx Ry]` with red/blue styling based on `flags` in `sums_stats`.

Scoped import context to avoid collisions:
- `_project_modules_first()` temporarily prepends `PROJECT_ROOT/modules` so imports resolve to the project’s `modules` tree, not the staged `scripts/auxiliary/working`.

Optional external Sums package (used when available):
- Inside `_project_modules_first()` the app attempts:
  - `from module_d_auxiliary_tools.refactored.sums_analysis import calculate_sums_stats as _calc_sums`
  - `from module_d_auxiliary_tools.refactored.sums_ui import build_sums_dataframe as _build_sums_df`
- A sidebar caption displays the import source module for troubleshooting: `SUMS ⦿ <module>` or `SUMS import failed: <error>`.

Runtime behavior:
- `analysis_draws = st.session_state.get("analysis_draws", 100)` sets the analysis window.
- If `_calc_sums` is callable, compute `sums_stats = _calc_sums(draws, window=analysis_draws)`; otherwise fallback to an empty structure: `{ "window": 0, "by_sum": {}, "by_root_sum": {} }`.
- Sums badges are appended to Singles/Doubles strings in the V‑Trac table rendering via `_sums_badge_for`.
- If `_build_sums_df` is available and `sums_stats.by_sum` is present, render a scrollable "Sums Tracking" table using `build_sums_dataframe(sums_stats)`.

Practical outcomes:
- Even if the external Sums package is missing, the UI remains functional — badges may be empty and the table omitted, but the page renders.
- When the package is present, Sums badges show alongside each combo and the Sums table appears.

## V‑Trac Table Rendering (Working Parity)

- Iterates `VTRAC_DISPLAY` per index.
- Each row renders Index cell, row tint, rank badge; Singles and Doubles cells use working pair status colors and shape overlays.
- Inline Sums badges are added per combo using `_sums_badge_for`.

## Overdue Pairs & Top 5

- Uses `calculate_overdue_pairs` for repeating/non‑repeating thresholds.
- Renders side‑by‑side sections and a compact "Top 5 Most Overdue Repeating Pairs" block.

## V‑Trac Index Hits (Working)

- Rebuilds recent/overdue rank sets from `vstat` and scans the 1,000‑draw window to compute per‑index Draws‑Since; renders a sortable table.

## Control Center (Cross‑state Doubles Aggregation)

- Reads all `data/cleaned/*_draws.csv`.
- Uses the same `get_doubles_history` as the Aux page to build the combined table.
- Cached in `st.session_state["combined_doubles_df"]`; a refresh button evicts cache and recomputes.

## Safety, Boundaries, and No‑Regression Guarantees

- Only `src/app.py` edited; other modules untouched.
- Staged working imports isolated behind `_AUX_WORKING_ROOT` to avoid clashes.
- Data generation writes only to `data/cleaned/` when needed; no mutation of legacy folders.
- Sums features degrade gracefully when modules are unavailable.

## Operator How‑To (Aux Page)

1) Open app (e.g., `run_app.bat`).
2) Navigate to “Auxiliary Tools”, choose a state.
3) Click “Run Auxiliary Tools Analysis”.
4) If needed, the staged runner will generate `data/cleaned/*_draws.csv` once, then the page renders working visuals:
   - V‑Trac table with badges and shapes
   - Overdue Pairs sections and Top‑5
   - V‑Trac Index Hits
   - Sums badges always present (content depends on package availability)
   - Sums Tracking table appears when Sums package is importable

## Known Limitations & Outstanding Work

- Sums package availability:
  - If `module_d_auxiliary_tools.refactored` is not on `PROJECT_ROOT/modules`, only local badges (empty) render and the Sums table is hidden. Action: ensure that folder exists with `sums_analysis.py` and `sums_ui.py` and imports succeed within `_project_modules_first()`.
- Styling parity:
  - Badge colors are controlled by `flags` in `sums_stats`. If the external analyzer returns different flag keys, the inline styling may need alignment.
- Error surfacing:
  - Import failures are shown via sidebar caption only; consider adding a subtle warning on the page if Sums is unavailable.
- CSV expectations:
  - Aux tools assume `data/cleaned/<State>_draws.csv` schema used by the working tool. If schema deviates, `_calc_sums` may require adapters.
- Performance knobs:
  - Cache TTL is 30 min (`@st.cache_data(ttl=1800)`). Adjust per usage. The V‑Trac Index Hits scan uses 1,000 draws; lowering can reduce compute if needed.

## Quick Pointers (for another AI)

- Entry: search for `show_aux_page` in `src/app.py`.
- Cache: `cached_aux_analysis` (nested inside show_aux_page).
- Sums glue:
  - Helpers: `_sum3`, `_root`, `_root_sum3`, `_sums_badge_for`.
  - Import context: `_project_modules_first()`; import targets are `module_d_auxiliary_tools.refactored.sums_analysis` and `.sums_ui`.
  - UI table: gated by `callable(_build_sums_df)` and `sums_stats.get("by_sum")`.
- Control Center: search `get_doubles_history` and `combined_doubles_df`.

## Change Log (this Part 2)

- Documented precise import contexts, cache lifetimes, and result model keys.
- Captured Sums fallback logic and UI gating conditions.
- Mapped data flow, safety boundaries, and operator steps for reproducible runs.
