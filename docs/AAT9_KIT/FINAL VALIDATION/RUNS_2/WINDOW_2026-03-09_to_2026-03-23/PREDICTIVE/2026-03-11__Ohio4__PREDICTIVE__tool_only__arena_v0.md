# Analysis Arena Predictive Run Report — Ohio4 — D=2026-03-11 (H=2026-03-10)

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
- Results date `D`: `2026-03-11`
- History date `H`: `2026-03-10`
- State: `Ohio4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-11/Ohio4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-11/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-11/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-11/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-11/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-11/Ohio4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-11/Ohio4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-11/Ohio4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-11/Ohio4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-11/Ohio4/aux/Ohio4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-11/Ohio4/aux/Ohio4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-11/Ohio4/stable/Ohio4/Ohio4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-11/Ohio4/stable/Ohio4/Ohio4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-11/Ohio4/stable/Ohio4/Ohio4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-11/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-11/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-11/Ohio4/vtrac/Ohio4/Ohio4_vtrac_enhanced_20260416_184012.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-11/Ohio4/hot_zones/Ohio4/Ohio4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `113`, `599`, `069`, `003`, `059`, `136`
- Dominant families: `114`, `8`, `5`, `14`, `24`, `23`
- Dominant VTRAC indices: `18`, `4`, `15`, `5`, `9`, `6`
- Context-reinforced canonicals: `113`, `599`, `069`, `003`, `059`, `013`
- Context-only pressure: _none_
- State regime: `dominant_canonical=113`, `dominant_family=114`, `dominant_vtrac_index=18`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=011,017,004,009,001,007`
- R-Consensus context: `events=3`, `signal_class=strong`, `trial_eligible=True`, `top_tails=03`, `top_support=003`
- VTRAC literal watchlist: `18->366,113,136,168`, `4->003,558,058,035`, `15->599,099,049`, `5->059,559,455`, `9->069,014,145,569`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=9`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `113`, `599`, `069`, `003`
- Scoreboard top VTRAC indices: `18`, `4`, `15`, `5`
- Positional shortlist top: `015`, `145`, `035`, `345`, `045`, `056`, `058`, `059`
- Blackapple recommended canonicals: `015`, `016`, `035`, `038`, `126`, `127`, `136`, `138`
- Profit-alert implied canonicals: `038`, `069`, `003`, `066`, `113`, `118`, `136`, `168`
- Due-double family pressure: `Combined:2:1/6-4/9,0/5-1/6,1/6-3/8`, `Evening:1:1/6-4/9,0/5-1/6,1/6-3/8`, `Midday:1:1/6-4/9,0/5-1/6,1/6-3/8`
- Due-double example canonicals: `699`, `466`, `669`, `446`, `066`, `001`, `118`, `688`
- Top profit alerts: `Evening:A01:038:BOX`, `Midday:A04:069:BOX`, `Evening:A05:003:STR8_3`, `Midday:A08:OVERLAY`, `Combined:A12:113:STR8_4of8`
- Top compound events: `Combined:CLAMP_4:P25`
- Diagnostic boxed seed: `113`, `136`, `003`, `009`, `066`, `069`, `059`, `004`, `038`, `013`, `118`, `599`, `168`, `011`, `017`, `001`
- Diagnostic straight seed: `015`, `415`, `035`, `435`, `045`, `065`, `085`, `095`, `009`, `090`, `900`, `559`, `595`, `955`, `113`, `136`
- Diagnostic VT-box seed: `18`, `4`, `15`, `5`, `9`, `23`, `12`, `13`, `6`, `2`, `21`, `33`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `113`, `599`, `069`, `003`, `136`, `009`, `066`, `059`, `004`
- Arena-preserved straight canonicals to watch: `015`, `415`, `035`, `435`, `045`, `065`, `085`, `095`, `113`, `599`, `069`, `003`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=197`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
