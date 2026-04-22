# Analysis Arena Decay / Carryover Scorecard

Purpose:

- keep same-day window metrics clean
- separately measure whether Arena-era state-day snapshots resolve inside a bounded future horizon
- preserve same-day carryforward and future-day decay as different resolution types

## 1. Configured Horizon

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09`
- Results root: `data/results`
- Snapshot dates: `2025-12-30` to `2026-01-09`
- Snapshot upload days: `11`
- Decay horizon: `5` total upload days (same-day included)
- Max draw horizon: `10` total draws
- Tail days required beyond the last snapshot day: `4`
- Results-tail rule: `A 5 total upload-day horizon requires results through snapshot day + 4 days.`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__DECAY_CARRYOVER_ROWS.csv`

## 2. Coverage

- State-day snapshots: `154`
- Full-horizon rows: `154`
- Right-censored rows: `0`
- Max observed upload days: `5`
- Max observed draws: `10`

## 3. Metric Family Scoreboard

| Metric | Active | Same-day | Horizon | Incremental decay lift | Direct same | Same-day precursor | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Board top box core | 154 | 4 (2.6%) | 25 (16.2%) | 21 | 3 | 0 | 1 | 21 | 129 | 0 |
| Board top VTRAC core | 154 | 32 (20.8%) | 103 (66.9%) | 71 | 22 | 0 | 10 | 71 | 51 | 0 |
| Brain 1 box core | 154 | 15 (9.7%) | 63 (40.9%) | 48 | 10 | 0 | 5 | 48 | 91 | 0 |
| Brain 1 VTRAC core | 154 | 57 (37.0%) | 139 (90.3%) | 82 | 35 | 0 | 22 | 82 | 15 | 0 |
| Sandbox box seed | 154 | 18 (11.7%) | 69 (44.8%) | 51 | 12 | 0 | 6 | 51 | 85 | 0 |
| Sandbox exact seed | 154 | 4 (2.6%) | 28 (18.2%) | 24 | 3 | 0 | 1 | 24 | 126 | 0 |
| Sandbox VTRAC seed | 154 | 88 (57.1%) | 151 (98.1%) | 63 | 55 | 0 | 33 | 63 | 3 | 0 |
| Preserved not budgeted | 133 | 3 (2.3%) | 8 (6.0%) | 5 | 0 | 0 | 3 | 5 | 125 | 0 |
| Arena box total | 154 | 22 (14.3%) | 83 (53.9%) | 61 | 14 | 0 | 8 | 61 | 71 | 0 |
| Arena VTRAC total | 154 | 88 (57.1%) | 151 (98.1%) | 63 | 55 | 0 | 33 | 63 | 3 | 0 |

## 4. Cohort Panels

| Cohort | State-days | Same-day | Horizon | Incremental decay lift | Direct same | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Arena any signal | 154 | 93 (60.4%) | 151 (98.1%) | 58 | 58 | 35 | 58 | 3 | 0 |
| Top primary target | 11 | 9 (81.8%) | 11 (100.0%) | 2 | 6 | 3 | 2 | 0 | 0 |
| Top-3 ranked states | 33 | 20 (60.6%) | 33 (100.0%) | 13 | 16 | 4 | 13 | 0 | 0 |
| Any tracker hint present | 154 | 93 (60.4%) | 151 (98.1%) | 58 | 58 | 35 | 58 | 3 | 0 |
| Profit-alert hint present | 154 | 93 (60.4%) | 151 (98.1%) | 58 | 58 | 35 | 58 | 3 | 0 |
| Due-double hint present | 154 | 93 (60.4%) | 151 (98.1%) | 58 | 58 | 35 | 58 | 3 | 0 |

## 5. Notable Examples

### Future-day decay

- `2026-01-01` `Connecticut4` rank=`1` event=`2026-01-02 Midday 970` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-07` `Connecticut4` rank=`1` event=`2026-01-08 Evening 331` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2025-12-31` `Delaware4` rank=`2` event=`2026-01-01 Midday 149` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-02` `Delaware4` rank=`2` event=`2026-01-04 Evening 269` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-03` `Delaware4` rank=`2` event=`2026-01-04 Midday 057` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-04` `Delaware4` rank=`2` event=`2026-01-06 Evening 758` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-05` `Delaware4` rank=`2` event=`2026-01-09 Midday 843` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-07` `Delaware4` rank=`2` event=`2026-01-08 Evening 031` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`

### Same-day carryforward

- `2025-12-31` `Connecticut4` rank=`1` event=`2025-12-31 Evening 361` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-03` `Connecticut4` rank=`1` event=`2026-01-03 Evening 181` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-08` `Connecticut4` rank=`1` event=`2026-01-08 Evening 331` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-07` `Florida4` rank=`3` event=`2026-01-07 Evening 963` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2025-12-30` `Indiana4` rank=`4` event=`2025-12-30 Evening 512` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-07` `Indiana4` rank=`4` event=`2026-01-07 Evening 290` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-03` `Michigan4` rank=`5` event=`2026-01-03 Evening 479` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2025-12-30` `NewJersey4` rank=`6` event=`2025-12-30 Evening 356` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`

### Right-censored

- _none_

## 6. Interpretation

- Same-day window grading stays clean; this scorecard separately measures delayed resolution within the configured horizon.
- A miss is only a true miss when the full tail is present. Incomplete tail coverage is reported as right_censored.
- Upload-day horizon is the primary setting. Draw-based accounting is preserved as a companion lens because same-day Midday/Evening crossover matters.
- Arena-any-signal state-days gained `58` extra resolutions beyond same-day inside the current decay horizon.
- Same-day carryforward remains distinct from future-day decay and should not be flattened into one generic later-hit bucket.
