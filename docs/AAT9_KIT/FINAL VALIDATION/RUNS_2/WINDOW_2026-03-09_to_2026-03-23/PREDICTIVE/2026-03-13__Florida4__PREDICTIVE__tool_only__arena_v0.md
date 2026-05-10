# Analysis Arena Predictive Run Report — Florida4 — D=2026-03-13 (H=2026-03-12)

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
- State: `Florida4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-13/Florida4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-13/Florida4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-13/Florida4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-13/Florida4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-13/Florida4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-13/Florida4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-13/Florida4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-13/Florida4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-13/Florida4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-13/Florida4/aux/Florida4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-13/Florida4/aux/Florida4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-13/Florida4/stable/Florida4/Florida4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-13/Florida4/stable/Florida4/Florida4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-13/Florida4/stable/Florida4/Florida4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-13/Florida4/digit_reduction/Florida4/Florida4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-13/Florida4/digit_reduction/Florida4/Florida4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-13/Florida4/vtrac/Florida4/Florida4_vtrac_enhanced_20260416_184855.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-13/Florida4/hot_zones/Florida4/Florida4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `224`, `499`, `226`, `022`, `024`, `255`
- Dominant families: `20`, `255`, `28`, `10`, `12`, `7`
- Dominant VTRAC indices: `28`, `20`, `10`, `35`, `12`, `25`
- Context-reinforced canonicals: `499`, `022`, `024`, `267`, `077`, `477`
- Context-only pressure: _none_
- State regime: `dominant_canonical=224`, `dominant_family=20`, `dominant_vtrac_index=28`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=004,007,006,009,001,044`
- R-Consensus context: `events=1`, `signal_class=moderate`, `trial_eligible=True`, `top_tails=99`, `top_support=499,799`
- VTRAC literal watchlist: `28->477,224`, `20->677,226,267`, `10->077,022,225,027`, `35->499,449`, `12->024,245,079,047`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=3`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-support`
- Scoreboard top canonicals: `224`, `499`, `226`, `022`
- Scoreboard top VTRAC indices: `28`, `20`, `10`, `35`
- Positional shortlist top: `247`, `477`, `147`, `244`, `249`, `024`, `248`, `246`
- Blackapple recommended canonicals: `012`, `015`, `023`, `024`, `025`, `026`, `027`, `028`
- Profit-alert implied canonicals: `267`, `499`
- Due-double family pressure: `Combined:3:0/5-4/9,1/6-3/8,0/5-1/6`, `Evening:4:0/5-4/9,1/6-3/8,0/5-1/6`, `Midday:1:0/5-4/9,1/6-3/8,0/5-1/6`
- Due-double example canonicals: `009`, `455`, `118`, `133`, `668`, `366`, `011`, `566`
- Top profit alerts: `Midday:A05:499:STR8_3`, `Combined:A04:267:BOX`
- Top compound events: _none_
- Diagnostic boxed seed: `499`, `024`, `267`, `009`, `477`, `027`, `247`, `244`, `022`, `077`, `004`, `007`, `006`, `012`, `249`, `003`
- Diagnostic straight seed: `427`, `424`, `429`, `477`, `417`, `420`, `428`, `426`, `003`, `030`, `300`, `149`, `267`, `244`, `442`, `499`
- Diagnostic VT-box seed: `20`, `35`, `12`, `28`, `23`, `15`, `3`, `31`, `10`, `7`, `2`, `11`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `224`, `499`, `226`, `022`, `024`, `267`, `009`, `477`, `027`, `247`, `244`
- Arena-preserved straight canonicals to watch: `427`, `424`, `429`, `477`, `417`, `420`, `428`, `426`, `499`, `022`, `024`, `267`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=194`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
