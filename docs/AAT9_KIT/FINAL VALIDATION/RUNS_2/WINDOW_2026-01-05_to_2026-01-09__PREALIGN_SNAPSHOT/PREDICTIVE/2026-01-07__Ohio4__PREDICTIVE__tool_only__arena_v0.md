# Analysis Arena Predictive Run Report — Ohio4 — D=2026-01-07 (H=2026-01-06)

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
- Results date `D`: `2026-01-07`
- History date `H`: `2026-01-06`
- State: `Ohio4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-07/Ohio4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-07/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-07/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-07/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-07/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-07/Ohio4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-07/Ohio4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-07/Ohio4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-07/Ohio4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-07/Ohio4/aux/Ohio4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-07/Ohio4/aux/Ohio4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-07/Ohio4/stable/Ohio4/Ohio4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-07/Ohio4/stable/Ohio4/Ohio4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-07/Ohio4/stable/Ohio4/Ohio4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-07/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-07/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-07/Ohio4/vtrac/Ohio4/Ohio4_vtrac_enhanced_20260326_044612.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-07/Ohio4/hot_zones/Ohio4/Ohio4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `559`, `088`, `299`, `889`, `599`, `055`
- Dominant families: `559`, `599`, `5`, `12`, `13`, `4`
- Dominant VTRAC indices: `5`, `13`, `1`, `31`, `33`, `10`
- Context-reinforced canonicals: `559`, `299`, `889`, `788`, `899`, `089`
- Context-only pressure: _none_
- State regime: `dominant_canonical=559`, `dominant_family=559`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=005,009,006,007,008,002`
- R-Consensus context: `events=1`, `signal_class=moderate`, `trial_eligible=True`, `top_tails=22`, `top_support=022`
- VTRAC literal watchlist: `5->559,009,059`, `13->088,588,038,358`, `1->055,005`, `31->299,249`, `33->889,339`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=9`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `559`, `088`, `299`, `889`
- Scoreboard top VTRAC indices: `5`, `13`, `1`, `31`
- Positional shortlist top: `289`, `889`, `288`, `299`, `888`, `789`, `899`
- Blackapple recommended canonicals: `013`, `023`, `034`, `123`, `134`, `234`, `568`, `578`
- Profit-alert implied canonicals: `089`, `559`
- Due-double family pressure: `Combined:2:1/6-3/8,1/6-4/9,0/5-1/6`, `Evening:1:1/6-3/8,1/6-4/9,0/5-1/6`, `Midday:4:1/6-3/8,1/6-4/9,0/5-1/6`
- Due-double example canonicals: `668`, `118`, `113`, `688`, `188`, `466`, `669`, `446`
- Top profit alerts: `Evening:A05:559:STR8_3`, `Combined:A04:089:BOX`, `Combined:A08:OVERLAY`, `Midday:A08:OVERLAY`
- Top compound events: _none_
- Diagnostic boxed seed: `559`, `889`, `009`, `088`, `299`, `059`, `089`, `899`, `005`, `006`, `007`, `788`, `008`, `004`, `022`, `599`
- Diagnostic straight seed: `889`, `899`, `829`, `828`, `929`, `888`, `879`, `989`, `009`, `090`, `900`, `559`, `595`, `955`, `088`, `808`
- Diagnostic VT-box seed: `5`, `1`, `12`, `15`, `3`, `10`, `13`, `31`, `33`, `14`, `8`, `11`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=198`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
