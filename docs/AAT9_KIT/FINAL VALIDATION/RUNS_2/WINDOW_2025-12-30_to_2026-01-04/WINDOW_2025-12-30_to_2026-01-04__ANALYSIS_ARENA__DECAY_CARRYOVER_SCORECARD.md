# Analysis Arena Decay / Carryover Scorecard

Purpose:

- keep same-day window metrics clean
- separately measure whether Arena-era state-day snapshots resolve inside a bounded future horizon
- preserve same-day carryforward and future-day decay as different resolution types

## 1. Configured Horizon

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04`
- Results root: `data/results`
- Snapshot dates: `2025-12-30` to `2026-01-04`
- Snapshot upload days: `6`
- Decay horizon: `5` total upload days (same-day included)
- Max draw horizon: `10` total draws
- Tail days required beyond the last snapshot day: `4`
- Results-tail rule: `A 5 total upload-day horizon requires results through snapshot day + 4 days.`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__DECAY_CARRYOVER_ROWS.csv`

## 2. Coverage

- State-day snapshots: `84`
- Full-horizon rows: `84`
- Right-censored rows: `0`
- Max observed upload days: `5`
- Max observed draws: `10`

## 3. Metric Family Scoreboard

| Metric | Active | Same-day | Horizon | Incremental decay lift | Direct same | Same-day precursor | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Board top box core | 84 | 2 (2.4%) | 13 (15.5%) | 11 | 1 | 0 | 1 | 11 | 71 | 0 |
| Board top VTRAC core | 84 | 20 (23.8%) | 53 (63.1%) | 33 | 17 | 0 | 3 | 33 | 31 | 0 |
| Brain 1 box core | 84 | 9 (10.7%) | 31 (36.9%) | 22 | 6 | 0 | 3 | 22 | 53 | 0 |
| Brain 1 VTRAC core | 84 | 32 (38.1%) | 78 (92.9%) | 46 | 22 | 0 | 10 | 46 | 6 | 0 |
| Sandbox box seed | 84 | 7 (8.3%) | 33 (39.3%) | 26 | 4 | 0 | 3 | 26 | 51 | 0 |
| Sandbox exact seed | 84 | 1 (1.2%) | 13 (15.5%) | 12 | 1 | 0 | 0 | 12 | 71 | 0 |
| Sandbox VTRAC seed | 84 | 49 (58.3%) | 82 (97.6%) | 33 | 31 | 0 | 18 | 33 | 2 | 0 |
| Preserved not budgeted | 64 | 3 (4.7%) | 9 (14.1%) | 6 | 2 | 0 | 1 | 6 | 55 | 0 |
| Arena box total | 84 | 13 (15.5%) | 48 (57.1%) | 35 | 9 | 0 | 4 | 35 | 36 | 0 |
| Arena VTRAC total | 84 | 49 (58.3%) | 82 (97.6%) | 33 | 31 | 0 | 18 | 33 | 2 | 0 |

## 4. Cohort Panels

| Cohort | State-days | Same-day | Horizon | Incremental decay lift | Direct same | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Arena any signal | 84 | 51 (60.7%) | 83 (98.8%) | 32 | 33 | 18 | 32 | 1 | 0 |
| Top primary target | 6 | 5 (83.3%) | 6 (100.0%) | 1 | 3 | 2 | 1 | 0 | 0 |
| Top-3 ranked states | 18 | 10 (55.6%) | 18 (100.0%) | 8 | 8 | 2 | 8 | 0 | 0 |
| Any tracker hint present | 84 | 51 (60.7%) | 83 (98.8%) | 32 | 33 | 18 | 32 | 1 | 0 |
| Profit-alert hint present | 84 | 51 (60.7%) | 83 (98.8%) | 32 | 33 | 18 | 32 | 1 | 0 |
| Due-double hint present | 84 | 51 (60.7%) | 83 (98.8%) | 32 | 33 | 18 | 32 | 1 | 0 |

## 5. Notable Examples

### Future-day decay

- `2026-01-01` `Connecticut4` rank=`1` event=`2026-01-02 Midday 970` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2025-12-31` `Delaware4` rank=`2` event=`2026-01-01 Midday 149` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-02` `Delaware4` rank=`2` event=`2026-01-04 Evening 269` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-03` `Delaware4` rank=`2` event=`2026-01-04 Midday 057` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-04` `Delaware4` rank=`2` event=`2026-01-06 Evening 758` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-01` `Florida4` rank=`3` event=`2026-01-03 Midday 708` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-02` `Florida4` rank=`3` event=`2026-01-03 Midday 708` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-04` `Florida4` rank=`3` event=`2026-01-05 Midday 080` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`

### Same-day carryforward

- `2025-12-31` `Connecticut4` rank=`1` event=`2025-12-31 Evening 361` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-03` `Connecticut4` rank=`1` event=`2026-01-03 Evening 181` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2025-12-30` `Indiana4` rank=`4` event=`2025-12-30 Evening 512` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-03` `Michigan4` rank=`5` event=`2026-01-03 Evening 479` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2025-12-30` `NewJersey4` rank=`6` event=`2025-12-30 Evening 356` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2025-12-31` `NewYork4` rank=`7` event=`2025-12-31 Evening 116` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-01` `NorthCarolina4` rank=`8` event=`2026-01-01 Evening 053` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2025-12-30` `Ohio4` rank=`9` event=`2025-12-30 Evening 327` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`

### Right-censored

- _none_

## 6. Interpretation

- Same-day window grading stays clean; this scorecard separately measures delayed resolution within the configured horizon.
- A miss is only a true miss when the full tail is present. Incomplete tail coverage is reported as right_censored.
- Upload-day horizon is the primary setting. Draw-based accounting is preserved as a companion lens because same-day Midday/Evening crossover matters.
- Arena-any-signal state-days gained `32` extra resolutions beyond same-day inside the current decay horizon.
- Same-day carryforward remains distinct from future-day decay and should not be flattened into one generic later-hit bucket.
