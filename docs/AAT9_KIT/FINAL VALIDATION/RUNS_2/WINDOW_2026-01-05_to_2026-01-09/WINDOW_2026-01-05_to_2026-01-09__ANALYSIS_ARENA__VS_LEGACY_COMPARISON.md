# Analysis Arena vs Legacy Same-Window Comparison

## 1. Scope

- Window: `2026-01-05_to_2026-01-09`
- Arena window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09`
- Legacy RUNS root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS`
- Same-day event denominator: arena `138` vs legacy dashboard `138`
- Windowed downstream rollups use `70` state-day windows (5 days x 14 states), which is a different denominator from the 138 state×period outcome ledger.

## 2. Arena Benchmark

- Winner on board: `138` (100.0%)
- Board top5 containment: `50` (36.2%)
- Candidate Universe exact / box: `28` (20.3%) / `34` (24.6%)
- Play Card any exact / box: `18` (13.0%) / `12` (8.7%)
- Opportunity gap box: `5` (3.6%)

## 3. Legacy Same-Window Baseline

- Legacy dashboard: [corpus dashboard](docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_DASHBOARD.md)
- Stable family presence: `134/138` (97.1%)
- Hot Zones top-lane presence: `135/138` (97.8%)
- DR top-candidate exact containment: `5/138` (3.6%)
- Blackapple top-list exact containment: `1/138` (0.7%)
- Legacy CU union exact / box: `25` (18.1%) / `31` (22.5%)
- DR VT-box tag on active rows: `106` (84.1%)
- Legacy BA Combined ALERT Midday inclusive same-day / N5 window: `25.0%` / `75.0%`
- Legacy BA Combined ALERT Evening inclusive same-day / N5 window: `37.5%` / `87.5%`

## 4. Shared Downstream Strategy Replay

These rows compare shared strategy names between the legacy same-window rollup and the arena-era rerun on the same dates.

| Strategy | Budget | Legacy Box | Arena Box | Delta | Legacy Inclusive | Arena Inclusive | Delta |
|---|---|---:|---:|---:|---:|---:|---:|
| `analysis_prefix` | `B12` | 12.9% | 10.0% | -2.9% | 44.3% | 34.3% | -10.0% |
| `analysis_prefix` | `B24` | 21.4% | 24.3% | 2.9% | 60.0% | 67.1% | 7.1% |
| `analysis_prefix` | `B36` | 21.4% | 25.7% | 4.3% | 72.9% | 81.4% | 8.6% |
| `play_box_first` | `B12` | 8.6% | 8.6% | 0.0% | 22.9% | 24.3% | 1.4% |
| `play_box_first` | `B24` | 12.9% | 14.3% | 1.4% | 44.3% | 44.3% | 0.0% |
| `play_box_first` | `B36` | 20.0% | 21.4% | 1.4% | 60.0% | 61.4% | 1.4% |
| `v0_2_default` | `B12` | 12.9% | 10.0% | -2.9% | 44.3% | 34.3% | -10.0% |
| `v0_2_default` | `B24` | 31.4% | 34.3% | 2.9% | 72.9% | 77.1% | 4.3% |
| `v0_2_default` | `B36` | 35.7% | 40.0% | 4.3% | 80.0% | 84.3% | 4.3% |
| `vtrac_pack_boxed_first_laneonly_presetB` | `B12` | 24.3% | 28.6% | 4.3% | 42.9% | 38.6% | -4.3% |
| `vtrac_pack_boxed_first_laneonly_presetB` | `B24` | 34.3% | 35.7% | 1.4% | 71.4% | 75.7% | 4.3% |
| `vtrac_pack_boxed_first_laneonly_presetB` | `B36` | 38.6% | 41.4% | 2.9% | 80.0% | 84.3% | 4.3% |

- Best shared-strategy box gains: `convergence_box_first` B12 7.1%->12.9%, `vtrac_pack_boxed_first` B12 20.0%->25.7%, `v0_2_default` B36 35.7%->40.0%, `v0_2_default_b12pack_lenient` B36 35.7%->40.0%, `v0_2_default_b12pack_strict` B36 35.7%->40.0%
- Shared-strategy box regressions: `analysis_prefix` B12 12.9%->10.0%, `v0_2_default` B12 12.9%->10.0%

## 5. Historical Codex Context

- Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md`
- Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-21__DISCONNECT_ANALYSIS__CODEX.md`
- The old deep-analysis SSOT concluded the system was usually not missing signal outright; it was losing probability mass in the B36 selection cut.
- The old disconnect analysis explicitly said low DR and Blackapple exact-hit rates were not the primary optimization target; they were intentionally used as lane, envelope, and triage evidence.

## 6. Interpretation

- The old deep-report thesis still fits this window: the system problem is much more downstream realization than upstream signal absence.
- On the aligned arena window, the winner reached the board on 100.0% of graded events, while Play Card any-box realization only converted 8.7%.
- Candidate Universe union containment improved versus the legacy same-window baseline: exact 18.1% -> 20.3%, box 22.5% -> 24.6%.
- Replaying the legacy `v0_2_default` downstream strategy on arena-era sharepacks improved the B36 box window rate from 35.7% to 40.0%, a delta of 4.3%.
- The legacy dashboard already showed strong upstream tool presence (Stable 134/138, Hot Zones 135/138); the arena branch improves how that truth is preserved, ranked, and audited across states.
- This supports using B12/B24/B36 as a control arm only: the richer arena system appears to know more than the old downstream expression can currently realize.

## 7. Practical Read

- The old system already had meaningful upstream tool presence, but it mostly evaluated itself through exact-hit and selection-cut surfaces.
- The arena branch adds board containment, cross-state context, tracker attribution, and explicit opportunity-gap measurement.
- This makes same-window comparison possible at two levels: legacy realized performance, and arena intrinsic truth quality plus downstream loss.
