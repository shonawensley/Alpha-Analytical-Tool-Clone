AAT9 — Auxiliary Tools Integration Checkpoint (2025-09-01)

Overview

This document records the successfully completed work to integrate the “Auxiliary Tools” from the standalone Lottery Analysis Tool into the consolidated Streamlit app (`src/app.py`). It focuses on working, shipped behavior: features, wiring, data flow, and boundaries to avoid regressions elsewhere in the app.

Scope of Changes

- Primary file edited: `src/app.py` only.
- No functional modifications to shared modules under `src/core` or `src/utils`.
- A staged, isolated import path is used for the working Aux logic under `scripts/auxiliary/working/` so other tools remain untouched.
- Control Center doubles aggregation added (cross‑state), consuming cleaned CSVs.

Key Capabilities Now Available

1) Auxiliary Tools page (state‑specific)
- Sources draws from `data/cleaned/*_draws.csv`; non‑destructive fallback to extractor (read‑only), and final fallback to run the staged “working” process once to generate cleaned CSVs.
- Computes and renders the following (mirrors the working app’s behavior and visuals):
  - V‑Trac Table (working logic): colorized digits, shape around combinations, index row tints and rank badges, with CSV download.
  - Overdue Pairs Analysis (working thresholds/sections for repeating and non‑repeating pairs) and the “Top 5 Most Overdue Repeating Pairs”.
  - Four‑panel row: Latest Draws, Pairs Analysis Results, Combinations Analysis (Draws Since) with shapes, and a second compact Top 5 block.
  - V‑Trac Index Hits table derived from the tracked ranks and 1,000‑draw scan.
  - Sums badges next to each combination cell; Sums Tracking table is wired to render when the Sums modules are available.

2) Control Center (cross‑state)
- “States Ranked by Draws Since Last Double” aggregated table computed from every `data/cleaned/*_draws.csv` using the same doubles logic as the working tool.
- Refresh button repopulates from disk and caches the result in `st.session_state`.

File/Directory Map and Purpose

- `src/app.py`: All Aux Tools and Control Center UI and orchestration lives here. The rest of the application pages (V‑TRAC Analyzer, Stable Pattern, Digit Reduction) are unchanged.
- `scripts/auxiliary/working/` (on `sys.path` only for Aux use): carries staged modules from the working tool so we can import `modules.analyze_pairs`, `modules.vtrac_reference`, and `modules.run_process` without colliding with the main project’s `modules` tree.
- Data directories used (read/write):
  - `data/cleaned/` — canonical location for `*_draws.csv` used by Aux and Control Center.
  - `data/original/Pick3StatsC4.xlsm` — optional local input if we must produce cleaned CSVs once via `modules.run_process`.

Import and Path Management

- Project root is inserted at startup for general imports:
  - `SRC_DIR = Path(__file__).resolve().parent`, `PROJECT_ROOT = SRC_DIR.parent` then `sys.path.insert(0, str(PROJECT_ROOT))`.
- Staged working Aux modules are isolated and prepended only for the Aux page:
  - `_AUX_WORKING_ROOT = .../scripts/auxiliary/working` is added to `sys.path` so absolute imports like `modules.analyze_pairs` resolve to the staged copy, not the main project.
- For Sums (to avoid name collisions), a scoped context manager prefers `PROJECT_ROOT/modules`:
  - `_project_modules_first()` temporarily prepends `PROJECT_ROOT/modules` so imports like `module_d_auxiliary_tools.refactored.sums_analysis` resolve reliably.

Auxiliary Tools — Runtime Data Flow

Button: “Run Auxiliary Tools Analysis” → function `cached_aux_analysis(state)` → renderers.

1) Draws acquisition (non‑destructive):
- `_load_draws_from_csv_candidates(state)`: tries `data/cleaned/<State>_draws.csv` then `data/processed/draws/<State>_draws.csv`.
- If not found and the legacy extractor is available: `extract_draw_list(state, None)` is used read‑only.
- If still not found and `data/original/Pick3StatsC4.xlsm` exists: call staged `modules.run_process()` once, which writes cleaned CSVs into `data/cleaned/`; then retry the CSV read. No changes are made to other tools’ data.

2) Working analysis logic (from staged modules):
- Imports within Aux context:
  - `from modules.analyze_pairs import calculate_overdue_pairs, get_top_overdue_repeating_pairs, get_vtrac_statuses, get_doubles_history, COLOR_*`
  - `from modules.vtrac_reference import VTRAC_DISPLAY, get_vtrac_index`
- Computations stored in a single result dict (cached for 30 minutes via `@st.cache_data`):
  - `draws`, `draws_100`, `draws_1000`
  - `nonrep`, `rep`, `pair_status`
  - `vstat` (per‑index status, row styles, draws‑since maps)
  - `top5` (list of `(pair, overdue)`)
  - `doubles` (state → draws since last double)

3) Sums helpers (local, side‑effect free):
- `_sum3`, `_root`, `_root_sum3`: used to compute Sum and Root‑Sum of a 3‑digit draw. These enable inline Sums badges even if external Sums modules are unavailable.
- `_sums_badge_for(combo, sums_stats)`: reads flags from `sums_stats` and renders `[Sx Ry]` with red/blue highlights; gracefully returns an empty string if stats aren’t present.
- If the Sums package is available under `modules/`, `calculate_sums_stats` and `build_sums_dataframe` are imported inside `_project_modules_first()` and used to compute and render the Sums Tracking table.

Auxiliary Tools — UI/Renderers

Common styling (exact classes used by the working tool):
- CSS classes for digits and status colors: `.red`, `.blue`, `.purple`, `.digit`.
- Shape classes around combinations: `.shape-red-circle`, `.shape-blue-square`.
- V‑Trac row tinting: `.row-green` and `.row-red`; `.rank-badge` shows the index rank.

V‑Trac Table (working logic):
- Iterates `VTRAC_DISPLAY` and renders each row with:
  - Index cell, optional row tint and rank badge.
  - Singles and Doubles cells: colorized digits per pair status; optional shape overlays; inline Sums badges.
- A plain CSV of Index/Singles/Doubles is downloadable via “Download V‑Trac Table (Working) CSV”.

Overdue Pairs Analysis (working thresholds):
- Thresholds mirror the working tool:
  - Repeating (doubles): RED ≥ 71, BLUE ≥ 107, PURPLE ≥ 25.
  - Non‑repeating: RED ≥ 37, BLUE ≥ 56, PURPLE ≥ 25.
- Side‑by‑side sections show the sets in each band. A Top‑5 list is also rendered in the four‑panel row.

Four‑Panel Row:
- Latest Draws — recent draws table.
- Pairs Analysis Results — counts of times drawn merged with current Draws‑Since.
- Combinations Analysis (Draws Since) — singles/doubles lists with shape badges and a scrollable container.
- Top 5 Most Overdue Repeating Pairs — compact, colorized list.

V‑Trac Index Hits (working logic):
- Reconstructs Recent/Overdue rank sets from `vstat` and scans the 1,000‑draw window to compute per‑index “Draws Since”.
- Renders a sortable table in a scrollable container.

Control Center — Doubles Aggregation

- Reads all `data/cleaned/*_draws.csv`, builds `state → draws`, and passes to the same `get_doubles_history` used on the Aux page.
- Produces a table with columns: `State`, `Draws Since Last Double`, `Latest Double`, `Total Draws`.
- Sorts by “Draws Since Last Double” (desc), then `State`.
- A “Refresh Combined Table” button evicts the cached dataframe from `st.session_state` and recomputes.

Caching and Session Behavior

- `@st.cache_data(ttl=1800)` on `cached_aux_analysis(state)` caches the full analysis per state for 30 minutes.
- `st.session_state["combined_doubles_df"]` stores the Control Center aggregation; the refresh button clears it.
- `analysis_draws` window defaults to 100 via `st.session_state.get("analysis_draws", 100)` and is used by Sums when available.

Safety and Boundaries (No Regressions)

- Only `src/app.py` was changed; other modules remain untouched.
- Staged “working” imports are isolated to the Aux page via `_AUX_WORKING_ROOT` so other tools do not resolve against the staged copies.
- Draw generation writes only to `data/cleaned/`; no mutation of legacy folders.
- V‑TRAC Analyzer continues to use `core.module_c_vtrac`. Stable Pattern and Digit Reduction pages are unchanged apart from their own page code.

How to Use (Operator Notes)

1) Launch the app (e.g., `run_app.bat`).
2) Go to “Auxiliary Tools”, pick a state, click “Run Auxiliary Tools Analysis”.
   - If cleaned CSVs exist, they’re used immediately.
   - If not, the page may run the staged `run_process` once to produce them, then proceed.
3) Review rendered sections; download the V‑Trac CSV if needed.
4) Go to “Control Center” and click “Refresh Combined Table” to see the cross‑state doubles table.

Known Limitations / Next Targets (non‑blocking)

- Sums: integration is wired and renders when the Sums package is importable; badges have local fallbacks. Further unification and error surfacing can be done later.
- Optional: unify V‑TRAC reference usage globally after Aux parity is fully finalized.

Change Log (high level)

- Added robust CSV‑first draw loading with extractor and staged runner fallbacks.
- Integrated working Aux analysis (`analyze_pairs`, `vtrac_reference`) with visual parity.
- Added V‑Trac Index Hits table.
- Added Control Center doubles aggregation using cleaned CSVs.
- Implemented import path isolation for safety and introduced local Sums helpers and context managers for conflict‑free imports.


