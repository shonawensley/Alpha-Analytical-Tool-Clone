## 2025-11-02 04:55 (UTC) - Digit Reduction Analyzer V2 consolidation

- Context: Digit Reduction still used the pre-DIGIT06 scaffolding (Part-1/Part-2 split, winner overlays bolted on) and couldn't capture extended cluster/density logic documented in the optimization packets.
- Change:
  - Rebuilt `analyzer_v2` around cluster-aware feature extraction (`clustering.py`, new `features.py`), config-driven scoring, and an additive pipeline with overlay hooks.
  - Added `config.yml` spec lock + doc (`docs/DR_OPT_SPEC_LOCK.md`), new writers, and overlay helper that can batch winner flags when requested.
  - Landed regression tests for drop metadata, aggregation metrics, and scoring shape; refreshed `test_digit_reduction_overlay.py` to the new score interface.
- Impact:
  - Per-item CSV now includes earliest/persistence for the six detection classes, family density, drop metadata, cross-column/variant/method echoes, and reproducibility metadata (config hash + git SHA).
  - Scoring is fully determined by `config.yml`; weights/gates can be tuned without editing code. Overlay generation is optional and no longer coupled to stale artifacts.
  - Future work (weight tuning, UI surfacing) can iterate on config/tests without touching reducers.
- Next:
  - Run the analyzer on a few real states, tune weights via config, and log findings / follow-ups in `AAT9_Analysis_Insights.md`.
  - Wire the Control Center panel to surface the new columns once we validate scores IRL.

## 2025-10-26 06:10 (UTC) - V-TRAC scoring/export config + bundle helper

- Context: After the parity sweeps we needed a repeatable way to turn validator outputs into a compact, shareable scorecard with explainability so ChatGPT Pro / agents can analyze runs without unzipping bundles.
- Change:
  - Rebuilt `TOOLS/vtrac_score_and_export.py` with argparse/logging, hardened parsing, union-based token echoes/ledger, and config overrides (`configs/vtrac_score_config.json`).
  - Updated `TOOLS/run_vtrac_share_bundle.py` to call the scorer (using the config) after `make_pro_payload.py`, keeping summaries, compact report, and optional ZIP in sync.
  - Dropped breadcrumbs across docs/tasks (`Analysis_Insights`, `Data_Validation_Workflow`, `VALIDATE_C`, `VTRAC_ENHANCMENTS`) and added unit coverage (`tests/test_vtrac_score_export.py`).
- Impact:
  - One command (`python TOOLS/run_vtrac_share_bundle.py`) now refreshes `summary.*`, `vtrac_compact_report.*`, and the optional ZIP, ready for GitHub raw links.
  - Compact report rows expose `section_prior`, `state_prior`, and a `why` string so reviewers can understand score contributions instantly.
  - Config file lets us adjust weights/priors per sweep without touching code.
- Next:
  - Run broader validation batches, inspect the compact CSV versus Winners HTML, and log findings in `AAT9_Analysis_Insights.md`.
  - Pull the compact report into the cross-tool aggregator once each analyzer has equivalent hand-offs.

## 2025-10-18 03:30 (UTC) - Validation workflow & data hand-off playbook

- Context: After landing the validator/batch tooling we needed a single reference covering how to run the enhanced analyzer sweep, where artifacts live, and how to share them with ChatGPT Pro / human reviewers.
- Change:
  - Authored `docs/AAT9_KIT/AAT9_Data_Validation_Workflow.md` (generate bundles, run validator, produce matrix/findings, share via push/zip/targeted upload).
  - Logged sharing considerations and aggregator outlook in `AAT9_Analysis_Insights.md`.
  - Cleaned `AAT9_Unified_Changelog.md` entry describing the validator regression work.
- Impact:
  - Every state run now leaves behind predictable evidence (`validation_report.{md,json}`, matrix.csv, findings.md) ready for analysts or assistants.
  - Documented workflow lets future sessions (Codex, human, or agent) jump straight into analysis without re-deriving the process.
  - Reinforces rule-based tuning today while leaving hooks for ML later once we have richer validation history.
- Next:
  - Commit/push summaries before handing them to ChatGPT Pro to avoid upload limits.
  - Extend validator parsing if we want to compare Winners legend markers (vt-straight/family gap) in addition to the table metrics.

## 2025-10-16 00:30 (UTC) - Enhanced V-TRAC engine implementation

- Context: Previous 'enhanced' drop only added scaffolding. Rebuilt the module to match the redesign (evidence features, straight rationale, tooling) without disturbing Winners Logger or the legacy UI.
- Change:
  - Replaced modules/vtrac_enhanced types/config/features/engine/adapters with the production implementation (shared evidence grid, ring/column weighting, set echoes, cross-section consensus, column-span depth, hot/support bonuses, mask-drop + mirror assists, order-sensitive straights).
  - Added headless CLI (`tools/vtrac_enhanced_cli.py`) and regression suite (`tests/test_vtrac_enhanced_basic.py`, `tests/test_vtrac_evidence.py`) plus a feature-gated Streamlit wrapper storing bundles in session state.
- Impact:
  - `python tools/vtrac_enhanced_cli.py --state Connecticut4` now produces ranked indices/straights and JSON bundles under data/outputs/analysis/vtrac/<STATE>/...; tests lock evidence/mask behaviour.
  - V-TRAC winners HTML now consumes the same evidence grid as the analyzer, so highlights and scoring line up.
  - Legacy analyzer remains default (AAT9_FLAGS.ENHANCED_VTRAC = False) so orchestration stays stable while we cross-check outputs.
- Verification:
  - `pytest tests/test_vtrac_enhanced_basic.py`
  - `python tools/vtrac_enhanced_cli.py --state SampleState --tables-root tests/fixtures/vtrac --analysis-root tests/fixtures/tmp_out`
  - `python tools/vtrac_enhanced_cli.py --state Connecticut4`
## 2025-10-08 05:30 (UTC) - Winners VT-straight + download hardening

- Context: Needed to capture 3344/336644-style VT-straight hits and avoid Streamlit /pages errors when opening reports.
- Change:
  - Extended modules/vtrac_matchers.collect_spans with VT-straight strict + value-block detection (digit-to-VT mapping + run-length logic).
  - Refreshed module_c_vtrac CSS/legend (blue classes) and both renderers to consume the new spans; compact winner report now styles green/blue/purple consistently.
  - Control Center winners tiles now serve an 'Open report (HTML)' download button instead of page navigation; smoke/tests updated for new classes.
- Impact:
  - Analyzer + compact reports highlight VT-straight patterns alongside winner/family hits, matching the training overlay behaviour.
  - Operators open reports reliably (no more missing CSS); unit + smoke guards catch regressions.

## 2025-10-07 22:15 (UTC) - Winners ladder matcher upgrade

- Context: Winners Logger was still missing many R2/R4/R6/R8 hits (and gap-hidden winners) because the renderer only did naive substring checks.
- Change:
  - Added modules/vtrac_matchers with shared helpers (digits-only normalisation, strict + gap-1 matcher, span collection) and rewired module_c_vtrac.generate_index_html_report to call them.
  - Updated the Streamlit tile to use the shared loader, dropped the ad-hoc green overlay, and refreshed the compact logger so singles/doubles panels reflect the same hits.
  - Added regression tests for the matcher and legend/highlight classes.
- Impact:
  - Winners overlays now light up the patterns you called out (including gap-hidden sequences) across Midday/Evening/Combined ladders; legend clarifies the styling.
  - Compact panel stays in sync with analyzer results, and automated tests guard the matcher + import hygiene.
- Verification:
  - python -m pytest tests/test_vtrac_matchers.py tests/test_winner_report_full.py tests/test_digit_reduction_overlay.py
  - python -m py_compile modules/vtrac_matchers.py modules/winner_report_full.py src/core/{module_c_vtrac.py,winners_vtrac_report.py} src/app.py
## 2025-10-07 20:45 (UTC) - Winners logger os-shadow guard

- Context: Control Center's winners tiles were still shadowing the module-level os import, so both the compact and analyzer-style buttons crashed with UnboundLocalError even though the renderer and tables were healthy.
- Change:
  - Added _load_write_winner_full_report() and reused it in the analyzer tile, dropping the inline import gymnastics and letting our bootstrap handle canonical modules.
  - Removed every function-level import os inside the Control Center helpers and appended a unit test that fails if we reintroduce one.
- Impact:
  - Both Winners buttons now call the builder reliably; the full analyzer HTML is produced instead of the "Full report unavailable" warning.
  - Future edits that accidentally add a local import os will fail CI rather than silently breaking the UI.
- Verification:
  - python -m pytest tests/test_winner_report_full.py tests/test_digit_reduction_overlay.py
  - python -m py_compile src/app.py modules/winner_report_full.py src/_import_hygiene.py
## 2025-10-06 04:20 (UTC) - Winners full report import guard

- Context: Control Center's Analyzer-style winner export intermittently failed ("Full report unavailable") whenever the legacy src/utils shim shadowed the canonical utils package during mixed module sessions.
- Change:
  - Updated modules/winner_report_full to pin PROJECT_ROOT to the front of sys.path, evict the shimmed utils modules, and import the canonical path helpers before touching the renderer.
  - Hardened src/_import_hygiene.project_modules_first to reorder sys.path and clear the shim so buttons that rely on the bootstrap always see the real modules tree.
  - Added tests/test_winner_report_full.py to simulate the shim shadowing scenario and ensure future bootstraps cannot regress the import guard.
- Impact:
  - The full Winners tile reliably renders again after the fixes, and future changes to the bootstrap will trip the regression test instead of silently breaking the report.
  - Dev Health continues to show canonical module bindings, making it obvious if the shim ever leaks back in.
- Verification:
  - python -m pytest tests/test_winner_report_full.py tests/test_digit_reduction_overlay.py
  - python -m py_compile modules/winner_report_full.py src/_import_hygiene.py src/app.py
## 2025-10-05 18:45 (UTC) - Digit Reduction overlay + scorer guardrails\n\n- Context: Winner overlay fixes addressed only the tail-row highlight; analyzer scoring lacked SSOT winner signals and there were no direct tests catching regressions.\n- Change:\n  - Replaced the overlay highlighter to scan every reduction step (exact + V-TRAC) and emit a legend/summary banner alongside map/flags/stamp metadata.\n  - Pulled the overlay flag CSV into Analyzer V2, added winner-weight entries to config.yml, and displayed earliest-step counts inside the Streamlit dev expander.\n  - Created ests/test_digit_reduction_overlay.py covering highlight, flag ingestion, and score-row contributions.\n- Impact:\n  - DEV overlays now make it obvious when/where the winner (or its V-TRAC mirrors) surfaced, and Combined autocompletes when only Midday/Evening winners are supplied.\n  - Analyzer CSVs carry dr.win_* evidence for downstream scoring/analysis, and the dev pane reports earliest-step metrics without manual JSON inspection.\n  - Unit coverage guards the overlay/scoring plumbing before future refactors.\n- Verification:\n  - python -m py_compile alpha_analytical/digit_reduction/analyzer_v2/winners_overlay.py alpha_analytical/digit_reduction/analyzer_v2/pipeline.py alpha_analytical/digit_reduction/analyzer_v2/score.py alpha_analytical/digit_reduction/analyzer_v2/ui_dev.py src/app.py\n  - `pytest tests/test_digit_reduction_overlay.py\n\n## 2025-10-05 05:40 (UTC) - Doubles variants regression net

- Context: Regressions around merged C/M/E badges and missing variant files kept recurring when doubles families were touched.
- Change:
  - Captured a 1,000-draw CT/FL snapshot (`tests/fixtures/acceptance/doubles/`) and wired both a ranker unit test plus a Streamlit acceptance case so per-variant tokens stay locked.
  - Added loader coverage (`tests/test_aux_loaders_variants.py`) to ensure Combined/Midday/Evening CSVs resolve predictably, refreshed the positional acceptance assertions, and let `.codex/preflight.ps1 -CheckDoubles` + `run_acceptance.py --with-doubles-health` call the audit automatically.
  - Introduced `scripts/health/check_doubles_variants.py` for post-import audits, updated the startup briefing + Aux docs + Testing Roadmap to call out the new guardrails, and made the pre-commit smoke hook respect `AAT9_RUN_DOUBLES_HEALTH`.
- Impact: Any future edit that collapses badges back to `CEM`, misroutes draw files, or drops a variant now fails fast in unit/acceptance/pre-commit; operators also get a one-command health check before/after data refreshes.
- Files/Refs: .codex/preflight.ps1, scripts/run_acceptance.py, scripts/hooks/run_pytest_smoke.py, scripts/health/check_doubles_variants.py, tests/fixtures/acceptance/doubles/*, tests/test_vtrac_family_ranker_regression.py, tests/acceptance/test_control_center_doubles.py, tests/test_aux_loaders_variants.py, tests/acceptance/test_positional_delaware.py, briefings/CODEX_READ_FIRST_AAT9.md, docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md, docs/AAT9_KIT/AAT9_Testing_Roadmap.md.
- Verification: `pytest tests/test_vtrac_family_ranker_regression.py tests/test_aux_loaders_variants.py`, `python scripts/run_acceptance.py --marker acceptance`, `python scripts/run_acceptance.py --marker smoke`, `.codex/preflight.ps1 -CheckDoubles`.

## 2025-10-03 09:10 (UTC) - Digit reduction winners overlay acceptance

- Context: After wiring the reducer/analyzer acceptance we still lacked guardrails for the winners overlay and its reliance on the new training log naming.
- Change:
  - Updated the overlay loader to search for both singular and legacy plural training JSON filenames so recent reducer runs are discovered.
  - Extended the acceptance scenario to cover Delaware and Florida, running the batch overlay and asserting HTML/map/hits/flags/stamp artifacts for each state.
  - Replaced `datetime.utcnow()` stamps in the overlay with timezone-aware equivalents and documented the expanded coverage in the Testing Roadmap and startup briefing.
- Impact: Acceptance now fails if the overlay stops emitting artifacts or if training logs drift, keeping the digit-reduction flow safe end-to-end.
- Files/Refs: alpha_analytical/digit_reduction/analyzer_v2/winners_overlay.py, tests/acceptance/test_digit_reduction_delaware.py, tests/fixtures/acceptance/digit_reduction/{Delaware4,Florida4}/*, docs/AAT9_KIT/AAT9_Testing_Roadmap.md, briefings/CODEX_READ_FIRST_AAT9.md.
- Follow-ups: Add winners overlay fixtures for additional states once captured, and consider a smoke-level assertion for the batch overlay timestamp output.

## 2025-10-03 07:45 (UTC) - Digit reduction acceptance guard

- Context: The acceptance harness only exercised Aux positional logic and the analyzer could still crash when reducer fixtures lacked own/combined cores.
- Change:
  - Hardened mode.agree_core in the analyzer pivot so empty own/combined terminals no longer raise int('').
  - Added a Delaware digit-reduction acceptance test that runs reducer + analyzer in an isolated analysis root and asserts the expected artifacts.
  - Documented the new coverage in the Testing Roadmap and updated the startup briefing.
- Impact: Acceptance now breaks if digit-reduction artifacts drift, and the analyzer gracefully handles sparse fixtures instead of crashing mid-run.
- Files/Refs: alpha_analytical/digit_reduction/analyzer_v2/pivot.py, tests/acceptance/test_digit_reduction_delaware.py, tests/fixtures/acceptance/digit_reduction/Delaware4/*, scripts/run_acceptance.py, briefings/CODEX_READ_FIRST_AAT9.md, docs/AAT9_KIT/AAT9_Testing_Roadmap.md.
- Follow-ups: Add a winners-overlay acceptance slice and broaden digit-reduction fixtures beyond Delaware once more states are captured.

## 2025-10-02 06:30 (UTC) - Aux heatboard + sums guardrails

- Context: Operators needed the new double-family strips to mirror Aux styling and wanted faster visibility into V-TRAC pressure while preparing downstream scoring hooks.
- Change:
  - Replaced the legacy pair/combination columns with shared Top-5 family strips (C/M/E severity tokens) so Control Center and Aux stay aligned.
  - Added a hazard-based "V-TRAC Heatboard" to both Control Center and Aux using the shared overlay cache.
  - Extended sums stats with `deficit`/`z_tail` fields for future scoring without altering existing UI consumers.
- Impact: The doubles view now matches Aux, hot indices surface at a glance, and sums analytics are ready for future compounding while Black Apple keeps working as-is.
- Files/Refs: src/app.py, modules/module_d_auxiliary_tools/refactored/sums_analysis.py, src/core/vtrac_families.py, tests/test_vtrac_families.py.
- Follow-ups: Consider per-variant heatboard filters and fold the sums deficit into Black Apple once the scoring pass begins.

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

## 2025-09-29 23:30 (UTC) - Aux unified view (DEV) + due doubles columns

- Context: After restoring the Control Center due-doubles columns, we needed a safer way to inspect Combined/Midday/Evening Aux outputs together without refactoring the legacy radio flow.
- Change:
  - Reused the cached Aux payloads to rebuild the due doubles table (pairs + RED combos) on Control Center.
  - Added a DEV-only Unified Aux View expander that renders top pairs/combos/V-TRAC summaries in side-by-side columns while keeping the original per-variant layout intact.
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
  - Replaced per-variant tabs with a side-by-side table (P1P3 columns per variant) while keeping draw-source captions, consensus notes, and the shortlist.
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
# AAT9  Checkpoint Log (Running, Detailed Notes)

Purpose: A single, datetagged log for deeper explanations, context, and rationale that complement the Unified Changelog. Use this when you (or AI) want to capture more than a oneline changelog entry.

How to update
- Append a new section at the top.
- Use the template below; keep entries concise but explanatory.
- Link to relevant files, PR notes, logs, and diagrams.

Template
```
## YYYYMMDD HH:MM (TZ)  Title

- Context: oneparagraph background
- Change: what changed (bullets)
- Rationale: why this improves stability/clarity/UX
- Impact: runtime behavior, workflows, or docs affected
- Files/Refs: file paths, doc sections, diagrams
- Followups: next steps if any
```

---

## 20250906 12:00 (UTC)  Preflight Tables Check + Startup Docs

- Context: We standardized AAT9 startup (KIT + preflight) and wanted a quick, optin validation for combined tables when working on Stable/DR/VTRAC.
- Change:
  - Added `-CheckTables` to `.codex/preflight.ps1` to list `data/outputs/tables` state dirs and confirm a specific state dir exists.
  - Added `docs/AAT9_KIT/HUMAN_READ_FIRST_AAT9.md` with simple operator instructions.
  - Added Codex boot doc `briefings/CODEX_READ_FIRST_AAT9.md` and a clipboard helper `TOOLS/codex_start_aat9.bat`.
- Rationale: Keeps preflight fast by default; adds a quick ondemand tables sanity check; standardizes session startup for both humans and agents.
- Impact: No runtime changes; faster diagnosis when working on combinedtables pages.
- Files/Refs:
  - `.codex/preflight.ps1` (new flags)
  - `docs/AAT9_KIT/HUMAN_READ_FIRST_AAT9.md`
  - `briefings/CODEX_READ_FIRST_AAT9.md`, `TOOLS/codex_start_aat9.bat`
  - KIT index: `docs/AAT9_KIT/AAT9_KIT_README.md`
- Followups: Consider Phase2 Aux audit after new Aux tools land.

## 20250906 13:30 (UTC)  Tables Pipeline Runner + Control Center UI

- Context: Daily workflow uploads a fresh Pick3StatsC4.xlsm and regenerates combined tables; we needed a safe way to run this inapp when needed.
- Change:
  - Added `src/core/pipeline_runner.py` (pure functions) that cleans  extracts  builds combined tables.
  - Wired an optional Tables Pipeline expander in Control Center to upload Excel and run the pipeline.
- Rationale: Keep pipeline runnable from the app, but only on demand; reuse outputs across pages; no recompute on render.
- Impact: No changes to existing pages; optional UI only. Outputs stored under `data/cleaned` and `data/outputs/tables`.
- Files/Refs: `src/core/pipeline_runner.py`, `src/app.py` (Control Center section), `docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md`
- Followups: None required; Phase2 Aux audit deferred until after new Aux tools are added.

## 20250907 10:10 (UTC)  Import Shadowing (utils)  SSOT Bootstrap

- Context: Intermittent startup errors (`ImportError: cannot import name get_cleaned_data_dir` or `NameError: Path is not defined`) after adding optional pipeline UI. Data/layout were fine; errors stemmed from module resolution.
- Root Cause: Two packages named `utils` exist (`/utils` canonical, `/src/utils` legacy). When Streamlit sys.path had `src` before project root, absolute imports (`from utils.path_handler ...`) bound to `src\utils` first, triggering a circular forwarder and partial module.
- Fix: Add a small SSOT import bootstrap at the very top of `src/app.py`:
  - Insert project root at sys.path[0].
  - Evict premature `utils`/`src.utils` bindings if they resolve under `/src/utils`.
  - Import and pin `utils.path_handler` from the toplevel package.
- Impact: Deterministic binding to canonical `utils`; no behavior changes to pages/pipeline.
- Files: `src/app.py`; docs updated: KEEPERS.md, Pitfalls.
- Followups: None  structural rename of `src/utils` not required now.

## 20250907 12:20 (UTC)  Aux Pairs Bands (DisplayOnly)

- Context: Overdue pairs lists used overlapping bands (e.g., repeating red  71 and blue  107), causing label confusion. Policy: red is the highest threshold.
- Change: Mutuallyexclusive bands (displayonly) with red highest:
  - Repeating: red  107; blue 71..106; purple 25..70
  - Nonrepeating: red  56; blue 37..55; purple 25..36
- Caption updated to ASCII ">=" to avoid mojibake. Top5 repeating color mapping aligned; list still sorted by draws_since.
- Impact: No calculation changes; UI buckets and captions now match policy.

## 20250907 12:40 (UTC)  VTrac Big Table: Badge Shows DrawsSince

- Context: Small Index Hits shows draws_since; big table should show it too for Top10 red rows.
- Change: Red rows now use badge "rank (draws_since)"; green rows unchanged.
- Impact: Displayonly; keeps small/big table alignment.

## 20250907 13:00 (UTC)  Digit Reduction: Stacked Report + Training Exports

- Context: Need trainingfriendly exports and stacked view for better screenshots; analysis unchanged.
- Change:
  - Added stacked report HTML and checkbox in page to embed it.
  - Added training CSV/JSON exports under `.../training/` with structural fields, ranks, guidance, and exportonly compaction.
- Outputs:
  - `data/outputs/analysis/digit_reduction/<STATE>/<STATE>digit_reduction_report.html`
  - `.../<STATE>digit_reduction_report_stacked.html`
  - `.../<STATE>digit_reduction_scores.csv`
  - `.../training/<STATE>digit_reduction_steps.csv`
  - `.../training/<STATE>digit_reduction_logs.json`
- Impact: No changes to reduction algorithms or tabbed HTML; only exports and optional embed.

## 20250907 14:10 (UTC)  Winners Logger: VTrac Winner Report (Index Panels)

- Context: Need a perstate, perwinner visual export for external training; older runs had correct vtrac_reports HTML under winners.
- Change: Added an indexbased report generator and UI expander in Control Center:
  - Inputs: State, 3digit winner
  - Renders 3 panels (Midday/Evening/Combined) with:
    - Purple: stablepattern combos for the winners index
    - Green: straight permutations of the winner
  - Writes to: `data/outputs/winners/<YYYYMMDD>/vtrac_reports/<STATE>/<STATE>_vtrac<index>_winner_<timestamp>.html`
- Impact: Does not require stringtables; safe for states whose tables arent mapped yet. Later we can overlay tabledriven details.
- Files: `src/core/winners_vtrac_report.py`, `src/app.py`
## 2025-09-16 16:00 (UTC)  Winners Full Report + Aux VTRAC Restore

- Context: The Aux tools rely on a staged VTRAC reference under `scripts/auxiliary/working/modules/` while the integrated app should use a canonical `modules/*`. A deleted staged `vtrac_reference.py` broke Aux; the Winners Logger (full) also failed due to imports resolving to the staged package and a missing canonical API. Goal: restore Aux, add a canonical VTRAC API, and enable a tableaware analyzerstyle Winners Full report (3 panes, purple index + green straights) without touching analyzer internals.
- Change:
  - Restored staged Aux reference: `scripts/auxiliary/working/modules/vtrac_reference.py` (exports restored; drawsonly Aux unaffected).
  - Added canonical API: `modules/vtrac_reference.py` exporting `get_vtrac_index`, `get_index_set`, `get_index_straights` (backed by analyzer utilities).
  - Implemented full builder: `modules/winner_report_full.py` (reads three combined tables, renders analyzerstyle 3pane HTML via analyzer renderer, applies green straights overlay, writes to `data/outputs/analysis/winners/<STATE>/...`).
  - Wired Control Center tile: Winners Logger (Analyzerstyle full report) now accepts Midday/Evening and generates one HTML per input; compact tile unchanged.
  - Import hygiene: ensured nonAux pages bind `modules/*` to the project tree, not the staged Aux path; added a robust import fallback in the full tile.
- Rationale: Cleanly separates Aux (staged) from the integrated app (canonical), removes import collisions, and reuses the established pipeline tables to produce the expected analyzerstyle Winners view. The canonical API gives nonAux code a single, stable entrypoint, reducing drift.
- Impact:
  - Aux tools: working again; no change to drawsonly behavior.
  - Winners Full tile: produces analyzerstyle HTML under `data/outputs/analysis/winners/<STATE>/...` with purple index coverage + green straights overlay; compact tile remains as a safe fallback when tables are missing.
  - No changes to analyzer internals or other tools; stringsafe CSV reads for new reporting prevent token coercion.
- Files/Refs:
  - Code: `modules/vtrac_reference.py`, `modules/winner_report_full.py`, `src/app.py` (full tile wiring), staged `scripts/auxiliary/working/modules/vtrac_reference.py` (restored)
  - Docs: `docs/AAT9_KIT/AAT9_Winners_VTrac_Report.md` (usage/paths), `docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md` (I/O mapping), `briefings/PITFALLS.txt` (import SSOT + stringsafe IO), `docs/AAT9_KIT/AAT9_Preflight_Reference.md` (tip for tables)
- Followups:
  - Optional: unify all tools on `modules/vtrac_reference.py` over time; keep Aux staged shim as a reexport when youre ready to retire duplicates.
  - Optional: move full report renderer to `src/reporting/` with a template; todays builder already mirrors analyzer layout.
  - Add a tiny smoke CLI to generate a winners full report outside Streamlit if desired.

## 2025-09-17 21:00 (UTC)  Aux Draws Pipeline + Legacy Archive

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


## 2025-10-02 02:30 (UTC) - Aux SSOT + V-TRAC repeat watch

- Context: Windows/thresholds for Aux features were scattered across the app and staged modules, the working V-TRAC table and index hits recomputed overlays separately, and Control Center lacked a quick view of repeat streaks. Pair extraction also relied on implicit behaviour without regression coverage.
- Change:
  - Added src/core/aux_config.py as the single source for Aux windows/thresholds and wired captions/dev health to show the active values.
  - Refactored src/app.py to reuse one _build_vtrac_overlay helper for the working table and index hits, and cached the overlay/repeat summary in cached_aux_analysis.
  - Introduced _summarize_vtrac_repeats and a Control Center "V-TRAC Repeat Watch" table that ranks state variants by current streaks/last repeats.
  - Hardened pair semantics by asserting the Any-Position box rules in scripts/auxiliary/working/modules/analyze_pairs.py and adding ests/test_analyze_pairs_semantics.py.
- Impact:
  - Aux thresholds/windows now stay in sync across captions, preflight, and staged modules; operators see the active depth immediately.
  - V-TRAC UI uses a single overlay source, eliminating mismatched top-10 lists and redundant scans.
  - Control Center highlights hot repeat streaks (with draws-since context) alongside the doubles table, improving cross-state monitoring.
  - Pair extraction has explicit guards + regression tests, reducing risk when staging logic changes.
- Follow-ups:
  - Consider exposing the cached repeat summary in Aux (e.g., badge near the V-TRAC table) for quicker variant-level insight.
  - Expand the repeat watch to include trend deltas (e.g., compare against previous run) once run logging is in place.

## 2025-10-02 07:45 (UTC) - Aux SSOT polish & staged import fallback

- Context: The Aux overdue-threshold caption injection was fragile (leading to syntax errors), and the staged smoke runner could no longer import `core.aux_config` once the SSOT moved under `src/`.
- Change:
  - Replaced the multi-line `st.info` injection with a joined list so thresholds render reliably from the SSOT constants.
  - Patched `scripts/auxiliary/working/modules/analyze_pairs.py` to add the project `src/` directory to `sys.path` when the module is executed from the staged copy, then re-import `core.aux_config`.
  - Regenerated `.codex/first_boot.log` via a headless Streamlit boot to confirm the page loads cleanly.
- Impact:
  - Aux UI now surfaces threshold text without risking syntax errors from scripted replacements.
  - Aux smoke (`python scripts/checks/smoke_aux_vtrac.py`) binds to the same SSOT as the app, keeping staging and prod in sync.
- Verification:
  - `python -m py_compile src/app.py scripts/auxiliary/working/modules/analyze_pairs.py`
  - `pytest -q tests/test_analyze_pairs_semantics.py`
  - `python scripts/checks/smoke_aux_vtrac.py`
  - Headless boot logged to `.codex/first_boot.log`
## 2025-10-02 08:05 (UTC) - Aux roadmap snapshot

- Added `docs/AAT9_KIT/AAT9_Aux_Roadmap.md` summarizing current Aux state (SSOT constants, repeat watch), Phase-1B follow-ups (feature extractor + logging, fresh-data validation), and deferred Phase-2 goals with references to AUX_WATCH/BIG_PICTURE/FIX_80.
- Ready for operators to resume training runs while keeping the next coding steps visible.
## 2025-10-02 08:30 (UTC) - Aux scoring roadmap note
- Added an "Aux Scoring Outlook" section to `docs/AAT9_KIT/AAT9_Aux_Roadmap.md`, outlining ready signals, staged feature extraction/logging work, and future scoring/Control Center integration tasks.

## 2025-10-02 09:10 (UTC) - Control Center V-TRAC double families

- Context: Due doubles table still showed ad-hoc pair/combination columns and Aux lacked a family-aware summary.
- Change:
  - Added a `core.vtrac_families` helper to group boxed doubles by mirror-class families (indices + combo sets).
  - Control Center now ranks Top-5 families per state (variant badges, severity) and displays them in the aggregated doubles table.
  - Aux V-TRAC section shows a matching "Hot Doubles Families" panel plus a family column for each index row.
- Impact: Operators get a compact, consistent watchlist of high-pressure doubles without scanning Aux manually; Control Center & Aux stay in sync.
- Verification: `python -m py_compile src/app.py src/core/vtrac_families.py`; `pytest -q tests/test_analyze_pairs_semantics.py tests/test_vtrac_families.py`.
## 2025-10-02 10:45 (UTC) - Positional tracker shortlist revamp

- Context: The Aux positional shortlist still relied on a fixed cartesian union, lacked V-TRAC awareness, and the UI could not tune caps/features without code edits.
- Change:
  - Promoted shortlist caps/weights/feature toggles into `core/aux_config.POS_SHORTLIST_CONFIG` and wired a Streamlit expander so operators can adjust Top-K/pool/feature flags per state.
  - Replaced the legacy shortlist builder with the new cartesian + repeat-endcap + lane concordance pipeline, feeding V-TRAC hot index/family data from the shared overlay helper.
  - Updated the candidate table to surface structured evidence (per-lane descriptors, repeat endcap lanes, V-TRAC nudges) and tag hot families/indices for cross-tool scoring.
- Impact:
  - Positional Tracker recommendations reflect the same SSOT thresholds used elsewhere, stay aligned with Control Center, and are easier to audit thanks to inline evidence.
  - Future tuning (weights, caps, feature tweaks) can be staged centrally without chasing scattered constants.
- Verification:
  - `python -m py_compile src/app.py modules/module_d_auxiliary_tools/refactored/positional_tool.py`
  - `PYTHONPATH=src;. pytest tests/test_positional_shortlist.py`
  - `PYTHONPATH=src;. pytest tests/test_vtrac_families.py`
  - `PYTHONPATH=src;. pytest tests/test_analyze_pairs_semantics.py`

## 2025-10-03 00:35 (UTC) - Positional shortlist hardening (pos_5)

- Context: pos_5 review flagged loose ends (Combined vs All-Variant terminology, V-TRAC cache reuse, repeat-endcap coverage, pool limits).
- Change:
  - Updated `core/aux_config.POS_SHORTLIST_CONFIG` to the agreed defaults (topk=3, pool=6, max_internal=64, max_rows=16) and synced the dataclass fallbacks.
  - Clarified the Streamlit copy to say "All-Variant consensus" and surfaced the window caption so operators know C/M/E are blended.
  - Cached V-TRAC hot indices/family rankings inside `results` and reused them for both shortlist scoring and the on-page family strip.
  - Added regression tests covering repeat-endcap (989 bridge), lane-concordance candidates, and union pool variant coverage.
- Impact:
  - Delaware-style 989 scenarios now appear with the correct repeat-endcap evidence.
  - Shortlist stays bounded (64 internal seeds, 16 rows) while using the same V-TRAC data the Control Center displays.
  - UI copy avoids the Combined vs All-Variant confusion noted in the audit.
- Verification:
  - `python -m py_compile src/app.py modules/module_d_auxiliary_tools/refactored/positional_tool.py`
  - `PYTHONPATH=scripts/auxiliary/working;src;. pytest tests/test_analyze_pairs_semantics.py`
  - `PYTHONPATH=src;. pytest tests/test_positional_shortlist.py`
  - `PYTHONPATH=src;. pytest tests/test_vtrac_families.py`

## 2025-10-03 02:40 (UTC) - Testing infrastructure baseline

- Context: We needed automated verification beyond health helpers so future sessions can trust refactors.
- Change:
  - Created `scripts/run_acceptance.py` (+ PowerShell wrapper) and seeded `tests/acceptance/test_positional_delaware.py` with fixtures under `tests/fixtures/acceptance/positional/`.
  - Added pre-commit hooks (py_compile + smoke acceptance), a positional stress harness, and a mutmut convenience wrapper.
  - Authored `docs/AAT9_KIT/AAT9_Testing_Roadmap.md` and updated Aux/briefing docs to reference the new process.
- Impact: Developers now have a one-command smoke suite, visible roadmap, and stress scaffolding before touching Aux/positional logic.
- Verification:
  - `python scripts/run_acceptance.py`
  - `python scripts/run_acceptance.py --marker smoke`
  - `python scripts/tools/stress_positional.py --iterations 1 --state Delaware4`






## 2025-10-11 01:10 (UTC) - Aux canonical draw pipeline

- Context: FIX_107/FIX_115 confirmed Aux was still resolving legacy draw paths and staging modules, so the page alternated between "no files" and UnboundLocal errors.
- Change:
  - Locked `utils.path_handler.get_cleaned_draws_dir()` and `modules.aux_loaders.load_state_draws()` to `data/cleaned/draws/*.csv` (legacy root only as an explicit fallback).
  - Vendored the working `analyze_pairs`/`vtrac_reference` modules into `modules/` and removed the staged sys.path shim.
  - Imported Aux windows as defaults (360/1000) so the rescue path no longer crashes; kept the legend/tuning UI as checkbox containers.
  - Dev Health now prints the resolved CSV path, module __file__, and window lengths for Combined/Midday/Evening.
- Impact:
  - Aux/Control Center/BA consistently bind the same draw history (reds back on doubles; V-TRAC overlay renders).
  - Restarting Streamlit can no longer fall back to staged modules or the legacy draw root.
- Verification:
  - `python scripts/tools/validate_aux_doubles.py Connecticut4 --max-n 1200 --no-pairs`
  - `python -c "from modules.aux_loaders import load_state_draws; from modules.analyze_pairs import build_aux_windows; from src.app import _build_vtrac_overlay; from modules.vtrac_reference import get_vtrac_index; draws,_=load_state_draws('Connecticut4'); d100,d1000=build_aux_windows(draws); overlay=_build_vtrac_overlay(d1000, get_vtrac_index); print(len(d100), len(d1000))"`
  - Manual Streamlit smoke via `run_app.bat`.
## 2025-10-15 21:20 (UTC) - V-TRAC enhanced engine scaffold

- Context: Tasks/VTRAC_ANALYZER_RESEARCH - FINAL, RE-DESIGN, and FINAL specs requested a next-gen analyzer with richer evidence without breaking existing UI/logging.
- Change:
  - Landing created the `modules.vtrac_enhanced` package placeholder plus a feature-gated Streamlit wrapper (`src/core/module_c_vtrac_enhanced.py`) and flag in `src/app.py`.
  - No production engine, CLI, or finalized tests shipped yet; entries referencing CLI/test execution remain aspirational until the rebuild completes.
- Impact:
  - Flag, scaffolding, and documentation exist, but the analyzer continues to use the legacy engine. Enhanced logic, tooling, and validation are being rebuilt to match the redesign briefs.
- Verification:
  - Pending (enhanced analyzer work continues).

