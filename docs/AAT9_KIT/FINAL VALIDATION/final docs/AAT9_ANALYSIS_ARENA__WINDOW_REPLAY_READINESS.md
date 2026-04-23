# Analysis Arena Window Replay Readiness

## 1. Verdict

- Scanned windows: `4`
- Same-window replay candidates: `1`
- Archived replication ready: `3`
- Archived replication with caveats: `0`
- Needs prep: `0`
- Strongest same-window replay candidate: `WINDOW_2026-03-09_to_2026-03-23`
- Strongest archived replication candidate: `WINDOW_2025-12-30_to_2026-01-04`
- Stage 6B-through-Stage 7B artifacts present: `true`

Operational meaning:

- use same-window replay for regression and before/after comparison
- use archived replication for historical stress testing
- use only true fresh confirmation to unlock Stage 8A consideration

## 2. Source Coverage

| Source | Count | Min | Max |
|---|---:|---|---|
| History workbooks | 43 | `2025-06-20` | `2026-03-22` |
| Core results | 63 | `2025-06-21` | `2026-03-27` |
| Bonus results | 47 | `2025-12-30` | `2026-03-27` |
| Predictive sharepacks | 34 | `2025-12-30` | `2026-03-23` |
| Truth sharepacks | 23 | `2025-06-21` | `2026-01-22` |

## 3. Stage 6B Through Stage 7B Artifact Status

- `stage6b_shadow_replay`: `true`
- `stage6b_readback`: `true`
- `stage6c_confirmation`: `true`
- `stage6d_restraint`: `true`
- `stage6e_support`: `true`
- `stage6f_atlas`: `true`
- `stage7a_scaffold`: `true`
- `stage7b_harness`: `true`

## 4. Window Readiness Matrix

| Window | Tier | Status | Files | Tail | Bonus | Recommendation |
|---|---|---|---:|---|---|---|
| `WINDOW_2025-12-30_to_2026-01-04` | `archived_window_replication` | `ready` | 240 | `true` | `true` | `archived_replication_candidate` |
| `WINDOW_2026-01-05_to_2026-01-09` | `archived_window_replication` | `ready` | 210 | `true` | `true` | `archived_replication_candidate` |
| `WINDOW_2026-01-15_to_2026-01-22` | `archived_window_replication` | `ready` | 300 | `true` | `true` | `archived_replication_candidate` |
| `WINDOW_2026-03-09_to_2026-03-23` | `same_window_replay` | `ready_with_caveats` | 517 | `true` | `true` | `strongest_same_window_replay_candidate` |

## 5. Coverage Caveats

- `WINDOW_2026-03-09_to_2026-03-23`: truth_missing=2026-03-09, 2026-03-10, 2026-03-11, 2026-03-12, 2026-03-13, ...

## 6. Baseline Manifest Use

Before any same-window replay:

- preserve the existing window root as the baseline
- choose a new run label or output namespace
- compare key artifact hashes and row-level outputs after the rerun
- classify differences as behavior changes, traceability improvements, or naming/reclassification only

## 7. Replay Comparison Design Stub

Durable design reference:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`

Baseline-vs-rerun categories:

- `unchanged`
- `improved_traceability`
- `newly_exposed`
- `degraded`
- `contradicted`
- `renamed_or_reclassified_only`
- `blocked_by_missing_data`

Stage 6B-through-Stage 7B comparison targets:

- scenario decisions
- requirement results
- rewrite blockers
- restraint bucket posture
- support narrowing posture
- lane decision atlas
- fresh-window carry-forward queue
- Stage 7B queue replay status

## 8. Hard Boundary

This report does not run a window and does not grant Stage 8 permission.
Same-window replay and archived-window replication can support development and historical stress testing, but they cannot replace true fresh-window confirmation.
