# AAT9 — Pitfalls & Fast Fixes

Synthesized from PITFALLS and recent integration experiences.

## Stray If / Def Indentation
- Symptom: `IndentationError: expected an indented block` near `if` or a `def` under an `if`.
- Fix: remove stray `if` or add a body (e.g., `pass`); keep function at correct indentation.

## Mixed Imports (bare vs namespaced)
- Symptom: Different modules with same names; silent empties or mismatched outputs.
- Fix: Use canonical imports (`modules.*`, `alpha_analytical.stable`); add forwarders/SSOT where needed.

## Duplicate Package Shadowing (`utils`)
- Symptom: `ImportError: cannot import name ...` from `utils.path_handler` resolving to `src\utils\path_handler.py`, or `NameError: Path is not defined`.
- Cause: Two `utils` packages exist (`/utils` canonical, `/src/utils` legacy). If `src` is first on `sys.path`, `utils.*` may bind to the legacy package.
- Fix:
  - SSOT bootstrap at app entry: ensure project root is first, evict premature `utils` bindings that point to `/src/utils`, and import canonical `utils.path_handler`.
  - Do not import from `src/utils` (see KEEPERS). Keep the legacy tree for reference only.

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

\n## Aux Staging Legacy Dependency\n- Symptom: Aux shows `cannot import name BOXED_LABEL_LOOKUP` or Dev Health reports staged modules missing.\n- Fix: Run `python scripts/checks/smoke_aux_vtrac.py`; restore the files listed in `docs/AAT9_DOCS/AAT9_Aux_Staging_Manifest.md` before archiving.

## Analyzer V2 Guardrails
- Treat `alpha_analytical/digit_reduction/analyzer_v2/` as read-only for the live page; it only consumes reducer training logs and emits artifacts to `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/`.
- Keep feature key names aligned with `config.yml` (`final.canon3`, `method.agree_count`, etc.) so the scorer remains zero-safe; adjust the config instead of patching callers.
- VTRAC synergy must go through `analyzer_v2.vtrac_index` (predictions JSON preferred, derived fallback). Do not import staged `modules.vtrac_reference` from Aux.
- Run `.codex/preflight.ps1 -State <STATE>` before edits and the documented python smoke command after changes to confirm artifacts are fresh and scores populate.
- Winners Overlay: run_winner_overlay_batch() only after the reducer outputs exist; artifacts land under analyzer_v2/winners plus a mirrored stamp in the Winners tree when enabled. Merge the flags CSV back onto the analyzer per-item table via the identity columns to expose dr_win_* signals.
