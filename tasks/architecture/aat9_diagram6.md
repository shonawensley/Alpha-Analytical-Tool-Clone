TL;DR:
Part 1 gives you a single, high‑level architecture diagram of what is actually wired today in AAT9:

Brain‑0: table & draws pipelines (from Pick3StatsC4 workbooks + results files).

Brain‑1: per‑state analyzers on string tables (Stable, Digit Reduction, V‑TRAC, Hot Zones) + draws‑only Aux/BA.

Brain‑2 shell: the Control Center + batch flow that orchestrates runs and produces lean outputs and winners artifacts, ready for the Aggregator/alerts layer.

Everything below is designed to be dropped straight into a new doc like
docs/AAT9_DOCS/AAT9_Architecture_Final_Part1.md.

Part 1 – System & Data Spine (What’s Actually Wired)
1. Top‑Level View: from Excel → Tools → Control Center (Brain‑0 → Brain‑1 → Brain‑2)

AAT9 is explicitly a two‑brain architecture:

Brain‑1: per‑state tools (Stable, Digit Reduction, V‑TRAC, Hot Zones, Aux) that analyse CSV tables and draws.

Brain‑2: Control Center + future Aggregator that combine those outputs across states for portfolio decisions.

The current wiring is already summarized in the Live Wiring doc and dir layout:

Tables pipeline: workbooks → data/outputs/tables/<STATE>/ (Combined/Midday/Evening).

Draws pipeline: draws‑only CSVs under data/cleaned/*_draws.csv for Aux/BA/Control Center.

Analyzers: Stable, DR, V‑TRAC, Hot Zones read the string tables (or JSON mirror) and write into data/outputs/analysis/<tool>/<STATE>/... (the “brain bundles”).

Control Center (Brain‑2 shell): orchestrates tables build, winners logging, and module runs over multiple states, then surfaces results in the UI.

Here is the master data‑flow diagram focusing strictly on what is live and wired:

flowchart TB

subgraph Hist[Brain‑0: History & Tables Pipeline]
  H[data/history/Pick3StatsC4_YYYY‑MM‑DD.xlsm]
  R[data/results/YYYY‑MM‑DD.txt]

  H -->|run_tables_with_guard<br/>generate_tables_pipeline.bat| T[data/outputs/tables/<STATE>/...]
  T --> JT[data/outputs/json_tables/<STATE>_tables.json]
  H -->|Aux draws pipeline<br/>(separate scripts / Control Center)| DCSV[data/cleaned/*_draws.csv]
end

subgraph Brain1[Brain‑1: Per‑State Analysis (Tools)]
  direction TB

  subgraph Stable[Stable Pattern (Module A)]
    ST[alpha_analytical/stable<br/>+ src/core/stable_pattern_extractor.py]
    ST --> ST_OUT[data/outputs/analysis/patterns/<STATE>/...]
  end

  subgraph DR[Digit Reduction (Module B)]
    DRP[src/core/module_b_digit_reduction.py<br/>+ analyzer_v2]
    DRP --> DR_OUT[data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/{per_item,top,meta}.csv/json]
  end

  subgraph VT[V‑TRAC Analyzer (Module D)]
    VTP[src/core/module_c_vtrac.py<br/>modules/vtrac_enhanced/*]
    VTP --> VT_OUT[data/outputs/analysis/vtrac/<STATE>/...]
  end

  subgraph HZ[Hot Zones (Module C)]
    HZE[alpha_analytical/hot_zones/*<br/>scripts/hot_zones/run_hot_zones_cli.py]
    HZE --> HZ_OUT[data/outputs/analysis/hot_zones/<STATE>/...]
  end

  subgraph AUX[Aux & Blackapple (Draws‑only)]
    AUXENG[modules.aux_loaders<br/>modules.blackapple<br/>positional_tool.py]
    AUXENG --> AUX_UI[Aux / BA tables<br/>(UI only, no analysis dir)]
  end
end

T --> ST
T --> DRP
T --> VTP
JT --> HZE
DCSV --> AUXENG

subgraph Brain2[Brain‑2 Shell: Control Center & Winners]
  CC[Control Center page<br/>+ batch runner]
  WL[Winners logger HTML/JSON<br/>reports/stable/winners_by_date/<DATE>/...]
end

T --> CC
DCSV --> CC
R --> WL
CC --> WL

ST_OUT --> CC
DR_OUT --> CC
VT_OUT --> CC
HZ_OUT --> CC
AUX_UI --> CC


This diagram is basically a cleaned‑up superset of the existing dir‑layout and Live Wiring mermaid, plus the Hot Zones and winners pieces.

2. Brain‑0 – Dataset Creation (What the tools actually sit on)

Goal: ensure every tool reads from a consistent, validated backbone:

Tables (for string‑table tools):

Combined/Midday/Evening CSVs per state under data/outputs/tables/<STATE>/.

Produced by guarded runners like run_tables_with_guard.py, with a manifest documenting which workbook is active.

JSON table mirrors (for Hot Zones + future tooling):

data/outputs/json_tables/<STATE>_tables.json – same content as tables, JSON‑structured.

Draws CSVs (for Aux/BA/Control Center doubles logic):

data/cleaned/*_draws.csv is the canonical draws‑only source; Aux/Blackapple and Control Center consume this directly, not string tables.

Winners files (for overlays + validation):

data/results/YYYY-MM-DD.txt feeds the winners logger and three‑table HTML overlays, and is always day‑ahead of the history workbook.

Key invariant:

Combined is the baseline dataset. Midday/Evening are additive variants surfaced alongside Combined; string‑table tools always treat Combined as canonical.

This is the “spine” everything else sits on.

3. Brain‑1 – Per‑State Tools Actually Wired Today

Brain‑1 is “per‑state brain”: each tool runs on one state at a time, reading from the shared tables/draws, and writing lean outputs into data/outputs/analysis/... that the Control Center (and later the Aggregator) can consume.

3.1 Shared wiring contract

Live Wiring spells out the real wiring and inputs/outputs per module:

All string‑table tools use utils.path_handler to resolve data/outputs/tables/<STATE>/.

Aux/BA only read draws CSVs under data/cleaned/*_draws.csv.

That contract is already enforced by preflight and Workflow Standard.

3.2 Stable Pattern – Module A

What it is (live):

Entry: src/core/stable_pattern_extractor.py → alpha_analytical/stable/*.

Inputs: data/outputs/tables/<STATE>/ Combined tables.

Outputs: data/outputs/analysis/patterns/<STATE>/ including:

<STATE>_stable_patterns_scores.csv (scored patterns).

<STATE>_stable_patterns_families.csv (pattern families).

<STATE>_stable_patterns_compound.csv + metrics and optional winners spotlight CSVs.

Brain vs projector:

Brain: extractor, feature_config.yml, persistence and compound scoring logic.

Projector: HTML reports + winners spotlight; for architecture we care most about the scores/families CSV + metrics.json as aggregator inputs.

3.3 Digit Reduction – Module B

What it is (live):

Entry: src/core/module_b_digit_reduction.py; core reducer in long_string_reducer_part*.py.

Analyzer: alpha_analytical/digit_reduction/analyzer_v2/*.

Inputs:

Combined tables via utils.path_handler.

Winners HTML/JSON overlays from reports/stable/winners_by_date/<DATE>/.

Outputs (“brain bundle”):

data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/ with:

*_per_item.csv

*_top_candidates.csv

*_meta.json

optional stacked HTML for dev inspection.

Why it matters to architecture:

These lean outputs already carry aggregator‑facing features: VT‑only flags, LS ladder flags, recency and persistence, etc. (vt_only_lane, funnel_precol1, ls_col_42, ls2_lane, ls2_progress).

That’s why the validation docs say the Aggregator should drive off the lean bundles, not the HTML overlays.

3.4 V‑TRAC Analyzer – Module D

What it is (live):

Entry: src/core/module_c_vtrac.py with an enhanced engine under modules/vtrac_enhanced/*.

Inputs: Combined tables via data/outputs/tables/<STATE>/.

Outputs: data/outputs/analysis/vtrac/<STATE>/ with analyzer CSV/JSON, evidence grid, overlays, and compact validation/summary reports.

Aggregator‑relevant signals (already defined in logs/specs):

Evidence grid: VT straights, family hits, column/ring weights.

Winners reports: per‑index evidence, used later in the Winners Module and Aggregator docs.

3.5 Hot Zones – Module C (wired as environment radar)

What it is (live CLI + planned app integration):

Entry: alpha_analytical/hot_zones/*; CLI: scripts/hot_zones/run_hot_zones_cli.py.

Inputs: JSON tables data/outputs/json_tables/<STATE>_tables.json.

Outputs:

<STATE>_hot_zones_per_lane.csv

<STATE>_hot_zones_top_lanes.csv

<STATE>_hot_zones_meta.json

winner maps YYYYMMDD_hot_zones_winner_map.{json,csv}.

How architecture treats it:

Not just “another scorer”; it’s environment radar: lane IDs, lane scores/ranks, variant coverage, and “environment class” (Calm / Focused / Noisy).

Overlap flags (HZ_OVERLAP_DR / VTRAC / STABLE / AUX) are the intended aggregator inputs rather than per‑candidate scores.

3.6 Aux / Blackapple + Positional Pressure (draws‑only)

What they are (live):

Engines:

Aux loaders: modules/aux_loaders.py.

Blackapple: modules/blackapple.py (score, triggers, candidates from draws only).

Positional Pressure: modules/module_d_auxiliary_tools/refactored/positional_tool.py.

Inputs: exclusively data/cleaned/*_draws.csv (Combined+Midday+Evening variants via load_state_draws(state, variant)).

Outputs:

In‑page rendered tables and badges: doubles trackers, BA status/trigger/candidates, positional pressure summaries – they don’t write into data/outputs/analysis yet; they are “projector only”.

Why this matters for the diagram:

In your architecture, Aux/BA sit on a parallel, draws‑only backbone feeding Control Center and per‑state Aux pages, so they’re clearly separated from the string‑table analyzers. This is explicitly enforced in dir layout & Workflow Standard.

4. Brain‑2 Shell – Control Center + Winners Layer (No Aggregator yet)

Right now, Brain‑2 in code is mainly:

Control Center page:

Uses draws CSVs (data/cleaned/*_draws.csv) and combined tables via utils.path_handler to render:

Doubles tracker (“draws since last double”) across states + variants.

Blackapple summary tables per variant (Combined/Midday/Evening).

Acts as a batch front‑end to:

Run the tables pipeline.

Run per‑state Stable/DR/V‑TRAC/Hot Zones.

Run winners logging, producing HTML/JSON overlays and module‑specific bundles.

Winners logger (Analyzer‑style full report & V‑TRAC winner views):

Reads tables and results to generate the three‑pane V‑TRAC/DR/Stable winner view under reports/stable/winners_by_date/<DATE>/<STATE>/....

These HTML/JSON outputs are projector: they are the “ground truth environment lens” for Master Validation and for explaining scores, not direct aggregator inputs.

Lean‑output discipline for Aggregator:

Final‑Validation docs stress: the Aggregator and future alerts must drive off the lean outputs (per_item/top/meta + compact reports), not projector HTMLs.

That’s why we already document an “Aggregator Inbox mini‑spec” in the checklist: it names the small set of fields per module that Brain‑2 is allowed to use (pattern_key, vt_only_lane, recency_lane, hot_level, pos.double_pressure, etc.).

At this point, Brain‑2 = Control Center + Winners + lean bundles, with the Aggregator as a documented, not‑yet‑wired layer on top.

5. How this Part‑1 Diagram Fits Your Goals

You asked to focus on:

What is actually wired into the app

The diagram and sections above stick strictly to live paths documented in Live Wiring, dir layout, Quickstart, and Final‑Validation docs: tables & JSON pipeline, draws backbone, Stable/DR/V‑TRAC/Hot Zones, Aux/BA, Control Center, winners logging.

Tools we’re likely to keep post Master‑Validation/Aggregation

Those are explicitly named as the four core tools (Stable, Digit, V‑TRAC, Hot Zones) plus Aux as a first‑class environment and confirmation layer; Macro Roadmap and Architecture/Validation docs both treat them as canonical.

Brain‑1 / Brain‑2 dynamic as reflected in the app

Brain‑1: per‑state analysis directories under data/outputs/analysis/<tool>/<STATE>/....

Brain‑2: Control Center, doubles/BA summaries, winners HTML/JSON, and the planned Aggregator inbox and synergy reports sitting on top of those lean bundles.

This Part‑1 doc gives you a single, authoritative diagram and narrative you can hand to future agents or devs as the anchor:

“If it’s not on this diagram, it’s either legacy or experimental. Brain‑1 tools and Brain‑2 shell sit on the data spine exactly as shown.”

Sanity Check – Two quick actions for you

To be sure this Part‑1 architecture truly matches your repo:

Open the Live Wiring diagram and compare:

Open docs/AAT9_DOCS/AAT9_Architecture_Dir_Layout_2025-09-06.md and confirm the mermaid block’s nodes (tables, app pages, draws) match the “System & Data Spine” diagram above.

Spot‑check one state through the whole spine:

For a state like Connecticut4, confirm you can see:

data/outputs/tables/Connecticut4/Combined_Combined.csv

data/outputs/analysis/patterns/Connecticut4/...

data/outputs/analysis/digit_reduction/Connecticut4/analyzer_v2/...

data/outputs/analysis/vtrac/Connecticut4/...

data/outputs/analysis/hot_zones/Connecticut4/... (if already run)

data/cleaned/Connecticut4_draws.csv

reports/stable/winners_by_date/<DATE>/Connecticut4/...

If both checks line up, we can safely treat this as the canonical Part‑1 architecture and, in the next parts, zoom into:

Per‑module feature contracts (what Aggregator can read),

The Brain‑2 Aggregator + alert layers,

And the final end‑to‑end workflow from “daily run” to “play/no‑play decision & ROI logging.”


__________________________


TL;DR:
This is Part 2 of your final AAT9 architecture: it defines the Brain‑1 tool contracts and the Aggregator inbox – i.e., exactly what each module is allowed to hand to the super‑brain.
Think of this as: “If a value isn’t in this contract, Brain‑2 is not allowed to use it.”

Part 2 – Brain‑1 Tool Contracts & Aggregator Inbox
2.0 Why this part matters

Part 1 gave you the wiring (tables → tools → Control Center).

Part 2 gives you the data contracts that the future Aggregator + alerts will rely on.

Goal here:

Lock down what each tool contributes to the global view (in a small, stable set of fields).

Define a single “pattern row” schema that the Aggregator will read per state/date.

Make it easy for Master Validation to say: “This field is trustworthy and in‑scope for Brain‑2; that one is dev‑only.”

I’ll keep this conceptual but concrete enough that you can turn it into an actual schema file or doc.

2.1 Aggregator inbox: the “pattern row” mental model

For every run (state + date + variant combo), the Aggregator should work on a unified row that represents one pattern / family / candidate set, e.g.:

a Stable family,

a Digit Reduction ladder (one R2 long‑string box),

a V‑TRAC lane or index family,

a Hot Zones lane,

or a fused entity that merges several of these when they clearly align.

Let’s call that row a pattern unit.

 

At minimum, each pattern unit needs:

Identity (what we’re talking about)

Scores & evidence (how strong it is in each tool)

Context (state, date, variant, lane, etc.)

Outcome tags (did it lead to a winner? what class?)

The Aggregator inbox is therefore a flat table with columns like:

state, date, variant, pattern_key,
stable_score, stable_tier, stable_family_size,
digit_score, vt_only_lane, ls2_lane, funnel_precol1, ls2_progress,
vtrac_score, vt_index, vt_lane_rank,
hot_level, hot_overlap_stable, hot_overlap_digit, hot_overlap_vtrac,
aux_pos_pressure, aux_double_pressure, aux_ba_tier,
winner_exact, winner_boxed, winner_vt_boxed, winner_vt_straight,
...


You don’t have to implement every column at once; but everything Brain‑2 cares about should fit into this pattern‑row idea.

 

Now we’ll define what each module is allowed to contribute to that row.

2.2 Digit Reduction – Aggregator contract (what’s already defined)

Digit Reduction is the most fully specified module already. Your recent Digit logs spell out:

The brain bundle files Aggregator can rely on:

.../digit_reduction/<STATE>/analyzer_v2/:

<STATE>_analyzer_v2_per_item.csv

<STATE>_analyzer_v2_top_candidates.csv

<STATE>_analyzer_v2_meta.json

Winners overlays/flags/hits under analyzer_v2/winners/ with dr.win_vt_boxed, dr.win_vt_straight etc.

The key scoring features that were proven in training and explicitly wired:

vt_only_lane

funnel_precol1

ls_col_42

ls2_lane

ls2_progress

drop_digit_mode_stability

persistence and recency fields (earliest_*, persistence_*, recency_carryover)

winners flags: dr.win_vt_boxed, dr.win_vt_straight and the four‑class taxonomy aligned with Stable.【user text you pasted】

From your Digit Analysis logs and Unified Changelog, you’ve explicitly marked these as integrator‑facing – they’re meant for the Aggregator, not just debugging.

 

So, the Digit → Aggregator contract can be written as:

2.2.1 Identity fields from Digit

Per pattern row, Aggregator can read:

state

date / results_date / run_stamp (exact name as per per_item/top/meta)

variant (Combined, Midday, Evening)

pattern_key – whatever identifies the LS ladder (long string ID + box column indices; exact encoding can be left as “Digit’s canonical ID”).

2.2.2 Core scoring / evidence fields (allowed for Brain‑2)

From per_item.csv (and mirrored in top_candidates.csv):

digit_score (the final analyzer score for that ladder; exact column name from per_item).

vt_only_lane – 1 if the pattern’s evidence was VT‑only (no exact hits).

ls2_lane – 1 if the ladder terminates in LS2 / Method‑T style endings.

funnel_precol1 – 1 if the ladder spent time in Set1 col‑4/3 before col‑1.

ls_col_42 – 1 if the Set1 col‑4/2 ladders were active for this row.

ls2_progress – float in [0,1] that measures extended ladder proximity.

drop_digit_mode_stability – stability of the one‑digit drop pattern.

earliest_exact / earliest_vt – earliest step index at which exact or VT hits appeared.

persistence_exact / persistence_vt – how long the evidence survived.

recency_carryover – whether the family carried over through recent draws (exact names per config/feature spec).

These are explicitly described in your Digit Integrator notes and lean‑outputs doc as the key interpretable features the scorer uses.

2.2.3 Outcome / winner flags

From winners overlays/flags/hits:

dr_win_exact_straight – 1 if this ladder contained the straight winner.

dr_win_exact_boxed – 1 if this ladder contained the boxed winner (non‑VT).

dr_win_vt_boxed – 1 if winner hit as VT box.

dr_win_vt_straight – 1 if winner hit in a VT‑aligned straight lane.

These are exactly the four hit classes that Digit was updated to expose, aligned with Stable’s taxonomy.

 

In the Aggregator row, these will typically be copied over (or merged via the central Winners module).

2.2.4 What Digit does not expose to Brain‑2

Raw steps logs and HTML overlays are projectors only – they’re for Master Validation and debugging, not for Aggregator ranking decisions.

Experimental or low‑impact features that aren’t documented in the Digit Analysis Log / Lean‑Outputs doc shouldn’t be used by Brain‑2.

2.3 Stable Pattern – Aggregator contract (conceptual but bounded)

For Stable, you already have:

stable_patterns_scores.csv

stable_patterns_families.csv

stable_patterns_compound.csv

metrics.json per state.【AAT9_Live_Wiring_and_Data_Paths + stable docs】

The stable docs describe:

a base score per family,

a notion of tiers / pattern types,

and compound signals (multi‑family or multi‑pattern evidence).

Even if the column names are more verbose, you can define a Stable → Aggregator view with:

2.3.1 Identity

state, date, variant

pattern_key – here, likely the Stable family ID (exact encoding from stable_patterns_families.csv).

2.3.2 Stable summary fields

From scores/families/metrics:

stable_score – the main stable score per family (numeric).

stable_tier – categorical (e.g., Tier1/2/3, or “core/secondary/experimental”).

stable_family_size – count of triads in the family.

stable_repeat_tag – whether it’s a repeating family across runs (if such flag exists in metrics).

stable_compound_score – if the compound CSV provides an aggregate or synergy score for families.

Even if the exact field names differ, your AAT9_Analyzer_Lean_Outputs doc will identify which columns are meant for the Aggregator. The architecture here says:

For Stable, restrict Brain‑2 usage to:
score, tier, family size / coverage, compound score, and simple pattern class tags.
Everything else stays dev‑only.

2.3.3 Outcome linkage

Stable itself may not carry winner flags; winner hits are typically computed at the Winners module. So in the Aggregator row:

You’ll attach stable_win_any / stable_win_family based on whether the stable family mapped to a winner in winner_flags, not by reading Stable CSV alone.

2.4 V‑TRAC Analyzer – Aggregator contract

From your V‑TRAC module and analysis logs, we know:

It produces per‑index and per‑lane evidence grids and compact share bundles.

It’s deeply aligned with your A09 VT‑echo concept and with the winners logger/overlay panels.

For Aggregator purposes, you want something like:

2.4.1 Identity

state, date, variant

vt_index – the main V‑TRAC index for the family/lane.

pattern_key – w.l.o.g., combine vt_index with lane ID to avoid conflicts.

2.4.2 Evidence fields

From the analyzer CSV/JSON and compact reports:

vtrac_score – main numeric strength of the lane.

vtrac_lane_rank – ranking within the state/variant.

vtrac_repeat_flag – 1 if this lane corresponds to a repeating VT index across recent runs (feeds directly into an A09‑like alert).

vtrac_straight_bias – if the report distinguishes lanes that drive straight winners more than boxes.

vtrac_coverage – how many draws or families the lane covers (optional).

Again, exact names will come from AAT9_Analyzer_Lean_Outputs and any V‑TRAC appendices, but architecturally, these are the only classes of V‑TRAC features Brain‑2 should see.

2.4.3 Outcome flags

From the Winners module / winner maps:

vtrac_win_exact – 1 if the lane matched the exact winner.

vtrac_win_boxed – 1 if the lane matched as a VT box.

vtrac_win_family – 1 if lane’s family captured the winner.

2.5 Hot Zones – Aggregator contract

Your Hot Zones validation log describes:

per‑lane scoring/flags,

a top‑lanes summary,

environment classification (calm / focused / noisy),

and cross‑over with DR/Stable/V‑TRAC and Aux.【AAT9_Hot_Zones_Validation_Log.md】

For Aggregator:

2.5.1 Identity

state, date

variant (if per‑variant; otherwise treat as Combined environment).

hz_lane_id – unique lane ID per state/date.

pattern_key – may be hz_lane_id or a composite (safe to treat lane as the pattern unit here).

2.5.2 Evidence fields

From *_hot_zones_per_lane.csv and *_hot_zones_top_lanes.csv:

hot_level – numeric lane strength (or normalized rank).

hot_env_class – e.g., Calm / Focused / Noisy.

hz_lane_rank – rank across lanes for that date/state.

Overlap flags:

hz_overlap_stable – 1 if lane overlaps stable families that scored above threshold.

hz_overlap_digit – 1 if lane lines up with Digit ladders (e.g., LS2 or critical Set1 slots).

hz_overlap_vtrac – 1 if lane intersects strong V‑TRAC indexes.

hz_overlap_aux – 1 if lane’s draws align with Aux/BA hotspots.

These overlap flags are already implied in your Hot Zones validation log (Part A/Part B mapping winners & tools onto lanes) and are meant to be aggregator‑visible.

2.5.3 Outcome flags

From Hot Zones winner maps:

hot_win_exact – 1 if the lane produced the winner that day.

hot_win_any – 1 if the lane produced any win in that evaluation horizon.

2.6 Aux / Blackapple / Positional – Aggregator contract

The Aux world is draws‑only and largely UI today, but your Auxiliary Feature Integration doc defines a clean concept:

Aux features are independent signals with config weights.

“Strings lead, aux compounds.”

Aux scores can boost but never create winners on their own.【AAT9 Auxiliary Feature Integration.md】

For Aggregator, you don’t want every low‑level aux metric; you want a small set of “environment/confirmation” signals.

2.6.1 Identity

state, date, variant

pattern_key – the same pattern unit as the other tools (Stable family, Digit ladder, or V‑TRAC lane) – Aux will attach to these via digits/ranges, not invent its own key.

2.6.2 Aux scalar fields (per pattern)

From BA + positional + doubles metrics:

aux_pos_pressure – numeric score measuring positional pressure favoring this pattern’s digits (P1/P2/P3 ranks and due status).

aux_double_pressure – whether the pattern’s digits sit in high double‑pressure zones.

aux_ba_score – BA composite score for the pattern’s digits.

aux_flags – a compact bitmask or set of booleans for important aux triggers (mirror support, consensus tags, etc.).

Your Aux/BA docs and positional tracker notes already talk about:

doubles pressure,

mirror / consensus tags,

positional shortlist ranks,

and BA tiers (Strong / Medium / Weak).

The architecture rule for Brain‑2 is:

Aux contributes compact scalar confirmations and tags; it does not define the pattern universe or winners.

2.6.3 Aux & winner logging

When a winner is logged, your Aux integration doc says:

log per‑winner aux scores and which aux compound rules fired.

Those logs will be folded into winner_flags / winner_map, not read directly by the Aggregator. Brain‑2 can then use that as “aux_confirmed=1” on winning patterns.

2.7 Winners & outcomes – shared contract

To close the loop, all the tools above must map into a shared hit schema, which your docs already standardize as:

four hit classes (exact_straight, exact_boxed, vt_boxed, vt_straight)

per‑tool win flags (stable, digit, vtrac, hot)

aux confirmations

Architecturally, that means:

A central winner_flags.csv is responsible for:

winner_exact_straight

winner_exact_boxed

winner_vt_boxed

winner_vt_straight

digit_win_any / stable_win_any / vtrac_win_any / hot_win_any

aux_confirmed (at least a boolean).

The Aggregator inbox must always carry, per pattern row:

either a direct link to the winner flags (pattern_key ↔ winner_id), or

explicit *_win_* columns as described above.

Master Validation will treat these as the truth when checking whether a high‑synergy row actually landed a hit in the context of the full system.

2.8 Putting it together – conceptual schema for aggregator_inbox

Here’s an example of what a first‑cut schema for the Aggregator inbox table could look like (conceptual; you will align exact names with AAT9_Analyzer_Lean_Outputs):

# Core identifiers
state
results_date
variant          # Combined / Midday / Evening
pattern_key      # canonical pattern ID (family/ladder/lane)

# Stable features
stable_score
stable_tier
stable_family_size
stable_compound_score

# Digit Reduction features
digit_score
vt_only_lane
ls2_lane
funnel_precol1
ls_col_42
ls2_progress
drop_digit_mode_stability
earliest_exact
earliest_vt
persistence_exact
persistence_vt
recency_carryover

# V-TRAC features
vt_index
vtrac_score
vtrac_lane_rank
vtrac_repeat_flag
vtrac_straight_bias

# Hot Zones features
hz_lane_id
hot_level
hz_lane_rank
hot_env_class
hz_overlap_stable
hz_overlap_digit
hz_overlap_vtrac
hz_overlap_aux

# Aux/BA features
aux_pos_pressure
aux_double_pressure
aux_ba_score
aux_flags   # e.g., encoded bitmask/tag-set

# Outcomes (via winner_flags)
winner_exact_straight
winner_exact_boxed
winner_vt_boxed
winner_vt_straight
digit_win_any
stable_win_any
vtrac_win_any
hot_win_any
aux_confirmed


This is the whole “inbox” Brain‑2 should see. Inside Brain‑2, you’ll compute:

final synergy score,

A01–A12 indicators,

and decisions (play/no‑play) – but none of those need extra raw tool internals beyond this contract.

2.9 How this helps Master Validation & future devs

Master Validation, when you run the state templates, can now say:

“For this pattern, we see digit_score high, vt_only_lane=1, hot_level high, aux_pos_pressure high, but stable_score low – should synergy still rank it top?”

or “LS2 lane with vt_only_lane=1 and aux_confirmed=1 yet winner_exact_straight=0 – good near‑miss, but not an actual hit.”

Future agents don’t have to re‑understand all raw analyzer fields; they only need this contract to know what’s safe for Brain‑2 use.

Implementation: you can materialize aggregator_inbox as:

a CSV per state/date, generated by a small script that:

reads tool lean bundles,

joins them by pattern_key,

joins winner_flags,

and outputs exactly these columns.

If you’d like me to continue from here, the next “optimal” piece would be Part 3, where I:

Design the central Winners module schema (winner_map.json / winner_flags.csv) explicitly.

Show how to join each tool’s pattern_key and the Aggregator inbox to those winner records.

And outline how A01–A12 indicators read from aggregator_inbox + winner_flags without touching raw tool outputs directly.


_________________________________________


This is Part 3 of your final AAT9 architecture: it defines the central Winners layer and how it connects Brain‑1 tool outputs to the Aggregator inbox and future A01–A12 Brain‑2 indicators.

 

Think of Part 3 as:

“Here is exactly how a winner is represented in the system, how each tool says ‘I saw this winner’, and how the super‑brain gets that information in one place.”

3.0 Role of the Winners Layer (why we need it)

By design, AAT9 separates:

Brain‑1: tools that read string tables / draws and produce rich per‑state analytics (Stable, Digit Reduction, V‑TRAC, Hot Zones, Aux).

Brain‑2: the super‑brain that cares only about:

Which patterns/families were strong.

Which ones actually caught winners (and how: exact/box/VT).

Which environments/alerts (A01–A12) were “right” or “wrong” for that day.

The Winners layer is the bridge:

It takes the raw winners (from data/results/*.txt and winners HTML/JSON).

It merges in each tool’s “hit” information.

It produces a single canonical record per winner plus a flat flags table that the Aggregator and A01–A12 can consume in a uniform way.

Without that, you’d be hard‑coding tool‑specific logic all over Brain‑2.

3.1 Entities in the winners space

Let’s define a couple of key ideas:

3.1.1 winner_id

A winner in AAT9 is uniquely identified by:

state (e.g., Connecticut4)

results_date (e.g., 2025‑06‑23)

variant (Combined / Midday / Evening)

draw_index (Midday vs Evening, or a unique tag)

digits (triad, e.g., "130")

All of that together is your winner_id. It’s the anchor for joins.

3.1.2 pattern_key (recap from Part 2)

A pattern unit is what Brain‑1 tools emit (and Aggregator ranks):

Stable family (family ID).

Digit ladder (long‑string R2 box ID).

V‑TRAC lane/index.

Hot Zones lane.

Each pattern has a pattern_key that identifies it within a state/date/variant.

 

The Winners layer’s job is to answer the question:

“For this winner_id, which pattern_keys from each tool were responsible; and in what class (exact, box, VT)?”

3.2 Winners pipeline stages

Architecturally, the winners pipeline sits between the winners logging (Brain‑1 UI/projector) and the Aggregator inbox (Part 2).

 

We can think of it in four stages:

flowchart LR
  R[data/results/YYYY-MM-DD.txt] --> WGEN[winners HTML/JSON<br/>per state/variant]
  WGEN --> WM[winner_map.json<br/>(per date)]
  WM --> WF[winner_flags.csv<br/>(flat flags)]
  WM --> PATT[pattern_winner_links.csv<br/>(pattern_key ↔ winner_id)]
  WF --> AGG_IN[aggregator_inbox.csv<br/>(Part 2)]
  PATT --> AGG_IN


WGEN – what you already have from generate_winners_from_results.py: HTML/JSON overlays per state/variant.

WM – new winner_map.json: structured view of each winner with all tools’ contributions.

WF – new winner_flags.csv: slim, flat flags per winner; easy to join in Pandas or SQL.

PATT – optional pattern_winner_links.csv: maps pattern_key ↔ winner_id when you need multi‑winner or multi‑pattern relationships.

AGG_IN – the Aggregator inbox defined in Part 2, enriched with win columns.

3.3 winner_map.json – canonical winners object

Goal: a readable JSON (or JSONL) file per date that captures all the structured data about each winner.

3.3.1 Minimal layout per winner

For each winner_id, you want something like:

{
  "winner_id": "Connecticut4_2025-06-23_Midday_130",
  "state": "Connecticut4",
  "results_date": "2025-06-23",
  "variant": "Midday",
  "draw_index": "Midday",
  "digits": "130",
  "vt_index": 8,
  "meta": {
    "history_workbook": "Pick3StatsC4_2025-06-22.xlsm",
    "tables_manifest_checksum": "d25b3d...",
    "env_stamp": "20250623"
  },
  "classes": {
    "exact_straight": true,
    "exact_boxed": true,
    "vt_boxed": true,
    "vt_straight": false
  },
  "tools": {
    "digit": {
      "pattern_keys": ["DR_CT_R2_LS1_col7", "DR_CT_LS2_col1"],
      "hit_exact": true,
      "hit_vt_boxed": true,
      "hit_vt_straight": false,
      "rank_in_top_candidates": 1
    },
    "stable": {
      "family_keys": ["ST_CT_FAM_123"],
      "hit_family": true,
      "score_at_hit": 9.8,
      "tier": "Tier1"
    },
    "vtrac": {
      "lane_keys": ["VT_CT_IDX8_MAINLANE"],
      "hit_lane": true,
      "repeat_flag": true
    },
    "hot_zones": {
      "lane_ids": ["HZ_CT_LANE_5"],
      "hit_lane": true,
      "env_class": "Focused"
    },
    "aux": {
      "aux_confirmed": true,
      "ba_tier": "Strong",
      "positional_confirmed": true
    }
  }
}


You don’t need to implement every field at once; this is the shape you’re aiming for.

 

Key pieces:

classes – the four standard win classes; Brain‑2 treats these as the canonical success taxonomy.

tools – what each module says about this winner:

which pattern_keys or lane IDs were involved,

whether they “hit” in their own terms,

optional context like rank or tier at time of hit.

3.3.2 How to populate winner_map.json from existing artifacts

At a high level:

Start from winners HTML/JSON per state/variant for a date (WGEN output).

For each winner:

Extract state, variant, digits, vt_index, etc.

Load each tool’s winner‑aware artifacts:

Digit: winners overlays/flags/hits (with dr.win_vt_boxed / dr.win_vt_straight etc.) (user text)

Stable: winners spotlight CSVs that mark which families contain the winner. (user text)

V‑TRAC: winner report / compact share bundles per index. (user text)

Hot Zones: *_hot_zones_winner_map.{json,csv}. (user text)

Aux: any per‑winner logging from Aux Integration (e.g., aux scores on that triad). (user text)

For each tool, record:

which pattern_keys or family IDs were responsible,

whether they matched the winner,

key contextual metrics (rank, tier).

This can be implemented as one Python script living in a clear path like:

scripts/winners/build_winner_map.py

that writes reports/stable/winner_map/<DATE>/winner_map.json.

3.4 winner_flags.csv – the flat, Aggregator‑friendly view

Goal: simple CSV with one row per winner_id, containing the minimal flags Brain‑2 cares about.

 

A practical schema could look like:

winner_id
state
results_date
variant
digits
vt_index

winner_exact_straight
winner_exact_boxed
winner_vt_boxed
winner_vt_straight

digit_win_any
stable_win_any
vtrac_win_any
hot_win_any
aux_confirmed

digit_pattern_keys
stable_family_keys
vtrac_lane_keys
hot_lane_ids


Notes:

digit_win_any / stable_win_any / vtrac_win_any / hot_win_any are booleans derived from the tools section in winner_map.json (true if that tool ever recognized the winner).

digits and vt_index allow you to cross‑check with raw overlays if needed.

*_pattern_keys lists (possibly comma‑separated) are optional but useful for debugging or joining back to pattern rows later.

Implementation: build_winner_map.py can easily emit both winner_map.json and winner_flags.csv from the same pass.

3.5 Pattern ↔ winner links (pattern_winner_links.csv)

For the Aggregator inbox in Part 2, each pattern row wants to know:

Did we hit a winner?

In what class?

You can either:

attach hit flags directly in tool outputs (as Digit already does with dr_win_*), and propagate them during Aggregator ingestion, or

define a small join table between patterns and winners.

A general‑purpose join table is flexible and future‑proof:

# pattern_winner_links.csv

state
results_date
variant
pattern_key
winner_id
hit_exact_straight
hit_exact_boxed
hit_vt_boxed
hit_vt_straight
tool_name   # "digit" / "stable" / "vtrac" / "hot_zones"


You can derive this table by:

Iterating over winner_map.json.

For each tool entry, emit one row per (pattern_key, winner_id) pair, with appropriate hit flags.

Then, when you build aggregator_inbox.csv (Part 2):

You join pattern rows with pattern_winner_links on (state, results_date, variant, pattern_key)

You aggregate flags (e.g., any hit on that pattern today?), or filter to “today’s winners only”.

This keeps pattern scoring logic clean and delegates all hit logic to a single dedicated place.

3.6 How Winners connects to the Aggregator inbox

Recall the Aggregator inbox schema sketch from Part 2. We can now explain where the win‑related columns come from:

winner_exact_straight, winner_exact_boxed, winner_vt_boxed, winner_vt_straight

Come from winner_flags.csv and/or pattern_winner_links.csv.

For a given pattern row, you can either:

look up its winner(s) via pattern_winner_links, or

if the tool already carries *_win_* flags (Digit), just copy them.

digit_win_any, stable_win_any, vtrac_win_any, hot_win_any, aux_confirmed

Are directly the *_win_any / aux_confirmed columns from winner_flags.csv, optionally filtered to the main triad of interest (same digits).

This ensures Brain‑2 never has to parse raw HTML or individual tool outputs. It sees only:

pattern features (Part 2),

plus these standardized hit flags from the Winners layer.

3.7 Preparing for A01–A12 (Brain‑2 alerts) on top of Winners + Aggregator

Your profit blueprint and validation docs describe A01–A12 indicators as a lean, interpretable layer that sits on top of:

Brain‑1 metrics,

Aggregator synergy scores,

and Winners outcomes.

We won’t define each indicator numerically here (that belongs to your profit blueprint), but we can define their data interface.

3.7.1 alerts_A01_A12.csv – daily alert table

For each state / results_date (/ variant if you decide per‑variant alerts), you can have:

state
results_date
variant

# per-alert flags / scores
A01_fired
A01_score
A02_fired
A02_score
...
A12_fired
A12_score

# optional explanation / context
BA_summary
vt_repeat_summary
double_pressure_summary
env_summary


These values would be computed by a Brain‑2 script (e.g., scripts/control_center/compute_alerts.py) that reads:

aggregator_inbox.csv (pattern rows with synergy + tool scores + aux flags),

winner_flags.csv (how the day actually turned out),

possibly a historical metrics file if some alerts are cross‑day (e.g., repeating VT indices or long “no‑hit” streaks).

The architectural rule:

A01–A12 never go back to raw tool internals or HTML; they work exclusively on
aggregator_inbox + winner_flags (+ simple state‑level aggregates).

That’s what keeps Brain‑2 logically separated and testable.

3.8 Where Master Validation uses this Winners architecture

Once this Winners layer exists, Master Validation can operate cleanly:

Brain‑1 templates:

Still inspect HTML and tool‑specific overlays for qualitative insight.

But when checking “did this ladder/family actually hit?”, they rely on the winner flags and pattern‑winner links, not manual eyeballing every time.

Brain‑2 templates (Control Center validation):

For each date:

look at alerts_A01_A12.csv (which alerts fired),

join with winner_flags.csv (which states / environments actually produced winners),

and join with summary stats from aggregator_inbox (how many top patterns were winners vs misses).

This gives you a repeatable way to validate A01–A12 using the same data model the live system will use.

3.9 How to turn Part 3 into an actual repo doc

You can make this architecture executable by:

Creating a doc docs/AAT9_DOCS/AAT9_Winners_Architecture.md with:

3.1 Entities (winner_id, pattern_key).

3.3 winner_map.json structure.

3.4 winner_flags.csv schema.

3.5 pattern_winner_links.csv schema.

3.7 alerts_A01_A12.csv schema.

Linking it from:

AAT9_Final_Validation_Help.md as the canonical “Outcome contracts” reference.

AAT9_Analyzer_Lean_Outputs.md (brief section: “All win flags are mediated via the Winners module”).

Later, once you start implementing:

Add a small “Winners module” section to AAT9_Workflow_Standard.md so any agent knows:

where to run the winner map builder,

where to find winner_map.json / winner_flags.csv / pattern_winner_links.csv.

Quick sanity actions for you

To make sure this feels solid and grounded:

Pick one date (e.g., 2025‑06‑23) for one state (e.g., Connecticut4) and manually mock:

a single winner_map JSON object for one winner,

a matching row in winner_flags.csv,

and 1–2 rows in pattern_winner_links.csv tied to existing Digit/Stable patterns.

Check it against your Digit log snippet you pasted:

confirm you can represent “vt_only lane, LS2 lane, rank #1, dr.win_vt_boxed=1” within this structure (you can).

confirm that “vt_only lane but buried in rank #300 with no exact_straight” also has a clean representation.

If those two examples are comfortably representable, this Winners architecture is doing its job: it can describe both great hits and near‑misses coherently for the super‑brain.

If you’d like me to keep going, the next optimal step would be Part 4:

designing the Aggregator scoring logic on top of aggregator_inbox + winner_flags (e.g., how to compute a single synergy_score per pattern),

and showing how A01–A12 plug into that to form a daily “Playboard” view for Control Center.