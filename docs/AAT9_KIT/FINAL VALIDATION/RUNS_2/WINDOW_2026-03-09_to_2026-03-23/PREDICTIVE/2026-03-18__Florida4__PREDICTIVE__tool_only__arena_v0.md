# Analysis Arena Predictive Run Report — Florida4 — D=2026-03-18 (H=2026-03-17)

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
- Results date `D`: `2026-03-18`
- History date `H`: `2026-03-17`
- State: `Florida4`
- Predictive sharepacks root: `sharepacks/_predictive`
- State sharepack dir: `sharepacks/_predictive/2026-03-18/Florida4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## File Lock

- Aggregated arena JSON: `sharepacks/_predictive/2026-03-18/Florida4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-18/Florida4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-18/Florida4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-18/Florida4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-18/Florida4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-18/Florida4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-18/Florida4/play_card__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-18/Florida4/signals_bundle__tool_only__arena_v0.json`
- Aux summary JSON: `sharepacks/_predictive/2026-03-18/Florida4/aux/Florida4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-18/Florida4/aux/Florida4/summary.md`

## Raw Tool Review Surfaces

- Stable scores CSV: `sharepacks/_predictive/2026-03-18/Florida4/stable/Florida4/Florida4_stable_patterns_scores.csv`
- Stable families CSV: `sharepacks/_predictive/2026-03-18/Florida4/stable/Florida4/Florida4_stable_patterns_families.csv`
- Stable report HTML: `sharepacks/_predictive/2026-03-18/Florida4/stable/Florida4/Florida4_stable_patterns_report.html`
- Digit Reduction scores CSV: `sharepacks/_predictive/2026-03-18/Florida4/digit_reduction/Florida4/Florida4_digit_reduction_scores.csv`
- Digit Reduction report HTML: `sharepacks/_predictive/2026-03-18/Florida4/digit_reduction/Florida4/Florida4_digit_reduction_report.html`
- VTRAC enhanced JSON: `sharepacks/_predictive/2026-03-18/Florida4/vtrac/Florida4/Florida4_vtrac_enhanced_20260416_191113.json`
- Hot Zones top lanes CSV: `sharepacks/_predictive/2026-03-18/Florida4/hot_zones/Florida4/Florida4_hot_zones_top_lanes.csv`

## Brain 1 — Aggregated Analysis Arena Snapshot

- Dominant canonicals: `006`, `224`, `114`, `255`, `124`, `246`
- Dominant families: `17`, `19`, `18`, `22`, `6`, `255`
- Dominant VTRAC indices: `19`, `28`, `2`, `22`, `3`, `18`
- Context-reinforced canonicals: `006`, `224`, `025`, `668`
- Context-only pressure: _none_
- State regime: `dominant_canonical=006`, `dominant_family=17`, `dominant_vtrac_index=19`, `survivor_pressure=True`, `last_remaining=False`, `hidden_terminal_support=True`
- Stable survivor context: `frontier_rows=0`, `progressions=27`, `last_remaining_rows=0`, `hidden_terminal_frontiers=27`, `top_frontier_canonicals=006,007,004,005,017,114`
- R-Consensus context: `events=1`, `signal_class=moderate`, `trial_eligible=True`, `top_tails=06`, `top_support=006`
- VTRAC literal watchlist: `19->466,114,669,146`, `28->224,477`, `2->006`, `22->246,124,467`, `3->002,025,255,007`

## Brain 2 Carry-Through / Translation Sandbox

- Scoreboard row: `rank=3`, `role=shared_host`, `bucket=small_shoulder`, `tracker=tracker-strong`
- Scoreboard top canonicals: `006`, `224`, `114`, `255`
- Scoreboard top VTRAC indices: `19`, `28`, `2`, `22`
- Positional shortlist top: `267`, `127`, `467`, `147`, `268`, `128`, `667`, `167`
- Blackapple recommended canonicals: `012`, `017`, `023`, `024`, `025`, `026`, `027`, `028`
- Profit-alert implied canonicals: `025`, `224`, `013`, `018`, `036`, `068`, `135`, `158`, `356`, `568`, `001`, `006`
- Due-double family pressure: `Combined:2:0/5-4/9,1/6-3/8,0/5-1/6`, `Evening:1:0/5-4/9,1/6-3/8,0/5-1/6`, `Midday:2:0/5-4/9,1/6-3/8,0/5-1/6`
- Due-double example canonicals: `009`, `455`, `118`, `133`, `668`, `366`, `011`, `566`
- Top profit alerts: `Combined:A09:STR8_8`, `Combined:A05:224:STR8_3`, `Evening:A04:025:BOX`, `Evening:A12:006:STR8_4of8`
- Top compound events: `Evening:CLAMP_4:P25`
- Diagnostic boxed seed: `006`, `224`, `025`, `668`, `026`, `118`, `114`, `007`, `004`, `005`, `017`, `001`, `267`, `127`, `667`, `009`
- Diagnostic straight seed: `627`, `127`, `667`, `647`, `147`, `628`, `128`, `167`, `003`, `030`, `300`, `118`, `181`, `811`, `122`, `622`
- Diagnostic VT-box seed: `19`, `28`, `2`, `3`, `17`, `23`, `12`, `22`, `8`, `18`, `10`, `20`

## Arena-Preserved Truth vs Control-Arm Expression

- Arena-preserved boxed canonicals to watch: `006`, `224`, `114`, `255`, `025`, `668`, `026`, `118`, `007`
- Arena-preserved straight canonicals to watch: `627`, `127`, `667`, `647`, `147`, `628`, `128`, `167`, `006`, `224`, `025`, `668`
- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results.
- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth.
- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below.

## Downstream Control Arm Snapshot

- Candidate Universe: `packs=27`, `union_combos=218`, `contains_winners_artifacts=False`
- Play Card: `analysis_prefix[B12,B24,B36]`, `convergence_box_first[B12,B24,B36]`, `conversion_box_first[B12,B24,B36]`, `conversion_box_first_conditional_lenient_presetA[B12,B24,B36]`

## Analyst Notes

- Strongest Brain 1 state thesis: `...`
- Strongest context reinforcement or tracker carry-through: `...`
- Is this state more boxed, straight, or VT-box leaning?: `...`
- What did the arena preserve that the control arm may compress later?: `...`
- Any anomalies, missing artifacts, or drift to check before results?: `...`
