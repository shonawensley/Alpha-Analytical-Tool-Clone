# AAT9 — Pitfalls & Fast Fixes

Synthesized from PITFALLS and recent integration experiences.

## Stray If / Def Indentation
- Symptom: `IndentationError: expected an indented block` near `if` or a `def` under an `if`.
- Fix: remove stray `if` or add a body (e.g., `pass`); keep function at correct indentation.

## Mixed Imports (bare vs namespaced)
- Symptom: Different modules with same names; silent empties or mismatched outputs.
- Fix: Use canonical imports (`modules.*`, `alpha_analytical.stable`); add forwarders/SSOT where needed.

## Wrong CWD / Interpreter
- Symptom: Missing files, odd paths (OneDrive/home) in logs.
- Fix: Launch via `run_app.bat` from repo root; use preflight to confirm cwd and Python.

## Expensive Compute on Render
- Symptom: Slow navigation; repeated reruns.
- Fix: Compute on button click; cache or write outputs and render from them.

## Artifacts in Source Tree
- Symptom: JSON/CSV files under `src/` or `modules/`.
- Fix: Write only under `data/outputs/analysis/...` or `data/runs` (if used).

## Aux/BA Using Wrong Data Source
- Symptom: BA candidates inconsistent; Aux tables empty.
- Fix: Ensure draws come from `data/cleaned/*_draws.csv` via `modules.aux_loaders`.

