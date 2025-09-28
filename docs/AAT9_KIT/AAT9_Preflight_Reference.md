# AAT9 — Preflight Reference

Script: `.codex/preflight.ps1`

## Usage
- Basic: `powershell -NoProfile -File .codex/preflight.ps1`
- With state: `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`

## What It Prints
- CWD (should be repo root)
- Python interpreter path
- Import file paths for:
  - `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`
- `data/cleaned/*_draws.csv` inventory (first 20 shown)
- If `-State` provided: resolved CSV path and draw count for that state

## Example Output (abbrev.)
```
AAT9 Preflight (Windows)
--------------------------------
CWD: C:\dev\Alpha-Analytical-Tool
Python: C:\Python\python.exe
Imports:
{ "utils.path_handler": ".../utils/path_handler.py",
  "modules.blackapple": ".../modules/blackapple.py",
  "modules.aux_loaders": ".../modules/aux_loaders.py",
  "alpha_analytical.stable": ".../alpha_analytical/stable/__init__.py" }
data/cleaned inventory: 18
 - Connecticut_draws.csv
 ...

Selected state resolution:
State: Connecticut4
Source: data\cleaned\Connecticut_draws.csv
Draws: 1000
--------------------------------
Tip: Use run_app.bat to launch the UI from repo root.
```

## Triage Tips
- If imports point outside the repo: re‑launch from repo root (`run_app.bat`) or fix the active interpreter.
- If draws inventory is empty: confirm CSVs exist under `data/cleaned/`.
- If a state doesn’t resolve: normalize the name (e.g., "Connecticut4" → base "Connecticut").


## Quick Smokes (run after preflight)
- `python scripts/checks/smoke_project_loader.py`
- `python scripts/checks/smoke_positional.py`
- `python scripts/checks/smoke_aux_vtrac.py`

