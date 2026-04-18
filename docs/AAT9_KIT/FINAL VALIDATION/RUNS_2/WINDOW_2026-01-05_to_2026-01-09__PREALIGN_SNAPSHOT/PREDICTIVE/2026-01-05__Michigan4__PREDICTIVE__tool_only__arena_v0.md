# Analysis Arena Predictive Run Report — Michigan4 — D=2026-01-05 (H=2026-01-04)

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
- Results date `D`: `2026-01-05`
- History date `H`: `2026-01-04`
- State: `Michigan4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-05/Michigan4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-05/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-05/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-05/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-05/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-05/Michigan4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-05/Michigan4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-05/Michigan4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-05/Michigan4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-05/Michigan4/aux/Michigan4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-05/Michigan4/aux/Michigan4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-05/Michigan4/stable/Michigan4/Michigan4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-05/Michigan4/stable/Michigan4/Michigan4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-05/Michigan4/stable/Michigan4/Michigan4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-05/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-05/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-05/Michigan4/vtrac/Michigan4/Michigan4_vtrac_enhanced_20260326_043654.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-05/Michigan4/hot_zones/Michigan4/Michigan4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `168`, `118`, `668`, `011`, `156`, `166`
- Dominant families: `18`, `6`, `8`, `23`, `24`, `2`
- Dominant VTRAC indices: `18`, `6`, `23`, `2`, `8`, `17`
- Context-reinforced canonicals: `168`, `668`, `011`, `156`, `166`, `016`
- Context-only pressure: _none_
- State regime: `dominant_canonical=168`, `dominant_family=18`, `dominant_vtrac_index=18`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=011,001,006,005,014,066`
- R-Consensus context: `available=false`
- VTRAC literal watchlist: `18->168,668,118,136`, `6->016,011,066,156,566`, `23->688,133,336,188,138,368`, `2->015,001,006,155,556`, `8->356,068,013`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=5`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `168`, `118`, `668`, `011`
- Scoreboard top VTRAC indices: `18`, `6`, `23`, `2`
- Positional shortlist top: `168`, `668`, `116`, `148`, `166`, `016`, `156`, `018`
- Blackapple recommended canonicals: `013`, `049`, `058`, `067`, `139`, `148`, `157`, `238`
- Profit-alert implied canonicals: `168`, `011`, `566`
- Due-double family pressure: `Combined:8:1/6-2/7,0/5-1/6,2/7-3/8`, `Evening:4:1/6-2/7,0/5-1/6,2/7-3/8`, `Midday:8:1/6-2/7,0/5-1/6,2/7-3/8`
- Due-double example canonicals: `112`, `667`, `226`, `266`, `566`, `155`, `066`, `556`
- Top profit alerts: `Combined:A05:011:STR8_3`, `Combined:A04:168:BOX`, `Combined:A10:566:STR8_3`, `Combined:A08:OVERLAY`
- Top compound events: `Combined:CARRY_PERM:P70`
- Diagnostic boxed seed: `168`, `668`, `156`, `016`, `011`, `118`, `166`, `566`, `013`, `066`, `116`, `112`, `136`, `001`, `006`, `005`
- Diagnostic straight seed: `168`, `668`, `161`, `160`, `165`, `148`, `661`, `108`, `112`, `121`, `211`, `119`, `191`, `911`, `186`, `681`
- Diagnostic VT-box seed: `18`, `15`, `6`, `23`, `2`, `8`, `17`, `16`, `4`, `7`, `24`, `19`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=150`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
