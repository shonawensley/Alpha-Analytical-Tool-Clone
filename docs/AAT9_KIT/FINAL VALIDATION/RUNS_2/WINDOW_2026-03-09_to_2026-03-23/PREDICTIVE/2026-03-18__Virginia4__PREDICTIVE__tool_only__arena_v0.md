# Analysis Arena Predictive Run Report — Virginia4 — D=2026-03-18 (H=2026-03-17)

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
- Results date `D`: `2026-03-18`
- History date `H`: `2026-03-17`
- State: `Virginia4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-18/Virginia4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-18/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-18/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-18/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-18/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-18/Virginia4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-18/Virginia4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-18/Virginia4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-18/Virginia4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-18/Virginia4/aux/Virginia4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-18/Virginia4/aux/Virginia4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-18/Virginia4/stable/Virginia4/Virginia4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-18/Virginia4/stable/Virginia4/Virginia4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-18/Virginia4/stable/Virginia4/Virginia4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-18/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-18/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-18/Virginia4/vtrac/Virginia4/Virginia4_vtrac_enhanced_20260416_191155.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-18/Virginia4/hot_zones/Virginia4/Virginia4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `559`, `255`, `225`, `235`, `668`, `256`
- Dominant families: `255`, `559`, `3`, `21`, `23`, `11`
- Dominant VTRAC indices: `3`, `5`, `10`, `1`, `11`, `7`
- Context-reinforced canonicals: `235`, `055`, `025`, `005`
- Context-only pressure: _none_
- State regime: `dominant_canonical=559`, `dominant_family=255`, `dominant_vtrac_index=3`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=005,013,015,055,009,022`
- R-Consensus context: `events=1`, `signal_class=moderate`, `trial_eligible=True`, `top_tails=55`, `top_support=055`
- VTRAC literal watchlist: `3->255,025,057`, `5->559,455`, `10->225,022,027`, `1->055,005`, `11->235,023`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=14`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `559`, `255`, `225`, `235`
- Scoreboard top VTRAC indices: `3`, `5`, `10`, `1`
- Positional shortlist top: `358`, `389`, `035`, `039`, `258`, `289`, `588`, `025`
- Blackapple recommended canonicals: `012`, `018`, `023`, `024`, `025`, `026`, `027`, `028`
- Profit-alert implied canonicals: `235`, `055`
- Due-double family pressure: `Combined:3:0/5-4/9,1/6-4/9,2/7-3/8`, `Evening:2:0/5-4/9,1/6-4/9,2/7-3/8`, `Midday:1:0/5-4/9,1/6-4/9,2/7-3/8`
- Due-double example canonicals: `445`, `599`, `004`, `699`, `199`, `144`, `778`, `223`
- Top profit alerts: `Evening:A05:055:STR8_3`, `Combined:A04:235:BOX`
- Top compound events: _none_
- Diagnostic boxed seed: `055`, `025`, `559`, `255`, `235`, `455`, `005`, `004`, `057`, `013`, `015`, `009`, `024`, `199`, `225`, `668`
- Diagnostic straight seed: `853`, `893`, `053`, `093`, `852`, `892`, `858`, `052`, `004`, `040`, `400`, `255`, `055`, `505`, `550`, `525`
- Diagnostic VT-box seed: `1`, `12`, `3`, `5`, `10`, `11`, `23`, `33`, `18`, `7`, `8`, `15`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `559`, `255`, `225`, `235`, `055`, `025`, `005`, `455`, `004`
- Arena-preserved straight canonicals to watch: `853`, `893`, `053`, `093`, `852`, `892`, `858`, `052`, `235`, `055`, `025`, `005`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=187`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
