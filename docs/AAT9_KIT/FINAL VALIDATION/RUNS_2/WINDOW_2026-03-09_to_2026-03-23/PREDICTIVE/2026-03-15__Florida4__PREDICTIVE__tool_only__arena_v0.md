# Analysis Arena Predictive Run Report — Florida4 — D=2026-03-15 (H=2026-03-14)

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
- State: `Florida4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-15/Florida4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-15/Florida4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-15/Florida4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-15/Florida4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-15/Florida4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-15/Florida4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-15/Florida4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-15/Florida4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-15/Florida4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-15/Florida4/aux/Florida4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-15/Florida4/aux/Florida4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-15/Florida4/stable/Florida4/Florida4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-15/Florida4/stable/Florida4/Florida4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-15/Florida4/stable/Florida4/Florida4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-15/Florida4/digit_reduction/Florida4/Florida4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-15/Florida4/digit_reduction/Florida4/Florida4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-15/Florida4/vtrac/Florida4/Florida4_vtrac_enhanced_20260416_185758.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-15/Florida4/hot_zones/Florida4/Florida4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `699`, `224`, `668`, `006`, `499`, `469`
- Dominant families: `559`, `599`, `20`, `28`, `25`, `8`
- Dominant VTRAC indices: `25`, `28`, `10`, `18`, `35`, `6`
- Context-reinforced canonicals: `699`, `668`, `469`, `022`, `266`
- Context-only pressure: _none_
- State regime: `dominant_canonical=699`, `dominant_family=559`, `dominant_vtrac_index=25`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=006,007,004,119,017,014`
- R-Consensus context: `available=false`
- VTRAC literal watchlist: `25->699,469,199,149`, `28->224`, `10->022,225,027,077`, `18->668,168,118`, `35->499`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=3`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `699`, `224`, `668`, `006`
- Scoreboard top VTRAC indices: `25`, `28`, `10`, `18`
- Positional shortlist top: `267`, `247`, `167`, `266`, `269`, `026`, `268`, `147`
- Blackapple recommended canonicals: `015`, `016`, `038`, `056`, `058`, `126`, `127`, `136`
- Profit-alert implied canonicals: `469`, `699`
- Due-double family pressure: `Combined:2:0/5-4/9,1/6-3/8,0/5-1/6`, `Evening:1:0/5-4/9,1/6-3/8,0/5-1/6`, `Midday:3:0/5-4/9,1/6-3/8,0/5-1/6`
- Due-double example canonicals: `009`, `455`, `118`, `133`, `668`, `366`, `011`, `566`
- Top profit alerts: `Midday:A04:469:BOX`, `Midday:A05:699:STR8_3`, `Midday:A08:OVERLAY`, `Combined:A08:OVERLAY`
- Top compound events: `Midday:CARRY_PERM:P70`
- Diagnostic boxed seed: `469`, `699`, `668`, `126`, `026`, `118`, `224`, `006`, `499`, `022`, `007`, `004`, `119`, `266`, `009`, `011`
- Diagnostic straight seed: `620`, `627`, `427`, `617`, `626`, `629`, `628`, `417`, `003`, `030`, `300`, `162`, `216`, `612`, `118`, `181`
- Diagnostic VT-box seed: `25`, `28`, `18`, `23`, `19`, `12`, `2`, `17`, `10`, `35`, `6`, `13`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `699`, `224`, `668`, `006`, `469`, `022`, `126`, `026`, `118`
- Arena-preserved straight canonicals to watch: `620`, `627`, `427`, `617`, `626`, `629`, `628`, `417`, `699`, `668`, `469`, `022`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=208`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
