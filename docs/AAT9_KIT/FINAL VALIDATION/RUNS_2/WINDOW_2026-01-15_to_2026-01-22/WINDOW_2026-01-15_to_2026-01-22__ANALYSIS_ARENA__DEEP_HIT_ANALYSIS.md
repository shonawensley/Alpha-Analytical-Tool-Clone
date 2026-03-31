# Analysis Arena Deep Hit Analysis

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22`
- Dates: `2026-01-15` to `2026-01-22`
- Total graded events: `221`
- Credited hit roster CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/WINDOW_2026-01-15_to_2026-01-22__ANALYSIS_ARENA__HIT_ROSTER.csv`
- Hit universe: any event with `play_inclusive_hit == True`.
- Credited hit classes tracked explicitly: `STRAIGHT`, `STRICT_BOXED`, `CANONICAL_BOX`, `VTRAC_ONLY`.
- Rolled credit signatures keep the VTRAC overlap explicit, e.g. `STRAIGHT+VTRAC`, `CANONICAL_BOX+VTRAC`.

## 2. Hit Inventory

- Credited hits: `142` (64.3%)
- Straight hits: `30` (13.6%)
- Strict boxed hits: `12` (5.4%)
- Canonical / any-box hits: `69` (31.2%)
- VTRAC hits: `142` (64.3%)
- VTRAC-only hits: `73` (33.0%)
- Primary hit classes: `CANONICAL_BOX` x39, `STRAIGHT` x30, `VTRAC_ONLY` x73
- Credit signatures: `CANONICAL_BOX+VTRAC` x39, `STRAIGHT+VTRAC` x30, `VTRAC_ONLY` x73

## 3. Ranking / State Targeting

- Rank tiers across credited hits: `LOW_BOARD` x66, `MID_BOARD` x29, `TOP3` x25, `TOP5` x22
- Median board rank, all hits: `8.0`
- Median board rank, high-conviction hits: `7.0`
- Median board rank, VTRAC-only hits: `9.0`
- Top-primary-target hits: `12`
- Secondary-target hits: `10`
- Best-clean-host hits: `12`
- Highest-context-support hits: `12`

## 4. Budget Floor

- Minimum budget for inclusive hits: `B12` x40, `B36` x78, `B24` x24
- Minimum budget for box-any hits: `B36` x33, `B24` x21, `B12` x15
- Minimum budget for straight hits: `B36` x11, `B24` x13, `B12` x6

## 5. Hit Morphology

- Inventory types: `mirror_double` x44, `_none_` x62, `double` x36
- Double-context strength: `MEDIUM` x39, `STRONG` x33, `WEAK` x8
- Blackapple status across hits: `OFF` x35, `ALERT` x34, `WATCH` x73
- Top compound-event tags across hits: `CARRY_PERM` x25, `CLAMP_4` x19, `ENGINE_GOV` x13, `STRAIGHT_GATE` x6, `DBL_BA` x4, `IDX_ECHO_BASE` x1

## 6. Signal Lift

- `arena box signal`: 18/142 (12.7%) vs 19/221 (8.6%); lift 1.47x
- `arena exact signal`: 2/142 (1.4%) vs 2/221 (0.9%); lift 1.56x
- `candidate box hit`: 49/142 (34.5%) vs 51/221 (23.1%); lift 1.50x
- `candidate straight hit`: 34/142 (23.9%) vs 34/221 (15.4%); lift 1.56x
- `candidate vtrac hit`: 142/142 (100.0%) vs 147/221 (66.5%); lift 1.50x
- `profit alert direct match`: 2/142 (1.4%) vs 2/221 (0.9%); lift 1.56x
- `profit alert implied match`: 2/142 (1.4%) vs 2/221 (0.9%); lift 1.56x
- `compound event present`: 68/142 (47.9%) vs 104/221 (47.1%); lift 1.02x
- `sandbox box seed`: 14/142 (9.9%) vs 15/221 (6.8%); lift 1.45x
- `sandbox exact seed`: 2/142 (1.4%) vs 2/221 (0.9%); lift 1.56x
- `sandbox vt seed`: 68/142 (47.9%) vs 84/221 (38.0%); lift 1.26x
- `preserved not budgeted`: 1/142 (0.7%) vs 1/221 (0.5%); lift 1.56x

## 7. Arena Final-Candidate Signatures

- Signature buckets: `LIGHT_ARENA_FINALIST` x70, `PARTIAL_ARENA_FINALIST` x44, `CONTROL_ARM_ONLY_CATCH` x24, `CLEAR_ARENA_FINALIST` x4
- Top signature hits: `2026-01-16 Indiana4 Evening 836`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 4], `2026-01-18 Connecticut4 Midday 238`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 1], `2026-01-16 OntarioCanada4 Evening 390`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 10], `2026-01-19 Pennsylvania4 Evening 030`[CANONICAL_BOX, CLEAR_ARENA_FINALIST, rank 11], `2026-01-21 Florida4 Midday 350`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 3], `2026-01-17 Indiana4 Evening 065`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 4], `2026-01-19 Ohio4 Evening 061`[VTRAC_ONLY, PARTIAL_ARENA_FINALIST, rank 9], `2026-01-22 OntarioCanada4 Evening 544`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 10]
- Low-rank but converted hits: `2026-01-22 Virginia4 Evening 100`[CANONICAL_BOX, rank 14], `2026-01-15 Virginia4 Midday 493`[STRAIGHT, rank 14], `2026-01-16 Virginia4 Midday 854`[CANONICAL_BOX, rank 14], `2026-01-16 SouthCarolina4 Evening 145`[STRAIGHT, rank 13], `2026-01-17 SouthCarolina4 Midday 716`[CANONICAL_BOX, rank 13], `2026-01-20 SouthCarolina4 Midday 786`[CANONICAL_BOX, rank 13], `2026-01-20 SouthCarolina4 Evening 328`[CANONICAL_BOX, rank 13], `2026-01-15 PuertoRico4 Midday 357`[STRAIGHT, rank 12]
- VTRAC-only examples: `2026-01-19 Ohio4 Evening 061`[rank 9, min B12], `2026-01-15 NorthCarolina4 Midday 045`[rank 8, min B24], `2026-01-20 Ohio4 Evening 843`[rank 9, min B24], `2026-01-16 Indiana4 Midday 954`[rank 4, min B36], `2026-01-16 NewJersey4 Evening 180`[rank 6, min B36], `2026-01-21 OntarioCanada4 Midday 197`[rank 10, min B36], `2026-01-15 NewJersey4 Evening 466`[rank 6, min B24], `2026-01-17 NorthCarolina4 Evening 594`[rank 8, min B24]
- Double / mirror examples: `2026-01-16 Indiana4 Evening 836`[mirror_double, due rank 4, MEDIUM], `2026-01-18 Connecticut4 Midday 238`[mirror_double, due rank 3, MEDIUM], `2026-01-19 Pennsylvania4 Evening 030`[double, due rank 3, STRONG], `2026-01-21 Florida4 Midday 350`[mirror_double, due rank 7, MEDIUM], `2026-01-17 Indiana4 Evening 065`[mirror_double, due rank 4, STRONG], `2026-01-19 Ohio4 Evening 061`[mirror_double, due rank 9, STRONG], `2026-01-22 OntarioCanada4 Evening 544`[double, due rank 14, STRONG], `2026-01-15 NorthCarolina4 Midday 045`[mirror_double, due rank 9, STRONG]

## 8. Design Read

- Use this report to separate high-conviction catches from lane-only catches; inclusive hit counts alone are not enough.
- Treat ambient supports cautiously. Profit-alert support, due-double support, positional support, and survivor support can be nearly universal and need lift-style interpretation.
- The main long-term value is linking converted hits back to rank, budget floor, and arena-final-candidate signature so later translator/budget work is grounded in real conversions.
