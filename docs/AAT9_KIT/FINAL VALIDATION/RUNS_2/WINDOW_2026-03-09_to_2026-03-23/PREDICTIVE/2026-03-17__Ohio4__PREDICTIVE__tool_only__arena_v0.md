# Analysis Arena Predictive Run Report — Ohio4 — D=2026-03-17 (H=2026-03-16)

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
- Results date `D`: `2026-03-17`
- History date `H`: `2026-03-16`
- State: `Ohio4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-17/Ohio4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-17/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-17/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-17/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-17/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-17/Ohio4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-17/Ohio4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-17/Ohio4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-17/Ohio4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-17/Ohio4/aux/Ohio4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-17/Ohio4/aux/Ohio4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-17/Ohio4/stable/Ohio4/Ohio4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-17/Ohio4/stable/Ohio4/Ohio4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-17/Ohio4/stable/Ohio4/Ohio4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-17/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-17/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-17/Ohio4/vtrac/Ohio4/Ohio4_vtrac_enhanced_20260416_190712.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-17/Ohio4/hot_zones/Ohio4/Ohio4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `069`, `559`, `224`, `009`, `244`, `299`
- Dominant families: `299`, `559`, `9`, `15`, `599`, `259`
- Dominant VTRAC indices: `5`, `15`, `9`, `31`, `28`, `34`
- Context-reinforced canonicals: `069`, `224`, `599`, `099`, `066`
- Context-only pressure: `026`
- State regime: `dominant_canonical=069`, `dominant_family=299`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=006,009,004,001,005,007`
- R-Consensus context: `events=6`, `signal_class=strong`, `trial_eligible=True`, `top_tails=3,06,09,99,03`, `top_support=099,006,009,003,039,399`
- VTRAC literal watchlist: `5->009,004,559,455`, `15->099,599,049`, `9->069,046,019`, `31->244,299`, `28->224,229,247`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=9`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `069`, `559`, `224`, `009`
- Scoreboard top VTRAC indices: `5`, `15`, `9`, `31`
- Positional shortlist top: `066`, `069`, `068`, `466`, `468`, `469`, `099`
- Blackapple recommended canonicals: `026`, `035`, `125`, `269`, `278`, `359`, `368`, `458`
- Profit-alert implied canonicals: `069`, `099`, `066`, `014`, `019`, `046`
- Due-double family pressure: `Combined:4:1/6-4/9,0/5-1/6,1/6-3/8`, `Evening:2:1/6-4/9,0/5-1/6,1/6-3/8`, `Midday:7:1/6-4/9,0/5-1/6,1/6-3/8`
- Due-double example canonicals: `699`, `466`, `669`, `446`, `066`, `001`, `118`, `688`
- Top profit alerts: `Evening:A05:099:STR8_3`, `Combined:A10:066:STR8_3`, `Combined:A04:069:BOX`, `Combined:A12:069:STR8_4of8`, `Combined:A08:OVERLAY`
- Top compound events: `Combined:CLAMP_4:P25`
- Diagnostic boxed seed: `066`, `069`, `099`, `009`, `006`, `004`, `559`, `001`, `224`, `599`, `026`, `466`, `118`, `244`, `299`, `455`
- Diagnostic straight seed: `066`, `069`, `096`, `068`, `466`, `468`, `469`, `099`, `009`, `090`, `900`, `606`, `660`, `004`, `040`, `400`
- Diagnostic VT-box seed: `15`, `5`, `9`, `23`, `18`, `4`, `34`, `31`, `28`, `7`, `6`, `22`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `069`, `559`, `224`, `009`, `599`, `099`, `066`, `006`, `004`, `001`
- Arena-preserved straight canonicals to watch: `066`, `069`, `096`, `068`, `466`, `468`, `469`, `099`, `224`, `599`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=189`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
