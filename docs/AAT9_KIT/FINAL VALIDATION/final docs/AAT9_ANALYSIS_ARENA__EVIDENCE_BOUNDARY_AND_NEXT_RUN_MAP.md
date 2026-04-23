# AAT9 Analysis Arena - Evidence Boundary And Next-Run Map

Local timestamp: `2026-04-22T22:28:49-04:00`

Status: `active_guardrail`

Runtime effect: none

## Purpose

This document records how to interpret the current evidence package after the
March Run2 canonical replay work. It exists to prevent three mistakes:

- treating same-window replay as fresh confirmation
- allowing archived-window replication to unlock Stage 8
- comparing a one-window replay cycle against a multi-window baseline cycle

For the exact Pick3StatsC4 gold-day ranges, results windows, decay tails, and
bonus sidecar coverage, use:

- `AAT9_ANALYSIS_ARENA__GOLD_DAY_WINDOW_INVENTORY.md`

## Current Evidence Boundary

Current confirmed state:

- March Run2 canonical mix comparison is complete.
- Candidate completeness is `candidate_complete`.
- Missing required candidate targets are `0`.
- Comparison category count is `unchanged: 26`.
- Stage8 permission remains `blocked`.
- Stage7B status is `ready_for_read_only_confirmation_replay`.
- Scoring rewrite status remains `blocked_until_future_confirmation`.

Interpretation:

- The system has strong regression and reproducibility evidence.
- The March Run2 replay did not create a fresh unlock.
- The downstream candidate, boxed/straight, and budget rebuild remains design-only.

## Evidence Tiers

`true_fresh_confirmation`

- New gold days not previously used as the basis for the current evidence chain.
- Highest-value evidence tier.
- Required before Stage8A can move beyond design/shadow specification.
- Must include full results, decay tail coverage, and bonus/fireball sidecar coverage when available.

`archived_window_replication`

- Previously available historical windows reused through the current Analysis Arena cadence.
- Useful for stress testing repeated patterns, blockers, and lane stability.
- Does not unlock Stage8 by itself.
- Must be labeled as archived replication in reports and readbacks.

`same_window_replay`

- Re-running a known window, such as March 09-23, against an enhanced or corrected system path.
- Useful for regression checks, reproducibility, traceability, and false-alarm detection.
- Does not unlock Stage8 by itself.
- Must use a canonical replacement-cycle comparison if Stage2B through Stage7B are involved.

## Canonical Replacement-Cycle Rule

For same-window replay, do not compare a one-window candidate cycle against the
multi-window baseline cycle.

Correct shape:

1. Keep the baseline peer windows.
2. Remove only the baseline version of the replayed window.
3. Insert the candidate replay window.
4. Regenerate Stage2B through Stage7B inside a dedicated replacement-cycle root.
5. Run `window-replay-compare` against that replacement-cycle root.

Current March Run2 canonical replacement cycle:

- `WINDOW_2025-12-30_to_2026-01-04`
- `WINDOW_2026-01-05_to_2026-01-09`
- `WINDOW_2026-01-15_to_2026-01-22`
- `REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23`

Forbidden in that cycle:

- `WINDOW_2026-01-05_to_2026-01-09__PREALIGN_SNAPSHOT`
- `WINDOW_2026-01-15_to_2026-01-18`

## Next-Run Decision Map

If the next goal is maximum unlock-relevant evidence:

- Run a true fresh gold-day window.
- Preserve the established cadence.
- Regenerate the post-run chain through Stage7B.
- Compare March Stage7B against fresh Stage7B.
- Only repeated, non-contradicted, denominator-safe findings can support Stage8A design progression.

If the next goal is more data without new gold-day preparation:

- Run archived-window replication.
- Use explicit evidence-tier labeling.
- Treat the result as stress-test evidence only.
- Do not use it as Stage8 permission.

If the next goal is regression safety after code changes:

- Run same-window replay.
- Use an isolated replay namespace.
- Use a canonical replacement-cycle root for Stage2B through Stage7B.
- Run the replay-plan guardrail check before and after the replay.

## Required Preflight Checks

Before any same-window replay:

- `window-replay-plan`
- `replay-plan-guardrails`
- `window-replay-readiness`
- baseline manifest, if preserving a new baseline

Before any true fresh window:

- `fresh-window-readiness`
- locked window dates
- locked decay upload-day horizon
- confirmed tail results coverage
- confirmed bonus/fireball sidecar coverage plan

Before any Stage8A work:

- fresh-window Stage6B through Stage7B regenerated
- March-vs-fresh Stage7B comparison complete
- repeated lanes separated from weakened, contradicted, blocked, and research-only lanes
- old Candidate Universe / Play Card / budget logic still labeled as control arm

## Current Recommended Path

The next project evidence step should be one of these:

- true fresh-window run if new gold days are ready
- archived-window replication if we want more stress-test evidence while waiting for fresh gold days
- same-window replay only when testing regression after meaningful code/cadence changes

Do not begin active Stage8A implementation yet. Stage8A can be refined as a
design brief, but live downstream candidate formation, boxed/straight expression,
and budget policy remain blocked until fresh confirmation evidence exists.
