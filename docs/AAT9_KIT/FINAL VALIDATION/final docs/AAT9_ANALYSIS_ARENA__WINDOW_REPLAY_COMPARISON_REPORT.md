# Analysis Arena Window Replay Comparison Report

## 1. Verdict

- run_label: `march_2026_15day_replay_v2_pending`
- evidence_tier: `same_window_replay`
- comparison_status: `baseline_preserved_candidate_pending`
- total_targets: `26`
- stage8_permission: `blocked`

Category counts:

- `unchanged`: `0`
- `improved_traceability`: `0`
- `newly_exposed`: `0`
- `degraded`: `0`
- `contradicted`: `0`
- `renamed_or_reclassified_only`: `0`
- `blocked_by_missing_data`: `26`

## 2. Compared Roots

- baseline_window_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- candidate_window_root: `not_provided`
- baseline_cycle_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- candidate_cycle_root: `not_provided`

Durable references:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`

## 3. Target Matrix

| Target | Layer | Category | Status | Baseline | Candidate |
|---|---|---|---|---|---|
| `window_performance_gap` | `window_close` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `window_deep_hit_analysis` | `window_close` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `window_frontier_harness` | `window_close` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `window_pure_finalist_scorecard` | `window_close` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `window_translator_ledger` | `window_close` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `window_deep_analysis` | `window_close` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `window_decay_carryover` | `window_close` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `window_stage2b_stack_scorecard` | `post_run_audit` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `window_stage3_casebook` | `post_run_audit` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6b_scenario_scorecard` | `stage6b` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6b_lane_increment` | `stage6b` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6b_guardrail_compliance` | `stage6b` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6b_readback_scenario_decisions` | `stage6b_readback` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6b_readback_requirement_results` | `stage6b_readback` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6c_confirmation_tests` | `stage6c` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6c_rewrite_blockers` | `stage6c` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6d_restraint_bucket_scorecard` | `stage6d` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6e_support_bucket_scorecard` | `stage6e` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6f_lane_decision_atlas` | `stage6f` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6f_active_blockers` | `stage6f` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage6f_carry_forward_queue` | `stage6f` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage7a_confirmation_requirements` | `stage7a` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage7a_march_seed_benchmarks` | `stage7a` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage7b_queue_replay_status` | `stage7b` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage7b_requirement_coverage` | `stage7b` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |
| `stage7b_blocker_recheck` | `stage7b` | `blocked_by_missing_data` | `candidate_not_provided` | `true` | `false` |

## 4. Allowed Conclusions

- baseline preservation, target inventory, and rerun planning only

## 5. Blocked Conclusions

- no fresh confirmation, no Stage 8A unlock, no live scoring/candidate/budget replacement
- This report does not run a window and does not grant Stage 8 permission.
- Same-window replay and archived-window replication cannot replace true fresh-window confirmation.

## 6. Next Use

- Preserve the baseline root before any rerun.
- Choose a separate rerun output namespace or run label.
- Re-run this comparison with candidate roots after the rerun exists.
