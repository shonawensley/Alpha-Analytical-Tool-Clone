# Analysis Arena Stage 6C Future Confirmation Protocol

## Guardrail

Stage 6C is read-only. It creates confirmation contracts and queue items for future windows; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- Stage 6B produced a promising primary restrained candidate expression, but Stage 6C treats it as provisional until future/fresh-window confirmation exists.
- Support, restraint, lineage, decay, duplicate-credit, and macro-findings gates remain separate so one favorable aggregate does not silently become a live rule.
- The translator/scoring rewrite remains blocked until the confirmation matrix is rerun against fresh evidence and its blockers are cleared or explicitly quarantined.

## Confirmation Matrix

| test_id | target | fresh_window_test | pass_threshold | live_permission |
| --- | --- | --- | --- | --- |
| S6C-001 | primary_restrained_candidate_expression | Repeat Stage 6B replay/readback on a fresh window and compare primary against the baseline clean boxed arm. | false_positive_proxy_rate_delta <= -0.050; pool_normalized_positive_yield_delta > 0; avg_pool_ratio_b_vs_a <= 1.500; positive conversions remain non-trivial. | none |
| S6C-002 | concentration_warning_break | Carry window/state concentration flags into the fresh run and require the finding to survive outside the March window. | Primary can pass with warnings only if metrics repeat and concentration warnings are explicit; concentration alone cannot confirm a macro finding. | none |
| S6C-003 | support_context_modifier | Retest support-on only as a narrower paired modifier, never as broad positive expansion. | support-on subset must reduce FP proxy or improve yield versus support-off peer while not materially expanding pool exposure. | none |
| S6C-004 | restraint_soft_penalty | Convert hard-exclusion evidence into soft-penalty simulations and test whether high-pressure rows can be downweighted without losing useful conversions. | soft penalty must reduce FP pressure versus no-penalty reference while preserving materially useful positive conversions; hard veto is forbidden at this stage. | none |
| S6C-005 | lineage_narrowing | Retest narrowed lineage variants; do not promote broad lineage foundation directly. | narrowed lineage must improve or preserve FP/yield versus primary while adding non-duplicate conversions. | none |
| S6C-006 | decay_companion_boundary | Keep decay evidence separate from candidate-pool scoring and repeat the boundary check in future windows. | decay remains companion-only; no candidate permission even when carrying useful explanatory hits. | none |
| S6C-007 | duplicate_credit_guardrail | Verify union replay never double-counts primary and secondary lineage-supported rows. | candidate union must not claim duplicate scoring credit. | none |
| S6C-008 | macro_findings_gate | No macro finding becomes confirmed without future/fresh repeat or explicit human review note. | repeat evidence exists and caveats are logged. | none |
| S6C-009 | translator_scoring_rewrite_gate | Rewrite discussion opens only after S6C primary repeat, duplicate-credit, concentration, support, restraint, and decay gates are cleanly resolved. | all prerequisite gates pass or remain explicitly quarantined. | none |

## Active Rewrite Blockers

| blocker_id | status | clearance_condition |
| --- | --- | --- |
| rewrite_blocker_primary_repeat | active_blocker | Pass on at least one future/fresh window for continued research; prefer two independent fresh confirmations before rewrite spec. |
| rewrite_blocker_concentration | active_blocker | At least one non-March fresh window, preferably two. |
| rewrite_blocker_support_modifier | active_blocker | Must pass narrowed-bucket evidence before entering any scoring rewrite. |
| rewrite_blocker_restraint_soft_before_hard | active_blocker | Soft-penalty workbench must show stable calibration before rewrite design. |
| rewrite_blocker_duplicate_credit | active_blocker | Required every Stage 6B replay/readback. |
| rewrite_blocker_decay_boundary | active_blocker | Boundary must remain explicit in every fresh-window readback. |

## Fresh Window Queue

| priority | queue_item | subject | acceptance_test |
| --- | --- | --- | --- |
| 1 | support_modifier_rework | support_context | Retest support-on only as a narrower paired modifier, never as broad positive expansion. |
| 2 | restraint_soft_penalty_calibration | restraint_filter | Convert hard-exclusion evidence into soft-penalty simulations and test whether high-pressure rows can be downweighted without losing useful conversions. |
| 3 | lineage_narrowing | broad_lineage_foundation_reference | Retest narrowed lineage variants; do not promote broad lineage foundation directly. |
| 4 | decay_companion_boundary | decay_watch_companion | Keep decay evidence separate from candidate-pool scoring and repeat the boundary check in future windows. |
| 5 | macro_findings_gate | macro_findings_log | No macro finding becomes confirmed without future/fresh repeat or explicit human review note. |
| 6 | rewrite_block | translator_scoring_rewrite | Rewrite discussion opens only after S6C primary repeat, duplicate-credit, concentration, support, restraint, and decay gates are cleanly resolved. |

## Macro Gate

| finding_id | disposition | promotion_condition |
| --- | --- | --- |
| S6B-MF-001 | hold_for_fresh_confirmation | repeat on future/fresh window or explicit review note with caveats |
| S6B-MF-002 | hold_for_fresh_confirmation | repeat on future/fresh window or explicit review note with caveats |
| S6B-MF-003 | hold_for_fresh_confirmation | repeat on future/fresh window or explicit review note with caveats |
| S6B-MF-004 | hold_for_fresh_confirmation | repeat on future/fresh window or explicit review note with caveats |

## Outputs

- protocol_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6C_FUTURE_CONFIRMATION_PROTOCOL.json`
- confirmation_test_matrix: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6C_CONFIRMATION_TEST_MATRIX.csv`
- threshold_contract: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6C_THRESHOLD_CONTRACT.csv`
- fresh_window_queue: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6C_FRESH_WINDOW_QUEUE.csv`
- rewrite_blockers: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6C_REWRITE_BLOCKERS.csv`
- macro_review_gate: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE6C_MACRO_REVIEW_GATE.csv`
