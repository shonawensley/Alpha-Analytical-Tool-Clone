# Analysis Arena Translator-Learning Ledger

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- Dates: `2026-03-09` to `2026-03-23`
- Winner-event denominator: `414`
- Translator-learning rows: `189`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv`

## 2. Cohort Counts

- VT_FINALIST: `162`
- VT_CONVERTED: `68`
- ARENA_EXPLICIT: `40`
- BOX_FINALIST: `40`
- BOX_GAP: `21`
- BOX_CONVERTED: `17`
- EXACT_CONVERTED: `7`
- EXACT_GAP: `2`
- PRESERVED: `1`

## 3. Signature Mix

- Arena finalist signatures: `PARTIAL_ARENA_FINALIST` x102, `LIGHT_ARENA_FINALIST` x54, `UNSPECIFIED` x22, `CONTROL_ARM_ONLY_CATCH` x8, `CLEAR_ARENA_FINALIST` x3
- Frontier signatures: `HIDDEN_COMPRESSED_FRONTIER` x78, `FEEDER_TO_FRONTIER` x58, `VTRAC_FRONTIER` x35, `FAMILY_FRONTIER` x16, `LITERAL_FRONTIER` x2
- Top states in the teaching cohort: `Indiana4` x17, `Michigan4` x16, `NorthCarolina4` x15, `SouthCarolina4` x15, `Delaware4` x14, `OntarioCanada4` x14, `PuertoRico4` x14, `Florida4` x13

## 4. Priority Examples

- `2026-03-09` `Connecticut4` `Evening` winner=`091` rank=`1` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-03-23` `Florida4` `Midday` winner=`196` rank=`3` cohort=`BOX_GAP` frontier=`FEEDER_TO_FRONTIER` sig=`LIGHT_ARENA_FINALIST` double=`MEDIUM`
- `2026-03-11` `Florida4` `Midday` winner=`700` rank=`3` cohort=`BOX_GAP` frontier=`VTRAC_FRONTIER` sig=`` double=`-`
- `2026-03-10` `Indiana4` `Evening` winner=`070` rank=`4` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`
- `2026-03-23` `Indiana4` `Evening` winner=`420` rank=`4` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2026-03-14` `Indiana4` `Midday` winner=`080` rank=`4` cohort=`BOX_GAP` frontier=`VTRAC_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`
- `2026-03-17` `Indiana4` `Evening` winner=`108` rank=`4` cohort=`EXACT_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`` double=`-`
- `2026-03-14` `Michigan4` `Evening` winner=`855` rank=`5` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`

## 5. Practical Read

- Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
- Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
- Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
- Current window produced `21` explicit box-gap rows worth preserving for translator study.
- Preserved-not-budgeted rows (`1`) remain useful as a reserve cohort for later combo/budget design.
