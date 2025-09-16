# AAT9 — AI/Contributor Guide

## Principles
- Path‑safe by default: always run from repo root; use canonical helpers.
- Minimal diffs; archive‑first for cleanup; reversible changes.
- Soft‑fail UI: show captions/warnings; log details in `.codex/first_boot.log` for validation.

## What to Read First
1) KIT README (this folder)
2) Architecture & Dir Layout (canonical)
3) Quickstart Cheat Sheet
4) Preflight Reference

## Adding a New Tool/Module
- Data contract: define exactly what it reads and where it writes.
- Read from canonical dirs:
  - Draws: `data/cleaned/*_draws.csv` (use `modules.aux_loaders.load_state_draws`)
  - Combined tables: `utils.path_handler.get_tables_output_dir()` / `get_state_tables_dir(state)`
- Write outputs under `data/outputs/analysis/<tool>/<STATE>/`.
- Keep logic pure (no `os.chdir`), use `pathlib.Path` joins.

## Wiring into the App (src/app.py)
- Add a new page or integrate with an existing page with a button‑triggered compute.
- For heavy/expensive steps: compute once, cache, and render from cache.
- For optional imports (e.g., sums), guard with try/except and show friendly captions on failure.

## Import & Path Hygiene
- Use `utils.path_handler` for all output/data paths.
- BA and Aux should never read combined string‑tables; BA is draws‑only.
- Absolute‑path BA loader remains in `src/app.py` to avoid `modules` collisions.
- Legacy forwarder: `src/utils/path_handler.py` re‑exports `utils.path_handler` — do not add logic there.

## Verification Workflow
- Preflight: `.codex/preflight.ps1 -State "Connecticut4"`
- Compile: `python -m py_compile` on changed files
- Import probes: `python -c "import importlib; importlib.import_module('utils.path_handler')"`
- Optional headless boot: `STREAMLIT_BROWSER=none` with log to `.codex/first_boot.log`

## Documentation Updates
- Update KIT docs alongside code changes:
  - Architecture/Dir Layout (if structure changes)
  - Unified Changelog (summarize the change)
  - App Flow Addendum (if page wiring or contracts change)
- Diagrams: prefer Mermaid blocks embedded in docs for easy diffs.

## Guardrails Checklist (before PR/delivery)
- Launch entry unchanged (`run_app.bat`, `src/app.py`).
- Imports resolve to in‑repo files (preflight confirms).
- Data contracts respected (Aux/BA vs Combined).
- UI soft‑fails with clear captions on missing data.
- Minimal diff; archive legacy if cleaning up.


### Dev Health
Toggle on app pages to quickly verify environment, import bindings, and data availability before coding:
- Control Center: bindings for `utils.path_handler`, `modules.vtrac_reference`, `modules.winner_report_full`, `modules.blackapple`, `modules.aux_loaders`, `core.pipeline_runner`; tables root inventory.
- Winners Full tile: `modules` binding, canonical vtrac_reference path, builder presence, per-state combined tables existence.
- V-TRAC Analyzer + Stable: module bindings and tables roots for their flows.
