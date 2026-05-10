# Analysis Arena Predictive Run Report — Ohio4 — D=2026-03-12 (H=2026-03-11)

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
- Results date `D`: `2026-03-12`
- History date `H`: `2026-03-11`
- State: `Ohio4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-12/Ohio4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-12/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-12/Ohio4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-12/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-12/Ohio4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-12/Ohio4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-12/Ohio4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-12/Ohio4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-12/Ohio4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-12/Ohio4/aux/Ohio4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-12/Ohio4/aux/Ohio4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-12/Ohio4/stable/Ohio4/Ohio4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-12/Ohio4/stable/Ohio4/Ohio4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-12/Ohio4/stable/Ohio4/Ohio4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-12/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-12/Ohio4/digit_reduction/Ohio4/Ohio4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-12/Ohio4/vtrac/Ohio4/Ohio4_vtrac_enhanced_20260416_184447.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-12/Ohio4/hot_zones/Ohio4/Ohio4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `033`, `338`, `013`, `599`, `059`, `334`
- Dominant families: `8`, `14`, `249`, `13.0`, `18`, `13`
- Dominant VTRAC indices: `13`, `15`, `5`, `4`, `8`, `32`
- Context-reinforced canonicals: `033`, `338`, `013`, `599`, `059`, `334`
- Context-only pressure: `038`
- State regime: `dominant_canonical=033`, `dominant_family=8`, `dominant_vtrac_index=13`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=011,017,001,004,009,014`
- R-Consensus context: `events=6`, `signal_class=strong`, `trial_eligible=True`, `top_tails=03,33`, `top_support=033,003`
- VTRAC literal watchlist: `13->033,335,038`, `15->599,459,044,049`, `5->059,559,004,455`, `4->003,558,058,035`, `8->013,036,356`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=9`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `033`, `338`, `013`, `599`
- Scoreboard top VTRAC indices: `13`, `15`, `5`, `4`
- Positional shortlist top: `033`, `334`, `034`, `344`, `013`, `036`, `003`, `333`
- Blackapple recommended canonicals: `035`, `038`, `136`, `138`, `237`, `238`, `348`, `349`
- Profit-alert implied canonicals: `034`, `033`, `059`, `066`, `338`, `388`, `888`
- Due-double family pressure: `Combined:4:1/6-4/9,0/5-1/6,1/6-3/8`, `Evening:2:1/6-4/9,0/5-1/6,1/6-3/8`, `Midday:2:1/6-4/9,0/5-1/6,1/6-3/8`
- Due-double example canonicals: `699`, `466`, `669`, `446`, `066`, `001`, `118`, `688`
- Top profit alerts: `Combined:A11:033:BOX`, `Evening:A01:034:BOX`, `Combined:A02:033:STR8_3`, `Combined:A05:033:STR8_3`, `Midday:A04:059:BOX`
- Top compound events: `Combined:STRAIGHT_GATE:P80`, `Evening:CLAMP_4:P25`
- Diagnostic boxed seed: `033`, `013`, `066`, `003`, `338`, `038`, `059`, `334`, `001`, `004`, `034`, `036`, `009`, `599`, `011`, `017`
- Diagnostic straight seed: `033`, `013`, `003`, `433`, `043`, `443`, `063`, `333`, `009`, `090`, `900`, `038`, `083`, `066`, `113`, `131`
- Diagnostic VT-box seed: `13`, `5`, `4`, `18`, `15`, `23`, `12`, `32`, `33`, `14`, `8`, `6`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `033`, `338`, `013`, `599`, `066`, `003`, `038`, `059`, `334`
- Arena-preserved straight canonicals to watch: `033`, `013`, `003`, `433`, `043`, `443`, `063`, `333`, `338`, `599`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=189`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
