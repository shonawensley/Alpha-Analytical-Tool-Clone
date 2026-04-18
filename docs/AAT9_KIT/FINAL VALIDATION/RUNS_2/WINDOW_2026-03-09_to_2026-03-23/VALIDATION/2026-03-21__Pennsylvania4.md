# Analysis Arena Master Validation Run Report — Pennsylvania4 — D=2026-03-21 (H=2026-03-20)

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
- Results date `D`: `2026-03-21`
- History date `H`: `2026-03-20`
- State: `Pennsylvania4`
- Predictive sharepack root: `sharepacks/_predictive`
- Predictive state dir: `sharepacks/_predictive/2026-03-21/Pennsylvania4`
- Truth/frozen sharepack root: `sharepacks`
- Truth state dir: `sharepacks/2026-03-21/Pennsylvania4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## Part A — Winners Environment Lens

### A0. File Lock And Truth Inputs
- Results file: `data/results/2026-03-21.txt`
- Midday winner: literal `573` | canonical `357`
- Evening winner: literal `107` | canonical `017`
- Truth winners dir: `sharepacks/2026-03-21/Pennsylvania4/winners/Pennsylvania4` (missing)
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
- Scores CSV: `sharepacks/_predictive/2026-03-21/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_scores.csv`
- Families CSV: `sharepacks/_predictive/2026-03-21/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_families.csv`
- Compound CSV: `sharepacks/_predictive/2026-03-21/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_compound.csv`
- Metrics JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_metrics.json`
- HTML report: `sharepacks/_predictive/2026-03-21/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_report.html`

### Digit Reduction
- Scores CSV: `sharepacks/_predictive/2026-03-21/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_scores.csv`
- Report HTML: `sharepacks/_predictive/2026-03-21/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report.html`
- Stacked report HTML: `sharepacks/_predictive/2026-03-21/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report_stacked.html`

### VTRAC
- Enhanced JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/vtrac/Pennsylvania4/Pennsylvania4_vtrac_enhanced_20260416_192454.json`
- Validation report JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/vtrac/Pennsylvania4/validation_report.json` (missing)
- Validation report MD: `sharepacks/_predictive/2026-03-21/Pennsylvania4/vtrac/Pennsylvania4/validation_report.md` (missing)

### Hot Zones
- Top lanes CSV: `sharepacks/_predictive/2026-03-21/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_top_lanes.csv`
- Per-lane CSV: `sharepacks/_predictive/2026-03-21/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_per_lane.csv`
- Meta JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_meta.json`
- Winner map JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/hot_zones/Pennsylvania4/2026-03-21_hot_zones_winner_map.json`

## Part F — Aggregated Analysis Arena

### F0. Arena File Lock And Review Surface
- Aggregated arena JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-03-21/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/signals_bundle__tool_only__arena_v0.json`
- Review links available: `True`

### F1-F9. Auto-captured arena snapshot
- Dominant canonicals: `446`, `447`, `478`, `014`, `677`, `477`
- Dominant families: `449`, `24`, `21`, `144`, `31`, `30`
- Dominant VTRAC indices: `25`, `30`, `31`, `14`, `35`, `20`
- Context-reinforced canonicals: `447`, `014`, `088`, `678`, `177`
- Context-only pressure: _none_
- State regime: ``dominant_canonical=446``, ``dominant_family=449``, ``dominant_vtrac_index=25``, ``survivor_pressure=True``, ``last_remaining=False``, ``hidden_terminal_support=True``
- VTRAC literal watchlist: ``25` -> `446,144,199,149``, ``30` -> `478,347,248``, ``31` -> `447,244``, ``14` -> `048,034,359``, ``35` -> `449,499``
- Stable survivor context: ``frontier_rows=0``, ``progressions=27``, ``last_remaining_rows=0``, ``hidden_terminal_frontiers=27``, ``top_frontier_canonicals=044,014,017,057,011,059``
- R-Consensus context: ``events=2``, ``signal_class=strong``, ``trial_eligible=True``, ``top_tails=04,07``, ``top_support=004,007``
- Arena truth alignment summary: `...`
- Arena added value read: `...`
- Arena judgment / handoff: `...`

## Part G — Context / Aux / Control Center Audit

### G0. Context file lock
- Aux summary JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/aux/Pennsylvania4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-03-21/Pennsylvania4/aux/Pennsylvania4/summary.md`
- Control Center dir: `sharepacks/_predictive/2026-03-21/control_center`

### G1-G10. Auto-captured context snapshot
- Positional pressure: ``shortlist_count=16``, ``shortlist_top=147,179,167,178,177,447``
- Due doubles / mirror-double family pressure: ``best_draws_since=0``, ``families=-``
- Blackapple context: ``best_status=OFF``, ``best_score=1``, ``recommended=014,149,248,347,023,059,068,158``
- Profit alerts: ``alert_count=4``, ``top_alerts=Combined:A09:STR8_8,Midday:A05:088:STR8_3,Combined:A04:678:BOX,Combined:A10:066:STR8_3``
- Compound events: ``top_events=Combined:IDX_ECHO_BASE:P60``
- Scoreboard carry-through: ``rank=11``, ``role=shared_host``, ``bucket=small_shoulder``, ``tracker=tracker-strong``
- Aux draw sources present: `True`

### G1a. Explicit Aux badge inventory
- Combined pair badges `RED`: `22`[DS=108; sev=red], `06`[DS=63; sev=red]
- Combined pair badges `BLUE`: `49`[DS=51; sev=blue], `78`[DS=49; sev=blue], `47`[DS=47; sev=blue], `39`[DS=46; sev=blue], `07`[DS=41; sev=blue]
- Combined pair badges `PURPLE`: `88`[DS=64; sev=purple], `44`[DS=29; sev=purple], `19`[DS=36; sev=purple], `68`[DS=32; sev=purple], `46`[DS=31; sev=purple], `35`[DS=30; sev=purple]
- Midday pair badges `RED`: `38`[DS=93; sev=red]
- Midday pair badges `BLUE`: `22`[DS=78; sev=blue], `18`[DS=54; sev=blue], `03`[DS=47; sev=blue], `05`[DS=42; sev=blue], `57`[DS=39; sev=blue]
- Midday pair badges `PURPLE`: `88`[DS=58; sev=purple], `99`[DS=37; sev=purple], `06`[DS=31; sev=purple], `19`[DS=30; sev=purple], `59`[DS=29; sev=purple], `16`[DS=28; sev=purple], `56`[DS=28; sev=purple]
- Evening pair badges `RED`: `06`[DS=57; sev=red]
- Evening pair badges `BLUE`: `47`[DS=40; sev=blue]
- Evening pair badges `PURPLE`: `22`[DS=54; sev=purple], `33`[DS=51; sev=purple], `55`[DS=42; sev=purple], `88`[DS=32; sev=purple], `44`[DS=25; sev=purple], `49`[DS=36; sev=purple], `28`[DS=34; sev=purple], `78`[DS=34; sev=purple], `34`[DS=30; sev=purple], `07`[DS=29; sev=purple], `17`[DS=29; sev=purple], `04`[DS=25; sev=purple]
- Cross-variant pair overlaps: `06`[Combined=red/DS=63; Midday=purple/DS=31; Evening=red/DS=57], `07`[Combined=blue/DS=41; Evening=purple/DS=29], `16`[Combined=purple/DS=28; Midday=purple/DS=28], `19`[Combined=purple/DS=36; Midday=purple/DS=30], `22`[Combined=red/DS=108; Midday=blue/DS=78; Evening=purple/DS=54], `34`[Combined=purple/DS=27; Evening=purple/DS=30], `35`[Combined=purple/DS=30; Midday=purple/DS=27], `39`[Combined=blue/DS=46; Midday=purple/DS=26], `44`[Combined=purple/DS=29; Evening=purple/DS=25], `47`[Combined=blue/DS=47; Evening=blue/DS=40], `49`[Combined=blue/DS=51; Midday=purple/DS=25; Evening=purple/DS=36], `78`[Combined=blue/DS=49; Evening=purple/DS=34]
- Combined boxed combo badges: `088`[DS=999; sev=B], `008`[DS=977; sev=B], `355`[DS=918; sev=B], `788`[DS=811; sev=B], `266`[DS=800; sev=B], `111`[DS=795; sev=B], `339`[DS=789; sev=B], `225`[DS=785; sev=B], `333`[DS=765; sev=B], `113`[DS=751; sev=B]
- Midday boxed combo badges: `668`[DS=995; sev=B], `199`[DS=943; sev=B], `499`[DS=869; sev=B], `399`[DS=852; sev=B], `039`[DS=840; sev=B], `448`[DS=829; sev=B], `005`[DS=821; sev=B], `222`[DS=820; sev=B], `066`[DS=818; sev=B], `599`[DS=708; sev=B]
- Evening boxed combo badges: `255`[DS=967; sev=B], `117`[DS=890; sev=B], `158`[DS=852; sev=B], `199`[DS=836; sev=B], `112`[DS=796; sev=B], `277`[DS=781; sev=B], `339`[DS=777; sev=B], `155`[DS=766; sev=B], `999`[DS=755; sev=B], `228`[DS=743; sev=B]
- Cross-variant boxed-combo overlaps: `005`[Combined=B/DS=698; Midday=B/DS=821], `008`[Combined=B/DS=977; Evening=B/DS=670], `088`[Combined=B/DS=999; Evening=B/DS=688], `199`[Midday=B/DS=943; Evening=B/DS=836], `339`[Combined=B/DS=789; Evening=B/DS=777], `388`[Combined=B/DS=693; Evening=B/DS=695], `455`[Midday=B/DS=705; Evening=B/DS=673]
- Combined badge-pressure top indices: `26`[PD=2.50; RAW=5], `10`[PD=2.00; RAW=12], `27`[PD=2.00; RAW=12], `28`[PD=2.00; RAW=12], `35`[PD=2.00; RAW=4], `30`[PD=1.88; RAW=15], `31`[PD=1.67; RAW=10], `34`[PD=1.67; RAW=10]
- Midday badge-pressure top indices: `32`[PD=3.00; RAW=6], `1`[PD=2.50; RAW=5], `29`[PD=2.00; RAW=12], `26`[PD=2.00; RAW=4], `5`[PD=1.67; RAW=10], `13`[PD=1.67; RAW=10], `8`[PD=1.50; RAW=12], `2`[PD=1.50; RAW=9]
- Evening badge-pressure top indices: `32`[PD=2.50; RAW=5], `28`[PD=1.67; RAW=10], `2`[PD=1.50; RAW=9], `30`[PD=1.38; RAW=11], `29`[PD=1.33; RAW=8], `7`[PD=1.25; RAW=10], `3`[PD=1.17; RAW=7], `5`[PD=1.17; RAW=7]

### G1b. Explicit due VTRAC inventory
- Combined due VTRAC overlay: `32`[DS=437], `26`[DS=394], `35`[DS=168], `2`[DS=139], `1`[DS=130], `33`[DS=117], `29`[DS=94], `17`[DS=81]
- Combined due VTRAC heatboard: `32`[DS=437; HZ=0.007; TR=1; AVG=135.500], `26`[DS=394; HZ=0.004; TR=-1; AVG=256.500], `35`[DS=168; HZ=0.007; TR=0; AVG=138.000], `2`[DS=139; HZ=0.035; TR=26; AVG=28.600], `1`[DS=130; HZ=0.005; TR=1; AVG=186.750], `33`[DS=117; HZ=0.028; TR=22; AVG=35.500], `29`[DS=94; HZ=0.026; TR=15; AVG=38.474], `17`[DS=81; HZ=0.028; TR=19; AVG=35.478]
- Midday due VTRAC overlay: `26`[DS=453], `1`[DS=438], `16`[DS=250], `32`[DS=218], `35`[DS=195], `29`[DS=99], `4`[DS=89], `2`[DS=69]
- Midday due VTRAC heatboard: `26`[DS=453; HZ=0.000; TR=0], `1`[DS=438; HZ=0.009; TR=0; AVG=109.600], `16`[DS=250; HZ=0.008; TR=-5; AVG=128.400], `32`[DS=218; HZ=0.007; TR=2; AVG=148.800], `35`[DS=195; HZ=0.003; TR=1; AVG=366.500], `29`[DS=99; HZ=0.022; TR=18; AVG=44.600], `4`[DS=89; HZ=0.020; TR=12; AVG=49.944], `2`[DS=69; HZ=0.023; TR=15; AVG=43.190]
- Evening due VTRAC overlay: `32`[DS=695], `26`[DS=197], `33`[DS=128], `11`[DS=112], `17`[DS=103], `31`[DS=100], `35`[DS=84], `20`[DS=79]
- Evening due VTRAC heatboard: `32`[DS=695; HZ=0.000; TR=0], `26`[DS=197; HZ=0.006; TR=1; AVG=176.500], `33`[DS=128; HZ=0.022; TR=12; AVG=45.167], `11`[DS=112; HZ=0.045; TR=40; AVG=22.125], `17`[DS=103; HZ=0.028; TR=24; AVG=35.333], `31`[DS=100; HZ=0.030; TR=26; AVG=33.885], `35`[DS=84; HZ=0.011; TR=2; AVG=87.625], `20`[DS=79; HZ=0.029; TR=24; AVG=35.077]
- Context reinforcement vs context-only pressure: `...`
- Policy relationship / handoff: `...`

## Part H — Translation Sandbox / Downstream Control Arm

### H0. File lock
- Translation sandbox JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-03-21/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-03-21/Pennsylvania4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-03-21/Pennsylvania4/play_card__tool_only__arena_v0.md`

### H1. Auto-captured control-arm snapshot
- Candidate Universe summary: `packs=27` | `union_combos=219`
- Play Card summary: `analysis_prefix`[B12,B24,B36], `convergence_box_first`[B12,B24,B36], `conversion_box_first`[B12,B24,B36], `conversion_box_first_conditional_lenient_presetA`[B12,B24,B36]
- Translation Sandbox positional shortlist top: `147`, `179`, `167`, `178`, `177`, `447`, `479`, `137`
- Translation Sandbox BA canonicals: `014`, `149`, `248`, `347`, `023`, `059`, `068`, `158`
- Translation Sandbox profit canonicals: `678`, `088`, `012`, `017`, `026`, `067`, `125`, `157`, `256`, `567`, `066`
- Diagnostic boxed seed: `447`, `014`, `066`, `478`, `477`, `017`, `088`, `678`, `007`, `009`, `149`, `347`, `044`, `057`, `177`, `059`
- Diagnostic straight seed: `167`, `447`, `147`, `197`, `187`, `177`, `497`, `137`, `007`, `070`, `700`, `477`, `747`, `774`, `048`, `084`
- Diagnostic VT-box seed: `31`, `18`, `23`, `33`, `15`, `9`, `20`, `25`, `30`, `14`, `35`, `28`
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
