# Analysis Arena Predictive Run Report — Connecticut4 — D=2026-03-22 (H=2026-03-21)

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
- Results date `D`: `2026-03-22`
- History date `H`: `2026-03-21`
- State: `Connecticut4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-22/Connecticut4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-22/Connecticut4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-22/Connecticut4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-22/Connecticut4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-22/Connecticut4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-22/Connecticut4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-22/Connecticut4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-22/Connecticut4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-22/Connecticut4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-22/Connecticut4/aux/Connecticut4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-22/Connecticut4/aux/Connecticut4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-22/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-22/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-22/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-22/Connecticut4/digit_reduction/Connecticut4/Connecticut4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-22/Connecticut4/digit_reduction/Connecticut4/Connecticut4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-22/Connecticut4/vtrac/Connecticut4/Connecticut4_vtrac_enhanced_20260416_192842.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-22/Connecticut4/hot_zones/Connecticut4/Connecticut4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `113`, `224`, `003`, `225`, `355`, `255`
- Dominant families: `225`, `18`, `255`, `559`, `23`, `30`
- Dominant VTRAC indices: `18`, `4`, `28`, `19`, `10`, `23`
- Context-reinforced canonicals: `113`, `355`, `123`, `112`, `117`, `223`
- Context-only pressure: `099`
- State regime: `dominant_canonical=113`, `dominant_family=225`, `dominant_vtrac_index=18`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=004,001,011,007,005,133`
- R-Consensus context: `available=false`
- VTRAC literal watchlist: `18->113,366,136,118,668`, `4->355,003,035,058`, `28->224`, `19->114,146,466,169`, `10->225,257`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=1`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `113`, `224`, `003`, `225`
- Scoreboard top VTRAC indices: `18`, `4`, `28`, `19`
- Positional shortlist top: `123`, `113`, `112`, `223`, `133`, `238`, `111`, `125`
- Blackapple recommended canonicals: `015`, `016`, `025`, `027`, `035`, `038`, `045`, `049`
- Profit-alert implied canonicals: `136`, `113`, `099`, `035`, `058`, `355`, `558`
- Due-double family pressure: `Combined:5:0/5-4/9,1/6-2/7,1/6`, `Evening:4:0/5-4/9,1/6-2/7,1/6`, `Midday:2:0/5-4/9,1/6-2/7,1/6`
- Due-double example canonicals: `099`, `044`, `004`, `117`, `677`, `112`, `177`, `116`
- Top profit alerts: `Evening:A04:136:BOX`, `Evening:A05:113:STR8_3`, `Evening:A08:OVERLAY`, `Midday:A08:OVERLAY`, `Midday:A12:355:STR8_4of8`
- Top compound events: `Evening:CARRY_PERM:P70`, `Midday:CLAMP_4:P25`
- Diagnostic boxed seed: `113`, `112`, `099`, `136`, `123`, `355`, `004`, `133`, `116`, `003`, `118`, `668`, `001`, `011`, `007`, `117`
- Diagnostic straight seed: `113`, `211`, `213`, `223`, `313`, `283`, `111`, `215`, `099`, `909`, `990`, `116`, `161`, `611`, `136`, `163`
- Diagnostic VT-box seed: `18`, `15`, `4`, `19`, `10`, `23`, `3`, `2`, `28`, `6`, `21`, `33`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `113`, `224`, `003`, `225`, `355`, `123`, `112`, `099`, `136`, `004`, `133`
- Arena-preserved straight canonicals to watch: `113`, `211`, `213`, `223`, `313`, `283`, `111`, `215`, `355`, `123`, `112`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=197`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
