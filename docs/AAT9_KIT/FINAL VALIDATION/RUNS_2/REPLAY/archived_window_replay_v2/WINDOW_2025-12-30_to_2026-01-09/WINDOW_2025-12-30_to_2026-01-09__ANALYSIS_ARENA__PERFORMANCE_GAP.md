# Analysis Arena Window Performance / Opportunity Gap Report

## 1. Window Metadata

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09`
- Dates: `2025-12-30` to `2026-01-09`
- Day count: `11`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2025-12-30_to_2026-01-09/WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`

## 2. Arena Intrinsic Quality

- Winner events: `301`
- Winner on board: `301` (100.0%)
- Board top3 containment: `66` (21.9%)
- Board top5 containment: `110` (36.5%)
- Top primary target hits: `22` (7.3%)
- Best clean host hits: `22` (7.3%)
- Arena box signal present: `22` (7.3%)
- Arena exact signal present: `4` (1.3%)
- Arena VTRAC signal present: `68` (22.6%)

## 3. Control-Arm Realized Performance

- Candidate Universe exact: `57` (18.9%)
- Candidate Universe box: `73` (24.3%)
- Play Card any exact: `39` (13.0%)
- Play Card any box: `21` (7.0%)
- B12 box: `8` (2.7%)
- B24 box: `15` (5.0%)
- B36 box: `20` (6.6%)

## 4. Opportunity Gap

- Preserved-not-budgeted winner canonicals: `3` (1.0%)
- Arena box signal but Play Card box miss: `12` (4.0%)
- Arena exact signal but Play Card exact miss: `0` (0.0%)

## 5. Tracker / Context Attribution

- profit alert: events=`301` arena_box=`22` cu_box=`73` play_box=`21` gap_box=`12`
- compound event: events=`185` arena_box=`14` cu_box=`50` play_box=`15` gap_box=`8`
- due double: events=`301` arena_box=`22` cu_box=`73` play_box=`21` gap_box=`12`
- blackapple: events=`301` arena_box=`22` cu_box=`73` play_box=`21` gap_box=`12`
- positional: events=`301` arena_box=`22` cu_box=`73` play_box=`21` gap_box=`12`
- r consensus: events=`227` arena_box=`19` cu_box=`56` play_box=`14` gap_box=`11`
- survivor: events=`301` arena_box=`22` cu_box=`73` play_box=`21` gap_box=`12`

## 6. Translator-Learning Signals

- Diagnostic boxed seeds: `011` x84, `004` x81, `006` x74, `014` x74, `017` x71, `009` x70, `007` x65, `001` x63
- Diagnostic straight seeds: `040` x32, `004` x31, `009` x29, `900` x28, `090` x27, `400` x27, `010` x25, `202` x24
- Diagnostic VT-box seeds: `23` x124, `18` x121, `15` x110, `5` x94, `12` x89, `2` x74, `31` x71, `9` x68
- Preserved-not-budgeted canonicals: `024` x9, `026` x7, `166` x7, `227` x7, `067` x7, `029` x6, `005` x6, `245` x5

## 7. Final Promotions / Warnings

- Preserve the layered metric split: arena truth quality, control-arm realization quality, and opportunity gap should remain separate.
- Use the opportunity-gap rows as the main design feed for future translator and budgeting research.
- Keep current B12/B24/B36 outcomes in the baseline/control-arm role; do not treat them as the full measure of arena quality.
