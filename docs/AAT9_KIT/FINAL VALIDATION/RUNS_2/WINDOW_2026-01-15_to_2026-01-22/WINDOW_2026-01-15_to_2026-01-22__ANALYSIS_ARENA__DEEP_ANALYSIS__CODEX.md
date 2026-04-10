# Analysis Arena Window Deep Analysis Report

## 1. Window Overview

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22`
- Dates: `2026-01-15` to `2026-01-22`
- Winner events reviewed: `221`
- Day count: `8`
- Performance gap metrics source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/WINDOW_2026-01-15_to_2026-01-22__ANALYSIS_ARENA__PERFORMANCE_GAP.json`

## 2. Board-Level Truth Read

- Top board states across the window: `Connecticut4` x8, `Delaware4` x8, `Florida4` x8, `Indiana4` x8, `Michigan4` x8
- Repeated board roles: `shared_host` x40
- Repeated top primary targets: `Connecticut4` x8
- Repeated best clean hosts: `Connecticut4` x8

## 3. Shared Complexes / Carryover / Decay

- Repeated canonicals: `559` x16, `255` x10, `224` x8, `007` x8, `599` x7, `259` x7, `077` x6, `899` x3, `225` x3, `368` x3, `011` x3, `378` x3
- Repeated VTRAC indices: `10` x14, `15` x12, `3` x11, `5` x9, `23` x7, `12` x7, `27` x5, `6` x5, `28` x5, `31` x4
- Carryover canonicals across consecutive days: `009` x7, `224` x7, `244` x7, `255` x7, `334` x7, `559` x7, `599` x7, `225` x6, `377` x6, `044` x6

## 4. Decay / Carryover Companion

- Decay horizon: `5` total upload days / `10` total draws max
- Tail days required beyond the last snapshot day: `4`
- State-day snapshots: `112` full_horizon=`56` right_censored=`56`
- Arena box total: same_day=`20/112` horizon=`48/112` incremental_decay=`28`
- Arena VTRAC total: same_day=`67/112` horizon=`102/112` incremental_decay=`35`
- Sandbox exact seed: same_day=`2/112` horizon=`6/112` incremental_decay=`4`
- Top-primary target decay: same_day=`5/8` horizon=`8/8`
- Decay interpretation: Same-day window grading stays clean; this scorecard separately measures delayed resolution within the configured horizon.; A miss is only a true miss when the full tail is present. Incomplete tail coverage is reported as right_censored.; Upload-day horizon is the primary setting. Draw-based accounting is preserved as a companion lens because same-day Midday/Evening crossover matters.

## 5. Tracker Families

- blackapple: events=`221` arena_box=`19` play_box=`12` gap_box=`11`
- compound event: events=`134` arena_box=`17` play_box=`9` gap_box=`10`
- due double: events=`221` arena_box=`19` play_box=`12` gap_box=`11`
- positional: events=`221` arena_box=`19` play_box=`12` gap_box=`11`
- profit alert: events=`221` arena_box=`19` play_box=`12` gap_box=`11`
- r consensus: events=`170` arena_box=`15` play_box=`9` gap_box=`8`
- survivor: events=`221` arena_box=`19` play_box=`12` gap_box=`11`
- Daily tracker ledgers present: `8/8`
- Profit-alert lead states: `Virginia4` x5, `NewJersey4` x5, `OntarioCanada4` x4, `Pennsylvania4` x4, `Delaware4` x3, `Indiana4` x3, `NorthCarolina4` x3, `PuertoRico4` x2
- Compound-event leaders: _none_
- Blackapple ALERT states: `Delaware4` x5, `Indiana4` x4, `Ohio4` x3, `NorthCarolina4` x2, `OntarioCanada4` x2, `Pennsylvania4` x2, `Michigan4` x2, `SouthCarolina4` x2
- Blackapple WATCH states: `Florida4` x8, `NewJersey4` x8, `Michigan4` x7, `Connecticut4` x6, `NewYork4` x5, `Indiana4` x4, `NorthCarolina4` x3, `Delaware4` x3
- Due-double threshold states: `OntarioCanada4` x4, `Indiana4` x4, `NewYork4` x4, `NorthCarolina4` x4, `Connecticut4` x4, `Virginia4` x4, `SouthCarolina4` x3, `NewJersey4` x2
- Repeat-watch exact hits: `NewJersey4:Midday:29` x1
- Scoreboard hint carries: profit=`Connecticut4` x8, `Delaware4` x8, `Florida4` x8, `Indiana4` x8, `Michigan4` x8, `NewJersey4` x8, `NewYork4` x8, `NorthCarolina4` x8; compound=`Connecticut4` x8, `Delaware4` x8, `Florida4` x8, `Indiana4` x8, `Michigan4` x8, `NewJersey4` x8, `NewYork4` x8, `NorthCarolina4` x8; BA=`Connecticut4` x8, `Delaware4` x8, `Florida4` x8, `Indiana4` x8, `Michigan4` x8, `NewJersey4` x8, `NewYork4` x8, `NorthCarolina4` x8; due=`Connecticut4` x8, `Delaware4` x8, `Florida4` x8, `Indiana4` x8, `Michigan4` x8, `NewJersey4` x8, `NewYork4` x8, `NorthCarolina4` x8; r_consensus=`Connecticut4` x8, `Delaware4` x8, `Florida4` x8, `Indiana4` x8, `Michigan4` x8, `NewJersey4` x8, `NewYork4` x8, `NorthCarolina4` x8
- Doubles result types: `mirror_double` x59, `double` x58, `triple` x2

## 6. Translational Pressure

- Boxed seeds: `001` x70, `004` x64, `009` x61, `006` x60, `007` x57, `014` x49, `005` x49, `011` x45, `017` x41, `559` x37
- Straight seeds: `040` x27, `004` x26, `400` x24, `009` x23, `090` x22, `100` x22, `900` x21, `001` x21, `010` x20, `007` x17
- VT-box seeds: `23` x103, `5` x88, `15` x86, `12` x80, `18` x71, `33` x66, `2` x64, `3` x61, `9` x53, `21` x50
- Preserved-not-budgeted canonicals: `017` x17, `028` x15, `012` x12, `026` x9, `245` x8, `023` x7, `019` x6, `037` x5, `357` x4, `499` x4

## 7. Pure Arena Finalist / Candidate Layer

- Any candidate-like event coverage: `90/221` (`40.7%`)
- VT-like finalist coverage: `85/221` (`38.5%`)
- Box-like candidate coverage: `20/221` (`9.0%`)
- Hit finalist support: `118/142` (`83.1%`)
- Straight hits with finalist support: `27/30` (`90.0%`)
- Strict box hits with finalist support: `11/12` (`91.7%`)
- Opportunity-gap box rows: `11/221` (`5.0%`)
- Opportunity-gap rows with explicit arena box: `11/11` (`100.0%`)
  - The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
  - Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
  - The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.

## 8. Translator Learning Ledger

- Translator-learning rows: `98/221`
- Box-gap cohort rate: `5.0%`
- Exact-gap cohort rate: `0.0%`
- Box-converted cohort rate: `3.6%`
- VT-converted cohort rate: `15.4%`
- Translator cohort counts: `ARENA_EXPLICIT` x19, `BOX_CONVERTED` x8, `BOX_FINALIST` x20, `BOX_GAP` x11, `EXACT_CONVERTED` x2, `PRESERVED` x1, `VT_CONVERTED` x34, `VT_FINALIST` x85
- Translator frontier mix: `FAMILY_FRONTIER` x10, `FEEDER_TO_FRONTIER` x22, `HIDDEN_COMPRESSED_FRONTIER` x50, `VTRAC_FRONTIER` x16
  - `2026-01-16` `Connecticut4` `Evening` winner=`431` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`1`
  - `2026-01-16` `Delaware4` `Evening` winner=`107` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`2`
  - `2026-01-19` `Michigan4` `Evening` winner=`402` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`5`
  - `2026-01-16` `NewJersey4` `Evening` winner=`180` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`6`
  - `2026-01-18` `NewJersey4` `Evening` winner=`955` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`6`
  - Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
  - Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
  - Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
  - Current window produced `11` explicit box-gap rows worth preserving for translator study.
  - Preserved-not-budgeted rows (`1`) remain useful as a reserve cohort for later combo/budget design.

## 9. Winner HTML Frontier

- Frontier cases reviewed: `220`
- Frontier signature mix: `HIDDEN_COMPRESSED_FRONTIER` x91, `FEEDER_TO_FRONTIER` x65, `VTRAC_FRONTIER` x54, `FAMILY_FRONTIER` x10
- Frontier hit-class mix: `NONE` x151, `BOXED|VTRAC_BOXED` x39, `STRAIGHT|BOXED|VTRAC_STRAIGHT|VTRAC_BOXED` x30
- Average frontier scores: `compression_score`=1.000, `cross_variant_echo_score`=0.415, `double_anchor_score`=0.342, `family_frontier_score`=0.209, `feeder_progression_score`=0.539, `frontier_purity_score`=0.255, `frontier_strength_score`=55.301, `hidden_winner_score`=0.506, `literal_frontier_score`=0.037, `vertical_stability_score`=0.909, `vtrac_frontier_score`=0.317
- Frontier promotion ideas sampled: `3`
  - `-` `-`: -
  - `-` `-`: -
  - `-` `-`: -

## 10. Best Findings / Worst Misses

- Control-arm realized rows sampled: `12`
- Opportunity-gap rows sampled: `12`
- Direct miss rows sampled: `0`

## 11. Promotion Ledger

- Preserve: Keep arena truth quality, control-arm realization, and opportunity gap as separate evaluation layers.
- Preserve: Keep translation sandbox seeds and preserved-not-budgeted canonicals as explicit translator-learning inputs.
- Observe: Repeated carryover canonicals across consecutive days.
- Observe: Tracker families that consistently show arena-box support but weak downstream realization.
- Demote: Using B12/B24/B36 alone as the main measure of analysis quality.
