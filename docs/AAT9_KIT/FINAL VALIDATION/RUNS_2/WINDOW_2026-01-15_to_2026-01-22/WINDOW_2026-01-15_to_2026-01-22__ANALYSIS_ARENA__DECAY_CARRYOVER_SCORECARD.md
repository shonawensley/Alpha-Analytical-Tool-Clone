# Analysis Arena Decay / Carryover Scorecard

Purpose:

- keep same-day window metrics clean
- separately measure whether Arena-era state-day snapshots resolve inside a bounded future horizon
- preserve same-day carryforward and future-day decay as different resolution types

## 1. Configured Horizon

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22`
- Results root: `data/results`
- Snapshot dates: `2026-01-15` to `2026-01-22`
- Snapshot upload days: `8`
- Decay horizon: `5` total upload days (same-day included)
- Max draw horizon: `10` total draws
- Tail days required beyond the last snapshot day: `4`
- Results-tail rule: `A 5 total upload-day horizon requires results through snapshot day + 4 days.`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/WINDOW_2026-01-15_to_2026-01-22__ANALYSIS_ARENA__DECAY_CARRYOVER_ROWS.csv`

## 2. Coverage

- State-day snapshots: `112`
- Full-horizon rows: `112`
- Right-censored rows: `0`
- Max observed upload days: `5`
- Max observed draws: `10`

## 3. Metric Family Scoreboard

| Metric | Active | Same-day | Horizon | Incremental decay lift | Direct same | Same-day precursor | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Board top box core | 112 | 4 (3.6%) | 16 (14.3%) | 12 | 0 | 0 | 4 | 12 | 96 | 0 |
| Board top VTRAC core | 112 | 31 (27.7%) | 68 (60.7%) | 37 | 16 | 0 | 15 | 37 | 44 | 0 |
| Brain 1 box core | 112 | 13 (11.6%) | 48 (42.9%) | 35 | 3 | 0 | 10 | 35 | 64 | 0 |
| Brain 1 VTRAC core | 112 | 51 (45.5%) | 100 (89.3%) | 49 | 32 | 0 | 19 | 49 | 12 | 0 |
| Sandbox box seed | 112 | 15 (13.4%) | 47 (42.0%) | 32 | 4 | 0 | 11 | 32 | 65 | 0 |
| Sandbox exact seed | 112 | 2 (1.8%) | 6 (5.4%) | 4 | 1 | 0 | 1 | 4 | 106 | 0 |
| Sandbox VTRAC seed | 112 | 67 (59.8%) | 110 (98.2%) | 43 | 40 | 0 | 27 | 43 | 2 | 0 |
| Preserved not budgeted | 94 | 1 (1.1%) | 5 (5.3%) | 4 | 0 | 0 | 1 | 4 | 89 | 0 |
| Arena box total | 112 | 20 (17.9%) | 61 (54.5%) | 41 | 5 | 0 | 15 | 41 | 51 | 0 |
| Arena VTRAC total | 112 | 67 (59.8%) | 110 (98.2%) | 43 | 41 | 0 | 26 | 43 | 2 | 0 |

## 4. Cohort Panels

| Cohort | State-days | Same-day | Horizon | Incremental decay lift | Direct same | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Arena any signal | 112 | 71 (63.4%) | 111 (99.1%) | 40 | 43 | 28 | 40 | 1 | 0 |
| Top primary target | 8 | 5 (62.5%) | 8 (100.0%) | 3 | 4 | 1 | 3 | 0 | 0 |
| Top-3 ranked states | 24 | 14 (58.3%) | 24 (100.0%) | 10 | 12 | 2 | 10 | 0 | 0 |
| Any tracker hint present | 112 | 71 (63.4%) | 111 (99.1%) | 40 | 43 | 28 | 40 | 1 | 0 |
| Profit-alert hint present | 112 | 71 (63.4%) | 111 (99.1%) | 40 | 43 | 28 | 40 | 1 | 0 |
| Due-double hint present | 112 | 71 (63.4%) | 111 (99.1%) | 40 | 43 | 28 | 40 | 1 | 0 |

## 5. Notable Examples

### Future-day decay

- `2026-01-17` `Connecticut4` rank=`1` event=`2026-01-19 Evening 429` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-19` `Connecticut4` rank=`1` event=`2026-01-21 Midday 786` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-20` `Connecticut4` rank=`1` event=`2026-01-21 Midday 786` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-15` `Delaware4` rank=`2` event=`2026-01-16 Midday 902` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-19` `Delaware4` rank=`2` event=`2026-01-20 Midday 099` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-15` `Florida4` rank=`3` event=`2026-01-16 Midday 273` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-17` `Florida4` rank=`3` event=`2026-01-19 Midday 863` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-18` `Florida4` rank=`3` event=`2026-01-19 Midday 863` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`

### Same-day carryforward

- `2026-01-16` `Connecticut4` rank=`1` event=`2026-01-16 Evening 431` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-22` `Delaware4` rank=`2` event=`2026-01-22 Evening 243` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-17` `Indiana4` rank=`4` event=`2026-01-17 Evening 065` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-19` `Indiana4` rank=`4` event=`2026-01-19 Evening 109` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-20` `Indiana4` rank=`4` event=`2026-01-20 Evening 208` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-16` `Michigan4` rank=`5` event=`2026-01-16 Evening 633` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-19` `Michigan4` rank=`5` event=`2026-01-19 Evening 402` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-22` `Michigan4` rank=`5` event=`2026-01-22 Evening 652` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`

### Right-censored

- _none_

## 6. Interpretation

- Same-day window grading stays clean; this scorecard separately measures delayed resolution within the configured horizon.
- A miss is only a true miss when the full tail is present. Incomplete tail coverage is reported as right_censored.
- Upload-day horizon is the primary setting. Draw-based accounting is preserved as a companion lens because same-day Midday/Evening crossover matters.
- Arena-any-signal state-days gained `40` extra resolutions beyond same-day inside the current decay horizon.
- Same-day carryforward remains distinct from future-day decay and should not be flattened into one generic later-hit bucket.
