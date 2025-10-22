
- **Scope**: Replace the legacy V-TRAC analyzer core with an enhanced engine while keeping the Streamlit UI layout, winners logging, and data contracts unchanged.
- **Non-goals**: No edits to Winners Logger, Aux pipelines, or other tools. No UI redesign—only swap the backend engine and add optional feature flag/tuning hooks.
- **Data contracts**:
  - Inputs: `data/outputs/tables/<STATE>/*_Combined.csv` (Midday/Evening/Combined) via `utils.path_handler`.
  - Outputs: predictions/evidence JSON + artifacts under `data/outputs/analysis/vtrac_enhanced/<STATE>/`.
- **Feature set** (must implement):
  - Right-column survival and persistence (cols 3→1) across R2/R4/R6/R8.
  - Hot/superhot boosts per draw & ring.
  - Cross-section echo (Midday/Evening/Combined) consensus.
  - Mask-drop emergence + reduction assists.
  - Straight-order cues & mirror assists (feeds straights ranking).
  - Doubles affinity & recency rotation dampers.
- **Packages / file map** (authoritative):
  1. `modules/vtrac_enhanced/__init__.py`
  2. `modules/vtrac_enhanced/types.py` – dataclasses: `Cell`, `PatternsGrid`, `SectionData`, `EngineInput`, `IndexEvidence`, `IndexScore`, `EngineOutput`.
  3. `modules/vtrac_enhanced/config.py` – default weights/flags (ring/column/set/section, hot boosts, bonuses, toggles for mirror/reduction/evidence).
  4. `modules/vtrac_enhanced/features.py` – pure extraction helpers producing a structured evidence map per index.
  5. `modules/vtrac_enhanced/engine.py` – orchestrates signals → scores → ranked indices + straights (expose `run_analysis(EngineInput) -> EngineOutput`).
  6. `modules/vtrac_enhanced/adapters.py` – table loader using `utils.path_handler`, JSON writer, helper to build `EngineInput` from combined tables.
  7. `tools/vtrac_enhanced_cli.py` – CLI smoke: load tables for a state, run engine, dump summary & write artifacts.
  8. `tests/test_vtrac_enhanced_basic.py` – unit tests using trimmed fixtures validating scoring & straight ordering.
  9. `src/core/module_c_vtrac_enhanced.py` – thin Streamlit orchestrator gated by feature flag (imports engine, renders using existing layout helpers).
- **Guardrails**:
  - Run every command from repo root (`c:\dev\Alpha-Analytical-Tool`).
  - Minimal diffs; no edits to Winners Logger or Aux modules.
  - Use only `utils.path_handler` for filesystem paths.
  - Add docstrings where code isn’t self-explanatory; keep ASCII.
  - All new modules must be deterministic & testable; no network I/O.
- **Verification**:
  - `pytest tests/test_vtrac_enhanced_basic.py`
  - `python tools/vtrac_enhanced_cli.py --state Connecticut4`
  - Manual Streamlit smoke (optional) behind feature flag; capture `.codex/first_boot.log` tail if run.
- **Rollout**:
  - Default feature flag `AAT9_FLAGS.ENHANCED_VTRAC` (true once validated).
  - Keep legacy engine callable for fallback until enhanced version is vetted.
