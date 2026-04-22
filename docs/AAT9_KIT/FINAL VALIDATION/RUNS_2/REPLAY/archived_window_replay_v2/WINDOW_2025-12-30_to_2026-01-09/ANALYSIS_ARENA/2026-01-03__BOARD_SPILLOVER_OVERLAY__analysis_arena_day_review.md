# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-03

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `5bd458b170e60b54`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 048, 478, 368, 001, 224, 456, 011, 249 | 14, 31, 23, 9, 30, 15, 32, 2 | - | - | shared_host | Midday:OFF/1, Evening:OFF/1, Combined:OFF/0 |
| 2 | Delaware4 | 449, 004, 599, 559, 244, 014, 144, 114 | 5, 35, 31, 15, 22, 25, 28, 9 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 3 | Florida4 | 138, 599, 559, 346, 368, 445 | 23, 15, 5, 24, 32, 9, 10, 18 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/1, Midday:OFF/0 |
| 4 | Indiana4 | 244, 368, 668, 138, 168, 066 | 23, 18, 31, 6, 16, 17, 9, 20 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 5 | Michigan4 | 006, 668, 016, 336, 168, 166, 133 | 18, 2, 6, 23, 19, 9, 25, 16 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/0 |
| 6 | NewJersey4 | 299, 599, 899, 229, 248, 199 | 31, 15, 30, 28, 34, 1, 10, 5 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 7 | NewYork4 | 788, 889, 038, 066, 025, 026, 667, 249 | 7, 29, 3, 33, 13, 6, 18, 31 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/0 |
| 8 | NorthCarolina4 | 229, 224, 299, 004, 044, 223, 029 | 28, 5, 31, 12, 15, 1, 4, 27 | - | - | shared_host | Evening:ALERT/4, Combined:WATCH/2, Midday:OFF/1 |
| 9 | Ohio4 | 559, 255, 055, 599, 088, 008, 257, 688 | 5, 3, 10, 1, 12, 13, 15, 4 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 10 | OntarioCanada4 | 267, 255, 188, 118, 007, 167, 559 | 20, 3, 10, 7, 17, 21, 18, 23 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 11 | Pennsylvania4 | 559, 599, 059, 579, 007, 899, 359 | 5, 15, 3, 12, 9, 34, 33, 29 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/1 |
| 12 | PuertoRico4 | 344, 225, 226, 003, 022, 002, 236, 224 | 10, 34, 20, 18, 3, 24, 31, 7 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 13 | SouthCarolina4 | 559, 002, 008, 007, 255, 189, 015, 118 | 3, 5, 4, 18, 28, 12, 2, 11 | - | - | shared_host | Midday:ALERT/3, Combined:OFF/1, Evening:OFF/1 |
| 14 | Virginia4 | 224, 229, 334, 177, 179, 477, 337, 227 | 28, 20, 26, 31, 27, 10, 22, 29 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 280 | 34 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 334 | 42 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 266 | 32 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 225 | 28 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 242 | 31 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 231 | 30 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 176 | 23 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 241 | 30 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 272 | 35 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 221 | 26 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| NewJersey4 | Florida4 | alert_implied_echo | lane/family | primary | 23, 15 | 133, 138, 188, 336, 368, 599, 688 | 7 | 13 | False | True |
| Delaware4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 009, 017, 045, 455, 559, 599 | 7 | 12 | False | True |
| Florida4 | Indiana4 | shared_box_family | lane/family | primary | - | 011, 014, 066, 138, 188, 368, 688 | 7 | 12 | False | True |
| Indiana4 | Michigan4 | shared_box_family | lane/family | primary | - | 011, 013, 014, 017, 168, 366, 668 | 7 | 12 | False | True |
| Florida4 | Ohio4 | shared_box_family | lane/family | primary | - | 014, 057, 077, 559, 599, 688 | 6 | 11 | False | True |
| NewJersey4 | Indiana4 | alert_implied_echo | lane/family | primary | 23 | 138, 188, 368, 688 | 4 | 10 | False | True |
| Delaware4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 004, 009, 044, 045, 559 | 5 | 10 | False | True |
| NewJersey4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 004, 005, 229, 299 | 5 | 10 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 009, 057, 059, 559, 599 | 5 | 10 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 008, 009, 255, 559 | 5 | 10 | False | True |
| Delaware4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 045 | 3 | 9 | False | True |
| Delaware4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 5 | 004, 009, 045 | 3 | 9 | False | True |
| Indiana4 | NewJersey4 | alert_implied_echo | lane/family | primary | 31 | 249, 299, 799 | 3 | 9 | False | True |
| Michigan4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 2 | 001, 006, 015 | 3 | 9 | False | True |
| Pennsylvania4 | Delaware4 | alert_implied_echo | lane/family | primary | 5 | 045, 455, 559 | 3 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 004, 011, 014, 244 | 4 | 9 | False | True |
| Connecticut4 | Florida4 | shared_box_family | lane/family | primary | - | 011, 014, 057, 368 | 4 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_box_family | lane/family | primary | - | 011, 014, 244, 368 | 4 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 004, 014, 249 | 4 | 9 | False | True |
| Delaware4 | Florida4 | shared_box_family | lane/family | primary | - | 011, 014, 559, 599 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 244 | 4 | 9 | False | True |
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 009, 014, 559, 599 | 4 | 9 | False | True |
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 044 | 4 | 9 | False | True |
| Indiana4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 014, 017, 188, 677 | 4 | 9 | False | True |
| NorthCarolina4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 009, 045, 559 | 4 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_lane | lane/family | primary | 15, 18, 31, 5, 9 | - | 5 | 9 | False | True |
| Connecticut4 | NorthCarolina4 | shared_lane | lane/family | primary | 15, 23, 28, 31, 5 | - | 5 | 9 | False | True |
| Connecticut4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 23, 5, 9 | - | 5 | 9 | False | True |
| Delaware4 | Pennsylvania4 | shared_lane | lane/family | primary | 15, 18, 34, 5, 9 | - | 5 | 9 | False | True |
| OntarioCanada4 | PuertoRico4 | shared_lane | lane/family | primary | 10, 18, 20, 23, 3 | - | 5 | 9 | False | True |
| Pennsylvania4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 18, 23, 3, 34 | - | 5 | 9 | False | True |
| Delaware4 | Connecticut4 | alert_implied_echo | lane/family | primary | 5, 9 | 004, 014 | 2 | 8 | False | True |
| Delaware4 | NewJersey4 | alert_implied_echo | lane/family | primary | 5, 9 | 004, 014 | 2 | 8 | False | True |
| Delaware4 | Ohio4 | alert_implied_echo | lane/family | primary | 5, 9 | 009, 014 | 2 | 8 | False | True |
| Florida4 | Ohio4 | alert_implied_echo | lane/family | primary | 10, 5 | 077, 559 | 2 | 8 | False | True |
| Indiana4 | Connecticut4 | alert_implied_echo | lane/family | primary | 31 | 244, 249 | 2 | 8 | False | True |
| Michigan4 | Connecticut4 | alert_implied_echo | lane/family | primary | 2 | 001, 006 | 2 | 8 | False | True |
| NewJersey4 | Ohio4 | alert_implied_echo | lane/family | primary | 15, 23 | 599, 688 | 2 | 8 | False | True |
| Pennsylvania4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 5 | 045, 559 | 2 | 8 | False | True |
| Pennsylvania4 | Ohio4 | alert_implied_echo | lane/family | primary | 5 | 059, 559 | 2 | 8 | False | True |

## Strongest Overlap Pairs

- `Delaware4 ↔ Pennsylvania4` score=`39` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Michigan4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NorthCarolina4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ Pennsylvania4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Ohio4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Michigan4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ NewJersey4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Ohio4 ↔ SouthCarolina4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Florida4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NewJersey4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
