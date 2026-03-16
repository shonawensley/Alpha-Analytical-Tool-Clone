# DR Winner Promotion Group Compare

- Purpose: split matched, winner-aware DR rows into promoted vs visible-under-promoted vs buried groups.
- Inputs:
  - `/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-15__DR_GOLD_DAY_AUDIT__DEV__V1_1.csv`
  - `/home/ser/code/Alpha-Analytical-Tool-Clone/docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-15__DR_GOLD_DAY_AUDIT__HOLDOUT__V1_1.csv`

- total audit rows: `383`
- matched + vtrac_any rows: `313`

## Promoted

- rows: `63`
- median signal_score: `538.000`
- median ls_signal_cells: `36.000`
- median cluster_score_gap: `44.189`
- top states: `Indiana4` (8), `NewJersey4` (7), `PuertoRico4` (6), `Florida4` (6), `Connecticut4` (5)
- top alignments: `vtrac_capture` (34), `literal_capture` (29)
- top trace attractors: `559` (15), `259` (9), `244` (5), `599` (4), `299` (4), `055` (4)
- top corridor attractors: `559` (15), `259` (9), `244` (5), `599` (4), `299` (4), `055` (4)
- top double attractors: `559` (19), `599` (6), `592` (5), `244` (5), `992` (4), `224` (3)

| Date | State | Var | Winner | VT | Cluster | Best | Signal | LS | Top corridor | Top double |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-06 | NewJersey4 | Evening | 942 | 31 | 1 | 1 | 1041.0 | 48 | 299 | 992 |
| 2025-06-21 | Connecticut4 | Midday | 950 | 5 | 1 | 1 | 975.5 | 47 | 559 | 559 |
| 2026-01-09 | Ohio4 | Evening | 090 | 5 | 1 | 1 | 954.0 | 50 | 559 | 559 |
| 2025-12-30 | Connecticut4 | Midday | 095 | 5 | 1 | 1 | 930.5 | 57 | 559 | 559 |
| 2025-12-30 | Michigan4 | Midday | 250 | 3 | 1 | 1 | 659.5 | 43 | 599 | 599 |
| 2025-12-31 | SouthCarolina4 | Evening | 044 | 15 | 1 | 1 | 597.5 | 41 | 599 | 599 |
| 2026-01-01 | NewJersey4 | Midday | 770 | 10 | 1 | 1 | 545.0 | 18 | 225 | 522 |
| 2026-01-06 | Florida4 | Midday | 209 | 12 | 1 | 1 | 462.5 | 41 | 259 | 592 |
| 2025-12-31 | Florida4 | Midday | 407 | 12 | 1 | 1 | 445.0 | 32 | 259 | 013 |
| 2025-06-21 | NorthCarolina4 | Midday | 427 | 28 | 1 | 1 | 355.0 | 22 | 224 | 224 |
| 2026-01-08 | NewJersey4 | Evening | 055 | 1 | 1 | 1 | 317.5 | 9 | 055 | 992 |
| 2026-01-03 | Pennsylvania4 | Evening | 909 | 15 | 2 | 1 | 1319.5 | 53 | 559 | 559 |

## Visible Under Promoted

- rows: `23`
- median signal_score: `411.500`
- median ls_signal_cells: `28.000`
- median cluster_score_gap: `82.801`
- top states: `Florida4` (5), `NewJersey4` (4), `Delaware4` (2), `Indiana4` (2), `Virginia4` (2)
- top alignments: `vtrac_capture` (15), `literal_capture` (8)
- top trace attractors: `259` (6), `029` (3), `229` (3), `559` (3), `225` (1), `599` (1)
- top corridor attractors: `259` (6), `029` (3), `229` (3), `559` (3), `225` (1), `599` (1)
- top double attractors: `559` (6), `592` (4), `922` (3), `992` (2), `522` (1), `994` (1)

| Date | State | Var | Winner | VT | Cluster | Best | Signal | LS | Top corridor | Top double |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-07 | NorthCarolina4 | Evening | 202 | 10 | 6 | 6 | 638.0 | 48 | 229 | 922 |
| 2026-01-09 | Florida4 | Evening | 093 | 14 | 6 | 6 | 497.5 | 43 | 445 | 544 |
| 2025-06-22 | Virginia4 | Evening | 938 | 33 | 6 | 6 | 488.0 | 20 | 559 | 559 |
| 2026-01-07 | Virginia4 | Evening | 990 | 15 | 6 | 6 | 419.5 | 37 | 229 | 922 |
| 2025-06-22 | Indiana4 | Evening | 702 | 10 | 6 | 6 | 411.5 | 21 | 229 | 922 |
| 2026-01-04 | Connecticut4 | Midday | 569 | 9 | 6 | 6 | 398.0 | 28 | 345 | 559 |
| 2026-01-07 | Florida4 | Midday | 434 | 34 | 7 | 7 | 1270.5 | 41 | 259 | 559 |
| 2025-12-31 | Ohio4 | Evening | 197 | 22 | 7 | 7 | 340.5 | 25 | 299 | 992 |
| 2026-01-02 | Florida4 | Evening | 589 | 14 | 7 | 7 | 274.5 | 21 | 259 | 559 |
| 2026-01-01 | Indiana4 | Midday | 474 | 31 | 8 | 8 | 489.0 | 22 | 259 | 592 |
| 2025-06-21 | Delaware4 | Midday | 756 | 7 | 8 | 7 | 318.0 | 24 | 225 | 522 |
| 2026-01-07 | Michigan4 | Evening | 616 | 16 | 8 | 8 | 258.0 | 18 | 059 | 590 |

## Buried

- rows: `227`
- median signal_score: `396.000`
- median ls_signal_cells: `26.000`
- median cluster_score_gap: `-`
- top states: `Virginia4` (20), `Connecticut4` (19), `Ohio4` (19), `NorthCarolina4` (18), `Pennsylvania4` (18)
- top alignments: `vtrac_capture` (136), `literal_capture` (91)
- top trace attractors: `559` (40), `259` (34), `599` (24), `299` (20), `255` (16), `229` (14)
- top corridor attractors: `559` (42), `259` (35), `599` (22), `299` (20), `255` (17), `229` (13)
- top double attractors: `559` (45), `592` (28), `599` (27), `992` (20), `552` (19), `922` (16)

| Date | State | Var | Winner | VT | Cluster | Best | Signal | LS | Top corridor | Top double |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-01-04 | Indiana4 | Midday | 813 | 23 | - | 1 | 1720.0 | 64 | 259 | 592 |
| 2026-01-06 | Michigan4 | Midday | 618 | 18 | - | 1 | 1712.0 | 70 | 449 | 944 |
| 2025-12-31 | Virginia4 | Evening | 636 | 18 | - | 1 | 1342.5 | 61 | 299 | 599 |
| 2026-01-09 | Delaware4 | Midday | 843 | 33 | - | 11 | 1234.0 | 14 | 559 | 559 |
| 2025-06-21 | Ohio4 | Evening | 868 | 23 | - | 4 | 1065.0 | 44 | 559 | 559 |
| 2026-01-09 | Pennsylvania4 | Midday | 811 | 18 | - | 3 | 1054.5 | 59 | 559 | 559 |
| 2025-06-23 | Connecticut4 | Evening | 938 | 33 | - | 12 | 997.5 | 47 | 445 | 544 |
| 2026-01-02 | NorthCarolina4 | Midday | 033 | 13 | - | 11 | 938.0 | 52 | 229 | 922 |
| 2026-01-04 | Virginia4 | Evening | 217 | 20 | - | 17 | 915.5 | 39 | 259 | 592 |
| 2025-06-23 | Ohio4 | Evening | 368 | 23 | - | 1 | 913.5 | 55 | 559 | 559 |
| 2025-12-30 | Florida4 | Midday | 377 | 27 | - | - | 880.0 | 54 | 259 | 592 |
| 2026-01-07 | Florida4 | Evening | 963 | 24 | - | 13 | 806.0 | 56 | 445 | 544 |
