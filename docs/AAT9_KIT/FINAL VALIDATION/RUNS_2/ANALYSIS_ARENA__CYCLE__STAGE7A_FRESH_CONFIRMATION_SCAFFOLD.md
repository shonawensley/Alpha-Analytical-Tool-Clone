# Analysis Arena Stage 7A Fresh Confirmation Scaffold

## Guardrail

Stage 7A is read-only. It prepares future/fresh-window evaluation rows from Stage 6C and Stage 6F evidence; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- confirmation requirements: `9`
- March seed benchmarks: `20`
- future-window template rows: `29`
- Nothing in this scaffold confirms a fresh-window result yet. It defines what the next fresh window must prove.

## Confirmation Requirements

| requirement_id | target | pass_threshold | active_blockers |
| --- | --- | --- | --- |
| S7A-REQ-001 | primary_restrained_candidate_expression | false_positive_proxy_rate_delta <= -0.050; pool_normalized_positive_yield_delta > 0; avg_pool_ratio_b_vs_a <= 1.500; positive conversions remain non-trivial. | rewrite_blocker_primary_repeat |
| S7A-REQ-002 | concentration_warning_break | Primary can pass with warnings only if metrics repeat and concentration warnings are explicit; concentration alone cannot confirm a macro finding. | rewrite_blocker_concentration |
| S7A-REQ-003 | support_context_modifier | support-on subset must reduce FP proxy or improve yield versus support-off peer while not materially expanding pool exposure. | rewrite_blocker_support_modifier |
| S7A-REQ-004 | restraint_soft_penalty | soft penalty must reduce FP pressure versus no-penalty reference while preserving materially useful positive conversions; hard veto is forbidden at this stage. | rewrite_blocker_restraint_soft_before_hard |
| S7A-REQ-005 | lineage_narrowing | narrowed lineage must improve or preserve FP/yield versus primary while adding non-duplicate conversions. |  |
| S7A-REQ-006 | decay_companion_boundary | decay remains companion-only; no candidate permission even when carrying useful explanatory hits. | rewrite_blocker_decay_boundary |
| S7A-REQ-007 | duplicate_credit_guardrail | candidate union must not claim duplicate scoring credit. | rewrite_blocker_duplicate_credit |
| S7A-REQ-008 | macro_findings_gate | repeat evidence exists and caveats are logged. |  |
| S7A-REQ-009 | translator_scoring_rewrite_gate | all prerequisite gates pass or remain explicitly quarantined. |  |

## March Seed Benchmarks

| benchmark_id | type | source_id | metrics |
| --- | --- | --- | --- |
| S7A-BENCH-001 | stage6b_scenario | baseline_clean_boxed | fp=60.4%; yield=12.407; positive=333; state_days=53 |
| S7A-BENCH-002 | stage6b_scenario | primary_restrained_candidate_expression | fp=46.8%; yield=16.075; positive=688; state_days=62 |
| S7A-BENCH-003 | stage6b_scenario | secondary_lineage_supported_restrained | fp=46.3%; yield=13.395; positive=434; state_days=43 |
| S7A-BENCH-004 | stage6b_scenario | broad_lineage_foundation_reference | fp=54.5%; yield=14.372; positive=1190; state_days=71 |
| S7A-BENCH-005 | stage6b_scenario | decay_watch_companion_excluded | fp=82.5%; yield=3.920; positive=1482; state_days=354 |
| S7A-BENCH-006 | stage6d_restraint_bucket | S6D-RESCUE-012 | fp=47.8%; yield=18.382; positive=50 |
| S7A-BENCH-007 | stage6d_restraint_bucket | S6D-RESCUE-015 | fp=47.6%; yield=18.571; positive=39 |
| S7A-BENCH-008 | stage6d_restraint_bucket | S6D-RESCUE-016 | fp=47.6%; yield=18.571; positive=39 |
| S7A-BENCH-009 | stage6d_restraint_bucket | S6D-RESCUE-001 | fp=62.8%; yield=12.623; positive=502 |
| S7A-BENCH-010 | stage6d_restraint_bucket | S6D-RESCUE-002 | fp=62.8%; yield=12.550; positive=502 |
| S7A-BENCH-011 | stage6e_support_bucket | S6E-SUPPORT-001 | fp=35.8%; yield=15.409; positive=98; fp_delta_peer=-0.200 |
| S7A-BENCH-012 | stage6e_support_bucket | S6E-SUPPORT-002 | fp=34.7%; yield=15.458; positive=81; fp_delta_peer=-0.212 |
| S7A-BENCH-013 | stage6e_support_bucket | S6E-SUPPORT-003 | fp=39.4%; yield=13.426; positive=29; fp_delta_peer=-0.180 |
| S7A-BENCH-014 | stage6e_support_bucket | S6E-SUPPORT-004 | fp=46.3%; yield=13.395; positive=434; fp_delta_peer=-0.022 |
| S7A-BENCH-015 | stage6e_support_bucket | S6E-SUPPORT-005 | fp=36.6%; yield=9.901; positive=20; fp_delta_peer=-0.050 |

## Run Checklist

| step | check | status |
| --- | --- | --- |
| 1 | Run normal fresh-window cadence and close the window artifacts. | pending_future_window |
| 2 | Run Stage 3 through Stage 6B readback on the fresh evidence. | pending_future_window |
| 3 | Run Stage 6C, Stage 6D, Stage 6E, and Stage 6F on the fresh evidence. | pending_future_window |
| 4 | Evaluate 9 Stage 7A confirmation requirements against the future window. | pending_future_window |
| 5 | Keep live scoring, candidate-generation, budget, support, restraint, and decay permissions blocked unless explicitly cleared by future readback. | always_required |

## Outputs

- scaffold_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_FRESH_CONFIRMATION_SCAFFOLD.json`
- confirmation_requirements: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_CONFIRMATION_REQUIREMENTS.csv`
- march_seed_benchmarks: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_MARCH_SEED_BENCHMARKS.csv`
- future_window_evaluation_template: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_FUTURE_WINDOW_EVALUATION_TEMPLATE.csv`
- run_checklist: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7A_RUN_CHECKLIST.csv`
