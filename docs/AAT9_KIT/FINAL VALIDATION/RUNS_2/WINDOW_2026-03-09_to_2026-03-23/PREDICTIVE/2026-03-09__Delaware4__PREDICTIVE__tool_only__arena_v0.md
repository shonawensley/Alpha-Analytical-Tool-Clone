# Analysis Arena Predictive Run Report — Delaware4 — D=2026-03-09 (H=2026-03-08)

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
- State: `Delaware4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-09/Delaware4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-09/Delaware4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-09/Delaware4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-09/Delaware4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-09/Delaware4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-09/Delaware4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-09/Delaware4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-09/Delaware4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-09/Delaware4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-09/Delaware4/aux/Delaware4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-09/Delaware4/aux/Delaware4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-09/Delaware4/stable/Delaware4/Delaware4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-09/Delaware4/stable/Delaware4/Delaware4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-09/Delaware4/stable/Delaware4/Delaware4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-09/Delaware4/digit_reduction/Delaware4/Delaware4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-09/Delaware4/digit_reduction/Delaware4/Delaware4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-09/Delaware4/vtrac/Delaware4/Delaware4_vtrac_enhanced_20260416_183036.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-09/Delaware4/hot_zones/Delaware4/Delaware4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `006`, `129`, `259`, `478`, `244`, `249`
- Dominant families: `259`, `245`, `30`, `24`, `21`, `599`
- Dominant VTRAC indices: `12`, `31`, `2`, `33`, `22`, `15`
- Context-reinforced canonicals: `006`, `129`, `119`, `014`
- Context-only pressure: _none_
- State regime: `dominant_canonical=006`, `dominant_family=259`, `dominant_vtrac_index=12`, `survivor_pressure=True`, `last_remaining=True`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=2`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=011,014,017,013,004,005`
- R-Consensus context: `events=3`, `signal_class=strong`, `trial_eligible=True`, `top_tails=06`, `top_support=006`
- VTRAC literal watchlist: `12->259,245,457,579,024`, `31->244,447,249`, `2->006,155`, `33->488,348,389`, `22->129,679,246`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=2`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `006`, `129`, `259`, `478`
- Scoreboard top VTRAC indices: `12`, `31`, `2`, `33`
- Positional shortlist top: `114`, `116`, `124`, `119`, `112`, `117`, `011`, `126`
- Blackapple recommended canonicals: `012`, `013`, `014`, `015`, `016`, `017`, `018`, `019`
- Profit-alert implied canonicals: `129`, `006`, `557`
- Due-double family pressure: `Combined:7:0/5-3/8,0/5-1/6,0/5-4/9`, `Evening:6:0/5-3/8,0/5-1/6,0/5-4/9`, `Midday:3:0/5-3/8,0/5-1/6,0/5-4/9`
- Due-double example canonicals: `033`, `088`, `355`, `558`, `566`, `155`, `066`, `006`
- Top profit alerts: `Combined:A11:006:BOX`, `Combined:A05:006:STR8_3`, `Combined:A10:557:STR8_3`, `Evening:A04:129:BOX`
- Top compound events: `Combined:STRAIGHT_GATE:P80`
- Diagnostic boxed seed: `006`, `014`, `011`, `017`, `129`, `249`, `024`, `013`, `119`, `117`, `557`, `004`, `033`, `088`, `009`, `559`
- Diagnostic straight seed: `171`, `141`, `161`, `241`, `191`, `121`, `101`, `261`, `009`, `090`, `900`, `117`, `711`, `559`, `595`, `955`
- Diagnostic VT-box seed: `12`, `2`, `31`, `33`, `22`, `29`, `30`, `23`, `18`, `15`, `13`, `10`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `006`, `129`, `259`, `478`, `119`, `014`, `011`, `017`, `249`, `024`, `013`
- Arena-preserved straight canonicals to watch: `171`, `141`, `161`, `241`, `191`, `121`, `101`, `261`, `006`, `129`, `119`, `014`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=220`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
