# Analysis Arena Master Validation Run Report — Pennsylvania4 — D=2026-03-12 (H=2026-03-11)

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
- Results date `D`: `2026-03-12`
- History date `H`: `2026-03-11`
- State: `Pennsylvania4`
- Predictive sharepack root: `sharepacks/_predictive`
- Predictive state dir: `sharepacks/_predictive/2026-03-12/Pennsylvania4`
- Truth/frozen sharepack root: `sharepacks`
- Truth state dir: `sharepacks/2026-03-12/Pennsylvania4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## Part A — Winners Environment Lens

### A0. File Lock And Truth Inputs
- Results file: `data/results/2026-03-12.txt`
- Midday winner: literal `732` | canonical `237`
- Evening winner: literal `052` | canonical `025`
- Truth winners dir: `sharepacks/2026-03-12/Pennsylvania4/winners/Pennsylvania4` (missing)
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
- Scores CSV: `sharepacks/_predictive/2026-03-12/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_scores.csv`
- Families CSV: `sharepacks/_predictive/2026-03-12/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_families.csv`
- Compound CSV: `sharepacks/_predictive/2026-03-12/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_compound.csv`
- Metrics JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_metrics.json`
- HTML report: `sharepacks/_predictive/2026-03-12/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_report.html`

### Digit Reduction
- Scores CSV: `sharepacks/_predictive/2026-03-12/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_scores.csv`
- Report HTML: `sharepacks/_predictive/2026-03-12/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report.html`
- Stacked report HTML: `sharepacks/_predictive/2026-03-12/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report_stacked.html`

### VTRAC
- Enhanced JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/vtrac/Pennsylvania4/Pennsylvania4_vtrac_enhanced_20260416_184455.json`
- Validation report JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/vtrac/Pennsylvania4/validation_report.json` (missing)
- Validation report MD: `sharepacks/_predictive/2026-03-12/Pennsylvania4/vtrac/Pennsylvania4/validation_report.md` (missing)

### Hot Zones
- Top lanes CSV: `sharepacks/_predictive/2026-03-12/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_top_lanes.csv`
- Per-lane CSV: `sharepacks/_predictive/2026-03-12/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_per_lane.csv`
- Meta JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_meta.json`
- Winner map JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/hot_zones/Pennsylvania4/2026-03-12_hot_zones_winner_map.json`

## Part F — Aggregated Analysis Arena

### F0. Arena File Lock And Review Surface
- Aggregated arena JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-12/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/signals_bundle__tool_only__arena_v0.json`
- Review links available: `True`

### F1-F9. Auto-captured arena snapshot
- Dominant canonicals: `559`, `233`, `224`, `259`, `002`, `005`
- Dominant families: `259`, `29`, `229`, `12`, `3`, `5`
- Dominant VTRAC indices: `29`, `5`, `12`, `28`, `3`, `1`
- Context-reinforced canonicals: `005`, `008`, `238`, `024`, `258`, `255`
- Context-only pressure: `158`
- State regime: ``dominant_canonical=559``, ``dominant_family=259``, ``dominant_vtrac_index=29``, ``survivor_pressure=True``, ``last_remaining=False``, ``hidden_terminal_support=True``
- VTRAC literal watchlist: ``29` -> `233,337,238,378``, ``5` -> `559,004``, ``12` -> `259,024``, ``28` -> `224,229``, ``3` -> `255,002``
- Stable survivor context: ``frontier_rows=0``, ``progressions=27``, ``last_remaining_rows=0``, ``hidden_terminal_frontiers=27``, ``top_frontier_canonicals=005,007,001,004,009,008``
- R-Consensus context: ``events=2``, ``signal_class=strong``, ``trial_eligible=True``, ``top_tails=05,03``, ``top_support=005,003``
- Arena truth alignment summary: `...`
- Arena added value read: `...`
- Arena judgment / handoff: `...`

## Part G — Context / Aux / Control Center Audit

### G0. Context file lock
- Aux summary JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/aux/Pennsylvania4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-12/Pennsylvania4/aux/Pennsylvania4/summary.md`
- Control Center dir: `sharepacks/_predictive/2026-03-12/control_center`

### G1-G10. Auto-captured context snapshot
- Positional pressure: ``shortlist_count=16``, ``shortlist_top=158,458,157,558,457,557``
- Due doubles / mirror-double family pressure: ``best_draws_since=0``, ``families=-``
- Blackapple context: ``best_status=WATCH``, ``best_score=2``, ``recommended=034,349,358,367,016,025,079,124``
- Profit alerts: ``alert_count=3``, ``top_alerts=Midday:A05:005:STR8_3,Combined:A04:238:BOX,Evening:A08:OVERLAY``
- Compound events: ``top_events=-``
- Scoreboard carry-through: ``rank=11``, ``role=shared_host``, ``bucket=small_shoulder``, ``tracker=tracker-strong``
- Aux draw sources present: `True`

### G1a. Explicit Aux badge inventory
- Combined pair badges `RED`: `38`[DS=64; sev=red]
- Combined pair badges `BLUE`: `22`[DS=90; sev=blue], `33`[DS=84; sev=blue], `02`[DS=52; sev=blue], `05`[DS=52; sev=blue], `12`[DS=51; sev=blue], `06`[DS=45; sev=blue], `25`[DS=37; sev=blue]
- Combined pair badges `PURPLE`: `55`[DS=66; sev=purple], `99`[DS=57; sev=purple], `88`[DS=46; sev=purple], `26`[DS=34; sev=purple], `49`[DS=33; sev=purple], `78`[DS=31; sev=purple], `47`[DS=29; sev=purple]
- Midday pair badges `RED`: `33`[DS=138; sev=red], `38`[DS=84; sev=red]
- Midday pair badges `BLUE`: `18`[DS=45; sev=blue], `26`[DS=42; sev=blue], `02`[DS=39; sev=blue], `03`[DS=38; sev=blue]
- Midday pair badges `PURPLE`: `22`[DS=69; sev=purple], `55`[DS=60; sev=purple], `88`[DS=49; sev=purple], `99`[DS=28; sev=purple], `11`[DS=27; sev=purple], `08`[DS=34; sev=purple], `05`[DS=33; sev=purple], `57`[DS=30; sev=purple], `27`[DS=26; sev=purple], `12`[DS=25; sev=purple]
- Evening pair badges `BLUE`: `06`[DS=48; sev=blue], `29`[DS=46; sev=blue], `24`[DS=43; sev=blue]
- Evening pair badges `PURPLE`: `99`[DS=67; sev=purple], `22`[DS=45; sev=purple], `33`[DS=42; sev=purple], `55`[DS=33; sev=purple], `38`[DS=32; sev=purple], `47`[DS=31; sev=purple], `58`[DS=30; sev=purple], `12`[DS=28; sev=purple], `49`[DS=27; sev=purple], `02`[DS=26; sev=purple], `05`[DS=26; sev=purple]
- Cross-variant pair overlaps: `02`[Combined=blue/DS=52; Midday=blue/DS=39; Evening=purple/DS=26], `05`[Combined=blue/DS=52; Midday=purple/DS=33; Evening=purple/DS=26], `06`[Combined=blue/DS=45; Evening=blue/DS=48], `12`[Combined=blue/DS=51; Midday=purple/DS=25; Evening=purple/DS=28], `22`[Combined=blue/DS=90; Midday=purple/DS=69; Evening=purple/DS=45], `25`[Combined=blue/DS=37; Evening=purple/DS=26], `26`[Combined=purple/DS=34; Midday=blue/DS=42], `33`[Combined=blue/DS=84; Midday=red/DS=138; Evening=purple/DS=42], `38`[Combined=red/DS=64; Midday=red/DS=84; Evening=purple/DS=32], `47`[Combined=purple/DS=29; Evening=purple/DS=31], `49`[Combined=purple/DS=33; Evening=purple/DS=27], `55`[Combined=purple/DS=66; Midday=purple/DS=60; Evening=purple/DS=33]
- Combined boxed combo badges: `088`[DS=981; sev=B], `008`[DS=959; sev=B], `355`[DS=900; sev=B], `788`[DS=793; sev=B], `266`[DS=782; sev=B], `111`[DS=777; sev=B], `339`[DS=771; sev=B], `225`[DS=767; sev=B], `333`[DS=747; sev=B], `113`[DS=733; sev=B]
- Midday boxed combo badges: `668`[DS=986; sev=B], `199`[DS=934; sev=B], `499`[DS=860; sev=B], `399`[DS=843; sev=B], `039`[DS=831; sev=B], `448`[DS=820; sev=B], `005`[DS=812; sev=B], `222`[DS=811; sev=B], `066`[DS=809; sev=B], `599`[DS=699; sev=B]
- Evening boxed combo badges: `255`[DS=958; sev=B], `138`[DS=898; sev=B], `117`[DS=881; sev=B], `158`[DS=843; sev=B], `199`[DS=827; sev=B], `112`[DS=787; sev=B], `277`[DS=772; sev=B], `339`[DS=768; sev=B], `155`[DS=757; sev=B], `999`[DS=746; sev=B]
- Cross-variant boxed-combo overlaps: `005`[Combined=B/DS=680; Midday=B/DS=812], `088`[Combined=B/DS=981; Evening=B/DS=679], `199`[Midday=B/DS=934; Evening=B/DS=827], `339`[Combined=B/DS=771; Evening=B/DS=768], `388`[Combined=B/DS=675; Evening=B/DS=686]
- Combined badge-pressure top indices: `32`[PD=3.00; RAW=6], `23`[PD=2.50; RAW=15], `1`[PD=2.50; RAW=5], `3`[PD=2.17; RAW=13], `13`[PD=2.17; RAW=13], `29`[PD=2.17; RAW=13], `33`[PD=2.17; RAW=13], `26`[PD=2.00; RAW=4]
- Midday badge-pressure top indices: `29`[PD=3.00; RAW=18], `32`[PD=3.00; RAW=6], `23`[PD=2.33; RAW=14], `33`[PD=2.33; RAW=14], `13`[PD=2.00; RAW=12], `26`[PD=2.00; RAW=4], `3`[PD=1.50; RAW=9], `5`[PD=1.50; RAW=9]
- Evening badge-pressure top indices: `32`[PD=2.50; RAW=5], `28`[PD=2.17; RAW=13], `30`[PD=1.75; RAW=14], `31`[PD=1.67; RAW=10], `12`[PD=1.50; RAW=12], `2`[PD=1.33; RAW=8], `3`[PD=1.33; RAW=8], `29`[PD=1.33; RAW=8]

### G1b. Explicit due VTRAC inventory
- Combined due VTRAC overlay: `32`[DS=419], `26`[DS=376], `35`[DS=150], `2`[DS=121], `1`[DS=112], `33`[DS=99], `13`[DS=84], `29`[DS=76]
- Combined due VTRAC heatboard: `32`[DS=419; HZ=0.007; TR=1; AVG=135.500], `26`[DS=376; HZ=0.004; TR=-1; AVG=256.500], `35`[DS=150; HZ=0.007; TR=0; AVG=138.000], `2`[DS=121; HZ=0.036; TR=27; AVG=28.097], `1`[DS=112; HZ=0.005; TR=1; AVG=186.750], `33`[DS=99; HZ=0.028; TR=22; AVG=35.500], `13`[DS=84; HZ=0.025; TR=20; AVG=40.773], `29`[DS=76; HZ=0.022; TR=14; AVG=46.050]
- Midday due VTRAC overlay: `26`[DS=444], `1`[DS=429], `16`[DS=241], `32`[DS=209], `35`[DS=186], `29`[DS=90], `23`[DS=85], `4`[DS=80]
- Midday due VTRAC heatboard: `26`[DS=444; HZ=0.000; TR=0], `1`[DS=429; HZ=0.009; TR=0; AVG=109.600], `16`[DS=241; HZ=0.008; TR=-5; AVG=128.400], `32`[DS=209; HZ=0.007; TR=2; AVG=148.800], `35`[DS=186; HZ=0.003; TR=1; AVG=366.500], `29`[DS=90; HZ=0.022; TR=18; AVG=44.600], `23`[DS=85; HZ=0.034; TR=28; AVG=29.767], `4`[DS=80; HZ=0.022; TR=14; AVG=45.900]
- Evening due VTRAC overlay: `32`[DS=686], `26`[DS=188], `33`[DS=119], `11`[DS=103], `17`[DS=94], `31`[DS=91], `35`[DS=75], `20`[DS=70]
- Evening due VTRAC heatboard: `32`[DS=686; HZ=0.003; TR=0; AVG=306.000], `26`[DS=188; HZ=0.006; TR=1; AVG=176.500], `33`[DS=119; HZ=0.022; TR=12; AVG=45.167], `11`[DS=103; HZ=0.045; TR=40; AVG=22.125], `17`[DS=94; HZ=0.028; TR=24; AVG=35.333], `31`[DS=91; HZ=0.030; TR=26; AVG=33.885], `35`[DS=75; HZ=0.011; TR=2; AVG=87.625], `20`[DS=70; HZ=0.029; TR=25; AVG=34.259]
- Context reinforcement vs context-only pressure: `...`
- Policy relationship / handoff: `...`

## Part H — Translation Sandbox / Downstream Control Arm

### H0. File lock
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-12/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-12/Pennsylvania4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-12/Pennsylvania4/play_card__tool_only__arena_v0.md`

### H1. Auto-captured control-arm snapshot
- Candidate Universe summary: `packs=27` | `union_combos=198`
- Play Card summary: `analysis_prefix`[B12,B24,B36], `convergence_box_first`[B12,B24,B36], `conversion_box_first`[B12,B24,B36], `conversion_box_first_conditional_lenient_presetA`[B12,B24,B36]
- Translation Sandbox positional shortlist top: `158`, `458`, `157`, `558`, `457`, `557`, `258`, `358`
- Translation Sandbox BA canonicals: `034`, `349`, `358`, `367`, `016`, `025`, `079`, `124`
- Translation Sandbox profit canonicals: `238`, `005`
- Diagnostic boxed seed: `005`, `238`, `007`, `002`, `008`, `258`, `358`, `557`, `004`, `001`, `024`, `255`, `009`, `559`, `233`, `224`
- Diagnostic straight seed: `575`, `583`, `581`, `584`, `571`, `585`, `574`, `582`, `007`, `070`, `700`, `238`, `283`, `832`, `002`, `020`
- Diagnostic VT-box seed: `1`, `29`, `3`, `5`, `12`, `23`, `21`, `28`, `8`, `14`, `34`, `13`
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
