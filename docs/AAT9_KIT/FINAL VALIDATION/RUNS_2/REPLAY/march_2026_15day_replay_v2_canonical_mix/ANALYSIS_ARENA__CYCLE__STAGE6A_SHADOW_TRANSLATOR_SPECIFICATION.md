# Analysis Arena Stage 6A Shadow Translator Specification

Purpose: turn Stage 5 readback decisions into a formal shadow translator contract before any replay simulator or scoring rewrite work.

## Metadata
- runs2_dir: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix`
- lane_contract_rows: `7`
- guardrail_rows: `9`
- simulation_requirements: `7`
- acceptance_checks: `8`

## Guardrails
- Stage 6A is read-only and grants no live scoring, candidate-generation, translator, budget, or legacy-infrastructure permission.
- The primary spec seed is restrained candidate-expression behavior, not a blend of every Stage 5 lane.
- Support context is modifier-only; decay/VTRAC is companion-only; low-denominator and restraint rows are retest/calibration lanes.
- Source overlap cannot receive duplicate confirmation credit because Stage 5 overlap ablation did not beat best-source baselines.
- Positive-conversion evidence remains March-led until future/fresh windows repeat the same readback shape.

## Lane Contract
| lane | source modes | permission | role | FP proxy | yield |
| --- | --- | --- | --- | --- | --- |
| primary_restrained_candidate_expression | clean_with_restraint_filter | shadow_spec_only | primary shadow candidate-expression seed | 41.0% | 25.815 |
| secondary_lineage_supported_restrained | clean_lineage_supported_restrained | shadow_spec_only | secondary shadow candidate-expression seed | 40.9% | 23.919 |
| narrowed_lineage_foundation | clean_plus_lineage_deduped | narrow_before_design | broad candidate foundation requiring narrowing | 47.2% | 21.296 |
| support_context_modifier | support_gate_context\|clean_with_support_context | context_modifier_only | paired support/ranking context | 58.1% | 19.317 |
| decay_watch_companion | decay_watch_companion | companion_only | carryforward/territory annotation | 82.5% | 4.382 |
| low_denominator_watchlist | low_denominator_watchlist | retest_before_design | retest/watchlist only | 36.1% | 23.954 |
| restraint_calibration_surface | restraint_retest | penalty_research_only | penalty/veto calibration surface | 59.3% | 16.612 |

## Guardrail Matrix
| guardrail | severity | rule | failure response |
| --- | --- | --- | --- |
| G01_no_live_permission | hard_block | Stage 6A is a shadow specification only. | Stop and redesign as read-only artifact. |
| G02_primary_lane_only_seed | hard_block | Primary spec seed is restrained candidate-expression behavior. | Reject Stage 6B simulator output as blended and rerun with separated lanes. |
| G03_secondary_lineage_dedup | hard_block | Secondary lane must carry lineage de-duplication. | Remove duplicate-credit rows before replay. |
| G04_overlap_no_duplicate_credit | hard_block | Overlap does not receive extra scoring credit unless it beats the best source-side baseline. | Keep overlap as pool narrowing or restraint. |
| G05_support_modifier_only | hard_block | Support context cannot create candidates. | Move support-only rows out of candidate-expression scoring. |
| G06_decay_companion_only | hard_block | Decay/VTRAC territory cannot become boxed or straight spend permission. | Remove decay-driven candidate rows from simulation. |
| G07_restraint_soft_before_hard | design_constraint | Calibrate restraint as penalty/veto pressure before any hard exclusion. | Keep restraint in research-only mode. |
| G08_march_concentration_warning | design_constraint | Positive-conversion metrics are March-led until future/fresh windows repeat the shape. | Do not promote from shadow spec to live rewrite. |
| G09_macro_findings_gate | documentation_gate | Macro Findings Log receives evidence-led findings, not infrastructure milestones. | Keep finding in readback/spec memo only. |

## Stage 6B Simulation Requirements
| requirement | target | metric | pass condition |
| --- | --- | --- | --- |
| S6B-001 | primary_restrained_candidate_expression | false_positive_proxy_rate, pool_normalized_positive_yield, active_state_days | beats clean_boxed_only on false-positive proxy or yield without larger pool explosion |
| S6B-002 | secondary_lineage_supported_restrained | incremental positive conversion versus primary-only; lineage duplicate count | adds value without duplicate-credit inflation |
| S6B-003 | support_context_modifier | support-on versus support-off false-positive proxy and yield | support improves or narrows paired candidate rows; standalone support remains excluded |
| S6B-004 | restraint_calibration_surface | no-penalty versus soft-penalty versus hard-exclusion readback | soft penalty reduces junk without killing useful signal; hard exclusion requires explicit proof |
| S6B-005 | source_a_source_b_overlap | overlap lift versus best source and pool reduction | overlap is treated as narrowing/restraint unless positive lift appears |
| S6B-006 | window_and_state_concentration | positive conversion share by window and state | all shadow outputs carry concentration warnings until repeated on future/fresh windows |
| S6B-007 | decay_watch_companion | annotation coverage and wrong-lane pressure | decay remains excluded from candidate pool metrics |

## Acceptance Checklist
| check | status | requirement |
| --- | --- | --- |
| A01_primary_lane_present | pass | primary restrained candidate-expression lane exists |
| A02_secondary_lane_present | pass | secondary lineage-supported restrained lane exists |
| A03_support_standalone_forbidden | pass | support-only context is forbidden as candidate source |
| A04_decay_spend_forbidden | pass | decay/VTRAC spend permission is blocked |
| A05_overlap_duplicate_credit_blocked | pass | source overlap duplicate-credit is blocked |
| A06_concentration_warning_carried | pass | March-led concentration warning is explicit |
| A07_simulation_requirements_exist | pass | Stage 6B simulation requirements are defined |
| A08_no_live_permission | pass | live scoring/candidate/budget changes are blocked |

## Shadow Spec Queue
| priority | work item | permission | blocked until |
| --- | --- | --- | --- |
| 1 | stage6b_shadow_replay_simulator | read_only_replay | Stage 6A acceptance checklist passes |
| 2 | support_modifier_ablation | read_only_replay | Stage 6B simulator exists |
| 3 | restraint_penalty_calibration | read_only_replay | Stage 6B simulator exists |
| 4 | narrowed_lineage_variant_design | shadow_design_only | primary/secondary simulator baselines exist |
| 5 | macro_findings_review_gate | documentation_only | Stage 6B readback or future/fresh repeat |

## Interpretation
- Stage 6A authorizes a future read-only Stage 6B replay simulator, not live scoring.
- The simulator should test the primary restrained lane first, then secondary lineage-supported restrained behavior, then support/restraint ablations.
- Any Stage 6B output must preserve concentration warnings and lane separation.
- Macro findings should wait for Stage 6B readback or future/fresh repeat evidence.

## Output Files
- md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_TRANSLATOR_SPECIFICATION.md`
- json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_TRANSLATOR_SPECIFICATION.json`
- lane_contract_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6A_LANE_CONTRACT.csv`
- guardrail_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6A_GUARDRAIL_MATRIX.csv`
- simulation_requirements_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6A_SIMULATION_REQUIREMENTS.csv`
- acceptance_checklist_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6A_ACCEPTANCE_CHECKLIST.csv`
- spec_queue_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2_canonical_mix/ANALYSIS_ARENA__CYCLE__STAGE6A_SHADOW_SPEC_QUEUE.csv`
