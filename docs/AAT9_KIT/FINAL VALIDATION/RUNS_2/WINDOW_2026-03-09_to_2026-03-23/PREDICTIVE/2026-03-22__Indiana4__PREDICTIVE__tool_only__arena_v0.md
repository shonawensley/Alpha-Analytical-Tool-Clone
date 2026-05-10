# Analysis Arena Predictive Run Report — Indiana4 — D=2026-03-22 (H=2026-03-21)

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
- Results date `D`: `2026-03-22`
- History date `H`: `2026-03-21`
- State: `Indiana4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-22/Indiana4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-22/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-22/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-22/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-22/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-22/Indiana4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-22/Indiana4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-22/Indiana4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-22/Indiana4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-22/Indiana4/aux/Indiana4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-22/Indiana4/aux/Indiana4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-22/Indiana4/stable/Indiana4/Indiana4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-22/Indiana4/stable/Indiana4/Indiana4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-22/Indiana4/stable/Indiana4/Indiana4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-22/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-22/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-22/Indiana4/vtrac/Indiana4/Indiana4_vtrac_enhanced_20260416_192854.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-22/Indiana4/hot_zones/Indiana4/Indiana4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `559`, `002`, `259`, `025`, `005`, `155`
- Dominant families: `559`, `5`, `12`, `3`, `9`, `24`
- Dominant VTRAC indices: `5`, `3`, `12`, `2`, `1`, `6`
- Context-reinforced canonicals: `559`, `259`, `025`, `005`
- Context-only pressure: _none_
- State regime: `dominant_canonical=559`, `dominant_family=559`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=017,014,055,019,024,004`
- R-Consensus context: `events=8`, `signal_class=strong`, `trial_eligible=True`, `top_tails=02,01,04,55,05`, `top_support=002,004,055,005,001`
- VTRAC literal watchlist: `5->004,559,455,059`, `3->557,002,255,057,025`, `12->259,245,024,029,079`, `2->001,556,155,015`, `1->055,005`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=4`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `559`, `002`, `259`, `025`
- Scoreboard top VTRAC indices: `5`, `3`, `12`, `2`
- Positional shortlist top: `345`, `234`, `344`, `349`, `034`, `123`, `457`, `134`
- Blackapple recommended canonicals: `016`, `026`, `036`, `046`, `056`, `067`, `068`, `069`
- Profit-alert implied canonicals: `023`, `025`, `259`, `005`, `045`, `059`, `455`, `559`
- Due-double family pressure: `Combined:2:0/5-4/9,1/6-2/7,2/7-3/8`, `Evening:1:0/5-4/9,1/6-2/7,2/7-3/8`, `Midday:1:0/5-4/9,1/6-2/7,2/7-3/8`
- Due-double example canonicals: `559`, `445`, `009`, `004`, `177`, `226`, `677`, `266`
- Top profit alerts: `Combined:A01:023:BOX`, `Evening:A01:025:BOX`, `Evening:A05:005:STR8_3`, `Evening:A04:259:BOX`, `Evening:A12:559:STR8_4of8`
- Top compound events: `Evening:CARRY_PERM:P70`
- Diagnostic boxed seed: `005`, `559`, `002`, `259`, `025`, `004`, `055`, `177`, `155`, `455`, `059`, `017`, `014`, `019`, `023`, `009`
- Diagnostic straight seed: `493`, `453`, `423`, `443`, `403`, `123`, `457`, `143`, `177`, `717`, `771`, `337`, `373`, `733`, `249`, `294`
- Diagnostic VT-box seed: `5`, `3`, `12`, `1`, `2`, `24`, `18`, `11`, `6`, `7`, `23`, `15`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `559`, `002`, `259`, `025`, `005`, `004`, `055`, `177`
- Arena-preserved straight canonicals to watch: `493`, `453`, `423`, `443`, `403`, `123`, `457`, `143`, `559`, `259`, `025`, `005`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=207`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
