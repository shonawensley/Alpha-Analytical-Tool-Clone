# Analysis Arena Deep Hit Analysis

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- Dates: `2026-03-09` to `2026-03-23`
- Total graded events: `414`
- Credited hit roster CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__HIT_ROSTER.csv`
- Hit universe: any event with `play_inclusive_hit == True`.
- Credited hit classes tracked explicitly: `STRAIGHT`, `STRICT_BOXED`, `CANONICAL_BOX`, `VTRAC_ONLY`.
- Rolled credit signatures keep the VTRAC overlap explicit, e.g. `STRAIGHT+VTRAC`, `CANONICAL_BOX+VTRAC`.

## 2. Hit Inventory

- Credited hits: `274` (66.2%)
- Straight hits: `54` (13.0%)
- Strict boxed hits: `29` (7.0%)
- Canonical / any-box hits: `127` (30.7%)
- VTRAC hits: `274` (66.2%)
- VTRAC-only hits: `147` (35.5%)
- Primary hit classes: `CANONICAL_BOX` x73, `STRAIGHT` x54, `VTRAC_ONLY` x147
- Credit signatures: `CANONICAL_BOX+VTRAC` x73, `STRAIGHT+VTRAC` x54, `VTRAC_ONLY` x147

## 3. Ranking / State Targeting

- Rank tiers across credited hits: `LOW_BOARD` x125, `MID_BOARD` x58, `TOP3` x53, `TOP5` x38
- Median board rank, all hits: `8.0`
- Median board rank, high-conviction hits: `7.0`
- Median board rank, VTRAC-only hits: `9.0`
- Top-primary-target hits: `16`
- Secondary-target hits: `18`
- Best-clean-host hits: `16`
- Highest-context-support hits: `18`

## 4. Budget Floor

- Minimum budget for inclusive hits: `B36` x147, `B12` x77, `B24` x50
- Minimum budget for box-any hits: `B36` x65, `B24` x34, `B12` x28
- Minimum budget for straight hits: `B36` x20, `B24` x18, `B12` x16

## 5. Hit Morphology

- Inventory types: `_none_` x95, `double` x105, `mirror_double` x74
- Double-context strength: `STRONG` x61, `MEDIUM` x106, `WEAK` x12
- Blackapple status across hits: `ALERT` x57, `OFF` x77, `WATCH` x140
- Top compound-event tags across hits: `CLAMP_4` x58, `CARRY_PERM` x40, `ENGINE_GOV` x21, `STRAIGHT_GATE` x20, `IDX_ECHO_BASE` x7, `DBL_BA` x2

## 6. Signal Lift

- `arena box signal`: 34/274 (12.4%) vs 35/414 (8.5%); lift 1.47x
- `arena exact signal`: 8/274 (2.9%) vs 9/414 (2.2%); lift 1.34x
- `candidate box hit`: 95/274 (34.7%) vs 97/414 (23.4%); lift 1.48x
- `candidate straight hit`: 78/274 (28.5%) vs 80/414 (19.3%); lift 1.47x
- `candidate vtrac hit`: 274/274 (100.0%) vs 300/414 (72.5%); lift 1.38x
- `profit alert direct match`: 1/274 (0.4%) vs 1/414 (0.2%); lift 1.51x
- `profit alert implied match`: 1/274 (0.4%) vs 1/414 (0.2%); lift 1.51x
- `compound event present`: 148/274 (54.0%) vs 212/414 (51.2%); lift 1.05x
- `sandbox box seed`: 26/274 (9.5%) vs 27/414 (6.5%); lift 1.45x
- `sandbox exact seed`: 8/274 (2.9%) vs 9/414 (2.2%); lift 1.34x
- `sandbox vt seed`: 141/274 (51.5%) vs 162/414 (39.1%); lift 1.32x
- `preserved not budgeted`: 1/274 (0.4%) vs 1/414 (0.2%); lift 1.51x

## 7. Arena Final-Candidate Signatures

- Signature buckets: `PARTIAL_ARENA_FINALIST` x115, `CONTROL_ARM_ONLY_CATCH` x45, `LIGHT_ARENA_FINALIST` x111, `CLEAR_ARENA_FINALIST` x3
- Top signature hits: `2026-03-10 SouthCarolina4 Evening 690`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 13], `2026-03-19 NorthCarolina4 Midday 611`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 8], `2026-03-12 Virginia4 Evening 400`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 14], `2026-03-21 NewJersey4 Evening 950`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 6], `2026-03-19 NewYork4 Midday 303`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 7], `2026-03-22 NewYork4 Evening 618`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 7], `2026-03-17 NorthCarolina4 Evening 383`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 8], `2026-03-23 NorthCarolina4 Midday 794`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 8]
- Low-rank but converted hits: `2026-03-12 Virginia4 Evening 400`[STRAIGHT, rank 14], `2026-03-10 Virginia4 Midday 316`[STRAIGHT, rank 14], `2026-03-09 Virginia4 Evening 188`[STRAIGHT, rank 14], `2026-03-16 Virginia4 Midday 440`[CANONICAL_BOX, rank 14], `2026-03-19 Virginia4 Evening 905`[STRAIGHT, rank 14], `2026-03-20 Virginia4 Midday 776`[CANONICAL_BOX, rank 14], `2026-03-22 Virginia4 Evening 742`[CANONICAL_BOX, rank 14], `2026-03-18 Virginia4 Midday 303`[CANONICAL_BOX, rank 14]
- VTRAC-only examples: `2026-03-09 NorthCarolina4 Midday 855`[rank 8, min B24], `2026-03-14 NewJersey4 Midday 274`[rank 6, min B36], `2026-03-19 NewJersey4 Evening 686`[rank 6, min B36], `2026-03-23 NewYork4 Evening 409`[rank 7, min B36], `2026-03-22 NorthCarolina4 Midday 532`[rank 8, min B36], `2026-03-12 OntarioCanada4 Evening 401`[rank 10, min B36], `2026-03-14 OntarioCanada4 Midday 290`[rank 10, min B36], `2026-03-23 Pennsylvania4 Midday 594`[rank 11, min B36]
- Double / mirror examples: `2026-03-19 NorthCarolina4 Midday 611`[double, due rank 12, MEDIUM], `2026-03-12 Virginia4 Evening 400`[double, due rank 14, MEDIUM], `2026-03-21 NewJersey4 Evening 950`[mirror_double, due rank 11, MEDIUM], `2026-03-19 NewYork4 Midday 303`[double, due rank 2, MEDIUM], `2026-03-22 NewYork4 Evening 618`[mirror_double, due rank 13, STRONG], `2026-03-17 NorthCarolina4 Evening 383`[double, due rank 14, MEDIUM], `2026-03-23 NorthCarolina4 Midday 794`[mirror_double, due rank 10, STRONG], `2026-03-09 OntarioCanada4 Evening 559`[double, due rank 12, MEDIUM]

## 8. Design Read

- Use this report to separate high-conviction catches from lane-only catches; inclusive hit counts alone are not enough.
- Treat ambient supports cautiously. Profit-alert support, due-double support, positional support, and survivor support can be nearly universal and need lift-style interpretation.
- The main long-term value is linking converted hits back to rank, budget floor, and arena-final-candidate signature so later translator/budget work is grounded in real conversions.
