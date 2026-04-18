# Analysis Arena Master Validation Run Report — Pennsylvania4 — D=2026-03-10 (H=2026-03-09)

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
- State: `Pennsylvania4`
- Predictive sharepack root: `sharepacks/_predictive`
- Predictive state dir: `sharepacks/_predictive/2026-03-10/Pennsylvania4`
- Truth/frozen sharepack root: `sharepacks`
- Truth state dir: `sharepacks/2026-03-10/Pennsylvania4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## Part A — Winners Environment Lens

### A0. File Lock And Truth Inputs
- Results file: `data/results/2026-03-10.txt`
- Midday winner: literal `458` | canonical `458`
- Evening winner: literal `108` | canonical `018`
- Truth winners dir: `sharepacks/2026-03-10/Pennsylvania4/winners/Pennsylvania4` (missing)
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
- Scores CSV: `sharepacks/_predictive/2026-03-10/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_scores.csv`
- Families CSV: `sharepacks/_predictive/2026-03-10/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_families.csv`
- Compound CSV: `sharepacks/_predictive/2026-03-10/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_compound.csv`
- Metrics JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_metrics.json`
- HTML report: `sharepacks/_predictive/2026-03-10/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_report.html`

### Digit Reduction
- Scores CSV: `sharepacks/_predictive/2026-03-10/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_scores.csv`
- Report HTML: `sharepacks/_predictive/2026-03-10/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report.html`
- Stacked report HTML: `sharepacks/_predictive/2026-03-10/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report_stacked.html`

### VTRAC
- Enhanced JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/vtrac/Pennsylvania4/Pennsylvania4_vtrac_enhanced_20260416_183549.json`
- Validation report JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/vtrac/Pennsylvania4/validation_report.json` (missing)
- Validation report MD: `sharepacks/_predictive/2026-03-10/Pennsylvania4/vtrac/Pennsylvania4/validation_report.md` (missing)

### Hot Zones
- Top lanes CSV: `sharepacks/_predictive/2026-03-10/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_top_lanes.csv`
- Per-lane CSV: `sharepacks/_predictive/2026-03-10/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_per_lane.csv`
- Meta JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_meta.json`
- Winner map JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/hot_zones/Pennsylvania4/2026-03-10_hot_zones_winner_map.json`

## Part F — Aggregated Analysis Arena

### F0. Arena File Lock And Review Surface
- Aggregated arena JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-10/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/signals_bundle__tool_only__arena_v0.json`
- Review links available: `True`

### F1-F9. Auto-captured arena snapshot
- Dominant canonicals: `559`, `008`, `024`, `002`, `224`, `288`
- Dominant families: `3`, `12`, `4`, `1`, `225`, `5`
- Dominant VTRAC indices: `5`, `4`, `3`, `12`, `1`, `32`
- Context-reinforced canonicals: `559`, `008`, `024`, `288`, `058`, `059`
- Context-only pressure: _none_
- State regime: ``dominant_canonical=559``, ``dominant_family=3``, ``dominant_vtrac_index=5``, ``survivor_pressure=True``, ``last_remaining=False``, ``hidden_terminal_support=True``
- VTRAC literal watchlist: ``5` -> `559,059,004,009``, ``4` -> `558,008,003,058,355``, ``3` -> `255,007,002,025,057``, ``12` -> `259,024,245``, ``1` -> `055,005``
- Stable survivor context: ``frontier_rows=0``, ``progressions=27``, ``last_remaining_rows=0``, ``hidden_terminal_frontiers=27``, ``top_frontier_canonicals=005,007,009,001,008,004``
- R-Consensus context: ``events=2``, ``signal_class=strong``, ``trial_eligible=True``, ``top_tails=24``, ``top_support=024``
- Arena truth alignment summary: `...`
- Arena added value read: `...`
- Arena judgment / handoff: `...`

## Part G — Context / Aux / Control Center Audit

### G0. Context file lock
- Aux summary JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/aux/Pennsylvania4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-10/Pennsylvania4/aux/Pennsylvania4/summary.md`
- Control Center dir: `sharepacks/_predictive/2026-03-10/control_center`

### G1-G10. Auto-captured context snapshot
- Positional pressure: ``shortlist_count=16``, ``shortlist_top=588,589,558,158,258,458``
- Due doubles / mirror-double family pressure: ``best_draws_since=0``, ``families=-``
- Blackapple context: ``best_status=WATCH``, ``best_score=2``, ``recommended=025,034,124,178,259,268,349,358``
- Profit alerts: ``alert_count=4``, ``top_alerts=Midday:A05:559:STR8_3,Evening:A04:024:BOX,Combined:A08:OVERLAY,Evening:A08:OVERLAY``
- Compound events: ``top_events=-``
- Scoreboard carry-through: ``rank=11``, ``role=shared_host``, ``bucket=small_shoulder``, ``tracker=tracker-strong``
- Aux draw sources present: `True`

### G1a. Explicit Aux badge inventory
- Combined pair badges `RED`: `08`[DS=65; sev=red], `38`[DS=60; sev=red], `57`[DS=57; sev=red], `58`[DS=56; sev=red]
- Combined pair badges `BLUE`: `22`[DS=86; sev=blue], `33`[DS=80; sev=blue], `29`[DS=49; sev=blue], `02`[DS=48; sev=blue], `05`[DS=48; sev=blue], `12`[DS=47; sev=blue], `28`[DS=46; sev=blue], `06`[DS=41; sev=blue]
- Combined pair badges `PURPLE`: `55`[DS=62; sev=purple], `99`[DS=53; sev=purple], `88`[DS=42; sev=purple]
- Midday pair badges `RED`: `33`[DS=136; sev=red], `38`[DS=82; sev=red], `58`[DS=56; sev=red]
- Midday pair badges `BLUE`: `28`[DS=48; sev=blue], `18`[DS=43; sev=blue], `26`[DS=40; sev=blue], `02`[DS=37; sev=blue]
- Midday pair badges `PURPLE`: `22`[DS=67; sev=purple], `55`[DS=58; sev=purple], `88`[DS=47; sev=purple], `99`[DS=26; sev=purple], `11`[DS=25; sev=purple], `03`[DS=36; sev=purple], `08`[DS=32; sev=purple], `05`[DS=31; sev=purple], `45`[DS=28; sev=purple]
- Evening pair badges `RED`: `08`[DS=64; sev=red], `57`[DS=60; sev=red]
- Evening pair badges `BLUE`: `06`[DS=46; sev=blue], `29`[DS=44; sev=blue], `24`[DS=41; sev=blue]
- Evening pair badges `PURPLE`: `99`[DS=65; sev=purple], `22`[DS=43; sev=purple], `33`[DS=40; sev=purple], `55`[DS=31; sev=purple], `38`[DS=30; sev=purple], `47`[DS=29; sev=purple], `58`[DS=28; sev=purple], `12`[DS=26; sev=purple], `49`[DS=25; sev=purple]
- Cross-variant pair overlaps: `02`[Combined=blue/DS=48; Midday=blue/DS=37], `05`[Combined=blue/DS=48; Midday=purple/DS=31], `06`[Combined=blue/DS=41; Evening=blue/DS=46], `08`[Combined=red/DS=65; Midday=purple/DS=32; Evening=red/DS=64], `12`[Combined=blue/DS=47; Evening=purple/DS=26], `22`[Combined=blue/DS=86; Midday=purple/DS=67; Evening=purple/DS=43], `26`[Combined=purple/DS=30; Midday=blue/DS=40], `28`[Combined=blue/DS=46; Midday=blue/DS=48], `29`[Combined=blue/DS=49; Evening=blue/DS=44], `33`[Combined=blue/DS=80; Midday=red/DS=136; Evening=purple/DS=40], `38`[Combined=red/DS=60; Midday=red/DS=82; Evening=purple/DS=30], `47`[Combined=purple/DS=25; Evening=purple/DS=29]
- Combined boxed combo badges: `088`[DS=977; sev=B], `008`[DS=955; sev=B], `355`[DS=896; sev=B], `788`[DS=789; sev=B], `266`[DS=778; sev=B], `111`[DS=773; sev=B], `339`[DS=767; sev=B], `225`[DS=763; sev=B], `333`[DS=743; sev=B], `113`[DS=729; sev=B]
- Midday boxed combo badges: `668`[DS=984; sev=B], `199`[DS=932; sev=B], `499`[DS=858; sev=B], `399`[DS=841; sev=B], `039`[DS=829; sev=B], `448`[DS=818; sev=B], `005`[DS=810; sev=B], `222`[DS=809; sev=B], `066`[DS=807; sev=B], `599`[DS=697; sev=B]
- Evening boxed combo badges: `009`[DS=998; sev=B], `255`[DS=956; sev=B], `138`[DS=896; sev=B], `117`[DS=879; sev=B], `158`[DS=841; sev=B], `199`[DS=825; sev=B], `112`[DS=785; sev=B], `277`[DS=770; sev=B], `339`[DS=766; sev=B], `155`[DS=755; sev=B]
- Cross-variant boxed-combo overlaps: `005`[Combined=B/DS=676; Midday=B/DS=810], `088`[Combined=B/DS=977; Evening=B/DS=677], `199`[Midday=B/DS=932; Evening=B/DS=825], `339`[Combined=B/DS=767; Evening=B/DS=766], `388`[Combined=B/DS=671; Evening=B/DS=684]
- Combined badge-pressure top indices: `32`[PD=3.00; RAW=6], `13`[PD=2.83; RAW=17], `23`[PD=2.50; RAW=15], `1`[PD=2.50; RAW=5], `11`[PD=2.38; RAW=19], `3`[PD=2.33; RAW=14], `4`[PD=2.33; RAW=14], `10`[PD=2.33; RAW=14]
- Midday badge-pressure top indices: `29`[PD=3.00; RAW=18], `32`[PD=3.00; RAW=6], `13`[PD=2.67; RAW=16], `23`[PD=2.33; RAW=14], `33`[PD=2.33; RAW=14], `14`[PD=1.88; RAW=15], `11`[PD=1.75; RAW=14], `4`[PD=1.67; RAW=10]
- Evening badge-pressure top indices: `32`[PD=2.50; RAW=5], `28`[PD=2.17; RAW=13], `12`[PD=2.12; RAW=17], `13`[PD=1.83; RAW=11], `7`[PD=1.75; RAW=14], `11`[PD=1.75; RAW=14], `3`[PD=1.67; RAW=10], `31`[PD=1.67; RAW=10]

### G1b. Explicit due VTRAC inventory
- Combined due VTRAC overlay: `32`[DS=415], `26`[DS=372], `35`[DS=146], `2`[DS=117], `1`[DS=108], `10`[DS=103], `33`[DS=95], `13`[DS=80]
- Combined due VTRAC heatboard: `32`[DS=415; HZ=0.007; TR=1; AVG=135.500], `26`[DS=372; HZ=0.004; TR=-1; AVG=256.500], `35`[DS=146; HZ=0.007; TR=0; AVG=138.000], `2`[DS=117; HZ=0.036; TR=27; AVG=28.097], `1`[DS=108; HZ=0.005; TR=1; AVG=186.750], `10`[DS=103; HZ=0.029; TR=23; AVG=34.720], `33`[DS=95; HZ=0.028; TR=22; AVG=35.500], `13`[DS=80; HZ=0.025; TR=20; AVG=40.773]
- Midday due VTRAC overlay: `26`[DS=442], `1`[DS=427], `16`[DS=239], `32`[DS=207], `35`[DS=184], `29`[DS=88], `23`[DS=83], `4`[DS=78]
- Midday due VTRAC heatboard: `26`[DS=442; HZ=0.000; TR=0], `1`[DS=427; HZ=0.009; TR=0; AVG=109.600], `16`[DS=239; HZ=0.008; TR=-5; AVG=128.400], `32`[DS=207; HZ=0.007; TR=2; AVG=148.800], `35`[DS=184; HZ=0.003; TR=1; AVG=366.500], `29`[DS=88; HZ=0.022; TR=18; AVG=44.600], `23`[DS=83; HZ=0.034; TR=28; AVG=29.767], `4`[DS=78; HZ=0.022; TR=14; AVG=45.900]
- Evening due VTRAC overlay: `32`[DS=684], `26`[DS=186], `33`[DS=117], `11`[DS=101], `17`[DS=92], `31`[DS=89], `35`[DS=73], `20`[DS=68]
- Evening due VTRAC heatboard: `32`[DS=684; HZ=0.003; TR=0; AVG=306.000], `26`[DS=186; HZ=0.006; TR=1; AVG=176.500], `33`[DS=117; HZ=0.022; TR=12; AVG=45.167], `11`[DS=101; HZ=0.045; TR=40; AVG=22.125], `17`[DS=92; HZ=0.028; TR=24; AVG=35.333], `31`[DS=89; HZ=0.030; TR=26; AVG=33.885], `35`[DS=73; HZ=0.011; TR=2; AVG=87.625], `20`[DS=68; HZ=0.029; TR=25; AVG=34.259]
- Context reinforcement vs context-only pressure: `...`
- Policy relationship / handoff: `...`

## Part H — Translation Sandbox / Downstream Control Arm

### H0. File lock
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-10/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-10/Pennsylvania4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-10/Pennsylvania4/play_card__tool_only__arena_v0.md`

### H1. Auto-captured control-arm snapshot
- Candidate Universe summary: `packs=27` | `union_combos=150`
- Play Card summary: `analysis_prefix`[B12,B24,B36], `convergence_box_first`[B12,B24,B36], `conversion_box_first`[B12,B24,B36], `conversion_box_first_conditional_lenient_presetA`[B12,B24,B36]
- Translation Sandbox positional shortlist top: `588`, `589`, `558`, `158`, `258`, `458`, `288`, `058`
- Translation Sandbox BA canonicals: `025`, `034`, `124`, `178`, `259`, `268`, `349`, `358`
- Translation Sandbox profit canonicals: `024`, `559`
- Diagnostic boxed seed: `288`, `007`, `008`, `024`, `002`, `059`, `058`, `255`, `559`, `004`, `009`, `558`, `005`, `001`, `025`, `224`
- Diagnostic straight seed: `288`, `508`, `588`, `589`, `585`, `581`, `582`, `584`, `070`, `007`, `700`, `085`, `020`, `509`, `255`, `525`
- Diagnostic VT-box seed: `12`, `5`, `3`, `1`, `15`, `23`, `29`, `21`, `4`, `28`, `14`, `22`
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
