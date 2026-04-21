# AAT9 Analysis Arena - March Replay Runbook

Date: `2026-04-21`

Status: `runbook_pending_approval`

Runtime effect: none

## Purpose

This runbook defines how to perform a future same-window replay of the March
2026 Analysis Arena window without overwriting the preserved baseline or
confusing replay evidence with true fresh confirmation.

Use this with:

- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`
- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS.md`
- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`
- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.md`

## Baseline

Baseline window root:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`

Baseline cycle root:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2`

Evidence tier:

- `same_window_replay`

Allowed purpose:

- regression replay
- before/after comparison
- deterministic rerun checks
- traceability improvement review
- development stress test before a true fresh window

Blocked purpose:

- no fresh-confirmation claim
- no Stage 8A unlock
- no live scoring change
- no candidate-generation change
- no translator or budget replacement

## Required Pre-Run Steps

Before any March replay is executed:

1. Regenerate replay readiness:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-replay-readiness --runs2-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 --force
```

2. Regenerate the pending comparison report:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-replay-compare --force
```

3. Choose a rerun namespace or output root that does not overwrite baseline
   March artifacts.

4. Record the rerun label before execution.

Suggested label:

- `march_2026_15day_replay_v2`

## Candidate Output Requirement

The rerun should write to a separate candidate window root and, if Stage 6B
through Stage 7B are regenerated, a separate candidate cycle root.

Do not write candidate artifacts directly over:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE6*`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA__CYCLE__STAGE7*`

## Post-Run Comparison

After the rerun exists, run:

```bash
python3 scripts/tools/run_analysis_arena_cycle.py window-replay-compare \
  --baseline-window-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23 \
  --candidate-window-root <candidate-window-root> \
  --baseline-cycle-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2 \
  --candidate-cycle-root <candidate-cycle-root> \
  --evidence-tier same_window_replay \
  --run-label march_2026_15day_replay_v2 \
  --force
```

Read the comparison report before interpreting any rerun result:

- `unchanged`: reproducibility / no observed comparison movement
- `improved_traceability`: more detail was exposed, not fresh confirmation
- `newly_exposed`: candidate produced rows or artifacts absent from baseline
- `degraded`: candidate lost baseline rows or artifacts
- `contradicted`: status, decision, blocker, or permission posture changed
- `renamed_or_reclassified_only`: non-material naming/classification movement
- `blocked_by_missing_data`: missing baseline or candidate data prevents a conclusion

## Review Order

Review in this order:

1. `contradicted`
2. `degraded`
3. `blocked_by_missing_data`
4. `newly_exposed`
5. `improved_traceability`
6. `renamed_or_reclassified_only`
7. `unchanged`

Any `contradicted` or `degraded` Stage 6B-through-Stage 7B row requires manual
review before the rerun is used as development evidence.

## Hard Boundary

This runbook is not approval to run the replay by itself.

It only defines the safe path when a same-window replay is explicitly approved.
True fresh-window confirmation is still required before Stage 8A can be
considered.
