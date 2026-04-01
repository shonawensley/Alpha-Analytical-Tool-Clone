# Analysis Arena Window Deep Analysis Report

## 1. Window Overview

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18`
- Dates: `2026-01-15` to `2026-01-18`
- Winner events reviewed: `109`
- Day count: `4`
- Performance gap metrics source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__PERFORMANCE_GAP.json`

## 2. Board-Level Truth Read

- Top board states across the window: `Connecticut4` x4, `Delaware4` x4, `Florida4` x4, `Indiana4` x4, `Michigan4` x4
- Repeated board roles: `shared_host` x20
- Repeated top primary targets: `Connecticut4` x4
- Repeated best clean hosts: `Connecticut4` x4

## 3. Shared Complexes / Carryover / Decay

- Repeated canonicals: `559` x10, `599` x6, `899` x3, `225` x3, `255` x3, `368` x3, `059` x2, `249` x2, `177` x2, `577` x2, `224` x2, `344` x2
- Repeated VTRAC indices: `15` x9, `5` x5, `10` x5, `34` x3, `31` x3, `20` x3, `27` x3, `23` x3, `18` x3, `12` x3
- Carryover canonicals across consecutive days: `001` x3, `009` x3, `014` x3, `049` x3, `224` x3, `225` x3, `244` x3, `255` x3, `334` x3, `344` x3

## 4. Tracker Families

- blackapple: events=`109` arena_box=`12` play_box=`11` gap_box=`4`
- compound event: events=`70` arena_box=`10` play_box=`9` gap_box=`3`
- due double: events=`109` arena_box=`12` play_box=`11` gap_box=`4`
- positional: events=`109` arena_box=`12` play_box=`11` gap_box=`4`
- profit alert: events=`109` arena_box=`12` play_box=`11` gap_box=`4`
- r consensus: events=`78` arena_box=`9` play_box=`9` gap_box=`2`
- survivor: events=`109` arena_box=`12` play_box=`11` gap_box=`4`
- Daily tracker ledgers present: `4/4`
- Profit-alert lead states: `NewJersey4` x4, `OntarioCanada4` x3, `Virginia4` x3, `Pennsylvania4` x3, `PuertoRico4` x2, `Michigan4` x2, `NewYork4` x2, `Indiana4` x2
- Compound-event leaders: _none_
- Blackapple ALERT states: `Indiana4` x4, `NorthCarolina4` x2, `Pennsylvania4` x2, `Michigan4` x2, `Delaware4` x1, `Florida4` x1, `OntarioCanada4` x1, `Virginia4` x1
- Blackapple WATCH states: `Florida4` x6, `Michigan4` x5, `NewJersey4` x5, `Indiana4` x4, `Connecticut4` x4, `NewYork4` x3, `Delaware4` x3, `NorthCarolina4` x1
- Due-double threshold states: `NewYork4` x4, `OntarioCanada4` x3, `NorthCarolina4` x3, `NewJersey4` x2, `Indiana4` x2, `Connecticut4` x2, `Virginia4` x2, `Pennsylvania4` x2
- Repeat-watch exact hits: `NewJersey4:Midday:29` x1
- Scoreboard hint carries: profit=`Connecticut4` x4, `Delaware4` x4, `Florida4` x4, `Indiana4` x4, `Michigan4` x4, `NewJersey4` x4, `NewYork4` x4, `NorthCarolina4` x4; compound=`Connecticut4` x4, `Delaware4` x4, `Florida4` x4, `Indiana4` x4, `Michigan4` x4, `NewJersey4` x4, `NewYork4` x4, `NorthCarolina4` x4; BA=`Connecticut4` x4, `Delaware4` x4, `Florida4` x4, `Indiana4` x4, `Michigan4` x4, `NewJersey4` x4, `NewYork4` x4, `NorthCarolina4` x4; due=`Connecticut4` x4, `Delaware4` x4, `Florida4` x4, `Indiana4` x4, `Michigan4` x4, `NewJersey4` x4, `NewYork4` x4, `NorthCarolina4` x4; r_consensus=`Connecticut4` x4, `Delaware4` x4, `Florida4` x4, `Indiana4` x4, `Michigan4` x4, `NewJersey4` x4, `NewYork4` x4, `NorthCarolina4` x4
- Doubles result types: `mirror_double` x35, `double` x27, `triple` x2

## 5. Translational Pressure

- Boxed seeds: `001` x35, `004` x32, `009` x31, `006` x30, `014` x29, `007` x25, `013` x22, `017` x22, `005` x21, `011` x20
- Straight seeds: `040` x13, `400` x13, `004` x12, `090` x11, `009` x10, `900` x10, `100` x9, `808` x8, `022` x8, `202` x8
- VT-box seeds: `23` x53, `15` x47, `5` x43, `33` x39, `12` x36, `18` x36, `2` x33, `9` x31, `3` x27, `21` x26
- Preserved-not-budgeted canonicals: `017` x7, `028` x7, `023` x4, `012` x4, `014` x3, `037` x3, `029` x3, `059` x3, `026` x3, `245` x3

## 6. Pure Arena Finalist / Candidate Layer

- Any candidate-like event coverage: `50/109` (`45.9%`)
- VT-like finalist coverage: `46/109` (`42.2%`)
- Box-like candidate coverage: `12/109` (`11.0%`)
- Hit finalist support: `65/79` (`82.3%`)
- Straight hits with finalist support: `16/16` (`100.0%`)
- Strict box hits with finalist support: `11/11` (`100.0%`)
- Opportunity-gap box rows: `4/109` (`3.7%`)
- Opportunity-gap rows with explicit arena box: `4/4` (`100.0%`)
  - The arena is currently stronger at preserving finalist/VTRAC territory than at expressing a finished box-like combo layer.
  - Most converted hits carried arena-native finalist support, which means the old downstream arm is not doing all the work alone.
  - The opportunity-gap box rows are especially valuable because they isolate places where arena showed candidate-like box evidence but the downstream arm failed to convert.

## 7. Translator Learning Ledger

- Translator-learning rows: `52/109`
- Box-gap cohort rate: `3.7%`
- Exact-gap cohort rate: `0.0%`
- Box-converted cohort rate: `7.3%`
- VT-converted cohort rate: `16.5%`
- Translator cohort counts: `ARENA_EXPLICIT` x12, `BOX_CONVERTED` x8, `BOX_FINALIST` x12, `BOX_GAP` x4, `EXACT_CONVERTED` x3, `VT_CONVERTED` x18, `VT_FINALIST` x46
- Translator frontier mix: `FAMILY_FRONTIER` x4, `FEEDER_TO_FRONTIER` x12, `HIDDEN_COMPRESSED_FRONTIER` x29, `VTRAC_FRONTIER` x7
  - `2026-01-16` `Connecticut4` `Evening` winner=`431` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`1`
  - `2026-01-16` `Delaware4` `Evening` winner=`107` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`2`
  - `2026-01-18` `NewJersey4` `Evening` winner=`955` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`6`
  - `2026-01-15` `NorthCarolina4` `Midday` winner=`045` cohort=`BOX_GAP` frontier=`FEEDER_TO_FRONTIER` rank=`8`
  - `2026-01-18` `Connecticut4` `Midday` winner=`238` cohort=`EXACT_CONVERTED` frontier=`HIDDEN_COMPRESSED_FRONTIER` rank=`1`
  - Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
  - Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
  - Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
  - Current window produced `4` explicit box-gap rows worth preserving for translator study.

## 8. Winner HTML Frontier

- Frontier cases reviewed: `108`
- Frontier signature mix: `HIDDEN_COMPRESSED_FRONTIER` x50, `VTRAC_FRONTIER` x28, `FEEDER_TO_FRONTIER` x26, `FAMILY_FRONTIER` x4
- Frontier hit-class mix: `NONE` x71, `BOXED|VTRAC_BOXED` x21, `STRAIGHT|BOXED|VTRAC_STRAIGHT|VTRAC_BOXED` x16
- Average frontier scores: `compression_score`=1.000, `cross_variant_echo_score`=0.415, `double_anchor_score`=0.369, `family_frontier_score`=0.216, `feeder_progression_score`=0.537, `frontier_purity_score`=0.260, `frontier_strength_score`=56.258, `hidden_winner_score`=0.534, `literal_frontier_score`=0.037, `vertical_stability_score`=0.923, `vtrac_frontier_score`=0.319
- Frontier promotion ideas sampled: `3`
  - `-` `-`: -
  - `-` `-`: -
  - `-` `-`: -

## 9. Best Findings / Worst Misses

- Control-arm realized rows sampled: `12`
- Opportunity-gap rows sampled: `12`
- Direct miss rows sampled: `0`

## 10. Promotion Ledger

- Preserve: Keep arena truth quality, control-arm realization, and opportunity gap as separate evaluation layers.
- Preserve: Keep translation sandbox seeds and preserved-not-budgeted canonicals as explicit translator-learning inputs.
- Observe: Repeated carryover canonicals across consecutive days.
- Observe: Tracker families that consistently show arena-box support but weak downstream realization.
- Demote: Using B12/B24/B36 alone as the main measure of analysis quality.
