# Analysis Arena Predictive Run Report — Delaware4 — D=2026-03-20 (H=2026-03-19)

Purpose
- Capture the pre-results state thesis for the Analysis Arena branch from the actual predictive-day sharepack.
- Preserve Brain 1, Brain 2 carry-through, translation-sandbox seeds, and the downstream control arm in one state-local artifact.
- This is the arena-era replacement for the older predictive run shell.

Template / SSOT anchors
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- Arena operating flow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- Arena cadence quickstart: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md`
- Aggregated arena contract: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md`
- Context-tool arena feed: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- String-tool arena feed: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- Translation sandbox companion: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

Scope
- Results date `D`: `2026-03-20`
- History date `H`: `2026-03-19`
- State: `Delaware4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-20/Delaware4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-20/Delaware4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-20/Delaware4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-20/Delaware4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-20/Delaware4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-20/Delaware4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-20/Delaware4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-20/Delaware4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-20/Delaware4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-20/Delaware4/aux/Delaware4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-20/Delaware4/aux/Delaware4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-20/Delaware4/stable/Delaware4/Delaware4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-20/Delaware4/stable/Delaware4/Delaware4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-20/Delaware4/stable/Delaware4/Delaware4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-20/Delaware4/digit_reduction/Delaware4/Delaware4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-20/Delaware4/digit_reduction/Delaware4/Delaware4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-20/Delaware4/vtrac/Delaware4/Delaware4_vtrac_enhanced_20260416_191955.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-20/Delaware4/hot_zones/Delaware4/Delaware4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `001`, `099`, `399`, `599`, `559`, `0016`
- Dominant families: `559`, `5`, `099`, `2`, `9`, `6`
- Dominant VTRAC indices: `2`, `15`, `5`, `34`, `9`, `14`
- Context-reinforced canonicals: `099`, `399`, `019`, `069`, `089`, `009`
- Context-only pressure: _none_
- State regime: `dominant_canonical=001`, `dominant_family=559`, `dominant_vtrac_index=2`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=001,009,006,013,004,005`
- R-Consensus context: `events=3`, `signal_class=strong`, `trial_eligible=True`, `top_tails=93,3`, `top_support=399,099,039`
- VTRAC literal watchlist: `2->001,006,155,015`, `15->099,599,049`, `5->559,009,004,059`, `34->399,899`, `9->069,019`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=2`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `001`, `099`, `399`, `599`
- Scoreboard top VTRAC indices: `2`, `15`, `5`, `34`
- Positional shortlist top: `079`, `089`, `037`, `379`, `009`, `099`, `479`, `279`
- Blackapple recommended canonicals: `019`, `028`, `037`, `046`, `127`, `136`, `145`, `235`
- Profit-alert implied canonicals: `069`, `399`
- Due-double family pressure: `Combined:3:0/5-3/8,0/5-4/9,0/5-1/6`, `Evening:3:0/5-3/8,0/5-4/9,0/5-1/6`, `Midday:1:0/5-3/8,0/5-4/9,0/5-1/6`
- Due-double example canonicals: `033`, `088`, `355`, `558`, `009`, `559`, `455`, `599`
- Top profit alerts: `Midday:A05:399:STR8_3`, `Combined:A04:069:BOX`, `Combined:A08:OVERLAY`, `Evening:A08:OVERLAY`
- Top compound events: _none_
- Diagnostic boxed seed: `009`, `099`, `399`, `559`, `019`, `001`, `069`, `089`, `033`, `088`, `599`, `006`, `013`, `004`, `037`, `155`
- Diagnostic straight seed: `900`, `909`, `907`, `908`, `307`, `937`, `947`, `927`, `009`, `090`, `033`, `088`, `559`, `595`, `955`, `099`
- Diagnostic VT-box seed: `34`, `15`, `18`, `2`, `5`, `9`, `23`, `11`, `20`, `13`, `33`, `12`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `001`, `099`, `399`, `599`, `019`, `069`, `009`, `559`, `089`
- Arena-preserved straight canonicals to watch: `900`, `909`, `907`, `908`, `307`, `937`, `947`, `927`, `099`, `399`, `019`, `069`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=183`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
