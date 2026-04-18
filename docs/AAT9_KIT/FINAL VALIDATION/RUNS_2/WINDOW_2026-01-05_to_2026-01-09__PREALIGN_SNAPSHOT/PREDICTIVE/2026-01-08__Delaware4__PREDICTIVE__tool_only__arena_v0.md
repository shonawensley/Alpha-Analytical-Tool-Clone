# Analysis Arena Predictive Run Report — Delaware4 — D=2026-01-08 (H=2026-01-07)

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
- State: `Delaware4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-08/Delaware4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-08/Delaware4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-08/Delaware4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-08/Delaware4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-08/Delaware4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-08/Delaware4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-08/Delaware4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-08/Delaware4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-08/Delaware4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-08/Delaware4/aux/Delaware4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-08/Delaware4/aux/Delaware4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-08/Delaware4/stable/Delaware4/Delaware4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-08/Delaware4/stable/Delaware4/Delaware4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-08/Delaware4/stable/Delaware4/Delaware4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-08/Delaware4/digit_reduction/Delaware4/Delaware4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-08/Delaware4/digit_reduction/Delaware4/Delaware4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-08/Delaware4/vtrac/Delaware4/Delaware4_vtrac_enhanced_20260326_045013.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-08/Delaware4/hot_zones/Delaware4/Delaware4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `033`, `334`, `003`, `044`, `011`, `344`
- Dominant families: `044`, `24`, `299`, `13.0`, `15`, `33`
- Dominant VTRAC indices: `13`, `15`, `33`, `4`, `31`, `34`
- Context-reinforced canonicals: `033`, `034`, `118`, `014`, `229`, `144`
- Context-only pressure: _none_
- State regime: `dominant_canonical=033`, `dominant_family=044`, `dominant_vtrac_index=13`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=011,014,004,015,044,009`
- R-Consensus context: `events=13`, `signal_class=strong`, `trial_eligible=True`, `top_tails=33,03,3`, `top_support=033,003,334,344,034,044`
- VTRAC literal watchlist: `13->033,038`, `15->044,049,459,599`, `33->334,339,389`, `4->003,035,355,008`, `31->244,299,249,447`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=2`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `033`, `334`, `003`, `044`
- Scoreboard top VTRAC indices: `13`, `15`, `33`, `4`
- Positional shortlist top: `118`, `148`, `018`, `048`, `111`, `138`, `144`
- Blackapple recommended canonicals: `016`, `025`, `034`, `079`, `124`, `169`, `259`, `349`
- Profit-alert implied canonicals: `033`, `034`, `011`, `016`, `066`, `115`, `156`, `566`
- Due-double family pressure: `Combined:0:2/7-3/8,0/5-4/9,0/5-1/6`, `Evening:0:2/7-3/8,0/5-4/9,0/5-1/6`, `Midday:4:2/7-3/8,0/5-4/9,0/5-1/6`
- Due-double example canonicals: `223`, `778`, `288`, `228`, `377`, `009`, `455`, `004`
- Top profit alerts: `Midday:A09:STR8_8`, `Midday:A05:033:STR8_3`, `Combined:A04:034:BOX`, `Midday:A02:033:STR8_3`
- Top compound events: `Midday:DBL_BA:P45`
- Diagnostic boxed seed: `034`, `011`, `118`, `033`, `044`, `004`, `009`, `334`, `014`, `144`, `003`, `344`, `015`, `016`, `048`, `559`
- Diagnostic straight seed: `811`, `414`, `814`, `801`, `810`, `804`, `111`, `831`, `009`, `090`, `900`, `559`, `595`, `955`, `011`, `034`
- Diagnostic VT-box seed: `13`, `15`, `33`, `4`, `31`, `23`, `18`, `6`, `34`, `14`, `5`, `3`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=212`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
