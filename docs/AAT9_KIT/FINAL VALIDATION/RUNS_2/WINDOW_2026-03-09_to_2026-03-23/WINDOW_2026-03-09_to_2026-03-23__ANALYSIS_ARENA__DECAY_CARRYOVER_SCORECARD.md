# Analysis Arena Decay / Carryover Scorecard

Purpose:

- keep same-day window metrics clean
- separately measure whether Arena-era state-day snapshots resolve inside a bounded future horizon
- preserve same-day carryforward and future-day decay as different resolution types

## 1. Configured Horizon

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- Results root: `data/results`
- Snapshot dates: `2026-03-09` to `2026-03-23`
- Snapshot upload days: `15`
- Decay horizon: `5` total upload days (same-day included)
- Max draw horizon: `10` total draws
- Tail days required beyond the last snapshot day: `4`
- Results-tail rule: `A 5 total upload-day horizon requires results through snapshot day + 4 days.`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__DECAY_CARRYOVER_ROWS.csv`

## 2. Coverage

- State-day snapshots: `210`
- Full-horizon rows: `210`
- Right-censored rows: `0`
- Max observed upload days: `5`
- Max observed draws: `10`

## 3. Metric Family Scoreboard

| Metric | Active | Same-day | Horizon | Incremental decay lift | Direct same | Same-day precursor | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Board top box core | 210 | 9 (4.3%) | 23 (11.0%) | 14 | 4 | 0 | 5 | 14 | 187 | 0 |
| Board top VTRAC core | 210 | 51 (24.3%) | 167 (79.5%) | 116 | 27 | 0 | 24 | 116 | 43 | 0 |
| Brain 1 box core | 210 | 28 (13.3%) | 98 (46.7%) | 70 | 13 | 0 | 15 | 70 | 112 | 0 |
| Brain 1 VTRAC core | 210 | 103 (49.0%) | 205 (97.6%) | 102 | 52 | 0 | 51 | 102 | 5 | 0 |
| Sandbox box seed | 210 | 27 (12.9%) | 112 (53.3%) | 85 | 11 | 0 | 16 | 85 | 98 | 0 |
| Sandbox exact seed | 210 | 9 (4.3%) | 30 (14.3%) | 21 | 5 | 0 | 4 | 21 | 180 | 0 |
| Sandbox VTRAC seed | 210 | 139 (66.2%) | 210 (100.0%) | 71 | 75 | 0 | 64 | 71 | 0 | 0 |
| Preserved not budgeted | 155 | 1 (0.6%) | 7 (4.5%) | 6 | 1 | 0 | 0 | 6 | 148 | 0 |
| Arena box total | 210 | 34 (16.2%) | 127 (60.5%) | 93 | 15 | 0 | 19 | 93 | 83 | 0 |
| Arena VTRAC total | 210 | 139 (66.2%) | 210 (100.0%) | 71 | 75 | 0 | 64 | 71 | 0 | 0 |

## 4. Cohort Panels

| Cohort | State-days | Same-day | Horizon | Incremental decay lift | Direct same | Same-day carryforward | Future-day decay | Miss | Right-censored |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Arena any signal | 210 | 144 (68.6%) | 210 (100.0%) | 66 | 78 | 66 | 66 | 0 | 0 |
| Top primary target | 15 | 9 (60.0%) | 15 (100.0%) | 6 | 6 | 3 | 6 | 0 | 0 |
| Top-3 ranked states | 45 | 27 (60.0%) | 45 (100.0%) | 18 | 15 | 12 | 18 | 0 | 0 |
| Any tracker hint present | 210 | 144 (68.6%) | 210 (100.0%) | 66 | 78 | 66 | 66 | 0 | 0 |
| Profit-alert hint present | 210 | 144 (68.6%) | 210 (100.0%) | 66 | 78 | 66 | 66 | 0 | 0 |
| Due-double hint present | 210 | 144 (68.6%) | 210 (100.0%) | 66 | 78 | 66 | 66 | 0 | 0 |

## 5. Notable Examples

### Future-day decay

- `2026-03-14` `Connecticut4` rank=`1` event=`2026-03-16 Midday 766` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-03-15` `Connecticut4` rank=`1` event=`2026-03-16 Midday 766` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-03-16` `Connecticut4` rank=`1` event=`2026-03-17 Midday 991` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-03-20` `Connecticut4` rank=`1` event=`2026-03-21 Evening 394` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-03-22` `Connecticut4` rank=`1` event=`2026-03-24 Midday 366` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-03-23` `Connecticut4` rank=`1` event=`2026-03-24 Midday 366` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-03-10` `Delaware4` rank=`2` event=`2026-03-11 Midday 526` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-03-13` `Delaware4` rank=`2` event=`2026-03-14 Midday 675` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`

### Same-day carryforward

- `2026-03-09` `Connecticut4` rank=`1` event=`2026-03-09 Evening 091` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-03-10` `Connecticut4` rank=`1` event=`2026-03-10 Evening 556` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-03-12` `Connecticut4` rank=`1` event=`2026-03-12 Evening 802` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-03-11` `Delaware4` rank=`2` event=`2026-03-11 Evening 179` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-03-12` `Delaware4` rank=`2` event=`2026-03-12 Evening 763` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-03-14` `Delaware4` rank=`2` event=`2026-03-14 Evening 474` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`
- `2026-03-16` `Delaware4` rank=`2` event=`2026-03-16 Evening 545` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, preserved_not_budgeted, arena_box_total, arena_vt_total`
- `2026-03-18` `Delaware4` rank=`2` event=`2026-03-18 Evening 483` metrics=`board_top_box_core, board_top_vt_core, brain1_box_core, brain1_vt_core, sandbox_box_seed, sandbox_exact_seed, sandbox_vt_seed, arena_box_total, arena_vt_total`

### Right-censored

- _none_

## 6. Interpretation

- Same-day window grading stays clean; this scorecard separately measures delayed resolution within the configured horizon.
- A miss is only a true miss when the full tail is present. Incomplete tail coverage is reported as right_censored.
- Upload-day horizon is the primary setting. Draw-based accounting is preserved as a companion lens because same-day Midday/Evening crossover matters.
- Arena-any-signal state-days gained `66` extra resolutions beyond same-day inside the current decay horizon.
- Same-day carryforward remains distinct from future-day decay and should not be flattened into one generic later-hit bucket.
