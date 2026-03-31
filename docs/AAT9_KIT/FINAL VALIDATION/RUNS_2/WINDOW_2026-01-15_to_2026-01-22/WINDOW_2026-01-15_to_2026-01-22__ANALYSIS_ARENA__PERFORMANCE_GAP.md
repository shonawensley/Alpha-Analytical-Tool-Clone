# Analysis Arena Window Performance / Opportunity Gap Report

## 1. Window Metadata

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22`
- Dates: `2026-01-15` to `2026-01-22`
- Day count: `8`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-22/WINDOW_2026-01-15_to_2026-01-22__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`

## 2. Arena Intrinsic Quality

- Winner events: `221`
- Winner on board: `221` (100.0%)
- Board top3 containment: `48` (21.7%)
- Board top5 containment: `80` (36.2%)
- Top primary target hits: `16` (7.2%)
- Best clean host hits: `16` (7.2%)
- Arena box signal present: `19` (8.6%)
- Arena exact signal present: `2` (0.9%)
- Arena VTRAC signal present: `62` (28.1%)

## 3. Control-Arm Realized Performance

- Candidate Universe exact: `34` (15.4%)
- Candidate Universe box: `51` (23.1%)
- Play Card any exact: `30` (13.6%)
- Play Card any box: `12` (5.4%)
- B12 box: `3` (1.4%)
- B24 box: `9` (4.1%)
- B36 box: `12` (5.4%)

## 4. Opportunity Gap

- Preserved-not-budgeted winner canonicals: `1` (0.5%)
- Arena box signal but Play Card box miss: `11` (5.0%)
- Arena exact signal but Play Card exact miss: `0` (0.0%)

## 5. Tracker / Context Attribution

- profit alert: events=`221` arena_box=`19` cu_box=`51` play_box=`12` gap_box=`11`
- compound event: events=`134` arena_box=`17` cu_box=`34` play_box=`9` gap_box=`10`
- due double: events=`221` arena_box=`19` cu_box=`51` play_box=`12` gap_box=`11`
- blackapple: events=`221` arena_box=`19` cu_box=`51` play_box=`12` gap_box=`11`
- positional: events=`221` arena_box=`19` cu_box=`51` play_box=`12` gap_box=`11`
- r consensus: events=`170` arena_box=`15` cu_box=`39` play_box=`9` gap_box=`8`
- survivor: events=`221` arena_box=`19` cu_box=`51` play_box=`12` gap_box=`11`

## 6. Translator-Learning Signals

- Diagnostic boxed seeds: `001` x69, `004` x63, `009` x61, `006` x59, `007` x57, `005` x49, `014` x48, `011` x44
- Diagnostic straight seeds: `040` x27, `004` x26, `009` x23, `400` x23, `090` x22, `100` x22, `900` x21, `001` x21
- Diagnostic VT-box seeds: `23` x102, `5` x87, `15` x85, `12` x80, `18` x70, `33` x65, `2` x63, `3` x61
- Preserved-not-budgeted canonicals: `017` x17, `028` x14, `012` x12, `026` x9, `245` x8, `023` x7, `019` x6, `037` x5

## 7. Final Promotions / Warnings

- Preserve the layered metric split: arena truth quality, control-arm realization quality, and opportunity gap should remain separate.
- Use the opportunity-gap rows as the main design feed for future translator and budgeting research.
- Keep current B12/B24/B36 outcomes in the baseline/control-arm role; do not treat them as the full measure of arena quality.
