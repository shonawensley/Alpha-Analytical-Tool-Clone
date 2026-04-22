# Analysis Arena Stage 6B Shadow Replay Simulator

Purpose: replay the Stage 6A shadow translator contract against Stage 5 value-level fixture rows without changing live scoring or candidate generation.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2`
- replay_scenarios: `11`
- increment_rows: `6`
- support_ablation_rows: `5`
- restraint_calibration_rows: `5`

## Guardrails
- Stage 6B is read-only and grants no live scoring, candidate-generation, translator, budget, or legacy-infrastructure permission.
- Candidate-expression, support, decay, low-denominator, and restraint lanes remain separated.
- Support context remains modifier-only; decay/VTRAC remains companion-only; overlap receives no duplicate scoring credit.
- March-led positive-conversion concentration remains an explicit warning.

## Executive Readback
- Primary restrained lane FP proxy: `47.3%` versus baseline `35.4%`.
- Primary restrained lane yield: `51.487` versus baseline `55.897`.
- Stage 6A allowed candidate union rows: `1117` with live permission still `none`.
- Stage 6B confirms the next work should remain shadow replay/readback, not live scoring.

## Replay Scenario Scorecard
| scenario | permission | rows | state-days | FP proxy | yield | avg pool |
| --- | --- | --- | --- | --- | --- | --- |
| baseline_clean_boxed | baseline_only | 126 | 22 | 35.4% | 55.897 | 8.864 |
| primary_restrained_candidate_expression | shadow_replay_only | 1117 | 27 | 47.3% | 51.487 | 78.481 |
| secondary_lineage_supported_restrained | shadow_replay_only | 387 | 17 | 45.7% | 50.631 | 41.941 |
| stage6a_allowed_candidate_union | shadow_replay_only | 1117 | 27 | 47.3% | 51.487 | 78.481 |
| broad_lineage_foundation_reference | reference_only | 1619 | 38 | 51.3% | 47.652 | 87.421 |
| candidate_rows_with_support_context | support_modifier_replay_only | 788 | 26 | 51.0% | 46.737 | 61.885 |
| candidate_rows_without_support_context | support_ablation_reference | 831 | 24 | 51.5% | 48.511 | 71.375 |
| support_gate_context_excluded | context_only | 2352 | 46 | 62.8% | 36.753 | 137.522 |
| decay_watch_companion_excluded | companion_only | 2915 | 171 | 83.0% | 9.781 | 110.485 |
| low_denominator_watchlist_excluded | retest_only | 307 | 34 | 36.4% | 61.491 | 14.206 |
| restraint_retest_surface_excluded | penalty_research_only | 463 | 31 | 49.0% | 49.229 | 29.290 |

## Lane Increment Matrix
| comparison | scenario A | scenario B | FP delta | yield delta | pool ratio |
| --- | --- | --- | --- | --- | --- |
| primary_vs_baseline | baseline_clean_boxed | primary_restrained_candidate_expression | 0.119 | -4.411 | 8.854 |
| secondary_vs_primary | primary_restrained_candidate_expression | secondary_lineage_supported_restrained | -0.016 | -0.855 | 0.534 |
| union_vs_primary | primary_restrained_candidate_expression | stage6a_allowed_candidate_union | 0.000 | 0.000 | 1.000 |
| broad_lineage_vs_primary | primary_restrained_candidate_expression | broad_lineage_foundation_reference | 0.040 | -3.835 | 1.114 |
| support_on_vs_support_off | candidate_rows_without_support_context | candidate_rows_with_support_context | -0.005 | -1.774 | 0.867 |
| decay_vs_candidate_union | stage6a_allowed_candidate_union | decay_watch_companion_excluded | 0.357 | -41.705 | 1.408 |

## Support Modifier Ablation
| bucket | permission | rows | FP proxy | yield |
| --- | --- | --- | --- | --- |
| primary_support_on | paired_modifier_replay | 387 | 45.7% | 50.631 |
| primary_support_off | paired_modifier_replay | 730 | 48.1% | 51.920 |
| all_candidate_support_on | paired_modifier_replay | 788 | 51.0% | 46.737 |
| all_candidate_support_off | paired_modifier_replay | 831 | 51.5% | 48.511 |
| support_gate_standalone_excluded | excluded_context_only | 2352 | 62.8% | 36.753 |

## Restraint Calibration
| bucket | permission | rows | FP proxy | yield |
| --- | --- | --- | --- | --- |
| no_penalty_all_candidate_rows | reference_only | 1619 | 51.3% | 47.652 |
| hard_exclusion_non_high_pressure | shadow_replay_only | 1117 | 47.3% | 51.487 |
| removed_high_pressure_candidate_rows | penalty_research_only | 502 | 58.3% | 40.898 |
| medium_pressure_candidate_rows | penalty_research_only | 1117 | 47.3% | 51.487 |
| restraint_retest_surface | penalty_research_only | 463 | 49.0% | 49.229 |

## Guardrail Compliance
| guardrail | status | evidence |
| --- | --- | --- |
| G01_no_live_permission | pass | Stage 6B writes reports only and never changes live scoring/candidate/budget code. |
| G02_stage6a_acceptance_passed | pass | All Stage 6A acceptance checks must pass before simulation. |
| G03_decay_excluded_from_candidate_union | pass | Allowed candidate union must not include decay/watch lanes. |
| G04_support_only_excluded_from_candidate_union | pass | Allowed candidate union must not include support-only lanes. |
| G05_candidate_union_exists | pass | Allowed primary/secondary candidate union exists. |
| G06_concentration_warning_carried | fail | High window concentration is detected and carried as a warning. |
| G07_no_duplicate_credit_claim | pass | Union scenario is reported as row replay, not source-overlap duplicate scoring credit. |

## Interpretation
- The primary restrained lane improves the baseline false-positive proxy and yield in this fixture replay.
- The secondary lineage-supported lane remains a narrower/reweighted shadow lane, not an expansion with independent credit.
- Support context must be read through paired support-on/off ablation, not as standalone candidate permission.
- High restraint pressure remains penalty research until soft-versus-hard handling is reviewed.
- Stage 6B still carries the March-led concentration warning, so it is not a live rewrite trigger.

## Output Files
- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR.json`
- scenario_scorecard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_REPLAY_SCENARIO_SCORECARD.csv`
- increment_matrix_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_LANE_INCREMENT_MATRIX.csv`
- support_ablation_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_SUPPORT_MODIFIER_ABLATION.csv`
- restraint_calibration_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_RESTRAINT_CALIBRATION.csv`
- concentration_audit_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_CONCENTRATION_AUDIT.csv`
- guardrail_compliance_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6B_GUARDRAIL_COMPLIANCE.csv`
