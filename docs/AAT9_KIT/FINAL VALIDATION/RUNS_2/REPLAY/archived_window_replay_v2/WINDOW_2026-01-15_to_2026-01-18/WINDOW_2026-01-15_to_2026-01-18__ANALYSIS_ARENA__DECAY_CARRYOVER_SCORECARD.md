# Analysis Arena Decay / Carryover Scorecard

Purpose:

- keep same-day window metrics clean
- separately measure whether Arena-era state-day snapshots resolve inside a bounded future horizon
- preserve same-day carryforward and future-day decay as different resolution types

## 1. Configured Horizon

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18`
- Results root: `data/results`
- Snapshot dates: `2026-01-15` to `2026-01-18`
- Snapshot upload days: `4`
- Decay horizon: `5` total upload days (same-day included)
- Max draw horizon: `10` total draws
- Tail days required beyond the last snapshot day: `4`
- Results-tail rule: `A 5 total upload-day horizon requires results through snapshot day + 4 days.`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__DECAY_CARRYOVER_ROWS.csv`

## 2. Coverage

- State-day snapshots: `56`
- Full-horizon rows: `56`
- Right-censored rows: `0`
- Max observed upload days: `5`
- Max observed draws: `10`

## 3. Metric Family Scoreboard

| Metric | Active | Same-day | Horizon | Incremental decay lift | Direct same | Same-day precursor | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Board top box core | 56 | 3 (5.4%) | 9 (16.1%) | 6 | 0 | 0 | 3 | 6 | 47 | 0 |
| Board top VTRAC core | 56 | 17 (30.4%) | 34 (60.7%) | 17 | 10 | 0 | 7 | 17 | 22 | 0 |
| Brain 1 box core | 56 | 9 (16.1%) | 25 (44.6%) | 16 | 3 | 0 | 6 | 16 | 31 | 0 |
| Brain 1 VTRAC core | 56 | 26 (46.4%) | 50 (89.3%) | 24 | 17 | 0 | 9 | 24 | 6 | 0 |
| Sandbox box seed | 56 | 10 (17.9%) | 22 (39.3%) | 12 | 3 | 0 | 7 | 12 | 34 | 0 |
| Sandbox exact seed | 56 | 3 (5.4%) | 8 (14.3%) | 5 | 1 | 0 | 2 | 5 | 48 | 0 |
| Sandbox VTRAC seed | 56 | 34 (60.7%) | 55 (98.2%) | 21 | 22 | 0 | 12 | 21 | 1 | 0 |
| Preserved not budgeted | 48 | 0 (0.0%) | 3 (6.2%) | 3 | 0 | 0 | 0 | 3 | 45 | 0 |
| Arena box total | 56 | 12 (21.4%) | 28 (50.0%) | 16 | 4 | 0 | 8 | 16 | 28 | 0 |
| Arena VTRAC total | 56 | 34 (60.7%) | 55 (98.2%) | 21 | 22 | 0 | 12 | 21 | 1 | 0 |

## 4. Cohort Panels

| Cohort | State-days | Same-day | Horizon | Incremental decay lift | Direct same | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Arena any signal | 56 | 37 (66.1%) | 55 (98.2%) | 18 | 24 | 13 | 18 | 1 | 0 |
| Top primary target | 4 | 3 (75.0%) | 4 (100.0%) | 1 | 2 | 1 | 1 | 0 | 0 |
| Top-3 ranked states | 12 | 7 (58.3%) | 12 (100.0%) | 5 | 6 | 1 | 5 | 0 | 0 |
| Any tracker hint present | 56 | 37 (66.1%) | 55 (98.2%) | 18 | 24 | 13 | 18 | 1 | 0 |
| Profit-alert hint present | 56 | 37 (66.1%) | 55 (98.2%) | 18 | 24 | 13 | 18 | 1 | 0 |
| Due-double hint present | 56 | 37 (66.1%) | 55 (98.2%) | 18 | 24 | 13 | 18 | 1 | 0 |

## 5. Notable Examples

### Future-day decay

- `2026-01-17` `Connecticut4` rank=`1` event=`2026-01-19 Evening 429` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-15` `Delaware4` rank=`2` event=`2026-01-16 Midday 902` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-15` `Florida4` rank=`3` event=`2026-01-16 Midday 273` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-17` `Florida4` rank=`3` event=`2026-01-19 Midday 863` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-18` `Florida4` rank=`3` event=`2026-01-19 Midday 863` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-16` `NewYork4` rank=`7` event=`2026-01-17 Midday 904` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-17` `NewYork4` rank=`7` event=`2026-01-18 Midday 682` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-18` `NewYork4` rank=`7` event=`2026-01-21 Evening 233` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`

### Same-day carryforward

- `2026-01-16` `Connecticut4` rank=`1` event=`2026-01-16 Evening 431` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-17` `Indiana4` rank=`4` event=`2026-01-17 Evening 065` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-16` `Michigan4` rank=`5` event=`2026-01-16 Evening 633` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-16` `NewJersey4` rank=`6` event=`2026-01-16 Evening 180` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-18` `NewJersey4` rank=`6` event=`2026-01-18 Evening 955` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-15` `NewYork4` rank=`7` event=`2026-01-15 Evening 684` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-18` `NorthCarolina4` rank=`8` event=`2026-01-18 Evening 772` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-15` `Ohio4` rank=`9` event=`2026-01-15 Evening 531` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`

### Right-censored

- _none_

## 6. Interpretation

- Same-day window grading stays clean; this scorecard separately measures delayed resolution within the configured horizon.
- A miss is only a true miss when the full tail is present. Incomplete tail coverage is reported as right_censored.
- Upload-day horizon is the primary setting. Draw-based accounting is preserved as a companion lens because same-day Midday/Evening crossover matters.
- Arena-any-signal state-days gained `18` extra resolutions beyond same-day inside the current decay horizon.
- Same-day carryforward remains distinct from future-day decay and should not be flattened into one generic later-hit bucket.
