# Analysis Arena Predictive Run Report — Ohio4 — D=2026-03-23 (H=2026-03-22)

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
- Results date `D`: `2026-03-23`
- History date `H`: `2026-03-22`
- State: `Ohio4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-23/Ohio4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-23/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-23/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-23/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-23/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-23/Ohio4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-23/Ohio4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-23/Ohio4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-23/Ohio4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-23/Ohio4/aux/Ohio4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-23/Ohio4/aux/Ohio4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-23/Ohio4/stable/Ohio4/Ohio4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-23/Ohio4/stable/Ohio4/Ohio4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-23/Ohio4/stable/Ohio4/Ohio4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-23/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-23/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-23/Ohio4/vtrac/Ohio4/Ohio4_vtrac_enhanced_20260416_193340.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-23/Ohio4/hot_zones/Ohio4/Ohio4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `224`, `667`, `128`, `002`, `012`, `011`
- Dominant families: `21`, `18`, `224`, `17`, `8`, `7`
- Dominant VTRAC indices: `28`, `17`, `21`, `7`, `3`, `18`
- Context-reinforced canonicals: `224`, `667`, `128`, `002`, `266`, `268`
- Context-only pressure: _none_
- State regime: `dominant_canonical=224`, `dominant_family=21`, `dominant_vtrac_index=28`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=001,011,014,002,006,007`
- R-Consensus context: `events=2`, `signal_class=strong`, `trial_eligible=True`, `top_tails=02`, `top_support=002`
- VTRAC literal watchlist: `28->224`, `17->667,266,126`, `21->128,268,678,178`, `7->012,026,125,067`, `3->002,255,025`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=9`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `224`, `667`, `128`, `002`
- Scoreboard top VTRAC indices: `28`, `17`, `21`, `7`
- Positional shortlist top: `268`, `228`, `688`, `288`, `128`, `028`, `289`
- Blackapple recommended canonicals: `013`, `067`, `139`, `238`, `247`, `256`, `346`, `679`
- Profit-alert implied canonicals: `268`, `667`, `014`, `019`, `046`, `069`, `145`, `159`, `456`, `569`, `126`, `167`
- Due-double family pressure: `Combined:4:1/6-4/9,0/5-1/6,1/6-3/8`, `Evening:2:1/6-4/9,0/5-1/6,1/6-3/8`, `Midday:3:1/6-4/9,0/5-1/6,1/6-3/8`
- Due-double example canonicals: `699`, `466`, `669`, `446`, `066`, `001`, `118`, `688`
- Top profit alerts: `Evening:A09:STR8_8`, `Evening:A05:667:STR8_3`, `Combined:A04:268:BOX`, `Evening:A12:667:STR8_4of8`, `Combined:A08:OVERLAY`
- Top compound events: `Evening:CLAMP_4:P25`
- Diagnostic boxed seed: `268`, `002`, `266`, `224`, `667`, `128`, `012`, `001`, `014`, `118`, `011`, `126`, `226`, `688`, `288`, `066`
- Diagnostic straight seed: `628`, `288`, `268`, `228`, `688`, `218`, `208`, `298`, `009`, `090`, `900`, `118`, `181`, `811`, `559`, `595`
- Diagnostic VT-box seed: `17`, `21`, `3`, `23`, `18`, `28`, `7`, `6`, `9`, `12`, `31`, `10`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `224`, `667`, `128`, `002`, `268`, `266`, `012`, `001`
- Arena-preserved straight canonicals to watch: `628`, `288`, `268`, `228`, `688`, `218`, `208`, `298`, `224`, `667`, `128`, `002`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=210`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
