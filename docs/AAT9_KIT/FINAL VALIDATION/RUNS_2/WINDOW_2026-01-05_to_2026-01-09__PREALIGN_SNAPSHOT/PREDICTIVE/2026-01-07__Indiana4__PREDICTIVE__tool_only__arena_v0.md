# Analysis Arena Predictive Run Report — Indiana4 — D=2026-01-07 (H=2026-01-06)

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
- State: `Indiana4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-07/Indiana4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-07/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-07/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-07/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-07/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-07/Indiana4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-07/Indiana4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-07/Indiana4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-07/Indiana4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-07/Indiana4/aux/Indiana4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-07/Indiana4/aux/Indiana4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-07/Indiana4/stable/Indiana4/Indiana4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-07/Indiana4/stable/Indiana4/Indiana4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-07/Indiana4/stable/Indiana4/Indiana4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-07/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-07/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-07/Indiana4/vtrac/Indiana4/Indiana4_vtrac_enhanced_20260326_044552.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-07/Indiana4/hot_zones/Indiana4/Indiana4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `244`, `066`, `004`, `669`, `366`, `006`
- Dominant families: `244`, `18`, `31`, `6`, `8`, `12`
- Dominant VTRAC indices: `31`, `6`, `18`, `5`, `12`, `19`
- Context-reinforced canonicals: `244`, `066`, `004`, `669`, `366`, `234`
- Context-only pressure: `016`
- State regime: `dominant_canonical=244`, `dominant_family=244`, `dominant_vtrac_index=31`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=006,003,004,017,005,013`
- R-Consensus context: `available=false`
- VTRAC literal watchlist: `31->244,447,299,249`, `6->066,016`, `18->366,668`, `5->059,004,559`, `12->029,259,024,245`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=4`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `244`, `066`, `004`, `669`
- Scoreboard top VTRAC indices: `31`, `6`, `18`, `5`
- Positional shortlist top: `367`, `677`, `667`, `467`, `067`, `678`, `037`, `346`
- Blackapple recommended canonicals: `015`, `016`, `025`, `027`, `035`, `038`, `045`, `049`
- Profit-alert implied canonicals: `234`, `244`, `002`, `004`, `009`, `045`, `059`
- Due-double family pressure: `Combined:6:1/6-2/7,0/5-2/7,0/5-4/9`, `Evening:3:1/6-2/7,0/5-2/7,0/5-4/9`, `Midday:5:1/6-2/7,0/5-2/7,0/5-4/9`
- Due-double example canonicals: `177`, `226`, `677`, `117`, `266`, `667`, `002`, `022`
- Top profit alerts: `Evening:A05:244:STR8_3`, `Combined:A04:234:BOX`, `Combined:A12:004:STR8_4of8`, `Combined:A10:002:STR8_3`, `Evening:A08:OVERLAY`
- Top compound events: `Combined:CLAMP_4:P25`
- Diagnostic boxed seed: `002`, `066`, `004`, `366`, `244`, `234`, `669`, `006`, `016`, `003`, `017`, `025`, `007`, `045`, `677`, `667`
- Diagnostic straight seed: `736`, `776`, `766`, `746`, `706`, `786`, `730`, `436`, `002`, `020`, `200`, `066`, `606`, `660`, `266`, `626`
- Diagnostic VT-box seed: `31`, `6`, `18`, `5`, `12`, `23`, `17`, `2`, `3`, `19`, `30`, `20`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=240`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
