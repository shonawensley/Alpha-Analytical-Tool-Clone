# Stage 7B Ready-For-Fresh-Window Readback

## Bottom Line

The next fresh window is ready for read-only confirmation replay, not for live scoring or candidate-generation changes.

## Replay Permissions

- `ready_for_fresh_confirmation`: 0 queue item(s)
- `ready_but_watch`: 9 queue item(s)
- `research_only`: 2 queue item(s)
- `needs_replay_evidence`: 0 queue item(s)
- `blocked_by_requirements`: 1 queue item(s)
- casebook watch targets: 17

## Allowed Next Action

Run the next fresh-window cadence, then rerun Stage 6B through Stage 7B and compare these March seed statuses against the future evidence.

## Explicitly Not Allowed

- No live scoring rewrite.
- No candidate-generation rewrite.
- No budget rewrite.
- No hard restraint veto.
- No broad support promotion.
- No decay conversion into candidate-pool spend evidence.

## First Items To Inspect After Fresh Window

| priority | subject | requirement | status |
| --- | --- | --- | --- |
| 1 | support_context | S7A-REQ-003 | ready_but_watch |
| 2 | restraint_filter | S7A-REQ-004 | ready_but_watch |
| 3 | broad_lineage_foundation_reference | S7A-REQ-005 | ready_but_watch |
| 5 | macro_findings_log | S7A-REQ-008 | ready_but_watch |
| 7 | restraint_pressure_high | S7A-REQ-004 | ready_but_watch |
| 8 | high_pressure_rescue_candidates | S7A-REQ-004 | ready_but_watch |
| 9 | restraint_soft_penalty | S7A-REQ-004 | ready_but_watch |
| 10 | narrow_support_modifier_candidates | S7A-REQ-003 | ready_but_watch |
| 12 | support_modifier_boundary | S7A-REQ-003 | ready_but_watch |

## Blockers That Must Stay Visible

| blocker | requirement | fresh test |
| --- | --- | --- |
| rewrite_blocker_primary_repeat | S7A-REQ-001 | Repeat Stage 6B replay/readback on a fresh window and compare primary against the baseline clean boxed arm. |
| rewrite_blocker_concentration | S7A-REQ-002 | Carry window/state concentration flags into the fresh run and require the finding to survive outside the March window. |
| rewrite_blocker_support_modifier | S7A-REQ-003 | Retest support-on only as a narrower paired modifier, never as broad positive expansion. |
| rewrite_blocker_restraint_soft_before_hard | S7A-REQ-004 | Convert hard-exclusion evidence into soft-penalty simulations and test whether high-pressure rows can be downweighted without losing useful conversions. |
| rewrite_blocker_duplicate_credit | S7A-REQ-007 | Verify union replay never double-counts primary and secondary lineage-supported rows. |
| rewrite_blocker_decay_boundary | S7A-REQ-006 | Keep decay evidence separate from candidate-pool scoring and repeat the boundary check in future windows. |

## Requirement Coverage Snapshot

| requirement | target | status | note |
| --- | --- | --- | --- |
| S7A-REQ-001 | primary_restrained_candidate_expression | ready_for_fresh_confirmation | primary confirmation target is testable; active_blockers=1 |
| S7A-REQ-002 | concentration_warning_break | ready_but_watch | testable with caveats; queue_paths=0; active_blockers=1 |
| S7A-REQ-003 | support_context_modifier | ready_but_watch | testable with caveats; queue_paths=4; active_blockers=1 |
| S7A-REQ-004 | restraint_soft_penalty | ready_but_watch | testable with caveats; queue_paths=4; active_blockers=1 |
| S7A-REQ-005 | lineage_narrowing | ready_but_watch | testable with caveats; queue_paths=1; active_blockers=0 |
| S7A-REQ-006 | decay_companion_boundary | research_only | boundary/context evidence must remain separate from candidate-pool scoring |
| S7A-REQ-007 | duplicate_credit_guardrail | ready_but_watch | testable with caveats; queue_paths=0; active_blockers=1 |
| S7A-REQ-008 | macro_findings_gate | ready_but_watch | testable with caveats; queue_paths=1; active_blockers=0 |
| S7A-REQ-009 | translator_scoring_rewrite_gate | blocked_by_requirements | rewrite/live permission remains blocked or required scaffold pieces are incomplete |
