# Analysis Arena Predictive Run Report — Michigan4 — D=2026-03-14 (H=2026-03-13)

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
- Results date `D`: `2026-03-14`
- History date `H`: `2026-03-13`
- State: `Michigan4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-14/Michigan4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-14/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-14/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-14/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-14/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-14/Michigan4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-14/Michigan4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-14/Michigan4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-14/Michigan4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-14/Michigan4/aux/Michigan4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-14/Michigan4/aux/Michigan4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-14/Michigan4/stable/Michigan4/Michigan4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-14/Michigan4/stable/Michigan4/Michigan4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-14/Michigan4/stable/Michigan4/Michigan4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-14/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-14/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-14/Michigan4/vtrac/Michigan4/Michigan4_vtrac_enhanced_20260416_185336.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-14/Michigan4/hot_zones/Michigan4/Michigan4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `008`, `688`, `455`, `445`, `088`, `448`
- Dominant families: `559`, `455`, `445`, `5`, `33`, `4`
- Dominant VTRAC indices: `5`, `4`, `23`, `15`, `13`, `1`
- Context-reinforced canonicals: `008`, `448`, `058`, `014`, `005`, `458`
- Context-only pressure: _none_
- State regime: `dominant_canonical=008`, `dominant_family=559`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=True`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=2`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=004,005,006,009,007,001`
- R-Consensus context: `available=false`
- VTRAC literal watchlist: `5->455,004,559,045`, `4->008,558,058`, `23->688,138,368`, `15->445,044,459`, `13->088,358`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=5`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `008`, `688`, `455`, `445`
- Scoreboard top VTRAC indices: `5`, `4`, `23`, `15`
- Positional shortlist top: `015`, `158`, `045`, `155`, `458`, `005`, `016`, `014`
- Blackapple recommended canonicals: `019`, `028`, `037`, `046`, `127`, `145`, `379`, `469`
- Profit-alert implied canonicals: `068`, `008`, `134`, `139`, `148`, `189`, `346`, `369`, `468`, `689`, `448`, `489`
- Due-double family pressure: `Combined:3:0/5-1/6,1/6-2/7,1/6-4/9`, `Evening:3:0/5-1/6,1/6-2/7,1/6-4/9`, `Midday:1:0/5-1/6,1/6-2/7,1/6-4/9`
- Due-double example canonicals: `066`, `556`, `566`, `155`, `006`, `115`, `667`, `226`
- Top profit alerts: `Combined:A09:STR8_8`, `Combined:A05:008:STR8_3`, `Combined:A04:068:BOX`, `Evening:A12:448:STR8_4of8`
- Top compound events: `Combined:CARRY_PERM:P70`, `Evening:CLAMP_4:P25`
- Diagnostic boxed seed: `008`, `011`, `014`, `005`, `448`, `058`, `004`, `045`, `006`, `066`, `445`, `017`, `024`, `009`, `068`, `458`
- Diagnostic straight seed: `501`, `581`, `504`, `551`, `584`, `500`, `601`, `401`, `066`, `606`, `660`, `580`, `058`, `085`, `008`, `508`
- Diagnostic VT-box seed: `4`, `1`, `5`, `23`, `15`, `13`, `3`, `12`, `10`, `34`, `8`, `24`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `008`, `688`, `455`, `445`, `448`, `058`, `014`, `011`, `005`, `004`, `045`
- Arena-preserved straight canonicals to watch: `501`, `581`, `504`, `551`, `584`, `500`, `601`, `401`, `008`, `448`, `058`, `014`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=174`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
