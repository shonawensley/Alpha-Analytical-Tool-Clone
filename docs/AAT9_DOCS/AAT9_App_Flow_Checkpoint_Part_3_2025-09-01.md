# AAT9 — Integrated App Data Flow (Part 3) — 2025‑09‑01

Purpose: Explain how the Streamlit app (`src/app.py`) stitches together all tools, what each page depends on, and how data moves. This clarifies that most tools consume the combined/tables pipeline while Auxiliary Tools uniquely run from per‑state draw CSVs.

## Big Picture

- Single Streamlit app with multiple pages:
  - V‑TRAC Analyzer
  - Stable Pattern Extractor
  - Digit Reduction
  - Auxiliary Tools (unique draw‑file source)
  - Control Center (cross‑state view)
- Shared rule: pages are self‑contained but read from the project’s canonical outputs, avoiding side effects on other tools.

## Data Sources by Page

- V‑TRAC Analyzer
  - Code: `show_vtrac_page(state)`
  - Uses `core.module_c_vtrac.main()` (internals read tables/structures used historically by the V‑TRAC page).
  - Input: processed/combined artifacts produced by the data pipeline (tables and HTML/CSV generated under `tables/` and `data/outputs/`).

- Stable Pattern Extractor
  - Code: `show_stable_pattern_page(state)`
  - Imports: `from core import stable_pattern_extractor as stable`
  - Paths: via `utils.path_handler` functions
    - `ph.get_state_tables_dir(state)` → state’s tables directory
    - `ph.get_analysis_dir("patterns", state)` → output dir for pattern results
  - Input: combined state tables; Output: pattern CSV/HTML to analysis directory

- Digit Reduction
  - Code: `show_digit_reduction_page(state)`
  - Imports: `from core.module_b_digit_reduction import run_digit_reduction`
  - Input path root: `get_tables_output_dir()`; checks `tables_root/state`
  - Input: state’s tables (combined); Output: digit‑reduction dataframe + CSV/HTML (paths returned by `run_digit_reduction`)

- Auxiliary Tools (Working parity logic; unique source)
  - Code: `show_aux_page(state)` with nested `cached_aux_analysis(state)`
  - Working imports (staged): `modules.analyze_pairs`, `modules.vtrac_reference`
  - Input order:
    1) `data/cleaned/<State>_draws.csv`
    2) `data/processed/draws/<State>_draws.csv`
    3) Fallbacks: read‑only extractor; or staged `modules.run_process()` to generate cleaned CSVs once
  - Outputs (rendered in‑page): V‑Trac table, Overdue Pairs, Top‑5, V‑Trac Index Hits, optional Sums badges/table

- Control Center (Cross‑state)
  - Code: `show_control_center_page()`
  - Data source: scans `data/cleaned/*_draws.csv`
  - Logic: `get_doubles_history` + aggregation into a dataframe; cached in `st.session_state["combined_doubles_df"]`

## Why Auxiliary Tools are Different

- Most tools read the “combined tables” pipeline outputs under `tables/` (via `utils.path_handler`) or project analysis outputs under `data/outputs/`.
- Auxiliary Tools expressly operate on raw per‑state draw CSVs `*_draws.csv` for working‑tool parity and speed.
- This separation ensures Aux changes don’t interfere with Stable Pattern, Digit Reduction, or V‑TRAC calculations.

## Import Isolation & Safety

- `_AUX_WORKING_ROOT` adds `scripts/auxiliary/working` to `sys.path` so `modules.*` resolves to staged copies only for Aux.
- `_project_modules_first()` temporarily prioritizes `PROJECT_ROOT/modules` for optional Sums imports:
  - `module_d_auxiliary_tools.refactored.sums_analysis`
  - `module_d_auxiliary_tools.refactored.sums_ui`
- Other pages continue to use their respective `core/*` and `utils/*` modules.

## Caching & Session State

- Aux analysis cached with `@st.cache_data(ttl=1800)` per state.
- Control Center stores its combined table in `st.session_state["combined_doubles_df"]`; a refresh button evicts cache.

## Typical End‑to‑End Flow (Operator Mental Model)

1) Run the data pipeline (outside the app if needed) to produce combined tables under `tables/`.
2) V‑TRAC, Stable Pattern, Digit Reduction pages read those tables for state‑specific analytics.
3) Auxiliary Tools page reads per‑state draw CSVs and renders working‑tool parity visuals; if CSVs are missing, it can generate them from `data/original/Pick3StatsC4.xlsm` once via the staged runner.
4) Control Center combines all `data/cleaned/*_draws.csv` to present a cross‑state doubles table.

## Key File & Function Index

- `src/app.py`
  - View functions: `show_vtrac_page`, `show_stable_pattern_page`, `show_digit_reduction_page`, `show_aux_page`, `show_control_center_page`, `show_hot_zones_page`
  - Aux cached core: `cached_aux_analysis(state)`
  - Sums helpers: `_sum3`, `_root`, `_root_sum3`, `_sums_badge_for`
  - Import contexts: `_project_modules_first()`, `_AUX_WORKING_ROOT` path hook
  - Table paths: `utils.path_handler.get_tables_output_dir()`, `ph.get_state_tables_dir`, `ph.get_analysis_dir`

## Current Gaps / Next Improvements

- Unify status messages for missing data across pages (common helper for "data/cleaned" and "tables").
- Optional banner if Sums package is missing (beyond sidebar caption), to guide operators.
- Document minimal CSV schema for `*_draws.csv` to prevent adapter churn across tools.
- Control Center: add per‑state links back to Aux or to CSV locations for quick inspection.

## TL;DR

- Combined tables power V‑TRAC, Stable Pattern, Digit Reduction.
- Auxiliary Tools uniquely run on per‑state draw CSVs (`data/cleaned/*_draws.csv` with safe fallbacks).
- Control Center summarizes across those CSVs.
- Import isolation and caching ensure these parts remain self‑contained while presented in one app.

## Visual Flow (Mermaid)

```mermaid
flowchart TB
  subgraph Pipeline[Combined Tables Pipeline]
    A[data/original/Pick3StatsC4.xlsm]
    A -->|extract/clean/build| T[tables/ (state tables)]
  end

  subgraph AppPages[Streamlit App Pages]
    V[V‑TRAC Analyzer]
    S[Stable Pattern Extractor]
    D[Digit Reduction]
    X[Auxiliary Tools]
    C[Control Center]
  end

  T --> V
  T --> S
  T --> D

  subgraph Draws[Per‑state Draw CSVs]
    DC[data/cleaned/*_draws.csv]
    DP[data/processed/draws/*_draws.csv]
  end

  DC --> X
  DP --> X
  A -->|staged runner (once if needed)| DC

  DC --> C

  style X fill:#eef,stroke:#88a,stroke-width:1px
  style C fill:#eef,stroke:#88a,stroke-width:1px
```

## Data Contracts & Directories (Quick Ref)

- Combined tables
  - Root: `tables/`
  - Accessors: `utils.path_handler.get_tables_output_dir()`, `ph.get_state_tables_dir(state)`
- Aux draw CSVs
  - Primary: `data/cleaned/<State>_draws.csv`
  - Secondary: `data/processed/draws/<State>_draws.csv`
  - One‑time generator: `modules.run_process(Pick3StatsC4.xlsm, ...)` (staged)
- Control Center cache
  - `st.session_state["combined_doubles_df"]`
- Sums
  - Optional package path: `modules/module_d_auxiliary_tools/refactored/{sums_analysis.py,sums_ui.py}`
  - Import guard: `_project_modules_first()`

## Troubleshooting Checklist

- Missing combined tables → run the pipeline; verify `tables/<State>/` exists.
- Aux page shows "Working modules unavailable" → ensure `scripts/auxiliary/working` is present and `_AUX_WORKING_ROOT` is active.
- No Sums table/badges → confirm `module_d_auxiliary_tools/refactored` exists under `PROJECT_ROOT/modules` and imports succeed (sidebar caption shows the module).
- Control Center empty → verify `data/cleaned/*_draws.csv` files exist.
