# Analysis Arena Predictive Run Report — Ohio4 — D=2026-03-13 (H=2026-03-12)

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
- Results date `D`: `2026-03-13`
- History date `H`: `2026-03-12`
- State: `Ohio4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-13/Ohio4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-13/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-13/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-13/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-13/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-13/Ohio4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-13/Ohio4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-13/Ohio4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-13/Ohio4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-13/Ohio4/aux/Ohio4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-13/Ohio4/aux/Ohio4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-13/Ohio4/stable/Ohio4/Ohio4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-13/Ohio4/stable/Ohio4/Ohio4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-13/Ohio4/stable/Ohio4/Ohio4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-13/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-13/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-13/Ohio4/vtrac/Ohio4/Ohio4_vtrac_enhanced_20260416_184920.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-13/Ohio4/hot_zones/Ohio4/Ohio4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `033`, `338`, `003`, `599`, `059`, `069`
- Dominant families: `14`, `8`, `559`, `13`, `23`, `33`
- Dominant VTRAC indices: `13`, `5`, `15`, `4`, `32`, `14`
- Context-reinforced canonicals: `033`, `338`, `003`, `599`, `059`, `069`
- Context-only pressure: _none_
- State regime: `dominant_canonical=033`, `dominant_family=14`, `dominant_vtrac_index=13`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=004,009,011,001,006,005`
- R-Consensus context: `events=8`, `signal_class=strong`, `trial_eligible=True`, `top_tails=03,33,3`, `top_support=003,033,039`
- VTRAC literal watchlist: `13->033,038,358,335`, `5->059,004,009,559,455,045`, `15->599,099,044,049`, `4->003,035,558,058`, `32->338,388`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=9`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `033`, `338`, `003`, `599`
- Scoreboard top VTRAC indices: `13`, `5`, `15`, `4`
- Positional shortlist top: `033`, `034`, `013`, `036`, `003`, `038`, `334`
- Blackapple recommended canonicals: `045`, `049`, `059`, `146`, `149`, `169`, `247`, `249`
- Profit-alert implied canonicals: `039`, `069`, `033`, `049`, `066`, `338`, `388`, `888`
- Due-double family pressure: `Combined:6:1/6-4/9,0/5-1/6,1/6-3/8`, `Evening:3:1/6-4/9,0/5-1/6,1/6-3/8`, `Midday:3:1/6-4/9,0/5-1/6,1/6-3/8`
- Due-double example canonicals: `699`, `466`, `669`, `446`, `066`, `001`, `118`, `688`
- Top profit alerts: `Combined:A11:033:BOX`, `Combined:A01:039:BOX`, `Midday:A04:069:BOX`, `Combined:A05:033:STR8_3`
- Top compound events: `Combined:ENGINE_GOV:P85`, `Evening:CLAMP_4:P25`
- Diagnostic boxed seed: `033`, `003`, `039`, `338`, `038`, `004`, `009`, `059`, `069`, `001`, `049`, `066`, `034`, `599`, `011`, `334`
- Diagnostic straight seed: `043`, `003`, `083`, `033`, `013`, `063`, `433`, `036`, `009`, `090`, `900`, `004`, `040`, `400`, `559`, `595`
- Diagnostic VT-box seed: `13`, `5`, `15`, `14`, `4`, `32`, `23`, `12`, `9`, `6`, `None`, `18`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `033`, `338`, `003`, `599`, `039`, `038`, `004`, `009`, `059`
- Arena-preserved straight canonicals to watch: `043`, `003`, `083`, `033`, `013`, `063`, `433`, `036`, `338`, `599`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=185`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
