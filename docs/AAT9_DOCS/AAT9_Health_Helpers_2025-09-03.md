# AAT9 — System Health Helpers (2025‑09‑03)

Overview

This document describes the small, read‑only “System Health” helpers added to the integrated app. These helpers make the environment, import sources, and data resolution visible so you can diagnose issues quickly without touching analytics logic. They are DEV‑gated and safe to leave in the codebase long‑term.

What Was Added

- Control Center: A System Health expander (dev only) that shows:
  - cwd (current working directory)
  - Python executable path
  - Blackapple module file path (loaded via absolute‑path loader)
  - (Optional) draws CSV inventory, per state
- Auxiliary Tools: A System Health (Aux) expander (dev only) that shows:
  - cwd, Python executable
  - Blackapple module file path (absolute‑path loader)
  - Resolved draws CSV for the selected state + row count (via CSV‑only loader)
- The helpers are read‑only UI blocks, behind a simple sidebar checkbox (“Show Dev Health”).

Why They Are Helpful

- Prevents “mystery bugs”: You see exactly which files and env are in use (no guessing).
- Faster diagnosis: Confirms whether a symptom is an env/import issue vs. a data issue within seconds.
- No risk: Purely observational; they never alter control flow or analytics logic.
- Scales with complexity: As you add tools/pages, a consistent health block keeps behavior predictable.

How They Work (Key Ideas)

- Absolute‑path loader for Blackapple ensures the project’s `modules/blackapple.py` is used even if a staged package named `modules` exists.
- CSV‑only loader for Aux/BA resolves `data/cleaned/*_draws.csv` robustly (tolerates underscores/trailing “4”).
- The health expander prints:
  - Env: `cwd`, Python binary; sys.path length (optional)
  - Modules: `__file__` for the relevant modules (BA, analyze_pairs, etc.)
  - Data: counts and the resolved draws CSV for the selected state (Aux)

When to Enable

- Development and debugging: turn on “Show Dev Health” in the sidebar.
- CI/preflight: prefer the `.codex/preflight.ps1` script when not running the UI.
- Daily operations: leave off — expanders are DEV‑only and add no noise when disabled.

What “Good” Looks Like

- Control Center/Aux:
  - `cwd` prints your repo root (e.g., `C:\dev\Alpha-Analytical-Tool`)
  - `python` path points to your intended interpreter/venv
  - `BA module` shows a path under `<repo>\modules\blackapple.py`
  - For the selected state: a valid draws CSV path under `data/cleaned` and a reasonable row count

Preflight (CLI)

- `.codex/preflight.ps1 -State "<State>"` prints:
  - cwd (repo root), Python info
  - verified BA import path
  - `data/cleaned/*_draws.csv` inventory
  - selected CSV for the given state (normalized)

Safety & Gating

- Read‑only: expanders never modify state or analytics
- DEV‑gated: sidebar checkbox or an `APP_DEV=1` environment flag can be used to show only in dev
- Small and local: helpers are per‑page blocks (no global refactors)

Troubleshooting Examples

- “No module named modules.blackapple”
  - The expander shows BA module “unavailable” or resolving from the wrong place
  - Absolute‑path loader ensures `<repo>\modules\blackapple.py` is used
- “No candidates” or empty BA rows
  - Confirm a `*_draws.csv` exists for the state (Aux expander shows the resolved CSV path). Look for `.cvs` typos and rename to `.csv`.
- “Works here, not there”
  - Check `cwd` and Python path. Ensure your BAT pushd’s to the repo root and (optionally) sets `PYTHONPATH=%CD%`.

Future Expansion

- Add similar expanders to V‑TRAC, Stable Pattern, Digit Reduction (dev‑only)
  - Show their entry modules’ `__file__` and expected input directories (tables/…) with existence and counts
- Dedicated “System Health” page that aggregates checks across all pages/modules
- Automated preflight that runs before a “Log Winner” action to guarantee input consistency

Checklist (Operator)

- Turn on “Show Dev Health” when diagnosing
- Confirm BA module path and draws CSV resolution
- Use `.codex/preflight.ps1 -State "<State>"` to verify outside UI
- Keep BAT launching from the repo root; activate your venv

Notes

- These helpers are intentionally minimal and extensible. If your needs grow (e.g., more detailed data checks or cache diagnostics), add them gradually behind the same DEV gate to keep the main UI clean.
