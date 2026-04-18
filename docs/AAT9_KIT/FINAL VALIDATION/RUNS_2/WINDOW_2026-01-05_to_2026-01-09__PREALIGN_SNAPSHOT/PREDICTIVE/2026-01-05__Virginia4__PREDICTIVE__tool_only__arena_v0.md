# Analysis Arena Predictive Run Report — Virginia4 — D=2026-01-05 (H=2026-01-04)

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
- State: `Virginia4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-05/Virginia4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-05/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-05/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-05/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-05/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-05/Virginia4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-05/Virginia4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-05/Virginia4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-05/Virginia4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-05/Virginia4/aux/Virginia4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-05/Virginia4/aux/Virginia4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-05/Virginia4/stable/Virginia4/Virginia4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-05/Virginia4/stable/Virginia4/Virginia4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-05/Virginia4/stable/Virginia4/Virginia4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-05/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-05/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-05/Virginia4/vtrac/Virginia4/Virginia4_vtrac_enhanced_20260326_043730.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-05/Virginia4/hot_zones/Virginia4/Virginia4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `224`, `559`, `377`, `008`, `229`, `259`
- Dominant families: `559`, `259`, `28`, `30`, `24`, `599`
- Dominant VTRAC indices: `28`, `27`, `5`, `12`, `33`, `4`
- Context-reinforced canonicals: `377`, `008`, `599`, `189`, `359`, `389`
- Context-only pressure: _none_
- State regime: `dominant_canonical=224`, `dominant_family=559`, `dominant_vtrac_index=28`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=014,017,011,113,114,117`
- R-Consensus context: `events=5`, `signal_class=strong`, `trial_eligible=True`, `top_tails=08,02`, `top_support=008,002`
- VTRAC literal watchlist: `28->477,224,229,279`, `27->377,228,223`, `5->559`, `12->259,079,029,579`, `33->334,339,889,488,389,348`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=14`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `224`, `559`, `377`, `008`
- Scoreboard top VTRAC indices: `28`, `27`, `5`, `12`
- Positional shortlist top: `159`, `359`, `145`, `189`, `599`, `156`, `345`, `158`
- Blackapple recommended canonicals: `038`, `058`, `138`, `168`, `238`, `278`, `348`, `358`
- Profit-alert implied canonicals: `089`, `359`, `008`
- Due-double family pressure: `Combined:1:1/6-4/9,2/7-3/8,0/5-4/9`, `Evening:4:1/6-4/9,2/7-3/8,0/5-4/9`, `Midday:0:1/6-4/9,2/7-3/8,0/5-4/9`
- Due-double example canonicals: `699`, `199`, `119`, `446`, `377`, `778`, `223`, `445`
- Top profit alerts: `Combined:A11:008:BOX`, `Combined:A01:089:BOX`, `Combined:A05:008:STR8_3`, `Evening:A08:OVERLAY`, `Midday:A04:359:BOX`
- Top compound events: `Combined:ENGINE_GOV:P85`
- Diagnostic boxed seed: `359`, `377`, `599`, `008`, `559`, `189`, `089`, `224`, `014`, `017`, `011`, `113`, `119`, `156`, `345`, `199`
- Diagnostic straight seed: `593`, `599`, `561`, `591`, `541`, `891`, `543`, `581`, `004`, `040`, `400`, `377`, `737`, `773`, `455`, `545`
- Diagnostic VT-box seed: `27`, `18`, `4`, `28`, `5`, `12`, `10`, `23`, `33`, `14`, `13`, `29`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=225`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
