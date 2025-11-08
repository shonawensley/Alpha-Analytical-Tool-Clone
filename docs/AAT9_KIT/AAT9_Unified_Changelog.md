## 2025-11-05 - Digit Reduction lockscore + validation suite
- Impact: Analyzer V2 now emits config-gated `final_linear`, `final_prob`, `score_v2`, and `lockscore_v2/lockscore_prob` columns so single-column survivors, fresh echoes, and V-TRAC heat get surfaced without touching reducers or winners writers.
- Impact: Dropped in `scripts/harness/dr_quickcheck.py` plus a winners-aware validation runner (`scripts/experiments/digit_reduction_validate.py`) and grid helper (`scripts/experiments/dr_grid_search.py`) that produce `reports/DR/<STAMP>/digit_reduction_{metrics,top_misses}.csv` and `DR_Perf_Summary.md` for rapid June-17-style regressions.
- Files: alpha_analytical/digit_reduction/analyzer_v2/{config.yml,pipeline.py,scoring.py}, scripts/{harness/dr_quickcheck.py,experiments/digit_reduction_validate.py,experiments/dr_grid_search.py}, data/winners_20250617.csv, reports/DR/20250617/**

## 2025-11-07 - Pick3 workbook history + Stable Pattern multi-variant ingest
- Impact: Added `utils.path_handler.get_pick3_workbook_path()` plus an optional helper (`scripts/tools/select_pick3_history.py`) so every module (cleaners, aux draws, pipelines, Streamlit) automatically loads dated `Pick3StatsC4_YYYY-MM-DD.xlsm` files without path edits; environment override supported via `PICK3_WORKBOOK`.
- Impact: Documented the new `data/history/` (dated workbooks) and `data/results/` (per-day outcomes) workflow in the KIT so backtests/examples can target any day; zipped reports can be dragged straight into review chats.
- Impact: Stable Pattern extractor now ingests Midday, Evening, and Combined tables in one run (instead of Combined-only) and tags each row’s `section`, giving us immediate coverage across variants before we add the new scoring features.
- Files: utils/path_handler.py, scripts/tools/select_pick3_history.py, scripts/auxiliary/generate_draws_csv.py, modules/module_d_auxiliary_tools/refactored/extractor.py, src/app.py, src/app_fixed.py, src/app_cp1252.py, docs/AAT9_KIT/{AAT9_Data_Validation_Workflow.md,AAT9_Analysis_Insights.md,AAT9_Checkpoint_Log.md}

## 2025-11-08 - Stable Pattern persistence + VTRAC straight cues
- Impact: Stable extractor now tracks Set3→Set2→Set1 carryover and Draw1→Draw7 chains per pattern, exporting `persistence_set_count`, `persistence_draw_run`, and their scored bonuses (`score_persistence_set/draw`) so lingering 3-value clusters rank higher and surface in the CSV/why ledger.
- Impact: Added `score_vtrac_straight` (config-driven) for straight candidates in late columns plus `set_chainX` / `draw_chainY` tags; `feature_config.yml` gained the corresponding weights. CSV schema updated accordingly.
- Impact: `tests/test_stable_multi_variant.py` now covers both multi-section ingestion and the persistence scoring path; `python -m py_compile` used for quick verification.
- Files: alpha_analytical/stable/{__init__.py,feature_config.yml}, tests/test_stable_multi_variant.py, docs/AAT9_KIT/{AAT9_Analysis_Insights.md,AAT9_Checkpoint_Log.md}

## 2025-11-05 - Digit Reduction VTRAC validator + extended-cluster tuning
- Impact: Validator now supports literal/box/VTRAC-family matching (`--match-mode`) and reports VTRAC-specific Hit@K so family-level wins count during June-17 reverse engineering.
- Impact: Added extended cluster + VTRAC-family rescues to `scoring_v2`/`lockscore`, enabling YAML-only tuning of long-run evidence; reran analyzers/validators to produce `reports/DR/20250617_V_*` bundles that show Hit@3 rising to ~6% when VTRAC families are credited.
- Files: scripts/experiments/{digit_reduction_validate.py,dr_grid_search.py}, alpha_analytical/digit_reduction/analyzer_v2/{config.yml,scoring.py}, reports/DR/20250617_V_*, docs/AAT9_KIT/AAT9_Checkpoint_Log.md

## 2025-11-02 - Digit Reduction Analyzer V2 refactor + spec lock
- Impact: Replaced the Analyzer V2 feature stack with cluster-aware detection (exact/V-TRAC/drop/family), per-item density + drop metadata, and config-driven scoring with lock gating.
- Impact: Pipeline now aggregates cross-column/variant/method echoes, records config hash + git SHA, and coordinates optional winners overlay bundles; writers gained diagnostics toggles.
- Impact: Added spec lock (`docs/DR_OPT_SPEC_LOCK.md`) plus regression tests covering feature extraction, aggregation metrics, and scoring behaviour.
- Files: alpha_analytical/digit_reduction/analyzer_v2/{clustering.py,config.yml,features.py,pipeline.py,score.py,vtrac_index.py,winners_overlay.py,writers.py}, docs/DR_OPT_SPEC_LOCK.md, tests/{test_digit_reduction_overlay.py,test_digit_reduction_features_v2.py}

## 2025-11-03 - Digit Reduction lean evidence bundle
- Impact: Analyzer V2 now emits only the evidence trio (`per_item.csv`, `top_candidates.csv`, `meta.json`) plus stacked HTML per variant; reducer steps stay optional diagnostics, and the verbose JSON log is retired.
- Impact: All per-tool winner artifacts are gated behind diagnostics; Control Center is the only writer of machine-readable `winner_map.json`/`winner_flags.csv` and the winners HTML.
- Impact: Training bundles package the lean files (plus steps when enabled) and no longer duplicate winners by default.
- Files: alpha_analytical/digit_reduction/analyzer_v2/{config.yml,pipeline.py,stacked.py,training_bundle.py,writers.py}, src/core/module_b_digit_reduction.py, scripts/checks/dr_analyzer_v2_harness.py.

## 2025-10-26 - V-TRAC scoring config + explainability
- Impact: `vtrac_score_and_export.py` now supports argparse, logging, explainability strings, union-based echoes, and config-driven weights/priors (including state overrides).
- Impact: Bundle helper auto-applies `configs/vtrac_score_config.json`; the compact report exposes `section_prior`, `state_prior`, and `why` columns so reviewers can audit contributions quickly.
- Impact: Added pytest-backed fixture ensuring consensus rescue, analyzer-only echo boosts, and config overrides stay stable.
- Files: TOOLS/vtrac_score_and_export.py, TOOLS/run_vtrac_share_bundle.py, configs/vtrac_score_config.json, tests/test_vtrac_score_export.py, tests/fixtures/vtrac_validation/DemoState4/validation_report.json, tasks/VTRAC_ENHANCMENTS.txt, tasks/VALIDATE_C.TXT, briefings/CODEX_READ_FIRST_AAT9_WSL.md.

## 2025-10-18 - Data validation workflow + insights refresh
- Impact: Added a dedicated workflow guide (`AAT9_Data_Validation_Workflow.md`) capturing the full loop for generating enhanced bundles, running the validator, producing `matrix.csv`/`findings.md`, and handing artifacts to reviewers (commit/push, zip, or targeted upload).
- Impact: Logged data-sharing best practices and aggregator outlook in `AAT9_Analysis_Insights.md`, emphasising continued rule-based tuning with optional ML later.
- Files: docs/AAT9_KIT/{AAT9_Data_Validation_Workflow.md,AAT9_Analysis_Insights.md}

## 2025-10-18 - Validator regression guardrails + batch metrics
- Impact: Section summaries now capture mask-drop/reduction/mirror/doubles stats per variant; validator compares straight occurrences and surfaces analyzer metrics/straights alongside Winners HTML.
- Impact: Added fixture-backed regression (`tests/test_vtrac_validate_fixture.py`) with frozen Delaware4/Florida4 HTML+JSON pairs so validator outputs stay populated; new batch helper (`tools/vtrac_validate_batch.py`) prints precision@K and supports comparison bundles.
- Impact: Florida4 Combined review confirmed the absence of 3-value clusters is expected (columns collapse to two digits); documentation updated with findings and new validator/batch workflows.
- Files: modules/vtrac_enhanced/adapters.py, tools/vtrac_validate.py, tools/vtrac_validate_batch.py, tests/test_vtrac_validate_fixture.py, tests/fixtures/vtrac_validation/**, docs/AAT9_KIT/{AAT9_Analysis_Insights.md,AAT9_Testing_Roadmap.md,AAT9_Unified_Changelog.md}

## 2025-10-17 - Validation - Enhanced V-TRAC parity harness and bundle summaries
- Impact: Added `tools/vtrac_validate.py` to parse Winners Logger HTML, recompute 3-value V-TRAC signatures, hot/super-hot counts, consensus flags, and compare them to analyzer outputs (supports single run and optional A/B inputs).
- Impact: Extended `modules.vtrac_enhanced.write_prediction_bundle` so JSON bundles now include per-section summaries (`hot_count`, `superhot_count`, `consensus`, `stable_columns`, `top_box_signatures`, `ring_votes`) and `top_straights`, enabling downstream parity checks without re-reading tables.
- Impact: Updated Streamlit wrapper, headless CLI, and regression test to pass the engine input into the bundle writer; refreshed sample validations for Delaware4, Michigan4, Florida4, NewJersey4, and Virginia4 with overlap now visible in `data/outputs/analysis/vtrac_validation/`.
- Files: tools/vtrac_validate.py, modules/vtrac_enhanced/adapters.py, tools/vtrac_enhanced_cli.py, src/core/module_c_vtrac_enhanced.py, tests/test_vtrac_enhanced_basic.py, docs/AAT9_KIT/AAT9_Analysis_Insights.md

## 2025-10-16 - Enhanced V-TRAC analyzer (engine + tooling delivered)
- Impact: Replaced the placeholder analyzer with the production engine: ring/column survival, set echoes, cross-section consensus, column-span depth, hot/super-hot support, reduction/mirror assists, and order-sensitive straight scoring. Outputs now land under `data/outputs/analysis/vtrac/<STATE>/...` with rich evidence.
- Impact: Introduced a shared evidence grid (`modules/vtrac_enhanced/evidence.py`) consumed by both the analyzer and the V-TRAC winners logger, so highlights and scoring share the same data.
- Impact: Added a headless CLI (`tools/vtrac_enhanced_cli.py`) and regression suite (`tests/test_vtrac_enhanced_basic.py` + fixtures) plus a feature-gated Streamlit wrapper (`src/core/module_c_vtrac_enhanced.py`). Legacy engine stays default until A/B review.
- Files: modules/vtrac_enhanced/{__init__.py,types.py,config.py,features.py,engine.py,adapters.py,evidence.py}, tools/vtrac_enhanced_cli.py, tests/{test_vtrac_enhanced_basic.py,test_vtrac_evidence.py}, tests/fixtures/vtrac/**, src/core/module_c_vtrac.py, src/core/module_c_vtrac_enhanced.py

## 2025-10-14 - Stable winners guardrail polish
- Impact: Winners enrichment now reuses the Stable canon helpers, coerces diagnostic booleans to nullable dtypes, and adds a pre-commit guard so the CSV export keeps the evidence columns; manifest tests assert evidence schema versions stay recorded.
- Impact: Digit Reduction bundle packaging verified in-situ (20251011 stamp) and Control Center batch smoke confirmed Stable metrics + winners evidence + lean DR bundles continue to land together.
- Files: alpha_analytical/stable/winners_enrich.py, scripts/hooks/check_winners_export.py, tests/test_stable_training_bundle.py, tests/test_stable_doubles_adjacency_negative.py, .pre-commit-config.yaml, .gitignore, docs/AAT9_KIT/AAT9_Testing_Roadmap.md

## 2025-10-14 - Docs - Onboarding compass and startup briefing refresh
- Impact: Added AAT9_Onboarding_Compass.md to centralize onboarding flow, validation loop, and documentation expectations.
- Impact: Updated CODEX_READ_FIRST briefing and KIT README to point at the compass and remove redundant checklists.
- Files: docs/AAT9_KIT/{AAT9_Onboarding_Compass.md,AAT9_KIT_README.md}, briefings/CODEX_READ_FIRST_AAT9.md

## 2025-10-13 - Stable evidence bus + lean Digit Reduction bundles
- Impact: Streamlined the Stable winners evidence flow so Control Center exposes consolidated metrics/evidence (downloadable CSV) and the training manifest records schema versions.
- Impact: Digit Reduction training bundles now package Midday/Evening winner artifacts by default (10 files) with an `include_combined` toggle; runtime overlays still emit Combined for diagnostics.
- Files: alpha_analytical/stable/{metrics.py,training_bundle.py,winners_enrich.py}, alpha_analytical/control_center/batch_runner.py, alpha_analytical/digit_reduction/analyzer_v2/training_bundle.py, tests/test_digit_training_bundle.py, src/app.py, docs/AAT9_KIT/{AAT9_Quickstart_Cheat_Sheet.md}.

## 2025-10-12 - Aux canonical draws guardrail
- Impact: Canonicalised Aux and Control Center draw loading through `modules.aux_loaders.load_state_draws`, removed staged fallbacks, and patched the V-TRAC overlay to reuse cached draw windows so the Aux page no longer crashes when staged modules disappear.
- Impact: Added regression coverage that asserts live data resolves under `data/cleaned/draws`, updated workflow docs, and standardised the Aux validation harness as the go-to guardrail after draw refreshes.
- Files: src/app.py, tests/test_aux_loader_canonical_paths.py, docs/AAT9_KIT/{AAT9_Quickstart_Cheat_Sheet.md,AAT9_Workflow_Standard.md,AAT9_Unified_Changelog.md}, scripts/checks/smoke_positional.py, .codex/preflight.ps1.

## 2025-10-10 - Digit Reduction batch workflow\n- Impact: Control Center batch workflow can now refresh Digit Reduction outputs, build Analyzer V2 overlays, and optionally assemble Digit Reduction training bundles alongside the winners logger and Stable pipeline so all auxiliary artefacts stay in sync.\n- Impact: Added batch runner helpers and Streamlit toggles covering reducer/overlay/analyzer/bundle steps plus mirror controls; UI now surfaces per-state artefact links and guards missing tables.\n- Impact: Hardened Analyzer V2 own_vs_combined to treat empty cores as False, preventing ValueErrors during class-triple runs.\n- Impact: Added regression coverage for the batch workflow scaffolding and the pivot guard.\n- Files: alpha_analytical/control_center/batch_runner.py, src/app.py, alpha_analytical/digit_reduction/analyzer_v2/pivot.py, tests/test_control_center_batch_runner.py, tests/test_digit_reduction_overlay.py, docs/AAT9_KIT/{AAT9_Analysis_Insights.md,AAT9_Workflow_Standard.md,AAT9_Quickstart_Cheat_Sheet.md,AAT9_Unified_Changelog.md}, briefings/CODEX_READ_FIRST_AAT9.md.\n\n## 2025-10-10 - Aux double/pair validation harness\n- Impact: Added aux_validation helpers and a CLI to recompute double and pair draws-since per variant directly from the draws CSVs, making it easy to cross-check Control Center badges and pair severity.\n- Impact: New unit tests cover thresholds, variant overlap, family badge extraction, and pair severity so regressions are caught automatically.\n- Files: alpha_analytical/control_center/aux_validation.py, scripts/tools/validate_aux_doubles.py, tests/test_aux_validation.py.
- Impact: Added repeat-watch and positional hard-due validators plus a CLI so streak summaries and hard-due tags can be replayed directly from CSVs without launching Streamlit.\n- Impact: Extended unit coverage to lock repeat streak metrics and hard-due tagging against the acceptance fixtures.\n- Files: alpha_analytical/control_center/aux_validation.py, scripts/tools/validate_aux_repeat.py, tests/test_aux_validation.py.
- Impact: Introduced V-TRAC overlay/heatboard and sums validators plus a CLI so Control Center overlays can be cross-checked directly from the CSVs.
- Acceptance: added tests/acceptance/test_vtrac_overlay_connecticut.py to snapshot overlay/heatboard/sums outputs for Connecticut, keeping the CLI and UI aligned with fixtures.
- Impact: Unit coverage now compares overlay and heatboard outputs against the Streamlit helpers to catch drift immediately.
- Files: alpha_analytical/control_center/aux_validation.py, scripts/tools/validate_aux_vtrac.py, tests/test_aux_validation.py.\n\n?## 2025-10-10 - Aux draw refresh guardrail
- Impact: Aux draw regeneration now offers a delete existing draw CSVs toggle that purges the selected state files before writing, preventing stale data from lingering between runs.
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
- Files: src/app.py, src/core/aux_config.py, scripts/auxiliary/working/modules/analyze_pairs.py, ests/test_analyze_pairs_semantics.py.


## 2025-10-02 - Aux SSOT follow-up (UI + smoke)
- Impact: Replaced the overdue-threshold info panel with a safe join using the SSOT constants and added a fallback in the staged analyze_pairs module so Aux smokes import core/aux_config even when launched from scripts/.
- Files: src/app.py, scripts/auxiliary/working/modules/analyze_pairs.py.
## 2025-10-02 - Aux roadmap doc
- Impact: Created `docs/AAT9_KIT/AAT9_Aux_Roadmap.md` to capture the current Aux baseline, Phase-1B follow-ups, and deferred goals with references to AUX_WATCH/BIG_PICTURE/FIX_80 so future sessions can ramp quickly.
- Files: docs/AAT9_KIT/AAT9_Aux_Roadmap.md, docs/AAT9_KIT/AAT9_Checkpoint_Log.md.


## 2025-10-02 - Control Center V-TRAC double families
- Impact: Replaced the due-doubles pair/combination columns with Top-5 V-TRAC double family strips (severity + variant tags) and surfaced the same rankings on the Aux page with a family column.
- Files: src/app.py, src/core/vtrac_families.py, docs/AAT9_KIT/AAT9_Aux_Roadmap.md.














## 2025-10-11 - Aux canonical draw loader & module cleanup
- Impact: Locked Aux/BA/Control Center draw resolution to `data/cleaned/draws/`, vendored the working analyze_pairs / vtrac_reference modules, flattened the remaining expander, and bound the 360/1000 windows via safe defaults. Aux now renders without staged fallbacks and the red tier returns consistently.
- Files: utils/path_handler.py, modules/aux_loaders.py, modules/analyze_pairs.py, modules/vtrac_reference.py, src/app.py.

# 2025-10-16 - Enhanced V-TRAC analyzer (engine + tooling delivered)
- Impact: Replaced the placeholder enhanced analyzer with the production engine: ring/column survival, hot-zone boosts, cross-section consensus, reduction/mirror assists, and order-sensitive straight scoring. Outputs now land under `data/outputs/analysis/vtrac/<STATE>/...` with rich evidence.
- Impact: Added a headless CLI (`tools/vtrac_enhanced_cli.py`) and regression suite (`tests/test_vtrac_enhanced_basic.py` + fixtures) so the analyzer can be smoked outside Streamlit. Feature-gated UI wrapper (`src/core/module_c_vtrac_enhanced.py`) mirrors the legacy page while storing results and bundles in session state.
- Files: modules/vtrac_enhanced/{__init__.py,types.py,config.py,features.py,engine.py,adapters.py}, tools/vtrac_enhanced_cli.py, tests/test_vtrac_enhanced_basic.py, tests/fixtures/vtrac/**, src/core/module_c_vtrac_enhanced.py.
- Notes: Tuning/Why panels and learning capsules remain future work; flag `AAT9_FLAGS.ENHANCED_VTRAC` stays false until cross-validated.

## 2025-10-13 - Stable extractor regression shield (work paused)
- Impact: Row payload now exports per-component score fields (score_covscore_hidden) and flags hidden 3-value patterns; YAML gained doubles_trigger_bonus / hidden3v_bonus.
- Impact: Family post-pass exports fam_* score parts and placeholders for section/progression bonuses.
- Status: consensus?doubles scoring, section/progression bonus plumbing, last_remaining 3v bonus, metrics writer, regression-guard tests/hooks still pending (see tasks/FIX_122.txt for checklist).
- Files: alpha_analytical/stable/__init__.py, alpha_analytical/stable/post_pass_families.py, alpha_analytical/stable/feature_config.yml, tests/test_stable_contracts.py.
## 2025-10-13 - Stable extractor regression shield (work paused)
- Impact: Row payload now exports per-component score fields (score_covscore_hidden) and flags hidden 3-value patterns; YAML gained doubles_trigger_bonus / hidden3v_bonus.
- Impact: Family post-pass exports fam_* score parts and placeholders for section/progression bonuses.
- Status: consensus?doubles scoring, section/progression bonus plumbing, last_remaining 3v bonus, metrics writer, regression-guard tests/hooks still pending (see tasks/FIX_122.txt for checklist).
- Files: alpha_analytical/stable/__init__.py, alpha_analytical/stable/post_pass_families.py, alpha_analytical/stable/feature_config.yml, tests/test_stable_contracts.py.
## 2025-10-13 - Stable extractor regression shield (work paused)
- Impact: Row payload now exports per-component score fields (score_covscore_hidden) and flags hidden 3-value patterns; YAML gained doubles_trigger_bonus / hidden3v_bonus.
- Impact: Family post-pass exports fam_* score parts and placeholders for section/progression bonuses.
- Status: consensus?doubles scoring, section/progression bonus plumbing, last_remaining 3v bonus, metrics writer, regression-guard tests/hooks still pending (see tasks/FIX_122.txt for checklist).
- Files: alpha_analytical/stable/__init__.py, alpha_analytical/stable/post_pass_families.py, alpha_analytical/stable/feature_config.yml, tests/test_stable_contracts.py.
## 2025-10-13 - Stable extractor regression shield (work paused)
- Impact: Row payload now exports per-component score fields (score_covscore_hidden) and flags hidden 3-value patterns; YAML gained doubles_trigger_bonus / hidden3v_bonus.
- Impact: Family post-pass exports fam_* score parts and placeholders for section/progression bonuses.
- Status: consensus?doubles scoring, section/progression bonus plumbing, last_remaining 3v bonus, metrics writer, regression-guard tests/hooks still pending (see tasks/FIX_122.txt for checklist).
- Files: alpha_analytical/stable/__init__.py, alpha_analytical/stable/post_pass_families.py, alpha_analytical/stable/feature_config.yml, tests/test_stable_contracts.py.
