# Analysis Arena Predictive Run Report — Virginia4 — D=2026-01-08 (H=2026-01-07)

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
- State: `Virginia4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-08/Virginia4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-08/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-08/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-08/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-08/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-08/Virginia4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-08/Virginia4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-08/Virginia4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-08/Virginia4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-08/Virginia4/aux/Virginia4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-08/Virginia4/aux/Virginia4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-08/Virginia4/stable/Virginia4/Virginia4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-08/Virginia4/stable/Virginia4/Virginia4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-08/Virginia4/stable/Virginia4/Virginia4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-08/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-08/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-08/Virginia4/vtrac/Virginia4/Virginia4_vtrac_enhanced_20260326_045059.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-08/Virginia4/hot_zones/Virginia4/Virginia4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `559`, `024`, `244`, `134`, `059`, `224`
- Dominant families: `559`, `12.0`, `24`, `224`, `229`, `18`
- Dominant VTRAC indices: `5`, `24`, `12`, `31`, `18`, `28`
- Context-reinforced canonicals: `559`, `024`, `134`, `136`, `016`
- Context-only pressure: `677`
- State regime: `dominant_canonical=559`, `dominant_family=559`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=011,001,004,009,014,017`
- R-Consensus context: `events=6`, `signal_class=strong`, `trial_eligible=True`, `top_tails=24,07,01`, `top_support=024,007,001`
- VTRAC literal watchlist: `5->559,059`, `24->134,346,189,689`, `12->024,579,047`, `31->244,249`, `18->668,113,366,136`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=14`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `559`, `024`, `244`, `134`
- Scoreboard top VTRAC indices: `5`, `24`, `12`, `31`
- Positional shortlist top: `134`, `014`, `349`, `136`, `049`, `016`, `344`, `139`
- Blackapple recommended canonicals: `016`, `034`, `124`, `169`, `178`, `268`, `349`, `358`
- Profit-alert implied canonicals: `024`, `029`, `047`, `079`, `245`, `259`, `457`, `579`, `045`, `059`, `455`, `559`
- Due-double family pressure: `Combined:0:1/6-4/9,2/7-3/8,0/5-4/9`, `Evening:0:1/6-4/9,2/7-3/8,0/5-4/9`, `Midday:3:1/6-4/9,2/7-3/8,0/5-4/9`
- Due-double example canonicals: `699`, `199`, `119`, `446`, `377`, `778`, `223`, `445`
- Top profit alerts: `Evening:A05:024:STR8_8`, `Evening:A01:024:BOX`, `Midday:A08:OVERLAY`, `Evening:A04:024:BOX`
- Top compound events: `Evening:CARRY_PERM:P70`, `Midday:CLAMP_4:P25`
- Diagnostic boxed seed: `136`, `024`, `059`, `004`, `016`, `349`, `559`, `134`, `001`, `009`, `014`, `244`, `011`, `178`, `199`, `377`
- Diagnostic straight seed: `349`, `361`, `061`, `341`, `041`, `049`, `344`, `391`, `004`, `040`, `400`, `059`, `136`, `163`, `316`, `613`
- Diagnostic VT-box seed: `12`, `5`, `18`, `23`, `28`, `24`, `31`, `20`, `17`, `33`, `19`, `3`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=231`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
