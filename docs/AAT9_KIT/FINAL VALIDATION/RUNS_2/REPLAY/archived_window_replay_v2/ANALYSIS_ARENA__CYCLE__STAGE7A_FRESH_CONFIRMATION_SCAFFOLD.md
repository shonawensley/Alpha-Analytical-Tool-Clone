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
| S7A-BENCH-001 | stage6b_scenario | baseline_clean_boxed | fp=35.4%; yield=55.897; positive=109; state_days=22 |
| S7A-BENCH-002 | stage6b_scenario | primary_restrained_candidate_expression | fp=47.3%; yield=51.487; positive=1091; state_days=27 |
| S7A-BENCH-003 | stage6b_scenario | secondary_lineage_supported_restrained | fp=45.7%; yield=50.631; positive=361; state_days=17 |
| S7A-BENCH-004 | stage6b_scenario | broad_lineage_foundation_reference | fp=51.3%; yield=47.652; positive=1583; state_days=38 |
| S7A-BENCH-005 | stage6b_scenario | decay_watch_companion_excluded | fp=83.0%; yield=9.781; positive=1848; state_days=171 |
| S7A-BENCH-006 | stage6d_restraint_bucket | S6D-RESCUE-003 | fp=55.2%; yield=43.638; positive=391 |
| S7A-BENCH-007 | stage6d_restraint_bucket | S6D-RESCUE-004 | fp=50.5%; yield=47.582; positive=246 |
| S7A-BENCH-008 | stage6d_restraint_bucket | S6D-RESCUE-005 | fp=50.7%; yield=47.544; positive=242 |
| S7A-BENCH-009 | stage6d_restraint_bucket | S6D-RESCUE-009 | fp=54.0%; yield=44.690; positive=101 |
| S7A-BENCH-010 | stage6d_restraint_bucket | S6D-RESCUE-011 | fp=52.1%; yield=46.061; positive=76 |
| S7A-BENCH-011 | stage6e_support_bucket | S6E-SUPPORT-001 | fp=55.2%; yield=43.638; positive=391; fp_delta_peer=-0.119 |
| S7A-BENCH-012 | stage6e_support_bucket | S6E-SUPPORT-002 | fp=50.2%; yield=49.774; positive=220; fp_delta_peer=-0.009 |
| S7A-BENCH-013 | stage6e_support_bucket | S6E-SUPPORT-003 | fp=50.7%; yield=49.261; positive=200; fp_delta_peer=-0.010 |
| S7A-BENCH-014 | stage6e_support_bucket | S6E-SUPPORT-004 | fp=44.8%; yield=52.446; positive=193; fp_delta_peer=-0.196 |
| S7A-BENCH-015 | stage6e_support_bucket | S6E-SUPPORT-005 | fp=45.0%; yield=52.500; positive=189; fp_delta_peer=-0.194 |

## Run Checklist

| step | check | status |
| --- | --- | --- |
| 1 | Run normal fresh-window cadence and close the window artifacts. | pending_future_window |
| 2 | Run Stage 3 through Stage 6B readback on the fresh evidence. | pending_future_window |
| 3 | Run Stage 6C, Stage 6D, Stage 6E, and Stage 6F on the fresh evidence. | pending_future_window |
| 4 | Evaluate 9 Stage 7A confirmation requirements against the future window. | pending_future_window |
| 5 | Keep live scoring, candidate-generation, budget, support, restraint, and decay permissions blocked unless explicitly cleared by future readback. | always_required |

## Outputs

- scaffold_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7A_FRESH_CONFIRMATION_SCAFFOLD.json`
- confirmation_requirements: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7A_CONFIRMATION_REQUIREMENTS.csv`
- march_seed_benchmarks: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7A_MARCH_SEED_BENCHMARKS.csv`
- future_window_evaluation_template: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7A_FUTURE_WINDOW_EVALUATION_TEMPLATE.csv`
- run_checklist: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7A_RUN_CHECKLIST.csv`
