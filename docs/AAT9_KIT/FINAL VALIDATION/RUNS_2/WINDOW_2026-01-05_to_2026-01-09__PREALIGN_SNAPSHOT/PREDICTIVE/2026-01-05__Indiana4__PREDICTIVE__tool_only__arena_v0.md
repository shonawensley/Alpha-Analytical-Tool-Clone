# Analysis Arena Predictive Run Report — Indiana4 — D=2026-01-05 (H=2026-01-04)

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
- State: `Indiana4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-05/Indiana4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-05/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-05/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-05/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-05/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-05/Indiana4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-05/Indiana4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-05/Indiana4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-05/Indiana4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-05/Indiana4/aux/Indiana4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-05/Indiana4/aux/Indiana4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-05/Indiana4/stable/Indiana4/Indiana4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-05/Indiana4/stable/Indiana4/Indiana4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-05/Indiana4/stable/Indiana4/Indiana4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-05/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-05/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-05/Indiana4/vtrac/Indiana4/Indiana4_vtrac_enhanced_20260326_043651.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-05/Indiana4/hot_zones/Indiana4/Indiana4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `244`, `668`, `0668`, `066`, `366`, `368`
- Dominant families: `23`, `244`, `17`, `21`, `6`, `18`
- Dominant VTRAC indices: `31`, `18`, `23`, `6`, `17`, `28`
- Context-reinforced canonicals: `244`, `668`, `066`, `366`, `368`, `126`
- Context-only pressure: _none_
- State regime: `dominant_canonical=244`, `dominant_family=23`, `dominant_vtrac_index=31`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=017,011,014,006,013,002`
- R-Consensus context: `available=false`
- VTRAC literal watchlist: `31->244,447,299,249,479`, `18->366,668,136`, `23->368,688,188,138`, `6->066,016`, `17->266,126`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=4`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `244`, `668`, `066`, `366`
- Scoreboard top VTRAC indices: `31`, `18`, `23`, `6`
- Positional shortlist top: `666`, `466`, `066`, `046`, `266`, `667`, `366`, `668`
- Blackapple recommended canonicals: `012`, `013`, `014`, `015`, `016`, `017`, `018`, `019`
- Profit-alert implied canonicals: `368`, `244`, `011`, `016`, `066`
- Due-double family pressure: `Combined:2:1/6-2/7,0/5-2/7,0/5-4/9`, `Evening:1:1/6-2/7,0/5-2/7,0/5-4/9`, `Midday:3:1/6-2/7,0/5-2/7,0/5-4/9`
- Due-double example canonicals: `177`, `226`, `677`, `117`, `266`, `667`, `002`, `022`
- Top profit alerts: `Evening:A05:244:STR8_3`, `Midday:A04:368:BOX`, `Midday:A12:066:STR8_4of8`
- Top compound events: `Midday:CLAMP_4:P25`
- Diagnostic boxed seed: `066`, `668`, `368`, `266`, `244`, `002`, `366`, `017`, `011`, `014`, `012`, `177`, `006`, `013`, `016`, `667`
- Diagnostic straight seed: `066`, `626`, `686`, `666`, `646`, `046`, `676`, `636`, `002`, `020`, `200`, `668`, `177`, `717`, `771`, `386`
- Diagnostic VT-box seed: `23`, `6`, `31`, `18`, `17`, `20`, `7`, `8`, `9`, `2`, `10`, `12`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=223`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
