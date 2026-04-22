# Analysis Arena Canonical Window Set - 2026-04-22

This note records the canonical evidence set used after the 2026-01-19 recovery pass. It exists to prevent accidental double-counting of overlapping windows or stale replay artifacts.

## Canonical Inputs

The refreshed Stage2B through Stage7B chain was regenerated with explicit `--window-root` inputs:

| Window | Role | Notes |
|---|---|---|
| `WINDOW_2025-12-30_to_2026-01-04` | canonical archived evidence | Included as a non-overlapping early-January window. |
| `WINDOW_2026-01-05_to_2026-01-09` | canonical archived evidence | Included as a non-overlapping early-January window. |
| `WINDOW_2026-01-15_to_2026-01-22` | canonical recovered evidence | Promoted over the split January interpretation after recovering 2026-01-19. |
| `WINDOW_2026-03-09_to_2026-03-23` | canonical comprehensive March evidence | Included as the large March replay/reference window. |

## Exclusions

The following artifacts must not be treated as additional independent evidence for cross-window promotion:

| Artifact | Reason |
|---|---|
| `WINDOW_2026-01-15_to_2026-01-18` | Superseded by recovered `WINDOW_2026-01-15_to_2026-01-22`; including both would double-count Jan15-Jan18. |
| `WINDOW_2026-01-05_to_2026-01-09__PREALIGN_SNAPSHOT` | Snapshot only; not a fresh independent window. |
| `REPLAY/archived_window_replay_v2_jan19_recovered/_scratch_initial_parent_analysis_arena_20260422` | Preserved scratch artifact from an initial wrong-layout attempt. |
| `REPLAY/archived_window_replay_v2_jan19_recovered/WINDOW_2026-01-15_to_2026-01-22/_scratch_flat_postrange_attempt_20260422` | Preserved scratch artifact from a flat postrange attempt. |

## Recovery Outcome

The 2026-01-19 issue was a missing sharepack/gold-day gap, not data corruption or tampering. After recovery, the canonical Jan15-Jan22 window contains 221 winner-event rows. This is expected for that results inventory because `data/results/2026-01-18.txt` does not include Puerto Rico and South Carolina only has Evening.

The canonical top-level Jan15-Jan22 decay scorecard was refreshed with full tail coverage:

| Metric | Value |
|---|---:|
| state-day snapshots | 112 |
| full-horizon rows | 112 |
| right-censored rows | 0 |
| max observed draws | 10 |
| max observed upload days | 5 |

## Regenerated Chain

The cross-window cycle was regenerated from the canonical window set through:

| Stage | Status |
|---|---|
| Cross-window rollup | refreshed |
| Stage2B cross-window stack rollup | refreshed |
| Stage3 decision workbench | refreshed with explicit windows |
| Stage4 fixture replay harness | refreshed with explicit windows |
| Stage4B replay readback | refreshed |
| Stage4C shadow translator prototype | refreshed |
| Stage5 shadow translator fixture evaluator | refreshed with explicit windows |
| Stage5 readback decision memo | refreshed |
| Stage6A shadow translator specification | refreshed |
| Stage6B shadow replay simulator and readback | refreshed |
| Stage6C confirmation protocol | refreshed |
| Stage6D restraint calibration workbench | refreshed |
| Stage6E support modifier narrowing workbench | refreshed |
| Stage6F integrated decision atlas | refreshed |
| Stage7A fresh confirmation scaffold | refreshed |
| Stage7B fixture replay harness | refreshed |

## Current Boundary

Stage7B is ready to support fresh-window replay/confirmation planning. The live downstream scoring, candidate-expression, boxed/straight formation, and budgeting infrastructure remain intentionally unchanged. Stage8A should remain specification/shadow-only until fresh or properly quarantined replay evidence clears the active rewrite gates.
