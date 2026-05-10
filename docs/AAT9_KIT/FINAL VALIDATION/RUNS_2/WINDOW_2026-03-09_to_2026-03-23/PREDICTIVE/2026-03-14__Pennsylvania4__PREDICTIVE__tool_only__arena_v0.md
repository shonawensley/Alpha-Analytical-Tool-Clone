# Analysis Arena Predictive Run Report — Pennsylvania4 — D=2026-03-14 (H=2026-03-13)

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
- Results date `D`: `2026-03-14`
- History date `H`: `2026-03-13`
- State: `Pennsylvania4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-14/Pennsylvania4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-14/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-14/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-14/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-14/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-14/Pennsylvania4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-14/Pennsylvania4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-14/Pennsylvania4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-14/Pennsylvania4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-14/Pennsylvania4/aux/Pennsylvania4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-14/Pennsylvania4/aux/Pennsylvania4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-14/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-14/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-14/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-14/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-14/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-14/Pennsylvania4/vtrac/Pennsylvania4/Pennsylvania4_vtrac_enhanced_20260416_185359.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-14/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `559`, `013`, `224`, `259`, `005`, `2334`
- Dominant families: `259`, `29`, `12`, `33`, `14`, `23`
- Dominant VTRAC indices: `8`, `5`, `18`, `28`, `32`, `12`
- Context-reinforced canonicals: `013`, `005`, `008`, `117`
- Context-only pressure: _none_
- State regime: `dominant_canonical=559`, `dominant_family=259`, `dominant_vtrac_index=8`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=005,007,009,001,008,004`
- R-Consensus context: `events=3`, `signal_class=strong`, `trial_eligible=True`, `top_tails=03,05`, `top_support=003,005`
- VTRAC literal watchlist: `8->013,135,036,356,568,158`, `5->559`, `18->113,136,366,668`, `28->224,229`, `32->338`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=11`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `559`, `013`, `224`, `259`
- Scoreboard top VTRAC indices: `8`, `5`, `18`, `28`
- Positional shortlist top: `128`, `248`, `127`, `247`, `258`, `257`, `028`, `238`
- Blackapple recommended canonicals: `012`, `013`, `014`, `015`, `016`, `017`, `018`, `019`
- Profit-alert implied canonicals: `013`, `005`, `034`, `039`, `048`, `089`, `345`, `359`, `458`, `589`, `018`, `036`
- Due-double family pressure: `Combined:4:0/5-2/7,3/8-4/9,0/5-4/9`, `Evening:2:0/5-2/7,3/8-4/9,0/5-4/9`, `Midday:4:0/5-2/7,3/8-4/9,0/5-4/9`
- Due-double example canonicals: `007`, `255`, `225`, `022`, `448`, `399`, `339`, `488`
- Top profit alerts: `Combined:A09:STR8_8`, `Midday:A05:005:STR8_3`, `Combined:A04:013:BOX`, `Combined:A12:013:STR8_4of8`, `Evening:A08:OVERLAY`
- Top compound events: `Combined:IDX_ECHO_BASE:P60`
- Diagnostic boxed seed: `013`, `005`, `007`, `009`, `008`, `015`, `036`, `001`, `117`, `014`, `019`, `018`, `127`, `238`, `002`, `388`
- Diagnostic straight seed: `271`, `283`, `281`, `284`, `274`, `285`, `275`, `280`, `007`, `070`, `700`, `013`, `002`, `020`, `200`, `031`
- Diagnostic VT-box seed: `1`, `8`, `5`, `18`, `23`, `12`, `15`, `28`, `32`, `30`, `14`, `17`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `559`, `013`, `224`, `259`, `005`, `008`, `117`, `007`, `009`, `015`, `036`, `001`
- Arena-preserved straight canonicals to watch: `271`, `283`, `281`, `284`, `274`, `285`, `275`, `280`, `013`, `005`, `008`, `117`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=216`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
