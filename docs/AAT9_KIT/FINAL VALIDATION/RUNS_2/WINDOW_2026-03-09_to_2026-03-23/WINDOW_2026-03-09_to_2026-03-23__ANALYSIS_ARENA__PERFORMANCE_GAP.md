# Analysis Arena Window Performance / Opportunity Gap Report

## 1. Window Metadata

- Window root: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23`
- Dates: `2026-03-09` to `2026-03-23`
- Day count: `15`
- Profile: `tool_only`
- Experiment tag: `arena_v0`
- Ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__PERFORMANCE_GAP__ledger.csv`

## 2. Arena Intrinsic Quality

- Winner events: `414`
- Winner on board: `414` (100.0%)
- Board top3 containment: `90` (21.7%)
- Board top5 containment: `150` (36.2%)
- Top primary target hits: `30` (7.2%)
- Best clean host hits: `30` (7.2%)
- Arena box signal present: `35` (8.5%)
- Arena exact signal present: `9` (2.2%)
- Arena VTRAC signal present: `116` (28.0%)

## 3. Control-Arm Realized Performance

- Candidate Universe exact: `80` (19.3%)
- Candidate Universe box: `97` (23.4%)
- Play Card any exact: `54` (13.0%)
- Play Card any box: `29` (7.0%)
- B12 box: `9` (2.2%)
- B24 box: `21` (5.1%)
- B36 box: `29` (7.0%)

## 4. Opportunity Gap

- Preserved-not-budgeted winner canonicals: `1` (0.2%)
- Arena box signal but Play Card box miss: `21` (5.1%)
- Arena exact signal but Play Card exact miss: `2` (0.5%)

## 5. Tracker / Context Attribution

- profit alert: events=`414` arena_box=`35` cu_box=`97` play_box=`29` gap_box=`21`
- compound event: events=`268` arena_box=`21` cu_box=`62` play_box=`18` gap_box=`10`
- due double: events=`414` arena_box=`35` cu_box=`97` play_box=`29` gap_box=`21`
- blackapple: events=`414` arena_box=`35` cu_box=`97` play_box=`29` gap_box=`21`
- positional: events=`414` arena_box=`35` cu_box=`97` play_box=`29` gap_box=`21`
- r consensus: events=`352` arena_box=`30` cu_box=`81` play_box=`26` gap_box=`17`
- survivor: events=`414` arena_box=`35` cu_box=`97` play_box=`29` gap_box=`21`

## 6. Translator-Learning Signals

- Diagnostic boxed seeds: `004` x132, `009` x124, `559` x104, `005` x98, `001` x96, `007` x94, `006` x93, `011` x93
- Diagnostic straight seeds: `090` x53, `009` x50, `900` x47, `040` x40, `004` x40, `400` x37, `070` x34, `700` x33
- Diagnostic VT-box seeds: `23` x191, `18` x169, `15` x167, `5` x148, `12` x121, `2` x95, `31` x91, `28` x88
- Preserved-not-budgeted canonicals: `449` x17, `499` x14, `029` x8, `159` x8, `227` x8, `468` x7, `039` x7, `157` x6

## 7. Final Promotions / Warnings

- Preserve the layered metric split: arena truth quality, control-arm realization quality, and opportunity gap should remain separate.
- Use the opportunity-gap rows as the main design feed for future translator and budgeting research.
- Keep current B12/B24/B36 outcomes in the baseline/control-arm role; do not treat them as the full measure of arena quality.
