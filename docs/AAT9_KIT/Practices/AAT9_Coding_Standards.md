# AAT9 — Coding Standards (Path‑Safe, Minimal, Maintainable)

## Imports & Structure
- Prefer explicit imports; avoid wildcard except for documented forwarders.
- Keep analyzers as pure functions (no global state mutations, no os.chdir).
- Use `pathlib.Path` for all filesystem paths; build paths relative to canonical roots (see `utils.path_handler`).
- Module boundaries: shared analyzers under `modules/` or `alpha_analytical/`; thin wrappers in `src/core/`; Streamlit wiring in `src/app.py` only.

## Path & Data Hygiene
- Always assume CWD is repo root when running app/bats.
- Read draws for Aux/BA only from `data/cleaned/*_draws.csv` (use `modules.aux_loaders.load_state_draws`).
- Read combined tables for V‑TRAC/Stable/DR via `utils.path_handler` helpers (`get_tables_output_dir`, `get_state_tables_dir`).
- Write outputs under `data/outputs/analysis/<tool>/<STATE>/`; never write inside source folders.

## UI & Error Handling
- UI computes on button click; avoid expensive compute on render.
- Soft‑fail: show `st.warning`/`st.caption` for missing data/imports instead of raising.
- Keep “System Health” diagnostic expanders available in dev.

## Style & Consistency
- Naming: descriptive, no one‑letter locals except obvious counters.
- Keep functions small; extract helpers when logic grows.
- Minimal diffs: change only what the task requires; prefer additive changes.

## Testing & Validation
- Run `python -m py_compile` on changed files.
- Use `.codex/preflight.ps1` for environment/import sanity.
- Optional headless boot with `.codex/first_boot.log` for UI validation.

## Forwarders & Shims
- One source of truth for path helpers: `utils.path_handler`.
- Legacy import forwarders are allowed (e.g., `src/utils/path_handler.py` → re‑exports canonical) to prevent breakage during cleanup.

