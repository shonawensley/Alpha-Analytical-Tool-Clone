# Analysis Arena Predictive Run Report — Pennsylvania4 — D=2026-03-21 (H=2026-03-20)

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
- State: `Pennsylvania4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-21/Pennsylvania4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-21/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-21/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-21/Pennsylvania4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/aux/Pennsylvania4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-21/Pennsylvania4/aux/Pennsylvania4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-21/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-21/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-21/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-21/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-21/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/vtrac/Pennsylvania4/Pennsylvania4_vtrac_enhanced_20260416_192454.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-21/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `446`, `447`, `478`, `014`, `677`, `477`
- Dominant families: `449`, `24`, `21`, `144`, `31`, `30`
- Dominant VTRAC indices: `25`, `30`, `31`, `14`, `35`, `20`
- Context-reinforced canonicals: `447`, `014`, `088`, `678`, `177`
- Context-only pressure: _none_
- State regime: `dominant_canonical=446`, `dominant_family=449`, `dominant_vtrac_index=25`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=044,014,017,057,011,059`
- R-Consensus context: `events=2`, `signal_class=strong`, `trial_eligible=True`, `top_tails=04,07`, `top_support=004,007`
- VTRAC literal watchlist: `25->446,144,199,149`, `30->478,347,248`, `31->447,244`, `14->048,034,359`, `35->449,499`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=11`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `446`, `447`, `478`, `014`
- Scoreboard top VTRAC indices: `25`, `30`, `31`, `14`
- Positional shortlist top: `147`, `179`, `167`, `178`, `177`, `447`, `479`, `137`
- Blackapple recommended canonicals: `014`, `149`, `248`, `347`, `023`, `059`, `068`, `158`
- Profit-alert implied canonicals: `678`, `088`, `012`, `017`, `026`, `067`, `125`, `157`, `256`, `567`, `066`
- Due-double family pressure: `Combined:7:0/5-4/9,3/8-4/9,2/7-3/8`, `Evening:6:0/5-4/9,3/8-4/9,2/7-3/8`, `Midday:3:0/5-4/9,3/8-4/9,2/7-3/8`
- Due-double example canonicals: `455`, `559`, `009`, `599`, `099`, `448`, `399`, `339`
- Top profit alerts: `Combined:A09:STR8_8`, `Midday:A05:088:STR8_3`, `Combined:A04:678:BOX`, `Combined:A10:066:STR8_3`
- Top compound events: `Combined:IDX_ECHO_BASE:P60`
- Diagnostic boxed seed: `447`, `014`, `066`, `478`, `477`, `017`, `088`, `678`, `007`, `009`, `149`, `347`, `044`, `057`, `177`, `059`
- Diagnostic straight seed: `167`, `447`, `147`, `197`, `187`, `177`, `497`, `137`, `007`, `070`, `700`, `477`, `747`, `774`, `048`, `084`
- Diagnostic VT-box seed: `31`, `18`, `23`, `33`, `15`, `9`, `20`, `25`, `30`, `14`, `35`, `28`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `446`, `447`, `478`, `014`, `088`, `678`, `066`, `477`, `017`
- Arena-preserved straight canonicals to watch: `167`, `447`, `147`, `197`, `187`, `177`, `497`, `137`, `014`, `088`, `678`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=219`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
