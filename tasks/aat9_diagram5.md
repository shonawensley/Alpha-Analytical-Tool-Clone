I’ll treat this as Part 5 of the AAT9 architecture – the run architecture for the whole system:

how a single day/workbook flows through Preflight → Tables → Brain 1 → Winners → Aggregator → Brain 2,

exactly where Master Validation plugs in,

and how this all lines up with your existing SOP/checklist docs.

You can drop this straight into an AAT9_Architecture_Run_Flow.md later.

Part 5 – Run Architecture & Master Validation Flow
5.1 Run modes (how AAT9 “lives” over time)

At a high level AAT9 runs in three distinct modes:

Historical Backtest / Training

You pick a history workbook date (e.g. Pick3StatsC4_2025-06-22.xlsm).

You pair it with the day‑ahead results (data/results/2025-06-23.txt).

Goal: regenerate tables, winners, and all tool artifacts so you can study them (Excel + HTML + CSV) without any live stakes.

Daily / Live‑style Run

Same mechanics as backtest, but aligned to “today’s” or “yesterday’s” workbook and results file.

Goal: produce fresh Brain 1 bundles, winners logs, Aggregator outputs, and Brain 2 alerts that Control Center uses to decide if/where to play.

Master Validation Runs

A curated subset of backtest runs (selected dates/states) where you:

follow the Brain 1 template (per‑state deep analysis), and

then the Brain 2 template (Control Center alerts / A01–A12 / BA boards).

Goal: validate that each tool and the combined brain behave as you intend, and record stable patterns you’ll hard‑wire into configs or reference docs.

Architecturally, all three modes share the same pipeline; the difference is what you log about them and whether you treat the result as experimental, training, or “live decision”.

5.2 End‑to‑end run timeline (one workbook / one results day)

Think of a single run as a sequence of stages:

flowchart LR
  subgraph S0["S0 – Preflight & Env Health"]
    PF[Preflight script<br/>+ System Health panels]
  end

  subgraph S1["S1 – Tables & JSON Regeneration"]
    TBL[run_tables_with_guard.py<br/>+ String Table SOP]
  end

  subgraph S2["S2 – Winners Generation & Guard"]
    WIN[generate_winners_from_results.py<br/>+ CT/FL guard checks]
  end

  subgraph S3["S3 – Brain 1 Analyzers"]
    ST[Stable]
    DR[Digit Reduction]
    VT[V‑TRAC Analyzer]
    HZ[Hot Zones]
    AUX[Aux/Blackapple]
  end

  subgraph S4["S4 – Central Winners Module"]
    WM[winner_map.json<br/>winner_flags.csv]
  end

  subgraph S5["S5 – Aggregator (Module D)"]
    AGG[aggregator_synergy.json/csv]
  end

  subgraph S6["S6 – Brain 2 / Control Center"]
    CC[Daily boards<br/>(A01–A12, BA, repeats, doubles)]
  end

  PF --> TBL --> WIN
  WIN --> ST
  WIN --> DR
  WIN --> VT
  TBL --> ST
  TBL --> DR
  TBL --> VT
  TBL --> HZ
  TBL --> AUX

  ST --> WM
  DR --> WM
  VT --> WM
  HZ --> WM

  WM --> AGG
  ST --> AGG
  DR --> AGG
  VT --> AGG
  HZ --> AGG
  AUX --> AGG

  WM --> CC
  AGG --> CC
  AUX --> CC


Now we break each stage down in terms of what actually exists and where Master Validation sits.

5.3 S0 – Preflight & Environment Health

Purpose: guarantee you are in the right repo, with the right Python, the expected draws/tables directories, before touching anything.

Anchors:

The Quickstart Cheat Sheet and Preflight Reference define a standard preflight script (PowerShell) that checks:

current working directory is repo root,

Python path and key imports (path_handler, blackapple, aux_loaders, stable),

draws inventory in data/cleaned/draws,

tables roots if you pass -CheckTables.

The Workflow Standard says: run preflight once per session, fix any red flags before coding or running analyzers.

Architectural role:

S0 guards against path drift and stale environments.

Master Validation will assume the preflight has passed; you don’t want to debug tool behavior just to discover you were in the wrong folder.

5.4 S1 – Tables & JSON Regeneration

Purpose: ensure string tables & JSON mirrors match the history workbook you intend to analyze.

Mechanics:

Use run_tables_with_guard.py (or the wrapper run_history_and_results.py) with a specific history workbook:

Copies the dated workbook into the canonical location (data/original/Pick3StatsC4.xlsm).

Empties and regenerates per‑state tables under data/outputs/tables/<STATE>/.

Writes a manifest (tables_manifest.json) recording workbook path, mtime, size, and per‑state checksums.

Produces JSON mirrors under data/outputs/json_tables/<STATE>_tables.json.

The String Table Testing SOP then spot‑checks:

Set1/Draw1/RowType=draw_data in Combined_Combined.csv for CT/FL,

that these digits match the intended “guard” draws for that workbook.

Architectural role:

S1 is the foundation for every tool:

Stable / Digit / V‑TRAC all read data/outputs/tables/<STATE>/*.csv.

Hot Zones reads data/outputs/json_tables/<STATE>_tables.json.

If S1 is wrong, everything is wrong; that’s why it’s separated and tightly logged.

Master Validation:

When you pick dates for Master Validation, you will reference the S1 logs (String Table SOP + Table Swap Verification) to be sure that environment is clean and reproducible.

5.5 S2 – Winners Generation & Guard

Purpose: convert the official results file for the day into winners HTML + JSON tied to the regenerated tables.

Mechanics:

generate_winners_from_results.py:

Reads data/results/YYYY-MM-DD.txt (the exact winners list).

For each state in the file, builds V‑TRAC/Stable winners HTML and JSON under reports/stable/winners_by_date/<DATE>/<STATE>/.

Ensures each winner has a V‑TRAC index, overlay, and winners lens in sync with the tables.

The Master Validation Preflight document adds an explicit guard:

For CT/FL, confirm the Set1/Draw1 sequence from Combined_Combined.csv appears inside the winners HTML.

That proves the HTML is tied to the current tables, not to a stale environment.

Architectural role:

S2 creates the winner lens that Digit Reduction, V‑TRAC Analyzer, and Stable logs use to align their features with actual hits.

It is also the source for the central winners module later.

Master Validation:

Your Brain 1 template heavily uses S2 artifacts:

winners HTML (3‑table view),

overlays (paths Set3→Set2→Set1),

per‑tool winners spotlight/overlays.

S0–S2 together give you a trusted environment for any analysis.

5.6 S3 – Brain 1 Analyzers (Per‑tool Runs)

Purpose: for a given state/date, produce standardized lean bundles (per‑item/top/meta) and human‑readable HTML/overlays for each tool.

Tools:

Stable Pattern (Module A)

Reads combined tables for the state.

Outputs pattern scores, families, and compound metrics under data/outputs/analysis/patterns/<STATE>/.

When provided winners, also writes winners spotlight CSVs and metrics JSON.

Digit Reduction (Module B)

Reducer: analyzes long‑string ladders and writes training/steps logs.

Analyzer V2: writes per‑item + top‑candidates + meta under .../digit_reduction/<STATE>/analyzer_v2/.

Winners overlays (per state/variant) are written under analyzer_v2/winners/ and feed the dr.win_* flags.

V‑TRAC Analyzer

Reads combined tables and produces analyzer CSV/JSON and compact “share bundle” reports for each winner/VT index.

These capture VT lanes, repeats, and evidence grid that later align with A09 (VT echo).

Hot Zones (Module C)

Reads JSON tables and produces per‑lane and top‑lane bundles under .../analysis/hot_zones/<STATE>/.

Has its own winners mapping at the lane level.

Aux / Blackapple

Reads draws‑only CSVs (data/cleaned/*_draws.csv).

Produces positional pressure tables, BA foundation sets, pair‑pressure, double/mirror bias, etc.

Outputs are mostly in‑UI plus any explicit CSV logs you’ve added.

Architectural role:

S3 is Brain 1: each engine runs on the same tables/results environment and yields a standardized “brain bundle” of CSV/JSON files.

These bundles are read by:

the central winners module to attach outcome flags, and

the Aggregator to compute synergy per pattern.

Master Validation:

Your Brain 1 template (Final Validation docs) lives almost entirely here:

read winners HTML + overlays,

cross‑check with per‑item/top CSVs,

log which feature combinations worked or missed,

record candidate boxes/families to add or adjust.

5.7 S4 – Central Winners Module (Shared Hit Taxonomy)

Purpose: unify winners + tool outputs into one canonical record per winner, with agreed hit classes.

Mechanics (design + partial implementation):

Inputs:

winners HTML/JSON and map from S2,

Stable/VT/Digit/Hot Zones lean outputs from S3 (ranks, lanes, hit flags),

(optionally) Aux/BA features for that winner’s digits.

Outputs (per date/variant):

winner_map.json: one JSON object per winner with:

state, variant, winner, draw date,

classes.{exact_straight, exact_boxed, vt_boxed, vt_straight},

tool_evidence.stable/vtrac/digit/aux blocks summarizing where/how each tool saw it.

winner_flags.csv: a flat CSV version of the same classification and hit flags.

Architectural role:

S4 is the single ground‑truth layer for hit classification.

Everything else (Aggregator, A01–A12, profit boards, ML later) should look only at these winners classes to define “success”.

Master Validation:

When you compare Brain 1 and Brain 2 behavior, you should always be checking:

“Did this pattern candidate correspond to a winner, and in what class?”

That answer comes from winner_map / winner_flags, not from local tool guesses.

5.8 S5 – Aggregator (Module D Synergy Engine)

Purpose: read brain bundles + winner map and produce a unified synergy view per pattern/family.

Mechanics (target):

Flatten/normalize tool outputs:

build a per‑pattern record from Stable families, Digit per‑item/top, Hot Zones lanes, V‑TRAC compact report, and Aux feature vectors.

Compute:

base module scores (Stable score, Digit final score, Hot Zones strength, V‑TRAC strength, Aux bias),

cross‑module bonuses (when tools agree on the same pattern),

cross‑set/cross‑variant bonuses (carry and consensus),

any “pending” or “triple‑value” bonuses you defined in the aggregator doc.

Emit aggregator_synergy.json/csv with:

one record per canonical pattern/family,

final_synergy_score,

breakdown of contributions,

references back to winner classes (if available).

Architectural role:

S5 is the mechanical super‑brain: a pure function from Brain 1 outputs + winners to ranked patterns, with transparent reasoning.

You can tune it via config weights without altering Brain 1 tools.

Master Validation:

Your Brain 1 template plus early Aggregator runs let you see:

which feature combinations lead to high synergy scores,

whether winners consistently float to the top,

and where synergy logic needs adjustment.

5.9 S6 – Brain 2 / Control Center (Profit & Boards)

Purpose: turn all those artifacts into a daily decision board: which states/variants are healthy, which alerts fire, and which combination sets to consider.

Mechanics (target architecture):

Read:

aggregator_synergy.json from S5,

winner_flags.csv from S4,

per‑state metrics from Brain 1 bundles (e.g., vt_only_hits counts, LS2/Hot Zone stars),

Aux/BA aggregates (doubles pressure, BA tempo, foundation size).

Compute A01–A12 indicator flags and scores on top of synergy and winners:

e.g., A01 = Dual Tail Consensus; A03 = cross‑variant consensus; A05/A12 = straight‑lean from perm/DR clamps; A09 = VT index echo; etc.

Render:

Per‑state dashboards: environment health, Brain 1 metrics, synergy summary.

Alert board: which A01–A12 fired where, with severity.

Play board (optional): final recommended box/straight sets per state.

Architectural role:

S6 is Brain 2: it doesn’t discover new evidence; it interprets Brain 1 + Aggregator evidence as profit/decision signals.

It is where you will eventually plug in the “12 profitability trackers” referenced in your profit blueprint.

Master Validation:

Your Brain 2 template (Control Center validation) will run here:

For each date, list fired alerts and cross‑check them against winner_flags and aggregator_synergy to see how often they pointed at winning environments or patterns.

5.10 Where Master Validation plugs into the architecture

To make it crystal‑clear:

Brain 1 Master Validation (per state)

Attaches at S2–S3:

After S2 & S3, you have:

CT/FL (or any state) winners HTML + overlays,

Stable / Digit / V‑TRAC / Hot Zones bundles for that date.

Brain 1 template steps:

trace winner paths in HTML and overlays,

inspect per‑item/top CSVs for how early, how strong they were scored,

log patterns where tools agreed, where they missed, and any candidate boxes/families to add.

Practically, you’re sitting inside S3’s outputs and S2’s lens.

Brain 2 Master Validation (Control Center / Profit)

Attaches at S4–S6:

After S4 & S5, you have:

winner_map and winner_flags,

aggregator_synergy,

per‑state Brain 1 metrics.

Brain 2 template steps:

evaluate which A01–A12 alerts should fire based on those features,

check whether those alerts actually predicted winners efficiently (few combos, good straight leverage),

adjust indicator definitions/thresholds and aggregator weights.

Practically, you’re reading from S4/S5 artifacts into S6’s boards.

5.11 How to turn this into a repo doc (practical)

If you want to make this a first‑class KIT doc:

Create docs/AAT9_KIT/AAT9_Architecture_Run_Flow.md.

Paste the Part 5 structure:

5.1 Run modes

5.2 End‑to‑end diagram

5.3–5.9 S0–S6 sections

5.10 Master Validation plugs

Link it from:

AAT9_KIT_README.md under an “Architecture” section,

and from AAT9_Final_Validation_Help.md as “Run Flow Reference”.

That way, any future session can:

glance once at this run architecture,

know exactly where their current work sits (S0–S6),

and not have to rediscover the pipeline.

If you’d like me to proceed further, the next “optimal” piece would be a schema‑level Part 6, where I:

define concrete column sets for:

winner_flags.csv,

aggregator_synergy.csv/json,

an alerts_A01_A12.csv per state/date,

so implementation and testing of the final super‑brain have zero ambiguity.