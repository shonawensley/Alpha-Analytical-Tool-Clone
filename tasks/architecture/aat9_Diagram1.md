1. Big picture: what AAT9 is (for the diagram)

From the curated README + architecture docs:

AAT9 is a modular analytics suite for:

Generating standard CSV tables per state (Midday/Evening/Combined),

Analyzing Stable patterns (Module A),

Digit Reduction (Module B),

Hot Zones (Module C),

Aggregating findings with synergy logic (Module D / future Brain‑2).

The integrated app launches via run_app.bat → streamlit run src\app.py, and all pages use in‑repo modules: utils.path_handler, modules.blackapple, modules.aux_loaders, alpha_analytical.stable.

Data contracts (hard rules):

Aux/Blackapple (Aux tools) read draws‑only CSVs under data/cleaned/*_draws.csv.

V‑TRAC / Stable / Digit Reduction read combined tables under tables/<STATE>/ or data/outputs/tables/<STATE>/ via utils.path_handler.

Combined is the baseline dataset; Midday/Evening are additive variants, never replacements.

That’s the core framing of Part 1: separate worlds for:

String‑table analyzers (Brain‑1): Stable, Digit, V‑TRAC, Hot Zones on combined tables.

Aux / Blackapple (draws‑only “side brain”): doubles, positional pressure, BA alerts.

Control Center (Brain‑2 surface): cross‑state doubles, winners/batch, and (future) aggregator reading tool outputs.

2. Data & validation layer (before any analyzer runs)

a) History workbook + results files

Daily workbooks live under data/history/ as Pick3StatsC4_YYYY-MM-DD.xlsm.

Matching draw outcomes live in data/results/YYYY-MM-DD.txt (one day after the workbook date).

b) Guarded table generation

The canonical guard pipeline is:

run_tables_with_guard – scripts/tools/run_tables_with_guard.py --history-file Pick3StatsC4_YYYY-MM-DD.xlsm

Writes combined tables for all tracked states under
data/outputs/tables/<STATE>/{Combined_Combined,Midday_Combined,Evening_Combined}.csv.

Writes JSON mirrors under data/outputs/json_tables/<STATE>_tables.json.

Maintains data/outputs/tables/tables_manifest.json linking each run to the workbook path/mtime.

Guard rule: Set1/Draw1 in Combined_Combined.csv must match the history workbook; associated results are always day + 1.

c) Winners generation

A second script, generate_winners_from_results.py, turns data/results/YYYY-MM-DD.txt into winners HTML/JSON under reports/stable/winners_by_date/YYYY-MM-DD/<STATE>/.

d) Final validation loop

The Final Validation help doc ties this into one master checklist: Stage 1 tables + JSON, Stage 2 winners HTML/JSON, Stage 3 Digit Reduction batch, all driven from the same workbook/results pair for 14 tracked states (CT, DE, FL, IN, MI, NJ, NY, NC, OH, OntarioCanada, PA, PR, SC, VA).

Conclusion for Part 1:
Your data layer is already architected as a deterministic “Excel → guarded tables → winners” pipeline. The diagram should treat that as a single, validated data spine that both Brain‑1 and Aux / Control Center sit on top of.

3. Brain‑1: per‑state string‑table analyzers (what’s actually wired)

The Live Wiring doc is explicit about engines and I/O per tool.

3.1 Stable Pattern Extractor (Module A)

Engine: src/core/stable_pattern_extractor.py → alpha_analytical/stable.

Inputs: data/outputs/tables/<STATE>/ (Combined tables).

Outputs (brain bundle): in data/outputs/analysis/patterns/<STATE>/

<STATE>_stable_patterns_scores.csv + HTML report (scores per family).

<STATE>_stable_patterns_families.csv via post‑pass aggregation.

Optional winner spotlights: <STATE>_winner_family_spotlight_{raw,families}.csv.

3.2 Digit Reduction (Module B)

Engine: src/core/module_b_digit_reduction.py.

Inputs: same Combined tables per state.

Outputs (two layers):

Reducer: tabbed/stacked HTML + summary CSV + steps CSV under
data/outputs/analysis/digit_reduction/<STATE>/.

Analyzer V2 (brain bundle): data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/ with
per_item.csv, top_candidates.csv, meta.json, plus stacked HTML per variant and optional _steps.csv.

Training sets: .../training_sets/<STAMP>/ mirroring the analyzer bundle + steps.

Digit’s lean bundle is explicitly described as “brain bundle” fields that the future Aggregator will consume (vt_only_lane, funnel flags, LS2 flags, etc.)—that’s the main reason we keep this structure in the final diagram.

3.3 V‑TRAC Analyzer (Module C / D in some docs)

Engine: core/module_c_vtrac.py plus helpers in src/utils.

Inputs: data/outputs/tables/<STATE>/ Combined tables.

Outputs:

Analyzer bundles under data/outputs/analysis/vtrac/<STATE>/ (evidence grid, straights, metrics).

Validation / compact report under data/outputs/analysis/vtrac_validation/* via the validation workflow.

3.4 Hot Zones

Engine: alpha_analytical/hot_zones/* (CLI scripts/hot_zones/run_hot_zones_cli.py).

Inputs: JSON tables data/outputs/json_tables/<STATE>_tables.json.

Outputs: data/outputs/analysis/hot_zones/<STATE>/ (per‑lane, top lanes, meta + winner maps).

Key point for Part 1:
All four Brain‑1 analyzers are already wired, read only from guarded tables/JSON, and write lean brain bundles under data/outputs/analysis/<tool>/<STATE>/.... These bundles are the stable contract you’ll keep into the Aggregator/Brain‑2 era.

4. Aux / Blackapple: draws‑only side brain (what’s wired & what you keep)

From Live Wiring + Workflow Standard + Quickstart:

Engines: modules.analyze_pairs, modules.vtrac_reference, and positional pressure under modules/module_d_auxiliary_tools/refactored/positional_tool.py, plus sums helpers in the same refactored folder.

Inputs: data/cleaned/*_draws.csv (draws‑only, newest‑first), with Combined/Midday/Evening variants resolved by modules.aux_loaders.

Outputs:

Rendered in‑page only (tables, captions, positional shortlists, badges).

No persisted CSV under data/outputs/analysis/—they’re intentionally ephemeral.

Control Center use:

A cross‑state doubles table and BA summary are rendered in Control Center by scanning the same draws CSVs.

Tests lock behaviour like control_center doubles, positional shortlists, and aux validation thresholds, confirming this wiring is real, not aspirational.

Why it matters for the diagram:
Aux/Blackapple are pure draws‑brain: they never touch tables, and they already drive Control Center doubles/alerts. That separation should be crystal‑clear in the architecture so you don’t accidentally entangle them with table‑based analyzers later.

5. Control Center & “Brain‑2 surface”

Control Center is your current Brain‑2 surface, even before the full Aggregator logic is wired.

From Quickstart + Live Wiring:

Launches as part of the same Streamlit app; Dev Health shows bindings for utils.path_handler, modules.vtrac_reference, modules.winner_report_full, modules.blackapple, modules.aux_loaders, core.pipeline_runner, and current tables root.

Data it uses:

Draws‑only: for cross‑state doubles table and BA summary.

Combined tables: via an optional “Tables Pipeline” expander that calls run_tables_with_guard when needed—this keeps Brain‑1 data fresh from the app.

Brain‑1 outputs: the batch workflow uses the same results list to run Stable and Digit Reduction, dropping outputs into data/outputs/analysis/.../<STAMP>/ for each state.

Batch workflow:
The Quickstart and Batch SOP describe a Control Center batch panel where you:

Paste a winners list,

Toggle Winners logger, Stable bundles, Digit Reduction bundle,

Set a bundle stamp so outputs land in the right data/outputs/analysis/<tool>/<STATE>/<STAMP>/ folder.

Together with Final Validation, that makes Control Center the hub that:

Regenerates tables (via guarded pipeline).

Triggers per‑state analyzers (Stable, Digit).

Surfaces cross‑state doubles/BA and winners reports.

The planned Aggregator module sits conceptually here: docs say it will read each module’s JSON/brain bundle, merge patterns, and calculate synergy scores. In reality today, the data contracts and brain bundles are in place; the scoring/aggregation layer is the main future addition.

_________________________________________________________________


Part 1 – Canonical system diagram (wired‑only view)

Here’s Part 1 as a ready‑to‑drop Mermaid block for your repo.

flowchart LR
  %% ===== Data Sources =====
  subgraph S[Data Sources]
    HW[History workbook<br/>data/history/Pick3StatsC4_YYYY-MM-DD.xlsm]
    RF[Results file<br/>data/results/YYYY-MM-DD.txt]
    DRW[Draws-only CSVs<br/>data/cleaned/*_draws.csv]
  end

  %% ===== Guarded Pipelines =====
  subgraph P[Guarded Pipelines (Master Validation Spine)]
    RTG[run_tables_with_guard.py<br/>(tables + JSON + manifest)]
    TBL[data/outputs/tables/&lt;STATE&gt;<br/>Combined/Midday/Evening CSV]
    JT[data/outputs/json_tables/&lt;STATE&gt;_tables.json]
    WGEN[generate_winners_from_results.py]
    WH[reports/stable/winners_by_date/&lt;DATE&gt;<br/>per-state winners HTML/JSON]
  end

  %% ===== Brain-1: Table-based analyzers =====
  subgraph B1[Brain‑1 – Per-State String-Table Analyzers]
    STABLE[Stable Pattern Extractor<br/>src/core/stable_pattern_extractor.py]
    DIGIT[src/core/module_b_digit_reduction.py]
    VTRAC[core/module_c_vtrac.py<br/>(enhanced analyzer)]
    HOTZ[alpha_analytical/hot_zones/*]
    
    STABLE_OUT[data/outputs/analysis/patterns/&lt;STATE&gt;/...]
    DIGIT_OUT[data/outputs/analysis/digit_reduction/&lt;STATE&gt;/...]
    VTRAC_OUT[data/outputs/analysis/vtrac/&lt;STATE&gt;/...]
    HOTZ_OUT[data/outputs/analysis/hot_zones/&lt;STATE&gt;/...]
  end

  %% ===== Aux / Blackapple =====
  subgraph AUX[Aux / Blackapple – Draws-only Side Brain]
    AUXENG[Aux engines<br/>modules.analyze_pairs<br/>modules.vtrac_reference]
    POS[Positional Pressure<br/>modules/module_d_auxiliary_tools/refactored/positional_tool.py]
    BA[Blackapple (MVP wiring)<br/>modules/blackapple.py]
  end

  %% ===== Control Center / Brain-2 Surface =====
  subgraph CC[Control Center – Brain‑2 Surface]
    CC_APP[Streamlit Control Center page<br/>src/app.py]
    CC_BATCH[Batch expander<br/>(Stable &amp; Digit bundles, winners)]
    CC_DOUBLES[Cross-state doubles &amp; BA summary]
    FUT_AGG[Future Aggregator<br/>module_D_aggregator.py<br/>(planned synergy scoring)]
  end

  %% ----- Edges: sources -> pipelines -----
  HW --> RTG
  RTG --> TBL
  RTG --> JT

  RF --> WGEN
  WGEN --> WH

  %% ----- Edges: tables -> Brain-1 tools -----
  TBL --> STABLE
  TBL --> DIGIT
  TBL --> VTRAC
  JT  --> HOTZ

  STABLE --> STABLE_OUT
  DIGIT  --> DIGIT_OUT
  VTRAC  --> VTRAC_OUT
  HOTZ   --> HOTZ_OUT

  %% ----- Edges: draws-only -> Aux/CC -----
  DRW --> AUXENG
  DRW --> POS
  DRW --> BA
  DRW --> CC_DOUBLES

  AUXENG --> CC_DOUBLES
  POS     --> CC_DOUBLES
  BA      --> CC_DOUBLES

  %% ----- Control Center edges -----
  TBL --> CC_APP
  DRW --> CC_APP
  WH  --> CC_APP

  STABLE_OUT --> CC_BATCH
  DIGIT_OUT  --> CC_BATCH
  VTRAC_OUT  --> CC_BATCH
  HOTZ_OUT   --> CC_BATCH

  %% Planned aggregator reads brain bundles
  STABLE_OUT --> FUT_AGG
  DIGIT_OUT  --> FUT_AGG
  VTRAC_OUT  --> FUT_AGG
  HOTZ_OUT   --> FUT_AGG
  FUT_AGG    --> CC_APP




How this aligns with the docs (no jargon, just wiring):

Data contracts and page inputs/outputs line up with the Live Wiring doc and Quickstart.

Guarded pipelines (RTG, WGEN, manifest, winners) match the Final Validation checklist.

Brain‑1 modules and their output folders match Live Wiring and Lean Outputs.

Aux, positional pressure, BA, and Control Center doubles wiring match Aux + Workflow Standard.

The future Aggregator node mirrors the architecture doc and README module map without claiming it’s fully wired in the UI yet.

7. How to use Part 1 going forward

For future parts of the diagram, we can:

Zoom into each Brain‑1 tool (Digit Reduction, Stable, V‑TRAC, Hot Zones) and show their internal feature/score flow and how that will feed the Aggregator.

Detail Control Center and Winners Module as the front‑door for master validation and cross‑tool review.

Layer in Brain‑2 Aggregator design once you’re ready to freeze the synergy logic.

But Part 1 is intentionally about what’s actually wired today and what is clearly “canon” post‑validation: the guarded pipelines, the table analyzers, the draws‑only Aux brain, and the Control Center hub.

Quick sanity‑check actions for you

Verify Brain‑1 wiring on disk

After a Control Center batch run, pick a state (e.g., Connecticut4) and confirm you see:

data/outputs/analysis/patterns/Connecticut4/... (Stable),

data/outputs/analysis/digit_reduction/Connecticut4/analyzer_v2/... (Digit),

data/outputs/analysis/vtrac/Connecticut4/... (V‑TRAC).

Verify Aux vs tables separation

Open the Aux page and Control Center doubles panel and confirm they still function even if data/outputs/tables/* are missing, as long as data/cleaned/*_draws.csv exist. That matches the contract: Aux/BA are draws‑only and independent of the string tables.

If this Part 1 shape looks good to you, the next step is Part 2: zooming into one of the analyzers (Digit or Stable) + the Winners Module to show exactly how their brain bundles and overlays step into the future Aggregator.

_____________________________________________________

1. Scope recap – what this part is locking down

From your own docs, the current AAT9 reality looks like this:

The integrated app is launched via run_app.bat → streamlit run src\app.py, and resolves in‑repo modules like utils.path_handler, modules.blackapple, modules.aux_loaders, and alpha_analytical.stable.

Data contracts are split cleanly:

Aux/Blackapple: reads data/cleaned/*_draws.csv (draws‑only).

V‑TRAC / Stable / Digit Reduction: read combined tables from tables/ or data/outputs/tables/<State>/ via utils.path_handler.

Each analyzer writes a lean brain bundle under data/outputs/analysis/<tool>/<State>/…, especially for Digit (per_item/top/meta), Stable (scores/families/compound), and V‑TRAC (per‑state analyzer files and compact reports).

Centralized winners artifacts (winner_map.json, winner_flags.csv and HTML overlays) are produced only by the Control Center batch, not by each tool anymore.

Aux tools and Control Center run entirely off draws CSVs, providing doubles tables, Blackapple alerts, V‑TRAC heatboards, sums analytics, and positional pressure, without touching combined tables.

Part 2 of the architecture diagram will therefore focus on:

Data & runtime layers – how history workbooks/results → tables/JSON → analyzers & Aux.

Brain 1 – per‑state analyzers wired today (Stable, Digit, V‑TRAC, Hot Zones).

Brain 2 – Control Center, winners module, and the planned Aggregator that will read the lean bundles.

2. Diagram 1 – Data & Runtime Layers (what feeds everything)

This first diagram shows only what’s actually running in the repo today: table pipeline, draws pipeline, analyzers, Aux, and Control Center.

flowchart TB
  %% ========= DATA SOURCES =========
  subgraph L0["L0 – Core Data Sources"]
    WB[["History workbook\n(data/history/Pick3StatsC4_2025-06-22.xlsm)"]]
    RESULTS[["Official results text\n(data/results/2025-06-23.txt)"]]
  end

  %% ========= PIPELINES =========
  subgraph L1["L1 – Pipelines & Storage"]
    subgraph PIPE["Table Pipeline\n(run_tables_with_guard / generate_tables_pipeline.bat)"]
      CLEAN[Clean & extract per state\n(data/cleaned/STATE_cleaned.xlsx)]
      TABLES[Standard string tables\n(data/outputs/tables/STATE/\nMidday_combined.csv,\nEvening_combined.csv,\nCombined_combined.csv)]
      JSONT[JSON table mirrors\n(data/outputs/json_tables/STATE_tables.json)]
    end

    subgraph DRAWPIPE["Draws Pipeline"]
      DRAWS[Draws CSVs\n(data/cleaned/*_draws.csv)]
    end

    subgraph WINLOG["Winners Generator\n(generate_winners_from_results.py + Control Center batch)"]
      WINMAP[Central winners\nreports/stable/winners_by_date/DATE/\n + winner_map.json / winner_flags.csv]
    end
  end

  %% ========= ENGINES (BRAIN 1 / AUX) =========
  subgraph L2["L2 – Engines (Brain 1 + Aux)"]
    subgraph BRAIN1["Brain 1 – Per‑state analyzers\n(string‑table tools)"]
      STABLE[Stable Pattern Extractor\nsrc/core/stable_pattern_extractor.py\n→ data/outputs/analysis/patterns/STATE/]
      DIGIT[Digit Reduction\nsrc/core/module_b_digit_reduction.py\n→ data/outputs/analysis/digit_reduction/STATE/]
      VTRAC[V‑TRAC Analyzer\nsrc/core/module_c_vtrac.py\n→ data/outputs/analysis/vtrac/STATE/]
      HOTZ[Hot Zones (JSON‑tables)\nalpha_analytical/hot_zones/\n→ data/outputs/analysis/hot_zones/STATE/]
    end

    subgraph AUX["Aux / Blackapple (draws‑only tools)"]
      AUXTOOLS[Auxiliary Tools page\nmodules.aux_loaders + staged modules\n(operate on draws CSVs)]
      BA[Blackapple engine\nmodules/blackapple.py\n(alerts from draws)]
    end
  end

  %% ========= CONTROL CENTER / BRAIN 2 =========
  subgraph L3["L3 – Control Center & Future Aggregator (Brain 2)"]
    CC[Control Center UI\n(cross‑state dashboards,\nTables Pipeline, batch runners)]
    WINMOD[Winners modules\n(V‑TRAC winner report\n+ Analyzer‑style winners HTML)]
    AGG[Planned Aggregator\n(reads lean brain bundles\nfrom Stable/Digit/V‑TRAC/Hot Zones)]
  end

  %% WIRES
  WB --> PIPE
  RESULTS --> WINLOG

  CLEAN --> TABLES
  TABLES --> JSONT

  TABLES --> STABLE
  TABLES --> DIGIT
  TABLES --> VTRAC
  JSONT --> HOTZ

  DRAWS --> AUXTOOLS
  DRAWS --> BA

  WINMAP --> WINMOD

  STABLE --> CC
  DIGIT --> CC
  VTRAC --> CC
  HOTZ --> CC
  AUXTOOLS --> CC
  BA --> CC
  WINMAP --> CC

  STABLE --> AGG
  DIGIT --> AGG
  VTRAC --> AGG
  HOTZ --> AGG
  AUXTOOLS --> AGG
  BA --> AGG
  WINMAP --> AGG

Why this matches what’s wired now

Tables pipeline: your data formats doc says generate_tables_pipeline.bat creates 6 CSVs (Midday/Evening/Combined, plus R2‑only) per state under data/outputs/tables/STATE/.

JSON tables: JSON mirrors live under data/outputs/json_tables/STATE_tables.json and are the inputs for Hot Zones.

Aux draws CSVs: Aux/Blackapple explicitly consume only data/cleaned/*_draws.csv (draws‑only, newest‑first).

Per‑state analyzers: Live Wiring maps each page to its engine and I/O under data/outputs/analysis/<tool>/<State>/….

Control Center & Aux: the Aux overview confirms Control Center reads draws CSVs for doubles tables, BA alerts, V‑TRAC heatboard, sums, and positional pressure.

Brain‑bundle + winners separation: the lean spec says Digit’s brain bundle lives at data/outputs/analysis/digit_reduction/STATE/analyzer_v2/ and that only the batch (not the analyzer) writes YYYYMMDD_Variant_winner_map.json/winner_flags.csv and 3‑table HTML.

This is the “plumbing map” you can treat as canonical: it’s exactly how data flows through the current app and batch tooling.