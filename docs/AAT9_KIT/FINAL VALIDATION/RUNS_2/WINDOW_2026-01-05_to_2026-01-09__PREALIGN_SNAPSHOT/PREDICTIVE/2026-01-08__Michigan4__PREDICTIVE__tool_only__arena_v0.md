# Analysis Arena Predictive Run Report — Michigan4 — D=2026-01-08 (H=2026-01-07)

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
- State: `Michigan4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-08/Michigan4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-08/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-08/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-08/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-08/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-08/Michigan4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-08/Michigan4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-08/Michigan4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-08/Michigan4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-08/Michigan4/aux/Michigan4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-08/Michigan4/aux/Michigan4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-08/Michigan4/stable/Michigan4/Michigan4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-08/Michigan4/stable/Michigan4/Michigan4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-08/Michigan4/stable/Michigan4/Michigan4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-08/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-08/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-08/Michigan4/vtrac/Michigan4/Michigan4_vtrac_enhanced_20260326_045025.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-08/Michigan4/hot_zones/Michigan4/Michigan4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `344`, `019`, `144`, `059`, `001`, `044`
- Dominant families: `559`, `9`, `8`, `2`, `5`, `18`
- Dominant VTRAC indices: `5`, `34`, `15`, `9`, `8`, `2`
- Context-reinforced canonicals: `344`, `019`, `144`, `015`, `599`, `004`
- Context-only pressure: _none_
- State regime: `dominant_canonical=344`, `dominant_family=559`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=011,001,014,005,006,017`
- R-Consensus context: `events=1`, `signal_class=moderate`, `trial_eligible=True`, `top_tails=44`, `top_support=044`
- VTRAC literal watchlist: `5->059,009,004,559`, `34->344`, `15->044,599,445,459`, `9->014,019,069,046`, `8->018,158,135`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=5`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `344`, `019`, `144`, `059`
- Scoreboard top VTRAC indices: `5`, `34`, `15`, `9`
- Positional shortlist top: `115`, `114`, `155`, `157`, `011`, `015`, `113`, `116`
- Blackapple recommended canonicals: `015`, `016`, `025`, `027`, `035`, `038`, `045`, `049`
- Profit-alert implied canonicals: `019`, `344`, `004`, `009`, `045`, `059`
- Due-double family pressure: `Combined:0:1/6-2/7,0/5-1/6,2/7-3/8`, `Evening:0:1/6-2/7,0/5-1/6,2/7-3/8`, `Midday:11:1/6-2/7,0/5-1/6,2/7-3/8`
- Due-double example canonicals: `112`, `667`, `226`, `266`, `566`, `155`, `066`, `556`
- Top profit alerts: `Midday:A05:344:STR8_3`, `Evening:A04:019:BOX`, `Combined:A12:004:STR8_4of8`, `Combined:A08:OVERLAY`, `Midday:A08:OVERLAY`
- Top compound events: `Combined:CLAMP_4:P25`
- Diagnostic boxed seed: `015`, `014`, `155`, `344`, `019`, `009`, `004`, `011`, `112`, `144`, `059`, `001`, `044`, `005`, `017`, `045`
- Diagnostic straight seed: `151`, `141`, `155`, `051`, `157`, `101`, `131`, `161`, `112`, `121`, `211`, `119`, `191`, `911`, `117`, `171`
- Diagnostic VT-box seed: `5`, `34`, `15`, `9`, `2`, `18`, `23`, `8`, `25`, `6`, `3`, `10`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=198`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
