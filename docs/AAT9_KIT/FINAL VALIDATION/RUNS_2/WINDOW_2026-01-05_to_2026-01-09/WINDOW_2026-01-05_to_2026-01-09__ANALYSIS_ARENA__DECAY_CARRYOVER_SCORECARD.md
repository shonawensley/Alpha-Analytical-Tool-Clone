# Analysis Arena Decay / Carryover Scorecard

Purpose:

- keep same-day window metrics clean
- separately measure whether Arena-era state-day snapshots resolve inside a bounded future horizon
- preserve same-day carryforward and future-day decay as different resolution types

## 1. Configured Horizon

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09`
- Results root: `data/results`
- Snapshot dates: `2026-01-05` to `2026-01-09`
- Snapshot upload days: `5`
- Decay horizon: `5` total upload days (same-day included)
- Max draw horizon: `10` total draws
- Tail days required beyond the last snapshot day: `4`
- Results-tail rule: `A 5 total upload-day horizon requires results through snapshot day + 4 days.`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__DECAY_CARRYOVER_ROWS.csv`

## 2. Coverage

- State-day snapshots: `70`
- Full-horizon rows: `14`
- Right-censored rows: `56`
- Max observed upload days: `5`
- Max observed draws: `10`

## 3. Metric Family Scoreboard

| Metric | Active | Same-day | Horizon | Incremental decay lift | Direct same | Same-day precursor | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Board top box core | 70 | 2 (2.9%) | 8 (11.4%) | 6 | 2 | 0 | 0 | 6 | 10 | 52 |
| Board top VTRAC core | 70 | 12 (17.1%) | 36 (51.4%) | 24 | 5 | 0 | 7 | 24 | 6 | 28 |
| Brain 1 box core | 70 | 6 (8.6%) | 21 (30.0%) | 15 | 4 | 0 | 2 | 15 | 8 | 41 |
| Brain 1 VTRAC core | 70 | 25 (35.7%) | 50 (71.4%) | 25 | 13 | 0 | 12 | 25 | 2 | 18 |
| Sandbox box seed | 70 | 8 (11.4%) | 27 (38.6%) | 19 | 6 | 0 | 2 | 19 | 5 | 38 |
| Sandbox exact seed | 70 | 3 (4.3%) | 17 (24.3%) | 14 | 2 | 0 | 1 | 14 | 9 | 44 |
| Sandbox VTRAC seed | 70 | 39 (55.7%) | 61 (87.1%) | 22 | 24 | 0 | 15 | 22 | 0 | 9 |
| Preserved not budgeted | 66 | 2 (3.0%) | 5 (7.6%) | 3 | 0 | 0 | 2 | 3 | 13 | 48 |
| Arena box total | 70 | 10 (14.3%) | 30 (42.9%) | 20 | 6 | 0 | 4 | 20 | 4 | 36 |
| Arena VTRAC total | 70 | 39 (55.7%) | 61 (87.1%) | 22 | 24 | 0 | 15 | 22 | 0 | 9 |

## 4. Cohort Panels

| Cohort | State-days | Same-day | Horizon | Incremental decay lift | Direct same | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Arena any signal | 70 | 43 (61.4%) | 62 (88.6%) | 19 | 26 | 17 | 19 | 0 | 8 |
| Top primary target | 5 | 4 (80.0%) | 5 (100.0%) | 1 | 3 | 1 | 1 | 0 | 0 |
| Top-3 ranked states | 15 | 10 (66.7%) | 15 (100.0%) | 5 | 8 | 2 | 5 | 0 | 0 |
| Any tracker hint present | 70 | 43 (61.4%) | 62 (88.6%) | 19 | 26 | 17 | 19 | 0 | 8 |
| Profit-alert hint present | 70 | 43 (61.4%) | 62 (88.6%) | 19 | 26 | 17 | 19 | 0 | 8 |
| Due-double hint present | 70 | 43 (61.4%) | 62 (88.6%) | 19 | 26 | 17 | 19 | 0 | 8 |

## 5. Notable Examples

### Future-day decay

- `2026-01-07` `Connecticut4` rank=`1` event=`2026-01-08 Evening 331` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-05` `Delaware4` rank=`2` event=`2026-01-09 Midday 843` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-07` `Delaware4` rank=`2` event=`2026-01-08 Evening 031` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-08` `Delaware4` rank=`2` event=`2026-01-09 Midday 843` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-06` `Florida4` rank=`3` event=`2026-01-07 Midday 434` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-05` `Indiana4` rank=`4` event=`2026-01-07 Evening 290` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-05` `NewJersey4` rank=`6` event=`2026-01-06 Evening 942` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-07` `NewJersey4` rank=`6` event=`2026-01-08 Evening 055` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`

### Same-day carryforward

- `2026-01-08` `Connecticut4` rank=`1` event=`2026-01-08 Evening 331` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-07` `Florida4` rank=`3` event=`2026-01-07 Evening 963` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-07` `Indiana4` rank=`4` event=`2026-01-07 Evening 290` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-06` `NewJersey4` rank=`6` event=`2026-01-06 Evening 942` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-06` `NorthCarolina4` rank=`8` event=`2026-01-06 Evening 298` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-07` `NorthCarolina4` rank=`8` event=`2026-01-07 Evening 202` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-09` `NorthCarolina4` rank=`8` event=`2026-01-09 Evening 960` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-07` `Ohio4` rank=`9` event=`2026-01-07 Evening 204` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`

### Right-censored

- `2026-01-08` `Indiana4` rank=`4` event=`-` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-09` `Indiana4` rank=`4` event=`-` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-08` `Michigan4` rank=`5` event=`-` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-09` `Michigan4` rank=`5` event=`-` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-08` `NewYork4` rank=`7` event=`-` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-09` `NewYork4` rank=`7` event=`-` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-08` `NorthCarolina4` rank=`8` event=`-` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-09` `OntarioCanada4` rank=`10` event=`-` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`

## 6. Interpretation

- Same-day window grading stays clean; this scorecard separately measures delayed resolution within the configured horizon.
- A miss is only a true miss when the full tail is present. Incomplete tail coverage is reported as right_censored.
- Upload-day horizon is the primary setting. Draw-based accounting is preserved as a companion lens because same-day Midday/Evening crossover matters.
- Arena-any-signal state-days gained `19` extra resolutions beyond same-day inside the current decay horizon.
- Same-day carryforward remains distinct from future-day decay and should not be flattened into one generic later-hit bucket.
