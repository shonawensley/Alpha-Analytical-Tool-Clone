# Analysis Arena Stage 7B Fixture Replay Harness

## Guardrail

Stage 7B is read-only. It replays the Stage 6F decision atlas against the Stage 7A fresh-window scaffold. It does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.

## Executive Readback

- queue rows replayed: `12`
- requirement coverage rows: `9`
- blocker recheck rows: `6`
- casebook traceability rows: `0`
- queue readiness counts: `{"blocked_by_requirements": 1, "ready_but_watch": 9, "research_only": 2}`
- requirement coverage counts: `{"blocked_by_requirements": 1, "ready_but_watch": 6, "ready_for_fresh_confirmation": 1, "research_only": 1}`
- blocker recheck counts: `{"ready_but_watch": 2, "ready_for_fresh_confirmation": 4}`
- casebook traceability counts: `{}`
- Fresh-window replay can proceed; scoring rewrite remains blocked until future evidence clears or quarantines the open gates.

## Queue Replay Status

| priority | subject | requirement | lane | status |
| --- | --- | --- | --- | --- |
| 1 | support_context | S7A-REQ-003 | S6F-LANE-004 | ready_but_watch |
| 2 | restraint_filter | S7A-REQ-004 | S6F-LANE-005 | ready_but_watch |
| 3 | broad_lineage_foundation_reference | S7A-REQ-005 | S6F-LANE-003 | ready_but_watch |
| 4 | decay_watch_companion | S7A-REQ-006 | S6F-LANE-006 | research_only |
| 5 | macro_findings_log | S7A-REQ-008 |  | ready_but_watch |
| 6 | translator_scoring_rewrite | S7A-REQ-009 | S6F-LANE-008 | blocked_by_requirements |
| 7 | restraint_pressure_high | S7A-REQ-004 | S6F-LANE-005 | ready_but_watch |
| 8 | high_pressure_rescue_candidates | S7A-REQ-004 | S6F-LANE-005 | ready_but_watch |
| 9 | restraint_soft_penalty | S7A-REQ-004 | S6F-LANE-005 | ready_but_watch |
| 10 | narrow_support_modifier_candidates | S7A-REQ-003 | S6F-LANE-004 | ready_but_watch |
| 11 | support_on_failure_modes | S7A-REQ-003 | S6F-LANE-004 | research_only |
| 12 | support_modifier_boundary | S7A-REQ-003 | S6F-LANE-004 | ready_but_watch |

## Requirement Coverage

| requirement | target | queue_count | lane | status |
| --- | --- | --- | --- | --- |
| S7A-REQ-001 | primary_restrained_candidate_expression | 0 | S6F-LANE-001 | ready_for_fresh_confirmation |
| S7A-REQ-002 | concentration_warning_break | 0 |  | ready_but_watch |
| S7A-REQ-003 | support_context_modifier | 4 | S6F-LANE-004 | ready_but_watch |
| S7A-REQ-004 | restraint_soft_penalty | 4 | S6F-LANE-005 | ready_but_watch |
| S7A-REQ-005 | lineage_narrowing | 1 | S6F-LANE-003 | ready_but_watch |
| S7A-REQ-006 | decay_companion_boundary | 1 | S6F-LANE-006 | research_only |
| S7A-REQ-007 | duplicate_credit_guardrail | 0 | S6F-LANE-007 | ready_but_watch |
| S7A-REQ-008 | macro_findings_gate | 1 |  | ready_but_watch |
| S7A-REQ-009 | translator_scoring_rewrite_gate | 1 | S6F-LANE-008 | blocked_by_requirements |

## Blocker Recheck

| blocker | requirement | blocks | status |
| --- | --- | --- | --- |
| rewrite_blocker_primary_repeat | S7A-REQ-001 | primary_restrained_candidate_expression | ready_for_fresh_confirmation |
| rewrite_blocker_concentration | S7A-REQ-002 | concentration_warning_break | ready_for_fresh_confirmation |
| rewrite_blocker_support_modifier | S7A-REQ-003 | support_context_modifier | ready_for_fresh_confirmation |
| rewrite_blocker_restraint_soft_before_hard | S7A-REQ-004 | restraint_soft_penalty | ready_for_fresh_confirmation |
| rewrite_blocker_duplicate_credit | S7A-REQ-007 | duplicate_credit_guardrail | ready_but_watch |
| rewrite_blocker_decay_boundary | S7A-REQ-006 | decay_companion_boundary | ready_but_watch |

## Highest-Priority Casebook Traceability

| target | candidate | requirement | examples | status |
| --- | --- | --- | --- | --- |

## Fresh-Window Operating Readback

- Ready or watch-list queue items: `9`
- Blocked queue items: `1`
- Worst requirement status: `blocked_by_requirements`
- Worst casebook status: `missing`
- Operational meaning: use Stage 7B as the pre-flight map for the next fresh window. Do not use it as permission to rewrite scoring.

## Outputs

- harness_json: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7B_FIXTURE_REPLAY_HARNESS.json`
- queue_replay_status: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7B_QUEUE_REPLAY_STATUS.csv`
- requirement_coverage: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7B_REQUIREMENT_COVERAGE.csv`
- blocker_recheck: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7B_BLOCKER_RECHECK.csv`
- casebook_traceability: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7B_CASEBOOK_TRACEABILITY.csv`
- ready_for_fresh_window: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/ANALYSIS_ARENA__CYCLE__STAGE7B_READY_FOR_FRESH_WINDOW.md`
