# CODEX READ FIRST — AAT9 (Standard Mode)

Goal
- Start in controlled mode (yolo=false). Highest-quality planning, path-safe execution, consistent logging. Ask before any destructive or repo-wide change.

Session Setup
- Model preset: **gpt-5-codex, High reasoning**.
- CWD must be **C:\dev\Alpha-Analytical-Tool** at all times.
- Print-only sanity:
  - `git status -s`
  - `git branch -vv`
  - `git remote -v` (no remote edits)

Read these first (order)
1) `.codex/AGENTS.universal.md` (non-negotiables)
2) `AGENTS.md` (project-specific rules override any ambiguity)
3) `docs/AAT9_KIT/AAT9_KIT_README.md`
4) `docs/AAT9_KIT/AAT9_Workflow_Standard.md`
5) `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`
6) `docs/AAT9_KIT/AAT9_Preflight_Reference.md`
7) `docs/AAT9_DOCS/AAT9_Live_Wiring_and_Data_Paths.md`  ← data contracts & page wiring
8) `docs/AAT9_DOCS/AAT9_Blackapple_Module.md`            ← BA uses data/cleaned/*_draws.csv, renders in Control Center
9) `docs/AAT9_KIT/AAT9_Diagrams_Guide.md`
10) `docs/AAT9_KIT/AAT9_Unified_Changelog.md` (for logging)
11) `docs/AAT9_KIT/AAT9_Checkpoint_Log.md` (context/rationale log)
12) `docs/AAT9_KIT/HUMAN_READ_FIRST_AAT9.md`
13) `docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md`
14) `docs/AAT9_DOCS/AAT9_App_Flow_Addendum_2025-09-06.md`
15) `docs/AAT9_DOCS/AAT9_Architecture_Dir_Layout_2025-09-06.md`
16) `briefings/PITFALLS.txt`


**Data contracts recap:** Aux/BA -> `data/cleaned/*_draws.csv` (draws-only). V-TRAC/Stable/DR -> combined tables (`tables/<STATE>/` or `data/outputs/tables/<STATE>/`) via `utils.path_handler`. Combined is baseline; Midday/Evening are additive variants surfaced alongside Combined.

Preflight (run now)
- PowerShell: `.codex\preflight.ps1 -State "Connecticut4"`
  - Confirms: cwd, Python path, and import locations for `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`.
  - Lists `data/cleaned/*_draws.csv` inventory.
- If anything off, stop and report the mismatch.

Dev Health (when you launch the app)
- Launch via `run_app.bat` (pushd to repo root → `streamlit run src\app.py`).
- Toggle the in‑app “System Health” expander once to confirm:
  - cwd, interpreter
  - module `__file__` paths resolve **inside the repo**
  - draws source root looks correct

Operate — Plan → Implement → Verify → Document
- Plan: state exact files to change and why; show minimal diffs beforehand.
- Implement: smallest possible diffs; **never** write outside the repo.
- Verify:
  - `python -m py_compile` on touched modules
  - optional headless boot (≤120s) → `.codex/first_boot.log`
- Document:
  - Append to `docs/AAT9_KIT/AAT9_Unified_Changelog.md` (concise)
  - Add a short section to `docs/AAT9_KIT/AAT9_Checkpoint_Log.md` (why/impact)
  - Update any affected KIT docs

Guardrails (must ask first)
- Any file writes under `src/`, `modules/`, `utils/`, or `alpha_analytical/`
- Any Streamlit run beyond headless smoke
- Any Git operations other than read‑only status
- Any change to table/draw pipelines

Done criteria (reply READY when all below are true)
- Preflight clean; paths confirmed
- No uncommitted unrelated diffs
- Work plan written; expected diffs listed
- You are waiting for approval to proceed
