# Analysis Arena Stage 6B Shadow Replay Simulator

Purpose: replay the Stage 6A shadow translator contract against Stage 5 value-level fixture rows without changing live scoring or candidate generation.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
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
- Primary restrained lane FP proxy: `41.0%` versus baseline `46.6%`.
- Primary restrained lane yield: `25.815` versus baseline `23.978`.
- Stage 6A allowed candidate union rows: `434` with live permission still `none`.
- Stage 6B confirms the next work should remain shadow replay/readback, not live scoring.

## Replay Scenario Scorecard
| scenario | permission | rows | state-days | FP proxy | yield | avg pool |
| --- | --- | --- | --- | --- | --- | --- |
| baseline_clean_boxed | baseline_only | 196 | 28 | 46.6% | 23.978 | 13.107 |
| primary_restrained_candidate_expression | shadow_replay_only | 434 | 19 | 41.0% | 25.815 | 38.737 |
| secondary_lineage_supported_restrained | shadow_replay_only | 410 | 16 | 40.9% | 23.919 | 43.375 |
| stage6a_allowed_candidate_union | shadow_replay_only | 434 | 19 | 41.0% | 25.815 | 38.737 |
| broad_lineage_foundation_reference | reference_only | 1654 | 50 | 47.2% | 21.296 | 62.640 |
| candidate_rows_with_support_context | support_modifier_replay_only | 1581 | 43 | 46.9% | 21.450 | 69.279 |
| candidate_rows_without_support_context | support_ablation_reference | 73 | 11 | 52.3% | 18.301 | 13.909 |
| support_gate_context_excluded | context_only | 3623 | 84 | 58.1% | 19.317 | 102.857 |
| decay_watch_companion_excluded | companion_only | 5475 | 310 | 82.5% | 4.382 | 109.100 |
| low_denominator_watchlist_excluded | retest_only | 168 | 41 | 36.1% | 23.954 | 6.415 |
| restraint_retest_surface_excluded | penalty_research_only | 1235 | 58 | 59.3% | 16.612 | 52.310 |

## Lane Increment Matrix
| comparison | scenario A | scenario B | FP delta | yield delta | pool ratio |
| --- | --- | --- | --- | --- | --- |
| primary_vs_baseline | baseline_clean_boxed | primary_restrained_candidate_expression | -0.056 | 1.837 | 2.955 |
| secondary_vs_primary | primary_restrained_candidate_expression | secondary_lineage_supported_restrained | -0.001 | -1.896 | 1.120 |
| union_vs_primary | primary_restrained_candidate_expression | stage6a_allowed_candidate_union | 0.000 | 0.000 | 1.000 |
| broad_lineage_vs_primary | primary_restrained_candidate_expression | broad_lineage_foundation_reference | 0.062 | -4.519 | 1.617 |
| support_on_vs_support_off | candidate_rows_without_support_context | candidate_rows_with_support_context | -0.054 | 3.149 | 4.981 |
| decay_vs_candidate_union | stage6a_allowed_candidate_union | decay_watch_companion_excluded | 0.415 | -21.433 | 2.816 |

## Support Modifier Ablation
| bucket | permission | rows | FP proxy | yield |
| --- | --- | --- | --- | --- |
| primary_support_on | paired_modifier_replay | 410 | 40.9% | 23.919 |
| primary_support_off | paired_modifier_replay | 24 | 42.9% | 57.143 |
| all_candidate_support_on | paired_modifier_replay | 1581 | 46.9% | 21.450 |
| all_candidate_support_off | paired_modifier_replay | 73 | 52.3% | 18.301 |
| support_gate_standalone_excluded | excluded_context_only | 3623 | 58.1% | 19.317 |

## Restraint Calibration
| bucket | permission | rows | FP proxy | yield |
| --- | --- | --- | --- | --- |
| no_penalty_all_candidate_rows | reference_only | 1654 | 47.2% | 21.296 |
| hard_exclusion_non_high_pressure | shadow_replay_only | 434 | 41.0% | 25.815 |
| removed_high_pressure_candidate_rows | penalty_research_only | 1220 | 49.1% | 19.908 |
| medium_pressure_candidate_rows | penalty_research_only | 434 | 41.0% | 25.815 |
| restraint_retest_surface | penalty_research_only | 1235 | 59.3% | 16.612 |

## Guardrail Compliance
| guardrail | status | evidence |
| --- | --- | --- |
| G01_no_live_permission | pass | Stage 6B writes reports only and never changes live scoring/candidate/budget code. |
| G02_stage6a_acceptance_passed | pass | All Stage 6A acceptance checks must pass before simulation. |
| G03_decay_excluded_from_candidate_union | pass | Allowed candidate union must not include decay/watch lanes. |
| G04_support_only_excluded_from_candidate_union | pass | Allowed candidate union must not include support-only lanes. |
| G05_candidate_union_exists | pass | Allowed primary/secondary candidate union exists. |
| G06_concentration_warning_carried | pass | High window concentration is detected and carried as a warning. |
| G07_no_duplicate_credit_claim | pass | Union scenario is reported as row replay, not source-overlap duplicate scoring credit. |

## Interpretation
- The primary restrained lane improves the baseline false-positive proxy and yield in this fixture replay.
- The secondary lineage-supported lane remains a narrower/reweighted shadow lane, not an expansion with independent credit.
- Support context must be read through paired support-on/off ablation, not as standalone candidate permission.
- High restraint pressure remains penalty research until soft-versus-hard handling is reviewed.
- Stage 6B still carries the March-led concentration warning, so it is not a live rewrite trigger.

## Output Files
- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR.json`
- scenario_scorecard_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_REPLAY_SCENARIO_SCORECARD.csv`
- increment_matrix_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_LANE_INCREMENT_MATRIX.csv`
- support_ablation_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_SUPPORT_MODIFIER_ABLATION.csv`
- restraint_calibration_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_RESTRAINT_CALIBRATION.csv`
- concentration_audit_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_CONCENTRATION_AUDIT.csv`
- guardrail_compliance_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6B_GUARDRAIL_COMPLIANCE.csv`
