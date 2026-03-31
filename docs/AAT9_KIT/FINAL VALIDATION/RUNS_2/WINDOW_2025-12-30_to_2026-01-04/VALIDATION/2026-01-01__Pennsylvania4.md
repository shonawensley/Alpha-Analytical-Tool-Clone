# Analysis Arena Master Validation Run Report — Pennsylvania4 — D=2026-01-01 (H=2025-12-31)

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
- Results date `D`: `2026-01-01`
- History date `H`: `2025-12-31`
- State: `Pennsylvania4`
- Predictive sharepack root: `sharepacks/_predictive`
- Predictive state dir: `sharepacks/_predictive/2026-01-01/Pennsylvania4`
- Truth/frozen sharepack root: `sharepacks`
- Truth state dir: `sharepacks/2026-01-01/Pennsylvania4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## Part A — Winners Environment Lens

### A0. File Lock And Truth Inputs
- Results file: `data/results/2026-01-01.txt`
- Midday winner: literal `322` | canonical `223`
- Evening winner: literal `328` | canonical `238`
- Truth winners dir: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4`
- Winners HTML: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac27_winner_322_20260105_053422.html`, `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac29_winner_328_20260105_053423.html`
- Winners JSON: `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac27_winner_322_20260105_053422.json`, `sharepacks/2026-01-01/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac29_winner_328_20260105_053423.json`

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
- Scores CSV: `sharepacks/_predictive/2026-01-01/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_scores.csv`
- Families CSV: `sharepacks/_predictive/2026-01-01/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_families.csv`
- Compound CSV: `sharepacks/_predictive/2026-01-01/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_compound.csv`
- Metrics JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_metrics.json`
- HTML report: `sharepacks/_predictive/2026-01-01/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_report.html`

### Digit Reduction
- Scores CSV: `sharepacks/_predictive/2026-01-01/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_scores.csv`
- Report HTML: `sharepacks/_predictive/2026-01-01/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report.html`
- Stacked report HTML: `sharepacks/_predictive/2026-01-01/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report_stacked.html`

### VTRAC
- Enhanced JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/vtrac/Pennsylvania4/Pennsylvania4_vtrac_enhanced_20260330_041527.json`
- Validation report JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/vtrac/Pennsylvania4/validation_report.json` (missing)
- Validation report MD: `sharepacks/_predictive/2026-01-01/Pennsylvania4/vtrac/Pennsylvania4/validation_report.md` (missing)

### Hot Zones
- Top lanes CSV: `sharepacks/_predictive/2026-01-01/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_top_lanes.csv`
- Per-lane CSV: `sharepacks/_predictive/2026-01-01/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_per_lane.csv`
- Meta JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_meta.json`
- Winner map JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/hot_zones/Pennsylvania4/2026-01-01_hot_zones_winner_map.json`

## Part F — Aggregated Analysis Arena

### F0. Arena File Lock And Review Surface
- Aggregated arena JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-01/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/signals_bundle__tool_only__arena_v0.json`
- Review links available: `True`

### F1-F9. Auto-captured arena snapshot
- Dominant canonicals: `559`, `359`, `339`, `138`, `113`, `599`
- Dominant families: `559`, `23`, `29`, `21`, `14`, `599`
- Dominant VTRAC indices: `5`, `23`, `18`, `33`, `14`, `15`
- Context-reinforced canonicals: `559`, `359`, `339`, `019`
- Context-only pressure: _none_
- State regime: ``dominant_canonical=559``, ``dominant_family=559``, ``dominant_vtrac_index=5``, ``survivor_pressure=True``, ``last_remaining=False``, ``hidden_terminal_support=True``
- VTRAC literal watchlist: ``5` -> `559,059,009``, ``23` -> `133,138,336,188``, ``18` -> `113,118,168,668``, ``33` -> `339``, ``14` -> `359``
- Stable survivor context: ``frontier_rows=0``, ``progressions=27``, ``last_remaining_rows=0``, ``hidden_terminal_frontiers=27``, ``top_frontier_canonicals=017,057,011,014,024,019``
- R-Consensus context: ``events=1``, ``signal_class=moderate``, ``trial_eligible=True``, ``top_tails=39``, ``top_support=339,379,337``
- Arena truth alignment summary: `...`
- Arena added value read: `...`
- Arena judgment / handoff: `...`

## Part G — Context / Aux / Control Center Audit

### G0. Context file lock
- Aux summary JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/aux/Pennsylvania4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-01/Pennsylvania4/aux/Pennsylvania4/summary.md`
- Control Center dir: `sharepacks/_predictive/2026-01-01/control_center`

### G1-G10. Auto-captured context snapshot
- Positional pressure: ``shortlist_count=16``, ``shortlist_top=135,345,137,177,355,347``
- Due doubles / mirror-double family pressure: ``best_draws_since=0``, ``families=-``
- Blackapple context: ``best_status=OFF``, ``best_score=1``, ``recommended=015,019,025,029,035,039,045,049``
- Profit alerts: ``alert_count=3``, ``top_alerts=Midday:A05:339:STR8_3,Midday:A04:359:BOX,Midday:A12:359:STR8_4of8``
- Compound events: ``top_events=Midday:CARRY_PERM:P70``
- Scoreboard carry-through: ``rank=11``, ``role=shared_host``, ``bucket=small_shoulder``, ``tracker=tracker-strong``
- Aux draw sources present: `True`

### G1a. Explicit Aux badge inventory
- Combined pair badges `RED`: `33`[DS=137; sev=red], `78`[DS=70; sev=red]
- Combined pair badges `BLUE`: `77`[DS=76; sev=blue], `88`[DS=75; sev=blue], `03`[DS=45; sev=blue], `07`[DS=43; sev=blue]
- Combined pair badges `PURPLE`: `44`[DS=69; sev=purple], `66`[DS=63; sev=purple], `55`[DS=40; sev=purple], `11`[DS=25; sev=purple], `35`[DS=36; sev=purple], `69`[DS=34; sev=purple], `36`[DS=31; sev=purple], `09`[DS=30; sev=purple], `34`[DS=29; sev=purple], `38`[DS=29; sev=purple], `19`[DS=27; sev=purple]
- Midday pair badges `RED`: `55`[DS=185; sev=red], `99`[DS=132; sev=red], `59`[DS=78; sev=red], `79`[DS=72; sev=red]
- Midday pair badges `BLUE`: `77`[DS=75; sev=blue], `12`[DS=47; sev=blue], `78`[DS=45; sev=blue], `06`[DS=42; sev=blue], `35`[DS=39; sev=blue]
- Midday pair badges `PURPLE`: `33`[DS=68; sev=purple], `22`[DS=61; sev=purple], `88`[DS=37; sev=purple], `44`[DS=34; sev=purple], `66`[DS=31; sev=purple], `56`[DS=31; sev=purple], `69`[DS=29; sev=purple]
- Evening pair badges `RED`: `88`[DS=127; sev=red], `68`[DS=85; sev=red], `07`[DS=62; sev=red]
- Evening pair badges `BLUE`: `15`[DS=50; sev=blue], `38`[DS=49; sev=blue], `23`[DS=46; sev=blue], `03`[DS=44; sev=blue]
- Evening pair badges `PURPLE`: `33`[DS=69; sev=purple], `44`[DS=40; sev=purple], `77`[DS=38; sev=purple], `66`[DS=36; sev=purple], `11`[DS=27; sev=purple], `78`[DS=35; sev=purple], `19`[DS=34; sev=purple], `28`[DS=33; sev=purple], `01`[DS=28; sev=purple]
- Cross-variant pair overlaps: `03`[Combined=blue/DS=45; Evening=blue/DS=44], `07`[Combined=blue/DS=43; Evening=red/DS=62], `11`[Combined=purple/DS=25; Evening=purple/DS=27], `19`[Combined=purple/DS=27; Evening=purple/DS=34], `33`[Combined=red/DS=137; Midday=purple/DS=68; Evening=purple/DS=69], `35`[Combined=purple/DS=36; Midday=blue/DS=39], `38`[Combined=purple/DS=29; Evening=blue/DS=49], `44`[Combined=purple/DS=69; Midday=purple/DS=34; Evening=purple/DS=40], `55`[Combined=purple/DS=40; Midday=red/DS=185], `66`[Combined=purple/DS=63; Midday=purple/DS=31; Evening=purple/DS=36], `69`[Combined=purple/DS=34; Midday=purple/DS=29], `77`[Combined=blue/DS=76; Midday=blue/DS=75; Evening=purple/DS=38]
- Combined boxed combo badges: `066`[DS=994; sev=B], `666`[DS=992; sev=B], `159`[DS=880; sev=B], `007`[DS=877; sev=B], `088`[DS=841; sev=B], `008`[DS=819; sev=B], `444`[DS=795; sev=B], `039`[DS=770; sev=B], `355`[DS=760; sev=B], `344`[DS=689; sev=B]
- Midday boxed combo badges: `559`[DS=976; sev=B], `288`[DS=963; sev=B], `255`[DS=934; sev=B], `668`[DS=916; sev=B], `199`[DS=864; sev=B], `499`[DS=790; sev=B], `399`[DS=773; sev=B], `039`[DS=761; sev=B], `448`[DS=750; sev=B], `005`[DS=742; sev=B]
- Evening boxed combo badges: `444`[DS=972; sev=B], `009`[DS=930; sev=B], `255`[DS=888; sev=B], `138`[DS=828; sev=B], `117`[DS=811; sev=B], `158`[DS=773; sev=B], `344`[DS=766; sev=B], `199`[DS=757; sev=B], `112`[DS=717; sev=B], `277`[DS=702; sev=B]
- Cross-variant boxed-combo overlaps: `039`[Combined=B/DS=770; Midday=B/DS=761], `066`[Combined=B/DS=994; Midday=B/DS=739], `199`[Midday=B/DS=864; Evening=B/DS=757], `255`[Midday=B/DS=934; Evening=B/DS=888], `344`[Combined=B/DS=689; Evening=B/DS=766], `444`[Combined=B/DS=795; Evening=B/DS=972]
- Combined badge-pressure top indices: `32`[PD=2.50; RAW=5], `13`[PD=2.33; RAW=14], `29`[PD=2.33; RAW=14], `23`[PD=2.17; RAW=13], `33`[PD=2.00; RAW=12], `26`[PD=2.00; RAW=4], `3`[PD=1.50; RAW=9], `27`[PD=1.50; RAW=9]
- Midday badge-pressure top indices: `26`[PD=2.50; RAW=5], `35`[PD=2.50; RAW=5], `2`[PD=2.00; RAW=12], `5`[PD=2.00; RAW=12], `31`[PD=2.00; RAW=12], `34`[PD=2.00; RAW=12], `1`[PD=2.00; RAW=4], `15`[PD=1.83; RAW=11]
- Evening badge-pressure top indices: `32`[PD=3.00; RAW=6], `23`[PD=2.50; RAW=15], `29`[PD=2.50; RAW=15], `13`[PD=2.17; RAW=13], `33`[PD=2.17; RAW=13], `8`[PD=2.12; RAW=17], `7`[PD=1.62; RAW=13], `21`[PD=1.62; RAW=13]

### G1b. Explicit due VTRAC inventory
- Combined due VTRAC overlay: `32`[DS=279], `26`[DS=236], `16`[DS=94], `27`[DS=70], `7`[DS=62], `6`[DS=57], `13`[DS=55], `19`[DS=51]
- Combined due VTRAC heatboard: `32`[DS=279; HZ=0.007; TR=1; AVG=135.500], `26`[DS=236; HZ=0.004; TR=-1; AVG=256.500], `16`[DS=94; HZ=0.007; TR=1; AVG=135.667], `27`[DS=70; HZ=0.017; TR=7; AVG=58.067], `7`[DS=62; HZ=0.040; TR=35; AVG=25.216], `6`[DS=57; HZ=0.025; TR=21; AVG=40.739], `13`[DS=55; HZ=0.025; TR=20; AVG=40.727], `19`[DS=51; HZ=0.026; TR=18; AVG=38.917]
- Midday due VTRAC overlay: `26`[DS=374], `1`[DS=359], `34`[DS=213], `16`[DS=171], `15`[DS=162], `32`[DS=139], `35`[DS=116], `27`[DS=83]
- Midday due VTRAC heatboard: `26`[DS=374; HZ=0.000; TR=0], `1`[DS=359; HZ=0.009; TR=0; AVG=109.600], `34`[DS=213; HZ=0.026; TR=18; AVG=38.000], `16`[DS=171; HZ=0.008; TR=-6; AVG=132.833], `15`[DS=162; HZ=0.029; TR=23; AVG=34.000], `32`[DS=139; HZ=0.007; TR=2; AVG=148.800], `35`[DS=116; HZ=0.004; TR=0; AVG=281.000], `27`[DS=83; HZ=0.029; TR=20; AVG=34.958]
- Evening due VTRAC overlay: `32`[DS=616], `23`[DS=155], `26`[DS=118], `18`[DS=115], `13`[DS=64], `29`[DS=57], `33`[DS=49], `16`[DS=47]
- Evening due VTRAC heatboard: `32`[DS=616; HZ=0.003; TR=0; AVG=306.000], `23`[DS=155; HZ=0.025; TR=15; AVG=39.737], `26`[DS=118; HZ=0.006; TR=1; AVG=176.500], `18`[DS=115; HZ=0.029; TR=21; AVG=34.360], `13`[DS=64; HZ=0.025; TR=19; AVG=40.190], `29`[DS=57; HZ=0.021; TR=13; AVG=48.684], `33`[DS=49; HZ=0.023; TR=16; AVG=43.000], `16`[DS=47; HZ=0.010; TR=2; AVG=105.000]
- Context reinforcement vs context-only pressure: `...`
- Policy relationship / handoff: `...`

## Part H — Translation Sandbox / Downstream Control Arm

### H0. File lock
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-01/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-01/Pennsylvania4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-01/Pennsylvania4/play_card__tool_only__arena_v0.md`

### H1. Auto-captured control-arm snapshot
- Candidate Universe summary: `packs=27` | `union_combos=170`
- Play Card summary: `analysis_prefix`[B12,B24,B36], `convergence_box_first`[B12,B24,B36], `conversion_box_first`[B12,B24,B36], `conversion_box_first_conditional_lenient_presetA`[B12,B24,B36]
- Translation Sandbox positional shortlist top: `135`, `345`, `137`, `177`, `355`, `347`, `477`, `357`
- Translation Sandbox BA canonicals: `015`, `019`, `025`, `029`, `035`, `039`, `045`, `049`
- Translation Sandbox profit canonicals: `359`, `339`, `345`, `458`, `589`
- Diagnostic boxed seed: `339`, `019`, `359`, `138`, `255`, `007`, `559`, `017`, `057`, `011`, `014`, `345`, `035`, `355`, `277`, `228`
- Diagnostic straight seed: `315`, `345`, `317`, `717`, `355`, `347`, `747`, `357`, `007`, `070`, `700`, `138`, `183`, `318`, `381`, `813`
- Diagnostic VT-box seed: `33`, `5`, `23`, `18`, `14`, `20`, `15`, `9`, `12`, `2`, `3`, `4`
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
