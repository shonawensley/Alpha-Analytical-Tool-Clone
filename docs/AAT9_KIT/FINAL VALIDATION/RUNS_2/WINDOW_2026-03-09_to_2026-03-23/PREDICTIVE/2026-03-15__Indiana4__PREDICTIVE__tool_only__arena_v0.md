# Analysis Arena Predictive Run Report — Indiana4 — D=2026-03-15 (H=2026-03-14)

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
- State: `Indiana4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-15/Indiana4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-15/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-15/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-15/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-15/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-15/Indiana4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-15/Indiana4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-15/Indiana4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-15/Indiana4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-15/Indiana4/aux/Indiana4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-15/Indiana4/aux/Indiana4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-15/Indiana4/stable/Indiana4/Indiana4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-15/Indiana4/stable/Indiana4/Indiana4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-15/Indiana4/stable/Indiana4/Indiana4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-15/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-15/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-15/Indiana4/vtrac/Indiana4/Indiana4_vtrac_enhanced_20260416_185802.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-15/Indiana4/hot_zones/Indiana4/Indiana4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `599`, `224`, `669`, `005`, `559`, `667`
- Dominant families: `599`, `299`, `15`, `32`, `31`, `30`
- Dominant VTRAC indices: `15`, `28`, `31`, `33`, `27`, `29`
- Context-reinforced canonicals: `599`, `005`, `559`, `056`, `566`, `799`
- Context-only pressure: _none_
- State regime: `dominant_canonical=599`, `dominant_family=599`, `dominant_vtrac_index=15`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=134,005,007,008,178,017`
- R-Consensus context: `events=7`, `signal_class=strong`, `trial_eligible=True`, `top_tails=99,05`, `top_support=005,499,099,599,477,559`
- VTRAC literal watchlist: `15->599,099,445`, `28->224,229,779,279`, `31->799,244,299,249`, `33->348,389`, `27->228,223,278`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=4`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `599`, `224`, `669`, `005`
- Scoreboard top VTRAC indices: `15`, `28`, `31`, `33`
- Positional shortlist top: `789`, `339`, `389`, `379`, `799`, `399`, `889`, `679`
- Blackapple recommended canonicals: `027`, `189`, `279`, `369`, `378`, `459`, `567`, `018`
- Profit-alert implied canonicals: `056`, `249`, `005`, `445`, `459`, `599`
- Due-double family pressure: `Combined:1:0/5-4/9,1/6-2/7,2/7-3/8`, `Evening:2:0/5-4/9,1/6-2/7,2/7-3/8`, `Midday:0:0/5-4/9,1/6-2/7,2/7-3/8`
- Due-double example canonicals: `559`, `445`, `009`, `004`, `177`, `226`, `677`, `266`
- Top profit alerts: `Midday:A01:056:BOX`, `Midday:A05:005:STR8_3`, `Combined:A04:249:BOX`, `Combined:A12:599:STR8_4of8`
- Top compound events: `Combined:CLAMP_4:P25`
- Diagnostic boxed seed: `005`, `599`, `559`, `799`, `445`, `056`, `389`, `177`, `226`, `224`, `099`, `134`, `007`, `008`, `249`, `459`
- Diagnostic straight seed: `398`, `799`, `798`, `393`, `793`, `399`, `898`, `796`, `717`, `177`, `771`, `262`, `299`, `699`, `929`, `969`
- Diagnostic VT-box seed: `28`, `15`, `31`, `12`, `1`, `33`, `23`, `18`, `5`, `10`, `27`, `19`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `599`, `224`, `669`, `005`, `559`, `056`, `799`, `445`, `389`, `177`
- Arena-preserved straight canonicals to watch: `398`, `799`, `798`, `393`, `793`, `399`, `898`, `796`, `599`, `005`, `559`, `056`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=205`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
