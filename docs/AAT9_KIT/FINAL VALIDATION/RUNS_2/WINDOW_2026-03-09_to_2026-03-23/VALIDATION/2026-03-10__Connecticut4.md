# Analysis Arena Master Validation Run Report — Connecticut4 — D=2026-03-10 (H=2026-03-09)

Purpose
- State-level post-results review packet for the Analysis Arena branch.
- Locks Part A truth inputs, points Parts B-E at the predictive raw tool evidence, and auto-captures Parts F/G/H from the live arena/runtime objects.
- This report is an arena-native working shell. It is not the old summary-driven validation scaffold.

Template / SSOT anchors
- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Aggregated arena contract: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md`
- String-tool arena feed: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- Context-tool arena feed: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- Translation Sandbox companion: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 operating template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Brain 2 Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- Arena system map: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`

Scope
- Results date `D`: `2026-03-10`
- History date `H`: `2026-03-09`
- State: `Connecticut4`
- Predictive sharepack root: `sharepacks/_predictive`
- Predictive state dir: `sharepacks/_predictive/2026-03-10/Connecticut4`
- Truth/frozen sharepack root: `sharepacks`
- Truth state dir: `sharepacks/2026-03-10/Connecticut4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## Part A — Winners Environment Lens

### A0. File Lock And Truth Inputs
- Results file: `data/results/2026-03-10.txt`
- Midday winner: literal `487` | canonical `478`
- Evening winner: literal `556` | canonical `556`
- Truth winners dir: `sharepacks/2026-03-10/Connecticut4/winners/Connecticut4` (missing)
- Winners HTML: _(none found)_
- Winners JSON: _(none found)_

### A1-A7. Analyst Read
- Winning pattern formation: `...`
- Variant behavior / environment class: `...`
- Winner structure class: `...`
- Progression / survivor read: `...`
- VTRAC winner read: `...`
- Pre-system predictive thesis: `...`
- Part A handoff: `a strong predictive system needed to preserve ...`

## Parts B-E — Raw Tool Review Surfaces

These sections remain governed by the arena-era template. This report locks the predictive-side files that should be reviewed for Parts B-E instead of trying to restage the old summary-only shell.

### Stable
- Scores CSV: `sharepacks/_predictive/2026-03-10/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_scores.csv`
- Families CSV: `sharepacks/_predictive/2026-03-10/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_families.csv`
- Compound CSV: `sharepacks/_predictive/2026-03-10/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_compound.csv`
- Metrics JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/stable/Connecticut4/Connecticut4_metrics.json`
- HTML report: `sharepacks/_predictive/2026-03-10/Connecticut4/stable/Connecticut4/Connecticut4_stable_patterns_report.html`

### Digit Reduction
- Scores CSV: `sharepacks/_predictive/2026-03-10/Connecticut4/digit_reduction/Connecticut4/Connecticut4_digit_reduction_scores.csv`
- Report HTML: `sharepacks/_predictive/2026-03-10/Connecticut4/digit_reduction/Connecticut4/Connecticut4_digit_reduction_report.html`
- Stacked report HTML: `sharepacks/_predictive/2026-03-10/Connecticut4/digit_reduction/Connecticut4/Connecticut4_digit_reduction_report_stacked.html`

### VTRAC
- Enhanced JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/vtrac/Connecticut4/Connecticut4_vtrac_enhanced_20260416_183508.json`
- Validation report JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/vtrac/Connecticut4/validation_report.json` (missing)
- Validation report MD: `sharepacks/_predictive/2026-03-10/Connecticut4/vtrac/Connecticut4/validation_report.md` (missing)

### Hot Zones
- Top lanes CSV: `sharepacks/_predictive/2026-03-10/Connecticut4/hot_zones/Connecticut4/Connecticut4_hot_zones_top_lanes.csv`
- Per-lane CSV: `sharepacks/_predictive/2026-03-10/Connecticut4/hot_zones/Connecticut4/Connecticut4_hot_zones_per_lane.csv`
- Meta JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/hot_zones/Connecticut4/Connecticut4_hot_zones_meta.json`
- Winner map JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/hot_zones/Connecticut4/2026-03-10_hot_zones_winner_map.json`

## Part F — Aggregated Analysis Arena

### F0. Arena File Lock And Review Surface
- Aggregated arena JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-10/Connecticut4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/signals_bundle__tool_only__arena_v0.json`
- Review links available: `True`

### F1-F9. Auto-captured arena snapshot
- Dominant canonicals: `168`, `006`, `368`, `668`, `068`, `688`
- Dominant families: `18`, `23`, `21`, `24`, `8`, `25`
- Dominant VTRAC indices: `18`, `23`, `8`, `15`, `21`, `24`
- Context-reinforced canonicals: `168`, `368`, `668`, `068`, `688`, `099`
- Context-only pressure: _none_
- State regime: ``dominant_canonical=168``, ``dominant_family=18``, ``dominant_vtrac_index=18``, ``survivor_pressure=True``, ``last_remaining=False``, ``hidden_terminal_support=True``
- VTRAC literal watchlist: ``18` -> `168,668,366``, ``23` -> `688,336,188,368,133``, ``8` -> `068,018,135``, ``15` -> `599,459,099,445,044``, ``21` -> `678,178,137``
- Stable survivor context: ``frontier_rows=0``, ``progressions=27``, ``last_remaining_rows=0``, ``hidden_terminal_frontiers=27``, ``top_frontier_canonicals=017,013,011,001,006,007``
- R-Consensus context: ``events=2``, ``signal_class=strong``, ``trial_eligible=True``, ``top_tails=06,66``, ``top_support=006,066``
- Arena truth alignment summary: `...`
- Arena added value read: `...`
- Arena judgment / handoff: `...`

## Part G — Context / Aux / Control Center Audit

### G0. Context file lock
- Aux summary JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/aux/Connecticut4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-10/Connecticut4/aux/Connecticut4/summary.md`
- Control Center dir: `sharepacks/_predictive/2026-03-10/control_center`

### G1-G10. Auto-captured context snapshot
- Positional pressure: ``shortlist_count=16``, ``shortlist_top=688,368,668,188,668,268``
- Due doubles / mirror-double family pressure: ``best_draws_since=0``, ``families=-``
- Blackapple context: ``best_status=WATCH``, ``best_score=2``, ``recommended=014,023,068,149,158,167,239,248``
- Profit alerts: ``alert_count=5``, ``top_alerts=Evening:A05:066:STR8_3,Evening:A04:368:BOX,Combined:A12:388:STR8_4of8,Combined:A10:099:STR8_3,Evening:A08:OVERLAY``
- Compound events: ``top_events=Evening:CARRY_PERM:P70,Combined:CLAMP_4:P25``
- Scoreboard carry-through: ``rank=1``, ``role=shared_host``, ``bucket=small_shoulder``, ``tracker=tracker-strong``
- Aux draw sources present: `True`

### G1a. Explicit Aux badge inventory
- Combined pair badges `RED`: `26`[DS=110; sev=red], `13`[DS=85; sev=red], `46`[DS=66; sev=red]
- Combined pair badges `BLUE`: `68`[DS=51; sev=blue], `08`[DS=46; sev=blue], `28`[DS=41; sev=blue]
- Combined pair badges `PURPLE`: `11`[DS=47; sev=purple], `33`[DS=45; sev=purple], `77`[DS=43; sev=purple], `88`[DS=37; sev=purple], `99`[DS=27; sev=purple], `66`[DS=26; sev=purple], `03`[DS=32; sev=purple], `49`[DS=31; sev=purple], `18`[DS=25; sev=purple], `89`[DS=25; sev=purple]
- Midday pair badges `RED`: `26`[DS=72; sev=red]
- Midday pair badges `BLUE`: `66`[DS=78; sev=blue], `13`[DS=42; sev=blue], `16`[DS=40; sev=blue], `08`[DS=38; sev=blue]
- Midday pair badges `PURPLE`: `46`[DS=33; sev=purple], `38`[DS=31; sev=purple], `12`[DS=30; sev=purple], `24`[DS=26; sev=purple], `27`[DS=26; sev=purple], `56`[DS=25; sev=purple]
- Evening pair badges `RED`: `68`[DS=81; sev=red], `04`[DS=56; sev=red]
- Evening pair badges `BLUE`: `26`[DS=55; sev=blue], `13`[DS=52; sev=blue], `36`[DS=41; sev=blue]
- Evening pair badges `PURPLE`: `33`[DS=60; sev=purple], `99`[DS=51; sev=purple], `11`[DS=47; sev=purple], `00`[DS=35; sev=purple], `77`[DS=27; sev=purple], `46`[DS=33; sev=purple], `69`[DS=33; sev=purple], `23`[DS=32; sev=purple], `45`[DS=28; sev=purple], `18`[DS=25; sev=purple]
- Cross-variant pair overlaps: `08`[Combined=blue/DS=46; Midday=blue/DS=38], `11`[Combined=purple/DS=47; Evening=purple/DS=47], `13`[Combined=red/DS=85; Midday=blue/DS=42; Evening=blue/DS=52], `18`[Combined=purple/DS=25; Evening=purple/DS=25], `26`[Combined=red/DS=110; Midday=red/DS=72; Evening=blue/DS=55], `33`[Combined=purple/DS=45; Evening=purple/DS=60], `46`[Combined=red/DS=66; Midday=purple/DS=33; Evening=purple/DS=33], `66`[Combined=purple/DS=26; Midday=blue/DS=78], `68`[Combined=blue/DS=51; Midday=purple/DS=25; Evening=red/DS=81], `77`[Combined=purple/DS=43; Evening=purple/DS=27], `99`[Combined=purple/DS=27; Evening=purple/DS=51]
- Combined boxed combo badges: `888`[DS=835; sev=B], `688`[DS=831; sev=B], `029`[DS=797; sev=B], `269`[DS=777; sev=B], `116`[DS=758; sev=B], `233`[DS=757; sev=B], `338`[DS=687; sev=B]
- Midday boxed combo badges: `117`[DS=946; sev=B], `099`[DS=859; sev=B], `004`[DS=751; sev=B], `155`[DS=747; sev=B], `227`[DS=710; sev=B], `448`[DS=680; sev=B]
- Evening boxed combo badges: `678`[DS=973; sev=B], `668`[DS=970; sev=B], `399`[DS=969; sev=B], `044`[DS=965; sev=B], `145`[DS=934; sev=B], `677`[DS=841; sev=B], `333`[DS=836; sev=B], `112`[DS=788; sev=B], `344`[DS=768; sev=B], `888`[DS=765; sev=B]
- Cross-variant boxed-combo overlaps: `888`[Combined=B/DS=835; Evening=B/DS=765]
- Combined badge-pressure top indices: `21`[PD=2.25; RAW=18], `23`[PD=2.17; RAW=13], `24`[PD=2.00; RAW=16], `18`[PD=2.00; RAW=12], `8`[PD=1.88; RAW=15], `29`[PD=1.67; RAW=10], `22`[PD=1.62; RAW=13], `17`[PD=1.50; RAW=9]
- Midday badge-pressure top indices: `16`[PD=3.00; RAW=6], `18`[PD=2.17; RAW=13], `21`[PD=1.75; RAW=14], `17`[PD=1.67; RAW=10], `8`[PD=1.50; RAW=12], `26`[PD=1.50; RAW=3], `22`[PD=1.38; RAW=11], `6`[PD=1.33; RAW=8]
- Evening badge-pressure top indices: `21`[PD=2.38; RAW=19], `18`[PD=2.33; RAW=14], `23`[PD=2.33; RAW=14], `24`[PD=2.25; RAW=18], `8`[PD=2.00; RAW=16], `15`[PD=2.00; RAW=12], `9`[PD=1.75; RAW=14], `5`[PD=1.33; RAW=8]

### G1b. Explicit due VTRAC inventory
- Combined due VTRAC overlay: `35`[DS=202], `26`[DS=155], `1`[DS=140], `18`[DS=128], `23`[DS=120], `17`[DS=106], `19`[DS=68], `27`[DS=64]
- Combined due VTRAC heatboard: `35`[DS=202; HZ=0.019; TR=6; AVG=53.286], `26`[DS=155; HZ=0.008; TR=1; AVG=123.167], `1`[DS=140; HZ=0.011; TR=7; AVG=91.333], `18`[DS=128; HZ=0.024; TR=16; AVG=42.400], `23`[DS=120; HZ=0.031; TR=25; AVG=32.000], `17`[DS=106; HZ=0.024; TR=17; AVG=42.000], `19`[DS=68; HZ=0.024; TR=16; AVG=42.045], `27`[DS=64; HZ=0.021; TR=15; AVG=47.526]
- Midday due VTRAC overlay: `16`[DS=268], `25`[DS=169], `18`[DS=153], `35`[DS=110], `1`[DS=91], `23`[DS=86], `26`[DS=77], `17`[DS=70]
- Midday due VTRAC heatboard: `16`[DS=268; HZ=0.009; TR=3; AVG=116.750], `25`[DS=169; HZ=0.024; TR=17; AVG=42.421], `18`[DS=153; HZ=0.027; TR=21; AVG=36.522], `35`[DS=110; HZ=0.013; TR=4; AVG=79.000], `1`[DS=91; HZ=0.013; TR=6; AVG=76.000], `23`[DS=86; HZ=0.030; TR=25; AVG=33.000], `26`[DS=77; HZ=0.005; TR=2; AVG=182.750], `17`[DS=70; HZ=0.031; TR=23; AVG=32.444]
- Evening due VTRAC overlay: `26`[DS=207], `34`[DS=159], `32`[DS=152], `35`[DS=101], `1`[DS=70], `18`[DS=64], `23`[DS=60], `17`[DS=53]
- Evening due VTRAC heatboard: `26`[DS=207; HZ=0.009; TR=2; AVG=115.200], `34`[DS=159; HZ=0.017; TR=8; AVG=57.857], `32`[DS=152; HZ=0.008; TR=2; AVG=118.333], `35`[DS=101; HZ=0.018; TR=11; AVG=56.545], `1`[DS=70; HZ=0.010; TR=0; AVG=102.111], `18`[DS=64; HZ=0.025; TR=19; AVG=40.261], `23`[DS=60; HZ=0.020; TR=13; AVG=49.053], `17`[DS=53; HZ=0.026; TR=19; AVG=39.130]
- Context reinforcement vs context-only pressure: `...`
- Policy relationship / handoff: `...`

## Part H — Translation Sandbox / Downstream Control Arm

### H0. File lock
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-10/Connecticut4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-10/Connecticut4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-10/Connecticut4/play_card__tool_only__arena_v0.md`

### H1. Auto-captured control-arm snapshot
- Candidate Universe summary: `packs=27` | `union_combos=203`
- Play Card summary: `analysis_prefix`[B12,B24,B36], `convergence_box_first`[B12,B24,B36], `conversion_box_first`[B12,B24,B36], `conversion_box_first_conditional_lenient_presetA`[B12,B24,B36]
- Translation Sandbox positional shortlist top: `688`, `368`, `668`, `188`, `268`, `168`, `468`
- Translation Sandbox BA canonicals: `014`, `023`, `068`, `149`, `158`, `167`, `239`, `248`
- Translation Sandbox profit canonicals: `368`, `066`, `099`, `338`, `388`, `888`
- Diagnostic boxed seed: `368`, `099`, `168`, `688`, `668`, `068`, `006`, `066`, `388`, `188`, `017`, `013`, `011`, `001`, `689`, `468`
- Diagnostic straight seed: `688`, `638`, `618`, `668`, `188`, `686`, `682`, `684`, `099`, `909`, `990`, `186`, `681`, `599`, `959`, `995`
- Diagnostic VT-box seed: `23`, `15`, `2`, `18`, `8`, `21`, `17`, `6`, `25`, `32`, `None`, `9`
- Translation-learning capture: `...`
- Control-arm comparison / bounded handoff: `...`

## Part I — Final State-Level Learning

- Strongest truth-side clue: `...`
- Strongest Brain 1 preservation win: `...`
- Strongest context/Brain 2 handoff clue: `...`
- Strongest conversion/control-arm gap: `...`
- Fix-now vs fix-later: `...`
- Translation Sandbox companion needed?: `yes/no`
- Brain 2 handoff: `...`
