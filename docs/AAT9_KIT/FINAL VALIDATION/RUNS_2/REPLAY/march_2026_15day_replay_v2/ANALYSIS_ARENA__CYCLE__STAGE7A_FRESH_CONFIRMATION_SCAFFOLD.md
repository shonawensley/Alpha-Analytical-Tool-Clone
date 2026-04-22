# Analysis Arena Stage 7A Fresh Confirmation Scaffold

## Guardrail

Stage 7A is read-only. It prepares future/fresh-window evaluation rows from Stage 6C and Stage 6F evidence; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- confirmation requirements: `9`
- March seed benchmarks: `5`
- future-window template rows: `14`
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
| S7A-BENCH-001 | stage6b_scenario | baseline_clean_boxed | fp=0.0%; yield=0.000; positive=0; state_days=0 |
| S7A-BENCH-002 | stage6b_scenario | primary_restrained_candidate_expression | fp=0.0%; yield=0.000; positive=0; state_days=0 |
| S7A-BENCH-003 | stage6b_scenario | secondary_lineage_supported_restrained | fp=0.0%; yield=0.000; positive=0; state_days=0 |
| S7A-BENCH-004 | stage6b_scenario | broad_lineage_foundation_reference | fp=0.0%; yield=0.000; positive=0; state_days=0 |
| S7A-BENCH-005 | stage6b_scenario | decay_watch_companion_excluded | fp=83.4%; yield=8.643; positive=1490; state_days=145 |

## Run Checklist

| step | check | status |
| --- | --- | --- |
| 1 | Run normal fresh-window cadence and close the window artifacts. | pending_future_window |
| 2 | Run Stage 3 through Stage 6B readback on the fresh evidence. | pending_future_window |
| 3 | Run Stage 6C, Stage 6D, Stage 6E, and Stage 6F on the fresh evidence. | pending_future_window |
| 4 | Evaluate 9 Stage 7A confirmation requirements against the future window. | pending_future_window |
| 5 | Keep live scoring, candidate-generation, budget, support, restraint, and decay permissions blocked unless explicitly cleared by future readback. | always_required |

## Outputs

- scaffold_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7A_FRESH_CONFIRMATION_SCAFFOLD.json`
- confirmation_requirements: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7A_CONFIRMATION_REQUIREMENTS.csv`
- march_seed_benchmarks: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7A_MARCH_SEED_BENCHMARKS.csv`
- future_window_evaluation_template: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7A_FUTURE_WINDOW_EVALUATION_TEMPLATE.csv`
- run_checklist: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7A_RUN_CHECKLIST.csv`
