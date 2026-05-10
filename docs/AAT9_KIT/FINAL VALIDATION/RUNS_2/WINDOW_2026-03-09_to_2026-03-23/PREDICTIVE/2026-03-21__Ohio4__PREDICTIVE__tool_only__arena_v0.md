# Analysis Arena Predictive Run Report — Ohio4 — D=2026-03-21 (H=2026-03-20)

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
- Results date `D`: `2026-03-21`
- History date `H`: `2026-03-20`
- State: `Ohio4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-21/Ohio4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-21/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-21/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-21/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-21/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-21/Ohio4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-21/Ohio4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-21/Ohio4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-21/Ohio4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-21/Ohio4/aux/Ohio4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-21/Ohio4/aux/Ohio4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-21/Ohio4/stable/Ohio4/Ohio4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-21/Ohio4/stable/Ohio4/Ohio4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-21/Ohio4/stable/Ohio4/Ohio4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-21/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-21/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-21/Ohio4/vtrac/Ohio4/Ohio4_vtrac_enhanced_20260416_192447.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-21/Ohio4/hot_zones/Ohio4/Ohio4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `699`, `002`, `018`, `299`, `255`, `024`
- Dominant families: `299`, `9`, `259`, `21`, `12`, `31`
- Dominant VTRAC indices: `3`, `25`, `31`, `8`, `12`, `24`
- Context-reinforced canonicals: `002`, `018`, `024`, `248`, `599`, `168`
- Context-only pressure: _none_
- State regime: `dominant_canonical=699`, `dominant_family=299`, `dominant_vtrac_index=3`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=006,009,044,001,005,007`
- R-Consensus context: `events=5`, `signal_class=strong`, `trial_eligible=True`, `top_tails=02,24,04`, `top_support=002,004,024`
- VTRAC literal watchlist: `3->002,255`, `25->699`, `31->244,299,799,249`, `8->018,158,013`, `12->024,259,245`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=9`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `699`, `002`, `018`, `299`
- Scoreboard top VTRAC indices: `3`, `25`, `31`, `8`
- Positional shortlist top: `889`, `289`, `188`, `689`, `128`, `168`, `488`, `248`
- Blackapple recommended canonicals: `134`, `017`, `035`, `125`, `179`, `278`, `368`, `012`
- Profit-alert implied canonicals: `024`, `018`, `002`
- Due-double family pressure: `Combined:0:1/6-4/9,0/5-1/6,1/6-3/8`, `Evening:0:1/6-4/9,0/5-1/6,1/6-3/8`, `Midday:1:1/6-4/9,0/5-1/6,1/6-3/8`
- Due-double example canonicals: `699`, `466`, `669`, `446`, `066`, `001`, `118`, `688`
- Top profit alerts: `Midday:A01:024:BOX`, `Combined:A04:018:BOX`, `Midday:A05:002:STR8_3`, `Combined:A08:OVERLAY`, `Midday:A08:OVERLAY`
- Top compound events: _none_
- Diagnostic boxed seed: `002`, `018`, `024`, `009`, `001`, `248`, `168`, `004`, `118`, `699`, `244`, `006`, `044`, `066`, `559`, `299`
- Diagnostic straight seed: `898`, `298`, `818`, `698`, `218`, `618`, `848`, `248`, `009`, `090`, `900`, `118`, `181`, `811`, `018`, `004`
- Diagnostic VT-box seed: `12`, `3`, `25`, `31`, `8`, `23`, `15`, `17`, `24`, `7`, `4`, `22`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `699`, `002`, `018`, `299`, `024`, `248`, `009`, `001`, `168`, `004`
- Arena-preserved straight canonicals to watch: `898`, `298`, `818`, `698`, `218`, `618`, `848`, `248`, `002`, `018`, `024`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=214`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
