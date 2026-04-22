# Analysis Arena Translator-Learning Ledger

## 1. Scope

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09`
- Dates: `2025-12-30` to `2026-01-09`
- Winner-event denominator: `301`
- Translator-learning rows: `129`
- CSV roster: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.csv`

## 2. Cohort Counts

- VT_FINALIST: `109`
- VT_CONVERTED: `46`
- BOX_FINALIST: `24`
- ARENA_EXPLICIT: `22`
- BOX_GAP: `12`
- BOX_CONVERTED: `10`
- EXACT_CONVERTED: `4`
- PRESERVED: `3`

## 3. Signature Mix

- Arena finalist signatures: `PARTIAL_ARENA_FINALIST` x57, `LIGHT_ARENA_FINALIST` x48, `UNSPECIFIED` x17, `CONTROL_ARM_ONLY_CATCH` x4, `CLEAR_ARENA_FINALIST` x3
- Frontier signatures: `HIDDEN_COMPRESSED_FRONTIER` x55, `VTRAC_FRONTIER` x30, `FEEDER_TO_FRONTIER` x29, `FAMILY_FRONTIER` x14, `LITERAL_FRONTIER` x1
- Top states in the teaching cohort: `Connecticut4` x12, `SouthCarolina4` x12, `Ohio4` x11, `Virginia4` x11, `Florida4` x10, `Indiana4` x10, `NewJersey4` x10, `Pennsylvania4` x9

## 4. Priority Examples

- `2026-01-05` `Connecticut4` `Midday` winner=`071` rank=`1` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`` double=`-`
- `2026-01-07` `Florida4` `Evening` winner=`963` rank=`3` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`
- `2025-12-31` `NewYork4` `Evening` winner=`116` rank=`7` cohort=`BOX_GAP` frontier=`FEEDER_TO_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-01` `NorthCarolina4` `Evening` winner=`053` rank=`8` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`
- `2026-01-02` `NorthCarolina4` `Midday` winner=`033` rank=`8` cohort=`BOX_GAP` frontier=`FEEDER_TO_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`
- `2025-12-30` `NorthCarolina4` `Midday` winner=`455` rank=`8` cohort=`BOX_GAP` frontier=`FAMILY_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`STRONG`
- `2026-01-08` `Ohio4` `Evening` winner=`580` rank=`9` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`MEDIUM`
- `2026-01-09` `Pennsylvania4` `Evening` winner=`014` rank=`11` cohort=`BOX_GAP` frontier=`HIDDEN_COMPRESSED_FRONTIER` sig=`PARTIAL_ARENA_FINALIST` double=`-`

## 5. Practical Read

- Use this ledger as the teaching cohort for future translator work, not as live scoring by itself.
- Opportunity-gap rows are the highest-value misses because they show candidate-like arena evidence without downstream conversion.
- Converted rows with arena-native support are the cleanest examples of what the rebuilt branch already expresses correctly.
- Current window produced `12` explicit box-gap rows worth preserving for translator study.
- Preserved-not-budgeted rows (`3`) remain useful as a reserve cohort for later combo/budget design.
