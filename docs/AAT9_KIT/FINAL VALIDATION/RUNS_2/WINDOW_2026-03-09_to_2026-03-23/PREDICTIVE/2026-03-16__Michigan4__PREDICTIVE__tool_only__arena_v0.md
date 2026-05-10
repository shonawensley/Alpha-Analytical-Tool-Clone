# Analysis Arena Predictive Run Report — Michigan4 — D=2026-03-16 (H=2026-03-15)

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
- State: `Michigan4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-16/Michigan4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-16/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-16/Michigan4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-16/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-16/Michigan4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-16/Michigan4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-16/Michigan4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-16/Michigan4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-16/Michigan4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-16/Michigan4/aux/Michigan4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-16/Michigan4/aux/Michigan4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-16/Michigan4/stable/Michigan4/Michigan4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-16/Michigan4/stable/Michigan4/Michigan4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-16/Michigan4/stable/Michigan4/Michigan4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-16/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-16/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-16/Michigan4/vtrac/Michigan4/Michigan4_vtrac_enhanced_20260416_190233.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-16/Michigan4/hot_zones/Michigan4/Michigan4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `044`, `067`, `677`, `455`, `458`, `558`
- Dominant families: `559`, `15.0`, `5`, `9`, `24`, `23`
- Dominant VTRAC indices: `15`, `5`, `20`, `14`, `7`, `3`
- Context-reinforced canonicals: `044`, `067`, `458`
- Context-only pressure: `135`
- State regime: `dominant_canonical=044`, `dominant_family=559`, `dominant_vtrac_index=15`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=004,006,005,007,009,001`
- R-Consensus context: `events=3`, `signal_class=strong`, `trial_eligible=True`, `top_tails=44`, `top_support=044`
- VTRAC literal watchlist: `15->044,445`, `5->455,045,004,559`, `20->677,267,226,122,127`, `14->458,048,034,345`, `7->067,125,012`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=5`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `044`, `067`, `677`, `455`
- Scoreboard top VTRAC indices: `15`, `5`, `20`, `14`
- Positional shortlist top: `158`, `148`, `118`, `568`, `589`, `155`, `015`, `159`
- Blackapple recommended canonicals: `019`, `028`, `127`, `136`, `145`, `235`, `289`, `037`
- Profit-alert implied canonicals: `044`, `067`, `034`, `039`, `048`, `089`, `345`, `359`, `458`, `589`, `049`, `099`
- Due-double family pressure: `Combined:0:0/5-1/6,1/6-2/7,1/6-4/9`, `Evening:0:0/5-1/6,1/6-2/7,1/6-4/9`, `Midday:3:0/5-1/6,1/6-2/7,1/6-4/9`
- Due-double example canonicals: `066`, `556`, `566`, `155`, `006`, `115`, `667`, `226`
- Top profit alerts: `Midday:A09:STR8_8`, `Evening:A05:044:STR8_3`, `Combined:A04:067:BOX`, `Evening:A12:044:STR8_4of8`, `Evening:A02:044:STR8_3`
- Top compound events: `Evening:CLAMP_4:P25`
- Diagnostic boxed seed: `044`, `067`, `458`, `006`, `066`, `004`, `005`, `007`, `011`, `048`, `589`, `155`, `566`, `688`, `077`, `088`
- Diagnostic straight seed: `581`, `481`, `181`, `586`, `589`, `551`, `501`, `591`, `066`, `606`, `660`, `088`, `077`, `707`, `770`, `688`
- Diagnostic VT-box seed: `15`, `5`, `20`, `14`, `7`, `23`, `1`, `4`, `8`, `18`, `33`, `21`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `044`, `067`, `677`, `455`, `458`, `006`, `066`, `004`, `005`, `007`
- Arena-preserved straight canonicals to watch: `581`, `481`, `181`, `586`, `589`, `551`, `501`, `591`, `044`, `067`, `458`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=203`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
