# Analysis Arena Translator-Learning Ledger

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18`
- Dates: `2026-01-15` to `2026-01-18`
- Winner-event denominator: `109`
- Translator-learning rows: `52`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv`

## 2. Cohort Counts

- VT_FINALIST: `46`
- VT_CONVERTED: `18`
- ARENA_EXPLICIT: `12`
- BOX_FINALIST: `12`
- BOX_CONVERTED: `8`
- BOX_GAP: `4`
- EXACT_CONVERTED: `3`

## 3. Signature Mix

- Arena finalist signatures: `PARTIAL_ARENA_FINALIST` x24, `LIGHT_ARENA_FINALIST` x20, `UNSPECIFIED` x5, `CLEAR_ARENA_FINALIST` x3
- Frontier signatures: `HIDDEN_COMPRESSED_FRONTIER` x29, `FEEDER_TO_FRONTIER` x12, `VTRAC_FRONTIER` x7, `FAMILY_FRONTIER` x4
- Top states in the teaching cohort: `NewJersey4` x7, `Indiana4` x6, `Michigan4` x6, `SouthCarolina4` x6, `Connecticut4` x4, `OntarioCanada4` x4, `Delaware4` x4, `NorthCarolina4` x3

## 4. Priority Examples

- `2026-01-16` `Connecticut4` `Evening` winner=`431` rank=`1` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`LIGHT_ARENA_FINALIST` double=`-`
- `2026-01-16` `Delaware4` `Evening` winner=`107` rank=`2` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-01-18` `NewJersey4` `Evening` winner=`955` rank=`6` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-15` `NorthCarolina4` `Midday` winner=`045` rank=`8` cohort=`BOX_GAP` frontier=`FEEDER_TO_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`
- `2026-01-18` `Connecticut4` `Midday` winner=`238` rank=`1` cohort=`EXACT_CONVERTED` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`CLEAR_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-15` `Connecticut4` `Midday` winner=`495` rank=`1` cohort=`VT_FINALIST` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`LIGHT_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-18` `Connecticut4` `Evening` winner=`781` rank=`1` cohort=`VT_CONVERTED` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-01-17` `Delaware4` `Midday` winner=`126` rank=`2` cohort=`VT_FINALIST` frontier=`FAMILY_FRONTIER` sig=`LIGHT_ARENA_FINALIST` double=`WEAK`

## 5. Practical Read

- Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
- Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
- Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
- Current window produced `4` explicit box-gap rows worth preserving for translator study.
