# Analysis Arena Window Performance / Opportunity Gap Report

## 1. Window Metadata

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04`
- Dates: `2025-12-30` to `2026-01-04`
- Day count: `6`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2025-12-30_to_2026-01-04/WINDOW_2025-12-30_to_2026-01-04__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`

## 2. Arena Intrinsic Quality

- Winner events: `163`
- Winner on board: `163` (100.0%)
- Board top3 containment: `36` (22.1%)
- Board top5 containment: `60` (36.8%)
- Top primary target hits: `12` (7.4%)
- Best clean host hits: `12` (7.4%)
- Arena box signal present: `11` (6.7%)
- Arena exact signal present: `1` (0.6%)
- Arena VTRAC signal present: `37` (22.7%)

## 3. Control-Arm Realized Performance

- Candidate Universe exact: `25` (15.3%)
- Candidate Universe box: `37` (22.7%)
- Play Card any exact: `20` (12.3%)
- Play Card any box: `10` (6.1%)
- B12 box: `2` (1.2%)
- B24 box: `5` (3.1%)
- B36 box: `10` (6.1%)

## 4. Opportunity Gap

- Preserved-not-budgeted winner canonicals: `3` (1.8%)
- Arena box signal but Play Card box miss: `5` (3.1%)
- Arena exact signal but Play Card exact miss: `0` (0.0%)

## 5. Tracker / Context Attribution

- profit alert: events=`163` arena_box=`11` cu_box=`37` play_box=`10` gap_box=`5`
- compound event: events=`97` arena_box=`6` cu_box=`22` play_box=`5` gap_box=`4`
- due double: events=`163` arena_box=`11` cu_box=`37` play_box=`10` gap_box=`5`
- blackapple: events=`163` arena_box=`11` cu_box=`37` play_box=`10` gap_box=`5`
- positional: events=`163` arena_box=`11` cu_box=`37` play_box=`10` gap_box=`5`
- r consensus: events=`125` arena_box=`10` cu_box=`30` play_box=`8` gap_box=`5`
- survivor: events=`163` arena_box=`11` cu_box=`37` play_box=`10` gap_box=`5`

## 6. Translator-Learning Signals

- Diagnostic boxed seeds: `011` x49, `017` x48, `006` x40, `004` x38, `014` x36, `001` x34, `007` x33, `009` x32
- Diagnostic straight seeds: `040` x21, `004` x19, `400` x18, `900` x16, `009` x16, `090` x16, `066` x14, `202` x14
- Diagnostic VT-box seeds: `23` x69, `18` x67, `15` x55, `12` x50, `5` x43, `7` x42, `9` x40, `2` x39
- Preserved-not-budgeted canonicals: `024` x7, `245` x7, `026` x7, `029` x6, `067` x6, `078` x5, `079` x5, `012` x5

## 7. Final Promotions / Warnings

- Preserve the layered metric split: arena truth quality, control-arm realization quality, and opportunity gap should remain separate.
- Use the opportunity-gap rows as the main design feed for future translator and budgeting research.
- Keep current B12/B24/B36 outcomes in the baseline/control-arm role; do not treat them as the full measure of arena quality.
