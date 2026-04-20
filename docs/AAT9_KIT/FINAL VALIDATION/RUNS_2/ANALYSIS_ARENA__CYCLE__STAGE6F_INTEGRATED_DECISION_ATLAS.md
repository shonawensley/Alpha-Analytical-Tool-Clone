# Analysis Arena Stage 6F Integrated Decision Atlas

## Guardrail

Stage 6F is read-only. It integrates Stage 6B through Stage 6E evidence into decision, blocker, queue, macro, and casebook artifacts. It does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- Primary restrained candidate expression remains the strongest current design seed, but Stage 6C future/fresh confirmation is still required.
- Restraint evidence is promising as soft-penalty research, not hard-veto permission.
- Support evidence remains broad-failed but narrow-candidate-positive in selected paired buckets.
- Rewrite remains blocked until fresh-window confirmation clears or quarantines the open gates.

## Lane Decision Atlas

| lane_id | lane_type | current_status | decision_posture | permission |
| --- | --- | --- | --- | --- |
| S6F-LANE-001 | primary_candidate_expression | future_window_confirmation_required | strongest_current_seed_but_future_confirmation_required | readback_only_no_live_permission |
| S6F-LANE-002 | secondary_lineage_modifier | keep_as_lineage_modifier_retest | modifier_only_not_independent_expansion | modifier_research_only |
| S6F-LANE-003 | broad_lineage_reference | narrow_before_design | blocked_until_narrowed | narrowing_research_only |
| S6F-LANE-004 | support_modifier_narrowing | fail_as_positive_modifier | 3 strict support candidates; 2 mixed retest candidates; broad support remains blocked | support_research_only |
| S6F-LANE-005 | restraint_soft_penalty | pass_research_not_live | 3 rescue buckets; 13 downweight buckets; hard veto remains blocked | penalty_research_only |
| S6F-LANE-006 | decay_companion_boundary | companion_only | companion_only_boundary_confirmed_for_now | companion_only |
| S6F-LANE-007 | duplicate_credit_guardrail | pass | mandatory_guardrail | readback_reference_only |
| S6F-LANE-008 | rewrite_gate | active_blocker | rewrite_not_allowed_yet | blocked_until_future_confirmation |

## Active Blockers

| blocker_id | blocks | clearance_condition |
| --- | --- | --- |
| rewrite_blocker_primary_repeat | primary_restrained_candidate_expression | Pass on at least one future/fresh window for continued research; prefer two independent fresh confirmations before rewrite spec. |
| rewrite_blocker_concentration | concentration_warning_break | At least one non-March fresh window, preferably two. |
| rewrite_blocker_support_modifier | support_context_modifier | Must pass narrowed-bucket evidence before entering any scoring rewrite. |
| rewrite_blocker_restraint_soft_before_hard | restraint_soft_penalty | Soft-penalty workbench must show stable calibration before rewrite design. |
| rewrite_blocker_duplicate_credit | duplicate_credit_guardrail | Required every Stage 6B replay/readback. |
| rewrite_blocker_decay_boundary | decay_companion_boundary | Boundary must remain explicit in every fresh-window readback. |

## Priority Casebook Targets

| target_id | source_stage | candidate | positive | yield | interpretation |
| --- | --- | --- | --- | --- | --- |
| S6F-TARGET-001 | Stage6D | S6D-RESCUE-012 | 50 | 18.382 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-002 | Stage6D | S6D-RESCUE-015 | 39 | 18.571 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-003 | Stage6D | S6D-RESCUE-016 | 39 | 18.571 | priority_restraint_rescue_casebook; inspect before globally downweighting high pressure |
| S6F-TARGET-004 | Stage6D | S6D-RESCUE-001 | 502 | 12.550 | research_casebook_review_only |
| S6F-TARGET-005 | Stage6D | S6D-RESCUE-002 | 502 | 12.550 | research_casebook_review_only |
| S6F-TARGET-006 | Stage6D | S6D-RESCUE-003 | 494 | 12.456 | research_casebook_review_only |
| S6F-TARGET-007 | Stage6D | S6D-RESCUE-004 | 294 | 12.312 | research_casebook_review_only |
| S6F-TARGET-008 | Stage6D | S6D-RESCUE-005 | 286 | 12.150 | research_casebook_review_only |
| S6F-TARGET-009 | Stage6D | S6D-RESCUE-006 | 208 | 12.903 | research_casebook_review_only |
| S6F-TARGET-010 | Stage6D | S6D-RESCUE-007 | 208 | 12.903 | research_casebook_review_only |
| S6F-TARGET-011 | Stage6D | S6D-RESCUE-008 | 79 | 13.036 | research_casebook_review_only |
| S6F-TARGET-012 | Stage6D | S6D-RESCUE-009 | 76 | 10.674 | research_casebook_review_only |
| S6F-TARGET-013 | Stage6E | S6E-SUPPORT-001 | 98 | 15.409 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-014 | Stage6E | S6E-SUPPORT-002 | 81 | 15.458 | priority_support_narrowing_casebook; requires fresh-window repeat |
| S6F-TARGET-015 | Stage6E | S6E-SUPPORT-003 | 29 | 13.426 | priority_support_narrowing_casebook; requires fresh-window repeat |

## Macro Findings Disposition

| finding_id | disposition | promotion_condition |
| --- | --- | --- |
| S6B-MF-001 | hold_for_fresh_confirmation | repeat on future/fresh window or explicit review note with caveats |
| S6B-MF-002 | hold_for_fresh_confirmation | repeat on future/fresh window or explicit review note with caveats |
| S6B-MF-003 | hold_for_fresh_confirmation | repeat on future/fresh window or explicit review note with caveats |
| S6B-MF-004 | hold_for_fresh_confirmation | repeat on future/fresh window or explicit review note with caveats |

## Outputs

- atlas_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_INTEGRATED_DECISION_ATLAS.json`
- lane_decision_atlas: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_LANE_DECISION_ATLAS.csv`
- active_blockers: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_ACTIVE_BLOCKERS_AND_CLEARANCE.csv`
- fresh_window_queue: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_FRESH_WINDOW_CARRY_FORWARD_QUEUE.csv`
- macro_findings_disposition: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_MACRO_FINDINGS_DISPOSITION.csv`
- priority_bucket_casebook_md: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_PRIORITY_BUCKET_CASEBOOK.md`
- priority_bucket_casebook_csv: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_PRIORITY_BUCKET_CASEBOOK.csv`
- bucket_example_ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6F_BUCKET_EXAMPLE_LEDGER.csv`
