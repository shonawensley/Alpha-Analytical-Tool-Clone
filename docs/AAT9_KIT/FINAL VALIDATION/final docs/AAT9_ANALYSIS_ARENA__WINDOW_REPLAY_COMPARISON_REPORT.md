# Analysis Arena Window Replay Comparison Report

## 1. Verdict

- run_label: `march_2026_15day_replay_v2`
- evidence_tier: `same_window_replay`
- comparison_status: `review_required_before_interpretation`
- total_targets: `26`
- stage8_permission: `blocked`
- candidate_completeness: `candidate_complete`
- missing_required_candidate_targets: `0`

Category counts:

- `unchanged`: `11`
- `improved_traceability`: `6`
- `newly_exposed`: `0`
- `degraded`: `5`
- `contradicted`: `4`
- `renamed_or_reclassified_only`: `0`
- `blocked_by_missing_data`: `0`

## 2. Compared Roots

- baseline_window_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- candidate_window_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23`
- baseline_cycle_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`
- candidate_cycle_root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2`

Durable references:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`

## 3. Target Matrix

| Target | Layer | Category | Status | Baseline | Candidate |
|---|---|---|---|---|---|
| `window_performance_gap` | `window_close` | `unchanged` | `summary_fields_match` | `true` | `true` |
| `window_deep_hit_analysis` | `window_close` | `unchanged` | `summary_fields_match` | `true` | `true` |
| `window_frontier_harness` | `window_close` | `unchanged` | `summary_fields_match` | `true` | `true` |
| `window_pure_finalist_scorecard` | `window_close` | `unchanged` | `summary_fields_match` | `true` | `true` |
| `window_translator_ledger` | `window_close` | `unchanged` | `summary_fields_match` | `true` | `true` |
| `window_deep_analysis` | `window_close` | `unchanged` | `summary_fields_match` | `true` | `true` |
| `window_decay_carryover` | `window_close` | `unchanged` | `summary_fields_match` | `true` | `true` |
| `window_stage2b_stack_scorecard` | `post_run_audit` | `unchanged` | `summary_fields_match` | `true` | `true` |
| `window_stage3_casebook` | `post_run_audit` | `unchanged` | `hash_match` | `true` | `true` |
| `stage6b_scenario_scorecard` | `stage6b` | `improved_traceability` | `material_metric_or_evidence_changed` | `true` | `true` |
| `stage6b_lane_increment` | `stage6b` | `improved_traceability` | `material_metric_or_evidence_changed` | `true` | `true` |
| `stage6b_guardrail_compliance` | `stage6b` | `contradicted` | `material_status_or_decision_changed` | `true` | `true` |
| `stage6b_readback_scenario_decisions` | `stage6b_readback` | `contradicted` | `material_status_or_decision_changed` | `true` | `true` |
| `stage6b_readback_requirement_results` | `stage6b_readback` | `contradicted` | `material_status_or_decision_changed` | `true` | `true` |
| `stage6c_confirmation_tests` | `stage6c` | `improved_traceability` | `material_metric_or_evidence_changed` | `true` | `true` |
| `stage6c_rewrite_blockers` | `stage6c` | `improved_traceability` | `material_metric_or_evidence_changed` | `true` | `true` |
| `stage6d_restraint_bucket_scorecard` | `stage6d` | `degraded` | `candidate_lost_baseline_rows` | `true` | `true` |
| `stage6e_support_bucket_scorecard` | `stage6e` | `degraded` | `candidate_lost_baseline_rows` | `true` | `true` |
| `stage6f_lane_decision_atlas` | `stage6f` | `contradicted` | `material_status_or_decision_changed` | `true` | `true` |
| `stage6f_active_blockers` | `stage6f` | `unchanged` | `row_signatures_match` | `true` | `true` |
| `stage6f_carry_forward_queue` | `stage6f` | `degraded` | `candidate_lost_baseline_rows` | `true` | `true` |
| `stage7a_confirmation_requirements` | `stage7a` | `improved_traceability` | `material_metric_or_evidence_changed` | `true` | `true` |
| `stage7a_march_seed_benchmarks` | `stage7a` | `degraded` | `candidate_lost_baseline_rows` | `true` | `true` |
| `stage7b_queue_replay_status` | `stage7b` | `degraded` | `candidate_lost_baseline_rows` | `true` | `true` |
| `stage7b_requirement_coverage` | `stage7b` | `unchanged` | `row_signatures_match` | `true` | `true` |
| `stage7b_blocker_recheck` | `stage7b` | `improved_traceability` | `material_metric_or_evidence_changed` | `true` | `true` |

## 4. Candidate Completeness

- status: `candidate_complete`
- required_target_count: `23`
- missing_required_candidate_target_count: `0`
- missing_required_baseline_target_count: `0`

Missing required candidate targets:

- none

## 5. Allowed Conclusions

- regression behavior, before-after differences, deterministic replay checks, traceability changes

## 6. Blocked Conclusions

- no fresh confirmation, no Stage 8A unlock, no live scoring/candidate/budget replacement
- This report does not run a window and does not grant Stage 8 permission.
- Same-window replay and archived-window replication cannot replace true fresh-window confirmation.

## 7. Next Use

- Review any `contradicted` or `degraded` rows manually first.
- Treat `improved_traceability` as development evidence, not fresh confirmation.
- Use only true fresh confirmation for Stage 8A consideration.
