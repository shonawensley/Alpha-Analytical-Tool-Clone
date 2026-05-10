# Analysis Arena Predictive Run Report — Michigan4 — D=2026-03-18 (H=2026-03-17)

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
- State: `Michigan4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-18/Michigan4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-18/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-18/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-18/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-18/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-18/Michigan4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-18/Michigan4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-18/Michigan4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-18/Michigan4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-18/Michigan4/aux/Michigan4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-18/Michigan4/aux/Michigan4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-18/Michigan4/stable/Michigan4/Michigan4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-18/Michigan4/stable/Michigan4/Michigan4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-18/Michigan4/stable/Michigan4/Michigan4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-18/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-18/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-18/Michigan4/vtrac/Michigan4/Michigan4_vtrac_enhanced_20260416_191120.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-18/Michigan4/hot_zones/Michigan4/Michigan4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `001`, `559`, `044`, `055`, `677`, `167`
- Dominant families: `559`, `229`, `5`, `2`, `3`, `12`
- Dominant VTRAC indices: `20`, `5`, `2`, `1`, `15`, `3`
- Context-reinforced canonicals: `001`, `055`, `267`, `557`
- Context-only pressure: `135`
- State regime: `dominant_canonical=001`, `dominant_family=559`, `dominant_vtrac_index=20`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=006,007,005,009,004,001`
- R-Consensus context: `events=4`, `signal_class=strong`, `trial_eligible=True`, `top_tails=55,44`, `top_support=055,044`
- VTRAC literal watchlist: `20->677,267,226,127,122`, `5->559,455,004`, `2->556,001,006,015`, `1->055`, `15->044,599,445`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=5`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `001`, `559`, `044`, `055`
- Scoreboard top VTRAC indices: `20`, `5`, `2`, `1`
- Positional shortlist top: `158`, `168`, `118`, `568`, `558`, `155`, `589`, `015`
- Blackapple recommended canonicals: `019`, `028`, `037`, `046`, `127`, `136`, `145`, `235`
- Profit-alert implied canonicals: `267`, `055`, `001`, `006`, `015`, `056`
- Due-double family pressure: `Combined:2:0/5-1/6,1/6-2/7,1/6-4/9`, `Evening:1:0/5-1/6,1/6-2/7,1/6-4/9`, `Midday:1:0/5-1/6,1/6-2/7,1/6-4/9`
- Due-double example canonicals: `066`, `556`, `566`, `155`, `006`, `115`, `667`, `226`
- Top profit alerts: `Midday:A05:055:STR8_3`, `Combined:A04:267:BOX`, `Evening:A12:001:STR8_4of8`, `Evening:A08:OVERLAY`
- Top compound events: `Evening:CLAMP_4:P25`
- Diagnostic boxed seed: `001`, `055`, `006`, `267`, `011`, `558`, `066`, `566`, `044`, `226`, `127`, `007`, `005`, `009`, `557`, `015`
- Diagnostic straight seed: `681`, `585`, `581`, `181`, `586`, `551`, `589`, `501`, `066`, `660`, `606`, `011`, `110`, `101`, `088`, `808`
- Diagnostic VT-box seed: `1`, `20`, `2`, `15`, `5`, `21`, `17`, `8`, `9`, `11`, `12`, `-1`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `001`, `559`, `044`, `055`, `267`, `557`, `006`, `011`, `558`, `066`, `566`
- Arena-preserved straight canonicals to watch: `681`, `585`, `581`, `181`, `586`, `551`, `589`, `501`, `001`, `055`, `267`, `557`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=193`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
