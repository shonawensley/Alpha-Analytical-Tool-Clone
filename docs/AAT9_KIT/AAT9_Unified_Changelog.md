## 2025-09-28 - Aux - Positional loader hardening, pairs window SSOT, UI polish
- Impact: Restored dynamic loader registration for staged modules (positional tracker), unified overdue pairs on a 360-draw window, refreshed tracker/cross-variant/shortlist styling, and renamed tags to XVAR-Cons / Mirror-Echo / Double-Pressure for clarity. Added the loader smoke to preflight docs.
- Files: `src/app.py`, `modules/module_d_auxiliary_tools/refactored/positional_tool.py`, `scripts/checks/smoke_project_loader.py`, `docs/AAT9_KIT/AAT9_Preflight_Reference.md`, `docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md`.

## 2025-09-26 – Aux – Positional tracker UI pass – Side-by-side variant table
- Impact: Positional Pressure expander now renders Combined / Midday / Evening simultaneously (P1–P3 columns, top-3 ranks) using a fixed 360-draw window, replacing per-variant tabs/sliders while retaining consensus notes and the ranked shortlist.
- Files: src/app.py, docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md, docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md, docs/AAT9_KIT/important/AAT9_Positional_Pressure.md, docs/AAT9_KIT/important/DETAIL CODEX LOG.txt.

## 2025-09-25 — Aux — Pairs window alignment
- Overdue pair logic now scans the most-recent 360 draws so RED (≥107) / BLUE (≥71) thresholds register correctly across boxed permutations.
- `get_vtrac_statuses` and Control Center caching reuse the same window for pair colors/top-4 doubles while preserving existing combo/double pipelines.
- Files: `scripts/auxiliary/working/modules/analyze_pairs.py`, `src/app.py`.

## 2025-09-25 — Control Center — Due Doubles table
- Added a new "Due Doubles — Top Pairs with RED/BLUE Combo Misses" table to Control Center.
- Reads only `data/cleaned/*_draws.csv` via `modules.aux_loaders` (Combined/Midday/Evening).
- Ranks Combined top-4 repeating pairs (100-draw logic) and, per pair, lists double combos meeting:
  - RED ≥ 1000 draws since (highest), BLUE ≥ 667. Tokens preserve color and show C/M/E badges.
- Minimal, isolated edit in `src/app.py`; caching reused from existing variant draws block; soft-fails with captions.
- No changes to combined string-table pipelines or legacy readers.
# AAT9 — Unified Changelog

## 2025-09-24 - Aux - Positional pressure tool + Control Center heat - Draws-only positional indicators across variants
- Impact: Aux page gains positional pressure panel with consensus/shortlist; Control Center shows positional heat badges; docs updated.
- Files: `src/app.py`, `modules/module_d_auxiliary_tools/refactored/positional_tool.py`, `scripts/checks/smoke_positional.py`, `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`, `docs/AAT9_KIT/AAT9_Workflow_Standard.md`, `docs/AAT9_KIT/important/AAT9_Positional_Pressure.md`, `docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md`, `docs/AAT9_DOCS/AAT9_Blackapple_Module.md`, `docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md`

## 2025-09-22 - Aux - Combined/Midday/Evening variant support - Cross-variant doubles and BA views
- Impact: Control Center doubles tracker and Blackapple table surface Combined/Midday/Evening rows; Aux page lets you rerun working analysis per variant (purple bands suppressed for Midday/Evening).
- Files: `src/app.py`, `modules/aux_loaders.py`, `docs/AAT9_DOCS/Aux_Variants_Addendum.md`, `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`, `docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md`, `docs/AAT9_DOCS/AAT9_Blackapple_Module.md`

Conventions: YYYY‑MM‑DD — Category — Summary — Impact — Files/Refs
## 2025-09-17 — Aux — Draw pipeline restructure + archive legacy — Cleaner pipeline + clearer tooling
- Impact: Combined Aux features stay pinned to `<State>_draws.csv`; Midday/Evening exports live under `data/cleaned/draws/`; legacy Aux packages/scripts archived for reference.
- Files: `modules/aux_loaders.py`, `modules/module_d_auxiliary_tools/refactored/{extractor.py,README.md}`, `scripts/auxiliary/generate_draws_csv.py`, `src/app.py`, `archived/2025-09-17_aux_legacy/README.md`
- Notes:
  - Control Center → “Aux Draws Pipeline” regenerates combined by default and shows destination filenames.
  - CLI helper mirrors the same behaviour (`py -3 scripts/auxiliary/generate_draws_csv.py ...`).
  - Archived trees: `modules/module_d_auxiliary_tools/{adapters_old_module,legacy_2}` + legacy scripts under `archived/2025-09-17_aux_legacy/`.


## 2025‑09‑06 — Cleanup — Archive legacy launchers/entrypoints — Safer surface
- Impact: No runtime changes; older scripts moved under `archived/2025-09-06/` with manifest
- Files: `archived/2025-09-06/ARCHIVE_MANIFEST.md`
- Note: `run_app.bat` + `src/app.py` remain canonical

## 2025‑09‑06 — Tooling — Added preflight script — Faster path/import triage
- File: `.codex/preflight.ps1`
- Use: `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`

## 2025‑09‑06 — Docs — Architecture & App Flow Addendum — Canonical setup
- Files: `docs/AAT9_DOCS/AAT9_Architecture_Dir_Layout_2025-09-06.md`, `docs/AAT9_DOCS/AAT9_App_Flow_Addendum_2025-09-06.md`
- Includes: directory tree, data contracts, Mermaid diagram, guardrails

## 2025‑09‑06 — Hygiene — Forwarder for legacy path handler — Single source of truth
- File: `src/utils/path_handler.py` → re‑exports `utils.path_handler`
- Advantage: avoids duplicate logic/signature drift

## 2025‑09‑06 — Docs — KIT created — Curated entrypoint for AAT9
- Folder: `docs/AAT9_KIT/*`
- Includes: KIT README, Quickstart, AI Guide, Preflight Ref, Unified Changelog, Diagrams Guide

## 2025‑09‑06 — Pipeline — Tables pipeline runner + Control Center UI (optional)
- Files: `src/core/pipeline_runner.py`; `src/app.py` (Control Center expander)
- Adds: Upload Pick3StatsC4.xlsm and “Generate Tables” (clean → extract → generate)
- Writes: `data/cleaned/<State>_cleaned.xlsx`; `data/outputs/tables/<STATE>/..._combined.csv`
- Safe: path_handler SSOT; no auto‑run; soft‑fail captions; pages keep reusing outputs

## 2025‑09‑07 — Imports — SSOT bootstrap for canonical utils
- Files: `src/app.py`
- Fix: Enforce top‑level `utils` package binding early to prevent `src\utils` shadowing
- Why: Streamlit/sys.path order could resolve `utils` to `src\utils`, causing `ImportError/NameError`
- Safe: small, surgical import bootstrap; no behavior change to pages

## 2025‑09‑07 — Aux — Pairs display bands & captions
- Files: `src/app.py` (Aux page)
- Change: Mutually‑exclusive bands (red highest) for repeating/non‑repeating; Top‑5 repeating coloring aligned; thresholds caption uses ASCII ">="
- Why: Old labels used overlapping checks (red ≥ 71 and blue ≥ 107) causing confusion; this is display‑only; calculations unchanged

## 2025‑09‑07 — V‑Trac — Big table badges
- Files: `src/app.py` (Aux page)
- Change: Red Top‑10 overdue rows show badge with "rank (draws_since)"; preserves green (recent)
- Why: Align big table with the small “Index Hits” table; display‑only

## 2025‑09‑07 — Digit Reduction — Stacked report + training exports
- Files: `src/core/module_b_digit_reduction.py` (orchestrator), `src/app.py` (page wiring)
- Adds: Stacked HTML report embed checkbox; training CSV/JSON with structural fields and export compaction (analysis unchanged)
- Outputs: `data/outputs/analysis/digit_reduction/<STATE>/{...report.html, ...report_stacked.html, ...scores.csv}`;
  `training/{...steps.csv, ...logs.json}` with guidance and schema

## 2025‑09‑07 — Winners — V‑Trac winner report (index panels)
- Files: `src/core/winners_vtrac_report.py`, `src/app.py` (Control Center expander)
- Adds: single‑state, per‑winner HTML export showing Midday/Evening/Combined index panels
  - Purple = index stable‑pattern combos; Green = straight permutations of the winning number
- Writes: `data/outputs/winners/<YYYY‑MM‑DD>/vtrac_reports/<STATE>/<STATE>_vtrac<index>_winner_<timestamp>.html`
- Notes: table‑agnostic (safe for states missing string‑tables); later can overlay table‑driven details
2025-09-16 — Winners — Analyzer-style Winners Full report + Aux restore — Adds table-aware 3‑pane HTML (purple index + green straights), restores staged Aux V‑TRAC reference, adds canonical vtrac_reference API; Files: modules/vtrac_reference.py, modules/winner_report_full.py, src/reporting (added via modules shim), src/app.py (full tile wiring); Refs: AAT9_Winners_VTrac_Report.md, AAT9_Live_Wiring_and_Data_Paths.md, AAT9_Checkpoint_Log.md, briefings/PITFALLS.txt

## 2025-09-19 � Cleanup � Archived legacy Stable Pattern scripts/run artifacts � Reduced confusion; canonical extractor unchanged � Files: archived/2025-09-19_stable_cleanup/*; Refs: docs/AAT9_KIT/important/stable_pattern_AAT9.txt
## 2025-09-19 � Stable � Modal straight scoring + families/spotlight exports � Richer signals; winner reports get dedicated CSVs � Files: alpha_analytical/stable/__init__.py, feature_config.yml, post_pass_families.py, winner_family_spotlight.py, src/core/stable_pattern_extractor.py, src/app.py; Refs: docs/AAT9_KIT/important/stable_pattern_AAT9.txt

## 2025-09-21 - Aux - Restored staged VTRAC reference & smoke check - Aux page stable again
- Files: `src/app.py`, `scripts/auxiliary/working/modules/{analyze_pairs.py,run_process.py}`, `modules/module_d_auxiliary_tools/refactored/{bootstrap_imports.py,boxed_vtrac.py,indicators.py}`, `scripts/checks/smoke_aux_vtrac.py`
- Notes: hardened Aux staging context, restored legacy boxed reference loader, added smoke script and documentation manifest.

