# AAT9 — Checkpoint 2025‑09‑03 — Integration & Hardening Notes

Context

Blackapple now renders in Control Center across states. The primary remaining risks were path/import drift and name collisions; we addressed these without refactors.

What Worked

- Absolute‑path loader for BA (and CSV loader) in `src/app.py`.
- CSV‑only data source via `modules/aux_loaders.load_state_draws()`.
- Control Center rows: coherent triggers/candidates matching recent draw sequences.

Pitfalls We Hit (and Fixes)

- `modules` name collision (staged vs project): fixed by loading BA via absolute path; avoids relying on sys.path order and hot‑reload quirks.
- Mixed data sources: BA must not use combined string‑tables; CSV‑only prevents confusion and silent empties.
- CWD drift (BAT/IDE): quote and pushd to project root; optional PYTHONPATH.
- Brittle text surgery: prefer small, explicit code blocks over bulk line edits; verify with `python -m py_compile`.

Minimal Guardrails (Keep)

- Absolute‑path BA loader at both import sites.
- Deterministic BAT launcher: pushd "%~dp0"; optional `set "PYTHONPATH=%CD%"`; activate venv; `streamlit run src\app.py`.
- Optional “System Health” expander: print `cwd`, `sys.executable`, and BA module path.
- No refactors to other tools (V‑TRAC/Stable/DR) — keep Aux isolated.

Directory Hygiene (Next Checkpoint)

- Ensure a single canonical `modules/` (project) is the source of truth.
- Consider renaming staged aux package to avoid `modules` collisions (e.g., `aux_working`) — do later, not now.
- Keep outputs under data/ or runs/; avoid mixing with code packages.

Operator Checklist (Daily)

- Verify target `*_draws.csv` present under `data/cleaned`.
- Launch via BAT (project root)
- Control Center → scan BA rows (ALERT/WATCH) and triggers.
- Use “View all candidates” expander for full lists & tags.
- If something looks off, open the “System Health” expander.

Next Milestones

- Winners logging + daily ledger.
- Threshold calibration for BA triggers after a trial period.
- Optional state BA panels once Control Center is stable.
