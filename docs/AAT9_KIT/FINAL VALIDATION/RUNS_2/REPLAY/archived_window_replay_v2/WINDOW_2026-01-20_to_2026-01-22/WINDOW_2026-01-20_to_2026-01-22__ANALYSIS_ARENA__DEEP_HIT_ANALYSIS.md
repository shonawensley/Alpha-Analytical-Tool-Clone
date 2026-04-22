# Analysis Arena Deep Hit Analysis

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22`
- Dates: `2026-01-20` to `2026-01-22`
- Total graded events: `84`
- Credited hit roster CSV: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__HIT_ROSTER.csv`
- Hit universe: any event with `play_inclusive_hit == True`.
- Credited hit classes tracked explicitly: `STRAIGHT`, `STRICT_BOXED`, `CANONICAL_BOX`, `VTRAC_ONLY`.
- Rolled credit signatures keep the VTRAC overlap explicit, e.g. `STRAIGHT+VTRAC`, `CANONICAL_BOX+VTRAC`.

## 2. Hit Inventory

- Credited hits: `63` (75.0%)
- Straight hits: `13` (15.5%)
- Strict boxed hits: `5` (6.0%)
- Canonical / any-box hits: `28` (33.3%)
- VTRAC hits: `63` (75.0%)
- VTRAC-only hits: `35` (41.7%)
- Primary hit classes: `CANONICAL_BOX` x15, `STRAIGHT` x13, `VTRAC_ONLY` x35
- Credit signatures: `CANONICAL_BOX+VTRAC` x15, `STRAIGHT+VTRAC` x13, `VTRAC_ONLY` x35

## 3. Ranking / State Targeting

- Rank tiers across credited hits: `LOW_BOARD` x31, `MID_BOARD` x11, `TOP3` x11, `TOP5` x10
- Median board rank, all hits: `8.0`
- Median board rank, high-conviction hits: `9.0`
- Median board rank, VTRAC-only hits: `8.0`
- Top-primary-target hits: `4`
- Secondary-target hits: `5`
- Best-clean-host hits: `4`
- Highest-context-support hits: `5`

## 4. Budget Floor

- Minimum budget for inclusive hits: `B24` x10, `B12` x18, `B36` x35
- Minimum budget for box-any hits: `B24` x9, `B36` x13, `B12` x6
- Minimum budget for straight hits: `B24` x5, `B36` x5, `B12` x3

## 5. Hit Morphology

- Inventory types: `_none_` x29, `double` x19, `mirror_double` x15
- Double-context strength: `STRONG` x14, `MEDIUM` x14, `WEAK` x6
- Blackapple status across hits: `ALERT` x20, `OFF` x18, `WATCH` x25
- Top compound-event tags across hits: `CLAMP_4` x8, `CARRY_PERM` x6, `STRAIGHT_GATE` x3, `DBL_BA` x2, `ENGINE_GOV` x2, `IDX_ECHO_BASE` x1

## 6. Signal Lift

- `arena box signal`: 4/63 (6.3%) vs 4/84 (4.8%); lift 1.33x
- `arena exact signal`: 1/63 (1.6%) vs 1/84 (1.2%); lift 1.33x
- `candidate box hit`: 20/63 (31.7%) vs 20/84 (23.8%); lift 1.33x
- `candidate straight hit`: 14/63 (22.2%) vs 14/84 (16.7%); lift 1.33x
- `candidate vtrac hit`: 63/63 (100.0%) vs 64/84 (76.2%); lift 1.31x
- `profit alert direct match`: 0/63 (0.0%) vs 0/84 (0.0%); lift n/a
- `profit alert implied match`: 0/63 (0.0%) vs 0/84 (0.0%); lift n/a
- `compound event present`: 22/63 (34.9%) vs 34/84 (40.5%); lift 0.86x
- `sandbox box seed`: 3/63 (4.8%) vs 3/84 (3.6%); lift 1.33x
- `sandbox exact seed`: 1/63 (1.6%) vs 1/84 (1.2%); lift 1.33x
- `sandbox vt seed`: 26/63 (41.3%) vs 30/84 (35.7%); lift 1.16x
- `preserved not budgeted`: 0/63 (0.0%) vs 0/84 (0.0%); lift n/a

## 7. Arena Final-Candidate Signatures

- Signature buckets: `LIGHT_ARENA_FINALIST` x33, `PARTIAL_ARENA_FINALIST` x17, `CONTROL_ARM_ONLY_CATCH` x13
- Top signature hits: `2026-01-21 NewYork4 Evening 233`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 7], `2026-01-22 OntarioCanada4 Evening 544`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 10], `2026-01-21 OntarioCanada4 Midday 197`[VTRAC_ONLY, PARTIAL_ARENA_FINALIST, rank 10], `2026-01-20 Ohio4 Evening 843`[VTRAC_ONLY, PARTIAL_ARENA_FINALIST, rank 9], `2026-01-22 Virginia4 Evening 100`[CANONICAL_BOX, PARTIAL_ARENA_FINALIST, rank 14], `2026-01-21 Florida4 Midday 350`[CANONICAL_BOX, PARTIAL_ARENA_FINALIST, rank 3], `2026-01-21 Pennsylvania4 Evening 816`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 11], `2026-01-20 Delaware4 Midday 099`[STRAIGHT, PARTIAL_ARENA_FINALIST, rank 2]
- Low-rank but converted hits: `2026-01-22 Virginia4 Evening 100`[CANONICAL_BOX, rank 14], `2026-01-20 Virginia4 Evening 367`[STRAIGHT, rank 14], `2026-01-20 Virginia4 Midday 260`[STRAIGHT, rank 14], `2026-01-21 SouthCarolina4 Evening 458`[STRAIGHT, rank 13], `2026-01-20 SouthCarolina4 Evening 328`[CANONICAL_BOX, rank 13], `2026-01-22 PuertoRico4 Midday 583`[CANONICAL_BOX, rank 12], `2026-01-21 PuertoRico4 Midday 328`[STRAIGHT, rank 12], `2026-01-21 PuertoRico4 Evening 257`[STRAIGHT, rank 12]
- VTRAC-only examples: `2026-01-21 OntarioCanada4 Midday 197`[rank 10, min B24], `2026-01-20 Ohio4 Evening 843`[rank 9, min B36], `2026-01-20 Indiana4 Evening 208`[rank 4, min B24], `2026-01-21 NewJersey4 Midday 185`[rank 6, min B36], `2026-01-20 SouthCarolina4 Midday 786`[rank 13, min B36], `2026-01-22 Virginia4 Midday 746`[rank 14, min B36], `2026-01-21 Ohio4 Midday 649`[rank 9, min B12], `2026-01-22 SouthCarolina4 Evening 187`[rank 13, min B12]
- Double / mirror examples: `2026-01-21 NewYork4 Evening 233`[double, due rank 12, MEDIUM], `2026-01-22 OntarioCanada4 Evening 544`[double, due rank 14, STRONG], `2026-01-20 Ohio4 Evening 843`[mirror_double, due rank 7, MEDIUM], `2026-01-22 Virginia4 Evening 100`[double, due rank 6, STRONG], `2026-01-21 Florida4 Midday 350`[mirror_double, due rank 7, MEDIUM], `2026-01-21 Pennsylvania4 Evening 816`[mirror_double, due rank 14, WEAK], `2026-01-20 Delaware4 Midday 099`[double, due rank 10, STRONG], `2026-01-22 Indiana4 Evening 757`[double, due rank 1, STRONG]

## 8. Design Read

- Use this report to separate high-conviction catches from lane-only catches; inclusive hit counts alone are not enough.
- Treat ambient supports cautiously. Profit-alert support, due-double support, positional support, and survivor support can be nearly universal and need lift-style interpretation.
- The main long-term value is linking converted hits back to rank, budget floor, and arena-final-candidate signature so later translator/budget work is grounded in real conversions.
