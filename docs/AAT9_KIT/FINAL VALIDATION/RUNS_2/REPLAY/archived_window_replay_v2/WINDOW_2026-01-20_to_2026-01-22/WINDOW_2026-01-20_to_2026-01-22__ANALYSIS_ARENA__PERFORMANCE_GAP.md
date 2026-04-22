# Analysis Arena Window Performance / Opportunity Gap Report

## 1. Window Metadata

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22`
- Dates: `2026-01-20` to `2026-01-22`
- Day count: `3`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/REPLAY/archived_window_replay_v2/WINDOW_2026-01-20_to_2026-01-22/WINDOW_2026-01-20_to_2026-01-22__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`

## 2. Arena Intrinsic Quality

- Winner events: `84`
- Winner on board: `84` (100.0%)
- Board top3 containment: `18` (21.4%)
- Board top5 containment: `30` (35.7%)
- Top primary target hits: `6` (7.1%)
- Best clean host hits: `6` (7.1%)
- Arena box signal present: `4` (4.8%)
- Arena exact signal present: `1` (1.2%)
- Arena VTRAC signal present: `24` (28.6%)

## 3. Control-Arm Realized Performance

- Candidate Universe exact: `14` (16.7%)
- Candidate Universe box: `20` (23.8%)
- Play Card any exact: `13` (15.5%)
- Play Card any box: `5` (6.0%)
- B12 box: `2` (2.4%)
- B24 box: `4` (4.8%)
- B36 box: `5` (6.0%)

## 4. Opportunity Gap

- Preserved-not-budgeted winner canonicals: `0` (0.0%)
- Arena box signal but Play Card box miss: `2` (2.4%)
- Arena exact signal but Play Card exact miss: `0` (0.0%)

## 5. Tracker / Context Attribution

- profit alert: events=`84` arena_box=`4` cu_box=`20` play_box=`5` gap_box=`2`
- compound event: events=`44` arena_box=`4` cu_box=`8` play_box=`3` gap_box=`2`
- due double: events=`84` arena_box=`4` cu_box=`20` play_box=`5` gap_box=`2`
- blackapple: events=`84` arena_box=`4` cu_box=`20` play_box=`5` gap_box=`2`
- positional: events=`84` arena_box=`4` cu_box=`20` play_box=`5` gap_box=`2`
- r consensus: events=`68` arena_box=`3` cu_box=`15` play_box=`3` gap_box=`2`
- survivor: events=`84` arena_box=`4` cu_box=`20` play_box=`5` gap_box=`2`

## 6. Translator-Learning Signals

- Diagnostic boxed seeds: `001` x28, `004` x24, `006` x23, `007` x23, `009` x23, `005` x21, `011` x19, `559` x18
- Diagnostic straight seeds: `040` x10, `090` x9, `009` x9, `001` x9, `004` x9, `010` x7, `900` x6, `007` x6
- Diagnostic VT-box seeds: `23` x37, `5` x35, `12` x33, `15` x29, `18` x27, `3` x26, `2` x24, `8` x21
- Preserved-not-budgeted canonicals: `028` x5, `017` x2, `227` x2, `079` x2, `039` x2, `147` x2, `245` x2, `455` x1

## 7. Final Promotions / Warnings

- Preserve the layered metric split: arena truth quality, control-arm realization quality, and opportunity gap should remain separate.
- Use the opportunity-gap rows as the main design feed for future translator and budgeting research.
- Keep current B12/B24/B36 outcomes in the baseline/control-arm role; do not treat them as the full measure of arena quality.
