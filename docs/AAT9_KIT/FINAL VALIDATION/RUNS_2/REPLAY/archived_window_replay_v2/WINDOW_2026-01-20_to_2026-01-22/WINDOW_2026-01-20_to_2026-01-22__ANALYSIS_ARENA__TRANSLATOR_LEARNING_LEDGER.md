# Analysis Arena Translator-Learning Ledger

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22`
- Dates: `2026-01-20` to `2026-01-22`
- Winner-event denominator: `84`
- Translator-learning rows: `37`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv`

## 2. Cohort Counts

- VT_FINALIST: `31`
- VT_CONVERTED: `15`
- ARENA_EXPLICIT: `5`
- BOX_FINALIST: `5`
- BOX_CONVERTED: `3`
- BOX_GAP: `2`
- EXACT_CONVERTED: `1`

## 3. Signature Mix

- Arena finalist signatures: `PARTIAL_ARENA_FINALIST` x16, `LIGHT_ARENA_FINALIST` x13, `UNSPECIFIED` x4, `CONTROL_ARM_ONLY_CATCH` x4
- Frontier signatures: `HIDDEN_COMPRESSED_FRONTIER` x16, `VTRAC_FRONTIER` x8, `FEEDER_TO_FRONTIER` x8, `FAMILY_FRONTIER` x5
- Top states in the teaching cohort: `Indiana4` x4, `SouthCarolina4` x4, `Virginia4` x4, `Delaware4` x3, `NewJersey4` x3, `NorthCarolina4` x3, `OntarioCanada4` x3, `NewYork4` x2

## 4. Priority Examples

- `2026-01-21` `NorthCarolina4` `Evening` winner=`577` rank=`8` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`WEAK`
- `2026-01-22` `Virginia4` `Evening` winner=`100` rank=`14` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`
- `2026-01-22` `Connecticut4` `Midday` winner=`556` rank=`1` cohort=`VT_CONVERTED` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`LIGHT_ARENA_FINALIST` double=`STRONG`
- `2026-01-21` `Connecticut4` `Midday` winner=`786` rank=`1` cohort=`VT_FINALIST` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`` double=`-`
- `2026-01-20` `Delaware4` `Midday` winner=`099` rank=`2` cohort=`VT_FINALIST` frontier=`VTRAC_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`
- `2026-01-21` `Delaware4` `Midday` winner=`029` rank=`2` cohort=`VT_FINALIST` frontier=`FAMILY_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-01-22` `Delaware4` `Evening` winner=`243` rank=`2` cohort=`VT_FINALIST` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`` double=`-`
- `2026-01-21` `Florida4` `Midday` winner=`350` rank=`3` cohort=`VT_FINALIST` frontier=`VTRAC_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`

## 5. Practical Read

- Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
- Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
- Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
- Current window produced `2` explicit box-gap rows worth preserving for translator study.
