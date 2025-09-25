# CODEX READ FIRST — AAT9 (Autonomous Mode)

Intent
- Work like an expert operator. **Phase A**: brief, high‑signal brainstorm that follows the docs and my instructions, YOU CAN GO WORK ON YOUR OWN WHEN I END BRAINSTORM BY SAYING "BRAINSTORM END". **Phase B**: execute without pausing for permission except when crossing explicit guardrails. Only stop if a decision materially risks data loss, repo structure, or contradicts project rules.

Session Setup
- Model: **gpt-5-codex (High)**.
- CWD: **C:\dev\Alpha-Analytical-Tool** (enforce continuously).
- Read in this order:
  1) `.codex/AGENTS.universal.md` (base rules)
  2) `AGENTS.md` (project-specific; overrides ambiguity)
  3) `docs/AAT9_KIT/AAT9_KIT_README.md`
  4) `docs/AAT9_KIT/AAT9_Workflow_Standard.md`
  5) `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`
  6) `docs/AAT9_KIT/AAT9_Preflight_Reference.md`
  7) `docs/AAT9_DOCS/AAT9_Live_Wiring_and_Data_Paths.md`
  8) `docs/AAT9_DOCS/AAT9_Blackapple_Module.md`
  9) `docs/AAT9_KIT/AAT9_Unified_Changelog.md`
  10) `docs/AAT9_KIT/AAT9_Checkpoint_Log.md`
  11) `briefings/PITFALLS.txt`


**Data contracts recap:** Aux/BA -> `data/cleaned/*_draws.csv` (draws-only). V-TRAC/Stable/DR -> combined tables (`tables/<STATE>/` or `data/outputs/tables/<STATE>/`) via `utils.path_handler`. Combined is baseline; Midday/Evening are additive variants surfaced alongside Combined.

Preflight (run now, no approval needed)
- `.codex\preflight.ps1 -State "Connecticut4"`
- If any mismatch (cwd/import/data) → fix exactly one root cause, re‑run preflight, then proceed.

Approvals profile (set now)
- Allow (no prompt):
  - read/list anywhere in repo
  - write under `docs/**`, `docs/AAT9_*`, `.codex/**` (docs, logs, images)
  - run `python -m py_compile` on touched files
  - run `.codex\preflight.ps1`
- Ask:
  - edits under `src/**`, `modules/**`, `utils/**`, `alpha_analytical/**`
  - launching Streamlit beyond headless smoke
  - Git commits/pushes
- Deny:
  - network operations or writes outside the repo

Phase A — Brainstorm (timebox: ~5 minutes, one screen)
- Summarize current repo state (preflight highlights), what you will do today, exact files you expect to touch, and why.
- Confirm any assumptions about variants (Combined vs Midday/Evening) against `AAT9_Live_Wiring_and_Data_Paths.md` and `AAT9_Blackapple_Module.md`.

Phase B — Execute (autonomous)
- Proceed without asking on:
  - documentation improvements in `docs/**`, adding/refreshing diagrams, updating `AAT9_Unified_Changelog.md` and `AAT9_Checkpoint_Log.md`
  - adding smoke scripts under `scripts/checks/**` that are read‑only except for repo‑internal outputs
  - running `py_compile` and `.codex\preflight.ps1`
- Escalate only if:
  - you need to change app wiring, analyzers, or pipelines
  - imports resolve outside the repo
  - you detect data writes outside `data/**` or `data/outputs/**`

Documentation & Logging (automatic)
- If you change behavior or wiring, update KIT docs in the same PR.
- Always append a terse line to `AAT9_Unified_Changelog.md` and a short context section to `AAT9_Checkpoint_Log.md`.

Finish signal
- When Phase A plan is printed and preflight is clean, reply: **"READY — Autonomous"** and begin Phase B immediately.
- During Phase B, only pause for explicit guardrails listed above.
