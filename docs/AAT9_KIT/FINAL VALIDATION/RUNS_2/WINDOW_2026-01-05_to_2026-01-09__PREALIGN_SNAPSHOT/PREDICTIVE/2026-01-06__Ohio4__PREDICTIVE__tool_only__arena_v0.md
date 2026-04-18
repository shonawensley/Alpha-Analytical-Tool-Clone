# Analysis Arena Predictive Run Report — Ohio4 — D=2026-01-06 (H=2026-01-05)

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
- Results date `D`: `2026-01-06`
- History date `H`: `2026-01-05`
- State: `Ohio4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-06/Ohio4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-06/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-06/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-06/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-06/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-06/Ohio4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-06/Ohio4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-06/Ohio4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-06/Ohio4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-06/Ohio4/aux/Ohio4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-06/Ohio4/aux/Ohio4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-06/Ohio4/stable/Ohio4/Ohio4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-06/Ohio4/stable/Ohio4/Ohio4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-06/Ohio4/stable/Ohio4/Ohio4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-06/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-06/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-06/Ohio4/vtrac/Ohio4/Ohio4_vtrac_enhanced_20260326_044141.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-06/Ohio4/hot_zones/Ohio4/Ohio4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `088`, `008`, `559`, `0088`, `009`, `229`
- Dominant families: `559`, `5`, `3`, `255`, `13`, `4`
- Dominant VTRAC indices: `5`, `13`, `10`, `12`, `4`, `28`
- Context-reinforced canonicals: `088`, `008`, `559`, `009`, `229`, `029`
- Context-only pressure: _none_
- State regime: `dominant_canonical=088`, `dominant_family=559`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=005,009,006,008,007,002`
- R-Consensus context: `events=1`, `signal_class=moderate`, `trial_eligible=True`, `top_tails=22`, `top_support=022`
- VTRAC literal watchlist: `5->009,559,059`, `13->088,588`, `10->022,225,027`, `12->029,259,024,079,047`, `4->008,035`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=9`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `088`, `008`, `559`, `009`
- Scoreboard top VTRAC indices: `5`, `13`, `10`, `12`
- Positional shortlist top: `002`, `007`, `009`, `008`, `006`, `005`, `025`, `029`
- Blackapple recommended canonicals: `012`, `013`, `014`, `015`, `016`, `017`, `018`, `019`
- Profit-alert implied canonicals: `059`, `229`, `033`, `038`, `088`
- Due-double family pressure: `Combined:0:1/6-3/8,1/6-4/9,0/5-4/9`, `Evening:0:1/6-3/8,1/6-4/9,0/5-4/9`, `Midday:3:1/6-3/8,1/6-4/9,0/5-4/9`
- Due-double example canonicals: `668`, `118`, `113`, `688`, `188`, `466`, `669`, `446`
- Top profit alerts: `Midday:A05:229:STR8_3`, `Midday:A08:OVERLAY`, `Combined:A04:059:BOX`, `Evening:A12:088:STR8_4of8`
- Top compound events: `Evening:CLAMP_4:P25`
- Diagnostic boxed seed: `009`, `005`, `008`, `559`, `007`, `002`, `088`, `229`, `022`, `006`, `029`, `025`, `059`, `299`, `588`, `224`
- Diagnostic straight seed: `020`, `070`, `090`, `050`, `025`, `080`, `060`, `029`, `009`, `900`, `002`, `200`, `559`, `595`, `955`, `005`
- Diagnostic VT-box seed: `5`, `10`, `13`, `12`, `3`, `15`, `1`, `28`, `4`, `31`, `7`, `8`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=172`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
