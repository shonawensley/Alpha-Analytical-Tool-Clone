# Analysis Arena Window Performance / Opportunity Gap Report

## 1. Window Metadata

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18`
- Dates: `2026-01-15` to `2026-01-18`
- Day count: `4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-15_to_2026-01-18/WINDOW_2026-01-15_to_2026-01-18__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`

## 2. Arena Intrinsic Quality

- Winner events: `109`
- Winner on board: `109` (100.0%)
- Board top3 containment: `24` (22.0%)
- Board top5 containment: `40` (36.7%)
- Top primary target hits: `8` (7.3%)
- Best clean host hits: `8` (7.3%)
- Arena box signal present: `12` (11.0%)
- Arena exact signal present: `3` (2.8%)
- Arena VTRAC signal present: `33` (30.3%)

## 3. Control-Arm Realized Performance

- Candidate Universe exact: `26` (23.9%)
- Candidate Universe box: `33` (30.3%)
- Play Card any exact: `16` (14.7%)
- Play Card any box: `11` (10.1%)
- B12 box: `2` (1.8%)
- B24 box: `8` (7.3%)
- B36 box: `10` (9.2%)

## 4. Opportunity Gap

- Preserved-not-budgeted winner canonicals: `0` (0.0%)
- Arena box signal but Play Card box miss: `4` (3.7%)
- Arena exact signal but Play Card exact miss: `0` (0.0%)

## 5. Tracker / Context Attribution

- profit alert: events=`109` arena_box=`12` cu_box=`33` play_box=`11` gap_box=`4`
- compound event: events=`70` arena_box=`10` cu_box=`25` play_box=`9` gap_box=`3`
- due double: events=`109` arena_box=`12` cu_box=`33` play_box=`11` gap_box=`4`
- blackapple: events=`109` arena_box=`12` cu_box=`33` play_box=`11` gap_box=`4`
- positional: events=`109` arena_box=`12` cu_box=`33` play_box=`11` gap_box=`4`
- r consensus: events=`78` arena_box=`9` cu_box=`25` play_box=`9` gap_box=`2`
- survivor: events=`109` arena_box=`12` cu_box=`33` play_box=`11` gap_box=`4`

## 6. Translator-Learning Signals

- Diagnostic boxed seeds: `001` x32, `004` x31, `009` x30, `014` x28, `006` x27, `007` x24, `013` x22, `005` x22
- Diagnostic straight seeds: `040` x13, `004` x13, `400` x12, `090` x10, `009` x10, `900` x9, `100` x9, `101` x8
- Diagnostic VT-box seeds: `23` x52, `15` x46, `5` x42, `33` x38, `12` x36, `18` x35, `2` x32, `9` x30
- Preserved-not-budgeted canonicals: `028` x8, `036` x5, `244` x4, `449` x3, `029` x3, `079` x3, `037` x2, `227` x2

## 7. Final Promotions / Warnings

- Preserve the layered metric split: arena truth quality, control-arm realization quality, and opportunity gap should remain separate.
- Use the opportunity-gap rows as the main design feed for future translator and budgeting research.
- Keep current B12/B24/B36 outcomes in the baseline/control-arm role; do not treat them as the full measure of arena quality.
