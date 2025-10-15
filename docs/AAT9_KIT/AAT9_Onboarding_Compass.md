# AAT9 - Onboarding Compass

Purpose: first-stop briefing for operators and Codex before touching the repo. It distills the essentials - startup discipline, what to read next, how to validate work, and when to update docs - so you can ramp quickly without losing the guardrails captured elsewhere in the KIT.

## 0) Quick Start Runbook
- Model preset: `gpt-5-codex` (High reasoning) unless latency demands Medium.
- Root checks (print-only): `git status -s`, `git branch -vv`, `git remote -v`.
- Preflight (always before coding): `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"` (swap state as needed). Confirms cwd, python, key imports, draw inventory, and the active CSV.
- Optional but recommended: Launch via `run_app.bat` and toggle "Show Dev Health" on Control Center plus any page you will touch to verify bindings and data paths.

## 1) Core References (read in this order)
1. Workflow Standard (`docs/AAT9_KIT/AAT9_Workflow_Standard.md`) - Plan -> Implement -> Verify -> Document loop plus doc-update map.
2. Coding Standards (`docs/AAT9_KIT/Practices/AAT9_Coding_Standards.md`) - path-safe coding, data contracts, UI soft-fail rules.
3. Agent Operating Rules (`docs/AAT9_KIT/Practices/AAT9_Agent_Operating_Rules.md`) together with `AGENTS.md` and `.codex/AGENTS.universal.md` - non-negotiable guardrails.
4. Architecture and App Flow addenda (`docs/AAT9_DOCS/AAT9_Architecture_Dir_Layout_2025-09-06.md`, `docs/AAT9_DOCS/AAT9_App_Flow_Addendum_2025-09-06.md`) - canonical layout, launch path, and page data contracts.
5. Quickstart Cheat Sheet (`docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`) - concise commands, variant policy, Control Center batch notes.
6. Area-specific primers - read only when relevant (for example Aux or Blackapple work -> `docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md`, `docs/AAT9_DOCS/AAT9_Blackapple_Module.md`; positional pressure -> `docs/AAT9_KIT/important/AAT9_Positional_Pressure.md`).

Skim the Unified Changelog (`docs/AAT9_KIT/AAT9_Unified_Changelog.md`) after the references above to understand recent shifts and which docs were touched.

## 2) Working Loop (baseline expectations)
- Plan: declare targeted files and rationale, stay within scope, prefer additive diffs. (See Workflow Standard section 2.)
- Implement: use canonical loaders (`modules.aux_loaders`, `utils.path_handler`), keep analyzers pure, and add Dev Health captions for diagnostics only. (Coding Standards.)
- Verify: run `python -m py_compile` on touched modules, the relevant smoke (`python scripts/checks/smoke_positional.py`, `python scripts/run_acceptance.py --marker smoke`, etc.), and capture `.codex/first_boot.log` if you run headless Streamlit. (Workflow Standard section 4 and Quickstart.)
- Document: log changes immediately (see next section). Never skip this step even for docs-only edits.

## 3) Documentation and logging checklist
- Unified Changelog: add `YYYY-MM-DD - Category - Summary - Impact - Files/Refs`.
- Checkpoint Log: short rationale plus links per change.
- Update affected KIT docs: architecture, app flow, testing roadmap, or area primers if your change touches structure, wiring, or data contracts.
- Diagrams: use embedded Mermaid; follow the four-step update process in `AAT9_Diagrams_Guide.md`.
- Acceptance fixtures and docs: if tests or guardrails change, note it in `docs/AAT9_KIT/AAT9_Testing_Roadmap.md`.

## 4) Testing and health shortlist
- `python -m py_compile <file>` - baseline compile check.
- `.codex/preflight.ps1 -State "<State>"` - environment sanity (rerun if paths change).
- `python scripts/run_acceptance.py --marker smoke` - required before deeper changes; run the full suite for cross-page updates.
- Aux validators (`scripts/tools/validate_aux_*.py`) after draw refreshes or Aux logic edits.
- `python scripts/checks/smoke_positional.py` when positional pressure or Control Center doubles logic moves.

## 5) Data contracts and guardrails
- Aux and Blackapple consume only `data/cleaned/draws/*_draws.csv` (Combined baseline; Midday/Evening additive). Use `modules.aux_loaders.load_state_draws`.
- V-TRAC, Stable Pattern, Digit Reduction consume combined tables via `utils.path_handler`.
- Always operate from `C:\dev\Alpha-Analytical-Tool`; never change git remotes; avoid touching `core_legacy/` and combined-table readers without explicit tasks.
- Soft-fail in the UI: show captions or warnings instead of raising when imports or data are missing.

## 6) Troubleshooting snapshot
- Imports wrong? Re-run preflight; confirm `modules.blackapple`, `modules.aux_loaders`, `utils.path_handler`, and `alpha_analytical.stable` resolve inside the repo.
- Aux data missing? Check `data/cleaned/draws` inventory, rerun the Control Center draws refresh with the delete toggle, then `validate_aux_all.ps1`.
- App boot issues? Launch via `run_app.bat`, set `STREAMLIT_BROWSER=none` for headless, log to `.codex/first_boot.log`, then inspect the tail.

## 7) Handoff and human instructions
- When starting a Codex session, direct it to: read this file first, then follow the reading order in section 1.
- For deliveries: summarize changes in 5-8 bullets, include the changelog entry, list updated docs, mention validation commands and log locations, and call out risks or follow-ups.

Keep this Compass in sync whenever startup steps, guardrails, or documentation expectations evolve. Log those updates in the Unified Changelog so readers know the onboarding flow is current.
