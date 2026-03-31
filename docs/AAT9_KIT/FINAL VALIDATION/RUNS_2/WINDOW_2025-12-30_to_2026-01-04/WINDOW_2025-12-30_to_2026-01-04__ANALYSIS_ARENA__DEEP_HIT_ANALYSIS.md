# Analysis Arena Deep Hit Analysis

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04`
- Dates: `2025-12-30` to `2026-01-04`
- Total graded events: `163`
- Credited hit roster CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__HIT_ROSTER.csv`
- Hit universe: any event with `play_inclusive_hit == True`.
- Credited hit classes tracked explicitly: `STRAIGHT`, `STRICT_BOXED`, `CANONICAL_BOX`, `VTRAC_ONLY`.
- Rolled credit signatures keep the VTRAC overlap explicit, e.g. `STRAIGHT+VTRAC`, `CANONICAL_BOX+VTRAC`.

## 2. Hit Inventory

- Credited hits: `103` (63.2%)
- Straight hits: `20` (12.3%)
- Strict boxed hits: `10` (6.1%)
- Canonical / any-box hits: `46` (28.2%)
- VTRAC hits: `103` (63.2%)
- VTRAC-only hits: `57` (35.0%)
- Primary hit classes: `CANONICAL_BOX` x26, `STRAIGHT` x20, `VTRAC_ONLY` x57
- Credit signatures: `CANONICAL_BOX+VTRAC` x26, `STRAIGHT+VTRAC` x20, `VTRAC_ONLY` x57

## 3. Ranking / State Targeting

- Rank tiers across credited hits: `LOW_BOARD` x40, `MID_BOARD` x26, `TOP3` x25, `TOP5` x12
- Median board rank, all hits: `7.0`
- Median board rank, high-conviction hits: `7.0`
- Median board rank, VTRAC-only hits: `7.0`
- Top-primary-target hits: `9`
- Secondary-target hits: `7`
- Best-clean-host hits: `9`
- Highest-context-support hits: `9`

## 4. Budget Floor

- Minimum budget for inclusive hits: `B12` x29, `B36` x59, `B24` x15
- Minimum budget for box-any hits: `B12` x9, `B36` x26, `B24` x11
- Minimum budget for straight hits: `B24` x7, `B36` x10, `B12` x3

## 5. Hit Morphology

- Inventory types: `mirror_double` x27, `_none_` x45, `double` x31
- Double-context strength: `MEDIUM` x43, `WEAK` x3, `STRONG` x12
- Blackapple status across hits: `WATCH` x41, `ALERT` x12, `OFF` x50
- Top compound-event tags across hits: `CLAMP_4` x19, `CARRY_PERM` x14, `STRAIGHT_GATE` x4, `ENGINE_GOV` x2, `CARRY_PERM_HARDLOCK` x1, `DBL_BA` x1, `IDX_ECHO_BASE` x1, `IDX_ECHO_CLAMP` x1

## 6. Signal Lift

- `arena box signal`: 11/103 (10.7%) vs 11/163 (6.7%); lift 1.58x
- `arena exact signal`: 1/103 (1.0%) vs 1/163 (0.6%); lift 1.58x
- `candidate box hit`: 37/103 (35.9%) vs 37/163 (22.7%); lift 1.58x
- `candidate straight hit`: 25/103 (24.3%) vs 25/163 (15.3%); lift 1.58x
- `candidate vtrac hit`: 103/103 (100.0%) vs 108/163 (66.3%); lift 1.51x
- `profit alert direct match`: 1/103 (1.0%) vs 1/163 (0.6%); lift 1.58x
- `profit alert implied match`: 1/103 (1.0%) vs 1/163 (0.6%); lift 1.58x
- `compound event present`: 43/103 (41.7%) vs 78/163 (47.9%); lift 0.87x
- `sandbox box seed`: 7/103 (6.8%) vs 7/163 (4.3%); lift 1.58x
- `sandbox exact seed`: 1/103 (1.0%) vs 1/163 (0.6%); lift 1.58x
- `sandbox vt seed`: 50/103 (48.5%) vs 61/163 (37.4%); lift 1.30x
- `preserved not budgeted`: 3/103 (2.9%) vs 3/163 (1.8%); lift 1.58x

## 7. Arena Final-Candidate Signatures

- Signature buckets: `PARTIAL_ARENA_FINALIST` x32, `LIGHT_ARENA_FINALIST` x49, `CONTROL_ARM_ONLY_CATCH` x22
- Top signature hits: `2025-12-30 Indiana4 Evening 512`[CANONICAL_BOX, PARTIAL_ARENA_FINALIST, rank 4], `2026-01-03 SouthCarolina4 Evening 051`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 13], `2026-01-01 NorthCarolina4 Evening 053`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 8], `2026-01-03 SouthCarolina4 Midday 189`[VTRAC_ONLY, PARTIAL_ARENA_FINALIST, rank 13], `2025-12-30 Connecticut4 Midday 095`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 1], `2025-12-30 Florida4 Evening 870`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 3], `2026-01-03 Florida4 Midday 708`[CANONICAL_BOX, PARTIAL_ARENA_FINALIST, rank 3], `2025-12-31 NewJersey4 Midday 366`[VTRAC_ONLY, PARTIAL_ARENA_FINALIST, rank 6]
- Low-rank but converted hits: `2025-12-31 Virginia4 Midday 686`[CANONICAL_BOX, rank 14], `2026-01-04 Virginia4 Midday 200`[STRAIGHT, rank 14], `2025-12-31 Virginia4 Evening 636`[CANONICAL_BOX, rank 14], `2026-01-04 Virginia4 Evening 217`[CANONICAL_BOX, rank 14], `2026-01-03 SouthCarolina4 Evening 051`[STRAIGHT, rank 13], `2025-12-31 SouthCarolina4 Midday 653`[CANONICAL_BOX, rank 13], `2026-01-02 PuertoRico4 Midday 144`[STRAIGHT, rank 12], `2025-12-30 Pennsylvania4 Evening 173`[CANONICAL_BOX, rank 11]
- VTRAC-only examples: `2026-01-03 SouthCarolina4 Midday 189`[rank 13, min B36], `2025-12-31 NewJersey4 Midday 366`[rank 6, min B12], `2025-12-31 NorthCarolina4 Evening 057`[rank 8, min B12], `2025-12-30 Indiana4 Midday 585`[rank 4, min B24], `2025-12-31 Connecticut4 Evening 361`[rank 1, min B36], `2026-01-02 Connecticut4 Midday 970`[rank 1, min B36], `2026-01-03 Connecticut4 Evening 181`[rank 1, min B36], `2026-01-04 Florida4 Midday 171`[rank 3, min B36]
- Double / mirror examples: `2026-01-03 SouthCarolina4 Evening 051`[mirror_double, due rank 9, MEDIUM], `2026-01-01 NorthCarolina4 Evening 053`[mirror_double, due rank 5, STRONG], `2025-12-30 Connecticut4 Midday 095`[mirror_double, due rank 10, MEDIUM], `2025-12-31 NewJersey4 Midday 366`[double, due rank 3, STRONG], `2026-01-01 NewJersey4 Midday 770`[double, due rank 13, MEDIUM], `2025-12-31 NorthCarolina4 Evening 057`[mirror_double, due rank 10, STRONG], `2025-12-30 Indiana4 Midday 585`[double, due rank 12, MEDIUM], `2026-01-02 Ohio4 Midday 747`[double, due rank 8, MEDIUM]

## 8. Design Read

- Use this report to separate high-conviction catches from lane-only catches; inclusive hit counts alone are not enough.
- Treat ambient supports cautiously. Profit-alert support, due-double support, positional support, and survivor support can be nearly universal and need lift-style interpretation.
- The main long-term value is linking converted hits back to rank, budget floor, and arena-final-candidate signature so later translator/budget work is grounded in real conversions.
