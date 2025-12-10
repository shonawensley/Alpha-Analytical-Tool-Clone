TL;DR:
Here’s Part 1 of your final AAT9 architecture doc: a top‑level, end‑to‑end diagram + explanation that focuses only on what is actually wired today and what clearly survives into the Brain‑2 / aggregation phase. It shows:

How history workbooks + results become string tables + JSON + draws.

How Stable, Digit Reduction, V‑TRAC, Hot Zones, Aux/BA sit on top of those inputs and what “brain bundles” they emit.

How the Control Center (Brain‑2 shell) orchestrates runs, centralizes winners, and prepares the Aggregator/Indicators (A01–A12) layer that THE PROFIT BLUEPRINT and the Architecture Framework describe.

This is designed to be dropped straight into an AAT9_Architecture_Final_Part1.md doc.

1. Brain‑0 → Brain‑1 → Brain‑2: the three layers

From your own roadmap and architecture notes, the system already has a clean three‑layer story:

Brain‑0 (Data & History)

Daily Excel Pick3StatsC4 history workbooks are activated and converted into:

Combined/Midday/Evening string tables under data/outputs/tables/<STATE>/.

JSON table mirrors under data/outputs/json_tables/<STATE>_tables.json.

Day‑ahead results text files (data/results/YYYY-MM-DD.txt) feed winners logging and validation.

Brain‑1 (Per‑tool analyzers on a single state)
For each tracked state/date, the main modules run on those tables:

Stable Pattern Extractor (Module A) – scans string tables, emits per‑pattern and per‑family CSVs + compound scores.

Digit Reduction (Module B) – long‑string reducer + Analyzer V2 with rich VT/LS features and a lean “brain bundle” per state/run.

Hot Zones (Module C, now actually wired) – JSON‑driven lane analysis with its own per‑lane/top/meta bundle.

V‑TRAC Analyzer (Module D) – V‑TRAC mapping and share‑bundle outputs (lean spec partially mirrored in Analyzer_Lean_Outputs).

Aux / BlackApple – draws‑only positional, pairs, doubles, BA tempo/foundation; used as confirming evidence only, never as the primary string‑table brain.

Each of these modules writes its own lean brain bundle to data/outputs/analysis/<module>/<STATE>/.... This is the contract the future Aggregator will read.

Brain‑2 (Control Center + Aggregator / Indicators)

The Control Center page orchestrates table rebuilds, batch runs for Stable/Digit/V‑TRAC/Hot Zones, and centralized winners logging, all from the same pasted winners list.

The planned Aggregator module reads all lean brain bundles (Digit, Stable, V‑TRAC, Hot Zones) and merges them into final synergy scores + indicators (A01–A12), which the Profit Blueprint specifies in detail.

The Control Center plus Aggregator is what your docs explicitly call Brain‑2 – cross‑state portfolio and profit management.

Key point for Part 1:
The architecture diagram below focuses strictly on those wired flows (history → tables → analyzers → brain bundles → Control Center / winners), while already reserving clear hook points for the Aggregator and A01–A12 indicator layer you’ll add next.

2. Part 1 Diagram – End‑to‑end system map (wired today, Aggregator‑ready)

You can paste this directly into a Markdown file and render it with Mermaid.

flowchart TD

  %% ===================
  %% L0: DATA & HISTORY
  %% ===================

  subgraph L0["Brain‑0 — Data & History (per date)"]
    H[["Pick3StatsC4 history workbooks\n(data/history/Pick3StatsC4_YYYY-MM-DD.xlsm)"]]
    R[["Results files\n(data/results/YYYY-MM-DD.txt)"]]

    TBL["run_tables_with_guard.py\n+ tables pipeline"]
    TOUT[["String tables per state\n(data/outputs/tables/<STATE>/{Combined,Midday,Evening}_Combined.csv)"]]
    JSON[["JSON table mirrors\n(data/outputs/json_tables/<STATE>_tables.json)"]]

    DRAWS_PIPE["Aux draws pipeline\n(Control Center expander)"]
    DRAWS[["Draws-only CSVs\n(data/cleaned/draws/<STATE>_draws.csv)"]]

    H --> TBL --> TOUT
    TBL --> JSON
    H --> DRAWS_PIPE --> DRAWS
  end

  %% ===================
  %% L1: ANALYSIS ENGINES
  %% ===================

  subgraph L1["Brain‑1 — Per‑tool analyzers (per state/date)"]
    direction LR

    STABLE["Stable Pattern Extractor\nsrc/core/stable_pattern_extractor.py"]
    STABLE_IN["Read string tables\n(Combined/Mid/Eve CSVs)"]
    STABLE_OUT[["Stable brain bundle\n data/outputs/analysis/patterns/<STATE>/\n - *_stable_patterns_scores.csv\n - *_stable_patterns_families.csv\n - *_stable_patterns_compound.csv"]]

    DIGIT["Digit Reduction\nmodule_B_digit_reduction + Analyzer V2"]
    DIGIT_IN["Read string tables\n+ winners HTML/JSON"]
    DIGIT_OUT[["Digit brain bundle\n data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/\n - *_analyzer_v2_per_item.csv\n - *_analyzer_v2_top_candidates.csv\n - *_analyzer_v2_meta.json"]]

    HOT["Hot Zones Engine\nalpha_analytical/hot_zones/*"]
    HOT_IN["Read JSON tables\n<STATE>_tables.json"]
    HOT_OUT[["Hot Zones brain bundle\n data/outputs/analysis/hot_zones/<STATE>/\n - *_hot_zones_per_lane.csv\n - *_hot_zones_top_lanes.csv\n - *_hot_zones_meta.json"]]

    VTRAC["V‑TRAC Analyzer\nmodule_C_vtrac_enhanced"]
    VTRAC_IN["Read string tables\n(Combined/Mid/Eve CSVs)"]
    VTRAC_OUT[["V‑TRAC analysis\n data/outputs/analysis/vtrac/<STATE>/\n (scores, overlays, share bundle)"]]

    AUX["Aux / BlackApple / Positional tools\nmodules.aux_loaders, modules.blackapple"]
    AUX_IN["Read draws-only CSVs\n(data/cleaned/draws/*_draws.csv)"]
    AUX_OUT[["Aux evidence (in‑page)\n + BA/tempo/doubles signals\n (optionally logged per state/day)"]]

    %% Wiring to inputs
    TOUT --> STABLE_IN --> STABLE --> STABLE_OUT
    TOUT --> DIGIT_IN --> DIGIT --> DIGIT_OUT
    JSON --> HOT_IN --> HOT --> HOT_OUT
    TOUT --> VTRAC_IN --> VTRAC --> VTRAC_OUT
    DRAWS --> AUX_IN --> AUX --> AUX_OUT
  end

  %% ===================
  %% L2: CONTROL CENTER & WINNERS
  %% ===================

  subgraph L2["Brain‑2 Shell — Control Center, Winners & Aggregator Inbox"]
    CC["Control Center (Streamlit)\n/pages/Control_Center.py"]
    WL["Winners Logger (V‑TRAC + Analyzer-style)"]
    WIN_HTML[["Winners HTML & JSON\nreports/stable/winners_by_date/<DATE>/..."]]

    CENTRAL_WIN[["Central winner artifacts\n data/outputs/analysis/winners/<STATE>/...\n + winner_map.json / winner_flags.csv"]]

    AGG_INBOX[["Aggregator Inbox (planned)\n - per_state brain bundles\n - Hot Zones winner_map\n - A01–A12 indicator rows"]]

    CC --> WL --> WIN_HTML --> CENTRAL_WIN

    %% Brain bundles feeding inbox
    STABLE_OUT --> AGG_INBOX
    DIGIT_OUT  --> AGG_INBOX
    HOT_OUT    --> AGG_INBOX
    VTRAC_OUT  --> AGG_INBOX
    AUX_OUT    --> AGG_INBOX
  end

  %% Top-level orchestration
  R --> CC
  TOUT --> CC
  JSON --> CC

How this lines up with your existing docs

The daily lifecycle in the Macro Roadmap is exactly what L0→L1→L2 shows: ingest Excel, run module execution, persist analysis outputs, log winners, update training bundles, then (future) track profitability.

The modules listed in the Architecture & Master Validation Framework appear as STABLE, DIGIT, HOT, VTRAC; each feeds a Final Aggregator module via structured JSON/CSV outputs.

The lean output spec formalizes the “brain bundle” contract for Digit and Stable (and mirrors it for Hot Zones and V‑TRAC). That’s what the *_per_item.csv, *_top_candidates.csv, *_meta.json nodes represent.

The Aggregator design in the Architecture doc and THE PROFIT BLUEPRINT is exactly what the AGG_INBOX node is for: a place where per‑tool patterns + scores + tags are normalized and scored for synergy (cross‑module overlaps, cross‑set persistence, variant consensus, etc.).

3. “What’s actually wired” vs “What’s design‑only” (so you don’t go in circles)

To keep this architecture grounded in the current app, here’s a clear line between what’s live and what’s still a design:

3.1 Live & wired today (Brain‑0 & Brain‑1 & CC shell)

Data / tables / JSON / draws

run_tables_with_guard.py is the canonical entry for activating a dated workbook and regenerating all per‑state tables + JSON mirrors, with a manifest guard to avoid stale tables.

data/outputs/tables/<STATE>/Combined_Combined.csv and siblings are the only string‑table inputs used by Stable, Digit, V‑TRAC, and indirectly by winners.

data/outputs/json_tables/<STATE>_tables.json is the Hot Zones input.

data/cleaned/draws/<STATE>_draws.csv is the Aux/BA input; these are regenerated via the Aux draws pipeline expander in Control Center.

Analyzers and their brain bundles

Digit Reduction already emits a clean brain bundle:

.../analyzer_v2_per_item.csv with features like vt_only_lane, funnel_precol1, ls_col_42, ls2_lane, persistence, recency, normalized score, and a reasons_json explaining the score.

..._top_candidates.csv with aggregated families and evidence_tags.

meta.json for config/git SHA.
This is explicitly documented as “Brain bundle — outputs the Aggregator can depend on.”

Stable Pattern Extractor’s lean contract is defined as:

*_stable_patterns_scores.csv (per‑pattern evidence).

*_stable_patterns_families.csv (family aggregates).

*_stable_patterns_compound.csv (Packet‑2 roll‑ups with funnel and vt_only flags).

Hot Zones brain bundle mirrors that structure with per‑lane and top‑lane CSVs plus meta and winner_map.

V‑TRAC Analyzer has its own analysis folder and share bundle; the lean spec says Stable/V‑TRAC will be brought into the same per_item/top/meta pattern as Digit.

Aux / BA are intentionally kept “draws‑only” and are mentioned as read‑only signal providers in the Profit Blueprint: BA foundation, tempo, due doubles rank, etc. feed aggregator indicators but do not touch string tables.

Control Center & winners

Control Center batch is the only writer of the cross‑tool winner_map.json, winner_flags.csv, and analyzer‑style winners HTML, so the winners layer is centralized rather than per‑tool.

The Master Validation / String Table Testing SOPs guarantee that when you swap workbooks, you always pair the right tables with the right results date and rebuild winners HTML from the up‑to‑date tables.

These are all firmly wired and safe to treat as canonical in the architecture.

3.2 Design‑level but clearly “on deck” (Aggregator & Indicators)

For Part 1, we only reserve the slot for these, but we anchor them to your own specs:

The Aggregator is described as Module D/E that reads tool JSON/CSV outputs (stable_patterns*.csv, Digit brain bundle, Hot Zones per_lane/top, V‑TRAC analysis) and produces a final synergy report per pattern. It boosts candidates when multiple tools, sets, or variants agree and annotates each pattern with a synergy breakdown.

Indicators A01–A12 are defined as separate “signal providers” that emit neutral alert rows like:

{
  "alert_id": "A01",
  "state": "ON",
  "section": "Mid",
  "set": "Set1",
  "draw": "2025-11-09",
  "col": 1,
  "anchor_id": "ON|Mid|2025-11-09|Set1|col1",
  "canonical": "397",
  "evidence": {
    "cons_tail_2d": 1,
    "cons_tail_pair": "93",
    "rowcov_3v": 3,
    "ba_foundation_ok": 1,
    "promoters": {
      "perm_dom": 1,
      "dr_clamp_size": 2,
      "index_echo": "ordered"
    },
    "star": "??"
  },
  "suggested_kind": "PROMOTE",
  "cap_lines": 0,
  "strength": 7,
  "created_at": "2025-11-09T04:00:00Z"
}


THE PROFIT BLUEPRINT then specifies how the Aggregator uses A01/A11/A05/A12 and BA foundation to decide when to play BOX vs STRAIGHT and how to clamp line counts (e.g., 12 BOX + 2–4 STRAIGHT).

Architecturally, those indicators simply live in the AGG_INBOX box in the diagram above: they are extra rows keyed by anchor_id that join to the Stable/Digit/V‑TRAC/Hot‑Zones bundles on the same anchor.

4. How this Part‑1 diagram should be used

Now that Part 1 is on paper, you can:

Add it to the project as docs/AAT9_KIT/AAT9_Architecture_Final_Part1.md (or similar).

Use it as the reference backbone when you:

Wire the Aggregator script/notebook to read the Digit/Stable/V‑TRAC/Hot‑Zones brain bundles.

Implement the A01–A12 indicators as pure alert rows (no line allocation inside the indicator itself).

Check any future refactor against the invariant that Brain‑1 tools stay lean and Aggregator does the heavy fusion, as your Stable Master Guide recommends.

If you’d like, in Part 2 I can go tool‑by‑tool and:

Draw separate mini‑diagrams for Stable, Digit, V‑TRAC, Hot Zones, Aux/BA, showing exact inputs, core features, key outputs, and the precise columns the Aggregator should read.

Then in Part 3, map out the Aggregator + A01–A12 indicator flow as its own architecture with concrete join keys and scoring steps.

But for now, this Part‑1 diagram gives you a clean, state‑of‑the‑art top‑level blueprint that:

Reflects the actual code wiring and file paths you’re using today, and

Leaves a clearly marked slot for the profit‑driven Aggregator and indicator layer you’re about to build.