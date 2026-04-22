# Analysis Arena Decay / Carryover Scorecard

Purpose:

- keep same-day window metrics clean
- separately measure whether Arena-era state-day snapshots resolve inside a bounded future horizon
- preserve same-day carryforward and future-day decay as different resolution types

## 1. Configured Horizon

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22`
- Results root: `data/results`
- Snapshot dates: `2026-01-20` to `2026-01-22`
- Snapshot upload days: `3`
- Decay horizon: `5` total upload days (same-day included)
- Max draw horizon: `10` total draws
- Tail days required beyond the last snapshot day: `4`
- Results-tail rule: `A 5 total upload-day horizon requires results through snapshot day + 4 days.`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__DECAY_CARRYOVER_ROWS.csv`

## 2. Coverage

- State-day snapshots: `42`
- Full-horizon rows: `42`
- Right-censored rows: `0`
- Max observed upload days: `5`
- Max observed draws: `10`

## 3. Metric Family Scoreboard

| Metric | Active | Same-day | Horizon | Incremental decay lift | Direct same | Same-day precursor | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Board top box core | 42 | 1 (2.4%) | 5 (11.9%) | 4 | 0 | 0 | 1 | 4 | 37 | 0 |
| Board top VTRAC core | 42 | 12 (28.6%) | 25 (59.5%) | 13 | 6 | 0 | 6 | 13 | 17 | 0 |
| Brain 1 box core | 42 | 4 (9.5%) | 18 (42.9%) | 14 | 0 | 0 | 4 | 14 | 24 | 0 |
| Brain 1 VTRAC core | 42 | 20 (47.6%) | 36 (85.7%) | 16 | 13 | 0 | 7 | 16 | 6 | 0 |
| Sandbox box seed | 42 | 3 (7.1%) | 16 (38.1%) | 13 | 0 | 0 | 3 | 13 | 26 | 0 |
| Sandbox exact seed | 42 | 1 (2.4%) | 3 (7.1%) | 2 | 0 | 0 | 1 | 2 | 39 | 0 |
| Sandbox VTRAC seed | 42 | 26 (61.9%) | 41 (97.6%) | 15 | 16 | 0 | 10 | 15 | 1 | 0 |
| Preserved not budgeted | 26 | 0 (0.0%) | 2 (7.7%) | 2 | 0 | 0 | 0 | 2 | 24 | 0 |
| Arena box total | 42 | 4 (9.5%) | 21 (50.0%) | 17 | 0 | 0 | 4 | 17 | 21 | 0 |
| Arena VTRAC total | 42 | 26 (61.9%) | 41 (97.6%) | 15 | 17 | 0 | 9 | 15 | 1 | 0 |

## 4. Cohort Panels

| Cohort | State-days | Same-day | Horizon | Incremental decay lift | Direct same | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Arena any signal | 42 | 27 (64.3%) | 42 (100.0%) | 15 | 17 | 10 | 15 | 0 | 0 |
| Top primary target | 3 | 2 (66.7%) | 3 (100.0%) | 1 | 2 | 0 | 1 | 0 | 0 |
| Top-3 ranked states | 9 | 6 (66.7%) | 9 (100.0%) | 3 | 5 | 1 | 3 | 0 | 0 |
| Any tracker hint present | 42 | 27 (64.3%) | 42 (100.0%) | 15 | 17 | 10 | 15 | 0 | 0 |
| Profit-alert hint present | 42 | 27 (64.3%) | 42 (100.0%) | 15 | 17 | 10 | 15 | 0 | 0 |
| Due-double hint present | 42 | 27 (64.3%) | 42 (100.0%) | 15 | 17 | 10 | 15 | 0 | 0 |

## 5. Notable Examples

### Future-day decay

- `2026-01-20` `Connecticut4` rank=`1` event=`2026-01-21 Midday 786` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-20` `Florida4` rank=`3` event=`2026-01-24 Evening 562` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-22` `Florida4` rank=`3` event=`2026-01-24 Evening 562` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-20` `Michigan4` rank=`5` event=`2026-01-21 Midday 220` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-22` `NewYork4` rank=`7` event=`2026-01-23 Evening 771` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-22` `NorthCarolina4` rank=`8` event=`2026-01-23 Midday 235` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-21` `Ohio4` rank=`9` event=`2026-01-22 Midday 217` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-22` `Ohio4` rank=`9` event=`2026-01-23 Midday 709` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`

### Same-day carryforward

- `2026-01-22` `Delaware4` rank=`2` event=`2026-01-22 Evening 243` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-20` `Indiana4` rank=`4` event=`2026-01-20 Evening 208` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-22` `Michigan4` rank=`5` event=`2026-01-22 Evening 652` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-22` `NewJersey4` rank=`6` event=`2026-01-22 Evening 152` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-20` `NewYork4` rank=`7` event=`2026-01-20 Evening 406` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-01-21` `NewYork4` rank=`7` event=`2026-01-21 Evening 233` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-20` `Ohio4` rank=`9` event=`2026-01-20 Evening 843` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-01-22` `OntarioCanada4` rank=`10` event=`2026-01-22 Evening 544` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`

### Right-censored

- _none_

## 6. Interpretation

- Same-day window grading stays clean; this scorecard separately measures delayed resolution within the configured horizon.
- A miss is only a true miss when the full tail is present. Incomplete tail coverage is reported as right_censored.
- Upload-day horizon is the primary setting. Draw-based accounting is preserved as a companion lens because same-day Midday/Evening crossover matters.
- Arena-any-signal state-days gained `15` extra resolutions beyond same-day inside the current decay horizon.
- Same-day carryforward remains distinct from future-day decay and should not be flattened into one generic later-hit bucket.
