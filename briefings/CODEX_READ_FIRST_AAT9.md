# CODEX READ FIRST — AAT9 Optimized Startup

Read and follow this sequence exactly before coding. Goal: highest‑quality planning, path‑safe execution, and consistent documentation/logging.

## 1) Session Setup
- Operate with high reasoning, yolo=false mindset (ask before destructive changes).
- Ensure CWD is the repo root: `C:\dev\Alpha-Analytical-Tool`.
- Print‑only sanity: `git status -s`, `git branch -vv`, `git remote -v` (no changes to remotes).
- Confirm launch path: `run_app.bat` → `streamlit run src\app.py`.

## 2) Read These (KIT first)
- `docs/AAT9_KIT/AAT9_KIT_README.md` (index)
- `docs/AAT9_KIT/AAT9_Workflow_Standard.md` (step‑by‑step workflow)
- `docs/AAT9_KIT/Practices/AAT9_Coding_Standards.md` (path‑safe coding)
- `docs/AAT9_KIT/Practices/AAT9_Agent_Operating_Rules.md` (guardrails)
- `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md` (daily flow)
- `docs/AAT9_KIT/AAT9_Preflight_Reference.md` (expected outputs)
- `docs/AAT9_KIT/AAT9_Diagrams_Guide.md` (Mermaid updates)
- `docs/AAT9_KIT/AAT9_Unified_Changelog.md` (so you know how to log changes)
- Also skim project rules: `AGENTS.md` and `.codex/AGENTS.universal.md`

## 3) Preflight
- Run: `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`
- Confirm imports resolve to in‑repo files and that draws CSVs are present.

## 3.5) Dev Health (fast checks in UI)
- Control Center: toggle Dev Health to see key module bindings (path_handler, vtrac_reference, winner_report_full, blackapple, aux_loaders, pipeline_runner) and tables root inventory.
- Winners Full tile: toggle Dev Health to confirm `modules` binding, canonical vtrac_reference path, builder presence, and per‑state combined tables existence.

## 4) Plan → Implement → Verify → Document
- Plan: small, explicit; state files to change and why; wait for approval if collaborating.
- Implement: minimal diffs; use `utils.path_handler` for outputs; Aux/BA draws‑only.
- Verify: `python -m py_compile`, import probes, optional headless boot (120s) → `.codex/first_boot.log`.
- Document: update KIT docs if affected; always add a Changelog entry.

## 5) Done Checklist
- App launches from `run_app.bat`; pages render without path errors.
- All changes logged in `AAT9_Unified_Changelog.md`.
- If structure/wiring changed, update Architecture/App Flow docs.

## Notes
- Never write outside the repo; do not modify git remotes.
- Archive‑first for cleanup; no deletions; keep changes reversible.
