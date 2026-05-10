# Analysis Arena Predictive Run Report — Virginia4 — D=2026-03-09 (H=2026-03-08)

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
- Results date `D`: `2026-03-09`
- History date `H`: `2026-03-08`
- State: `Virginia4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-09/Virginia4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-09/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-09/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-09/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-09/Virginia4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-09/Virginia4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-09/Virginia4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-09/Virginia4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-09/Virginia4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-09/Virginia4/aux/Virginia4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-09/Virginia4/aux/Virginia4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-09/Virginia4/stable/Virginia4/Virginia4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-09/Virginia4/stable/Virginia4/Virginia4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-09/Virginia4/stable/Virginia4/Virginia4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-09/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-09/Virginia4/digit_reduction/Virginia4/Virginia4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-09/Virginia4/vtrac/Virginia4/Virginia4_vtrac_enhanced_20260416_183127.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-09/Virginia4/hot_zones/Virginia4/Virginia4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `039`, `599`, `358`, `138`, `009`, `559`
- Dominant families: `559`, `599`, `14.0`, `23`, `8`, `5`
- Dominant VTRAC indices: `15`, `5`, `14`, `13`, `1`, `23`
- Context-reinforced canonicals: `039`, `358`, `138`, `005`, `334`, `339`
- Context-only pressure: _none_
- State regime: `dominant_canonical=039`, `dominant_family=559`, `dominant_vtrac_index=15`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=005,001,009,006,013,004`
- R-Consensus context: `events=5`, `signal_class=strong`, `trial_eligible=True`, `top_tails=93,33`, `top_support=039,339,033`
- VTRAC literal watchlist: `15->599,099`, `5->559,059,009`, `14->039,034`, `13->033,358,038`, `1->005,055`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=14`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `039`, `599`, `358`, `138`
- Scoreboard top VTRAC indices: `15`, `5`, `14`, `13`
- Positional shortlist top: `335`, `033`, `133`, `334`, `339`, `338`, `356`, `036`
- Blackapple recommended canonicals: `156`, `489`, `039`, `057`, `129`, `138`, `237`, `246`
- Profit-alert implied canonicals: `039`, `034`, `048`, `089`, `345`, `359`, `458`, `589`, `005`
- Due-double family pressure: `Combined:4:0/5-4/9,1/6-4/9,2/7-3/8`, `Evening:2:0/5-4/9,1/6-4/9,2/7-3/8`, `Midday:2:0/5-4/9,1/6-4/9,2/7-3/8`
- Due-double example canonicals: `445`, `599`, `004`, `699`, `199`, `144`, `778`, `223`
- Top profit alerts: `Midday:A05:039:STR8_8`, `Midday:A01:039:BOX`, `Combined:A08:OVERLAY`, `Midday:A04:039:BOX`
- Top compound events: `Midday:CARRY_PERM:P70`
- Diagnostic boxed seed: `039`, `138`, `339`, `358`, `009`, `005`, `004`, `033`, `599`, `338`, `559`, `059`, `001`, `006`, `334`, `099`
- Diagnostic straight seed: `303`, `393`, `353`, `313`, `343`, `383`, `356`, `306`, `040`, `004`, `400`, `358`, `183`, `538`, `583`, `835`
- Diagnostic VT-box seed: `14`, `1`, `15`, `5`, `13`, `23`, `18`, `33`, `6`, `2`, `34`, `-1`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `039`, `599`, `358`, `138`, `005`, `339`, `009`, `004`, `033`
- Arena-preserved straight canonicals to watch: `303`, `393`, `353`, `313`, `343`, `383`, `356`, `306`, `039`, `358`, `138`, `005`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=195`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
