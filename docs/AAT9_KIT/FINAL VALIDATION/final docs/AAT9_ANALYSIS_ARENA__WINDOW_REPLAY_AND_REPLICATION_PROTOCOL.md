# AAT9 Analysis Arena - Window Replay And Replication Protocol

Date: `2026-04-21`

Status: `operating_protocol`

Runtime effect: none

## Purpose

This protocol defines how the Analysis Arena should use available windows when a
new fully fresh window is not ready yet.

It solves a practical problem:

- preparing new Pick3StatsC4 windows is expensive
- the March 8-22 window is already complete and valuable
- older shorter windows may exist and can still teach the modern Arena
- development should not stall while waiting for brand-new windows

It also preserves evidence discipline:

- same-window replay is not fresh confirmation
- archived-window replication is stronger than same-window replay but still not fresh confirmation
- only true fresh-window confirmation can unlock Stage 8 implementation gates

Current candidate-window inventory:

- `AAT9_ANALYSIS_ARENA__AVAILABLE_WINDOW_REPLAY_INVENTORY.md`

## Evidence Tiers

### Tier 1 - Same-Window Replay / Regression

Definition:

- rerun the current/enhanced system on a window already studied by the current project cycle
- example: rerun the March 8-22 2026 15-day window after new docs, tools, reports, or cadence fixes

Allowed uses:

- regression testing
- report comparison
- traceability improvement
- detecting changed outputs
- proving new tooling is deterministic
- measuring whether an enhancement exposes more detail from the same evidence
- comparing current artifacts against a frozen baseline

Not allowed uses:

- claiming fresh predictive confirmation
- unlocking Stage 8A implementation by itself
- creating live scoring weights
- replacing old Candidate Universe / Play Card / budget behavior

Evidence label:

- `same_window_replay`

Recommended run label examples:

- `march_2026_15day_baseline`
- `march_2026_15day_replay_v2`
- `march_2026_15day_stage7b_current_rerun`

### Tier 2 - Archived-Window Replication

Definition:

- run the modern Analysis Arena cadence on older available windows that were not fully processed through the current branch/stage stack
- examples: older 5-7 day gold-day windows with enough history/results/tail data to close the cadence

Allowed uses:

- testing whether March findings appear in different historical conditions
- comparing window character
- stress-testing Stage 6B through Stage 7B on non-March data
- expanding casebook examples
- identifying fragile one-window effects
- improving replay tooling and readback docs

Not allowed uses:

- treating historical replication as equivalent to future/fresh confirmation
- deploying Stage 8 candidate, boxed/straight, or budget logic by itself
- overriding active Stage 6C / Stage 7A / Stage 7B blockers

Evidence label:

- `archived_window_replication`

Recommended run label examples:

- `archive_january_2026_5day_replication_v1`
- `archive_june_2025_3day_replication_v1`
- `archive_window_stage7b_replication_v1`

### Tier 3 - True Fresh-Window Confirmation

Definition:

- run a newly prepared window after the current confirmation gates and replay protocol are already defined
- the window should not have been used to design the specific Stage 6B-through-Stage 7B decisions being tested

Allowed uses:

- confirming or contradicting March Stage 7B findings
- clearing or preserving Stage 6C rewrite blockers
- deciding whether Stage 8A can begin as shadow-only specification work
- determining which lanes repeated, weakened, changed, or stayed blocked

Evidence label:

- `true_fresh_confirmation`

Required before Stage 8A:

- full cadence close
- Stage 6B through Stage 7B regenerated on the fresh window
- March Stage 7B and fresh Stage 7B compared directly
- repeated lanes separated from weakened, contradicted, blocked, and research-only lanes

## Required Metadata For Any Replay Or Replication Run

Every replay/replication run should declare:

- `evidence_tier`
- `run_label`
- `window_start`
- `window_end`
- `history_source_status`
- `results_source_status`
- `decay_tail_status`
- `bonus_ball_sidecar_status`
- `baseline_artifact_status`
- `previous_run_label`
- `current_system_checkpoint`
- `allowed_conclusions`
- `blocked_conclusions`

## Readiness Checklist

Before running any available window, confirm:

1. Window start/end dates are explicit.
2. History files are present for each target gold day.
3. Core results files are present for window close.
4. Decay tail coverage is present or explicitly right-censored.
5. Bonus-ball sidecar files are present when the run intends to evaluate them.
6. Previous baseline artifacts are preserved if this is a same-window replay.
7. The evidence tier is selected before execution.
8. The run label is selected before execution.
9. Stage 6B-through-Stage 7B expectations are understood.
10. The run is not being misrepresented as fresh confirmation unless it is truly fresh.

## Baseline Preservation

For same-window replay:

- do not overwrite the old baseline without preserving it
- use a new run label or output namespace when possible
- compare against prior outputs explicitly
- record what changed because of code/docs/cadence changes versus what is inherent in the data

Suggested comparison categories:

- unchanged
- improved traceability
- newly exposed
- degraded
- contradicted
- renamed/reclassified only
- blocked by missing data

## Allowed Conclusions By Evidence Tier

### Same-Window Replay Can Say

- the current system reproduces or changes prior outputs
- the enhanced reports expose more useful detail
- a bug or labeling issue was corrected
- traceability improved
- a known-window result remains consistent under the current stack

### Same-Window Replay Cannot Say

- the pattern is newly confirmed
- the signal generalizes
- Stage 8A can start
- budget/scoring changes are live-safe

### Archived-Window Replication Can Say

- a finding appears outside the March window
- a lane is more or less stable across historical conditions
- a blocker should be rechecked on fresh data
- a casebook target deserves higher or lower priority

### Archived-Window Replication Cannot Say

- future/fresh confirmation has passed
- live scoring should change
- Stage 8A can start without true fresh comparison

### True Fresh Confirmation Can Say

- a March finding repeated, weakened, contradicted, or stayed blocked
- a Stage 6C blocker may be cleared or preserved
- Stage 8A may be considered if enough required lanes repeated
- a lane should remain research-only if it failed fresh confirmation

## Stage 8 Relationship

This protocol supports Stage 8 readiness but does not unlock it.

Stage 8A remains blocked until:

- a true fresh window is run
- Stage 6B through Stage 7B are regenerated on that fresh evidence
- March Stage 7B is compared against fresh Stage 7B
- repeated lanes are separated from weakened, contradicted, blocked, and research-only lanes

Same-window replay and archived-window replication may improve the quality of
Stage 8 design, but they do not replace the true fresh comparison gate.

## Practical Use Order

When more run work is needed, use this order:

1. Same-window replay of the March 8-22 2026 window if the goal is regression or before/after comparison.
2. Archived-window replication if the goal is wider historical stress testing.
3. True fresh-window confirmation when new prepared gold days are available.

This keeps development moving without confusing development evidence with
confirmation evidence.
