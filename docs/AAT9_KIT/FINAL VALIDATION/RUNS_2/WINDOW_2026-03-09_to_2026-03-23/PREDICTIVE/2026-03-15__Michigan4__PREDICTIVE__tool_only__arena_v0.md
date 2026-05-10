# Analysis Arena Predictive Run Report — Michigan4 — D=2026-03-15 (H=2026-03-14)

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
- Results date `D`: `2026-03-15`
- History date `H`: `2026-03-14`
- State: `Michigan4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-15/Michigan4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-15/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-15/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-15/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-15/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-15/Michigan4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-15/Michigan4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-15/Michigan4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-15/Michigan4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-15/Michigan4/aux/Michigan4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-15/Michigan4/aux/Michigan4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-15/Michigan4/stable/Michigan4/Michigan4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-15/Michigan4/stable/Michigan4/Michigan4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-15/Michigan4/stable/Michigan4/Michigan4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-15/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-15/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-15/Michigan4/vtrac/Michigan4/Michigan4_vtrac_enhanced_20260416_185807.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-15/Michigan4/hot_zones/Michigan4/Michigan4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `455`, `044`, `008`, `445`, `088`, `004`
- Dominant families: `455`, `445`, `5`, `559`, `229`, `15`
- Dominant VTRAC indices: `5`, `15`, `4`, `3`, `23`, `14`
- Context-reinforced canonicals: `008`, `448`, `048`, `058`
- Context-only pressure: _none_
- State regime: `dominant_canonical=455`, `dominant_family=455`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=004,005,006,007,009,001`
- R-Consensus context: `events=2`, `signal_class=strong`, `trial_eligible=True`, `top_tails=44`, `top_support=044`
- VTRAC literal watchlist: `5->455,045,004,559,059`, `15->044,445,459`, `4->558,008,058,003`, `3->007,255,557,025`, `23->688,368`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=5`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `455`, `044`, `008`, `445`
- Scoreboard top VTRAC indices: `5`, `15`, `4`, `3`
- Positional shortlist top: `158`, `148`, `058`, `578`, `118`, `159`, `048`, `589`
- Blackapple recommended canonicals: `037`, `127`, `379`, `478`, `019`, `028`, `046`, `136`
- Profit-alert implied canonicals: `068`, `008`, `448`, `489`, `899`
- Due-double family pressure: `Combined:0:0/5-1/6,1/6-2/7,1/6-4/9`, `Evening:0:0/5-1/6,1/6-2/7,1/6-4/9`, `Midday:2:0/5-1/6,1/6-2/7,1/6-4/9`
- Due-double example canonicals: `066`, `556`, `566`, `155`, `006`, `115`, `667`, `226`
- Top profit alerts: `Combined:A05:008:STR8_3`, `Combined:A04:068:BOX`, `Evening:A12:448:STR8_4of8`
- Top compound events: `Combined:CARRY_PERM:P70`, `Evening:CLAMP_4:P25`
- Diagnostic boxed seed: `008`, `448`, `048`, `445`, `006`, `058`, `011`, `066`, `455`, `044`, `004`, `005`, `007`, `068`, `118`, `566`
- Diagnostic straight seed: `181`, `581`, `481`, `580`, `587`, `591`, `480`, `589`, `066`, `606`, `660`, `077`, `707`, `770`, `011`, `101`
- Diagnostic VT-box seed: `15`, `5`, `4`, `23`, `1`, `3`, `13`, `8`, `34`, `11`, `20`, `30`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `455`, `044`, `008`, `445`, `448`, `048`, `058`, `006`, `011`, `066`
- Arena-preserved straight canonicals to watch: `181`, `581`, `481`, `580`, `587`, `591`, `480`, `589`, `008`, `448`, `048`, `058`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=192`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
