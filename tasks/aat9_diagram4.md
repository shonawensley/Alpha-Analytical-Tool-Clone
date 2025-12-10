This “Part 4” locks in the data‑contract layer of AAT9 – how Brain 1 tools (Stable, Digit Reduction, V‑TRAC, Hot Zones) write lean outputs, how the central winners module unifies hits, and how the Aggregator turns those into synergy scores and, later, Brain 2 profit boards. Everything below is wired to the actual modules and paths you already have, not wishful thinking.

Part 4 – Data‑Contract Architecture (Brain 1 → Winners → Aggregator → Brain 2)
4.1 Big picture in one diagram

This is the data architecture that sits under the high‑level diagrams we already did:

flowchart LR
    subgraph T[Tables & Results]
      X1[Pick3StatsC4_xxx.xlsm]
      X2[data/results/YYYY-MM-DD.txt]
    end

    subgraph B1[Brain 1 – Per‑tool Analyzers]
      SA[Stable Pattern<br/>Module A]
      DR[Digit Reduction<br/>Module B]
      VT[V‑TRAC Analyzer<br/>(Module D)]
      HZ[Hot Zones<br/>Module C]
    end

    subgraph W[Central Winners Layer]
      WM[winner_map.json<br/>winner_flags.csv]
    end

    subgraph AG[Aggregator (Synergy)]
      SY[aggregator_synergy.json]
    end

    subgraph B2[Brain 2 – Control Center / Profit]
      CC[Control Center Boards<br/>(A01–A12, BA, repeats, doubles)]
    end

    X1 -->|run_tables_with_guard<br/>+ winners generation| T
    T -->|combined tables| SA
    T --> DR
    T --> VT
    T -->|JSON tables| HZ

    SA -->|lean outputs| B1
    DR --> B1
    VT --> B1
    HZ --> B1

    B1 -->|per‑date evidence| WM
    T -->|official winners| WM

    WM -->|hit taxonomy + tool evidence| SY
    B1 -->|scores + features| SY

    SY -->|top candidates + reasons| CC
    WM -->|ground‑truth hit classes| CC


All of these pieces are already described in your docs:

AAT9 is explicitly defined as a four‑module analyzer stack (Stable, Digit Reduction, Hot Zones, V‑TRAC) feeding an Aggregator.

The older AAT9 architecture doc shows exactly this: combined tables → Modules A/B/C → Aggregator → “Final Synergy Scores”.

The module_D_aggregator spec defines the aggregator as merging Stable/Digit/HotZone outputs with synergy bonuses and writing aggregator_synergy.json.

The winners module spec defines a per‑date, per‑variant winner_map.json + winner_flags.csv, with the four hit classes (exact_straight, exact_boxed, vt_boxed, vt_straight) and embedded tool evidence.

Part 4 is about nailing down the contracts and schemas so you (and future agents) can implement the final Brain 2 work cleanly.

4.2 Canonical file contracts (what’s actually wired)
4.2.1 Tables & JSON

From the data‑formats doc: each state has 6 canonical combined/R2 CSVs under data/outputs/tables/<STATE>/, all with the standard columns Set, Draw, RowType, 7, 6, 5, 4, 3, 2, 1.

 

JSON mirrors (for Hot Zones & future APIs) live under data/outputs/json_tables/<STATE>_tables.json.

 

These are already enforced by run_tables_with_guard.py and the String Table testing SOP, which verify the workbook identity and Set1 guard columns before any analyzer runs.

4.2.2 Brain 1 lean outputs

The lean‑outputs spec already declares the Digit Reduction “brain bundle” as canonical; its layout is exactly what the Aggregator and Brain 2 will consume:

data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/

<STATE>_analyzer_v2_per_item.csv – per box candidate, with:

core features: earliest/persistence per evidence type; density; drop metadata; cross‑column / cross‑variant / method echoes; recency flags;

VT & LS: vt_only_lane, funnel_precol1, ls_col_42, ls2_lane;

scoring: score, score_raw, score_v2, final_linear, final_prob, etc.;

winners taxonomy: dr.win_* flags mirroring Stable’s hit classes;

a JSON “reasons” column.

<STATE>_analyzer_v2_top_candidates.csv – per‑family summary, with the same match‑type taxonomy (exact, vtrac, family_vtrac, drop_vtrac) and evidence_tags.

Stable and V‑TRAC are in the process of being leaned out to the same pattern (scores CSV, families/compounds CSV, metrics JSON), and that plan is explicitly documented as the target for the aggregator wiring.

 

You don’t have to invent new formats here – you just treat each tool’s “brain bundle” as:

Per‑item CSV: one row per canonical pattern / box candidate.

Top‑candidates CSV: one row per canonical family.

Meta JSON: config hash + git SHA so Brain 2 can see which version generated the run.

4.3 Central Winners Layer – contract & schema

The winners layer is the bridge between raw winners and tool outputs.

4.3.1 Artifacts and locations

From the winners module and lean‑outputs spec:

winners/YYYYMMDD_<Variant>_winner_map.json

winners/YYYYMMDD_<Variant>_winner_flags.csv

(Optional) winners/YYYYMMDD_summary.md

These are only written by the Control Center batch / winners module, not by the individual tools.

4.3.2 Winner record schema (JSON)

The winners module already sketches a canonical record:

 

Here is that schema made concrete (no placeholders):

{
  "winner": "733",
  "state": "Florida4",
  "variant": "Midday",
  "draw_date": "2025-06-24",
  "classes": {
    "exact_straight": true,
    "exact_boxed": true,
    "vt_boxed": true,
    "vt_straight": true
  },
  "tool_evidence": {
    "stable": {
      "best_compound_rank": 60,
      "found_in_families": true,
      "vt_only_lane": false
    },
    "vtrac": {
      "index": 29,
      "straight_lane": ["733", "373", "337"],
      "best_rank": 5
    },
    "digit_reduction": {
      "top_rank": 12,
      "vt_only_lane": true,
      "ls2_lane": false,
      "funnel_precol1": true
    },
    "aux": {
      "positional_hit": true,
      "double_gap_rank": 3
    }
  }
}


Key design points:

The four hit classes in classes (exact_straight, exact_boxed, vt_boxed, vt_straight) are defined explicitly in the winners module doc and are meant to be the ground‑truth taxonomy for all tools.

tool_evidence is deliberately read‑only: it just quotes ranks and flags that already exist in Stable’s metrics / spotlight CSVs, V‑TRAC’s compact report, and Digit Reduction’s top‑candidates CSV / winners overlay.

You already pushed Digit Reduction to emit dr_win_vt_boxed and dr_win_vt_straight in winner_flags.csv and winner_hits.csv with the same taxonomy as Stable, which aligns perfectly with this design.

4.3.3 Winner flags CSV

A minimal row in winner_flags.csv per winner could look like this, matching your docs:

date,state,variant,winner,exact_straight,exact_boxed,vt_boxed,vt_straight,stable_hit,vtrac_hit,dr_win_vt_boxed,dr_win_vt_straight
2025-06-24,Florida4,Midday,733,1,1,1,1,1,1,0,0


The four class columns mirror the JSON classes.*.

The extra booleans (stable_hit, vtrac_hit, dr_win_vt_boxed, dr_win_vt_straight) mirror the brain‑bundle flags and make it trivial for regression tests and Control Center boards to compute per‑tool hit rates.

This is the only place where ground‑truth is defined; Brain 2 and any ML later should learn exclusively from this taxonomy.

4.4 Aggregator contract – per pattern

The Aggregator spec is already very clear about inputs and outputs:

4.4.1 Inputs

Per state / variant:

Stable: stable_patterns.json (or CSV → JSON mirror) with pattern_str, score_in_module, “where it appears”.

Digit Reduction: digitreduce_patterns.json or “analysis_results” JSON built from per‑item / top‑candidates.

Hot Zones: hotzone_patterns.json with pattern + local_hotzone_score + hot_level.

V‑TRAC: a compact vtrac_corr.json or similar, described in the Stable master guide as “V‑TRAC clusters” exported in a compatible key schema.

The Stable guide also recommends two aggregator strategies:

RAW fusion: concatenate all module CSVs/JSON and rescore together.

Pre‑aggregated: modules collapse to one “best per box” row before shipping to Aggregator.

Given your lean top‑candidates CSVs, you’re well‑positioned for the pre‑aggregated mode.

4.4.2 Output schema: aggregator_synergy.json

module_D_aggregator gives an example synergy report; we just make it concrete and slightly extended.

{
  "aggregator_module": "AAT9 Synergy",
  "timestamp": "2025-06-24T00:00:00Z",
  "state": "Florida4",
  "variant": "Combined",
  "pattern_count": 12,
  "patterns": [
    {
      "canonical_form": "569",
      "pattern_variants": ["695", "956"],
      "modules_found": ["StableExtractor", "DigitReduction", "HotZones"],
      "sections_found": ["Combined", "Midday"],
      "sets_found": ["Set3", "Set2", "Set1"],
      "final_synergy_score": 25,
      "synergy_breakdown": {
        "sum_module_scores": 12,
        "cross_module_bonus": 3,
        "cross_set_bonus": 3,
        "cross_variant_bonus": 3,
        "pending_bonus": 2,
        "hot_super_bonus": 2
      },
      "winner_classes": {
        "exact_straight": true,
        "exact_boxed": true,
        "vt_boxed": true,
        "vt_straight": true
      },
      "brain1_features": {
        "stable_best_rank": 8,
        "dr_best_rank": 3,
        "dr_vt_only_lane": true,
        "dr_ls2_lane": false,
        "dr_funnel_precol1": true,
        "hz_hot_level": 2,
        "vtrac_best_index_rank": 5
      }
    }
  ]
}


This aligns exactly with the aggregator doc’s intent:

Normalize patterns to a canonical form and list variants.

Track which modules saw them and where (sections / sets).

Provide a synergy breakdown that decomposes final_synergy_score into sum of module scores plus bonuses for cross‑module, cross‑set, “pending”, hot‑zone, etc.

I’ve added two fields that are natural extensions, not contradictions:

winner_classes – a direct copy of the winners module classification; this lets Brain 2 (and ML) see which synergistic patterns actually matched winners.

brain1_features – a compact view of key Brain 1 signals (ranks, VT‑only lane, LS2 lane, funnel, hot level) taken from the lean bundles.

These fields don’t require new code in the tools; they just read existing CSV/JSON.

4.5 How Brain 1 concepts flow into Brain 2 rules

This is where your methodology shows up clearly.

4.5.1 Digit Reduction → features used by Aggregator & profit logic

The Digit analysis log and lean‑outputs doc highlight the finalized feature set for aggregation: vt_only_lane, funnel_precol1, ls_col_42, ls2_lane, and the dr.win_* flags that now mirror Stable’s taxonomy.

vt_only_lane – winner had VT evidence but no exact hit; these are the “VT‑only ladders” you want treated as partial wins.

funnel_precol1 / ls_col_42 / ls2_lane – encodes your near‑column ladder and LS2/Method‑T exposure; these were added specifically because repeated unmapped hits in Set1 columns 4/2 and LS2 lanes showed up in your long HTML reviews.

In Brain 2, these become:

Features in brain1_features inside aggregator_synergy.json.

Conditions for alerts A10/A12 in the Profit Blueprint (e.g., DR clamp / 3‑value family confirmation).

4.5.2 Stable / BA / Hot Zones → A01, A11, etc.

The Profit Blueprint spells out the key alerts and how they combine: A01 Dual‑Tail Consensus, A11 Hot‑Zones (star radar), plus A05 Perm‑Lean and A12 DR Clamp for straight lines.

 

The architecture we’ve just defined lets you implement them as pure functions over the synergy / winners layer:

A01: computed from Stable’s consensus/tail fields and BA foundation flags; surfaced either in brain1_features or as its own indicator_scores.A01 field in aggregator_synergy.json.

A11: uses Stable’s star scores + Hot Zone strength to produce a a11_star_level that the Profit Blueprint recommends computing in Stable and logging for Control Center.

A05/A12: combine Stable permutation drift metrics and Digit Reduction clamp signals to decide 8/4/2/1 straight lines.

Nothing here requires a new data path; it’s all derived from:

Per‑tool lean outputs (Stable, Digit, Hot Zones, V‑TRAC).

Winners maps/flags.

Aggregator’s normalized view (aggregator_synergy.json).

4.6 How this ties back to the app wiring

From the AAT9 KIT readme and Live Wiring docs:

The Streamlit app entry (src/app.py) uses utils.path_handler to locate:

combined tables under data/outputs/tables/<STATE>/ for Stable / Digit / V‑TRAC;

JSON tables under data/outputs/json_tables/<STATE>_tables.json for Hot Zones;

Aux/Blackapple draws under data/cleaned/*_draws.csv.

Control Center batch is already the orchestrator that:

runs tables + winners generation per workbook/date;

runs Stable / Digit / V‑TRAC analyzers and writes their brain bundles;

writes central winner_map.json + winner_flags.csv.

The only missing step to complete the architecture is to:

Implement the Aggregator as either:

a CLI (aggregator.py) exactly as suggested in module_D_aggregator.md;

or a Control Center batch step that reads the same lean outputs + winners artifacts and writes aggregator_synergy.json.

Add a Control Center “Brain 2 – Profit Board” page that:

reads aggregator_synergy.json + winner_flags.csv;

computes A0x indicators on top;

draws daily boards (per state + cross‑state) with star levels, BA status, repeat/doubles, and suggested box/straight sets.

Architecturally, everything is now aligned: no new data formats, just wiring together the contracts you already formalized.

Sanity check – 2 concrete actions for you

To verify this Part 4 architecture is usable and grounded:

Pick one date/state and walk the chain manually
For, say, Florida4 on 2025‑06‑24, confirm that you can locate:

data/outputs/tables/Florida4/Combined_Combined.csv

data/outputs/analysis/digit_reduction/Florida4/analyzer_v2/*

winners/20250624_Midday_winner_map.json + winner_flags.csv

(If present) a test aggregator_synergy.json you create by hand from those.
If you can fill one patterns[..] entry using real scores and flags, the schema is correct for implementation.

Draft a minimal Aggregator prototype spec file in your repo
Create docs/AAT9_DOCS/AAT9_Aggregator_Contract.md and paste:

the file paths list from §4.2–4.4;

the JSON examples for winner_map and aggregator_synergy;

a short note that Control Center batch will be the only writer.
That doc becomes the “single source of truth” for whoever implements the final synergy engine.

If you’d like, next step I can turn this into that exact markdown file (with headings ready to drop into the repo) or zoom into one of the layers (e.g., precise Aggregator weights & indicator fields) as “Part 5”.