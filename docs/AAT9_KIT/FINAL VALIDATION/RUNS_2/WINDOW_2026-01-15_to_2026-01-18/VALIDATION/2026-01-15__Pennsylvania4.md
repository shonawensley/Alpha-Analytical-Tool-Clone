# Analysis Arena Master Validation Run Report — Pennsylvania4 — D=2026-01-15 (H=2026-01-14)

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
- Results date `D`: `2026-01-15`
- History date `H`: `2026-01-14`
- State: `Pennsylvania4`
- Predictive sharepack root: `sharepacks/_predictive`
- Predictive state dir: `sharepacks/_predictive/2026-01-15/Pennsylvania4`
- Truth/frozen sharepack root: `sharepacks`
- Truth state dir: `sharepacks/2026-01-15/Pennsylvania4`
- Profile: `tool_only`
- Experiment tag: `arena_v0`

## Part A — Winners Environment Lens

### A0. File Lock And Truth Inputs
- Results file: `data/results/2026-01-15.txt`
- Midday winner: literal `612` | canonical `126`
- Evening winner: literal `385` | canonical `358`
- Truth winners dir: `sharepacks/2026-01-15/Pennsylvania4/winners/Pennsylvania4`
- Winners HTML: `sharepacks/2026-01-15/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac13_winner_385_20260127_014851.html`, `sharepacks/2026-01-15/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_612_20260127_014850.html`
- Winners JSON: `sharepacks/2026-01-15/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac13_winner_385_20260127_014851.json`, `sharepacks/2026-01-15/Pennsylvania4/winners/Pennsylvania4/Pennsylvania4_vtrac17_winner_612_20260127_014850.json`

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
- Scores CSV: `sharepacks/_predictive/2026-01-15/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_scores.csv`
- Families CSV: `sharepacks/_predictive/2026-01-15/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_families.csv`
- Compound CSV: `sharepacks/_predictive/2026-01-15/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_compound.csv`
- Metrics JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_metrics.json`
- HTML report: `sharepacks/_predictive/2026-01-15/Pennsylvania4/stable/Pennsylvania4/Pennsylvania4_stable_patterns_report.html`

### Digit Reduction
- Scores CSV: `sharepacks/_predictive/2026-01-15/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_scores.csv`
- Report HTML: `sharepacks/_predictive/2026-01-15/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report.html`
- Stacked report HTML: `sharepacks/_predictive/2026-01-15/Pennsylvania4/digit_reduction/Pennsylvania4/Pennsylvania4_digit_reduction_report_stacked.html`

### VTRAC
- Enhanced JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/vtrac/Pennsylvania4/Pennsylvania4_vtrac_enhanced_20260328_054630.json`
- Validation report JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/vtrac/Pennsylvania4/validation_report.json` (missing)
- Validation report MD: `sharepacks/_predictive/2026-01-15/Pennsylvania4/vtrac/Pennsylvania4/validation_report.md` (missing)

### Hot Zones
- Top lanes CSV: `sharepacks/_predictive/2026-01-15/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_top_lanes.csv`
- Per-lane CSV: `sharepacks/_predictive/2026-01-15/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_per_lane.csv`
- Meta JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/hot_zones/Pennsylvania4/Pennsylvania4_hot_zones_meta.json`
- Winner map JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/hot_zones/Pennsylvania4/2026-01-15_hot_zones_winner_map.json`

## Part F — Aggregated Analysis Arena

### F0. Arena File Lock And Review Surface
- Aggregated arena JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- Aggregated arena MD: `sharepacks/_predictive/2026-01-15/Pennsylvania4/analysis/aggregated_analysis_arena__tool_only__arena_v0.md`
- Signals bundle JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/signals_bundle__tool_only__arena_v0.json`
- Review links available: `True`

### F1-F9. Auto-captured arena snapshot
- Dominant canonicals: `244`, `446`, `234`, `239`, `388`, `688`
- Dominant families: `299`, `30`, `34`, `31`, `25`, `249`
- Dominant VTRAC indices: `31`, `30`, `25`, `33`, `32`, `23`
- Context-reinforced canonicals: `244`, `446`, `239`, `007`, `344`
- Context-only pressure: `255`, `444`
- State regime: ``dominant_canonical=244``, ``dominant_family=299``, ``dominant_vtrac_index=31``, ``survivor_pressure=True``, ``last_remaining=False``, ``hidden_terminal_support=True``
- VTRAC literal watchlist: ``31` -> `244,447,249,299``, ``30` -> `234,239,379,347,789``, ``25` -> `446,469,199``, ``33` -> `339,889``, ``32` -> `388``
- Stable survivor context: ``frontier_rows=0``, ``progressions=27``, ``last_remaining_rows=0``, ``hidden_terminal_frontiers=27``, ``top_frontier_canonicals=009,044,004,006,007,113``
- R-Consensus context: ``available=false``
- Arena truth alignment summary: `...`
- Arena added value read: `...`
- Arena judgment / handoff: `...`

## Part G — Context / Aux / Control Center Audit

### G0. Context file lock
- Aux summary JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/aux/Pennsylvania4/summary.json`
- Aux summary MD: `sharepacks/_predictive/2026-01-15/Pennsylvania4/aux/Pennsylvania4/summary.md`
- Control Center dir: `sharepacks/_predictive/2026-01-15/control_center`

### G1-G10. Auto-captured context snapshot
- Positional pressure: ``shortlist_count=16``, ``shortlist_top=344,034,134,013,444,447``
- Due doubles / mirror-double family pressure: ``best_draws_since=0``, ``families=-``
- Blackapple context: ``best_status=ALERT``, ``best_score=3``, ``recommended=049,058,238,247,067,148,256,346``
- Profit alerts: ``alert_count=5``, ``top_alerts=Midday:A05:244:STR8_3,Combined:A08:OVERLAY,Midday:A04:239:BOX,Combined:A12:446:STR8_4of8,Evening:A08:OVERLAY``
- Compound events: ``top_events=Midday:CARRY_PERM:P70,Combined:CLAMP_4:P25``
- Scoreboard carry-through: ``rank=11``, ``role=shared_host``, ``bucket=small_shoulder``, ``tracker=tracker-rich``
- Aux draw sources present: `True`

### G1a. Explicit Aux badge inventory
- Combined pair badges `RED`: `33`[DS=165; sev=red], `34`[DS=57; sev=red]
- Combined pair badges `BLUE`: `66`[DS=91; sev=blue], `27`[DS=41; sev=blue], `67`[DS=41; sev=blue], `49`[DS=38; sev=blue]
- Combined pair badges `PURPLE`: `02`[DS=35; sev=purple], `25`[DS=35; sev=purple], `24`[DS=34; sev=purple], `16`[DS=31; sev=purple], `12`[DS=28; sev=purple], `28`[DS=26; sev=purple]
- Midday pair badges `RED`: `99`[DS=146; sev=red], `79`[DS=86; sev=red], `12`[DS=61; sev=red]
- Midday pair badges `BLUE`: `77`[DS=89; sev=blue], `33`[DS=82; sev=blue]
- Midday pair badges `PURPLE`: `66`[DS=45; sev=purple], `03`[DS=36; sev=purple], `09`[DS=31; sev=purple], `36`[DS=29; sev=purple], `34`[DS=28; sev=purple], `38`[DS=28; sev=purple], `49`[DS=27; sev=purple]
- Evening pair badges `RED`: `88`[DS=141; sev=red], `68`[DS=99; sev=red], `15`[DS=64; sev=red]
- Evening pair badges `BLUE`: `33`[DS=83; sev=blue], `78`[DS=49; sev=blue], `19`[DS=48; sev=blue], `18`[DS=42; sev=blue], `39`[DS=39; sev=blue], `16`[DS=38; sev=blue]
- Evening pair badges `PURPLE`: `44`[DS=54; sev=purple], `66`[DS=50; sev=purple], `11`[DS=41; sev=purple], `34`[DS=36; sev=purple], `29`[DS=35; sev=purple], `35`[DS=32; sev=purple]
- Cross-variant pair overlaps: `02`[Combined=purple/DS=35; Evening=purple/DS=28], `12`[Combined=purple/DS=28; Midday=red/DS=61], `16`[Combined=purple/DS=31; Evening=blue/DS=38], `25`[Combined=purple/DS=35; Evening=purple/DS=30], `33`[Combined=red/DS=165; Midday=blue/DS=82; Evening=blue/DS=83], `34`[Combined=red/DS=57; Midday=purple/DS=28; Evening=purple/DS=36], `38`[Combined=purple/DS=26; Midday=purple/DS=28], `49`[Combined=blue/DS=38; Midday=purple/DS=27], `66`[Combined=blue/DS=91; Midday=purple/DS=45; Evening=purple/DS=50], `78`[Combined=purple/DS=25; Evening=blue/DS=49]
- Combined boxed combo badges: `007`[DS=905; sev=B], `088`[DS=869; sev=B], `008`[DS=847; sev=B], `444`[DS=823; sev=B], `039`[DS=798; sev=B], `355`[DS=788; sev=B], `344`[DS=717; sev=B], `788`[DS=681; sev=B], `266`[DS=670; sev=B]
- Midday boxed combo badges: `559`[DS=990; sev=B], `288`[DS=977; sev=B], `255`[DS=948; sev=B], `668`[DS=930; sev=B], `199`[DS=878; sev=B], `499`[DS=804; sev=B], `399`[DS=787; sev=B], `039`[DS=775; sev=B], `448`[DS=764; sev=B], `005`[DS=756; sev=B]
- Evening boxed combo badges: `444`[DS=986; sev=B], `009`[DS=944; sev=B], `255`[DS=902; sev=B], `138`[DS=842; sev=B], `117`[DS=825; sev=B], `158`[DS=787; sev=B], `344`[DS=780; sev=B], `199`[DS=771; sev=B], `112`[DS=731; sev=B], `277`[DS=716; sev=B]
- Cross-variant boxed-combo overlaps: `039`[Combined=B/DS=798; Midday=B/DS=775], `199`[Midday=B/DS=878; Evening=B/DS=771], `255`[Midday=B/DS=948; Evening=B/DS=902], `344`[Combined=B/DS=717; Evening=B/DS=780], `444`[Combined=B/DS=823; Evening=B/DS=986]
- Combined badge-pressure top indices: `26`[PD=3.00; RAW=6], `32`[PD=2.00; RAW=4], `35`[PD=2.00; RAW=4], `29`[PD=1.83; RAW=11], `13`[PD=1.67; RAW=10], `17`[PD=1.67; RAW=10], `33`[PD=1.67; RAW=10], `34`[PD=1.67; RAW=10]
- Midday badge-pressure top indices: `35`[PD=2.50; RAW=5], `34`[PD=2.17; RAW=13], `26`[PD=2.00; RAW=4], `31`[PD=1.83; RAW=11], `20`[PD=1.67; RAW=10], `22`[PD=1.50; RAW=12], `25`[PD=1.50; RAW=9], `32`[PD=1.50; RAW=3]
- Evening badge-pressure top indices: `32`[PD=3.50; RAW=7], `23`[PD=2.83; RAW=17], `33`[PD=2.33; RAW=14], `29`[PD=2.17; RAW=13], `24`[PD=2.12; RAW=17], `8`[PD=2.00; RAW=16], `30`[PD=2.00; RAW=16], `16`[PD=2.00; RAW=4]

### G1b. Explicit due VTRAC inventory
- Combined due VTRAC overlay: `32`[DS=307], `26`[DS=264], `16`[DS=122], `6`[DS=85], `19`[DS=79], `11`[DS=65], `23`[DS=59], `5`[DS=58]
- Combined due VTRAC heatboard: `32`[DS=307; HZ=0.007; TR=1; AVG=135.500], `26`[DS=264; HZ=0.004; TR=-1; AVG=256.500], `16`[DS=122; HZ=0.007; TR=1; AVG=135.667], `6`[DS=85; HZ=0.026; TR=20; AVG=39.045], `19`[DS=79; HZ=0.026; TR=17; AVG=39.087], `11`[DS=65; HZ=0.053; TR=47; AVG=18.957], `23`[DS=59; HZ=0.024; TR=20; AVG=41.864], `5`[DS=58; HZ=0.020; TR=13; AVG=50.706]
- Midday due VTRAC overlay: `26`[DS=388], `1`[DS=373], `34`[DS=227], `16`[DS=185], `15`[DS=176], `32`[DS=153], `35`[DS=130], `28`[DS=75]
- Midday due VTRAC heatboard: `26`[DS=388; HZ=0.000; TR=0], `1`[DS=373; HZ=0.009; TR=0; AVG=109.600], `34`[DS=227; HZ=0.026; TR=18; AVG=38.000], `16`[DS=185; HZ=0.008; TR=-6; AVG=132.833], `15`[DS=176; HZ=0.029; TR=23; AVG=34.000], `32`[DS=153; HZ=0.007; TR=2; AVG=148.800], `35`[DS=130; HZ=0.004; TR=0; AVG=281.000], `28`[DS=75; HZ=0.035; TR=25; AVG=28.444]
- Evening due VTRAC overlay: `32`[DS=630], `23`[DS=169], `26`[DS=132], `18`[DS=129], `13`[DS=78], `33`[DS=63], `16`[DS=61], `30`[DS=60]
- Evening due VTRAC heatboard: `32`[DS=630; HZ=0.003; TR=0; AVG=306.000], `23`[DS=169; HZ=0.025; TR=15; AVG=39.737], `26`[DS=132; HZ=0.006; TR=1; AVG=176.500], `18`[DS=129; HZ=0.029; TR=21; AVG=34.360], `13`[DS=78; HZ=0.025; TR=19; AVG=40.190], `33`[DS=63; HZ=0.023; TR=15; AVG=43.333], `16`[DS=61; HZ=0.009; TR=1; AVG=110.125], `30`[DS=60; HZ=0.038; TR=33; AVG=26.114]
- Context reinforcement vs context-only pressure: `...`
- Policy relationship / handoff: `...`

## Part H — Translation Sandbox / Downstream Control Arm

### H0. File lock
- Translation sandbox JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.json`
- Translation sandbox MD: `sharepacks/_predictive/2026-01-15/Pennsylvania4/analysis/translation_sandbox_seed__tool_only__arena_v0.md`
- Candidate Universe JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/candidate_universe__tool_only__arena_v0.json`
- Play Card JSON: `sharepacks/_predictive/2026-01-15/Pennsylvania4/play_card__tool_only__arena_v0.json`
- Play Card MD: `sharepacks/_predictive/2026-01-15/Pennsylvania4/play_card__tool_only__arena_v0.md`

### H1. Auto-captured control-arm snapshot
- Candidate Universe summary: `packs=27` | `union_combos=208`
- Play Card summary: `analysis_prefix`[B12,B24,B36], `convergence_box_first`[B12,B24,B36], `conversion_box_first`[B12,B24,B36], `conversion_box_first_conditional_lenient_presetA`[B12,B24,B36]
- Translation Sandbox positional shortlist top: `344`, `034`, `134`, `013`, `444`, `447`, `114`, `044`
- Translation Sandbox BA canonicals: `049`, `058`, `238`, `247`, `067`, `148`, `256`, `346`
- Translation Sandbox profit canonicals: `239`, `244`, `446`, `469`, `699`
- Diagnostic boxed seed: `007`, `244`, `344`, `446`, `239`, `044`, `688`, `234`, `388`, `447`, `009`, `004`, `006`, `255`, `228`, `249`
- Diagnostic straight seed: `443`, `404`, `403`, `143`, `103`, `444`, `447`, `141`, `007`, `070`, `700`, `244`, `424`, `442`, `344`, `434`
- Diagnostic VT-box seed: `31`, `30`, `25`, `33`, `23`, `18`, `15`, `32`, `3`, `None`, `4`, `29`
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
