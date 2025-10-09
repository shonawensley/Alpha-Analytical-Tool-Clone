## 2025-10-10 - Aux double validation harness\n- Impact: Added ux_validation helpers and a CLI to recompute double draws-since per variant directly from the draws CSVs, making it easy to cross-check Control Center badges.\n- Impact: New unit tests cover threshold classification, variant overlap, and family badge extraction so regressions are caught automatically.\n- Files: alpha_analytical/control_center/aux_validation.py, scripts/tools/validate_aux_doubles.py, tests/test_aux_validation.py.\n\n﻿## 2025-10-10 - Aux draw refresh guardrail
- Impact: Aux draw regeneration now offers a “delete existing draw CSVs” toggle that purges the selected state files before writing, preventing stale data from lingering between runs.
- Impact: Added `alpha_analytical.control_center.draws_refresh.purge_draw_csvs` with unit coverage so the Control Center refresh stays clean and reproducible.
- Files: alpha_analytical/control_center/draws_refresh.py, src/app.py, tests/test_draws_refresh.py, briefings/CODEX_READ_FIRST_AAT9.md, docs/AAT9_KIT/{AAT9_Analysis_Insights.md,AAT9_Testing_Roadmap.md,AAT9_Unified_Changelog.md}.
## 2025-10-10 - Control Center batch winners workflow
- Impact: Control Center now exposes a batch expander that parses the Pick3StatsC4 winners list, runs the winners logger across all tracked states, and optionally kicks off Stable Pattern training bundles in one pass.
- Impact: Added batch_runner utilities (state-order parser, project-state fallbacks) plus unit coverage so the pasted sheet stays aligned with tracked outputs.
- Files: alpha_analytical/control_center/{__init__.py,batch_runner.py}, src/app.py, tests/test_batch_runner.py, docs/AAT9_KIT/{AAT9_Analysis_Insights.md,AAT9_Testing_Roadmap.md,AAT9_Unified_Changelog.md}, briefings/CODEX_READ_FIRST_AAT9.md.
## 2025-10-09 - Stable extractor training bundle\n- Impact: Stable Pattern runs can now emit versioned training bundles (scores, families, spotlight) with manifests for downstream ML; the Streamlit page exposes a toggle to create them per run.\n- Files: alpha_analytical/stable/training_bundle.py, src/core/stable_pattern_extractor.py, src/app.py, tests/test_stable_training_bundle.py, docs/AAT9_KIT/{AAT9_Analysis_Insights.md,AAT9_Testing_Roadmap.md,AAT9_Unified_Changelog.md}.\n\n## 2025-10-09 - V-TRAC long-string highlight overlay
- Impact: Introduced a shared long-string window map so V-TRAC tables permanently tint the Digit-Reduction LS1/LS2 boxes in pale yellow, making it obvious when winners originate from the reduction zones.
- Impact: Wired the renderer to layer the overlay alongside existing winner/V-TRAC/family spans, added CSS legend chips, and enforced the behaviour with unit + smoke tests.
- Files: alpha_analytical/digit_reduction/{__init__.py,long_string_windows.py}, src/core/module_c_vtrac.py, src/utils/path_handler.py, tests/test_long_string_overlay.py, tests/test_winners_renderer.py, scripts/smoke_winners_logger.py, docs/AAT9_KIT/{AAT9_Analysis_Insights.md,AAT9_Testing_Roadmap.md,AAT9_Unified_Changelog.md}.

## 2025-10-09 - Due-doubles cache + snapshot guard
- Impact: Control Center now snapshots draw CSV mtimes/sizes and rebuilds the due-doubles table automatically, eliminating stale draws-since metrics after data refreshes and keeping positional hard-due flags honest.
- Impact: Added `modules/draw_catalog` helpers plus `tests/test_draw_catalog.py`; briefings/testing docs updated so future sessions rerun the guardrails after loader edits.
- Files: src/app.py, modules/draw_catalog.py, tests/test_draw_catalog.py, briefings/CODEX_READ_FIRST_AAT9.md, docs/AAT9_KIT/{AAT9_Analysis_Insights.md,AAT9_Testing_Roadmap.md,AAT9_Unified_Changelog.md}.

## 2025-10-08 - Winners VT-straight coverage + download guard
- Impact: Extended the matcher to emit blue VT-straight spans (strict + value-block), added legend chips, and wired the compact/analyzer tiles to reuse the spans so R2/R4/R6/R8 overlays stay in sync.
- Impact: Replaced Streamlit link navigation with download buttons so Control Center opens analyzer reports without /pages routing errors; smoke/tests updated to assert new classes.
- Files: modules/vtrac_matchers.py, src/core/module_c_vtrac.py, src/core/winners_vtrac_report.py, src/app.py, tests/test_vtrac_matchers.py, tests/test_winners_renderer.py, scripts/smoke_winners_logger.py, docs/AAT9_KIT/{AAT9_Winners_VTrac_Report.md,AAT9_Live_Wiring_and_Data_Paths.md,AAT9_Testing_Roadmap.md,AAT9_Preflight_Reference.md,PITFALLS.txt}, briefings/CODEX_READ_FIRST_AAT9.md.

## 2025-10-07 - Winners pattern-matcher overhaul
- Impact: Analyzer-style reports now use the shared matcher to highlight winner straights (strict + gap-1) and index-family combos across R2/R4/R6/R8, mirroring the digit-reduction overlay; gap hits get dashed styling and a legend.
- Impact: Compact V-TRAC winner report reuses the same targets so singles/doubles panels flag actual winner/family combos instead of literal string matches.
- Impact: Added modules/vtrac_matchers.py with utilities, plus unit tests guarding the matcher and the no-local-import os rule.
- Files: modules/vtrac_matchers.py, src/core/module_c_vtrac.py, src/core/winners_vtrac_report.py, modules/winner_report_full.py, src/app.py, tests/test_vtrac_matchers.py, tests/test_winner_report_full.py, docs/AAT9_KIT/AAT9_Winners_VTrac_Report.md.
## 2025-10-07 - Winners full-report os-shadow fix
- Impact: Refactored the Control Center winners tiles to use a shared loader and eliminated function-level import os, preventing the UnboundLocalError that blocked the analyzer-style export.
- Impact: Added a regression unit test so future edits cannot reintroduce local import os shadowing inside src/app.py.
- Files: src/app.py, tests/test_winner_report_full.py.
## 2025-10-06 - Winners full report import hardening
- Impact: Control Center now normalizes sys.path before running the Analyzer-style winner report, evicts the legacy src/utils shim, and guarantees the builder imports the canonical helpers, so the V-TRAC full report no longer disappears during mixed sessions.
- Impact: Added a regression unit test that simulates the legacy shim shadowing utils to keep future bootstrap edits from reintroducing the failure.
- Files: modules/winner_report_full.py, src/_import_hygiene.py, tests/test_winner_report_full.py.

## 2025-10-05 - Digit Reduction overlay + scoring hardening\n- Impact: Winner overlays now scan every reduction step (exact permutations + V-TRAC mirrors), inject a legend/summary banner, auto-fill the Combined slot when only Midday/Evening winners are provided, and persist summary metadata in the map/flags/stamp artifacts.\n- Impact: Analyzer V2 ingests the overlay flag CSV into per-item rows, adds SSOT weights for winner evidence in config.yml, and surfaces the earliest-step recap inside the Streamlit dev panel.\n- Impact: Added regression tests for overlay highlighting, winner-flag ingestion, and scoring contributions so future refactors keep the guardrails.\n- Files: alpha_analytical/digit_reduction/analyzer_v2/{winners_overlay.py,pipeline.py,score.py,ui_dev.py,config.yml}, src/app.py, tests/test_digit_reduction_overlay.py, docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md, docs/AAT9_KIT/{AAT9_Checkpoint_Log.md,AAT9_Testing_Roadmap.md}, briefings/CODEX_READ_FIRST_AAT9.md.\n\n## 2025-10-05 - Doubles family regression guardrails
- Impact: Locked the CT/FL doubles snapshot into fixtures, added unit/acceptance coverage for the V-TRAC family ranker + Streamlit render, introduced a loader sanity test, and wired the doubles audit into preflight+acceptance hooks so variant badges cannot silently regress.
- Files: .codex/preflight.ps1, scripts/run_acceptance.py, scripts/hooks/run_pytest_smoke.py, scripts/health/check_doubles_variants.py, tests/fixtures/acceptance/doubles/*, tests/test_vtrac_family_ranker_regression.py, tests/acceptance/test_control_center_doubles.py, tests/test_aux_loaders_variants.py, tests/acceptance/test_positional_delaware.py, briefings/CODEX_READ_FIRST_AAT9.md, docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md, docs/AAT9_KIT/AAT9_Testing_Roadmap.md.

## 2025-10-03 - Digit Reduction overlay acceptance (multi-state)
- Impact: Extended the overlay acceptance to cover Delaware and Florida fixtures, keeping reducer/analyzer/overlay artifacts aligned, patched the loader to honour both singular/plural training logs, and replaced utcnow stamps with timezone-aware values.
- Files: alpha_analytical/digit_reduction/analyzer_v2/winners_overlay.py, tests/acceptance/test_digit_reduction_delaware.py, tests/fixtures/acceptance/digit_reduction/{Delaware4,Florida4}/*, docs/AAT9_KIT/AAT9_Testing_Roadmap.md, briefings/CODEX_READ_FIRST_AAT9.md.

## 2025-10-03 - Testing infrastructure baseline
- Impact: Added an acceptance harness (`scripts/run_acceptance.py` + fixtures) with a positional Delaware scenario, smoke-tested via pre-commit; created a Testing Roadmap, stress/mutation helpers, and updated briefings/docs so future sessions run the suite before making changes.
- Files: scripts/run_acceptance.py, scripts/run_acceptance.ps1, scripts/hooks/{py_compile.py,run_pytest_smoke.py}, tests/acceptance/test_positional_delaware.py, tests/fixtures/acceptance/positional/*.txt, scripts/tools/{stress_positional.py,mutate_positional.py}, docs/AAT9_KIT/AAT9_Testing_Roadmap.md, docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md, briefings/CODEX_READ_FIRST_AAT9.md.
## 2025-10-03 - Positional shortlist hardening (pos_5)\n- Impact: Applied the pos_5 checklist by dialing SSOT defaults (pool=6, max_internal=64), clarifying All-Variant consensus labels, reusing Control Center V-TRAC caches, and adding regression tests for repeat-endcap, lane concordance, and union pool coverage.\n- Files: src/app.py, src/core/aux_config.py, modules/module_d_auxiliary_tools/refactored/positional_tool.py, tests/test_positional_shortlist.py.\n\n## 2025-10-02 - Positional tracker shortlist revamp\n- Impact: Aux Positional Tracker now reads a SSOT shortlist config, exposes tuning controls, folds in repeat-endcap/lane concordance seeds, and adds V-TRAC index/family boosts with evidence-rich rows that stay in sync with Control Center.\n- Files: src/app.py, modules/module_d_auxiliary_tools/refactored/positional_tool.py, src/core/aux_config.py, tests/test_positional_shortlist.py.\n\n## 2025-10-02 - Aux heatboard & sums metadata
- Impact: Control Center now renders Top-5 V-TRAC double families with consistent HTML badges, both Control Center and Aux expose a hazard-based "V-TRAC Heatboard" for quick index pressure scans, and sums stats capture `deficit`/`z_tail` for future scoring.
- Files: src/app.py, modules/module_d_auxiliary_tools/refactored/sums_analysis.py, src/core/vtrac_families.py, tests/test_vtrac_families.py.

## 2025-10-01 - V-TRAC Analyzer - tables reader & health
- Impact: V-TRAC now reads the pipeline's combined tables, adds preflight/system-health info, clears stale caches, and no longer exposes the legacy mini-pipeline controls.
- Files: `src/app.py`, `src/core/module_c_vtrac.py`.

## 2025-10-01 - Digit Reduction - training log guardrails
- Impact: Reducer now writes `digit_reduction/<STATE>/training/<STATE>_digit_reduction_log.json` deterministically, analyzer tolerates blank fields, and the Streamlit tab adds preflight checks plus DEV overlay guards to prevent blank screens.
- Files: `src/app.py`, `src/core/module_b_digit_reduction.py`, `alpha_analytical/digit_reduction/analyzer_v2/{io.py,pipeline.py}`.

## 2025-10-01 - V-TRAC UI sanitization
- Impact: Replaced emoji/en dash UI markers with ASCII-only text so the Mojibake guard stays green and the page renders without warnings.
- Files: src/core/module_c_vtrac.py.


## 2025-10-02 - Aux SSOT windows & V-TRAC repeat watch
- Impact: Added core/aux_config.py as the single source of truth for Aux windows/thresholds, surfaced the values in UI captions/dev health, unified the V-TRAC overlay for the working table and index hits, and introduced a Control Center repeat watch panel backed by new overlay helpers.
- Files: src/app.py, src/core/aux_config.py, scripts/auxiliary/working/modules/analyze_pairs.py, 	ests/test_analyze_pairs_semantics.py.


## 2025-10-02 - Aux SSOT follow-up (UI + smoke)
- Impact: Replaced the overdue-threshold info panel with a safe join using the SSOT constants and added a fallback in the staged analyze_pairs module so Aux smokes import core/aux_config even when launched from scripts/.
- Files: src/app.py, scripts/auxiliary/working/modules/analyze_pairs.py.
## 2025-10-02 - Aux roadmap doc
- Impact: Created `docs/AAT9_KIT/AAT9_Aux_Roadmap.md` to capture the current Aux baseline, Phase-1B follow-ups, and deferred goals with references to AUX_WATCH/BIG_PICTURE/FIX_80 so future sessions can ramp quickly.
- Files: docs/AAT9_KIT/AAT9_Aux_Roadmap.md, docs/AAT9_KIT/AAT9_Checkpoint_Log.md.


## 2025-10-02 - Control Center V-TRAC double families
- Impact: Replaced the due-doubles pair/combination columns with Top-5 V-TRAC double family strips (severity + variant tags) and surfaced the same rankings on the Aux page with a family column.
- Files: src/app.py, src/core/vtrac_families.py, docs/AAT9_KIT/AAT9_Aux_Roadmap.md.













