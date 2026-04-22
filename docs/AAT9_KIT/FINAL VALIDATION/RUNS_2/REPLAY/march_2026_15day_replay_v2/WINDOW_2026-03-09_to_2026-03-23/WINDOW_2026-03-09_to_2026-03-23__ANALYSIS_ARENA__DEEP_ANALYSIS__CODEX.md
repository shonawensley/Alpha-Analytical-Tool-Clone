# Analysis Arena Window Deep Analysis Report

## 1. Window Overview

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23`
- Dates: `2026-03-09` to `2026-03-23`
- Winner events reviewed: `414`
- Day count: `15`
- Performance gap metrics source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/march_2026_15day_replay_v2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__PERFORMANCE_GAP.json`

## 2. Board-Level Truth Read

- Top board states across the window: `Connecticut4` x15, `Delaware4` x15, `Florida4` x15, `Indiana4` x15, `Michigan4` x15
- Repeated board roles: `shared_host` x75
- Repeated top primary targets: `Connecticut4` x15
- Repeated best clean hosts: `Connecticut4` x15

## 3. Shared Complexes / Carryover / Decay

- Repeated canonicals: `559` x22, `224` x20, `599` x18, `006` x9, `001` x9, `455` x8, `113` x7, `499` x6, `368` x5, `044` x5, `344` x5, `244` x5
- Repeated VTRAC indices: `5` x31, `15` x26, `28` x20, `18` x17, `23` x13, `12` x12, `2` x11, `3` x8, `10` x8, `31` x7
- Carryover canonicals across consecutive days: `224` x14, `559` x14, `599` x14, `006` x12, `368` x12, `244` x12, `455` x11, `667` x10, `069` x9, `255` x9

## 4. Decay / Carryover Companion

- Decay horizon: _not generated_

## 5. Tracker Families

- blackapple: events=`414` arena_box=`35` play_box=`29` gap_box=`21`
- compound event: events=`268` arena_box=`21` play_box=`18` gap_box=`10`
- due double: events=`414` arena_box=`35` play_box=`29` gap_box=`21`
- positional: events=`414` arena_box=`35` play_box=`29` gap_box=`21`
- profit alert: events=`414` arena_box=`35` play_box=`29` gap_box=`21`
- r consensus: events=`352` arena_box=`30` play_box=`26` gap_box=`17`
- survivor: events=`414` arena_box=`35` play_box=`29` gap_box=`21`
- Daily tracker ledgers present: `15/15`
- Profit-alert lead states: _none_
- Compound-event leaders: _none_
- Blackapple ALERT states: _none_
- Blackapple WATCH states: _none_
- Due-double threshold states: _none_
- Repeat-watch exact hits: _none_
- Scoreboard hint carries: profit=`Connecticut4` x15, `Delaware4` x15, `Florida4` x15, `Indiana4` x15, `Michigan4` x15, `NewJersey4` x15, `NewYork4` x15, `NorthCarolina4` x15; compound=`Connecticut4` x15, `Delaware4` x15, `Florida4` x15, `Indiana4` x15, `Michigan4` x15, `NewJersey4` x15, `NewYork4` x15, `NorthCarolina4` x15; BA=`Connecticut4` x15, `Delaware4` x15, `Florida4` x15, `Indiana4` x15, `Michigan4` x15, `NewJersey4` x15, `NewYork4` x15, `NorthCarolina4` x15; due=`Connecticut4` x15, `Delaware4` x15, `Florida4` x15, `Indiana4` x15, `Michigan4` x15, `NewJersey4` x15, `NewYork4` x15, `NorthCarolina4` x15; r_consensus=`Connecticut4` x15, `Delaware4` x15, `Florida4` x15, `Indiana4` x15, `Michigan4` x15, `NewJersey4` x15, `NewYork4` x15, `NorthCarolina4` x15
- Doubles result types: `double` x131, `mirror_double` x89, `triple` x3

## 6. Translational Pressure

- Boxed seeds: `004` x134, `009` x124, `559` x104, `005` x99, `001` x96, `007` x96, `006` x94, `011` x94, `013` x86, `014` x81
- Straight seeds: `090` x53, `009` x50, `900` x47, `040` x41, `004` x40, `400` x37, `070` x34, `700` x33, `007` x32, `066` x30
- VT-box seeds: `23` x192, `18` x171, `15` x169, `5` x149, `12` x122, `2` x95, `31` x92, `28` x90, `8` x87, `33` x87
- Preserved-not-budgeted canonicals: `449` x17, `499` x14, `029` x8, `159` x8, `227` x8, `468` x7, `039` x7, `157` x6, `224` x6, `559` x6

## 7. Pure Arena Finalist / Candidate Layer

- Any candidate-like event coverage: `168/414` (`40.6%`)
- VT-like finalist coverage: `162/414` (`39.1%`)
- Box-like candidate coverage: `40/414` (`9.7%`)
- Hit finalist support: `229/274` (`83.6%`)
- Straight hits with finalist support: `46/54` (`85.2%`)
- Strict box hits with finalist support: `24/29` (`82.8%`)
- Opportunity-gap box rows: `21/414` (`5.1%`)
- Opportunity-gap rows with explicit arena box: `21/21` (`100.0%`)
  - The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
  - Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
  - The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.

## 8. Translator Learning Ledger

- Translator-learning rows: `189/414`
- Box-gap cohort rate: `5.1%`
- Exact-gap cohort rate: `0.5%`
- Box-converted cohort rate: `4.1%`
- VT-converted cohort rate: `16.4%`
- Translator cohort counts: `ARENA_EXPLICIT` x40, `BOX_CONVERTED` x17, `BOX_FINALIST` x40, `BOX_GAP` x21, `EXACT_CONVERTED` x7, `EXACT_GAP` x2, `PRESERVED` x1, `VT_CONVERTED` x68, `VT_FINALIST` x162
- Translator frontier mix: `FAMILY_FRONTIER` x16, `FEEDER_TO_FRONTIER` x58, `HIDDEN_COMPRESSED_FRONTIER` x78, `LITERAL_FRONTIER` x2, `VTRAC_FRONTIER` x35
  - `2026-03-09` `Connecticut4` `Evening` winner=`091` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`1`
  - `2026-03-23` `Florida4` `Midday` winner=`196` cohort=`BOX_GAP` frontier=`FEEDER_TO_FRONTIER` rank=`3`
  - `2026-03-11` `Florida4` `Midday` winner=`700` cohort=`BOX_GAP` frontier=`VTRAC_FRONTIER` rank=`3`
  - `2026-03-10` `Indiana4` `Evening` winner=`070` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`4`
  - `2026-03-23` `Indiana4` `Evening` winner=`420` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`4`
  - Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
  - Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
  - Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
  - Current window produced `21` explicit box-gap rows worth preserving for translator study.
  - Preserved-not-budgeted rows (`1`) remain useful as a reserve cohort for later combo/budget design.

## 9. Winner HTML Frontier

- Frontier cases reviewed: `414`
- Frontier signature mix: `HIDDEN_COMPRESSED_FRONTIER` x156, `FEEDER_TO_FRONTIER` x132, `VTRAC_FRONTIER` x103, `FAMILY_FRONTIER` x21, `LITERAL_FRONTIER` x2
- Frontier hit-class mix: `NONE` x287, `BOXED|VTRAC_BOXED` x73, `STRAIGHT|BOXED|VTRAC_STRAIGHT|VTRAC_BOXED` x54
- Average frontier scores: `compression_score`=1.000, `cross_variant_echo_score`=0.406, `double_anchor_score`=0.382, `family_frontier_score`=0.207, `feeder_progression_score`=0.536, `frontier_purity_score`=0.251, `frontier_strength_score`=55.409, `hidden_winner_score`=0.477, `literal_frontier_score`=0.038, `vertical_stability_score`=0.931, `vtrac_frontier_score`=0.317
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
