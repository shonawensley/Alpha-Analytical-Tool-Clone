# Analysis Arena Translator-Learning Ledger

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22`
- Dates: `2026-01-15` to `2026-01-22`
- Winner-event denominator: `221`
- Translator-learning rows: `98`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/WINDOW_2026-01-15_to_2026-01-22__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv`

## 2. Cohort Counts

- VT_FINALIST: `85`
- VT_CONVERTED: `34`
- BOX_FINALIST: `20`
- ARENA_EXPLICIT: `19`
- BOX_GAP: `11`
- BOX_CONVERTED: `8`
- EXACT_CONVERTED: `2`
- PRESERVED: `1`

## 3. Signature Mix

- Arena finalist signatures: `PARTIAL_ARENA_FINALIST` x39, `LIGHT_ARENA_FINALIST` x36, `UNSPECIFIED` x16, `CLEAR_ARENA_FINALIST` x4, `CONTROL_ARM_ONLY_CATCH` x3
- Frontier signatures: `HIDDEN_COMPRESSED_FRONTIER` x50, `FEEDER_TO_FRONTIER` x22, `VTRAC_FRONTIER` x16, `FAMILY_FRONTIER` x10
- Top states in the teaching cohort: `Indiana4` x11, `NewJersey4` x11, `SouthCarolina4` x11, `Michigan4` x9, `OntarioCanada4` x8, `Connecticut4` x7, `Delaware4` x7, `NorthCarolina4` x6

## 4. Priority Examples

- `2026-01-16` `Connecticut4` `Evening` winner=`431` rank=`1` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`LIGHT_ARENA_FINALIST` double=`-`
- `2026-01-16` `Delaware4` `Evening` winner=`107` rank=`2` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-01-19` `Michigan4` `Evening` winner=`402` rank=`5` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`` double=`-`
- `2026-01-16` `NewJersey4` `Evening` winner=`180` rank=`6` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-01-18` `NewJersey4` `Evening` winner=`955` rank=`6` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-21` `NewYork4` `Evening` winner=`233` rank=`7` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-21` `NorthCarolina4` `Evening` winner=`577` rank=`8` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`WEAK`
- `2026-01-15` `NorthCarolina4` `Midday` winner=`045` rank=`8` cohort=`BOX_GAP` frontier=`FEEDER_TO_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`

## 5. Practical Read

- Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
- Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
- Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
- Current window produced `11` explicit box-gap rows worth preserving for translator study.
- Preserved-not-budgeted rows (`1`) remain useful as a reserve cohort for later combo/budget design.
