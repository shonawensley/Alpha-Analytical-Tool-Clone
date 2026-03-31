# Analysis Arena Window Performance / Opportunity Gap Report

## 1. Window Metadata

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09`
- Dates: `2026-01-05` to `2026-01-09`
- Day count: `5`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-01-05_to_2026-01-09/WINDOW_2026-01-05_to_2026-01-09__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`

## 2. Arena Intrinsic Quality

- Winner events: `138`
- Winner on board: `138` (100.0%)
- Board top3 containment: `30` (21.7%)
- Board top5 containment: `50` (36.2%)
- Top primary target hits: `10` (7.2%)
- Best clean host hits: `10` (7.2%)
- Arena box signal present: `10` (7.2%)
- Arena exact signal present: `3` (2.2%)
- Arena VTRAC signal present: `31` (22.5%)

## 3. Control-Arm Realized Performance

- Candidate Universe exact: `28` (20.3%)
- Candidate Universe box: `34` (24.6%)
- Play Card any exact: `18` (13.0%)
- Play Card any box: `12` (8.7%)
- B12 box: `6` (4.3%)
- B24 box: `10` (7.2%)
- B36 box: `12` (8.7%)

## 4. Opportunity Gap

- Preserved-not-budgeted winner canonicals: `2` (1.4%)
- Arena box signal but Play Card box miss: `5` (3.6%)
- Arena exact signal but Play Card exact miss: `0` (0.0%)

## 5. Tracker / Context Attribution

- profit alert: events=`138` arena_box=`10` cu_box=`34` play_box=`12` gap_box=`5`
- compound event: events=`88` arena_box=`8` cu_box=`25` play_box=`9` gap_box=`4`
- due double: events=`138` arena_box=`10` cu_box=`34` play_box=`12` gap_box=`5`
- blackapple: events=`138` arena_box=`10` cu_box=`34` play_box=`12` gap_box=`5`
- positional: events=`138` arena_box=`10` cu_box=`34` play_box=`12` gap_box=`5`
- r consensus: events=`102` arena_box=`8` cu_box=`24` play_box=`7` gap_box=`4`
- survivor: events=`138` arena_box=`10` cu_box=`34` play_box=`12` gap_box=`5`

## 6. Translator-Learning Signals

- Diagnostic boxed seeds: `004` x43, `014` x38, `009` x37, `011` x36, `006` x35, `007` x33, `005` x31, `044` x29
- Diagnostic straight seeds: `595` x14, `808` x13, `040` x13, `004` x13, `009` x12, `900` x12, `400` x12, `088` x11
- Diagnostic VT-box seeds: `15` x55, `23` x55, `18` x54, `5` x51, `12` x39, `31` x37, `2` x35, `6` x35
- Preserved-not-budgeted canonicals: `227` x5, `024` x5, `029` x5, `116` x4, `166` x4, `048` x4, `345` x4, `067` x3

## 7. Final Promotions / Warnings

- Preserve the layered metric split: arena truth quality, control-arm realization quality, and opportunity gap should remain separate.
- Use the opportunity-gap rows as the main design feed for future translator and budgeting research.
- Keep current B12/B24/B36 outcomes in the baseline/control-arm role; do not treat them as the full measure of arena quality.
