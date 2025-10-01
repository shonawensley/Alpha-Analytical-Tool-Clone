## 2025-10-01 04:15 (UTC) - V-TRAC tables & cache alignment

- Context: Legacy mini-pipeline inside the V-TRAC page was desyncing from the global tables pipeline, leading to "analysis completed" but missing tables for states like Delaware4.
- Change:
  - Removed the in-page Process/Clean/Extract/Generate controls so the analyzer only consumes pipeline tables.
  - Added preflight/status rows, system-health details, and a cache reset button on the V-TRAC tab.
  - Loader now tolerates slug variants and lists the actual `_combined` files before running.
- Impact: The V-TRAC Analyzer now reads the canonical combined tables, exposes diagnostics when files are missing, and no longer masks stale results.
- Files/Refs: `src/app.py`, `src/core/module_c_vtrac.py`.
- Follow-ups: Consider wiring winners logging to the consolidated bundle once other tools align.

## 2025-10-01 03:45 (UTC) - Digit Reduction training/analyzer alignment

- Context: New Pick3StatsC4 run exposed missing training logs and analyzer crashes on empty strings, plus the occasional Streamlit blank screen warning.
- Change:
  - Reducer now always writes `digit_reduction/<STATE>/training/<STATE>_digit_reduction_log.json` (legacy plural file cleaned up).
  - Analyzer tolerates blank/whitespace numeric fields and reuses the newest training log automatically.
  - Digit Reduction UI shows preflight status, folder shortcuts, disables Analyzer until training JSON exists, and wraps the dev overlay import/rescue boot.
- Impact: Fresh pipeline runs for any state immediately produce the training JSON, Analyzer V2 no longer fails on empty ints, and the tab guides operators instead of blank-screening.
- Files/Refs: `src/app.py`, `src/core/module_b_digit_reduction.py`, `alpha_analytical/digit_reduction/analyzer_v2/{io.py,pipeline.py}`.
- Follow-ups: Monitor first full-state run; expand preflight to include slate artifacts if helpful.

## 2025-09-30 03:30 (UTC) - Control Center due doubles badges

- Context: Operators needed the reinstated due-doubles columns to carry the top repeating pairs and cross-variant combo badges without the extra Latest/Total clutter.
- Change:
  - Load combined repeating pairs from Aux analytics and attach them to every state/variant row.
  - Scan Combined/Midday/Evening draws for >=1000-draw doubles, merge their C/M/E badges per pair, and render compact hyphen lists.
  - Renamed the primary metric to 'Draws Since Double' and removed legacy columns while keeping positional heat/notes untouched.
- Impact: Due doubles view once again highlights the same critical combos surfaced in Aux, with consistent badges and without wasting table real estate.
- Files/Refs: `src/app.py`, `tasks/task_doublescontrol.txt`, docs/AAT9_KIT/AAT9_Unified_Changelog.md.
- Follow-ups: Consider surfacing BLUE (>=700) combos in a hover/supplement once we validate the red baseline.

﻿## 2025-09-29 23:30 (UTC) - Aux unified view (DEV) + due doubles columns

- Context: After restoring the Control Center due-doubles columns, we needed a safer way to inspect Combined/Midday/Evening Aux outputs together without refactoring the legacy radio flow.
- Change:
  - Reused the cached Aux payloads to rebuild the due doubles table (pairs + RED combos) on Control Center.
  - Added a DEV-only “Unified Aux View” expander that renders top pairs/combos/V-TRAC summaries in side-by-side columns while keeping the original per-variant layout intact.
- Impact: Operators can keep the familiar workflow but optionally scan all variants together; Control Center regains the columns operators rely on for doubles monitoring.
- Files/Refs: `src/app.py`, docs/AAT9_KIT/AAT9_Unified_Changelog.md.
- Follow-ups: Consider expanding the unified expander with sums/BA once we vet the current summaries.
## 2025-09-28 02:00 (UTC) - Positional loader guardrails + pairs window SSOT

- Context: Post-mojibake cleanup left the positional tracker dependent on a non-registered loader module and pairs capped at 100 draws, muting RED/BLUE thresholds.
- Change:
  - Restored `_load_project_module` registration (sys.modules) and added a dedicated loader smoke; variant fallback now always resolves Combined/Midday/Evening draws with source captions.
  - Standardised overdue pair analysis on a 360-draw window (`PAIRS_ANALYSIS_WINDOW`), refreshed the Overdue Pairs caption, and polished positional summary/shortlist styling with XVAR-Cons / Mirror-Echo / Double-Pressure tags.
- Impact: Positional tracker loads reliably from staged modules, pair colours fire at documented thresholds, and operators can read cross-variant cues without tag ambiguity.
- Files/Refs: `src/app.py`, `modules/module_d_auxiliary_tools/refactored/positional_tool.py`, `scripts/checks/smoke_project_loader.py`, `docs/AAT9_KIT/AAT9_Preflight_Reference.md`, `docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md`.
- Follow-ups: Consider tagging this baseline (AAT9_Aux_Positional_GOLD) and wiring positional hits into Winners logging.

## 2025-09-26 06:00 (UTC) - Positional tracker UI consolidation

- Context: Operators requested the Aux tracker mirror the training markup (Combined/Midday/Evening stacked) without extra sliders or tabs.
- Change:
  - Locked the positional engine to a 360-draw window with Top-3 ranks and removed the Streamlit slider/radio controls.
  - Replaced per-variant tabs with a side-by-side table (P1â€“P3 columns per variant) while keeping draw-source captions, consensus notes, and the shortlist.
  - Updated Quickstart, Aux overview, positional pressure brief, and detail log to describe the new layout.
- Impact: Positional pressure is now scannable across variants at a glance, matching the documented mock and ready for downstream compound scoring.
- Files/Refs: src/app.py, docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md, docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md, docs/AAT9_KIT/important/AAT9_Positional_Pressure.md, docs/AAT9_KIT/important/DETAIL CODEX LOG.txt.
- Follow-ups: Consider aligning other Aux tables into variant columns and logging positional hits in the winners pipeline.

## 2025-09-24 05:00 (UTC) - Positional pressure tool + Control Center heat

- Context: Aux needed an in-app positional tracker (Combined/Midday/Evening) that stays draws-only and compounds with existing doubles/BA cues.
- Change:
  - Added `modules/module_d_auxiliary_tools/refactored/positional_tool.py` with configurable scoring (rank, lag, mirror, consensus, double pressure).
  - Wired Aux page expander with window/top-k controls, consensus notes, positional shortlist, and explicit draw source captions.
  - Extended Control Center doubles/BA table with a positional heat badge per state/variant using the same engine.
  - Published smoke script and refreshed KIT/Aux docs with usage guidance.
- Impact: Operators can read per-position pressure alongside existing Aux/BA signals without touching combined-table pipelines.
- Files/Refs: `src/app.py`, `modules/module_d_auxiliary_tools/refactored/positional_tool.py`, `scripts/checks/smoke_positional.py`, `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`, `docs/AAT9_KIT/AAT9_Workflow_Standard.md`, `docs/AAT9_KIT/important/AAT9_Positional_Pressure.md`, `docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md`, `docs/AAT9_DOCS/AAT9_Blackapple_Module.md`, `docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md`.
- Follow-ups: Monitor scoring weights (mirror/consensus boosts) and consider optional logging to Winners pipeline.

## 2025-09-22 04:30 (UTC) - Aux variants + Control Center expansion

- Context: Preparing for Midday/Evening tooling required exposing those draw files without disturbing the combined baseline.
- Change:
  - Extended `modules.aux_loaders.load_state_draws` with an explicit variant selector and tolerant staged fallback.
  - Control Center doubles tracker + Blackapple now iterate Combined/Midday/Evening (variant-aware DataFrame, dev captions).
  - Aux page adds a variant selector (Combined default) that reuses the working analysis; purple pair band is suppressed for Midday/Evening while BA consumes variant-specific draws.
  - Documented the contract (`docs/AAT9_DOCS/Aux_Variants_Addendum.md`) and refreshed KIT/Blackapple docs to mention variants.
- Impact: Combined behaviour stays identical; operators can inspect Midday/Evening draws/alerts directly in both Control Center and Aux without manual file swaps.
- Files/Refs: `src/app.py`, `modules/aux_loaders.py`, `docs/AAT9_DOCS/Aux_Variants_Addendum.md`, `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`, `docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md`, `docs/AAT9_DOCS/AAT9_Blackapple_Module.md`.
- Follow-ups: Optional UI polish (side-by-side columns for variants), consider surfacing missing variant files in Control Center Dev Health.
## 2025-09-21 02:00 (UTC) - Aux staging restore

- Context: Aux began failing after the Sept-16 cleanup because the rich boxed VTRAC reference (legacy) was archived. Lazily imported modules fell back to the slim canonical API, so Aux lost `BOXED_LABEL_LOOKUP` and returned empty tables.
- Change:
  - Hardened `_aux_working_first()` (stages working modules for full run; restores sys.path and prior bindings).
  - Converted staged imports to relative (`scripts/auxiliary/working/modules/*`).
  - Updated refactored bootstrap to locate legacy assets and register them before loading Aux helpers.
  - Removed ad-hoc sys.path tweaks in refactored helpers; added smoke script `scripts/checks/smoke_aux_vtrac.py`.
  - Added Aux staging manifest + doc hooks (Quickstart, Live Wiring, Pitfalls).
- Rationale: Keep Aux draws-only flow stable while maintaining the canonical VTRAC API for Winners and other pages.
- Impact: Aux runs again (boxed VTRAC grid + overdue panels), Dev Health shows staged bindings, quick smoke script catches regressions.
- Files/Refs: src/app.py; scripts/auxiliary/working/modules/{analyze_pairs.py,run_process.py}; modules/module_d_auxiliary_tools/refactored/{bootstrap_imports.py,boxed_vtrac.py,indicators.py}; scripts/checks/smoke_aux_vtrac.py; docs/AAT9_DOCS/AAT9_Aux_Staging_Manifest.md; Quickstart/LW/Pitfalls updates.
- Follow-ups: Optional - remove duplicate legacy copies once archive-only loader is validated; consider compat shim so Aux can consume canonical API long-term.

## 2025-09-19 20:30 (UTC)  Stable Pattern Modal Scoring + Families

- Context: Needed richer Stable outputs (permutation density, family grouping, winner spotlights) to prep for training and operational use.
- Change:
  - Updated analyser to count permutation/repeat density, modal straights, debug columns, and consensus tails using digits-only logic.
  - Added post-pass family aggregator + YAML weights; winner spotlight CSVs generated when winners provided.
  - Extended Streamlit UI with winners input, family/spotlight download links, and dev health prints for engine/YAML.
- Rationale: Improves scoring fidelity and exposes structured outputs for downstream analysis without touching other tools.
- Impact: New CSVs under data/outputs/analysis/patterns/<STATE>/ (families + optional spotlight); Stable page now accepts winners list; Stable UI shows quick links + preview for the families frame.
- Files/Refs: alpha_analytical/stable/{__init__.py,feature_config.yml,post_pass_families.py,winner_family_spotlight.py}, alpha_analytical/vtrac/, src/core/stable_pattern_extractor.py, src/app.py, docs/AAT9_KIT/important/stable_pattern_AAT9.txt.
- Follow-ups: Consider cross-section/progression bonuses (post_pass_families) and unit tests for rep3 helper.
## 2025-09-19 01:05 (UTC)  Stable Pattern Archive Cleanup

- Context: Multiple legacy Stable Pattern runners/tests were still in the repo, creating confusion about which extractor feeds the integrated app.
- Change:
  - Archived root BATs, scripts/archive/* demos, scripts/utils_old/* helpers, historical `data/outputs/stable_patterns/`, and the legacy pytest into `archived/2025-09-19_stable_cleanup/` with a manifest.
  - Added Stable Dev Health details so the page prints engine + feature_config paths.
  - Updated KIT docs/changelog to reference the canonical chain and archive location.
- Rationale: Eliminates duplicate entry points while keeping references available; Dev Health now confirms bindings explicitly.
- Impact: No runtime change  Streamlit uses `src/core/stable_pattern_extractor.py` ? `alpha_analytical/stable/__init__.py`; legacy assets are preserved for reference.
- Files/Refs: archived/2025-09-19_stable_cleanup/*, src/app.py, docs/AAT9_KIT/important/stable_pattern_AAT9.txt, docs/AAT9_DOCS/stable_pattern_master_guide_AAT9.md, docs/AAT9_KIT/AAT9_Unified_Changelog.md.
- Follow-ups: None required; restore specific runners from archive only if a CLI is needed.
# AAT9 â€” Checkpoint Log (Running, Detailed Notes)

Purpose: A single, dateâ€‘tagged log for deeper explanations, context, and rationale that complement the Unified Changelog. Use this when you (or AI) want to capture more than a oneâ€‘line changelog entry.

How to update
- Append a new section at the top.
- Use the template below; keep entries concise but explanatory.
- Link to relevant files, PR notes, logs, and diagrams.

Template
```
## YYYYâ€‘MMâ€‘DD HH:MM (TZ) â€” Title

- Context: oneâ€‘paragraph background
- Change: what changed (bullets)
- Rationale: why this improves stability/clarity/UX
- Impact: runtime behavior, workflows, or docs affected
- Files/Refs: file paths, doc sections, diagrams
- Followâ€‘ups: next steps if any
```

---

## 2025â€‘09â€‘06 12:00 (UTC) â€” Preflight Tables Check + Startup Docs

- Context: We standardized AAT9 startup (KIT + preflight) and wanted a quick, optâ€‘in validation for combined tables when working on Stable/DR/Vâ€‘TRAC.
- Change:
  - Added `-CheckTables` to `.codex/preflight.ps1` to list `data/outputs/tables` state dirs and confirm a specific state dir exists.
  - Added `docs/AAT9_KIT/HUMAN_READ_FIRST_AAT9.md` with simple operator instructions.
  - Added Codex boot doc `briefings/CODEX_READ_FIRST_AAT9.md` and a clipboard helper `TOOLS/codex_start_aat9.bat`.
- Rationale: Keeps preflight fast by default; adds a quick onâ€‘demand tables sanity check; standardizes session startup for both humans and agents.
- Impact: No runtime changes; faster diagnosis when working on combinedâ€‘tables pages.
- Files/Refs:
  - `.codex/preflight.ps1` (new flags)
  - `docs/AAT9_KIT/HUMAN_READ_FIRST_AAT9.md`
  - `briefings/CODEX_READ_FIRST_AAT9.md`, `TOOLS/codex_start_aat9.bat`
  - KIT index: `docs/AAT9_KIT/AAT9_KIT_README.md`
- Followâ€‘ups: Consider Phaseâ€‘2 Aux audit after new Aux tools land.

## 2025â€‘09â€‘06 13:30 (UTC) â€” Tables Pipeline Runner + Control Center UI

- Context: Daily workflow uploads a fresh Pick3StatsC4.xlsm and regenerates combined tables; we needed a safe way to run this inâ€‘app when needed.
- Change:
  - Added `src/core/pipeline_runner.py` (pure functions) that cleans â†’ extracts â†’ builds combined tables.
  - Wired an optional â€œTables Pipelineâ€ expander in Control Center to upload Excel and run the pipeline.
- Rationale: Keep pipeline runnable from the app, but only on demand; reuse outputs across pages; no recompute on render.
- Impact: No changes to existing pages; optional UI only. Outputs stored under `data/cleaned` and `data/outputs/tables`.
- Files/Refs: `src/core/pipeline_runner.py`, `src/app.py` (Control Center section), `docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md`
- Followâ€‘ups: None required; Phaseâ€‘2 Aux audit deferred until after new Aux tools are added.

## 2025â€‘09â€‘07 10:10 (UTC) â€” Import Shadowing (utils) â†’ SSOT Bootstrap

- Context: Intermittent startup errors (`ImportError: cannot import name get_cleaned_data_dir` or `NameError: Path is not defined`) after adding optional pipeline UI. Data/layout were fine; errors stemmed from module resolution.
- Root Cause: Two packages named `utils` exist (`/utils` canonical, `/src/utils` legacy). When Streamlit sys.path had `src` before project root, absolute imports (`from utils.path_handler ...`) bound to `src\utils` first, triggering a circular forwarder and partial module.
- Fix: Add a small SSOT import bootstrap at the very top of `src/app.py`:
  - Insert project root at sys.path[0].
  - Evict premature `utils`/`src.utils` bindings if they resolve under `/src/utils`.
  - Import and pin `utils.path_handler` from the topâ€‘level package.
- Impact: Deterministic binding to canonical `utils`; no behavior changes to pages/pipeline.
- Files: `src/app.py`; docs updated: KEEPERS.md, Pitfalls.
- Followâ€‘ups: None â€” structural rename of `src/utils` not required now.

## 2025â€‘09â€‘07 12:20 (UTC) â€” Aux Pairs Bands (Displayâ€‘Only)

- Context: Overdue pairs lists used overlapping bands (e.g., repeating red â‰¥ 71 and blue â‰¥ 107), causing label confusion. Policy: red is the highest threshold.
- Change: Mutuallyâ€‘exclusive bands (displayâ€‘only) with red highest:
  - Repeating: red â‰¥ 107; blue 71..106; purple 25..70
  - Nonâ€‘repeating: red â‰¥ 56; blue 37..55; purple 25..36
- Caption updated to ASCII ">=" to avoid mojibake. Topâ€‘5 repeating color mapping aligned; list still sorted by draws_since.
- Impact: No calculation changes; UI buckets and captions now match policy.

## 2025â€‘09â€‘07 12:40 (UTC) â€” Vâ€‘Trac Big Table: Badge Shows Drawsâ€‘Since

- Context: Small â€œIndex Hitsâ€ shows draws_since; big table should show it too for Topâ€‘10 red rows.
- Change: Red rows now use badge "rank (draws_since)"; green rows unchanged.
- Impact: Displayâ€‘only; keeps small/big table alignment.

## 2025â€‘09â€‘07 13:00 (UTC) â€” Digit Reduction: Stacked Report + Training Exports

- Context: Need trainingâ€‘friendly exports and stacked view for better screenshots; analysis unchanged.
- Change:
  - Added stacked report HTML and checkbox in page to embed it.
  - Added training CSV/JSON exports under `.../training/` with structural fields, ranks, guidance, and exportâ€‘only compaction.
- Outputs:
  - `data/outputs/analysis/digit_reduction/<STATE>/<STATE>digit_reduction_report.html`
  - `.../<STATE>digit_reduction_report_stacked.html`
  - `.../<STATE>digit_reduction_scores.csv`
  - `.../training/<STATE>digit_reduction_steps.csv`
  - `.../training/<STATE>digit_reduction_logs.json`
- Impact: No changes to reduction algorithms or tabbed HTML; only exports and optional embed.

## 2025â€‘09â€‘07 14:10 (UTC) â€” Winners Logger: Vâ€‘Trac Winner Report (Index Panels)

- Context: Need a perâ€‘state, perâ€‘winner visual export for external training; older runs had correct â€œvtrac_reportsâ€ HTML under winners.
- Change: Added an indexâ€‘based report generator and UI expander in Control Center:
  - Inputs: State, 3â€‘digit winner
  - Renders 3 panels (Midday/Evening/Combined) with:
    - Purple: stableâ€‘pattern combos for the winnerâ€™s index
    - Green: straight permutations of the winner
  - Writes to: `data/outputs/winners/<YYYYâ€‘MMâ€‘DD>/vtrac_reports/<STATE>/<STATE>_vtrac<index>_winner_<timestamp>.html`
- Impact: Does not require stringâ€‘tables; safe for states whose tables arenâ€™t mapped yet. Later we can overlay tableâ€‘driven details.
- Files: `src/core/winners_vtrac_report.py`, `src/app.py`
## 2025-09-16 16:00 (UTC) â€” Winners Full Report + Aux Vâ€‘TRAC Restore

- Context: The Aux tools rely on a staged Vâ€‘TRAC reference under `scripts/auxiliary/working/modules/` while the integrated app should use a canonical `modules/*`. A deleted staged `vtrac_reference.py` broke Aux; the Winners Logger (full) also failed due to imports resolving to the staged package and a missing canonical API. Goal: restore Aux, add a canonical Vâ€‘TRAC API, and enable a tableâ€‘aware analyzerâ€‘style Winners Full report (3 panes, purple index + green straights) without touching analyzer internals.
- Change:
  - Restored staged Aux reference: `scripts/auxiliary/working/modules/vtrac_reference.py` (exports restored; drawsâ€‘only Aux unaffected).
  - Added canonical API: `modules/vtrac_reference.py` exporting `get_vtrac_index`, `get_index_set`, `get_index_straights` (backed by analyzer utilities).
  - Implemented full builder: `modules/winner_report_full.py` (reads three combined tables, renders analyzerâ€‘style 3â€‘pane HTML via analyzer renderer, applies green straights overlay, writes to `data/outputs/analysis/winners/<STATE>/...`).
  - Wired Control Center tile: â€œWinners Logger (Analyzerâ€‘style full report)â€ now accepts Midday/Evening and generates one HTML per input; compact tile unchanged.
  - Import hygiene: ensured nonâ€‘Aux pages bind `modules/*` to the project tree, not the staged Aux path; added a robust import fallback in the full tile.
- Rationale: Cleanly separates Aux (staged) from the integrated app (canonical), removes import collisions, and reuses the established pipeline tables to produce the expected analyzerâ€‘style Winners view. The canonical API gives nonâ€‘Aux code a single, stable entrypoint, reducing drift.
- Impact:
  - Aux tools: working again; no change to drawsâ€‘only behavior.
  - Winners Full tile: produces analyzerâ€‘style HTML under `data/outputs/analysis/winners/<STATE>/...` with purple index coverage + green straights overlay; compact tile remains as a safe fallback when tables are missing.
  - No changes to analyzer internals or other tools; stringâ€‘safe CSV reads for new reporting prevent token coercion.
- Files/Refs:
  - Code: `modules/vtrac_reference.py`, `modules/winner_report_full.py`, `src/app.py` (full tile wiring), staged `scripts/auxiliary/working/modules/vtrac_reference.py` (restored)
  - Docs: `docs/AAT9_KIT/AAT9_Winners_VTrac_Report.md` (usage/paths), `docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md` (I/O mapping), `briefings/PITFALLS.txt` (import SSOT + stringâ€‘safe IO), `docs/AAT9_KIT/AAT9_Preflight_Reference.md` (tip for tables)
- Followâ€‘ups:
  - Optional: unify all tools on `modules/vtrac_reference.py` over time; keep Aux staged shim as a reâ€‘export when youâ€™re ready to retire duplicates.
  - Optional: move full report renderer to `src/reporting/` with a template; todayâ€™s builder already mirrors analyzer layout.
  - Add a tiny smoke CLI to generate a winners full report outside Streamlit if desired.

## 2025-09-17 21:00 (UTC) â€” Aux Draws Pipeline + Legacy Archive

- Context: Combined Aux features relied on historical folders (`adapters_old_module`, `legacy_2`, assorted scripts) and drew from `data/cleaned/*_draws.csv`. We now have a canonical extractor + Control Center exporter, so clutter was causing confusion and file-lock issues when rebuilding Midday/Evening draws.
- Change:
  - Added `scripts/auxiliary/generate_draws_csv.py` and Control Center "Aux Draws Pipeline" expander. Both write Combined/Midday/Evening CSVs to `data/cleaned/draws/` (combined enabled by default).
  - Loader (`modules/aux_loaders.load_state_draws`) prefers `data/cleaned/draws/` with fallback to legacy location so existing Aux/BA logic stays on combined.
  - Archived unused Aux packages (`modules/module_d_auxiliary_tools/{adapters_old_module,legacy_2}`) and legacy helper scripts under `archived/2025-09-17_aux_legacy/` with a README.
  - Documented the refactored surface in `modules/module_d_auxiliary_tools/refactored/README.md`.
- Impact:
  - Daily flow: run tables pipeline (if needed) then run Aux Draws Pipeline to refresh combined + Midday/Evening files.
  - Combined Aux features remain untouched; Midday/Evening ready for future wiring.
  - Less risk of grabbing stale modules; clearer directory layout for new contributors.
- Follow-ups:
  - Remove the leftover `data/cleaned/Connecticut_Midday_draws.csv` once Excel releases the file lock.
  - When ready, wire Midday/Evening into Control Center doubles + Blackapple (combined stays the baseline).
  - Consider retiring `scripts/auxiliary/working/` once staged modules are no longer needed by the Aux page.




## 2025-10-01 23:30 (UTC) - V-TRAC ASCII cleanup
- Context: Streamlit surfaced the Mojibake guard after piping new tables; inspection showed the V-TRAC analyzer UI still rendered emoji arrows and en dashes.
- Change: Replaced the non-ASCII glyphs in `src/core/module_c_vtrac.py` and `src/core/module_b_digit_reduction.py` with bracketed ASCII markers so the guard stays silent while keeping the preflight readability.
- Impact: Digit Reduction and V-TRAC pages now load without Mojibake warnings after a fresh pipeline run.


