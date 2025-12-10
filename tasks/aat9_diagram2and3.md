Diagram 2 – Brain 1: per‑state analyzers and brain bundles

Now we zoom into a single state (say Connecticut4) and show how the three main analyzers + Hot Zones produce the brain bundles the Aggregator and Control Center will rely on.

flowchart LR
  %% INPUTS
  subgraph INPUT["Connecticut4 – Inputs"]
    CT_TABLES[Combined tables\n(data/outputs/tables/Connecticut4/\nMidday_combined.csv,\nEvening_combined.csv,\nCombined_combined.csv)]
    CT_JSON[JSON tables\n(data/outputs/json_tables/Connecticut4_tables.json)]
  end

  %% STABLE
  subgraph STABLE_AREA["Stable Pattern Extractor"]
    ST_ENGINE[stable_pattern_extractor.py\n→ alpha_analytical/stable]
    ST_SCORES[CT_stable_patterns_scores.csv]
    ST_FAM[CT_stable_patterns_families.csv]
    ST_COMP[CT_stable_patterns_compound.csv]
  end

  %% DIGIT
  subgraph DIGIT_AREA["Digit Reduction – Analyzer V2"]
    DR_ENGINE[module_b_digit_reduction.py\n+ analyzer_v2 pipeline]
    DR_PER[CT_analyzer_v2_per_item.csv]
    DR_TOP[CT_analyzer_v2_top_candidates.csv]
    DR_META[CT_analyzer_v2_meta.json]
    DR_STEPS[training/CT_digit_reduction_steps.csv]
  end

  %% VTRAC
  subgraph VTRAC_AREA["V‑TRAC Analyzer"]
    VT_ENGINE[module_c_vtrac.py]
    VT_ANALYZER[Analyzer CSV/JSON\n(data/outputs/analysis/vtrac/Connecticut4/…)]
    VT_COMPACT[vtrac_compact_report.csv/json]
  end

  %% HOT ZONES
  subgraph HZ_AREA["Hot Zones (JSON‑tables)"]
    HZ_ENGINE[hot_zones CLI\nalpha_analytical/hot_zones/…]
    HZ_PER[CT_hot_zones_per_lane.csv]
    HZ_TOP[CT_hot_zones_top_lanes.csv]
    HZ_META[CT_hot_zones_meta.json]
  end

  %% WIRES
  CT_TABLES --> ST_ENGINE
  CT_TABLES --> DR_ENGINE
  CT_TABLES --> VT_ENGINE
  CT_JSON --> HZ_ENGINE

  ST_ENGINE --> ST_SCORES
  ST_ENGINE --> ST_FAM
  ST_ENGINE --> ST_COMP

  DR_ENGINE --> DR_PER
  DR_ENGINE --> DR_TOP
  DR_ENGINE --> DR_META
  DR_ENGINE --> DR_STEPS

  VT_ENGINE --> VT_ANALYZER
  VT_ENGINE --> VT_COMPACT

  HZ_ENGINE --> HZ_PER
  HZ_ENGINE --> HZ_TOP
  HZ_ENGINE --> HZ_META

How this matches the “brain bundle” contracts

Stable brain bundle

data/outputs/analysis/patterns/<STATE>/

<STATE>_stable_patterns_scores.csv (full matrix per cell).

<STATE>_stable_patterns_families.csv (family aggregates).

<STATE>_stable_patterns_compound.csv (Packet‑2 compound features).

Digit brain bundle

data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/ with per_item, top_candidates, meta, plus stacked HTML previews.

Per‑item rows include all the features you care about (vt_only_lane, funnel_precol1, ls_col_42, ls2_lane, scores, reasons_json, dr.win_* flags).

Training exports add steps.csv and logs for deeper inspection.

V‑TRAC outputs

Analyzer outputs live under data/outputs/analysis/vtrac/<STATE>/ along with evidence grids and compact reports.

Hot Zones brain bundle

Uses JSON tables as input and writes <STATE>_hot_zones_per_lane.csv, <STATE>_hot_zones_top_lanes.csv, and <STATE>_hot_zones_meta.json (as described in your wiring and validation docs).

Key takeaway:
For each state/date, “Brain 1” produces four brain bundles (Stable, Digit, V‑TRAC, Hot Zones). These are already in a lean, per_item/top/meta style for Digit and partially for Stable/V‑TRAC, exactly so the Aggregator can read them later without wading through heavy winners bundles.

_____________________________________________


Diagram 3 – Aux / Blackapple & Brain 2 (Control Center + Winners + Aggregator)

This diagram focuses on the draws‑only brain (Aux/BA) and how Control Center + Winners sit on top of everything.

flowchart TB
  %% DRAWS BRAIN
  subgraph D0["Draws‑Only Brain – Aux & Blackapple"]
    D_DRAWS[Draws CSVs\n(data/cleaned/*_draws.csv)]
    subgraph AUXP["Auxiliary Tools page"]
      POS[Positional Pressure\npositional_tool.py\n(shortlists + evidence)]
      DOUBLES[Hot Families & doubles\nanalyze_pairs.py\n+ V‑TRAC overlays]
      SUMS[Sums analytics\nsums_analysis.py]
    end
    subgraph BA["Blackapple Analyzer"]
      BA_ENGINE[modules/blackapple.py\n(core BA logic)]
      BA_ALERTS[BA alerts & candidates\n(rendered in app)]
    end
  end

  %% CONTROL CENTER / WINNERS
  subgraph C0["Brain 2 – Control Center & Winners"]
    CC_MAIN[Control Center main panel\n(state dashboards,\nTables Pipeline controls)]
    CC_DOUBLES[Cross‑state doubles table\n+ BA summary row per state]
    CC_VTRAC[V‑TRAC heatboard\n(index pressure, trend, gaps)]
    CC_BATCH[Batch runner\n(tables regen + Stable/Digit/V‑TRAC/HotZones\n+ centralized winners)]
    WIN_VT[Winners Logger – V‑TRAC report\n(quick VT winner view)]
    WIN_FULL[Winners Logger – Analyzer‑style full report\n(3‑pane HTML from tables)]
  end

  %% AGGREGATOR
  subgraph A0["Future Aggregator (Brain 2 – scoring layer)"]
    AGG_ENGINE[AAT9 Aggregator engine\n(reads brain bundles + Aux signals\n+ winners flags)]
    AGG_OUTPUT[Synergy outputs\n(final pattern shortlist + scores)]
  end

  %% WIRES
  D_DRAWS --> POS
  D_DRAWS --> DOUBLES
  D_DRAWS --> SUMS
  D_DRAWS --> BA_ENGINE
  BA_ENGINE --> BA_ALERTS

  POS --> CC_DOUBLES
  DOUBLES --> CC_DOUBLES
  SUMS --> CC_DOUBLES
  BA_ALERTS --> CC_DOUBLES

  CC_DOUBLES --> CC_MAIN
  CC_VTRAC --> CC_MAIN

  CC_BATCH --> WIN_VT
  CC_BATCH --> WIN_FULL

  %% AGG FEEDS
  POS --> AGG_ENGINE
  DOUBLES --> AGG_ENGINE
  SUMS --> AGG_ENGINE
  BA_ALERTS --> AGG_ENGINE

  CC_BATCH --> AGG_ENGINE
  WIN_FULL --> AGG_ENGINE
  AGG_ENGINE --> AGG_OUTPUT

Why this matches your Aux + Control Center wiring

Aux overview: Aux Tools and Control Center are explicitly defined as a draws‑only analytics brain that uses data/cleaned/*_draws.csv, with variants (Combined/Midday/Evening) all resolved via modules.aux_loaders.load_state_draws.

Control Center functions:

Cross‑state doubles table + BA summary using draws CSVs.

V‑TRAC heatboard plus sums analytics surfaced both in Aux and Control Center.

Positional Pressure panel (with All‑Variant / Midday / Evening grids) and its shortlist logic is described in Aux docs.

Winners module:

The “V‑TRAC winner report” and “Analyzer‑style full report” are separate logger tools wired in your Winners Module doc, using either VT‑index overlays or full 3‑pane HTML based on tables.

Aggregator design:

README_AAT9 and the Architecture Overview both describe an Aggregator module that consumes Stable, Digit, and Hot Zones outputs and produces a synergy JSON; your newer Aggregator notes extend that to lean brain bundles and Control Center outputs as the inputs.

Right now, Aggregator is designed and contracted but not yet exposed as a live page. This diagram shows exactly where it will sit: a Brain 2 scoring layer on top of:

Brain 1 brain bundles (from Diagram 2),

Aux & BA signals (this diagram), and

Winners maps/flags from Control Center.

5. How this all ties back to Brain 1 vs Brain 2 for the final master diagram

To connect this back to the Brain‑1/Brain‑2 language in your Master Validation Framework:

Brain 1 = per‑state analyzers on the string tables, plus Hot Zones. Each state/day gets a local brain bundle (Stable/Digit/V‑TRAC/Hot Zones).

Brain 1’ (draws‑only brain) = Aux/Blackapple on draws CSVs, giving you doubles/BA/positional/sums signals per state.

Brain 2 = Control Center + Aggregator, which:

orchestrates table generation and analyzer batches,

centralizes winners logging and QA counters, and

will eventually compute cross‑tool, cross‑state synergy scores from all brain bundles + Aux signals.

From here, for Part 3+ of the architecture, we can:

Drill into exact feature‑level contracts the Aggregator will use (e.g., Digit’s vt_only_lane, ls2_lane, Stable’s compound_score, Hot Zones’ lane scores, Aux positional evidence).

Map Brain 2 scoring layers (A01–A12 profitability indicators, environment labels, etc.) onto these inputs using the Final Validation and Profit Blueprint docs.

6. How to turn this into the official AAT9 architecture doc

You can paste these three diagrams into a new markdown such as:

docs/AAT9_DOCS/AAT9_Architecture_Final.md

and add a short header like:

Part 1 – Bird’s‑eye module flow (you already have this in ARCHITECTURE_AAT9.md).

Part 2 – Runtime wiring (the three diagrams above).

Part 3 – Aggregator contracts & scoring layers (we’ll design next).

Sanity‑check actions for you

Visual check: Drop these three mermaid blocks into your repo’s docs and render them (GitHub or your markdown viewer). Confirm node labels and paths match what you see on disk for one state (e.g., Connecticut4).

Path check: For each tool tab in the app, run it once for a small date range and confirm the outputs land in the folders shown here (data/outputs/analysis/...). If any path differs, we’ll tweak the diagram in the next iteration.

When you’re ready, we can move to Part 3, where we define the Aggregator view: exactly which columns from each brain bundle + Aux signal + winners flag flow into the final scoring matrix.