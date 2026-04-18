# Analysis Arena Predictive Run Report — Virginia4 — D=2026-01-06 (H=2026-01-05)

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
- State: `Virginia4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-06/Virginia4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-06/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-06/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-06/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-06/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-06/Virginia4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-06/Virginia4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-06/Virginia4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-06/Virginia4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-06/Virginia4/aux/Virginia4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-06/Virginia4/aux/Virginia4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-06/Virginia4/stable/Virginia4/Virginia4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-06/Virginia4/stable/Virginia4/Virginia4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-06/Virginia4/stable/Virginia4/Virginia4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-06/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-06/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-06/Virginia4/vtrac/Virginia4/Virginia4_vtrac_enhanced_20260326_044200.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-06/Virginia4/hot_zones/Virginia4/Virginia4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `224`, `559`, `189`, `008`, `009`, `377`
- Dominant families: `229`, `259`, `27`, `28`, `24`, `30`
- Dominant VTRAC indices: `5`, `28`, `12`, `27`, `24`, `23`
- Context-reinforced canonicals: `189`, `009`, `377`, `024`, `089`, `889`
- Context-only pressure: `677`
- State regime: `dominant_canonical=224`, `dominant_family=229`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=001,009,011,014,017,057`
- R-Consensus context: `events=8`, `signal_class=strong`, `trial_eligible=True`, `top_tails=08,09,07,24`, `top_support=008,009,007,024`
- VTRAC literal watchlist: `5->559,004,009`, `28->224,229`, `12->024,259,029,579,047`, `27->377,228,223`, `24->189,148,689`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=14`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `224`, `559`, `189`, `008`
- Scoreboard top VTRAC indices: `5`, `28`, `12`, `27`
- Positional shortlist top: `189`, `148`, `139`, `899`, `134`, `489`, `128`, `889`
- Blackapple recommended canonicals: `057`, `156`, `246`, `345`, `579`, `678`, `012`, `039`
- Profit-alert implied canonicals: `089`, `024`, `009`
- Due-double family pressure: `Combined:0:1/6-4/9,2/7-3/8,0/5-4/9`, `Evening:0:1/6-4/9,2/7-3/8,0/5-4/9`, `Midday:1:1/6-4/9,2/7-3/8,0/5-4/9`
- Due-double example canonicals: `699`, `199`, `119`, `446`, `377`, `778`, `223`, `445`
- Top profit alerts: `Combined:A11:009:BOX`, `Combined:A01:089:BOX`, `Combined:A05:009:STR8_3`, `Evening:A04:024:BOX`, `Midday:A08:OVERLAY`
- Top compound events: `Combined:ENGINE_GOV:P85`
- Diagnostic boxed seed: `009`, `377`, `089`, `189`, `004`, `024`, `899`, `489`, `224`, `008`, `001`, `011`, `014`, `889`, `148`, `057`
- Diagnostic straight seed: `899`, `849`, `891`, `841`, `391`, `341`, `821`, `898`, `004`, `040`, `400`, `377`, `098`, `737`, `773`, `089`
- Diagnostic VT-box seed: `5`, `12`, `28`, `27`, `23`, `18`, `4`, `3`, `24`, `20`, `14`, `6`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=215`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
