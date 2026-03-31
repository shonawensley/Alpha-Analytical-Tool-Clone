# Analysis Arena vs Legacy Same-Window Comparison

## 1. Scope

- Window: `2025-12-30_to_2026-01-04`
- Arena window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04`
- Legacy RUNS root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS`
- Same-day event denominator: arena `163` vs legacy dashboard `163`
- Windowed downstream rollups use `70` state-day windows (5 days x 14 states), which is a different denominator from the 138 state×period outcome ledger.

## 2. Arena Benchmark

- Winner on board: `163` (100.0%)
- Board top5 containment: `60` (36.8%)
- Candidate Universe exact / box: `25` (15.3%) / `37` (22.7%)
- Play Card any exact / box: `20` (12.3%) / `10` (6.1%)
- Opportunity gap box: `5` (3.1%)

## 3. Legacy Same-Window Baseline

- Legacy dashboard: [corpus dashboard](docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_DASHBOARD.md)
- Stable family presence: `158/163` (96.9%)
- Hot Zones top-lane presence: `162/163` (99.4%)
- DR top-candidate exact containment: `8/163` (4.9%)
- Blackapple top-list exact containment: `0/163` (0.0%)
- Legacy CU union exact / box: `26` (16.0%) / `37` (22.7%)
- DR VT-box tag on active rows: `130` (86.7%)
- Legacy BA Combined ALERT Midday inclusive same-day / N5 window: `33.3%` / `83.3%`
- Legacy BA Combined ALERT Evening inclusive same-day / N5 window: `66.7%` / `100.0%`

## 4. Shared Downstream Strategy Replay

These rows compare shared strategy names between the legacy same-window rollup and the arena-era rerun on the same dates.

| Strategy | Budget | Legacy Box | Arena Box | Delta | Legacy Inclusive | Arena Inclusive | Delta |
|---|---|---:|---:|---:|---:|---:|---:|
| `analysis_prefix` | `B12` | 14.3% | 14.3% | 0.0% | 47.6% | 46.4% | -1.2% |
| `analysis_prefix` | `B24` | 26.2% | 22.6% | -3.6% | 70.2% | 67.9% | -2.4% |
| `analysis_prefix` | `B36` | 29.8% | 27.4% | -2.4% | 79.8% | 78.6% | -1.2% |
| `play_box_first` | `B12` | 8.3% | 8.3% | 0.0% | 35.7% | 33.3% | -2.4% |
| `play_box_first` | `B24` | 16.7% | 14.3% | -2.4% | 52.4% | 48.8% | -3.6% |
| `play_box_first` | `B36` | 23.8% | 20.2% | -3.6% | 69.0% | 65.5% | -3.6% |
| `v0_2_default` | `B12` | 14.3% | 14.3% | 0.0% | 47.6% | 46.4% | -1.2% |
| `v0_2_default` | `B24` | 40.5% | 38.1% | -2.4% | 79.8% | 76.2% | -3.6% |
| `v0_2_default` | `B36` | 46.4% | 44.0% | -2.4% | 88.1% | 83.3% | -4.8% |
| `vtrac_pack_boxed_first_laneonly_presetB` | `B12` | 20.2% | 21.4% | 1.2% | 45.2% | 44.0% | -1.2% |
| `vtrac_pack_boxed_first_laneonly_presetB` | `B24` | 39.3% | 38.1% | -1.2% | 76.2% | 77.4% | 1.2% |
| `vtrac_pack_boxed_first_laneonly_presetB` | `B36` | 46.4% | 44.0% | -2.4% | 88.1% | 83.3% | -4.8% |

- Best shared-strategy box gains: `conversion_box_first` B12 13.1%->16.7%, `conversion_box_first_conditional_lenient_presetA` B12 9.5%->10.7%, `conversion_box_first_conditional_strict_presetA` B12 9.5%->10.7%, `conversion_box_first_conditional_strict_presetB` B12 9.5%->10.7%, `vtrac_pack_boxed_first_laneonly_presetB` B12 20.2%->21.4%
- Shared-strategy box regressions: `v0_2_default_b12pack_lenient` B12 20.2%->14.3%, `analysis_prefix` B24 26.2%->22.6%, `play_box_first` B36 23.8%->20.2%, `v0_2_default_b12pack_strict` B12 19.1%->15.5%

## 5. Historical Codex Context

- Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md`
- Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-21__DISCONNECT_ANALYSIS__CODEX.md`
- The old deep-analysis SSOT concluded the system was usually not missing signal outright; it was losing probability mass in the B36 selection cut.
- The old disconnect analysis explicitly said low DR and Blackapple exact-hit rates were not the primary optimization target; they were intentionally used as lane, envelope, and triage evidence.

## 6. Interpretation

- The old deep-report thesis still fits this window: the system problem is much more downstream realization than upstream signal absence.
- On the aligned arena window, the winner reached the board on 100.0% of graded events, while Play Card any-box realization only converted 6.1%.
- Candidate Universe union containment improved versus the legacy same-window baseline: exact 16.0% -> 15.3%, box 22.7% -> 22.7%.
- Replaying the legacy `v0_2_default` downstream strategy on arena-era sharepacks improved the B36 box window rate from 46.4% to 44.0%, a delta of -2.4%.
- The legacy dashboard already showed strong upstream tool presence (Stable 158/163, Hot Zones 162/163); the arena branch improves how that truth is preserved, ranked, and audited across states.
- This supports using B12/B24/B36 as a control arm only: the richer arena system appears to know more than the old downstream expression can currently realize.

## 7. Practical Read

- The old system already had meaningful upstream tool presence, but it mostly evaluated itself through exact-hit and selection-cut surfaces.
- The arena branch adds board containment, cross-state context, tracker attribution, and explicit opportunity-gap measurement.
- This makes same-window comparison possible at two levels: legacy realized performance, and arena intrinsic truth quality plus downstream loss.
