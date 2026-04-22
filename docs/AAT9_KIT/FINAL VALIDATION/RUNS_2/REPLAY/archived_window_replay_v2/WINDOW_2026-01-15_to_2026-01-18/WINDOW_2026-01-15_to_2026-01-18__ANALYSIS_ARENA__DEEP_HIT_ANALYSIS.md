# Analysis Arena Deep Hit Analysis

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18`
- Dates: `2026-01-15` to `2026-01-18`
- Total graded events: `109`
- Credited hit roster CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__HIT_ROSTER.csv`
- Hit universe: any event with `play_inclusive_hit == True`.
- Credited hit classes tracked explicitly: `STRAIGHT`, `STRICT_BOXED`, `CANONICAL_BOX`, `VTRAC_ONLY`.
- Rolled credit signatures keep the VTRAC overlap explicit, e.g. `STRAIGHT+VTRAC`, `CANONICAL_BOX+VTRAC`.

## 2. Hit Inventory

- Credited hits: `79` (72.5%)
- Straight hits: `16` (14.7%)
- Strict boxed hits: `11` (10.1%)
- Canonical / any-box hits: `37` (33.9%)
- VTRAC hits: `79` (72.5%)
- VTRAC-only hits: `42` (38.5%)
- Primary hit classes: `CANONICAL_BOX` x21, `STRAIGHT` x16, `VTRAC_ONLY` x42
- Credit signatures: `CANONICAL_BOX+VTRAC` x21, `STRAIGHT+VTRAC` x16, `VTRAC_ONLY` x42

## 3. Ranking / State Targeting

- Rank tiers across credited hits: `LOW_BOARD` x32, `MID_BOARD` x20, `TOP3` x14, `TOP5` x13
- Median board rank, all hits: `7.0`
- Median board rank, high-conviction hits: `6.0`
- Median board rank, VTRAC-only hits: `8.5`
- Top-primary-target hits: `7`
- Secondary-target hits: `5`
- Best-clean-host hits: `7`
- Highest-context-support hits: `5`

## 4. Budget Floor

- Minimum budget for inclusive hits: `B24` x24, `B36` x42, `B12` x13
- Minimum budget for box-any hits: `B36` x18, `B24` x10, `B12` x9
- Minimum budget for straight hits: `B36` x5, `B24` x7, `B12` x4

## 5. Hit Morphology

- Inventory types: `mirror_double` x29, `double` x22, `_none_` x28
- Double-context strength: `MEDIUM` x27, `STRONG` x21, `WEAK` x3
- Blackapple status across hits: `OFF` x14, `WATCH` x50, `ALERT` x15
- Top compound-event tags across hits: `CARRY_PERM` x18, `ENGINE_GOV` x9, `CLAMP_4` x8, `DBL_BA` x2, `STRAIGHT_GATE` x2, `IDX_ECHO_BASE` x1

## 6. Signal Lift

- `arena box signal`: 12/79 (15.2%) vs 12/109 (11.0%); lift 1.38x
- `arena exact signal`: 3/79 (3.8%) vs 3/109 (2.8%); lift 1.38x
- `candidate box hit`: 33/79 (41.8%) vs 33/109 (30.3%); lift 1.38x
- `candidate straight hit`: 26/79 (32.9%) vs 26/109 (23.9%); lift 1.38x
- `candidate vtrac hit`: 79/79 (100.0%) vs 88/109 (80.7%); lift 1.24x
- `profit alert direct match`: 2/79 (2.5%) vs 2/109 (1.8%); lift 1.38x
- `profit alert implied match`: 2/79 (2.5%) vs 2/109 (1.8%); lift 1.38x
- `compound event present`: 40/79 (50.6%) vs 54/109 (49.5%); lift 1.02x
- `sandbox box seed`: 10/79 (12.7%) vs 10/109 (9.2%); lift 1.38x
- `sandbox exact seed`: 3/79 (3.8%) vs 3/109 (2.8%); lift 1.38x
- `sandbox vt seed`: 41/79 (51.9%) vs 46/109 (42.2%); lift 1.23x
- `preserved not budgeted`: 0/79 (0.0%) vs 0/109 (0.0%); lift n/a

## 7. Arena Final-Candidate Signatures

- Signature buckets: `LIGHT_ARENA_FINALIST` x34, `CONTROL_ARM_ONLY_CATCH` x14, `PARTIAL_ARENA_FINALIST` x28, `CLEAR_ARENA_FINALIST` x3
- Top signature hits: `2026-01-16 Indiana4 Evening 836`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 4], `2026-01-18 Connecticut4 Midday 238`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 1], `2026-01-16 OntarioCanada4 Evening 390`[STRAIGHT, CLEAR_ARENA_FINALIST, rank 10], `2026-01-16 NewJersey4 Evening 180`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 6], `2026-01-18 NorthCarolina4 Evening 772`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 8], `2026-01-17 Indiana4 Evening 065`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 4], `2026-01-16 Delaware4 Evening 107`[CANONICAL_BOX, PARTIAL_ARENA_FINALIST, rank 2], `2026-01-16 Indiana4 Midday 954`[VTRAC_ONLY, PARTIAL_ARENA_FINALIST, rank 4]
- Low-rank but converted hits: `2026-01-15 Virginia4 Midday 493`[STRAIGHT, rank 14], `2026-01-16 Virginia4 Midday 854`[CANONICAL_BOX, rank 14], `2026-01-16 SouthCarolina4 Evening 145`[STRAIGHT, rank 13], `2026-01-17 SouthCarolina4 Midday 716`[CANONICAL_BOX, rank 13], `2026-01-15 SouthCarolina4 Evening 118`[STRAIGHT, rank 13], `2026-01-16 Pennsylvania4 Evening 439`[CANONICAL_BOX, rank 11], `2026-01-18 Pennsylvania4 Evening 461`[CANONICAL_BOX, rank 11], `2026-01-16 OntarioCanada4 Evening 390`[STRAIGHT, rank 10]
- VTRAC-only examples: `2026-01-16 Indiana4 Midday 954`[rank 4, min B36], `2026-01-15 NewJersey4 Evening 466`[rank 6, min B24], `2026-01-17 NorthCarolina4 Evening 594`[rank 8, min B24], `2026-01-18 Connecticut4 Evening 781`[rank 1, min B36], `2026-01-15 Indiana4 Evening 094`[rank 4, min B36], `2026-01-18 Indiana4 Midday 864`[rank 4, min B36], `2026-01-15 NewJersey4 Midday 419`[rank 6, min B36], `2026-01-15 NewYork4 Evening 684`[rank 7, min B36]
- Double / mirror examples: `2026-01-16 Indiana4 Evening 836`[mirror_double, due rank 4, MEDIUM], `2026-01-18 Connecticut4 Midday 238`[mirror_double, due rank 3, MEDIUM], `2026-01-18 NorthCarolina4 Evening 772`[double, due rank 2, MEDIUM], `2026-01-17 Indiana4 Evening 065`[mirror_double, due rank 4, STRONG], `2026-01-16 Indiana4 Midday 954`[mirror_double, due rank 13, MEDIUM], `2026-01-15 NorthCarolina4 Midday 045`[mirror_double, due rank 9, STRONG], `2026-01-17 NewJersey4 Midday 873`[mirror_double, due rank 11, MEDIUM], `2026-01-15 NewJersey4 Evening 466`[double, due rank 4, STRONG]

## 8. Design Read

- Use this report to separate high-conviction catches from lane-only catches; inclusive hit counts alone are not enough.
- Treat ambient supports cautiously. Profit-alert support, due-double support, positional support, and survivor support can be nearly universal and need lift-style interpretation.
- The main long-term value is linking converted hits back to rank, budget floor, and arena-final-candidate signature so later translator/budget work is grounded in real conversions.
