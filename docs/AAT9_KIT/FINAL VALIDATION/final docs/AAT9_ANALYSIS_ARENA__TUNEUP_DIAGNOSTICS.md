# Analysis Arena Tune-Up Diagnostics

## 1. Scope

- Windows reviewed: `4`
- Ranking CSV: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__BRAIN2_RANKING_DIAGNOSTIC.csv`
- Tracker-lift CSV: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__TRACKER_LIFT_ROLLUP.csv`
- Doubles subtype CSV: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__DOUBLES_SUBTYPE_ROLLUP.csv`

## 2. Brain 2 Ranking Diagnostic

- Repeated false-positive top states:
  - `Connecticut4` top_primary_days=`23` high_conviction_hits=`14` credited_hits=`34` median_hit_rank=`1.0`
- Productive non-primary states:
  - `Indiana4` credited_hits=`37` top_primary_days=`0` strict_box=`7` straight=`8` median_hit_rank=`4.0`
  - `NewJersey4` credited_hits=`36` top_primary_days=`0` strict_box=`5` straight=`9` median_hit_rank=`6.0`
  - `NorthCarolina4` credited_hits=`31` top_primary_days=`0` strict_box=`4` straight=`9` median_hit_rank=`8.0`
  - `OntarioCanada4` credited_hits=`31` top_primary_days=`0` strict_box=`5` straight=`8` median_hit_rank=`10.0`
  - `Pennsylvania4` credited_hits=`31` top_primary_days=`0` strict_box=`0` straight=`2` median_hit_rank=`11.0`
  - `Ohio4` credited_hits=`30` top_primary_days=`0` strict_box=`2` straight=`3` median_hit_rank=`9.0`
  - `SouthCarolina4` credited_hits=`30` top_primary_days=`0` strict_box=`1` straight=`4` median_hit_rank=`13.0`
  - `Virginia4` credited_hits=`30` top_primary_days=`0` strict_box=`3` straight=`4` median_hit_rank=`14.0`

## 3. Tracker-Family Lift

- Event-layer signals with strongest gap-box lift:
  - `event::arena_primary_box` overall=`5.7%` gap_box=`72.0%` lift=`12.62x`
  - `event::arena_box_signal` overall=`8.2%` gap_box=`100.0%` lift=`12.13x`
  - `event::sandbox_box_seed` overall=`6.5%` gap_box=`60.0%` lift=`9.23x`
  - `event::preserved_not_budgeted` overall=`1.0%` gap_box=`4.0%` lift=`4.21x`
  - `event::arena_primary_vt` overall=`25.8%` gap_box=`64.0%` lift=`2.48x`
  - `event::sandbox_vt_seed` overall=`37.9%` gap_box=`72.0%` lift=`1.90x`
- Hit-layer signals with strongest strict-box lift:
  - `hit::arena_exact_signal` overall=`2.2%` strict_box=`20.0%` lift=`9.29x`
  - `hit::profit_alert_direct_match` overall=`1.4%` strict_box=`13.3%` lift=`9.29x`
  - `hit::profit_alert_implied_match` overall=`1.7%` strict_box=`13.3%` lift=`7.96x`
  - `hit::sandbox_box_seed` overall=`9.3%` strict_box=`57.8%` lift=`6.19x`
  - `hit::arena_box_signal` overall=`12.0%` strict_box=`60.0%` lift=`5.02x`
  - `hit::sandbox_vt_seed` overall=`48.3%` strict_box=`62.2%` lift=`1.29x`

## 4. Doubles Subtype Split

- `all_hits` inventory types: `none` x172, `mirror_double` x126, `double` x120
- `all_hits` double strength: `NONE` x172, `MEDIUM` x146, `STRONG` x84, `WEAK` x16
- `strict_box_hits` inventory types: `mirror_double` x23, `double` x17, `none` x5
- `strict_box_hits` double strength: `MEDIUM` x28, `STRONG` x9, `NONE` x5, `WEAK` x3
- `box_gap_rows` inventory types: `none` x11, `double` x10, `mirror_double` x4
- `box_gap_rows` double strength: `NONE` x11, `STRONG` x7, `MEDIUM` x6, `WEAK` x1

## 5. Practical Read

- Use the ranking diagnostic to find states the board over-promotes versus states that keep converting without being primary.
- Use the tracker-lift tables to separate sharp signals from ambient support before changing Brain 2 weights.
- Use the doubles subtype table to learn which double forms matter most before turning 'doubles matter' into a blunt scoring rule.
