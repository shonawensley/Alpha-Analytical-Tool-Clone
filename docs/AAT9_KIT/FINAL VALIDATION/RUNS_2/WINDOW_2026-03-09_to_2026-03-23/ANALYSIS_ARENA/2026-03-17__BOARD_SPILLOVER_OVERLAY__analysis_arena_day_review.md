# Board Spillover Overlay — analysis_arena_day_review — D=2026-03-17

Purpose: compare strong states at the board level, surface shared families/lanes, and classify simple spillover and spent-vs-unspent conditions.

## Summary

- schema_version: `board_spillover_overlay_v0`
- profile: `tool_only`
- experiment_tag: `arena_v0`
- midday_results_available: `False`
- inputs_hash: `71cec5a0ba99c679`

## State Summaries

| Rank | State | Top Canonicals | Top VTRAC | Midday Status | Evening Bias | Role Hint | BA Standing |
|---:|---|---|---|---|---|---|---|
| 1 | Connecticut4 | 344, 559, 139, 399, 144, 599, 039, 589 | 34, 24, 5, 18, 15, 25, 14, 23 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:WATCH/2 |
| 2 | Delaware4 | 599, 099, 019, 559, 399, 229, 334, 199 | 15, 5, 9, 34, 35, 33, 28, 31 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 3 | Florida4 | 668, 006, 255, 466, 669, 166, 266 | 18, 19, 25, 2, 3, 10, 23, 35 | - | - | shared_host | Midday:WATCH/2, Evening:WATCH/2, Combined:OFF/0 |
| 4 | Indiana4 | 599, 559, 224, 569, 248, 699, 499, 229 | 15, 28, 5, 30, 9, 31, 12, 6 | - | - | shared_host | Combined:WATCH/2, Evening:WATCH/2, Midday:OFF/1 |
| 5 | Michigan4 | 044, 667, 677, 055, 559, 267, 229, 158 | 20, 15, 5, 17, 1, 8, 3, 35 | - | - | shared_host | Combined:WATCH/2, Midday:OFF/1, Evening:OFF/0 |
| 6 | NewJersey4 | 038, 118, 499, 199, 169, 013, 001, 018 | 13, 25, 19, 35, 2, 18, 8, 6 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 7 | NewYork4 | 007, 668, 035, 244, 017, 003, 234 | 18, 7, 4, 3, 21, 12, 33, 31 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/0 |
| 8 | NorthCarolina4 | 138, 366, 036, 338, 368, 378, 112 | 23, 18, 29, 8, 20, 17, 32, 33 | - | - | shared_host | Combined:ALERT/3, Evening:ALERT/3, Midday:OFF/1 |
| 9 | Ohio4 | 069, 559, 224, 009, 244, 299, 599, 099 | 5, 15, 9, 31, 28, 34, 33, 35 | - | - | shared_host | Combined:WATCH/2, Midday:WATCH/2, Evening:OFF/1 |
| 10 | OntarioCanada4 | 223, 168, 138, 368, 148, 113, 378, 014 | 18, 23, 27, 24, 29, 35, 2, 4 | - | - | shared_host | Midday:WATCH/2, Combined:OFF/1, Evening:OFF/0 |
| 11 | Pennsylvania4 | 077, 559, 033, 007, 259, 133, 067, 006 | 10, 5, 30, 3, 23, 12, 4, 32 | - | - | shared_host | Combined:WATCH/2, Evening:OFF/1, Midday:OFF/0 |
| 12 | PuertoRico4 | 244, 677, 047, 024, 445, 144, 077, 449 | 31, 12, 15, 20, 10, 5, 3, 7 | - | - | shared_host | Combined:OFF/1, Midday:OFF/1, Evening:OFF/1 |
| 13 | SouthCarolina4 | 344, 455, 559, 036, 477, 022, 003, 447 | 5, 34, 4, 10, 31, 3, 8, 2 | - | - | shared_host | Evening:WATCH/2, Combined:OFF/1, Midday:OFF/1 |
| 14 | Virginia4 | 255, 559, 289, 599, 055, 689, 688 | 3, 5, 1, 23, 15, 10, 21, 30 | - | - | shared_host | Evening:ALERT/3, Combined:WATCH/2, Midday:WATCH/2 |

## Board Scoreboard

| Score Rank | State | Priority Score | Role | Spent | Evening Bias | Overlap Score | Primary Overlap Hits | Direct Cross Hits |
|---:|---|---:|---|---|---|---:|---:|---:|
| 1 | Connecticut4 | 128 | shared_host | unknown | - | 259 | 31 | 0 |
| 2 | Delaware4 | 118 | shared_host | unknown | - | 266 | 34 | 0 |
| 3 | Florida4 | 108 | shared_host | unknown | - | 242 | 28 | 0 |
| 4 | Indiana4 | 98 | shared_host | unknown | - | 250 | 30 | 0 |
| 5 | Michigan4 | 88 | shared_host | unknown | - | 313 | 38 | 0 |
| 6 | NewJersey4 | 78 | shared_host | unknown | - | 216 | 28 | 0 |
| 7 | NewYork4 | 68 | shared_host | unknown | - | 262 | 33 | 0 |
| 8 | NorthCarolina4 | 58 | shared_host | unknown | - | 155 | 18 | 0 |
| 9 | Ohio4 | 48 | shared_host | unknown | - | 290 | 33 | 0 |
| 10 | OntarioCanada4 | 38 | shared_host | unknown | - | 237 | 29 | 0 |

## Relationships

| State A | State B | Type | Directness | Tier | Shared VTRAC | Shared Families | Support | Pair Score | Midday Consumed | Still Live Evening |
|---|---|---|---|---|---|---|---:|---:|---|---|
| Delaware4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 009, 099, 455, 559, 599 | 6 | 11 | False | True |
| Florida4 | NewYork4 | shared_box_family | lane/family | primary | - | 004, 007, 136, 168, 366, 668 | 6 | 11 | False | True |
| NewYork4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 013, 017, 136, 168, 366, 668 | 6 | 11 | False | True |
| Delaware4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 009, 455, 559, 599 | 5 | 10 | False | True |
| Florida4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 113, 136, 168, 366, 668 | 5 | 10 | False | True |
| Michigan4 | Pennsylvania4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 067, 559 | 5 | 10 | False | True |
| Michigan4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 007, 044, 445, 677 | 5 | 10 | False | True |
| NewJersey4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 011, 013, 014, 017, 118 | 5 | 10 | False | True |
| Ohio4 | Virginia4 | shared_box_family | lane/family | primary | - | 006, 009, 455, 559, 599 | 5 | 10 | False | True |
| Pennsylvania4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 455, 559 | 5 | 10 | False | True |
| Indiana4 | Ohio4 | shared_lane | lane/family | primary | 15, 18, 23, 28, 5, 9 | - | 6 | 10 | False | True |
| Delaware4 | Indiana4 | alert_implied_echo | lane/family | primary | 15 | 445, 459, 599 | 3 | 9 | False | True |
| NewYork4 | Michigan4 | alert_implied_echo | lane/family | primary | 2, 3, 7 | 006, 007, 067 | 3 | 9 | False | True |
| OntarioCanada4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 10 | 027, 077, 225 | 3 | 9 | False | True |
| SouthCarolina4 | OntarioCanada4 | alert_implied_echo | composite | secondary | 10 | 022, 027, 077, 225, 257, 577 | 6 | 9 | False | True |
| SouthCarolina4 | Pennsylvania4 | alert_implied_echo | lane/family | primary | 10 | 027, 077, 225 | 3 | 9 | False | True |
| Virginia4 | Delaware4 | alert_implied_echo | lane/family | primary | 5 | 059, 455, 559 | 3 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_box_family | lane/family | primary | - | 001, 399, 559, 599 | 4 | 9 | False | True |
| Connecticut4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 004, 559, 599 | 4 | 9 | False | True |
| Delaware4 | Indiana4 | shared_box_family | lane/family | primary | - | 001, 229, 559, 599 | 4 | 9 | False | True |
| Delaware4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 005, 009, 455, 559 | 4 | 9 | False | True |
| Florida4 | Michigan4 | shared_box_family | lane/family | primary | - | 004, 005, 006, 007 | 4 | 9 | False | True |
| Indiana4 | Ohio4 | shared_box_family | lane/family | primary | - | 001, 224, 559, 599 | 4 | 9 | False | True |
| Michigan4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 005, 007, 559 | 4 | 9 | False | True |
| Michigan4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 006, 055, 559 | 4 | 9 | False | True |
| NewYork4 | PuertoRico4 | shared_box_family | lane/family | primary | - | 004, 007, 017, 244 | 4 | 9 | False | True |
| NorthCarolina4 | OntarioCanada4 | shared_box_family | lane/family | primary | - | 113, 138, 366, 368 | 4 | 9 | False | True |
| Ohio4 | SouthCarolina4 | shared_box_family | lane/family | primary | - | 004, 009, 455, 559 | 4 | 9 | False | True |
| SouthCarolina4 | Virginia4 | shared_box_family | lane/family | primary | - | 005, 009, 455, 559 | 4 | 9 | False | True |
| Connecticut4 | Delaware4 | shared_lane | lane/family | primary | 15, 18, 33, 34, 5 | - | 5 | 9 | False | True |
| Connecticut4 | Indiana4 | shared_lane | lane/family | primary | 15, 18, 23, 25, 5 | - | 5 | 9 | False | True |
| Connecticut4 | NewJersey4 | shared_lane | lane/family | primary | 15, 18, 23, 25, 34 | - | 5 | 9 | False | True |
| Connecticut4 | Virginia4 | shared_lane | lane/family | primary | 15, 23, 24, 33, 5 | - | 5 | 9 | False | True |
| Delaware4 | Indiana4 | shared_lane | lane/family | primary | 15, 18, 28, 5, 9 | - | 5 | 9 | False | True |
| Delaware4 | Ohio4 | shared_lane | lane/family | primary | 15, 18, 28, 5, 9 | - | 5 | 9 | False | True |
| Florida4 | NewJersey4 | shared_lane | lane/family | primary | 18, 19, 2, 23, 25 | - | 5 | 9 | False | True |
| Indiana4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 18, 23, 30, 5 | - | 5 | 9 | False | True |
| Indiana4 | Virginia4 | shared_lane | lane/family | primary | 12, 15, 23, 30, 5 | - | 5 | 9 | False | True |
| NewYork4 | Pennsylvania4 | shared_lane | lane/family | primary | 12, 18, 21, 23, 3 | - | 5 | 9 | False | True |
| Ohio4 | SouthCarolina4 | shared_lane | lane/family | primary | 15, 23, 28, 31, 5 | - | 5 | 9 | False | True |

## Strongest Overlap Pairs

- `Delaware4 ↔ Ohio4` score=`36` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Indiana4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Florida4 ↔ NewYork4` score=`34` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Delaware4 ↔ Virginia4` score=`33` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Connecticut4 ↔ Delaware4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ PuertoRico4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ Virginia4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Pennsylvania4 ↔ SouthCarolina4` score=`32` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Indiana4 ↔ Virginia4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
- `Michigan4 ↔ NewYork4` score=`31` types=`alert_implied_echo, shared_box_family, shared_lane`
