# Board Spillover Overlay — analysis_arena_day_review — D=2026-01-02

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `4957c9e060a96b66`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 368, 559, 388, 011, 001, 006, 003, 008 | 23, 5, 32, 4, 2, 15, 33, 18 | - | - | shared_host | Midday:OFF/1, Combined:OFF/0, Evening:OFF/0 |
| 2 | Delaware4 | 244, 449, 499, 144, 114, 004, 014, 599 | 31, 35, 15, 22, 25, 28, 19, 5 | - | - | shared_host | Midday:WATCH/2, Evening:OFF/1, Combined:OFF/0 |
| 3 | Florida4 | 559, 466, 366, 599, 677 | 18, 19, 23, 5, 9, 15, 32, 17 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 4 | Indiana4 | 244, 668, 367, 677, 368, 144, 146 | 18, 21, 23, 31, 20, 19, 6, 25 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/1 |
| 5 | Michigan4 | 006, 069, 599, 133, 199, 166, 168 | 2, 23, 9, 18, 25, 6, 15, 16 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 6 | NewJersey4 | 299, 599, 899, 229, 778, 128 | 31, 15, 34, 27, 28, 33, 8, 1 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 7 | NewYork4 | 688, 788, 778, 677, 066, 559, 248, 889 | 30, 23, 18, 28, 6, 33, 29, 27 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 8 | NorthCarolina4 | 224, 223, 229, 003, 033, 299, 004 | 28, 13, 4, 27, 1, 5, 11, 31 | - | - | shared_host | Evening:ALERT/4, Combined:WATCH/2, Midday:WATCH/2 |
| 9 | Ohio4 | 055, 559, 255, 224, 057, 025, 068, 009 | 3, 1, 5, 28, 2, 10, 8, 12 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 10 | OntarioCanada4 | 118, 255, 188, 022, 559, 224, 225 | 10, 23, 18, 3, 21, 2, 5, 8 | - | - | shared_host | Combined:OFF/1, Evening:OFF/1, Midday:OFF/0 |
| 11 | Pennsylvania4 | 559, 579, 599, 359, 059, 339, 007 | 5, 12, 15, 3, 33, 23, 14, 13 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 12 | PuertoRico4 | 344, 113, 224, 002, 001, 226, 134, 244 | 24, 34, 18, 31, 28, 10, 12, 3 | - | - | shared_host | Evening:OFF/1, Combined:OFF/0, Midday:OFF/0 |
| 13 | SouthCarolina4 | 118, 008, 009, 138, 255, 559, 011, 368 | 5, 18, 23, 4, 2, 3, 6, 15 | - | - | shared_host | Midday:OFF/1, Evening:OFF/1, Combined:OFF/0 |
| 14 | Virginia4 | 224, 177, 133, 229, 477, 334, 113, 577 | 28, 20, 23, 18, 31, 10, 17, 26 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 268 | 35 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 228 | 30 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 270 | 33 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 221 | 27 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 255 | 35 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 172 | 24 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 250 | 30 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 267 | 33 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 214 | 27 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 241 | 30 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Connecticut4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 001, 006, 009, 138, 368, 559 | 6 | 11 | False | True |
| Connecticut4 | NewYork4 | shared_box_family | lane/family | primary | - | 006, 009, 478, 559, 688 | 5 | 10 | False | True |
| NewJersey4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 004, 005, 229, 299 | 5 | 10 | False | True |
| NewYork4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 006, 007, 009, 559 | 5 | 10 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 007, 009, 255, 559 | 5 | 10 | False | True |
| Connecticut4 | SouthCarolina4 | shared_lane | lane/family | primary | 18, 2, 23, 33, 4, 5 | - | 6 | 10 | False | True |
| Pennsylvania4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 5 | 045, 059, 559 | 3 | 9 | False | True |
| Connecticut4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 009, 455, 559 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 011, 017, 144, 244 | 4 | 9 | False | True |
| Delaware4 | NewJersey4 | shared_box_family | lane/family | primary | - | 004, 011, 249, 299 | 4 | 9 | False | True |
| Delaware4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 011, 014, 017, 044 | 4 | 9 | False | True |
| Florida4 | Indiana4 | shared_box_family | lane/family | primary | - | 066, 366, 668, 677 | 4 | 9 | False | True |
| NewYork4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 006, 007, 009, 559 | 4 | 9 | False | True |
| NorthCarolina4 | Ohio4 | shared_box_family | lane/family | primary | - | 005, 007, 009, 224 | 4 | 9 | False | True |
| Ohio4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 007, 009, 057, 559 | 4 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 118, 188, 255, 559 | 4 | 9 | False | True |
| OntarioCanada4 | Virginia4 | shared_box_family | lane/family | primary | - | 114, 119, 224, 577 | 4 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 007, 009, 059, 559 | 4 | 9 | False | True |
| NewYork4 | OntarioCanada4 | shared_lane | lane/family | primary | 17, 18, 23, 28, 5 | - | 5 | 9 | False | True |
| NorthCarolina4 | Ohio4 | shared_lane | lane/family | primary | 1, 15, 23, 28, 5 | - | 5 | 9 | False | True |
| Ohio4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 15, 23, 3, 5 | - | 5 | 9 | False | True |
| Ohio4 | PuertoRico4 | shared_lane | lane/family | primary | 15, 2, 23, 28, 3 | - | 5 | 9 | False | True |
| OntarioCanada4 | SouthCarolina4 | shared_lane | lane/family | primary | 18, 21, 23, 3, 5 | - | 5 | 9 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_lane | lane/family | primary | 18, 23, 3, 33, 5 | - | 5 | 9 | False | True |
| PuertoRico4 | Virginia4 | shared_lane | lane/family | primary | 18, 20, 23, 28, 31 | - | 5 | 9 | False | True |
| Connecticut4 | Indiana4 | alert_implied_echo | lane/family | primary | 2, 23 | 006, 368 | 2 | 8 | False | True |
| Connecticut4 | SouthCarolina4 | alert_implied_echo | lane/family | primary | 2, 23 | 006, 368 | 2 | 8 | False | True |
| NorthCarolina4 | PuertoRico4 | alert_implied_echo | lane/family | primary | 2, 15 | 001, 044 | 2 | 8 | False | True |
| Pennsylvania4 | Connecticut4 | alert_implied_echo | lane/family | primary | 5 | 455, 559 | 2 | 8 | False | True |
| SouthCarolina4 | NorthCarolina4 | alert_implied_echo | lane/family | primary | 4 | 003, 035 | 2 | 8 | False | True |
| Connecticut4 | Indiana4 | shared_box_family | lane/family | primary | - | 006, 011, 368 | 3 | 8 | False | True |
| Connecticut4 | Michigan4 | shared_box_family | lane/family | primary | - | 001, 006, 133 | 3 | 8 | False | True |
| Connecticut4 | NewJersey4 | shared_box_family | lane/family | primary | - | 001, 004, 011 | 3 | 8 | False | True |
| Connecticut4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 001, 004, 009 | 3 | 8 | False | True |
| Connecticut4 | Ohio4 | shared_box_family | lane/family | primary | - | 006, 009, 559 | 3 | 8 | False | True |
| Delaware4 | NorthCarolina4 | shared_box_family | lane/family | primary | - | 004, 044, 299 | 3 | 8 | False | True |
| Delaware4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 014, 017, 114 | 3 | 8 | False | True |
| Florida4 | NewYork4 | shared_box_family | lane/family | primary | - | 066, 559, 677 | 3 | 8 | False | True |
| Florida4 | Virginia4 | shared_box_family | lane/family | primary | - | 113, 114, 117 | 3 | 8 | False | True |
| Indiana4 | NewYork4 | shared_box_family | lane/family | primary | - | 006, 066, 677 | 3 | 8 | False | True |

## Strongest Overlap Pairs

- `Connecticut4 ↔ SouthCarolina4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ SouthCarolina4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ PuertoRico4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `NorthCarolina4 ↔ SouthCarolina4` score=`30` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Michigan4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ NorthCarolina4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Pennsylvania4` score=`29` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ PuertoRico4` score=`28` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ Indiana4` score=`27` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ NewYork4` score=`27` types=`alert_implied_echo, shared_box_family, shared_lane`
