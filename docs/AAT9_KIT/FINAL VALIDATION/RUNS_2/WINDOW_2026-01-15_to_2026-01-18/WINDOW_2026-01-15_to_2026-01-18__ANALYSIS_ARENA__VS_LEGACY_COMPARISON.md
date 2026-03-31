# Analysis Arena vs Legacy Same-Window Comparison

## 1. Scope

- Window: `2026-01-15_to_2026-01-18`
- Arena window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18`
- Legacy RUNS root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS`
- Same-day event denominator: arena `109` vs legacy dashboard `0`
- Windowed downstream rollups use `70` state-day windows (5 days x 14 states), which is a different denominator from the 138 state×period outcome ledger.

## 2. Arena Benchmark

- Winner on board: `109` (100.0%)
- Board top5 containment: `40` (36.7%)
- Candidate Universe exact / box: `26` (23.9%) / `33` (30.3%)
- Play Card any exact / box: `16` (14.7%) / `11` (10.1%)
- Opportunity gap box: `4` (3.7%)

## 3. Legacy Same-Window Baseline

- Legacy dashboard: [corpus dashboard](docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-18__CORPUS_DASHBOARD.md)
- Legacy dashboard status: `Same-window legacy corpus dashboard is missing.`
- Stable family presence: `0/0` (0.0%)
- Hot Zones top-lane presence: `0/0` (0.0%)
- DR top-candidate exact containment: `0/0` (0.0%)
- Blackapple top-list exact containment: `0/0` (0.0%)
- Legacy CU union exact / box: `15` (18.5%) / `22` (27.2%)
- DR VT-box tag on active rows: `0` (0.0%)

## 4. Shared Downstream Strategy Replay

These rows compare shared strategy names between the legacy same-window rollup and the arena-era rerun on the same dates.

| Strategy | Budget | Legacy Box | Arena Box | Delta | Legacy Inclusive | Arena Inclusive | Delta |
|---|---|---:|---:|---:|---:|---:|---:|

- Best shared-strategy box gains: _none_

## 5. Historical Codex Context

- Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md`
- Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-21__DISCONNECT_ANALYSIS__CODEX.md`
- The old deep-analysis SSOT concluded the system was usually not missing signal outright; it was losing probability mass in the B36 selection cut.
- The old disconnect analysis explicitly said low DR and Blackapple exact-hit rates were not the primary optimization target; they were intentionally used as lane, envelope, and triage evidence.

## 6. Interpretation

- The old deep-report thesis still fits this window: the system problem is much more downstream realization than upstream signal absence.
- On the aligned arena window, the winner reached the board on 100.0% of graded events, while Play Card any-box realization only converted 10.1%.
- Candidate Universe union containment improved versus the legacy same-window baseline: exact 18.5% -> 23.9%, box 27.2% -> 30.3%.
- The legacy dashboard already showed strong upstream tool presence (Stable 0/0, Hot Zones 0/0); the arena branch improves how that truth is preserved, ranked, and audited across states.
- This supports using B12/B24/B36 as a control arm only: the richer arena system appears to know more than the old downstream expression can currently realize.

## 7. Practical Read

- The old system already had meaningful upstream tool presence, but it mostly evaluated itself through exact-hit and selection-cut surfaces.
- The arena branch adds board containment, cross-state context, tracker attribution, and explicit opportunity-gap measurement.
- This makes same-window comparison possible at two levels: legacy realized performance, and arena intrinsic truth quality plus downstream loss.
