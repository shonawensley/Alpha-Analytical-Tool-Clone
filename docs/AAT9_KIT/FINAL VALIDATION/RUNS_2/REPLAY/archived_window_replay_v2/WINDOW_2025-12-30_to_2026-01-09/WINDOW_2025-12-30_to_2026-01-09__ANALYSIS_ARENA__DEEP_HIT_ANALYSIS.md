# Analysis Arena Deep Hit Analysis

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09`
- Dates: `2025-12-30` to `2026-01-09`
- Total graded events: `301`
- Credited hit roster CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__HIT_ROSTER.csv`
- Hit universe: any event with `play_inclusive_hit == True`.
- Credited hit classes tracked explicitly: `STRAIGHT`, `STRICT_BOXED`, `CANONICAL_BOX`, `VTRAC_ONLY`.
- Rolled credit signatures keep the VTRAC overlap explicit, e.g. `STRAIGHT+VTRAC`, `CANONICAL_BOX+VTRAC`.

## 2. Hit Inventory

- Credited hits: `200` (66.4%)
- Straight hits: `39` (13.0%)
- Strict boxed hits: `21` (7.0%)
- Canonical / any-box hits: `83` (27.6%)
- VTRAC hits: `200` (66.4%)
- VTRAC-only hits: `117` (38.9%)
- Primary hit classes: `CANONICAL_BOX` x44, `STRAIGHT` x39, `VTRAC_ONLY` x117
- Credit signatures: `CANONICAL_BOX+VTRAC` x44, `STRAIGHT+VTRAC` x39, `VTRAC_ONLY` x117

## 3. Ranking / State Targeting

- Rank tiers across credited hits: `LOW_BOARD` x81, `MID_BOARD` x44, `TOP3` x45, `TOP5` x30
- Median board rank, all hits: `7.0`
- Median board rank, high-conviction hits: `8.0`
- Median board rank, VTRAC-only hits: `7.0`
- Top-primary-target hits: `14`
- Secondary-target hits: `14`
- Best-clean-host hits: `14`
- Highest-context-support hits: `15`

## 4. Budget Floor

- Minimum budget for inclusive hits: `B12` x49, `B36` x109, `B24` x42
- Minimum budget for box-any hits: `B12` x24, `B24` x20, `B36` x39
- Minimum budget for straight hits: `B12` x15, `B36` x16, `B24` x8

## 5. Hit Morphology

- Inventory types: `mirror_double` x54, `_none_` x78, `double` x68
- Double-context strength: `MEDIUM` x81, `WEAK` x6, `STRONG` x35
- Blackapple status across hits: `WATCH` x88, `ALERT` x28, `OFF` x84
- Top compound-event tags across hits: `CLAMP_4` x48, `CARRY_PERM` x28, `ENGINE_GOV` x10, `STRAIGHT_GATE` x8, `DBL_BA` x2, `CARRY_PERM_HARDLOCK` x1, `IDX_ECHO_CLAMP` x1

## 6. Signal Lift

- `arena box signal`: 21/200 (10.5%) vs 22/301 (7.3%); lift 1.44x
- `arena exact signal`: 4/200 (2.0%) vs 4/301 (1.3%); lift 1.50x
- `candidate box hit`: 70/200 (35.0%) vs 73/301 (24.3%); lift 1.44x
- `candidate straight hit`: 57/200 (28.5%) vs 57/301 (18.9%); lift 1.50x
- `candidate vtrac hit`: 200/200 (100.0%) vs 218/301 (72.4%); lift 1.38x
- `profit alert direct match`: 2/200 (1.0%) vs 2/301 (0.7%); lift 1.50x
- `profit alert implied match`: 3/200 (1.5%) vs 3/301 (1.0%); lift 1.51x
- `compound event present`: 98/200 (49.0%) vs 150/301 (49.8%); lift 0.98x
- `sandbox box seed`: 18/200 (9.0%) vs 19/301 (6.3%); lift 1.43x
- `sandbox exact seed`: 4/200 (2.0%) vs 4/301 (1.3%); lift 1.50x
- `sandbox vt seed`: 93/200 (46.5%) vs 109/301 (36.2%); lift 1.28x
- `preserved not budgeted`: 3/200 (1.5%) vs 3/301 (1.0%); lift 1.51x

## 7. Arena Final-Candidate Signatures

- Signature buckets: `PARTIAL_ARENA_FINALIST` x63, `LIGHT_ARENA_FINALIST` x94, `CONTROL_ARM_ONLY_CATCH` x40, `CLEAR_ARENA_FINALIST` x3
- Top signature hits: `2026-01-08 NewJersey4 Midday 089`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 6], `2026-01-09 Ohio4 Evening 090`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 9], `2026-01-09 Pennsylvania4 Midday 811`[CANONICAL_BOX, CLEAR_ARENA_FINALIST, rank 11], `2025-12-30 Connecticut4 Midday 095`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 1], `2026-01-05 Florida4 Midday 080`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 3], `2025-12-30 Indiana4 Evening 512`[CANONICAL_BOX, PARTIAL_ARENA_FINALIST, rank 4], `2026-01-06 Michigan4 Midday 618`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 5], `2026-01-05 NewYork4 Midday 080`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 7]
- Low-rank but converted hits: `2025-12-31 Virginia4 Midday 686`[CANONICAL_BOX, rank 14], `2026-01-04 Virginia4 Midday 200`[CANONICAL_BOX, rank 14], `2026-01-06 Virginia4 Evening 958`[CANONICAL_BOX, rank 14], `2025-12-31 Virginia4 Evening 636`[CANONICAL_BOX, rank 14], `2026-01-04 Virginia4 Evening 217`[CANONICAL_BOX, rank 14], `2026-01-07 Virginia4 Evening 990`[STRAIGHT, rank 14], `2026-01-03 SouthCarolina4 Evening 051`[STRAIGHT, rank 13], `2025-12-31 SouthCarolina4 Midday 653`[CANONICAL_BOX, rank 13]
- VTRAC-only examples: `2026-01-05 Virginia4 Evening 585`[rank 14, min B24], `2026-01-03 SouthCarolina4 Midday 189`[rank 13, min B36], `2026-01-09 Delaware4 Midday 843`[rank 2, min B24], `2026-01-09 Delaware4 Evening 681`[rank 2, min B24], `2026-01-06 Florida4 Evening 160`[rank 3, min B24], `2026-01-09 Florida4 Midday 860`[rank 3, min B24], `2025-12-30 Indiana4 Midday 585`[rank 4, min B24], `2026-01-02 Indiana4 Midday 974`[rank 4, min B24]
- Double / mirror examples: `2026-01-09 Ohio4 Evening 090`[double, due rank 3, STRONG], `2026-01-09 Pennsylvania4 Midday 811`[double, due rank 11, MEDIUM], `2025-12-30 Connecticut4 Midday 095`[mirror_double, due rank 10, MEDIUM], `2026-01-05 Florida4 Midday 080`[double, due rank 13, MEDIUM], `2026-01-06 Michigan4 Midday 618`[mirror_double, due rank 1, STRONG], `2026-01-05 NewYork4 Midday 080`[double, due rank 6, MEDIUM], `2026-01-01 NorthCarolina4 Evening 053`[mirror_double, due rank 5, STRONG], `2026-01-08 Ohio4 Evening 580`[mirror_double, due rank 4, MEDIUM]

## 8. Design Read

- Use this report to separate high-conviction catches from lane-only catches; inclusive hit counts alone are not enough.
- Treat ambient supports cautiously. Profit-alert support, due-double support, positional support, and survivor support can be nearly universal and need lift-style interpretation.
- The main long-term value is linking converted hits back to rank, budget floor, and arena-final-candidate signature so later translator/budget work is grounded in real conversions.
