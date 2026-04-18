# Analysis Arena Master Validation Run Report — Pennsylvania4 — D=2026-03-18 (H=2026-03-17)

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
- Results date `D`: `2026-03-18`
- History date `H`: `2026-03-17`
- State: `Pennsylvania4`
- Predictive sharepack root: `sharepacks/_predictive`
- Predictive state dir: `sharepacks/_predictive/2026-03-18/Pennsylvania4`
- Truth/frozen sharepack root: `sharepacks`
- Truth state dir: `sharepacks/2026-03-18/Pennsylvania4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## Part A — Winners Environment Lens

### A0. File Lock And Truth Inputs
- Results file: `data/results/2026-03-18.txt`
- Midday winner: literal `629` | canonical `269`
- Evening winner: literal `083` | canonical `038`
- Truth winners dir: `sharepacks/2026-03-18/Pennsylvania4/winners/Pennsylvania4` (missing)
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
- Scores CSV: `sharepacks/_predictive/2026-03-18/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_scores.csv`
- Families CSV: `sharepacks/_predictive/2026-03-18/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_families.csv`
- Compound CSV: `sharepacks/_predictive/2026-03-18/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_compound.csv`
- Metrics JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_metrics.json`
- HTML report: `sharepacks/_predictive/2026-03-18/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_report.html`

### Digit Reduction
- Scores CSV: `sharepacks/_predictive/2026-03-18/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_scores.csv`
- Report HTML: `sharepacks/_predictive/2026-03-18/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report.html`
- Stacked report HTML: `sharepacks/_predictive/2026-03-18/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report_stacked.html`

### VTRAC
- Enhanced JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/vtrac/Pennsylvania4/Pennsylvania4_vtrac_enhanced_20260416_191143.json`
- Validation report JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/vtrac/Pennsylvania4/validation_report.json` (missing)
- Validation report MD: `sharepacks/_predictive/2026-03-18/Pennsylvania4/vtrac/Pennsylvania4/validation_report.md` (missing)

### Hot Zones
- Top lanes CSV: `sharepacks/_predictive/2026-03-18/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_top_lanes.csv`
- Per-lane CSV: `sharepacks/_predictive/2026-03-18/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_per_lane.csv`
- Meta JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_meta.json`
- Winner map JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/hot_zones/Pennsylvania4/2026-03-18_hot_zones_winner_map.json`

## Part F — Aggregated Analysis Arena

### F0. Arena File Lock And Review Surface
- Aggregated arena JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-18/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/signals_bundle__tool_only__arena_v0.json`
- Review links available: `True`

### F1-F9. Auto-captured arena snapshot
- Dominant canonicals: `077`, `067`, `034`, `259`, `477`, `677`
- Dominant families: `259`, `10.0`, `28`, `30`, `24`, `23`
- Dominant VTRAC indices: `10`, `28`, `12`, `7`, `23`, `14`
- Context-reinforced canonicals: `077`, `067`, `034`, `677`, `027`, `255`
- Context-only pressure: _none_
- State regime: ``dominant_canonical=077``, ``dominant_family=259``, ``dominant_vtrac_index=10``, ``survivor_pressure=True``, ``last_remaining=False``, ``hidden_terminal_support=True``
- VTRAC literal watchlist: ``10` -> `077,027,257``, ``28` -> `224,477,247,279``, ``12` -> `259,047,024,029``, ``7` -> `067,125,017,026``, ``23` -> `688,133,336,138``
- Stable survivor context: ``frontier_rows=0``, ``progressions=27``, ``last_remaining_rows=0``, ``hidden_terminal_frontiers=27``, ``top_frontier_canonicals=004,007,014,057,005,044``
- R-Consensus context: ``events=8``, ``signal_class=strong``, ``trial_eligible=True``, ``top_tails=77,33,06,03``, ``top_support=077,033,003,006``
- Arena truth alignment summary: `...`
- Arena added value read: `...`
- Arena judgment / handoff: `...`

## Part G — Context / Aux / Control Center Audit

### G0. Context file lock
- Aux summary JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/aux/Pennsylvania4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-18/Pennsylvania4/aux/Pennsylvania4/summary.md`
- Control Center dir: `sharepacks/_predictive/2026-03-18/control_center`

### G1-G10. Auto-captured context snapshot
- Positional pressure: ``shortlist_count=16``, ``shortlist_top=367,137,677,236,067,267``
- Due doubles / mirror-double family pressure: ``best_draws_since=0``, ``families=-``
- Blackapple context: ``best_status=OFF``, ``best_score=1``, ``recommended=016,017,026,027,036,037,046,047``
- Profit alerts: ``alert_count=5``, ``top_alerts=Combined:A11:077:BOX,Combined:A05:077:STR8_3,Evening:A04:034:BOX,Combined:A02:077:STR8_3,Combined:A02:077:STR8_3``
- Compound events: ``top_events=Combined:STRAIGHT_GATE:P80``
- Scoreboard carry-through: ``rank=11``, ``role=shared_host``, ``bucket=small_shoulder``, ``tracker=tracker-strong``
- Aux draw sources present: `True`

### G1a. Explicit Aux badge inventory
- Combined pair badges `RED`: `06`[DS=57; sev=red]
- Combined pair badges `BLUE`: `22`[DS=102; sev=blue], `26`[DS=46; sev=blue], `49`[DS=45; sev=blue], `78`[DS=43; sev=blue], `47`[DS=41; sev=blue], `39`[DS=40; sev=blue]
- Combined pair badges `PURPLE`: `88`[DS=58; sev=purple], `03`[DS=36; sev=purple], `07`[DS=35; sev=purple], `19`[DS=30; sev=purple], `17`[DS=29; sev=purple]
- Midday pair badges `RED`: `38`[DS=90; sev=red]
- Midday pair badges `BLUE`: `22`[DS=75; sev=blue], `18`[DS=51; sev=blue], `26`[DS=48; sev=blue], `03`[DS=44; sev=blue], `05`[DS=39; sev=blue]
- Midday pair badges `PURPLE`: `88`[DS=55; sev=purple], `99`[DS=34; sev=purple], `57`[DS=36; sev=purple], `12`[DS=31; sev=purple], `06`[DS=28; sev=purple], `19`[DS=27; sev=purple], `59`[DS=26; sev=purple]
- Evening pair badges `BLUE`: `06`[DS=54; sev=blue], `47`[DS=37; sev=blue]
- Evening pair badges `PURPLE`: `22`[DS=51; sev=purple], `33`[DS=48; sev=purple], `55`[DS=39; sev=purple], `88`[DS=29; sev=purple], `49`[DS=33; sev=purple], `28`[DS=31; sev=purple], `78`[DS=31; sev=purple], `34`[DS=27; sev=purple], `07`[DS=26; sev=purple], `17`[DS=26; sev=purple]
- Cross-variant pair overlaps: `03`[Combined=purple/DS=36; Midday=blue/DS=44], `06`[Combined=red/DS=57; Midday=purple/DS=28; Evening=blue/DS=54], `07`[Combined=purple/DS=35; Evening=purple/DS=26], `17`[Combined=purple/DS=29; Evening=purple/DS=26], `19`[Combined=purple/DS=30; Midday=purple/DS=27], `22`[Combined=blue/DS=102; Midday=blue/DS=75; Evening=purple/DS=51], `26`[Combined=blue/DS=46; Midday=blue/DS=48], `47`[Combined=blue/DS=41; Evening=blue/DS=37], `49`[Combined=blue/DS=45; Evening=purple/DS=33], `78`[Combined=blue/DS=43; Evening=purple/DS=31], `88`[Combined=purple/DS=58; Midday=purple/DS=55; Evening=purple/DS=29]
- Combined boxed combo badges: `088`[DS=993; sev=B], `008`[DS=971; sev=B], `355`[DS=912; sev=B], `788`[DS=805; sev=B], `266`[DS=794; sev=B], `111`[DS=789; sev=B], `339`[DS=783; sev=B], `225`[DS=779; sev=B], `333`[DS=759; sev=B], `113`[DS=745; sev=B]
- Midday boxed combo badges: `668`[DS=992; sev=B], `199`[DS=940; sev=B], `499`[DS=866; sev=B], `399`[DS=849; sev=B], `039`[DS=837; sev=B], `448`[DS=826; sev=B], `005`[DS=818; sev=B], `222`[DS=817; sev=B], `066`[DS=815; sev=B], `599`[DS=705; sev=B]
- Evening boxed combo badges: `255`[DS=964; sev=B], `117`[DS=887; sev=B], `158`[DS=849; sev=B], `199`[DS=833; sev=B], `112`[DS=793; sev=B], `277`[DS=778; sev=B], `339`[DS=774; sev=B], `155`[DS=763; sev=B], `999`[DS=752; sev=B], `228`[DS=740; sev=B]
- Cross-variant boxed-combo overlaps: `005`[Combined=B/DS=692; Midday=B/DS=818], `008`[Combined=B/DS=971; Evening=B/DS=667], `088`[Combined=B/DS=993; Evening=B/DS=685], `199`[Midday=B/DS=940; Evening=B/DS=833], `339`[Combined=B/DS=783; Evening=B/DS=774], `388`[Combined=B/DS=687; Evening=B/DS=692], `455`[Midday=B/DS=702; Evening=B/DS=670]
- Combined badge-pressure top indices: `26`[PD=2.00; RAW=4], `35`[PD=2.00; RAW=4], `30`[PD=1.75; RAW=14], `27`[PD=1.67; RAW=10], `20`[PD=1.50; RAW=9], `6`[PD=1.33; RAW=8], `10`[PD=1.33; RAW=8], `25`[PD=1.33; RAW=8]
- Midday badge-pressure top indices: `32`[PD=3.00; RAW=6], `1`[PD=2.50; RAW=5], `29`[PD=2.00; RAW=12], `26`[PD=2.00; RAW=4], `5`[PD=1.67; RAW=10], `2`[PD=1.50; RAW=9], `13`[PD=1.50; RAW=9], `7`[PD=1.38; RAW=11]
- Evening badge-pressure top indices: `32`[PD=2.50; RAW=5], `28`[PD=1.67; RAW=10], `30`[PD=1.38; RAW=11], `29`[PD=1.33; RAW=8], `2`[PD=1.17; RAW=7], `3`[PD=1.17; RAW=7], `33`[PD=1.17; RAW=7], `7`[PD=1.00; RAW=8]

### G1b. Explicit due VTRAC inventory
- Combined due VTRAC overlay: `32`[DS=431], `26`[DS=388], `35`[DS=162], `2`[DS=133], `1`[DS=124], `33`[DS=111], `13`[DS=96], `29`[DS=88]
- Combined due VTRAC heatboard: `32`[DS=431; HZ=0.007; TR=1; AVG=135.500], `26`[DS=388; HZ=0.004; TR=-1; AVG=256.500], `35`[DS=162; HZ=0.007; TR=0; AVG=138.000], `2`[DS=133; HZ=0.035; TR=26; AVG=28.600], `1`[DS=124; HZ=0.005; TR=1; AVG=186.750], `33`[DS=111; HZ=0.028; TR=22; AVG=35.500], `13`[DS=96; HZ=0.025; TR=20; AVG=40.773], `29`[DS=88; HZ=0.026; TR=15; AVG=38.474]
- Midday due VTRAC overlay: `26`[DS=450], `1`[DS=435], `16`[DS=247], `32`[DS=215], `35`[DS=192], `29`[DS=96], `4`[DS=86], `2`[DS=66]
- Midday due VTRAC heatboard: `26`[DS=450; HZ=0.000; TR=0], `1`[DS=435; HZ=0.009; TR=0; AVG=109.600], `16`[DS=247; HZ=0.008; TR=-5; AVG=128.400], `32`[DS=215; HZ=0.007; TR=2; AVG=148.800], `35`[DS=192; HZ=0.003; TR=1; AVG=366.500], `29`[DS=96; HZ=0.022; TR=18; AVG=44.600], `4`[DS=86; HZ=0.020; TR=12; AVG=49.944], `2`[DS=66; HZ=0.023; TR=15; AVG=43.190]
- Evening due VTRAC overlay: `32`[DS=692], `26`[DS=194], `33`[DS=125], `11`[DS=109], `17`[DS=100], `31`[DS=97], `35`[DS=81], `20`[DS=76]
- Evening due VTRAC heatboard: `32`[DS=692; HZ=0.003; TR=0; AVG=306.000], `26`[DS=194; HZ=0.006; TR=1; AVG=176.500], `33`[DS=125; HZ=0.022; TR=12; AVG=45.167], `11`[DS=109; HZ=0.045; TR=40; AVG=22.125], `17`[DS=100; HZ=0.028; TR=24; AVG=35.333], `31`[DS=97; HZ=0.030; TR=26; AVG=33.885], `35`[DS=81; HZ=0.011; TR=2; AVG=87.625], `20`[DS=76; HZ=0.029; TR=24; AVG=35.077]
- Context reinforcement vs context-only pressure: `...`
- Policy relationship / handoff: `...`

## Part H — Translation Sandbox / Downstream Control Arm

### H0. File lock
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-18/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-18/Pennsylvania4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-18/Pennsylvania4/play_card__tool_only__arena_v0.md`

### H1. Auto-captured control-arm snapshot
- Candidate Universe summary: `packs=27` | `union_combos=205`
- Play Card summary: `analysis_prefix`[B12,B24,B36], `convergence_box_first`[B12,B24,B36], `conversion_box_first`[B12,B24,B36], `conversion_box_first_conditional_lenient_presetA`[B12,B24,B36]
- Translation Sandbox positional shortlist top: `367`, `137`, `677`, `236`, `067`, `267`, `567`, `026`
- Translation Sandbox BA canonicals: `016`, `017`, `026`, `027`, `036`, `037`, `046`, `047`
- Translation Sandbox profit canonicals: `077`, `034`
- Diagnostic boxed seed: `077`, `067`, `677`, `007`, `034`, `027`, `224`, `004`, `014`, `057`, `026`, `037`, `047`, `267`, `009`, `277`
- Diagnostic straight seed: `677`, `670`, `627`, `673`, `173`, `623`, `675`, `620`, `007`, `070`, `700`, `237`, `077`, `707`, `770`, `047`
- Diagnostic VT-box seed: `10`, `12`, `7`, `23`, `18`, `33`, `14`, `20`, `28`, `6`, `8`, `11`
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
