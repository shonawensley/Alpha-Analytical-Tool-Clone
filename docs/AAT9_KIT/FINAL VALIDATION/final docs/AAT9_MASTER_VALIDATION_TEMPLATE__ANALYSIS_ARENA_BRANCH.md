# AAT9 Master Validation Template — Analysis Arena Branch

Purpose: provide a deliberate Master Validation template for the Analysis Arena branch of the system.

This template is meant to sit on top of the arena-era architecture:
- predictive-side runtime arena artifacts
- frozen/results-side winners artifacts
- arena review harnesses
- state-day and row-level scoreboards

This document is not a tool contract and not a replacement for the arena feed docs.
It is the human review shell for extracting learning from the arena branch in a structured way.

Use alongside:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_ANALYSIS_ARENA_INTEGRATION_QUEUE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_ARENA_ANALYSIS_BACKLOG.md`

Core rule:
- Part A reads the winner-conditioned truth lens first.
- Later parts compare the predictive system against that truth.

Do not blur these:
- winner-conditioned truth reading
- predictive arena evidence
- bounded downstream policy

The template is strongest when it keeps those layers separate.

---

## Template Operating Model

The Analysis Arena branch should be reviewed in this order:

1. `Part A`
   - read the winners HTML / JSON environment lens first
   - analyze how the winning pattern formed before consulting predictive arena judgments

2. `Part B+`
   - review tool and arena evidence against the Part A truth read
   - identify what was preserved, what was promotable, and what stayed only as evidence

3. `Final synthesis`
   - classify the result as:
     - truth preserved and converted
     - truth preserved but underweighted
     - truth visible only in one tool
     - truth absent
   - record bounded hypotheses, not broad analyzer rewrites

Important guardrail:
- the old failure mode was narrowing too early
- the arena-era failure mode would be mixing truth reading, predictive evidence, and downstream policy into one blurred discussion

This template is designed to prevent that.

---

# Part A — Winners Environment Lens

Purpose:
- analyze how the winning pattern formed across the three variant string-table environments
- identify the true structural environment of the win
- do this before judging the predictive arena, Candidate Universe, Play Card, or any downstream packaging

This part is intentionally:
- winner-conditioned
- truth-first
- predictive-policy-blind
- environment-focused

This part should answer:
- what really happened in the winning environment?
- what kind of pattern structure produced the win?
- what would a strong predictive system have needed to preserve here?

This part should not answer:
- whether the arena hit
- whether Stable/DR/VTRAC/Hot Zones were correct
- whether Candidate Universe or Play Card closed the win
- whether a bounded rule should be promoted

Those belong later.

---

## Part A Inputs

Primary inputs:
- `sharepacks/<D>/<STATE>/winners/<STATE>/*.html`
- `sharepacks/<D>/<STATE>/winners/<STATE>/*.json`

Recommended companion inputs:
- winners digest if present
- results line for the state/day
- canonicalized winner mapping notes if needed

When multiple winner files exist:
- prefer the latest valid stamp per winning result
- record the exact files used
- do not mix multiple duplicate stamps into the narrative unless the duplicates differ materially

Always record:
- results date `D`
- history date `H` if known
- state
- Midday result
- Evening result
- canonical winner form(s)
- VTRAC winner index / indices

---

## Part A Reading Rules

1. Read the winners lens before opening predictive arena artifacts.
2. Treat `Combined` as a lens, not a third outcome stream.
3. Treat cross-variant actualization as real diagnostic information.
4. Treat Pick-3 winners as 3-digit literals first, then canonical / VTRAC forms second.
5. Focus on environment class and progression quality, not only exact winner visibility.
6. End Part A with a predictive requirement statement:
   - “a strong system needed to preserve ___ here.”

---

## Part A Output Shape

Part A should end with:
- one truth-side environment classification
- one or more strongest structural clues
- one statement of what the predictive system needed to preserve
- one clean handoff into later arena/tool review

Recommended answer style:
- short structured paragraphs
- compact bullet lists only where they clarify
- avoid giant raw dumps
- focus on synthesis

---

## A0. File Lock And Truth Inputs

Purpose:
- lock the exact winner-conditioned evidence used for Part A
- prevent later drift across duplicate stamps or alternate lenses

Record:
- results date `D`
- state
- Midday literal + canonical + VTRAC index
- Evening literal + canonical + VTRAC index
- primary winners HTML used
- primary winners JSON used
- any important supporting winners digest / overlay files

Template:

```md
### A0. File Lock And Truth Inputs

- Results date: `...`
- State: `...`
- Midday winner: literal `...` | canonical `...` | VTRAC index `...`
- Evening winner: literal `...` | canonical `...` | VTRAC index `...`
- Primary winners HTML:
  - `...`
  - `...`
- Primary winners JSON:
  - `...`
  - `...`
- Supporting truth artifacts:
  - `...`

Notes:
- duplicate stamps reviewed?: `yes/no`
- chosen latest/primary stamp reason: `...`
```

---

## A1. Winning Pattern Formation

Purpose:
- describe how the winning pattern formed across Midday / Evening / Combined
- establish whether the win formed cleanly, diffusely, or only through a broader family/lane environment

Primary questions:
- where is the exact winner visible?
- where is only the family/lane visible?
- where is the pattern broad, narrow, compressed, or diluted?
- does the win emerge directly, or does it appear through a broader corridor first?

What to look for:
- exact winner tags
- family saturation vs exact narrowing
- column progression
- set-to-set carry
- whether the path tightens late or stays diffuse

Template:

```md
### A1. Winning Pattern Formation

Midday:
- ...

Evening:
- ...

Combined lens:
- ...

Truth-side read:
- The winning pattern formed as `clean exact / family-first / lane-first / cross-variant / mixed`.
- The clearest evidence of formation was `...`.
- The weakest or most diluted part of the formation was `...`.
```

---

## A2. Variant Behavior

Purpose:
- determine which variant carried the clearest winner truth
- classify whether the environment was same-variant, cross-variant, Combined-heavy, or split

Primary questions:
- which variant best expressed the winner?
- did the winner’s own period carry the strongest truth?
- did another variant carry the clearer clue?
- did Combined preserve the environment better than either period alone?

Environment classes to choose from:
- same-variant dominant
- cross-variant bounce
- Combined-heavy
- split / diluted
- noisy mixed environment

Template:

```md
### A2. Variant Behavior

- Clearest variant for Midday winner: `...`
- Clearest variant for Evening winner: `...`
- Combined lens role: `supportive / dominant / weak / misleading`

Variant behavior verdict:
- Environment class: `...`
- Why: `...`

Cross-variant notes:
- ...
```

---

## A3. Winner Structure Class

Purpose:
- classify what kind of structural win this actually was
- move beyond “hit or miss” language into environment type

Choose one primary structure class and optional secondary class:
- direct exact corridor
- family-wide pressure
- VTRAC-lane-first
- doubles-heavy
- survivor/frontier tightening
- hidden/cluttered reveal
- split-state / diluted
- transform / order-sensitive
- mixed structure

Primary questions:
- was the winner mainly a literal narrowing event?
- was it mainly a family/lane environment?
- was it mainly VTRAC-led?
- was it hiding behind clutter?
- was it survivor/frontier based?

Template:

```md
### A3. Winner Structure Class

- Primary structure class: `...`
- Secondary structure class: `...`

Reasoning:
- ...

Most important structural clue:
- ...
```

---

## A4. Progression And Survivor Read

Purpose:
- read the progression quality of the winner environment
- explicitly capture lingering-pattern and survivor behavior

This section is where to look for:
- survivor effects
- last-remaining behavior
- late/frontier tightening
- column pressure shifts
- col2 -> col1 style tightening if present
- repeated late pattern survival
- lingering 3-value or repeat-style persistence

Primary questions:
- did the win look like something that had been lingering?
- was there a last-surviving lane or family?
- did the pattern tighten late?
- did the win form through frontier/currentness behavior rather than early dominance?

Template:

```md
### A4. Progression And Survivor Read

Progression notes:
- ...

Survivor / frontier notes:
- ...

Currentness / tightening notes:
- ...

Part A judgment:
- The winner behaved like `lingering / tightening late / already dominant / hidden-until-late / mixed`.
```

---

## A5. VTRAC Winner Read

Purpose:
- read the winner through the VTRAC truth lens separately from the literal lens
- determine whether the VTRAC corridor was cleaner than the literal corridor

Primary questions:
- was the VTRAC winning pattern clearer than the literal winner?
- did the VTRAC lane show early and stay alive?
- was the win better described as VTRAC-family truth than literal exact truth?
- was the VTRAC environment clean, split, or diluted?

Template:

```md
### A5. VTRAC Winner Read

- Midday VTRAC read: `...`
- Evening VTRAC read: `...`

VTRAC environment verdict:
- Cleaner than literal?: `yes/no/mixed`
- Why: `...`

Key VTRAC clue:
- ...
```

---

## A6. Pre-System Predictive Thesis

Purpose:
- force a truth-first predictive requirement statement
- answer what a strong system would have needed to preserve here even without consulting predictive artifacts

Primary question:
- if you had only the winner-conditioned environment lens and no system outputs, what would you say the predictive system needed to preserve?

Answer in terms like:
- family
- VTRAC lane
- survivor frontier
- hidden reveal
- cross-variant bounce
- direct literal corridor
- double-heavy family

Template:

```md
### A6. Pre-System Predictive Thesis

A strong predictive system needed to preserve:
- ...

It did not necessarily need to isolate immediately:
- ...

The minimum viable “correct read” of this win would have been:
- ...
```

---

## A7. Part A Handoff

Purpose:
- produce the compact truth-side summary that later arena/tool sections will be judged against

This should be short and decisive.

Template:

```md
### A7. Part A Handoff

- Environment class: `...`
- Strongest winner truth: `...`
- Clearest progression clue: `...`
- Clearest VTRAC clue: `...`
- Predictive requirement: `...`
- Main comparison target for later arena review: `...`
```

---

## Part A Analyst Guidance

Good Part A outputs are:
- specific
- truth-side
- structural
- not yet predictive-policy driven

Bad Part A outputs are:
- “Stable missed”
- “CU didn’t have it”
- “Play Card should have covered it”
- “this bounded rule would have fixed it”

Those belong later.

If Part A is done correctly, later sections should be able to ask:
- did the arena preserve this truth?
- which tool preserved it?
- which context source reinforced it?
- was it visible but underweighted?
- was it promoted at all downstream?

That is the exact role of Part A.

---

# Part B — Stable Pattern Extractor

Purpose:
- compare Stable evidence against the Part A truth-side read
- determine what Stable preserved, what it amplified, and what it failed to preserve
- separate Stable’s role as an arena evidence producer from Stable’s role in bounded downstream policy

Stable should be reviewed here as:
- a family/lane preservation tool
- a pattern-compounding tool
- a survivor/frontier tool
- a hidden-family and transformation clue tool

Stable should not be reviewed here mainly as:
- a tiny top-N direct caller
- a standalone oracle that must exactly surface the winner canonical near the very top

The key Part B question is:
- **did Stable preserve the structural truth identified in Part A, and if so, where?**

This section should answer:
- what Stable saw
- which Stable evidence family mattered most
- whether Stable’s strongest contribution was exact, family, VTRAC-adjacent, survivor, hidden, or transform-oriented
- whether any of that Stable truth was already used in bounded policy

This section should not answer:
- final cross-tool ranking
- final arena synthesis
- final context-layer reinforcement
- final downstream blame assignment

Those belong later.

---

## Part B Inputs

Primary predictive-side Stable inputs:
- `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_stable_patterns_scores.csv`
- `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_stable_patterns_compound.csv`
- `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_stable_patterns_families.csv`
- `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_metrics.json`

Primary Stable arena bridge:
- `sharepacks/_predictive/<D>/<STATE>/analysis/stable_arena*.json`
- `sharepacks/_predictive/<D>/<STATE>/analysis/stable_arena*.md`

Truth-side Stable lens when needed:
- `sharepacks/<D>/<STATE>/winners/<STATE>/*winner_family_spotlight_raw.csv`
- `sharepacks/<D>/<STATE>/winners/<STATE>/*winner_family_spotlight_families.csv`
- Stable winners HTML / JSON when available
- winner placement / hit fields in `metrics.json`

Optional comparison-only inputs:
- aggregated arena markdown/json for the same state
- Candidate Universe surfaces that explicitly use Stable:
  - `stable_top`
  - `stable_compound_top`
  - `stable_family_vote`
  - `stable_family_vote_v2`
  - `stable_last_remaining`

Important guardrail:
- use Stable truth-side winners artifacts only for post-results explanation
- do not treat winners-dependent Stable artifacts as predictive inputs

---

## Part B Reading Rules

1. Start from the Part A handoff, not from Stable ranks alone.
2. Read Stable as a preservation-and-structure tool before reading it as a direct caller.
3. Check `stable_arena` before spelunking every raw CSV.
4. Only drill into raw Stable files when the arena artifact leaves something unclear.
5. Separate conclusions into:
   - preserved in Stable evidence
   - amplified in Stable compounding/family surfaces
   - used in bounded policy
   - visible but not yet promoted
   - absent
6. Do not confuse:
   - “winner canonical not top-ranked”
   with
   - “Stable did not preserve the winner corridor”

---

## Part B Output Shape

Part B should end with:
- one Stable truth-alignment judgment
- one strongest Stable evidence family
- one strongest unused Stable insight if present
- one statement about whether existing Stable bounded policies already used the most important truth

Recommended answer style:
- synthesis first
- then evidence family notes
- then bounded policy relationship
- avoid long raw field inventories unless a specific field is central to the case

---

## B0. Stable File Lock And Review Surface

Purpose:
- lock the exact Stable artifacts used in the review
- prevent drift between raw Stable files, Stable arena slices, and truth-side spotlight files

Template:

```md
### B0. Stable File Lock And Review Surface

- Stable predictive scores: `...`
- Stable predictive compound: `...`
- Stable predictive families: `...`
- Stable metrics: `...`
- Stable arena artifact: `...`
- Stable truth-side spotlight / winners files used:
  - `...`
  - `...`

Notes:
- Stable arena version / profile: `...`
- Any missing Stable artifact?: `yes/no`
- If something is missing, is this a pipeline issue or just a performance issue?: `...`
```

---

## B1. Stable Truth Alignment Summary

Purpose:
- answer immediately whether Stable preserved the Part A truth
- stop the section from drifting into raw CSV inspection too early

Primary questions:
- did Stable preserve the winner’s exact corridor?
- did Stable preserve the winner family/lane?
- did Stable preserve the winner only indirectly through compounding, survivor, hidden, or transform evidence?
- what is the cleanest way to describe Stable’s relationship to the Part A truth?

Use labels like:
- exact-preserved
- family/lane-preserved
- VTRAC-adjacent-preserved
- survivor/frontier-preserved
- hidden/transform-preserved
- weakly preserved
- absent

Template:

```md
### B1. Stable Truth Alignment Summary

Part A target:
- `...`

Stable alignment verdict:
- Exact corridor: `strong / moderate / weak / absent`
- Family/lane preservation: `strong / moderate / weak / absent`
- Advanced evidence preservation (survivor/hidden/transform): `strong / moderate / weak / absent`

Best one-sentence Stable read:
- `...`

Most important Stable contribution to the Part A truth:
- `...`
```

---

## B2. Row-Level Pattern Evidence

Purpose:
- inspect the most granular Stable evidence only after the truth-alignment summary is set
- identify which row-level score parts, flags, locations, and why-tags actually mattered

Primary surfaces:
- `top_row_patterns`
- row-level `score_breakdown`
- row-level `flags`
- modal order / permutation clues
- set / draw / column location

Primary questions:
- which row-level patterns best aligned with the Part A truth?
- which score parts mattered most?
- which flags mattered most?
- did the winner corridor appear as literal rows, family-adjacent rows, or transform-adjacent rows?
- was the evidence same-variant, cross-variant, or Combined-heavy?

Helpful score-part families to mention only when they matter:
- `score_repeat`
- `score_hidden`
- `score_vtrac_straight`
- `score_persistence_set`
- `score_persistence_draw`
- `score_double_mirror`

Helpful flags to mention only when they matter:
- `single_left`
- `hidden3v`
- `double_mirror`
- straight-style flags
- consensus flags

Template:

```md
### B2. Row-Level Pattern Evidence

Most relevant Stable row patterns:
- `...`
- `...`

Most relevant score parts:
- `...`

Most relevant row flags / structural tags:
- `...`

Location/currentness read:
- `...`

Row-level judgment:
- Stable row evidence was `direct / family-adjacent / transform-adjacent / noisy / mixed`.
```

---

## B3. Compound And Pattern Ledger Read

Purpose:
- determine what became visible only once Stable evidence was compounded
- identify whether Stable’s true value in this case was broader than raw top rows

Primary surfaces:
- `top_compound_patterns`
- `pattern_ledgers_top`
- `compound_context`
- `frontier_summary`
- `score_breakdown_sums`
- `top_box_contributions`

Primary questions:
- what did compounding reveal that raw row review alone would have missed?
- did the winner corridor strengthen meaningfully in compound or ledger surfaces?
- was this a case of:
  - raw literal weak but compound strong
  - family stronger than literal
  - frontier/currentness stronger than rank alone
  - VTRAC-adjacent compounding

Key Stable compound concepts worth checking:
- chain depth
- breadth of support
- `funnel_precol1`
- `vt_only_lane`
- hot counts
- `col1_hits`
- `hidden3v_hits`
- `vtrac_straight_hits`
- `double_mirror_hits`

Template:

```md
### B3. Compound And Pattern Ledger Read

Compound verdict:
- `...`

Most important compounded canonical or corridor:
- `...`

Most important ledger insight:
- `...`

Did compounding reveal more truth than raw row ranks?:
- `yes/no/mixed`

Why:
- `...`
```

---

## B4. Family And Lane Preservation Read

Purpose:
- treat family/lane preservation as the central Stable question
- evaluate whether this was one of the classic cases where Stable knew the family better than the literal

Primary surfaces:
- `family_rollups_top`
- top canonicals within family
- family score totals/max
- progression counts
- survivor counts
- hidden/transform summaries inside family rollups

Primary questions:
- did Stable preserve the winning family/lane strongly?
- was this a “family right, literal weak” case?
- was the winning family present but underweighted?
- was the family clean, split, or diluted?

This is the section where bounded policy relationship starts to matter, but only lightly.

Template:

```md
### B4. Family And Lane Preservation Read

Winning family/lane preservation:
- `...`

Strongest Stable family object:
- `...`

Did Stable know the family better than the literal?:
- `yes/no/mixed`

Family/lane judgment:
- `...`
```

---

## B5. Survivor, Frontier, Hidden, And Transform Read

Purpose:
- capture the advanced Stable evidence classes without scattering them across the section
- give a deliberate place for lingering-pattern and survivor logic

Primary surfaces:
- `survivor_frontiers`
- `last_remaining` / survivor counts
- `hidden_family_reveal`
- `hidden_family_reveal_summary`
- `order_transform_hints`
- `order_transform_summary`
- VT-straight style clues when they are structurally important

Primary questions:
- was this a survivor/frontier case?
- was hidden-family reveal important?
- were transform or modal-order clues important?
- did Stable preserve something subtle here that is visible but not yet strongly promoted?

Template:

```md
### B5. Survivor, Frontier, Hidden, And Transform Read

Survivor/frontier read:
- `...`

Hidden/clutter-reveal read:
- `...`

Order/transform / VT-straight read:
- `...`

Advanced Stable evidence verdict:
- The strongest advanced Stable clue in this case was `...`.
```

---

## B6. Stable Policy Relationship

Purpose:
- explicitly separate Stable evidence from existing Stable bounded conversion policies
- prevent later confusion about what the system already uses vs what it only preserves

Primary policy surfaces:
- `stable_top`
- `stable_compound_top`
- `stable_family_vote`
- `stable_family_vote_v2`
- `stable_last_remaining`

Primary questions:
- did an existing bounded Stable policy already use the most important truth from this case?
- if yes, did it preserve only the lane, or did it also materially improve closure?
- if no, which Stable evidence remained visible but unpromoted?

Helpful conclusion buckets:
- already used well
- partially used
- preserved but unused
- visible but not yet promotable

Template:

```md
### B6. Stable Policy Relationship

Already-used Stable bounded surfaces relevant here:
- `...`

What those surfaces captured:
- `...`

What Stable preserved but current bounded policy still did not fully use:
- `...`

Policy relationship verdict:
- `already used well / partially used / preserved but unused / visible but not yet promotable`
```

---

## B7. Stable Handoff

Purpose:
- close Part B with the shortest possible Stable-specific learning statement for later sections

Template:

```md
### B7. Stable Handoff

- Strongest Stable truth: `...`
- Strongest Stable evidence family: `row / compound / family / survivor / hidden / transform`
- Strongest unused Stable insight: `...`
- Most relevant current Stable policy surface: `...`
- Stable-specific limitation in this case: `...`
- Main comparison target for Part C or later arena synthesis: `...`
```

---

## Part B Analyst Guidance

Good Part B outputs:
- compare Stable directly against Part A truth
- identify which Stable evidence family mattered most
- separate preserved evidence from bounded policy usage
- note what is visible but not yet promoted

Bad Part B outputs:
- “winner not top-ranked so Stable failed”
- “Stable top list missed so nothing was there”
- “all interesting Stable features should become policy immediately”
- “one strong field means analyzer retuning now”

Correct Part B posture:
- preserve first
- understand second
- promote only after repeated proof

That is especially important for:
- survivor/frontier signals
- hidden-family reveal
- order/transform hints
- VT-straight clues

These are often powerful as evidence before they are ready as policy.

---

---

# Part C — Digit Reduction

Purpose:
- compare Digit Reduction evidence against the Part A truth-side read
- determine whether DR exposed the winning structure as a residue, corridor, lane, VTRAC cluster, or bounded assigned-box environment
- explicitly evaluate extractability, currentness, and structural compactness instead of reducing DR to “top candidates hit or miss”

DR should be reviewed here as:
- a long-string reduction tool
- a residue and reveal tool
- a corridor and lane exposure tool
- a structural clustering tool
- a fourth-variable / extra-digit pressure tool
- a bounded extractability tool

DR should not be reviewed here mainly as:
- a tiny top-K straight caller
- a literal-only top-candidate oracle
- a tool that “failed” simply because the winner did not sit at the top of one short list

The key Part C question is:
- **did DR expose the winner-side structure in a way that was extractable, current, and small enough to matter operationally?**

This section should answer:
- what DR exposed before and after reduction
- whether the winner was structurally visible as a residue, corridor, family neighborhood, or VTRAC cluster
- whether the winning cluster was extractable from a small assigned-box environment
- whether currentness / progression across boxes materially supported the win
- whether DR truth was visible but compressed, underweighted, or unconsumed

This section should not answer:
- final cross-tool synthesis
- final arena scoring
- final budget or packaging decisions
- broad analyzer-tuning decisions

Those belong later.

---

## Part C Inputs

Primary predictive-side DR inputs:
- `sharepacks/_predictive/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_per_item.csv`
- `sharepacks/_predictive/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_top_candidates.csv`
- `sharepacks/_predictive/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_meta.json`
- `sharepacks/_predictive/<D>/<STATE>/digit_reduction/<STATE>/*digit_reduction*_report*.html`
- `sharepacks/_predictive/<D>/<STATE>/digit_reduction/<STATE>/*digit_reduction*_scores.csv`

Primary DR arena bridge:
- `sharepacks/_predictive/<D>/<STATE>/analysis/dr_arena*.json`
- `sharepacks/_predictive/<D>/<STATE>/analysis/dr_arena*.md`

Truth-side DR lens when needed:
- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/winners/*_winner_stamp.json`
- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/winners/*_winner_flags.csv`
- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/winners/*_winner_hits.csv`
- winners overlays and winners HTML/JSON that help explain the DR environment

Important DR arena surfaces to prioritize:
- `Trace Strength`
- `Lane Only`
- `Competing Literal Pressure`
- `Double Pressure`
- `Row Repeat / Final Survival`
- `Fourth Variable`
- `dr_empty_lens`
- `dr_corridor_strength`
- `corridor_scope`
- `corridor_band`
- `pre_reduction_cluster_strength`
- `reveal_purity`
- `early_activation_strength`
- `neighbor_box_support`
- `consecutive_box_progression`
- `family_neighborhood_saturation`
- `family_asymmetry_inside_corridor`
- `core_vs_clutter_transit_score`

Guardrail:
- winner-aware DR artifacts are explanation and validation tools
- they are not predictive inputs

---

## Part C Reading Rules

1. Start from the Part A handoff, not from DR top candidates.
2. Read DR first as a structural exposure tool, not a direct caller.
3. Check `dr_arena` before drilling into every raw DR file.
4. Separate:
   - pre-reduction structural presence
   - post-reduction reveal quality
   - corridor / lane extractability
   - currentness / progression
   - consumption / compression gaps
5. Explicitly ask whether the win was extractable from a small assigned-box environment.
6. Explicitly ask whether currentness / movement toward recent boxes made the win more actionable.
7. Do not confuse:
   - “winner not in top candidates”
   with
   - “DR did not expose the winning structure”

---

## Part C Output Shape

Part C should end with:
- one DR truth-alignment judgment
- one extractability judgment
- one currentness/progression judgment
- one statement on whether DR truth was:
  - used
  - compressed too early
  - visible but unconsumed
  - or absent

Recommended answer style:
- synthesis first
- then structural exposure
- then extractability/currentness
- then consumer relationship

---

## C0. DR File Lock And Review Surface

Purpose:
- lock the exact DR artifacts used in the review
- prevent drift between raw DR files, DR arena slices, and winner-aware overlays

Template:

```md
### C0. DR File Lock And Review Surface

- DR per_item: `...`
- DR top_candidates: `...`
- DR meta: `...`
- DR report / scores: `...`
- DR arena artifact: `...`
- DR winner-aware files used:
  - `...`
  - `...`

Notes:
- DR arena version / profile: `...`
- Any missing DR artifact?: `yes/no`
- If something is missing, is this a pipeline issue or just a performance issue?: `...`
```

---

## C1. DR Truth Alignment Summary

Purpose:
- answer immediately whether DR exposed the Part A truth in any meaningful way
- stop the section from drifting into raw top-candidate ranking too early

Primary questions:
- did DR expose the winner structure at all?
- was the exposure:
  - residue-level
  - corridor-level
  - lane-level
  - VTRAC-cluster-level
  - reveal-only
  - or absent?
- was DR’s best contribution exact, family, VTRAC, repeat-survival, or extra-variable oriented?

Helpful verdict buckets:
- residue-preserved
- corridor-preserved
- lane-preserved
- VTRAC-cluster-preserved
- reveal-only
- clutter-drowned
- absent

Template:

```md
### C1. DR Truth Alignment Summary

Part A target:
- `...`

DR alignment verdict:
- Residue / reveal: `strong / moderate / weak / absent`
- Corridor / lane exposure: `strong / moderate / weak / absent`
- VTRAC-cluster exposure: `strong / moderate / weak / absent`
- Extractability quality: `strong / moderate / weak / absent`

Best one-sentence DR read:
- `...`

Most important DR contribution to the Part A truth:
- `...`
```

---

## C2. Pre-Reduction And Trace Read

Purpose:
- determine what DR knew before reduction cleaned anything up
- capture the broad structural pressure that existed in the long strings

Primary surfaces:
- `Trace Strength`
- `pre_reduction_cluster_strength`
- early activation
- family neighborhood saturation
- raw exposure counts

Primary questions:
- what families / clusters were already alive before reduction?
- did the winning corridor already appear structurally before the cleaner reveal?
- was the winner-side pressure broad, repeated, and meaningful, or thin and incidental?

Template:

```md
### C2. Pre-Reduction And Trace Read

Strongest pre-reduction clusters:
- `...`

Did the winner-side structure already exist before reduction?:
- `yes/no/mixed`

Most important trace-side clue:
- `...`

Pre-reduction judgment:
- `...`
```

---

## C3. Reduction Reveal And Empty-Lens Read

Purpose:
- determine whether reduction actually clarified the winner structure
- explicitly distinguish true emptiness from misleading low-trust sparsity

Primary surfaces:
- `dr_empty_lens`
- `reveal_purity`
- `core_vs_clutter_transit_score`
- raw exposure vs path summary counts
- reduction reveal objects and purity-style clues

Primary questions:
- did reduction clarify something real?
- did the case become cleaner after reduction?
- was the apparent miss really a `true_empty`, an `active_low_trust`, or a `positive_trace`?
- did the winner structure sit behind clutter that DR partially removed but not enough?

Template:

```md
### C3. Reduction Reveal And Empty-Lens Read

Reduction reveal verdict:
- `...`

Empty-lens classification:
- `true_empty / active_low_trust / positive_trace / mixed`

Did reduction improve winner-side visibility?:
- `yes/no/mixed`

Why:
- `...`
```

---

## C4. Assigned-Box Corridor And VTRAC Cluster Isolation Read

Purpose:
- deliberately evaluate whether the winner was extractable from a small assigned-box environment
- bring explicit attention to bounded, actionable DR isolation rather than diffuse descriptive truth

Primary surfaces:
- `dr_corridor_strength`
- `corridor_scope`
- `corridor_band`
- assigned-box / family-neighborhood exposure
- `Lane Only`
- assigned-box VTRAC strength / corridor semantics when present

Primary questions:
- was the winner or winner-family extractable from a small group of assigned boxes?
- how many boxes were really carrying the live cluster?
- was the extractable object:
  - exact corridor
  - family neighborhood
  - compact double corridor
  - VTRAC corridor
- was the VTRAC-winning cluster visible repeatedly inside those boxes?
- if the cluster was visible, what stopped better isolation?

This is one of the most important Part C sections because it connects DR review to:
- cost efficiency
- practical extractability
- state ranking value
- profitability

Template:

```md
### C4. Assigned-Box Corridor And VTRAC Cluster Isolation Read

Assigned-box extractability:
- `...`

Small-box isolation quality:
- `tight / moderate / diffuse / absent`

VTRAC-cluster isolation quality:
- `strong / moderate / weak / absent`

Most important assigned-box / corridor insight:
- `...`

If visible but not isolated well, why not?:
- `extraction / weighting / compression / promotion / clutter / mixed`
```

---

## C5. Currentness, Progression, And Box-Mapping Read

Purpose:
- evaluate whether the winner cluster was progressing toward more recent / current boxes
- determine whether DR is valuing currentness and box progression appropriately in this case

Primary surfaces:
- `corridor_band`
- `early_activation_strength`
- `neighbor_box_support`
- `consecutive_box_progression`
- `family_neighborhood_saturation`
- `family_asymmetry_inside_corridor`
- current-endpoint or near-column-1 style box progression clues

Primary questions:
- was the winning cluster moving toward more recent boxes?
- was the corridor becoming more current and tighter?
- did the box mapping imply increasing extractability?
- does this case suggest currentness should matter more strongly?

Template:

```md
### C5. Currentness, Progression, And Box-Mapping Read

Currentness / progression read:
- `...`

Did the winner cluster move toward a more current box region?:
- `yes/no/mixed`

Was that progression actionable?:
- `yes/no/mixed`

Most important progression clue:
- `...`
```

---

## C6. Repeat, Survival, Double, And Fourth-Variable Read

Purpose:
- capture the classic DR-native structural truths that are often easy to underrate
- explicitly evaluate lingering repeat regimes and bounded closure pressure

Primary surfaces:
- `Row Repeat / Final Survival`
- `Double Pressure`
- `Fourth Variable`
- repeat rows / final survival
- extra-variable support and duplication depth

Primary questions:
- did DR expose the win as a repeat-survival case?
- did double pressure materially support the winner-side structure?
- was there a real fourth-variable / extra-digit closure problem?
- was this a bounded closure opportunity rather than a total absence problem?

Template:

```md
### C6. Repeat, Survival, Double, And Fourth-Variable Read

Repeat / survival read:
- `...`

Double-pressure read:
- `...`

Fourth-variable / extra-digit read:
- `...`

Most important DR-native structural clue:
- `...`
```

---

## C7. DR Consumer And Policy Relationship

Purpose:
- explicitly separate what DR preserved from what current consumers did with it
- ask whether the issue was extraction, scoring, compression, or consumption

Primary questions:
- was DR truth already visible but compressed too early?
- was it visible in arena surfaces but not used by current downstream logic?
- was this a consumer problem more than a DR extraction problem?

Helpful conclusion buckets:
- already used well
- partially used
- visible but compressed
- visible but unconsumed
- not yet promotable
- absent

Template:

```md
### C7. DR Consumer And Policy Relationship

What DR clearly preserved:
- `...`

What current consumers actually used:
- `...`

Main failure point if the win was not closed:
- `extraction / scoring / compression / consumption / mixed`

Policy relationship verdict:
- `already used well / partially used / visible but compressed / visible but unconsumed / not yet promotable / absent`
```

---

## C8. DR Handoff

Purpose:
- close Part C with the shortest possible DR-specific learning statement for later sections

Template:

```md
### C8. DR Handoff

- Strongest DR truth: `...`
- Strongest DR evidence family: `trace / reveal / corridor / VTRAC cluster / progression / repeat / fourth variable`
- Strongest extractability insight: `...`
- Strongest unused DR insight: `...`
- DR-specific limitation in this case: `...`
- Main comparison target for Part D or later arena synthesis: `...`
```

---

## Part C Analyst Guidance

Good Part C outputs:
- compare DR directly against Part A truth
- evaluate extractability, not just visibility
- explicitly assess currentness and box progression
- separate preserved DR truth from consumed DR truth
- identify whether the real issue was extraction, compression, or downstream use

Bad Part C outputs:
- “winner not top-ranked so DR failed”
- “DR top candidates missed so there was no signal”
- “every DR corridor should immediately become a policy rule”
- “one interesting box cluster means retune the analyzer now”

Correct Part C posture:
- expose first
- judge extractability second
- judge consumer relationship third
- promote only after repeated proof

This is especially important for:
- assigned-box VTRAC cluster isolation
- currentness / progression valuation
- repeat-survival classes
- bounded fourth-variable closure pressure

These are often where DR’s real value lives.

---

## Part D — VTRAC Analyzer

Purpose:
- compare VTRAC evidence against the Part A truth-side read
- determine whether VTRAC preserved the correct winner lane, same-index neighborhood, and section-led environment
- explicitly separate lane correctness from tiny straight-caller expectations

VTRAC should be reviewed here as:
- a lane / index evidence tool
- a straight-neighborhood witness tool
- a cross-section corroboration tool
- a right-column / stable-column context tool
- a mask-drop, mirror, and double-support clue tool

VTRAC should not be reviewed here mainly as:
- a tiny top-k direct straight caller
- a standalone exact-winner oracle
- a substitute for later cross-tool aggregation

The key Part D question is:
- **did VTRAC preserve the correct winner lane environment clearly enough that later aggregation should have been able to use it?**

This section should answer:
- whether the winner lane / index was present and how strongly
- whether the same-index straight neighborhood was clean, asymmetric, or noisy
- whether the lane was section-led, broadly shared, or weakly corroborated
- whether right-column, hot/superhot, consensus, mask-drop, mirror, or double descriptors materially strengthened the lane
- whether the remaining problem was tool extraction, arena preservation, or downstream compression

This section should not answer:
- final cross-tool synthesis
- final arena ranking
- final budget or packaging decisions
- broad VTRAC scorer retunes

Those belong later.

---

## Part D Inputs

Primary predictive-side VTRAC inputs:
- `sharepacks/_predictive/<D>/<STATE>/vtrac/<STATE>/<STATE>_vtrac_enhanced_*.json`

Primary global compact layer:
- `sharepacks/<D>/vtrac_compact_report.json`
- `sharepacks/<D>/vtrac_compact_report.csv`

Helpful review-side companions when needed:
- `scripts/tools/vtrac_sharepack_summary.py`
- `scripts/tools/validate_vtrac_compact_report.py`
- VTRAC validation / winners review summaries if present

Truth-side VTRAC lens when needed:
- winners HTML / analyzer-style winners overlays
- winners JSON / winner placement diagnostics
- winner-layer families such as:
  - `pattern_occurrence`
  - `pattern_persistence`
  - `pattern_stability`
  - `straight_counts`

Important VTRAC arena-facing evidence families to prioritize:
- `indices_ranked`
- `straights_ranked`
- `top_straights`
- `section_summaries`
- `top_indices_by_state` from the compact layer
- compact descriptor families such as:
  - `overlap`
  - `stable_cols_count`
  - `stable_cols`
  - `consensus_col1`
  - `consensus_col2`
  - `cross_section_echo`
  - `hot_count`
  - `superhot_count`
  - `mask_drop`
  - `mirror_supported`
  - `double_hits`
  - `confidence_score`
  - `tier`
  - `flags`
  - `top_tokens`
  - `recommended_tokens`
  - `section_prior`
  - `state_prior`
  - `why`

Important note:
- VTRAC does **not** currently have a standalone `vtrac_arena*.json`
- so Part D should read the enhanced bundle and compact report as the primary VTRAC review surfaces, then compare that against the later aggregated arena if needed

Telemetry note:
- `telemetry` is audit/provenance context, not first-order winner evidence
- treat it as:
  - configuration context
  - reproducibility context
  - mask / weight context
- do not treat it as a direct predictive signal family

Guardrail:
- winners-aware VTRAC artifacts remain review and confirmation tools
- they are not predictive inputs

---

## Part D Reading Rules

1. Start from the Part A handoff, not from `top_straights`.
2. Read VTRAC first as a lane / neighborhood lens, not as a direct straight oracle.
3. Check the enhanced JSON and compact report before jumping to downstream helpers.
4. Separate:
   - lane correctness
   - same-index neighborhood quality
   - section-led corroboration
   - descriptor-backed currentness
   - consumer / compression gaps
5. Explicitly ask whether the winner lane was clearer than the literal straight surface.
6. Explicitly ask whether the same-index neighborhood was:
   - clean
   - shoulder-heavy
   - split
   - or noisy
7. Do not confuse:
   - “winner straight not near the top”
   with
   - “VTRAC did not preserve the winner lane truth”
8. Treat telemetry as audit context only unless configuration/provenance itself explains an anomaly.

---

## Part D Output Shape

Part D should end with:
- one VTRAC truth-alignment judgment
- one lane-dominance / neighborhood-quality judgment
- one section/currentness judgment
- one statement on whether VTRAC truth was:
  - already used
  - partially used
  - compressed too early
  - visible but unconsumed
  - or absent

Recommended answer style:
- lane truth first
- neighborhood shape second
- descriptor context third
- consumer relationship fourth

---

## D0. VTRAC File Lock And Review Surface

Purpose:
- lock the exact VTRAC artifacts used in the review
- prevent drift between state enhanced bundles, global compact feeds, and winner-aware review artifacts

Template:

```md
### D0. VTRAC File Lock And Review Surface

- VTRAC enhanced bundle: `...`
- VTRAC compact report JSON: `...`
- VTRAC compact report CSV: `...`
- VTRAC winners / validation files used:
  - `...`
  - `...`
- Any companion VTRAC summary / validator output used:
  - `...`

Notes:
- Standalone `vtrac_arena` artifact available?: `yes/no`
- If no, primary review surface used: `enhanced bundle / compact report / both`
- Any missing VTRAC artifact?: `yes/no`
- If something is missing, is this a pipeline issue or just a review-surface issue?: `...`
```

---

## D1. VTRAC Truth Alignment Summary

Purpose:
- answer immediately whether VTRAC preserved the Part A truth in a meaningful way
- stop the section from collapsing too early into straight-only ranking language

Primary questions:
- did VTRAC preserve the winner lane / index?
- did it preserve the same-index neighborhood?
- was the lane truth stronger than the literal straight truth?
- was the environment section-led, broadly corroborated, or only faintly present?

Helpful verdict buckets:
- lane_correct_literal_mixed
- lane_correct_neighbor_strong
- lane_correct_but_noisy
- lane_soft_but_present
- literal_visible_without_lane_strength
- absent

Template:

```md
### D1. VTRAC Truth Alignment Summary

Part A target:
- `...`

VTRAC alignment verdict:
- Winner lane / index: `strong / moderate / weak / absent`
- Same-index neighborhood: `strong / moderate / weak / absent`
- Straight-level witness quality: `strong / moderate / weak / absent`
- Section corroboration: `strong / moderate / weak / absent`

Best one-sentence VTRAC read:
- `...`

Most important VTRAC contribution to the Part A truth:
- `...`
```

---

## D2. Ranked Lane / Index Read

Purpose:
- evaluate where the winner lane ranked and how dominant it actually was
- determine whether VTRAC was speaking clearly or only softly

Primary surfaces:
- `indices_ranked`
- lane score gaps
- compact `top_indices_by_state`
- compact `confidence_score`
- compact `tier` and `flags`

Primary questions:
- where did the winner lane rank?
- how far behind or ahead was it?
- was one lane truly dominant, or was the board flat?
- was the lane truth stronger in the enhanced bundle, the compact layer, or both?

Template:

```md
### D2. Ranked Lane / Index Read

Winner lane rank / presence:
- `...`

Lane dominance read:
- `dominant / near-front / present-but-soft / buried / absent`

Compact-layer corroboration:
- `...`

Most important lane-strength clue:
- `...`
```

---

## D3. Same-Index Straight-Neighborhood Read

Purpose:
- inspect the internal shape of the winner lane rather than only its top straight
- explicitly preserve same-index neighborhood structure and asymmetry

Primary surfaces:
- `straights_ranked`
- `top_straights`
- `indices_ranked[].straights`
- winner-side same-index shoulders from the truth layer when needed

Primary questions:
- was the winner central inside the lane or only one shoulder?
- which same-index straights dominated the lane?
- was the neighborhood clean, asymmetric, split, or noisy?
- was the winner visible as a neighborhood member even if not the lead witness?

This is one of the most important Part D sections because VTRAC often knows more at the lane-neighborhood level than the literal top-straight surface suggests.

Template:

```md
### D3. Same-Index Straight-Neighborhood Read

Neighborhood shape:
- `clean / asymmetric / shoulder-heavy / split / noisy`

Winner position inside the lane:
- `central / strong shoulder / weak shoulder / buried / absent`

Most important same-index witnesses:
- `...`

Most important neighborhood insight:
- `...`
```

---

## D4. Section And Cross-Variant Lead Read

Purpose:
- determine whether the lane was Midday-led, Evening-led, Combined-led, or broadly shared
- evaluate how strongly VTRAC corroborated the winner lane across sections

Primary surfaces:
- `section_summaries`
- `ring_votes`
- `cross_section_echo`
- `section_prior`
- `state_prior`

Primary questions:
- which section carried the clearest lane truth?
- was the lane shared across sections or concentrated in one?
- was the environment Combined-supported, same-section dominant, or cross-section echoing?
- does this case look like a timing/currentness clue more than a literal-caller clue?

Template:

```md
### D4. Section And Cross-Variant Lead Read

Section-lead profile:
- `Midday-led / Evening-led / Combined-led / broadly shared / mixed`

Cross-section echo quality:
- `strong / moderate / weak / absent`

Most important section-based clue:
- `...`

Section / variant verdict:
- `...`
```

---

## D5. Right-Column, Stable-Column, And Hot Context Read

Purpose:
- evaluate descriptor-backed currentness and support behind the lane
- determine whether right-column stability, consensus rescue, and hot/superhot pressure materially strengthened the lane

Primary surfaces:
- `stable_columns`
- `stable_cols_count`
- `consensus_col1`
- `consensus_col2`
- `hot_count`
- `superhot_count`
- `top_box_signatures`

Primary questions:
- was the lane current or merely present?
- did right-column / stable-column behavior make the lane more trustworthy?
- was there frontier/pre-frontier consensus rescue?
- did hot/superhot pressure materially strengthen the lane?

Template:

```md
### D5. Right-Column, Stable-Column, And Hot Context Read

Currentness / stability read:
- `...`

Right-column / stable-column support:
- `strong / moderate / weak / absent`

Hot / superhot reinforcement:
- `strong / moderate / weak / absent`

Most important descriptor-backed clue:
- `...`
```

---

## D6. Mask-Drop, Mirror, And Double Support Read

Purpose:
- capture the structural support clues that often explain why a lane is persuasive even before literal closure is clean
- distinguish hidden-lane reveal from ordinary lane presence

Primary surfaces:
- `mask_drop`
- `mask_drop_count`
- `mirror_supported`
- `double_hits`
- `telemetry.mask_digits`

Primary questions:
- was the lane partly hidden and then revealed?
- did mask-drop meaningfully help explain the lane?
- did mirror or double support materially strengthen the lane?
- was this a structurally persuasive lane even if literal witnesses stayed mixed?

Template:

```md
### D6. Mask-Drop, Mirror, And Double Support Read

Mask-drop read:
- `...`

Mirror support read:
- `...`

Double support read:
- `...`

Most important structural support clue:
- `...`
```

---

## D7. VTRAC Consumer And Policy Relationship

Purpose:
- explicitly separate the full VTRAC evidence from the bounded helper surfaces currently used downstream
- ask whether the remaining problem was VTRAC-local, arena-level, or downstream-level

Primary bounded helpers to compare against:
- `vtrac_top_straights`
- `signals_bundle.vtrac_enhanced.top_indices`
- `signals_bundle.vtrac_enhanced.top_straights`

Primary questions:
- what did the full VTRAC evidence preserve that bounded helpers did not?
- was the lane truth visible but compressed too early into top-straight language?
- is the remaining issue better described as:
  - tool extraction
  - arena preservation
  - downstream compression / consumption
  - or no-action

Helpful conclusion buckets:
- already used well
- partially used
- visible but compressed
- visible but unconsumed
- not yet promotable
- absent

Template:

```md
### D7. VTRAC Consumer And Policy Relationship

What VTRAC clearly preserved:
- `...`

What current bounded consumers actually used:
- `...`

Main failure point if the win was not closed:
- `tool extraction / arena preservation / downstream compression / no_action / mixed`

Policy relationship verdict:
- `already used well / partially used / visible but compressed / visible but unconsumed / not yet promotable / absent`
```

---

## D8. VTRAC Handoff

Purpose:
- close Part D with the shortest possible VTRAC-specific learning statement for later sections

Template:

```md
### D8. VTRAC Handoff

- Strongest VTRAC truth: `...`
- Strongest VTRAC evidence family: `lane rank / neighborhood shape / section lead / stable-column context / mask-drop / mirror-double support`
- Strongest unused VTRAC insight: `...`
- VTRAC-specific limitation in this case: `...`
- Main comparison target for Part E or later arena synthesis: `...`
```

---

## Part D Analyst Guidance

Good Part D outputs:
- judge lane correctness before literal witness ranking
- preserve same-index neighborhood structure, not just lane presence
- explicitly assess section-led vs broadly shared lane behavior
- use compact descriptors to explain why a lane was persuasive
- separate VTRAC evidence from VTRAC bounded helpers

Bad Part D outputs:
- “winner straight was not top-3 so VTRAC failed”
- “lane alive means everything inside the lane is equally strong”
- “mask-drop or mirror support automatically implies promotion”
- “telemetry is a winner-facing evidence family”

Correct Part D posture:
- lane truth first
- neighborhood quality second
- descriptor-backed currentness third
- consumer/compression relationship fourth
- promotion only after repeated proof

This is especially important for:
- same-index neighborhood asymmetry
- section-led vs state-led lane pressure
- right-column / stable-column reinforcement
- mask-drop / mirror / double support

These are often where VTRAC's real value lives.

---

## Part E — Hot Zones

Purpose:
- compare Hot Zones evidence against the Part A truth-side read
- determine whether Hot Zones preserved the winner-side pressure environment, survivorship pattern, and funnel/currentness shape
- explicitly separate pressure truth from tiny top-triad expectations

Hot Zones should be reviewed here as:
- a late-tail pressure extractor
- a vertical-support / survivorship extractor
- a col1 / pre-col1 funnel extractor
- a lane / index corroboration tool
- a hot / superhot pressure lens

Hot Zones should not be reviewed here mainly as:
- a tiny top-k direct straight caller
- a standalone exact-winner oracle
- a replacement for later cross-tool aggregation

The key Part E question is:
- **did Hot Zones preserve where pressure was surviving and tightening around the winner corridor clearly enough that later aggregation should have been able to use it?**

This section should answer:
- whether the winner-side pressure was materially present
- whether that pressure lived in late tails, vertical support, Set1 currentness, or col1 / pre-col1 funneling
- whether the truth was stronger as a VT lane than as a literal triad
- whether concrete counts, spans, and evidence tags made the row stronger than raw rank alone suggests
- whether the remaining problem was tool extraction, arena preservation, or downstream narrowing to bounded triad helpers

This section should not answer:
- final cross-tool synthesis
- final arena ranking
- final budget or packaging decisions
- broad Hot Zones weight or guard retunes

Those belong later.

---

## Part E Inputs

Primary predictive-side Hot Zones inputs:
- `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<STATE>_hot_zones_top_lanes.csv`
- `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<STATE>_hot_zones_meta.json`

Secondary deep-drill predictive layer:
- `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<STATE>_hot_zones_per_lane.csv`

Transitional compatibility layer:
- `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<D>_hot_zones_winner_map.json`

Helpful review-side companions when needed:
- `scripts/tools/hot_zones_sharepack_summary.py`
- Hot Zones winner summaries
- post-results placement summaries
- winner-map hit diagnostics

Important Hot Zones arena-facing evidence families to prioritize:
- `support_count`
- `hot_hits`
- `superhot_hits`
- `vertical_hits`
- `set1_hits`
- `col1_hits`
- `precol1_hits`
- `vt_straight_hits`
- `vt_only_lane_hits`
- `guard_hits`
- `literal_hits`
- `variant_span`
- `set_span`
- `column_span`
- `score_mean`
- `score_max`
- `evidence_tags`

Important deep-drill location/context families when needed:
- `section`
- `set_name`
- `draw_name`
- `column_index`
- `vertical_support`
- `horizontal_span`
- `variant_echo`
- `has_straight`
- `has_vt_straight`
- `vt_only_lane`
- `col1_arrival`
- `precol1_funnel`
- `is_superhot_slot`
- `is_set1`
- `guard_injected`
- `reasons`

Important note:
- Hot Zones does **not** currently have a standalone `hot_zones_arena*.json`
- so Part E should read `top_lanes.csv + meta.json` as the primary Hot Zones review surface, with `per_lane.csv` available for deep-drill confirmation

Guardrail:
- winner-aware Hot Zones artifacts remain review and confirmation tools
- they are not predictive inputs

---

## Part E Reading Rules

1. Start from the Part A handoff, not from raw top-triad rank.
2. Read Hot Zones first as a pressure / survivorship / funnel tool, not as a direct caller.
3. Check `top_lanes.csv + meta.json` before dropping into the full `per_lane.csv`.
4. Separate:
   - pressure presence
   - survivorship / vertical support
   - funnel/currentness
   - VT-only corroboration
   - consumer / compression gaps
5. Explicitly ask whether the winner-side pressure was stronger than its simple row rank implies.
6. Explicitly ask whether the pressure was current and tightening toward Set1 / col1.
7. Treat top-band under-reading as a live possibility, not an exception.
8. Do not confuse:
   - “winner triad not high-ranked”
   with
   - “Hot Zones did not preserve the winner-side pressure environment”

---

## Part E Output Shape

Part E should end with:
- one Hot Zones truth-alignment judgment
- one survivorship / funnel judgment
- one VT-only / lane corroboration judgment
- one statement on whether Hot Zones truth was:
  - already used
  - partially used
  - compressed too early
  - visible but unconsumed
  - or absent

Recommended answer style:
- pressure environment first
- survivorship and funneling second
- count/span/tag explanation third
- consumer relationship fourth

---

## E0. Hot Zones File Lock And Review Surface

Purpose:
- lock the exact Hot Zones artifacts used in the review
- prevent drift between the compact top-lane feed, deep-drill lane rows, and winner-aware review artifacts

Template:

```md
### E0. Hot Zones File Lock And Review Surface

- Hot Zones top_lanes: `...`
- Hot Zones meta: `...`
- Hot Zones per_lane used?: `yes/no`
- If yes, per_lane file: `...`
- Winner_map used?: `yes/no`
- If yes, winner_map file: `...`
- Hot Zones winners / review files used:
  - `...`
  - `...`

Notes:
- Standalone `hot_zones_arena` artifact available?: `yes/no`
- Primary review surface used: `top_lanes+meta / top_lanes+meta+per_lane`
- Any missing Hot Zones artifact?: `yes/no`
- If something is missing, is this a pipeline issue or just a review-surface issue?: `...`
```

---

## E1. Hot Zones Truth Alignment Summary

Purpose:
- answer immediately whether Hot Zones preserved the Part A truth in a meaningful way
- stop the section from drifting too early into simple top-rank language

Primary questions:
- did Hot Zones preserve the winner-side pressure environment?
- was that pressure late-tail, vertical, funnel-based, VT-only, or diffuse?
- was the winner-side structure stronger as pressure than as literal-caller rank?
- was this a clear Hot Zones case or a faint corroborative one?

Helpful verdict buckets:
- late-tail strong
- vertical strong
- funnel strong
- VT-only lane strong
- pressure present but diffuse
- top-band under-read
- absent

Template:

```md
### E1. Hot Zones Truth Alignment Summary

Part A target:
- `...`

Hot Zones alignment verdict:
- Pressure presence: `strong / moderate / weak / absent`
- Survivorship / vertical support: `strong / moderate / weak / absent`
- Funnel / currentness: `strong / moderate / weak / absent`
- VT-only / lane corroboration: `strong / moderate / weak / absent`

Best one-sentence Hot Zones read:
- `...`

Most important Hot Zones contribution to the Part A truth:
- `...`
```

---

## E2. Top-Lane Pressure Read

Purpose:
- evaluate the primary Hot Zones pressure objects without collapsing immediately into row rank
- determine whether the winner corridor or its pressure-neighborhood was materially represented

Primary surfaces:
- `support_count`
- `score_mean`
- `score_max`
- `literal_hits`
- `guard_hits`
- `evidence_tags`

Primary questions:
- what were the strongest pressure objects?
- was the winner corridor directly represented, pressure-adjacent, or only weakly implied?
- was the Hot Zones row structurally stronger than the raw rank suggested?

Template:

```md
### E2. Top-Lane Pressure Read

Strongest pressure objects:
- `...`

Winner corridor presence:
- `direct / adjacent / weak / absent`

Top-band under-reading risk:
- `high / medium / low / none`

Most important pressure-side clue:
- `...`
```

---

## E3. Late-Tail And Vertical Survivorship Read

Purpose:
- capture the core Hot Zones truth about pressure that survives late and repeats vertically
- determine whether this was a real survivorship environment rather than a shallow hot-slot coincidence

Primary surfaces:
- `vertical_hits`
- `vertical_support`
- `column_span`
- `horizontal_span`
- `variant_echo`
- evidence tags related to vertical or repeat behavior

Primary questions:
- was the pressure truly surviving late?
- was the corridor repeating vertically?
- did the winner-side environment look like a real survivorship case?
- was this pressure persistent or incidental?

Template:

```md
### E3. Late-Tail And Vertical Survivorship Read

Late-tail read:
- `...`

Vertical survivorship read:
- `...`

Was this a real survivorship case?:
- `yes/no/mixed`

Most important survivorship clue:
- `...`
```

---

## E4. Col1, Pre-Col1, And Set1 Funnel Read

Purpose:
- evaluate currentness and tightening toward the frontier
- determine whether the pressure was becoming more actionable through Set1 / pre-col1 / col1 concentration

Primary surfaces:
- `set1_hits`
- `col1_hits`
- `precol1_hits`
- `col1_arrival`
- `precol1_funnel`
- `is_set1`
- tags such as:
  - `col1`
  - `funnel_precol1`
  - `superhot_set1`

Primary questions:
- was the winner-side pressure current?
- was it tightening toward the frontier?
- did Set1 / col1 concentration materially strengthen the case?
- was the pressure actionable rather than only broadly present?

Template:

```md
### E4. Col1, Pre-Col1, And Set1 Funnel Read

Currentness / funnel read:
- `...`

Set1 / col1 concentration:
- `strong / moderate / weak / absent`

Was the pressure tightening toward the frontier?:
- `yes/no/mixed`

Most important funnel/currentness clue:
- `...`
```

---

## E5. VT-Only Lane And VT-Straight Read

Purpose:
- determine whether Hot Zones was telling a lane-first story rather than a literal-first story
- preserve the Hot Zones equivalent of “the right lane is alive even if the literal is noisy”

Primary surfaces:
- `vt_triad`
- `vt_only_lane_hits`
- `vt_only_lane`
- `vt_straight_hits`
- `has_vt_straight`

Primary questions:
- was the truth stronger as a VT lane than as a literal triad?
- did VT-only pressure materially support the winner corridor?
- was Hot Zones reinforcing a lane the literal surface underexplained?

Template:

```md
### E5. VT-Only Lane And VT-Straight Read

VT-only / lane read:
- `...`

VT-straight corroboration:
- `strong / moderate / weak / absent`

Was the lane story stronger than the literal story?:
- `yes/no/mixed`

Most important VT-only clue:
- `...`
```

---

## E6. Count, Span, And Evidence-Tag Read

Purpose:
- preserve the concrete texture that makes Hot Zones meaningful beyond simple row ranking
- stop count/span/tag families from being flattened away in review

Primary surfaces:
- `variant_span`
- `set_span`
- `column_span`
- `hot_hits`
- `superhot_hits`
- `evidence_tags`
- guard/literal context

Primary questions:
- which concrete counts, spans, and tags best explain why this pressure mattered?
- was the row broad, current, concentrated, or diffuse?
- did the counts/spans imply a stronger case than the row rank alone suggests?

Template:

```md
### E6. Count, Span, And Evidence-Tag Read

Most important count/span families:
- `...`

Most important evidence tags:
- `...`

Did the concrete pressure texture exceed the simple rank impression?:
- `yes/no/mixed`

Most important count/span/tag insight:
- `...`
```

---

## E7. Deep-Drill Per-Lane And Digest Relationship

Purpose:
- use the heavier per-lane surface only when needed to confirm the physical story of the pressure
- explicitly note when a digest/ledger layer would improve future review clarity

Primary surfaces:
- `per_lane.csv`
- `hot_zones_sharepack_summary.py`
- any summary/digest outputs available for the case

Primary questions:
- did `top_lanes.csv + meta.json` already tell enough of the story?
- what did `per_lane.csv` clarify that the compact surface did not?
- is this a case where a digest/ledger layer would materially reduce future review friction?

Template:

```md
### E7. Deep-Drill Per-Lane And Digest Relationship

Was deep-drill needed?:
- `yes/no`

What the deep-drill clarified:
- `...`

Digest / ledger value in this case:
- `high / medium / low / none`

Most important per-lane confirmation:
- `...`
```

---

## E8. Hot Zones Consumer And Policy Relationship

Purpose:
- explicitly separate the full Hot Zones evidence from the bounded helper surfaces currently used downstream
- ask whether the remaining problem was Hot Zones-local, arena-level, or downstream-level

Primary bounded helpers to compare against:
- `hot_zones_top_triads`
- `hot_zones_index_closure`
- `signals_bundle.hot_zones.triads`

Primary questions:
- what did the full Hot Zones evidence preserve that bounded helpers did not?
- was the pressure truth visible but compressed too early into top-triad language?
- is the remaining issue better described as:
  - tool extraction
  - arena preservation
  - downstream compression / consumption
  - or no-action

Helpful conclusion buckets:
- already used well
- partially used
- visible but compressed
- visible but unconsumed
- not yet promotable
- absent

Template:

```md
### E8. Hot Zones Consumer And Policy Relationship

What Hot Zones clearly preserved:
- `...`

What current bounded consumers actually used:
- `...`

Main failure point if the win was not closed:
- `tool extraction / arena preservation / downstream compression / no_action / mixed`

Policy relationship verdict:
- `already used well / partially used / visible but compressed / visible but unconsumed / not yet promotable / absent`
```

---

## E9. Hot Zones Handoff

Purpose:
- close Part E with the shortest possible Hot Zones-specific learning statement for later sections

Template:

```md
### E9. Hot Zones Handoff

- Strongest Hot Zones truth: `...`
- Strongest Hot Zones evidence family: `late-tail / vertical / funnel / Set1-currentness / VT-only lane / count-span-tag texture`
- Strongest unused Hot Zones insight: `...`
- Hot Zones-specific limitation in this case: `...`
- Main comparison target for Part F or later arena synthesis: `...`
```

---

## Part E Analyst Guidance

Good Part E outputs:
- judge pressure environment before top-triad rank
- explicitly assess survivorship and funnel/currentness
- preserve concrete counts, spans, and tags
- treat VT-only pressure as a real lane clue when warranted
- separate full Hot Zones truth from bounded helper consumption

Bad Part E outputs:
- “winner triad was not top-ranked so Hot Zones failed”
- “top-10 is the whole story”
- “one interesting evidence tag means immediate promotion”
- “the tool needs another broad weight sweep because a lower-ranked row mattered”

Correct Part E posture:
- pressure truth first
- survivorship and funneling second
- concrete pressure texture third
- consumer/compression relationship fourth
- promotion only after repeated proof

This is especially important for:
- top-band under-reading
- late-tail survivorship
- col1 / pre-col1 funnel strength
- VT-only lane corroboration
- concrete count/span/tag preservation

These are often where Hot Zones' real value lives.

---

## Part F Placeholder

Planned next section:
- `Part F — Aggregated Analysis Arena`

Future Parts are expected to continue through the aggregated arena, then context layers, then downstream baseline comparison and final synthesis.
