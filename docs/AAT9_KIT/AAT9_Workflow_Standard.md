# AAT9 — Workflow Standard (Agents & Devs)

Purpose: A clear, repeatable process for implementing changes safely, updating docs/diagrams consistently, and logging updates in one place.

## 0) Read‑First (once per session)
- KIT README: `docs/AAT9_KIT/AAT9_KIT_README.md`
- Architecture & Dir Layout: `docs/AAT9_DOCS/AAT9_Architecture_Dir_Layout_2025-09-06.md`
- Quickstart Cheat Sheet: `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`
- Preflight Reference: `docs/AAT9_KIT/AAT9_Preflight_Reference.md`

## 1) Preflight & Sanity
- Run: `powershell -NoProfile -File .codex/preflight.ps1 -State "<State>"`
- Confirm in‑repo imports and draws CSV inventory.
- If anything looks off, fix environment/paths before coding.

## 2) Plan (small, explicit)
- State the exact files to change and why.
- Keep diffs minimal; avoid refactors unless explicitly requested.
- For cleanup, prefer archive‑first moves with a manifest; no deletions.

## 3) Implement (path‑safe)
- Use `utils.path_handler` for all outputs.
- Aux/BA read only `data/cleaned/draws/*_draws.csv`; other tools read combined tables via helpers.
- Positional Pressure lives under `modules/module_d_auxiliary_tools/refactored/positional_tool.py`; keep it draws-only and isolated from combined-table pipelines.
- Pure functions; avoid `os.chdir`; use `pathlib.Path` joins.
- UI: soft‑fail (captions/warnings) instead of raising.

## 4) Verify
- Compile: `python -m py_compile` on changed files.
- Import probes for key modules (show `__file__`).
- Smoke: `python scripts/checks/smoke_positional.py` when positional wiring changes.
- Auxiliary guardrail: `powershell -NoProfile -File scripts/tools/validate_aux_all.ps1` after draw refreshes or Aux wiring changes; it fails fast if the canonical loader drifts.
- Commits run the Aux pre-commit guard (`python scripts/hooks/validate_aux_draws.py`). Only bypass with `AAT9_SKIP_AUX_GUARD=1` in rare emergencies.
- Optional: headless boot with log → `.codex/first_boot.log`.

## 5) Update Documentation (always)
- Unified Changelog: `docs/AAT9_KIT/AAT9_Unified_Changelog.md`
  - Entry format: `YYYY‑MM‑DD — Category — Summary — Impact — Files/Refs`
- Checkpoint Log (detailed notes): `docs/AAT9_KIT/AAT9_Checkpoint_Log.md`
  - One short section per change with context, rationale, links
- Stable reverse-engineering: append each analysis run (winner overlay + insights) to `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md` so future sessions can resume from the same evidence.
- Affected docs by change type:
  - Structure/paths: update Architecture & Dir Layout; add/adjust Mermaid diagram.
  - Page wiring/data contracts: update App Flow Addendum; note page names and inputs/outputs.
  - New tool/module: add a short “Data Contracts & Where It Lives” block in a relevant doc; link from KIT README.
  - Preflight behavior: update Preflight Reference with example output.
  - Diagrams: follow AAT9_Diagrams_Guide; embed Mermaid blocks in the doc itself.

## 6) Handoff / PR Notes
- Summarize what changed in 5–8 bullets.
- Paste the Changelog entry.
- Include links to updated docs/sections and screenshots/log tails when relevant.

## 7) Templates (copy‑paste)
- Changelog entry:
  - `YYYY‑MM‑DD — <Category> — <Summary> — <Impact> — Files: <paths>; Refs: <docs/sections>`
- Commit/Delivery notes:
  - Goal
  - Files touched
  - Validation (compile/import/smoke)
  - Docs updated (links)
  - Risks/Follow‑ups

## 9) Trigger Phrase
- “document and process” → Agents execute the Post-Implementation Checklist and return a concise report with links.

## 10) Example-Driven Optimisation Loop
- Run the tool on the chosen state(s) with training thresholds (e.g., `min_occ=1`, `min_score_to_highlight=7`) and save all artefacts to `artifacts/`.
- Drop the three Combined/Midday/Evening input CSVs alongside the outputs so follow-up analysis can replay the exact run.
- Log key observations in `docs/AAT9_KIT/AAT9_Analysis_Insights.md` (winners, section_count, progression, noteworthy features).
- File the smallest follow-up tasks (feature additions, weight tweaks) with explicit file lists.
- Add a regression test or hook entry for every new feature so the next batch run “just works.”
- Repeat until the checklist for the tool is complete; only then tune winner-specific heuristics.

## 8) Golden Rules (AAT9)
- Run from repo root; never rely on `C:\Windows\System32` defaults.
- Never change remotes or repo config.
- Keep BA draws-only; don’t mix combined string-tables with Aux/BA.
- Keep changes reversible and documented.

### Dev Health (quick checks in UI)
- Control Center: shows bindings for utils.path_handler, modules.vtrac_reference, modules.winner_report_full, modules.blackapple, modules.aux_loaders, core.pipeline_runner, and tables root inventory.
- Winners Full tile: shows actual modules binding, modules.vtrac_reference path, builder presence, and per-state combined tables existence.
- V-TRAC Analyzer + Stable pages: show module bindings and tables roots for their flows.
- Control Center batch winners expander now runs winners logging, Stable bundles, and the Digit Reduction pipeline (reducer/analyzer/overlay with optional bundle) from the same pasted sheet; set the bundle stamp before enabling either bundle toggle.
