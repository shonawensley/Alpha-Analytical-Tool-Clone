# Analysis Arena Window Deep Analysis Report

## 1. Window Overview

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04`
- Dates: `2025-12-30` to `2026-01-04`
- Winner events reviewed: `163`
- Day count: `6`
- Performance gap metrics source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__PERFORMANCE_GAP.json`

## 2. Board-Level Truth Read

- Top board states across the window: `Connecticut4` x6, `Delaware4` x6, `Florida4` x6, `Indiana4` x6, `Michigan4` x6
- Repeated board roles: `shared_host` x30
- Repeated top primary targets: `Connecticut4` x6
- Repeated best clean hosts: `Connecticut4` x6

## 3. Shared Complexes / Carryover / Decay

- Repeated canonicals: `244` x11, `559` x7, `599` x7, `668` x7, `677` x4, `368` x4, `011` x3, `138` x3, `006` x3, `449` x3, `344` x2, `116` x2
- Repeated VTRAC indices: `23` x16, `18` x11, `31` x9, `6` x6, `15` x6, `5` x5, `2` x5, `35` x5, `20` x3, `10` x3
- Carryover canonicals across consecutive days: `118` x5, `138` x5, `224` x5, `244` x5, `299` x5, `344` x5, `559` x5, `599` x5, `668` x5, `003` x4

## 4. Decay / Carryover Companion

- Decay horizon: `5` total upload days / `10` total draws max
- Tail days required beyond the last snapshot day: `4`
- State-day snapshots: `84` full_horizon=`84` right_censored=`0`
- Arena box total: same_day=`13/84` horizon=`48/84` incremental_decay=`35`
- Arena VTRAC total: same_day=`49/84` horizon=`82/84` incremental_decay=`33`
- Sandbox exact seed: same_day=`1/84` horizon=`13/84` incremental_decay=`12`
- Top-primary target decay: same_day=`5/6` horizon=`6/6`
- Decay interpretation: Same-day window grading stays clean; this scorecard separately measures delayed resolution within the configured horizon.; A miss is only a true miss when the full tail is present. Incomplete tail coverage is reported as right_censored.; Upload-day horizon is the primary setting. Draw-based accounting is preserved as a companion lens because same-day Midday/Evening crossover matters.

## 5. Tracker Families

- blackapple: events=`163` arena_box=`11` play_box=`10` gap_box=`5`
- compound event: events=`97` arena_box=`6` play_box=`5` gap_box=`4`
- due double: events=`163` arena_box=`11` play_box=`10` gap_box=`5`
- positional: events=`163` arena_box=`11` play_box=`10` gap_box=`5`
- profit alert: events=`163` arena_box=`11` play_box=`10` gap_box=`5`
- r consensus: events=`125` arena_box=`10` play_box=`8` gap_box=`5`
- survivor: events=`163` arena_box=`11` play_box=`10` gap_box=`5`
- Daily tracker ledgers present: `6/6`
- Profit-alert lead states: `PuertoRico4` x6, `OntarioCanada4` x5, `Michigan4` x5, `SouthCarolina4` x4, `Ohio4` x4, `Connecticut4` x3, `NorthCarolina4` x3, `Delaware4` x2
- Compound-event leaders: `Michigan4:Combined:ENGINE_GOV` x3, `Connecticut4:Combined:ENGINE_GOV` x2, `SouthCarolina4:Midday:CARRY_PERM` x2, `Ohio4:Combined:STRAIGHT_GATE` x2, `Delaware4:Combined:ENGINE_GOV` x2, `OntarioCanada4:Combined:ENGINE_GOV` x2, `Ohio4:Combined:CARRY_PERM` x2, `Connecticut4:Combined:CLAMP_4` x2
- Blackapple ALERT states: `NorthCarolina4` x7, `Ohio4` x2, `NewYork4` x2, `Indiana4` x1, `Connecticut4` x1, `OntarioCanada4` x1, `SouthCarolina4` x1, `Florida4` x1
- Blackapple WATCH states: `Indiana4` x7, `Florida4` x6, `NewYork4` x6, `Delaware4` x5, `Michigan4` x5, `NorthCarolina4` x4, `OntarioCanada4` x4, `Connecticut4` x3
- Due-double threshold states: `PuertoRico4` x5, `OntarioCanada4` x5, `SouthCarolina4` x4, `Michigan4` x4, `Ohio4` x3, `Delaware4` x2, `NewYork4` x2, `Pennsylvania4` x2
- Repeat-watch exact hits: _none_
- Scoreboard hint carries: profit=`Connecticut4` x6, `Delaware4` x6, `Florida4` x6, `Indiana4` x6, `Michigan4` x6, `NewJersey4` x6, `NewYork4` x6, `NorthCarolina4` x6; compound=`Connecticut4` x6, `Delaware4` x6, `Florida4` x6, `Indiana4` x6, `Michigan4` x6, `NewJersey4` x6, `NewYork4` x6, `NorthCarolina4` x6; BA=`Connecticut4` x6, `Delaware4` x6, `Florida4` x6, `Indiana4` x6, `Michigan4` x6, `NewJersey4` x6, `NewYork4` x6, `NorthCarolina4` x6; due=`Connecticut4` x6, `Delaware4` x6, `Florida4` x6, `Indiana4` x6, `Michigan4` x6, `NewJersey4` x6, `NewYork4` x6, `NorthCarolina4` x6; r_consensus=`Connecticut4` x6, `Delaware4` x6, `Florida4` x6, `Indiana4` x6, `Michigan4` x6, `NewJersey4` x6, `NewYork4` x6, `NorthCarolina4` x6
- Doubles result types: `double` x41, `mirror_double` x33, `triple` x1

## 6. Translational Pressure

- Boxed seeds: `011` x51, `017` x49, `006` x41, `004` x38, `014` x38, `001` x35, `007` x33, `009` x32, `005` x30, `044` x24
- Straight seeds: `040` x21, `004` x19, `400` x18, `900` x16, `009` x16, `090` x16, `202` x16, `242` x15, `066` x14, `022` x13
- VT-box seeds: `23` x71, `18` x69, `15` x57, `12` x50, `7` x44, `5` x43, `2` x40, `9` x40, `3` x40, `10` x39
- Preserved-not-budgeted canonicals: `024` x7, `245` x7, `026` x7, `029` x6, `067` x6, `078` x5, `079` x5, `012` x5, `013` x4, `037` x4

## 7. Pure Arena Finalist / Candidate Layer

- Any candidate-like event coverage: `64/163` (`39.3%`)
- VT-like finalist coverage: `61/163` (`37.4%`)
- Box-like candidate coverage: `14/163` (`8.6%`)
- Hit finalist support: `81/103` (`78.6%`)
- Straight hits with finalist support: `19/20` (`95.0%`)
- Strict box hits with finalist support: `10/10` (`100.0%`)
- Opportunity-gap box rows: `5/163` (`3.1%`)
- Opportunity-gap rows with explicit arena box: `5/5` (`100.0%`)
  - The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
  - Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
  - The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.

## 8. Translator Learning Ledger

- Translator-learning rows: `70/163`
- Box-gap cohort rate: `3.1%`
- Exact-gap cohort rate: `0.0%`
- Box-converted cohort rate: `3.7%`
- VT-converted cohort rate: `15.3%`
- Translator cohort counts: `ARENA_EXPLICIT` x11, `BOX_CONVERTED` x6, `BOX_FINALIST` x14, `BOX_GAP` x5, `EXACT_CONVERTED` x1, `PRESERVED` x3, `VT_CONVERTED` x25, `VT_FINALIST` x61
- Translator frontier mix: `FAMILY_FRONTIER` x6, `FEEDER_TO_FRONTIER` x21, `HIDDEN_COMPRESSED_FRONTIER` x26, `VTRAC_FRONTIER` x17
  - `2025-12-31` `NewYork4` `Evening` winner=`116` cohort=`BOX_GAP` frontier=`FEEDER_TO_FRONTIER` rank=`7`
  - `2026-01-01` `NorthCarolina4` `Evening` winner=`053` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` rank=`8`
  - `2025-12-30` `NorthCarolina4` `Midday` winner=`455` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` rank=`8`
  - `2025-12-30` `Pennsylvania4` `Evening` winner=`173` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` rank=`11`
  - `2026-01-03` `SouthCarolina4` `Midday` winner=`189` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`13`
  - Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
  - Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
  - Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
  - Current window produced `5` explicit box-gap rows worth preserving for translator study.
  - Preserved-not-budgeted rows (`3`) remain useful as a reserve cohort for later combo/budget design.

## 9. Winner HTML Frontier

- Frontier cases reviewed: `163`
- Frontier signature mix: `HIDDEN_COMPRESSED_FRONTIER` x62, `FEEDER_TO_FRONTIER` x49, `VTRAC_FRONTIER` x44, `FAMILY_FRONTIER` x8
- Frontier hit-class mix: `NONE` x117, `BOXED|VTRAC_BOXED` x26, `STRAIGHT|BOXED|VTRAC_STRAIGHT|VTRAC_BOXED` x20
- Average frontier scores: `compression_score`=1.000, `cross_variant_echo_score`=0.408, `double_anchor_score`=0.334, `family_frontier_score`=0.221, `feeder_progression_score`=0.546, `frontier_purity_score`=0.266, `frontier_strength_score`=55.954, `hidden_winner_score`=0.492, `literal_frontier_score`=0.044, `vertical_stability_score`=0.947, `vtrac_frontier_score`=0.320
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
