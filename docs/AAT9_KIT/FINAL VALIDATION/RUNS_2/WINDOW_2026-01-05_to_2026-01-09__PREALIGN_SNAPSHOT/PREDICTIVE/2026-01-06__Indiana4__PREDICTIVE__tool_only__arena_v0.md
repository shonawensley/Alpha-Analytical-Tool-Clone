# Analysis Arena Predictive Run Report — Indiana4 — D=2026-01-06 (H=2026-01-05)

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
- State: `Indiana4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-06/Indiana4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-06/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-06/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-06/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-06/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-06/Indiana4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-06/Indiana4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-06/Indiana4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-06/Indiana4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-06/Indiana4/aux/Indiana4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-06/Indiana4/aux/Indiana4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-06/Indiana4/stable/Indiana4/Indiana4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-06/Indiana4/stable/Indiana4/Indiana4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-06/Indiana4/stable/Indiana4/Indiana4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-06/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-06/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-06/Indiana4/vtrac/Indiana4/Indiana4_vtrac_enhanced_20260326_044121.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-06/Indiana4/hot_zones/Indiana4/Indiana4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `244`, `366`, `066`, `006`, `138`, `014`
- Dominant families: `244`, `225`, `23`, `21`, `17`, `18`
- Dominant VTRAC indices: `31`, `18`, `6`, `23`, `12`, `8`
- Context-reinforced canonicals: `244`, `066`, `014`, `024`, `068`
- Context-only pressure: `677`
- State regime: `dominant_canonical=244`, `dominant_family=244`, `dominant_vtrac_index=31`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=006,017,003,011,005,004`
- R-Consensus context: `available=false`
- VTRAC literal watchlist: `31->244,447,299`, `18->366,668,168,136`, `6->066`, `23->688,368,138`, `12->029,259,024`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=4`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-support`
- Scoreboard top canonicals: `244`, `366`, `066`, `006`
- Scoreboard top VTRAC indices: `31`, `18`, `6`, `23`
- Positional shortlist top: `066`, `046`, `667`, `467`, `036`, `367`, `067`, `016`
- Blackapple recommended canonicals: `012`, `013`, `014`, `015`, `016`, `017`, `018`, `019`
- Profit-alert implied canonicals: `039`, `244`
- Due-double family pressure: `Combined:4:1/6-2/7,0/5-2/7,0/5-4/9`, `Evening:2:1/6-2/7,0/5-2/7,0/5-4/9`, `Midday:4:1/6-2/7,0/5-2/7,0/5-4/9`
- Due-double example canonicals: `177`, `226`, `677`, `117`, `266`, `667`, `002`, `022`
- Top profit alerts: `Evening:A05:244:STR8_3`, `Midday:A04:039:BOX`
- Top compound events: _none_
- Diagnostic boxed seed: `066`, `244`, `014`, `017`, `177`, `266`, `002`, `366`, `006`, `138`, `003`, `011`, `024`, `039`, `007`, `016`
- Diagnostic straight seed: `066`, `046`, `766`, `746`, `036`, `736`, `076`, `061`, `002`, `020`, `200`, `177`, `717`, `771`, `386`, `683`
- Diagnostic VT-box seed: `31`, `20`, `18`, `6`, `23`, `12`, `17`, `2`, `9`, `14`, `7`, `8`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=232`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
