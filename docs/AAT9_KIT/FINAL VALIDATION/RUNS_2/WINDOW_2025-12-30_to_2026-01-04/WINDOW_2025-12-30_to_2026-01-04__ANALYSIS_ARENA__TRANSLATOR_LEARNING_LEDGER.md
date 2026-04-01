# Analysis Arena Translator-Learning Ledger

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04`
- Dates: `2025-12-30` to `2026-01-04`
- Winner-event denominator: `163`
- Translator-learning rows: `70`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv`

## 2. Cohort Counts

- VT_FINALIST: `61`
- VT_CONVERTED: `25`
- BOX_FINALIST: `14`
- ARENA_EXPLICIT: `11`
- BOX_CONVERTED: `6`
- BOX_GAP: `5`
- PRESERVED: `3`
- EXACT_CONVERTED: `1`

## 3. Signature Mix

- Arena finalist signatures: `LIGHT_ARENA_FINALIST` x31, `PARTIAL_ARENA_FINALIST` x27, `UNSPECIFIED` x11, `CONTROL_ARM_ONLY_CATCH` x1
- Frontier signatures: `HIDDEN_COMPRESSED_FRONTIER` x26, `FEEDER_TO_FRONTIER` x21, `VTRAC_FRONTIER` x17, `FAMILY_FRONTIER` x6
- Top states in the teaching cohort: `Connecticut4` x8, `Indiana4` x7, `Virginia4` x7, `SouthCarolina4` x7, `Ohio4` x6, `NewJersey4` x5, `OntarioCanada4` x5, `Florida4` x4

## 4. Priority Examples

- `2025-12-31` `NewYork4` `Evening` winner=`116` rank=`7` cohort=`BOX_GAP` frontier=`FEEDER_TO_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-01` `NorthCarolina4` `Evening` winner=`053` rank=`8` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`
- `2025-12-30` `NorthCarolina4` `Midday` winner=`455` rank=`8` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`
- `2025-12-30` `Pennsylvania4` `Evening` winner=`173` rank=`11` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-01-03` `SouthCarolina4` `Midday` winner=`189` rank=`13` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2025-12-30` `Connecticut4` `Midday` winner=`095` rank=`1` cohort=`BOX_CONVERTED` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-04` `Connecticut4` `Midday` winner=`569` rank=`1` cohort=`VT_FINALIST` frontier=`VTRAC_FRONTIER` sig=`LIGHT_ARENA_FINALIST` double=`-`
- `2025-12-31` `Connecticut4` `Evening` winner=`361` rank=`1` cohort=`VT_CONVERTED` frontier=`VTRAC_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`

## 5. Practical Read

- Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
- Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
- Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
- Current window produced `5` explicit box-gap rows worth preserving for translator study.
- Preserved-not-budgeted rows (`3`) remain useful as a reserve cohort for later combo/budget design.
