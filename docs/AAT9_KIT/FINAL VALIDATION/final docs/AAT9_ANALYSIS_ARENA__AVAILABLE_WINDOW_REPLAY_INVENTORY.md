# AAT9 Analysis Arena - Available Window Replay Inventory

Date: `2026-04-21`

Status: `read_only_inventory`

Runtime effect: none

## Purpose

This inventory records which existing windows appear useful for future
same-window replay or archived-window replication.

No cadence was run to create this inventory. It only inspected file presence for:

- `data/history`
- `data/results`
- `data/results_bonus`
- `sharepacks/_predictive`
- `sharepacks`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_*`

Use this with:

- `AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_AND_REPLICATION_PROTOCOL.md`

## Best Immediate Same-Window Replay Candidate

### `WINDOW_2026-03-09_to_2026-03-23`

Evidence tier:

- `same_window_replay`

Why it is strongest:

- current March package is the most complete modern Arena window
- existing RUNS_2 window root is present
- existing window root contains `517` files
- predictive sharepacks exist for `2026-03-09` through `2026-03-23`
- core results exist for `2026-03-09` through `2026-03-27`
- bonus-ball sidecars exist for `2026-03-09` through `2026-03-27`
- history files exist for the mapped history dates, including `2026-03-08` through `2026-03-22`
- full decay tail appears available for a 5-upload-day horizon through `window_end + 4 days`

Caveat:

- truth sharepacks under `sharepacks/<D>/` were not present for March dates in this inventory scan
- the existing March RUNS_2 package should be treated as the baseline to preserve before any rerun
- any rerun should use a new run label or output namespace before comparison

Allowed next use:

- regression replay
- before/after comparison
- current-system rerun against a frozen baseline
- Stage 6B-through-Stage 7B artifact comparison if output namespacing is controlled

Blocked conclusion:

- this cannot be called fresh confirmation

## Best Archived-Window Replication Candidates

### `WINDOW_2025-12-30_to_2026-01-04`

Evidence tier:

- `archived_window_replication`

Observed status:

- existing RUNS_2 window root is present
- existing window root contains `236` files
- history coverage appears complete
- predictive sharepack coverage appears complete
- truth sharepack coverage appears complete
- core results coverage appears complete
- full decay tail through `window_end + 4 days` appears complete
- bonus-ball sidecars are absent, which is expected for older non-bonus inventory

Allowed next use:

- strongest archived replication candidate after March
- good target for rerunning modern Stage 6B-through-Stage 7B logic if namespacing is controlled

### `WINDOW_2026-01-15_to_2026-01-18`

Evidence tier:

- `archived_window_replication`

Observed status:

- existing RUNS_2 window root is present
- existing window root contains `176` files
- history coverage appears complete
- predictive sharepack coverage appears complete
- truth sharepack coverage appears complete
- core results coverage appears complete
- full decay tail through `window_end + 4 days` appears complete
- bonus-ball sidecars are absent

Allowed next use:

- compact archived replication candidate
- useful as a shorter controlled replay after the December/January window

## Usable With Caveats

### `WINDOW_2026-01-05_to_2026-01-09`

Evidence tier:

- `archived_window_replication`

Observed status:

- existing RUNS_2 window root is present
- existing window root contains `206` files
- history coverage appears complete
- predictive sharepack coverage appears complete
- truth sharepack coverage appears complete
- core results coverage appears complete for the main window
- full decay tail has missing core results for `2026-01-10` and `2026-01-11`
- bonus-ball sidecars are absent

Allowed next use:

- archived replication if decay rows are explicitly treated as partial/right-censored

Do not use as:

- full decay-horizon confirmation without addressing missing tail results

### `WINDOW_2026-01-05_to_2026-01-09__PREALIGN_SNAPSHOT`

Evidence tier:

- `same_window_replay` / archived snapshot reference

Observed status:

- existing RUNS_2 snapshot root is present
- existing window root contains `226` files
- same coverage caveats as `WINDOW_2026-01-05_to_2026-01-09`

Allowed next use:

- baseline comparison snapshot only

### `WINDOW_2026-01-15_to_2026-01-22`

Evidence tier:

- `archived_window_replication`

Observed status:

- existing RUNS_2 window root is present
- existing window root contains `296` files
- history coverage appears complete
- predictive sharepack coverage appears complete
- core results coverage appears complete for the main window
- truth sharepack for `2026-01-19` was not present in the scan
- full decay tail has missing core results for `2026-01-23`, `2026-01-24`, and `2026-01-25`
- bonus-ball sidecars are absent

Allowed next use:

- broader archived replication only if the missing truth sharepack and decay-tail gaps are accepted or repaired

Do not use as:

- clean full-tail replication without resolving the missing coverage

## Lower-Readiness Historical Material

June 2025 material exists in parts of the repository:

- results exist for `2025-06-21` through `2025-07-06`
- truth sharepacks exist for `2025-06-21` through `2025-06-24`
- history files exist for several June dates

But no modern `RUNS_2/WINDOW_*` root was found for a June replay window in this
scan.

Allowed next use:

- future archived replication candidate after explicit prep

Do not use as:

- immediate modern Analysis Arena replay without first building/confirming the required RUNS_2 window structure

## Recommended Future Run Order

1. `WINDOW_2026-03-09_to_2026-03-23`
   - evidence tier: `same_window_replay`
   - purpose: current-system replay against the March baseline
2. `WINDOW_2025-12-30_to_2026-01-04`
   - evidence tier: `archived_window_replication`
   - purpose: strongest older historical replication candidate
3. `WINDOW_2026-01-15_to_2026-01-18`
   - evidence tier: `archived_window_replication`
   - purpose: compact second replication check
4. `WINDOW_2026-01-05_to_2026-01-09`
   - evidence tier: `archived_window_replication`
   - purpose: usable only with explicit partial-decay treatment
5. `WINDOW_2026-01-15_to_2026-01-22`
   - evidence tier: `archived_window_replication`
   - purpose: broader stress test only after coverage caveats are resolved or accepted

## Hard Boundary

None of these existing windows should be treated as true fresh confirmation.

They can keep development moving, improve regression confidence, and test
historical robustness, but Stage 8A still requires a true fresh window rerun
through Stage 6B through Stage 7B and March-vs-fresh comparison.
