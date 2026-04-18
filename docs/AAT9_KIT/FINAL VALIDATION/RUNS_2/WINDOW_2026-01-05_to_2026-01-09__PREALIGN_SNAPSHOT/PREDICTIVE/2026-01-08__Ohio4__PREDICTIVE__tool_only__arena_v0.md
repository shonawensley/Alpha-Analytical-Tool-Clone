# Analysis Arena Predictive Run Report — Ohio4 — D=2026-01-08 (H=2026-01-07)

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
- Results date `D`: `2026-01-08`
- History date `H`: `2026-01-07`
- State: `Ohio4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-08/Ohio4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-08/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-08/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-08/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-08/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-08/Ohio4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-08/Ohio4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-08/Ohio4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-08/Ohio4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-08/Ohio4/aux/Ohio4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-08/Ohio4/aux/Ohio4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-08/Ohio4/stable/Ohio4/Ohio4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-08/Ohio4/stable/Ohio4/Ohio4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-08/Ohio4/stable/Ohio4/Ohio4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-08/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-08/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-08/Ohio4/vtrac/Ohio4/Ohio4_vtrac_enhanced_20260326_045041.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-08/Ohio4/hot_zones/Ohio4/Ohio4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `889`, `559`, `599`, `299`, `788`, `899`
- Dominant families: `559`, `599`, `12`, `13`, `5`, `3`
- Dominant VTRAC indices: `33`, `5`, `15`, `13`, `14`, `31`
- Context-reinforced canonicals: `889`, `299`, `788`, `899`, `688`
- Context-only pressure: `699`
- State regime: `dominant_canonical=889`, `dominant_family=559`, `dominant_vtrac_index=33`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=005,009,007,006,008,002`
- R-Consensus context: `events=1`, `signal_class=moderate`, `trial_eligible=True`, `top_tails=22`, `top_support=022`
- VTRAC literal watchlist: `33->889,389,348`, `5->559`, `15->599,099`, `13->088,588,038,335`, `14->359,089,039,589`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=9`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `889`, `559`, `599`, `299`
- Scoreboard top VTRAC indices: `33`, `5`, `15`, `13`
- Positional shortlist top: `289`, `889`, `288`, `299`, `888`, `789`, `899`
- Blackapple recommended canonicals: `589`, `679`, `013`, `049`, `058`, `139`, `148`, `157`
- Profit-alert implied canonicals: `359`, `889`
- Due-double family pressure: `Combined:1:1/6-3/8,1/6-4/9,0/5-1/6`, `Evening:2:1/6-3/8,1/6-4/9,0/5-1/6`, `Midday:0:1/6-3/8,1/6-4/9,0/5-1/6`
- Due-double example canonicals: `668`, `118`, `113`, `688`, `188`, `466`, `669`, `446`
- Top profit alerts: `Combined:A04:359:BOX`, `Evening:A05:889:STR8_3`, `Combined:A08:OVERLAY`, `Midday:A08:OVERLAY`
- Top compound events: _none_
- Diagnostic boxed seed: `889`, `899`, `009`, `559`, `299`, `788`, `389`, `005`, `007`, `006`, `359`, `688`, `008`, `004`, `022`, `058`
- Diagnostic straight seed: `889`, `989`, `899`, `829`, `828`, `929`, `888`, `879`, `009`, `090`, `900`, `559`, `595`, `955`, `898`, `988`
- Diagnostic VT-box seed: `33`, `15`, `5`, `14`, `12`, `3`, `29`, `13`, `31`, `34`, `25`, `22`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=201`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
