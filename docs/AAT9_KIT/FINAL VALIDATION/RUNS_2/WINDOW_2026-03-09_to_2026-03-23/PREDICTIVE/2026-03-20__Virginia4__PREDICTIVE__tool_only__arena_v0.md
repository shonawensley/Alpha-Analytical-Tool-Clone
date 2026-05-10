# Analysis Arena Predictive Run Report — Virginia4 — D=2026-03-20 (H=2026-03-19)

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
- Results date `D`: `2026-03-20`
- History date `H`: `2026-03-19`
- State: `Virginia4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-20/Virginia4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-20/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-20/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-20/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-20/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-20/Virginia4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-20/Virginia4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-20/Virginia4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-20/Virginia4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-20/Virginia4/aux/Virginia4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-20/Virginia4/aux/Virginia4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-20/Virginia4/stable/Virginia4/Virginia4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-20/Virginia4/stable/Virginia4/Virginia4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-20/Virginia4/stable/Virginia4/Virginia4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-20/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-20/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-20/Virginia4/vtrac/Virginia4/Virginia4_vtrac_enhanced_20260416_192041.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-20/Virginia4/hot_zones/Virginia4/Virginia4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `225`, `255`, `559`, `268`, `259`, `022`
- Dominant families: `259`, `559`, `225`, `10`, `12`, `255`
- Dominant VTRAC indices: `10`, `3`, `21`, `28`, `5`, `12`
- Context-reinforced canonicals: `225`, `268`, `022`, `229`, `025`, `677`
- Context-only pressure: _none_
- State regime: `dominant_canonical=225`, `dominant_family=259`, `dominant_vtrac_index=10`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=024,013,015,018,022,055`
- R-Consensus context: `events=1`, `signal_class=moderate`, `trial_eligible=True`, `top_tails=22`, `top_support=022`
- VTRAC literal watchlist: `10->225,022,027`, `3->255,025,057`, `21->268,236,678`, `28->224,229`, `5->559,059`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=14`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `225`, `255`, `559`, `268`
- Scoreboard top VTRAC indices: `10`, `3`, `21`, `28`
- Positional shortlist top: `225`, `229`, `256`, `269`, `122`, `156`, `566`, `569`
- Blackapple recommended canonicals: `015`, `016`, `025`, `027`, `126`, `127`, `136`, `138`
- Profit-alert implied canonicals: `268`, `022`
- Due-double family pressure: `Combined:3:0/5-4/9,1/6-4/9,2/7-3/8`, `Evening:4:0/5-4/9,1/6-4/9,2/7-3/8`, `Midday:1:0/5-4/9,1/6-4/9,2/7-3/8`
- Due-double example canonicals: `445`, `599`, `004`, `699`, `199`, `144`, `778`, `223`
- Top profit alerts: `Combined:A05:022:STR8_3`, `Midday:A04:268:BOX`, `Combined:A08:OVERLAY`
- Top compound events: _none_
- Diagnostic boxed seed: `022`, `025`, `225`, `255`, `559`, `268`, `015`, `229`, `004`, `027`, `024`, `013`, `018`, `199`, `059`, `259`
- Diagnostic straight seed: `252`, `292`, `652`, `692`, `212`, `651`, `656`, `659`, `004`, `040`, `400`, `255`, `025`, `520`, `052`, `250`
- Diagnostic VT-box seed: `10`, `21`, `3`, `28`, `5`, `12`, `23`, `2`, `6`, `17`, `20`, `15`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `225`, `255`, `559`, `268`, `022`, `229`, `025`, `015`
- Arena-preserved straight canonicals to watch: `252`, `292`, `652`, `692`, `212`, `651`, `656`, `659`, `225`, `268`, `022`, `229`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=183`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
