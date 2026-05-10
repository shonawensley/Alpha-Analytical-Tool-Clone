# Analysis Arena Predictive Run Report — Indiana4 — D=2026-03-13 (H=2026-03-12)

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
- State: `Indiana4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-13/Indiana4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-13/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-13/Indiana4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-13/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-13/Indiana4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-13/Indiana4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-13/Indiana4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-13/Indiana4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-13/Indiana4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-13/Indiana4/aux/Indiana4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-13/Indiana4/aux/Indiana4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-13/Indiana4/stable/Indiana4/Indiana4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-13/Indiana4/stable/Indiana4/Indiana4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-13/Indiana4/stable/Indiana4/Indiana4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-13/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-13/Indiana4/digit_reduction/Indiana4/Indiana4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-13/Indiana4/vtrac/Indiana4/Indiana4_vtrac_enhanced_20260416_184859.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-13/Indiana4/hot_zones/Indiana4/Indiana4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `599`, `788`, `005`, `889`, `689`, `4889`
- Dominant families: `23`, `21`, `255`, `599`, `29`, `18`
- Dominant VTRAC indices: `29`, `15`, `33`, `24`, `1`, `6`
- Context-reinforced canonicals: `005`, `889`, `689`, `559`, `488`
- Context-only pressure: _none_
- State regime: `dominant_canonical=599`, `dominant_family=23`, `dominant_vtrac_index=29`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=005,007,008,011,134,178`
- R-Consensus context: `events=2`, `signal_class=strong`, `trial_eligible=True`, `top_tails=05`, `top_support=005`
- VTRAC literal watchlist: `29->788,288,238,378`, `15->599,445`, `33->889,488`, `24->689,468,148,189`, `1->005`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=4`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `599`, `788`, `005`, `889`
- Scoreboard top VTRAC indices: `29`, `15`, `33`, `24`
- Positional shortlist top: `588`, `589`, `359`, `358`, `488`, `568`, `458`
- Blackapple recommended canonicals: `018`, `019`, `028`, `029`, `038`, `039`, `048`, `049`
- Profit-alert implied canonicals: `689`, `005`
- Due-double family pressure: `Combined:0:0/5-4/9,1/6-2/7,2/7-3/8`, `Evening:0:0/5-4/9,1/6-2/7,2/7-3/8`, `Midday:7:0/5-4/9,1/6-2/7,2/7-3/8`
- Due-double example canonicals: `559`, `445`, `009`, `004`, `177`, `226`, `677`, `266`
- Top profit alerts: `Midday:A05:005:STR8_3`, `Combined:A04:689:BOX`, `Evening:A08:OVERLAY`, `Midday:A08:OVERLAY`
- Top compound events: _none_
- Diagnostic boxed seed: `005`, `889`, `689`, `288`, `559`, `488`, `177`, `226`, `599`, `445`, `007`, `008`, `011`, `358`, `677`, `122`
- Diagnostic straight seed: `358`, `848`, `853`, `858`, `859`, `359`, `856`, `854`, `177`, `771`, `717`, `288`, `828`, `882`, `255`, `525`
- Diagnostic VT-box seed: `1`, `12`, `29`, `15`, `33`, `24`, `23`, `18`, `17`, `8`, `9`, `11`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `599`, `788`, `005`, `889`, `689`, `559`, `288`, `488`, `177`, `226`
- Arena-preserved straight canonicals to watch: `358`, `848`, `853`, `858`, `859`, `359`, `856`, `854`, `005`, `889`, `689`, `559`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=212`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
