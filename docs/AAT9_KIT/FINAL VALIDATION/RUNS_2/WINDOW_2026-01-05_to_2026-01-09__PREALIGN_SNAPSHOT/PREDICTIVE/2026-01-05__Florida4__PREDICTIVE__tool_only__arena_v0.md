# Analysis Arena Predictive Run Report — Florida4 — D=2026-01-05 (H=2026-01-04)

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
- Results date `D`: `2026-01-05`
- History date `H`: `2026-01-04`
- State: `Florida4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-05/Florida4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-05/Florida4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-05/Florida4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-05/Florida4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-05/Florida4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-05/Florida4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-05/Florida4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-05/Florida4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-05/Florida4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-05/Florida4/aux/Florida4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-05/Florida4/aux/Florida4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-05/Florida4/stable/Florida4/Florida4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-05/Florida4/stable/Florida4/Florida4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-05/Florida4/stable/Florida4/Florida4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-05/Florida4/digit_reduction/Florida4/Florida4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-05/Florida4/digit_reduction/Florida4/Florida4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-05/Florida4/vtrac/Florida4/Florida4_vtrac_enhanced_20260326_043646.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-05/Florida4/hot_zones/Florida4/Florida4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `344`, `033`, `334`, `445`, `336`, `346`
- Dominant families: `445`, `259`, `559`, `24`, `33`, `23`
- Dominant VTRAC indices: `33`, `15`, `34`, `23`, `13`, `24`
- Context-reinforced canonicals: `344`, `033`, `334`, `445`, `034`, `014`
- Context-only pressure: _none_
- State regime: `dominant_canonical=344`, `dominant_family=445`, `dominant_vtrac_index=33`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=014,006,007,033,011,044`
- R-Consensus context: `events=4`, `signal_class=strong`, `trial_eligible=True`, `top_tails=33`, `top_support=033,334,344,044,034`
- VTRAC literal watchlist: `33->334,889,339`, `15->445,044,599,459,049`, `34->344,349`, `23->336,138,368,688,188,133`, `13->335,033`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=3`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `344`, `033`, `334`, `445`
- Scoreboard top VTRAC indices: `33`, `15`, `34`, `23`
- Positional shortlist top: `034`, `045`, `344`, `347`, `445`, `048`, `457`, `033`
- Blackapple recommended canonicals: `014`, `023`, `149`, `239`, `248`, `257`, `347`, `356`
- Profit-alert implied canonicals: `467`, `033`, `334`, `339`, `348`, `389`
- Due-double family pressure: `Combined:1:0/5-3/8,3/8-4/9,0/5-4/9`, `Evening:1:0/5-3/8,3/8-4/9,0/5-4/9`, `Midday:0:0/5-3/8,3/8-4/9,0/5-4/9`
- Due-double example canonicals: `588`, `003`, `008`, `335`, `889`, `488`, `339`, `448`
- Top profit alerts: `Combined:A05:033:STR8_3`, `Evening:A04:467:BOX`, `Combined:A12:334:STR8_4of8`, `Combined:A08:OVERLAY`
- Top compound events: `Combined:CLAMP_4:P25`
- Diagnostic boxed seed: `033`, `344`, `334`, `445`, `014`, `034`, `339`, `044`, `347`, `048`, `003`, `008`, `336`, `889`, `006`, `007`
- Diagnostic straight seed: `434`, `454`, `084`, `033`, `034`, `054`, `734`, `754`, `003`, `030`, `300`, `008`, `080`, `800`, `344`, `443`
- Diagnostic VT-box seed: `33`, `15`, `13`, `34`, `23`, `18`, `24`, `22`, `9`, `11`, `25`, `30`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=171`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
