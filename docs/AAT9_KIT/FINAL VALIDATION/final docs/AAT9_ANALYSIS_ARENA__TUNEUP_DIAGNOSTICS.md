# Analysis Arena Tune-Up Diagnostics

## 1. Scope

- Windows reviewed: `5`
- Ranking CSV: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__BRAIN2_RANKING_DIAGNOSTIC.csv`
- Tracker-lift CSV: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__TRACKER_LIFT_ROLLUP.csv`
- Doubles subtype CSV: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__DOUBLES_SUBTYPE_ROLLUP.csv`

## 2. Brain 2 Ranking Diagnostic

- Repeated false-positive top states:
  - `Connecticut4` top_primary_days=`38` high_conviction_hits=`17` credited_hits=`50` median_hit_rank=`1.0`
- Productive non-primary states:
  - `Indiana4` credited_hits=`55` top_primary_days=`0` strict_box=`8` straight=`11` median_hit_rank=`4.0`
  - `Pennsylvania4` credited_hits=`55` top_primary_days=`0` strict_box=`1` straight=`5` median_hit_rank=`11.0`
  - `NewJersey4` credited_hits=`54` top_primary_days=`0` strict_box=`6` straight=`11` median_hit_rank=`6.0`
  - `NorthCarolina4` credited_hits=`52` top_primary_days=`0` strict_box=`8` straight=`14` median_hit_rank=`8.0`
  - `Ohio4` credited_hits=`52` top_primary_days=`0` strict_box=`2` straight=`5` median_hit_rank=`9.0`
  - `OntarioCanada4` credited_hits=`52` top_primary_days=`0` strict_box=`7` straight=`11` median_hit_rank=`10.0`
  - `Virginia4` credited_hits=`50` top_primary_days=`0` strict_box=`6` straight=`8` median_hit_rank=`14.0`
  - `SouthCarolina4` credited_hits=`49` top_primary_days=`0` strict_box=`6` straight=`10` median_hit_rank=`13.0`

## 3. Tracker-Family Lift

- Event-layer signals with strongest gap-box lift:
  - `event::arena_primary_box` overall=`5.8%` gap_box=`73.9%` lift=`12.66x`
  - `event::arena_box_signal` overall=`8.3%` gap_box=`100.0%` lift=`12.01x`
  - `event::sandbox_box_seed` overall=`6.5%` gap_box=`65.2%` lift=`10.02x`
  - `event::preserved_not_budgeted` overall=`0.7%` gap_box=`4.3%` lift=`6.49x`
  - `event::arena_primary_vt` overall=`26.7%` gap_box=`69.6%` lift=`2.61x`
  - `event::sandbox_vt_seed` overall=`38.4%` gap_box=`78.3%` lift=`2.04x`
- Hit-layer signals with strongest strict-box lift:
  - `hit::profit_alert_direct_match` overall=`1.0%` strict_box=`9.5%` lift=`9.35x`
  - `hit::arena_exact_signal` overall=`2.5%` strict_box=`21.6%` lift=`8.80x`
  - `hit::profit_alert_implied_match` overall=`1.2%` strict_box=`9.5%` lift=`8.18x`
  - `hit::sandbox_box_seed` overall=`9.4%` strict_box=`51.4%` lift=`5.47x`
  - `hit::arena_box_signal` overall=`12.1%` strict_box=`55.4%` lift=`4.56x`
  - `hit::sandbox_vt_seed` overall=`49.6%` strict_box=`62.2%` lift=`1.25x`

## 4. Doubles Subtype Split

- `all_hits` inventory types: `none` x267, `double` x225, `mirror_double` x200
- `all_hits` double strength: `NONE` x267, `MEDIUM` x252, `STRONG` x145, `WEAK` x28
- `strict_box_hits` inventory types: `double` x34, `mirror_double` x32, `none` x8
- `strict_box_hits` double strength: `MEDIUM` x46, `STRONG` x16, `NONE` x8, `WEAK` x4
- `box_gap_rows` inventory types: `double` x22, `none` x19, `mirror_double` x5
- `box_gap_rows` double strength: `NONE` x20, `STRONG` x14, `MEDIUM` x11, `WEAK` x1

## 5. Practical Read

- Use the ranking diagnostic to find states the board over-promotes versus states that keep converting without being primary.
- Use the tracker-lift tables to separate sharp signals from ambient support before changing Brain 2 weights.
- Use the doubles subtype table to learn which double forms matter most before turning 'doubles matter' into a blunt scoring rule.
