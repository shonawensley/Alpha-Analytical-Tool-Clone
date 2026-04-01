# Analysis Arena Translator-Learning Ledger

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09`
- Dates: `2026-01-05` to `2026-01-09`
- Winner-event denominator: `138`
- Translator-learning rows: `57`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv`

## 2. Cohort Counts

- VT_FINALIST: `48`
- VT_CONVERTED: `22`
- BOX_FINALIST: `11`
- ARENA_EXPLICIT: `10`
- BOX_GAP: `5`
- BOX_CONVERTED: `5`
- EXACT_CONVERTED: `3`
- PRESERVED: `2`

## 3. Signature Mix

- Arena finalist signatures: `PARTIAL_ARENA_FINALIST` x26, `LIGHT_ARENA_FINALIST` x20, `UNSPECIFIED` x6, `CLEAR_ARENA_FINALIST` x3, `CONTROL_ARM_ONLY_CATCH` x2
- Frontier signatures: `HIDDEN_COMPRESSED_FRONTIER` x27, `VTRAC_FRONTIER` x13, `FEEDER_TO_FRONTIER` x9, `FAMILY_FRONTIER` x7, `LITERAL_FRONTIER` x1
- Top states in the teaching cohort: `Florida4` x6, `PuertoRico4` x6, `Ohio4` x5, `SouthCarolina4` x5, `NewJersey4` x5, `Connecticut4` x4, `NewYork4` x4, `Pennsylvania4` x4

## 4. Priority Examples

- `2026-01-05` `Connecticut4` `Midday` winner=`071` rank=`1` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`` double=`-`
- `2026-01-07` `Florida4` `Evening` winner=`963` rank=`3` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-01-08` `Ohio4` `Evening` winner=`580` rank=`9` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-09` `Pennsylvania4` `Evening` winner=`014` rank=`11` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-01-09` `Pennsylvania4` `Midday` winner=`811` rank=`11` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` sig=`CLEAR_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-09` `Connecticut4` `Midday` winner=`234` rank=`1` cohort=`VT_FINALIST` frontier=`FAMILY_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-01-08` `Connecticut4` `Evening` winner=`331` rank=`1` cohort=`VT_CONVERTED` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`LIGHT_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-06` `Connecticut4` `Midday` winner=`576` rank=`1` cohort=`VT_CONVERTED` frontier=`FEEDER_TO_FRONTIER` sig=`LIGHT_ARENA_FINALIST` double=`-`

## 5. Practical Read

- Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
- Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
- Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
- Current window produced `5` explicit box-gap rows worth preserving for translator study.
- Preserved-not-budgeted rows (`2`) remain useful as a reserve cohort for later combo/budget design.
