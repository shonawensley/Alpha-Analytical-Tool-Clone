# Analysis Arena Deep Hit Analysis

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09`
- Dates: `2026-01-05` to `2026-01-09`
- Total graded events: `138`
- Credited hit roster CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__HIT_ROSTER.csv`
- Hit universe: any event with `play_inclusive_hit == True`.
- Credited hit classes tracked explicitly: `STRAIGHT`, `STRICT_BOXED`, `CANONICAL_BOX`, `VTRAC_ONLY`.
- Rolled credit signatures keep the VTRAC overlap explicit, e.g. `STRAIGHT+VTRAC`, `CANONICAL_BOX+VTRAC`.

## 2. Hit Inventory

- Credited hits: `94` (68.1%)
- Straight hits: `18` (13.0%)
- Strict boxed hits: `12` (8.7%)
- Canonical / any-box hits: `36` (26.1%)
- VTRAC hits: `94` (68.1%)
- VTRAC-only hits: `58` (42.0%)
- Primary hit classes: `CANONICAL_BOX` x18, `STRAIGHT` x18, `VTRAC_ONLY` x58
- Credit signatures: `CANONICAL_BOX+VTRAC` x18, `STRAIGHT+VTRAC` x18, `VTRAC_ONLY` x58

## 3. Ranking / State Targeting

- Rank tiers across credited hits: `LOW_BOARD` x38, `MID_BOARD` x19, `TOP3` x22, `TOP5` x15
- Median board rank, all hits: `7.0`
- Median board rank, high-conviction hits: `8.5`
- Median board rank, VTRAC-only hits: `6.0`
- Top-primary-target hits: `6`
- Secondary-target hits: `6`
- Best-clean-host hits: `6`
- Highest-context-support hits: `8`

## 4. Budget Floor

- Minimum budget for inclusive hits: `B12` x24, `B36` x52, `B24` x18
- Minimum budget for box-any hits: `B12` x15, `B24` x10, `B36` x11
- Minimum budget for straight hits: `B12` x9, `B36` x4, `B24` x5

## 5. Hit Morphology

- Inventory types: `double` x31, `_none_` x37, `mirror_double` x26
- Double-context strength: `MEDIUM` x37, `STRONG` x18, `WEAK` x2
- Blackapple status across hits: `WATCH` x43, `OFF` x34, `ALERT` x17
- Top compound-event tags across hits: `CLAMP_4` x25, `CARRY_PERM` x13, `ENGINE_GOV` x6, `DBL_BA` x2, `STRAIGHT_GATE` x2

## 6. Signal Lift

- `arena box signal`: 9/94 (9.6%) vs 10/138 (7.2%); lift 1.32x
- `arena exact signal`: 3/94 (3.2%) vs 3/138 (2.2%); lift 1.47x
- `candidate box hit`: 34/94 (36.2%) vs 34/138 (24.6%); lift 1.47x
- `candidate straight hit`: 28/94 (29.8%) vs 28/138 (20.3%); lift 1.47x
- `candidate vtrac hit`: 94/94 (100.0%) vs 96/138 (69.6%); lift 1.44x
- `profit alert direct match`: 1/94 (1.1%) vs 1/138 (0.7%); lift 1.47x
- `profit alert implied match`: 2/94 (2.1%) vs 2/138 (1.4%); lift 1.47x
- `compound event present`: 48/94 (51.1%) vs 72/138 (52.2%); lift 0.98x
- `sandbox box seed`: 8/94 (8.5%) vs 9/138 (6.5%); lift 1.30x
- `sandbox exact seed`: 3/94 (3.2%) vs 3/138 (2.2%); lift 1.47x
- `sandbox vt seed`: 43/94 (45.7%) vs 48/138 (34.8%); lift 1.32x
- `preserved not budgeted`: 2/94 (2.1%) vs 2/138 (1.4%); lift 1.47x

## 7. Arena Final-Candidate Signatures

- Signature buckets: `PARTIAL_ARENA_FINALIST` x29, `LIGHT_ARENA_FINALIST` x44, `CONTROL_ARM_ONLY_CATCH` x18, `CLEAR_ARENA_FINALIST` x3
- Top signature hits: `2026-01-08 NewJersey4 Midday 089`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 6], `2026-01-09 Ohio4 Evening 090`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 9], `2026-01-09 Pennsylvania4 Midday 811`[CANONICAL_BOX, CLEAR_ARENA_FINALIST, rank 11], `2026-01-05 Florida4 Midday 080`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 3], `2026-01-06 Michigan4 Midday 618`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 5], `2026-01-05 NewYork4 Midday 080`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 7], `2026-01-08 Ohio4 Evening 580`[CANONICAL_BOX, PARTIAL_ARENA_FINALIST, rank 9], `2026-01-09 PuertoRico4 Evening 225`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 12]
- Low-rank but converted hits: `2026-01-06 Virginia4 Evening 958`[CANONICAL_BOX, rank 14], `2026-01-07 Virginia4 Evening 990`[STRAIGHT, rank 14], `2026-01-05 SouthCarolina4 Evening 712`[CANONICAL_BOX, rank 13], `2026-01-08 SouthCarolina4 Evening 910`[CANONICAL_BOX, rank 13], `2026-01-09 PuertoRico4 Evening 225`[STRAIGHT, rank 12], `2026-01-08 PuertoRico4 Midday 073`[STRAIGHT, rank 12], `2026-01-05 PuertoRico4 Midday 732`[STRAIGHT, rank 12], `2026-01-09 Pennsylvania4 Midday 811`[CANONICAL_BOX, rank 11]
- VTRAC-only examples: `2026-01-05 Virginia4 Evening 585`[rank 14, min B24], `2026-01-09 Delaware4 Midday 843`[rank 2, min B24], `2026-01-09 Delaware4 Evening 681`[rank 2, min B24], `2026-01-06 Florida4 Evening 160`[rank 3, min B24], `2026-01-09 Florida4 Midday 860`[rank 3, min B24], `2026-01-06 Florida4 Midday 209`[rank 3, min B36], `2026-01-08 Florida4 Midday 429`[rank 3, min B36], `2026-01-07 Michigan4 Midday 692`[rank 5, min B36]
- Double / mirror examples: `2026-01-09 Ohio4 Evening 090`[double, due rank 3, STRONG], `2026-01-09 Pennsylvania4 Midday 811`[double, due rank 11, MEDIUM], `2026-01-05 Florida4 Midday 080`[double, due rank 13, MEDIUM], `2026-01-06 Michigan4 Midday 618`[mirror_double, due rank 1, STRONG], `2026-01-05 NewYork4 Midday 080`[double, due rank 6, MEDIUM], `2026-01-08 Ohio4 Evening 580`[mirror_double, due rank 4, MEDIUM], `2026-01-09 PuertoRico4 Evening 225`[double, due rank 9, MEDIUM], `2026-01-05 Virginia4 Evening 585`[double, due rank 6, STRONG]

## 8. Design Read

- Use this report to separate high-conviction catches from lane-only catches; inclusive hit counts alone are not enough.
- Treat ambient supports cautiously. Profit-alert support, due-double support, positional support, and survivor support can be nearly universal and need lift-style interpretation.
- The main long-term value is linking converted hits back to rank, budget floor, and arena-final-candidate signature so later translator/budget work is grounded in real conversions.
