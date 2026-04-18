# Analysis Arena Predictive Run Report — Pennsylvania4 — D=2026-01-09 (H=2026-01-08)

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
- Results date `D`: `2026-01-09`
- History date `H`: `2026-01-08`
- State: `Pennsylvania4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-01-09/Pennsylvania4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-01-09/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-09/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-09/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-09/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-09/Pennsylvania4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-09/Pennsylvania4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-09/Pennsylvania4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-09/Pennsylvania4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-01-09/Pennsylvania4/aux/Pennsylvania4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-09/Pennsylvania4/aux/Pennsylvania4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-01-09/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-01-09/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-01-09/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-01-09/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-01-09/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-01-09/Pennsylvania4/vtrac/Pennsylvania4/Pennsylvania4_vtrac_enhanced_20260326_045516.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-01-09/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `445`, `019`, `009`, `113`, `455`, `559`
- Dominant families: `299`, `559`, `18`, `24`, `229`, `19`
- Dominant VTRAC indices: `5`, `9`, `18`, `15`, `19`, `31`
- Context-reinforced canonicals: `445`, `019`, `009`, `559`, `014`
- Context-only pressure: _none_
- State regime: `dominant_canonical=445`, `dominant_family=299`, `dominant_vtrac_index=5`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=118,113,114,119,009,117`
- R-Consensus context: `events=1`, `signal_class=moderate`, `trial_eligible=True`, `top_tails=09`, `top_support=009`
- VTRAC literal watchlist: `5->009,455,559,059`, `9->019,014,456,569,159`, `18->118,113,668`, `15->599,445`, `19->119,114`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=11`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-rich`
- Scoreboard top canonicals: `445`, `019`, `009`, `113`
- Scoreboard top VTRAC indices: `5`, `9`, `18`, `15`
- Positional shortlist top: `145`, `459`, `148`, `124`, `158`, `345`, `134`, `146`
- Blackapple recommended canonicals: `012`, `013`, `014`, `015`, `016`, `017`, `018`, `019`
- Profit-alert implied canonicals: `019`, `009`, `066`
- Due-double family pressure: `Combined:3:3/8-4/9,0/5-2/7,2/7-3/8`, `Evening:2:3/8-4/9,0/5-2/7,2/7-3/8`, `Midday:1:3/8-4/9,0/5-2/7,2/7-3/8`
- Due-double example canonicals: `448`, `399`, `344`, `339`, `255`, `007`, `228`, `788`
- Top profit alerts: `Midday:A04:019:BOX`, `Midday:A05:009:STR8_3`, `Midday:A08:OVERLAY`, `Combined:A10:066:STR8_3`
- Top compound events: `Midday:CARRY_PERM:P70`
- Diagnostic boxed seed: `019`, `009`, `445`, `014`, `066`, `007`, `113`, `559`, `059`, `118`, `114`, `119`, `015`, `146`, `255`, `228`
- Diagnostic straight seed: `416`, `415`, `495`, `418`, `412`, `815`, `435`, `413`, `007`, `070`, `700`, `445`, `019`, `112`, `121`, `211`
- Diagnostic VT-box seed: `5`, `34`, `9`, `18`, `15`, `19`, `23`, `10`, `6`, `7`, `8`, `2`

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=211`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
