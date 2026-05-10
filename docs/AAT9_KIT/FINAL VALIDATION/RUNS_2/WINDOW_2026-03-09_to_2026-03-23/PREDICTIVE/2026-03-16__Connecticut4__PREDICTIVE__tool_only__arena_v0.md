# Analysis Arena Predictive Run Report — Connecticut4 — D=2026-03-16 (H=2026-03-15)

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
- Results date `D`: `2026-03-16`
- History date `H`: `2026-03-15`
- State: `Connecticut4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-16/Connecticut4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-16/Connecticut4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-16/Connecticut4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-16/Connecticut4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-16/Connecticut4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-16/Connecticut4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-16/Connecticut4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-16/Connecticut4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-16/Connecticut4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-16/Connecticut4/aux/Connecticut4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-16/Connecticut4/aux/Connecticut4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-16/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-16/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-16/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-16/Connecticut4/digit_reduction/Connecticut4/Connecticut4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-16/Connecticut4/digit_reduction/Connecticut4/Connecticut4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-16/Connecticut4/vtrac/Connecticut4/Connecticut4_vtrac_enhanced_20260416_190217.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-16/Connecticut4/hot_zones/Connecticut4/Connecticut4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `559`, `344`, `044`, `368`, `346`, `689`
- Dominant families: `559`, `449`, `24`, `18`, `23`, `8`
- Dominant VTRAC indices: `5`, `24`, `18`, `15`, `34`, `23`
- Context-reinforced canonicals: `559`, `044`, `569`
- Context-only pressure: _none_
- State regime: `dominant_canonical=559`, `dominant_family=559`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=014,011,013,017,044,178`
- R-Consensus context: `events=1`, `signal_class=moderate`, `trial_eligible=True`, `top_tails=01`, `top_support=001`
- VTRAC literal watchlist: `5->559,059`, `24->689,346,139,369,189`, `18->136,113,366,168,668`, `15->599,044,459,099`, `34->399,899,344`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=1`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `559`, `344`, `044`, `368`
- Scoreboard top VTRAC indices: `5`, `24`, `18`, `15`
- Positional shortlist top: `169`, `369`, `469`, `156`, `356`, `456`, `166`, `366`
- Blackapple recommended canonicals: `014`, `023`, `059`, `068`, `149`, `248`, `347`, `158`
- Profit-alert implied canonicals: `569`, `559`
- Due-double family pressure: `Combined:0:0/5-4/9,3/8-4/9,1/6-2/7`, `Evening:0:0/5-4/9,3/8-4/9,1/6-2/7`, `Midday:2:0/5-4/9,3/8-4/9,1/6-2/7`
- Due-double example canonicals: `099`, `044`, `004`, `399`, `344`, `448`, `488`, `117`
- Top profit alerts: `Midday:A05:559:STR8_3`, `Midday:A04:569:BOX`, `Combined:A08:OVERLAY`, `Evening:A08:OVERLAY`
- Top compound events: `Midday:CARRY_PERM:P70`
- Diagnostic boxed seed: `044`, `559`, `344`, `368`, `369`, `014`, `569`, `366`, `099`, `399`, `346`, `059`, `139`, `011`, `013`, `017`
- Diagnostic straight seed: `636`, `619`, `639`, `649`, `615`, `635`, `645`, `616`, `099`, `909`, `990`, `399`, `939`, `993`, `386`, `683`
- Diagnostic VT-box seed: `15`, `5`, `24`, `18`, `23`, `25`, `34`, `9`, `11`, `8`, `30`, `33`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `559`, `344`, `044`, `368`, `569`, `369`, `014`, `366`
- Arena-preserved straight canonicals to watch: `636`, `619`, `639`, `649`, `615`, `635`, `645`, `616`, `559`, `044`, `569`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=209`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
