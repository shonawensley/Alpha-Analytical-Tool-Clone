This part turns all the pieces you’ve wired (tables → tools → lean outputs → winners logs) into a clear Brain‑2 architecture:

what the Aggregator will actually read,

how the 12 A01–A12 profit indicators sit on top,

and how Control Center uses both to drive “play / don’t play” and final combinations.

I’ll treat this as Architecture Part 3 – Brain‑2 Aggregator & Profit Layer, assuming Parts 1–2 already covered pipeline + Brain‑1 tools.

3.0 Brain‑2 in One Picture

Conceptual role:

Brain 1 = per‑state engines: Stable, Digit Reduction, V‑TRAC, Hot Zones, Aux/Blackapple. They consume tables/JSON and emit lean analysis bundles and overlays.
(See live wiring + lean outputs spec: Digit, Stable, V‑TRAC, Hot Zones all publish under data/outputs/analysis/<tool>/<STATE>/… with per‑item/top/meta bundles. /mnt/data/AAT9_Live_Wiring_and_Data_Paths.md, /mnt/data/AAT9_Analyzer_Lean_Outputs.md)

Brain 2 = two layers:

Central Winners Module + A01–A12 alerts (profit blueprint / Control Center alerts).

Module D Aggregator (synergy scoring over Brain‑1 outputs + Aux features), feeding Control Center and, eventually, play slips.
(Aggregator and profit indicators are laid out in module_D_aggregator.md, THE PROFIT BLUEPRINT.md, and Architecture and Master Validation Framework.)

High‑level flow (target architecture):

flowchart LR
  subgraph Inputs["History + Results"]
    H[Pick3StatsC4_xxx.xlsm<br/>history workbook]
    R[data/results/YYYY-MM-DD.txt<br/>official results]
  end

  subgraph Tables["Core Tables Pipeline"]
    T1[run_tables_with_guard.py<br/>Combined/Midday/Evening CSV]
    T2[json_tables mirrors<br/>STATE_tables.json]
  end

  subgraph Brain1["Brain 1 — Per-State Engines"]
    ST[Stable Pattern<br/>stable_patterns_*.csv/json]
    DR[Digit Reduction<br/>analyzer_v2_per_item/top/meta]
    VT[V-TRAC Analyzer<br/>vtrac_analyzer + compact_report]
    HZ[Hot Zones<br/>hot_zones_per_lane/top/meta]
    AUX[Aux / Blackapple<br/>draws-only features]
  end

  subgraph Winners["Central Winners Module"]
    WM[winners_map.{json,csv}<br/>winner_flags.csv<br/>hit classes exact/box/VT]
  end

  subgraph Brain2["Brain 2 — Profit Layer (Control Center)"]
    IND[A01–A12 profit indicators<br/>+ BA/Repeat/Due-Doubles alerts]
    AGG[Module D Aggregator<br/>synergy scores per pattern/family]
    CC[Control Center UI<br/>boards + state dashboards]
  end

  H --> T1 --> T2
  T1 --> ST
  T1 --> DR
  T1 --> VT
  T2 --> HZ

  R --> WM
  ST --> WM
  DR --> WM
  VT --> WM
  HZ --> WM

  ST --> AGG
  DR --> AGG
  VT --> AGG
  HZ --> AGG
  AUX --> AGG

  WM --> IND
  ST --> IND
  DR --> IND
  VT --> IND
  HZ --> IND
  AUX --> IND

  IND --> CC
  AGG --> CC


What is real today:

Brain‑1 tools + tables pipeline are fully wired and emitting lean bundles and winners overlays. (AAT9_Live_Wiring_and_Data_Paths.md, AAT9_Analyzer_Lean_Outputs.md, Digit/Stable/VTRAC/Hot Zones module docs)

A prototype winners log already exists (build_winners_log.py → winners_map.{json,csv}) with 4 hit classes: exact_straight, exact_boxed, vt_boxed, vt_straight. (AAT9_Winners_Module.md)

Control Center already shows Blackapple alerts and doubles boards, plus system health, and has hooks for winner reports. (AAT9_Roadmap_2025-09-03_Winners_Logging_and_Health.md)

What is design‑level (to be implemented):

Module D aggregator as a first‑class module that reads the lean bundles and produces a unified synergy view. (module_D_aggregator.md)

Full wiring of the 12 indicators A01–A12 as formal alert objects fed by the Brain‑1 metrics and Aux signals. (THE PROFIT BLUEPRINT.md)

Part 3 is about making those design‑level pieces concrete and structured so you can implement them safely.

3.1 Aggregator Inputs — Exact Contracts from Brain 1

Here’s the “shopping list” of what Module D actually needs to read, based on the current lean‑outputs spec and your winners module.

3.1.1 Core analyzer bundles (per tool / per state / per date)

Digit Reduction (Analyzer V2)
data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/
From lean spec: per‑item + top + meta + stacked HTML. Key columns: earliest/persistence, vt_only_lane, funnel_precol1, ls_col_42, ls2_lane, dr.win_* flags. (AAT9_Analyzer_Lean_Outputs.md, Digit section)

For aggregator, we care about:

Per‑item CSV per candidate triad / VT family:

Evidence timing: earliest_exact, earliest_vtrac, persistence_steps

Lane identity: vt_only_lane, ls2_lane, funnel_precol1, ls2_progress

Outcome flags (from winners): dr.win_exact_straight, dr.win_exact_boxed, dr.win_vt_boxed, dr.win_vt_straight

Top‑candidates CSV:

Rank per candidate; aggregator can treat Brain‑1 rank as one feature.

Stable Pattern (Packet‑2)
data/outputs/analysis/patterns/<STATE>/
Contract: scores, families, compound, metrics. (AAT9_Analyzer_Lean_Outputs.md, Stable section)

Aggregator inputs:

*_stable_patterns_scores.csv:

score_* components, persistence, VT‑straight, double‑mirror metrics.

*_stable_patterns_families.csv:

round_score, hot1_count, hot2_count, consensus_hits, etc.

*_stable_patterns_compound.csv:

compact roll‑up including chain_depth, funnel_precol1, vt_only_lane, compound_why.

*_metrics.json:

winners array, metadata, signals.hot2_bias, signals.consensus_of_consensus etc.

V‑TRAC Analyzer
data/outputs/analysis/vtrac/<STATE>/

Current outputs include analyzer CSV/JSON and compact reports with winner_map and winner_flags (to be centralized, but for aggregator you mainly need per‑pattern VT evidence). (AAT9_Analyzer_Lean_Outputs.md, V‑TRAC section)

Aggregator inputs:

Per‑candidate VT index, VT straight flags, family tags, and any “compact score” summarizing recency, lane quality, etc.

Hot Zones
data/outputs/analysis/hot_zones/<STATE>/

Brain bundle mirrors Digit/Stable: per‑lane + top + meta + winners map. (AAT9_Analyzer_Lean_Outputs.md, Hot Zones section)

Aggregator inputs:

*_hot_zones_per_lane.csv:

lane‑level evidence: vt_only_lane, funnel_precol1, col1_arrival, ls2_lane.

*_hot_zones_top_lanes.csv:

aggregated lane scores, cross‑variant spans, set spans.

Aux / Blackapple

Aux tools are draws‑only, reading data/cleaned/*_draws.csv and producing signals like pair‑pressure, consensus, mirror pressure, etc. (AAT9_Aux_Tools_Official.md, AAT9_Auxiliary Feature Integration.md)

For aggregator, we don’t need entire Aux outputs, we need:

Feature vector per candidate / pair / family, e.g.:

aux_pair_is_RED, aux_pair_is_BLUE,

aux_positional_hot,

aux_double_pressure_rank,

aux_mirror_bias.

Docs recommend treating each as a separate keyed feature with config weights (“strings lead, aux compounds”). (AAT9 Auxiliary Feature Integration.md)

3.1.2 Winners ground truth (Central Winners Module)

The winners module already defines a canonical label per winner:

exact_straight, exact_boxed, vt_boxed, vt_straight. (AAT9_Winners_Module.md)

And it prototypes a script:

python scripts/tools/build_winners_log.py --date 2025-06-24


writing:

winners/2025-06-24/2025-06-24_winners_map.{json,csv}

Each row merges Stable and VT/DR evidence: which families were hit, which VT index, etc. (AAT9_Winners_Module.md)

Brain‑2 contract:

Aggregator treats winners_map as labels when training thresholds or ML, and as a daily audit spine when validating A01–A12 alerts and synergy logic.

3.2 Inside Module D — Synergy Engine Design

Your dedicated doc for this is module_D_aggregator.md. The key design points:

3.2.1 Input JSONs and CLI

Module D is intended to ingest JSON summaries per tool and emit a unified aggregator_synergy.json. Example CLI:

python aggregator.py \
  --stable stable_patterns.json \
  --digit digitreduce_patterns.json \
  --hot hotzone_patterns.json \
  --recent_draws last6_draws.json \
  --output aggregator_synergy.json


(From module_D_aggregator.md.)

Under the hood, those JSONs should be thin views over the Brain‑1 lean bundles—basically one record per candidate triad/family with:

candidate id (state, date, variant, triad key or family id),

main Stable score metrics,

main Digit metrics (vt_only_lane, ls2_lane, funnel_precol1, etc.),

Hot Zones lane metrics,

Aux feature flags.

3.2.2 Synergy scoring layers

Module D then applies synergy rules, based on your architecture doc:

Base score from each tool (e.g., Stable compound score, Digit top‑candidate rank, Hot Zones lane score). (AAT9 Architecture and Master Validation Framework.md, Aggregator section)

Cross‑tool bonuses:

Examples from module_D_aggregator.md and Architecture & Master Validation:

cross_module_bonus when the same candidate is Top‑N in 2+ tools.

hot_star_bonus / hot_super_bonus when Hot Zones and Stable agree on a column/triad.

pending_bonus / three_value_bonus when Digit reveals VT‑only + LS2 ladder + 3‑value funnels.

Config is meant to be data‑driven:

{
  "cross_module_bonus": 3,
  "hot_star_bonus": 2,
  "hot_super_bonus": 4,
  "pending_bonus": 3,
  "three_value_bonus": 2
}


(Module D doc.)

These weights are tunable without touching the tools themselves—critical for keeping Master Validation + ML flexible.

3.2.3 Aggregator output: what Brain‑2 sees

The aggregator’s output row for each candidate should look roughly like:

Keys:

state, date, variant, triad_id/family_id.

Scores:

score_stable, score_digit, score_vtrac, score_hot_zones, score_aux,

synergy_score_total, synergy_explain.

Feature flags:

stable_hot1, stable_hot2, digit_vt_only_lane, digit_ls2_lane,

vtrac_repeat_flag, hot_zone_star, etc.

Label linkages:

winner_exact_straight, winner_exact_boxed, winner_vt_boxed, winner_vt_straight
(read from the winners log when available).

Result: a single per‑candidate record that Brain‑2 can rank, filter, and reason over.

3.2.4 Aggregator in the architecture

Small, focused diagram:

flowchart LR
  subgraph S1["Per-State Lean Bundles"]
    ST[Stable families/compound]
    DR[Digit per_item/top]
    VT[V-TRAC compact]
    HZ[Hot Zones top_lanes]
    AUX[Aux feature vectors]
  end

  subgraph S2["Module D Aggregator"]
    M1[Feature Join<br/>(by state/date/triad)]
    M2[Synergy Scorer<br/>(config weights)]
    M3[Aggregator Output<br/>aggregator_synergy.json/csv]
  end

  ST --> M1
  DR --> M1
  VT --> M1
  HZ --> M1
  AUX --> M1

  M1 --> M2 --> M3

3.3 The 12 Profit Indicators (A01–A12) as a Layer on Top

THE PROFIT BLUEPRINT.md defines a 12‑indicator grid. Each indicator has:

a Trigger (pattern / evidence condition)

a Shrink effect (how much it reduces the universe)

a Sooner effect (why hits cluster)

a Straight effect (how cheaply you can tilt toward straights)

The blueprint explicitly says: “Key profit levers shown per indicator: Shrink (how it reduces search space), Sooner (why hits cluster), Straight (when we can safely overlay 8–4–2–1).” (Profit blueprint, indicator table.)

3.3.1 High‑level map (what each alert “means”)

Based on the indicator table in the blueprint:

A01 – Dual Tail Consensus + 3‑Value Support

Trigger: same 2‑digit tail appears in ≥3 of R2/R4/R6/R8 (Set1) with BA foundation OK.

Shrink: ~6–12 box lines.

Sooner: consensus concentrates near‑term mass.

Straight: overlay when A05/A12 present.

A02 – Doubles Proof & Mirror‑Double Bias

Trigger: doubles family dominates rows or mirrors align.

Shrink: 3 permutations only.

Sooner: doubles cycle quickly.

Straight: cheap straight path by nature.

A03 – Cross‑Variant Consensus

Trigger: Midday & Evening share same tail “bag” today.

Shrink: shared coverage across sections.

Sooner: cross‑agreement accelerates.

Straight: overlay with A05/A12 or A09 echo.

A04 – Set2 Carry / Persistence

Trigger: same canonical/tail echoed yesterday (Set2).

Shrink: re‑use tiny family.

Sooner: carry shortens time‑to‑hit.

Straight: boost overlay priority.

A05 – Permutation Drift Straight‑Lean

Trigger: perm=1 or dominance beyond threshold in R2/R4/R6/R8.

Shrink: N/A (still box).

Sooner: order stabilizes.

Straight: enables clamp to 4/2/1.

A06 – BA Foundation Filter (27–29 pairs)

Trigger: all internal pairs within BA’s remaining set.

Shrink: removes noise.

Sooner: BA alert weeks cluster wins.

Straight: foundation + A01 → safe overlay.

A07 – Mirror Side Tilt

Trigger: mirror side imbalance in data.

Shrink: prefer one side of mirror.

Sooner: resolves ambiguity.

Straight: tilt straights toward “star side”.

A08 – BA Tempo / Remaining‑Pairs Density

Trigger: BA “tempo” window; smallest viable families.

Shrink: small, dense families.

Sooner: tempo days hit earlier.

Straight: with A01/A11, justify overlay.

A09 – V‑TRAC Index Echo (ordered/bag)

Trigger: today’s VT index matches Set2 (ordered or bag).

Shrink: 8 straights only.

Sooner: true repeats fire within days.

Straight: ordered echo + A05 → 2/1.

A10 – 3‑Value Repeat / End‑of‑Progression Trap

Trigger: only one 3‑value remains in box or repeats across rows.

Shrink: often 8‑index box.

Sooner: end‑stage tends to resolve.

Straight: link to A05/A12.

A11 – Hot‑Zones Star (Consensus Radar)

Trigger: Consensus + Set2 echo + X‑Var + DR + BA weigh to ?/??/???.

Shrink: pick only ??/??? columns.

Sooner: high‑star columns hit sooner.

Straight: level‑gated overlay.

A12 – Digit Reduction Clamp (DR Pins)

Trigger: 1–3 positions pinned by DR/VT pair.

Shrink: 8→4→2→1 ladder.

Sooner: pinned positions collapse order.

Straight: enables ultra‑cheap straights.

The blueprint sums it up:

A01/A03/A11 tell you where to look.
A04/A09/A10 tell you when it repeats.
A05/A12/A02 tell you how to take the straight cheaply.
A06/A08 keep you on good foundation/tempo days.
A07 decides mirror side.
(Paraphrased from THE PROFIT BLUEPRINT.md.)

3.3.2 What data each alert needs (Brain‑1 → Brain‑2)

This is where your architecture work pays off: almost every alert can be implemented as a function of existing Brain‑1 outputs + Aux:

Alert	Data it needs (source)
A01 – Dual Tail Consensus	Stable tail families (stable_patterns_families), DR ladder tail counts, BA foundation pairs (Aux).
A02 – Doubles / Mirror Bias	Aux doubles pressure + Stable/VTRAC flags for double/mirror families.
A03 – Cross‑Variant Consensus	Stable & DR cross‑variant echoes (Combined vs Midday vs Evening) + winners evidence.
A04 – Set2 Carry	Digit & Stable “yesterday” features (Set2) exposed through compound metrics + winners overlay (Set2 → Set1 paths).
A05 – Perm Drift Straight‑Lean	Digit per‑item perm_*/order stability metrics (already tracked in steps & features).
A06 – BA Foundation	Blackapple “foundation set” for pairs + current candidate coverage.
A07 – Mirror Side Tilt	Aux and Stable mirror‑side scores (already part of Stable metrics + draws_features).
A08 – BA Tempo / Density	BA tempo and remaining‑pairs density (Aux modules over draws).
A09 – VT Index Echo	V‑TRAC compact report + winners log: whether today’s index matches Set2’s index.
A10 – 3‑Value Repeat Trap	Digit Reduction long‑string ladders + Stable 3‑value cluster metrics.
A11 – Hot‑Zones Star	Hot Zones per‑lane star levels combined with Stable/DR consensus and Set2 echo.
A12 – DR Clamp	Digit vt_only_lane, ls2_lane, funnel_precol1, ls2_progress + pinned position counts.

Architecturally:

You do not need new tools for A01–A12.

Everything comes from Stable/Digit/V‑TRAC/Hot Zones/Aux + winners logs.

You do need to surface the right features in a way Brain‑2 can query quickly (which is exactly what the lean bundles + winners_map + Aux feature vectors already establish).

3.3.3 Alerts layer in the architecture

Structure the indicators as a thin layer over aggregator + winners:

flowchart LR
  subgraph B1["Brain 1 Outputs"]
    ST[Stable compound/families]
    DR[Digit per_item/top]
    VT[V-TRAC compact]
    HZ[Hot Zones per_lane/top]
    AUX[Aux features]
    WM[winners_map + winner_flags]
  end

  subgraph B2["Brain 2 — Alerts Layer"]
    A01A12[A01–A12 Alert Engine<br/>(rules + thresholds)]
  end

  ST --> A01A12
  DR --> A01A12
  VT --> A01A12
  HZ --> A01A12
  AUX --> A01A12
  WM --> A01A12


Each alert is basically:

A0x_alert = f_x(ST_metrics, DR_metrics, VT_metrics, HZ_metrics, AUX_flags, WM_recent)


and returns:

is_firing (bool),

confidence (e.g. 0–1),

shrink_factor,

straight_bias_level.

These become columns on the state/day record and are what Brain‑2 uses to gate play and risk.

3.4 How Brain‑2 Drives Control Center and Final Workflow

Now we connect it back to the app and to Master Validation.

3.4.1 Control Center as Brain‑2 surface

Control Center is already documented as the cross‑state dashboard that aggregates metrics from tools and Aux to decide whether states are favorable and to manage profitability across the portfolio. (AAT9_Macro_Roadmap.md, AAT9 Architecture and Master Validation Framework.md)

In the final state:

Each date/state row in Control Center has:

Environment metrics from Brain‑1: hit counts, vt_only lanes, LS2 lanes, Hot Zones stars, etc.

A01–A12 flags + BA alerts (foundation, tempo) + VTRAC repeat and due‑doubles.

Aggregator synergy summaries: top candidates, pattern families, coverage stats.

Profit trackers (12 trackers from the Profit Blueprint) keyed per state and per alert combination.

The daily Brain‑2 loop is:

Swap workbook + regenerate tables/JSON (Master Validation Preflight / String Table SOP).

Run Control Center batch to:

regenerate winners HTML / winners_map,

run Stable/Digit/V‑TRAC/Hot Zones batches,

refresh Aux/BA stats. (AAT9_Control_Center_Batch_Workflow.md style docs; Backtesting/Preflight SOPs)

Module D Aggregator computes synergy per candidate and writes aggregator_synergy.

Alert engine computes A01–A12 per state/day using aggregator + Brain‑1 metrics.

Control Center renders:

state dashboards (Brain‑1 view),

alert board (Brain‑2 view),

optional “play board” / candidate lists (combined view).

3.4.2 Relation to Master Validation templates (Brain‑1 vs Brain‑2)

From the Final Validation docs:

Brain‑1 master validation = per‑state, per‑tool, pattern‑focused review (digit ladders, stable families, VT lanes, Hot Zones), using HTML + overlays + lean bundles. (AAT9_Final_Validation_Help.md, FINAL_VALIDATION_TEMPLATE* in tasks)

Brain‑2 control template = cross‑state, indicator/alert‑focused daily checklist (which A0x fired where, which hit, cost posture, etc.). (final_validation_control.md, THE PROFIT BLUEPRINT.md)

The architecture we just laid out matches that split:

Module D + lean bundles = mechanical aggregator you can trust as a data feed.

A01–A12 = profit layer you use to decide:

which environments to play at all,

whether to overlay straights (and how heavily),

how to adjust progression.

The Master Validation work you’re about to do is essentially:

walking through examples using these structures,

confirming which Brain‑1 features and alert combinations actually cluster winners,

and deciding which parts of the architecture to lock in for v1 of the super‑brain.

3.5 How to Use This Part (Concrete next actions)

So you can actually use this architecture doc as an implementation guide, here’s how I’d treat Part 3 inside the repo:

Create a dedicated doc like
docs/AAT9_KIT/AAT9_Architecture_Brain2_Aggregator.md
and drop this Part 3 there.

Wire contracts in code exactly as described:

Ensure each Brain‑1 tool writes the lean bundle columns that A01–A12 need (if any are missing, add them in add‑only fashion).

Confirm build_winners_log.py produces winners_map in a shape that Module D and the alert engine can join on (state/date/variant/triad).

Implement Module D to read the lean bundles and write aggregator_synergy.{json,csv}.

Stub alert engine A01–A12:

Implement them as pure functions that take “feature snapshot” rows and return is_firing, confidence, shrink, straight_bias.

Start by logging their outputs in Control Center without changing play rules.

Use Master Validation to calibrate:

When you run your Brain‑1 templates per state, also look at:

which A01–A12 would have fired,

what the aggregator scores for the winners vs near‑misses.

Adjust config.yml for Module D (synergy weights) and alert thresholds accordingly.

Keep everything documented:

Whenever you change a feature or contract, update:

AAT9_Analyzer_Lean_Outputs.md,

AAT9_Unified_Changelog.md,

this Brain‑2 architecture doc.

If you’d like, the next step can be:

a schematic “data schema” table for aggregator_synergy and for an A01–A12_alerts.csv (column names and types), so you can implement them without guesswork.