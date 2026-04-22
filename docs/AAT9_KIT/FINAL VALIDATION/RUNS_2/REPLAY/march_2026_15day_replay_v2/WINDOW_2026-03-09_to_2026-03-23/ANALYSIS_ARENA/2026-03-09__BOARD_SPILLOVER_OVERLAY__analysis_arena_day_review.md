# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-09

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `b82fcc82ed1ac078`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 168, 189, 006, 019, 668, 199, 018 | 18, 9, 25, 23, 24, 15, 8, 21 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |
| 2 | Delaware4 | 006, 129, 259, 478, 244, 249, 599, 788 | 12, 31, 2, 33, 22, 15, 14, 30 | - | - | shared_host | Combined:OFF/0, Midday:OFF/0, Evening:OFF/0 |
| 3 | Florida4 | 224, 778, 889, 004, 189, 488, 489, 148 | 28, 33, 27, 15, 31, 25, 24, 5 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 4 | Indiana4 | 011, 225, 255, 559, 223, 088, 113, 788 | 3, 10, 6, 27, 13, 4, 11, 1 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:OFF/1 |
| 5 | Michigan4 | 118, 778, 188, 334, 378, 255, 114 | 18, 27, 23, 33, 3, 24, 19, 29 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 006, 177, 007, 229, 259, 009, 677, 069 | 20, 28, 12, 2, 5, 15, 17, 31 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/1, Midday:OFF/0 |
| 7 | NewYork4 | 559, 368, 689, 224, 059, 299, 589, 778 | 5, 23, 24, 28, 32, 2, 15, 27 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 8 | NorthCarolina4 | 599, 003, 344, 034, 188, 035, 445, 009 | 15, 4, 5, 34, 23, 18, 14, 2 | - | - | shared_host | Combined:ALERT/3, Midday:ALERT/3, Evening:ALERT/3 |
| 9 | Ohio4 | 599, 559, 003, 069, 569, 224, 002, 022 | 5, 15, 9, 4, 3, 33, 28, 10 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 10 | OntarioCanada4 | 559, 899, 599, 199, 049, 077, 019 | 5, 15, 31, 25, 34, 35, 9, 7 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 559, 008, 024, 002, 025, 009, 088, 007 | 5, 12, 4, 3, 1, 32, 13, 11 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 12 | PuertoRico4 | 177, 359, 339, 559, 599, 117, 179 | 20, 14, 15, 12, 17, 33, 19, 5 | - | - | shared_host | Combined:ALERT/3, Midday:WATCH/2, Evening:WATCH/2 |
| 13 | SouthCarolina4 | 667, 006, 069, 007, 009, 077, 002, 224 | 17, 2, 5, 9, 10, 3, 15, 1 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 14 | Virginia4 | 039, 599, 358, 138, 009, 559, 005, 334 | 15, 5, 14, 13, 1, 23, 32, 2 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 226 | 29 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 235 | 31 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 209 | 27 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 240 | 31 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 199 | 25 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 264 | 34 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 255 | 33 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 241 | 28 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 344 | 43 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 314 | 35 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Ohio4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 045, 059, 099, 559, 599 | 8 | 13 | False | True |
| OntarioCanada4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 15 | 044, 049, 099, 445, 459, 599 | 6 | 12 | False | True |
| Indiana4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 002, 005, 007, 008, 025, 559 | 7 | 12 | False | True |
| Connecticut4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 011, 013, 017, 118, 168 | 6 | 11 | False | True |
| Indiana4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 008, 011, 559 | 6 | 11 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 23, 31, 33, 34, 5 | - | 7 | 11 | False | True |
| Virginia4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 1, 14 | 005, 048, 089, 359 | 4 | 10 | False | True |
| Connecticut4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 013, 017, 099, 199 | 5 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 006, 013, 069, 667 | 5 | 10 | False | True |
| Florida4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 009, 224, 229, 477 | 5 | 10 | False | True |
| NewJersey4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 009, 069 | 5 | 10 | False | True |
| NorthCarolina4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 044, 599 | 5 | 10 | False | True |
| NorthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 099, 599 | 5 | 10 | False | True |
| OntarioCanada4 | Virginia4 | shared_box_family | lane/family | primary | - | 009, 059, 099, 559, 599 | 5 | 10 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 008, 559 | 5 | 10 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 009, 559 | 5 | 10 | False | True |
| Pennsylvania4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 009, 059, 559 | 5 | 10 | False | True |
| PuertoRico4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 117, 559 | 5 | 10 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 001, 005, 006, 009, 559 | 5 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 17, 18, 2, 21, 23, 9 | - | 6 | 10 | False | True |
| Delaware4 | PuertoRico4 | shared_lane | lane/family | primary | 12, 15, 18, 23, 31, 33 | - | 6 | 10 | False | True |
| Florida4 | Ohio4 | shared_lane | lane/family | primary | 15, 23, 28, 33, 5, 9 | - | 6 | 10 | False | True |
| NorthCarolina4 | PuertoRico4 | shared_lane | lane/family | primary | 14, 15, 18, 23, 34, 5 | - | 6 | 10 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 006, 011, 013, 017 | 4 | 9 | False | True |
| Connecticut4 | Ohio4 | shared_box_family | lane/family | primary | - | 011, 017, 069, 099 | 4 | 9 | False | True |
| Connecticut4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 001, 011, 017, 019 | 4 | 9 | False | True |
| Delaware4 | Michigan4 | shared_box_family | lane/family | primary | - | 011, 013, 017, 119 | 4 | 9 | False | True |
| Delaware4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 013, 014, 017 | 4 | 9 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 011, 057, 255 | 4 | 9 | False | True |
| Indiana4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 559 | 4 | 9 | False | True |
| NewJersey4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 009 | 4 | 9 | False | True |
| NewJersey4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 005, 007, 177, 677 | 4 | 9 | False | True |
| NewYork4 | Ohio4 | shared_box_family | lane/family | primary | - | 059, 224, 455, 559 | 4 | 9 | False | True |
| NewYork4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 059, 138, 559 | 4 | 9 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 009, 049, 099, 599 | 4 | 9 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 009 | 4 | 9 | False | True |
| NorthCarolina4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 005, 007, 009 | 4 | 9 | False | True |
| Ohio4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 011, 017, 559, 599 | 4 | 9 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 059, 099, 559, 599 | 4 | 9 | False | True |
| OntarioCanada4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 009, 059, 559 | 4 | 9 | False | True |

## Strongest Overlap Pairs

- `Ohio4 ↔ OntarioCanada4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ SouthCarolina4` score=`35` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Pennsylvania4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ SouthCarolina4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `PuertoRico4 ↔ Virginia4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Ohio4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewYork4 ↔ Ohio4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `OntarioCanada4 ↔ Virginia4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ Virginia4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NewJersey4 ↔ Ohio4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
