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
- `survivor_progressions`
- `last_remaining` / survivor counts
- `frontier_pattern_summary.hidden_terminal_patterns_*`
- `hidden_family_reveal`
- `hidden_family_reveal_summary`
- `order_transform_hints`
- `order_transform_summary`
- VT-straight style clues when they are structurally important

Primary questions:
- was this a survivor/frontier case?
- was the terminal survivor truth literal, family-like, VTRAC-like, or hidden-terminal?
- was hidden-family reveal important?
- were transform or modal-order clues important?
- did Stable preserve something subtle here that is visible but not yet strongly promoted?

Template:

```md
### B5. Survivor, Frontier, Hidden, And Transform Read

Survivor/frontier read:
- `...`

Last-remaining / hidden-terminal read:
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

## Part F — Aggregated Analysis Arena

Purpose:
- review the actual Brain-1 synthesis object
- judge whether the arena integrated the strongest truths from Parts B-E into the right per-state story
- separate:
  - what the tools knew
  - what the arena surfaced
  - what later layers still have to decide

This part is the first place in the template that directly asks:
- did the per-state system itself form the correct integrated state thesis?

This part should answer:
- did the arena preserve the Part A truth coherently?
- did it synthesize the strongest tool truths correctly?
- was the state more lane-right, family-right, or canonical-right?
- did context reinforce the same truth, or create separate pressure?
- what did the arena make clearer than the individual tool sections alone?

This part should not answer:
- whether Aux / Control Center was semantically correct in full detail
- whether Candidate Universe or Play Card closed the win
- what the final pack geometry should be
- whether a budget should be raised or lowered

Those belong later.

---

## Part F Inputs

Primary inputs:
- `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__*.json`
- optional markdown twin:
  - `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__*.md`

If reviewing frozen/results roots:
- use the same arena artifact under the frozen sharepack root
- winners links may be present for review, but the arena evidence remains predictive-side in meaning

Recommended companion inputs:
- Part A notes
- Part B-E notes
- arena contract:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md`
- state-level arena review memo / scoreboard if present
- state-day review scoreboard if present

Use tool-local artifacts only when:
- the arena summary leaves an ambiguity
- provenance is unclear
- a tie between surfaces needs to be resolved

Do not reopen whole raw tool folders by default.

---

## Part F Reading Rules

1. Treat the arena as an integrator, not a final caller.
2. Read `cross_tool_relations` before `arena_synthesis`.
3. Judge lane/family truth fairly even when literal canonical concentration is weak.
4. Treat `context_reinforced` and `context_only_pressure` as different states.
5. Treat contradiction flags as prompts for diagnosis, not automatic failure labels.
6. Treat the VTRAC watchlist as a corridor-review surface, not a direct play pack.
7. Keep downstream handoff in the background only; direct downstream comparison belongs later.
8. Ask what the arena made clearer than Parts B-E alone, not only what it ranked first.

---

## Part F Output Shape

Part F should end with:
- one overall arena verdict
- one dominant state-thesis statement
- one strongest preserved truth
- one main aggregation gap
- one explicit handoff into Part G

Recommended answer style:
- synthesis first
- tables and top lists only where they clarify
- avoid raw payload dumping
- explicitly separate:
  - preserved
  - underweighted
  - contradicted
  - only context-driven

---

## F0. Arena File Lock And Review Surface

Purpose:
- lock the exact aggregated arena artifact used for review
- make the section auditable before interpretation begins

Record:
- results date `D`
- history date `H`
- state
- arena JSON path
- arena markdown path if used
- profile / experiment tag
- predictive root or frozen/results root
- whether winners links are present inside the arena object

Template:

```md
### F0. Arena File Lock And Review Surface

- Results date: `...`
- History date: `...`
- State: `...`
- Arena JSON:
  - `...`
- Arena markdown:
  - `...`
- Profile / experiment: `...`
- Root mode: `predictive / frozen-results`
- Arena contains winners links: `true/false`

Review surface notes:
- primary arena object reviewed: `...`
- any supporting arena review memo used?: `yes/no`
- reason those supports were needed: `...`
```

---

## F1. Arena Truth Alignment Summary

Purpose:
- give the shortest possible answer to whether the arena preserved the Part A truth as an integrated state story

Recommended verdict language:
- `truth preserved coherently`
- `lane preserved, literal weak`
- `family preserved, lane mixed`
- `truth present but underweighted`
- `context-reinforced but split`
- `truth diluted by contradiction`
- `truth absent`

Template:

```md
### F1. Arena Truth Alignment Summary

Part A target:
- `...`

Arena truth-alignment verdict:
- `truth preserved coherently / lane preserved, literal weak / family preserved, lane mixed / truth present but underweighted / context-reinforced but split / truth diluted by contradiction / truth absent`

Why:
- `...`

Most important Brain-1 read:
- `...`
```

---

## F2. Provenance, Source Status, And Predictive-Safe Boundary

Purpose:
- verify that the arena object is complete and trustworthy before drawing meaning from it

Focus:
- `metadata`
- `provenance`
- `source_status`
- `evidence_paths`
- `contains_winners_artifacts`

Primary questions:
- were all major tool/context sources present?
- was anything rebuilt, preloaded, or missing?
- was the object reviewed under predictive-safe or frozen conditions?
- are winners links being treated only as review aids rather than predictive meaning?

Template:

```md
### F2. Provenance, Source Status, And Predictive-Safe Boundary

Source-status read:
- Stable: `available / missing / degraded`
- Digit Reduction: `available / missing / degraded`
- VTRAC: `available / missing / degraded`
- Hot Zones: `available / missing / degraded`
- Aux / Control Center: `available / missing / degraded`

Boundary read:
- Arena mode: `predictive-safe / frozen-review`
- Winners links role: `none / navigation only / active review aid`
- Any source ambiguity?: `...`

Trust judgment:
- `fully reviewable / reviewable with caveats / partially degraded / not safe to interpret strongly`
```

---

## F3. Cross-Tool Consensus Read

Purpose:
- review the raw cross-tool agreement layer before judging the arena summary layer

Centered on:
- `canonical_consensus_top`
- `vtrac_index_consensus_top`
- `family_consensus_top`

Primary questions:
- where did tools actually agree?
- was literal agreement stronger or weaker than lane agreement?
- was family agreement the clearest preserved truth?
- did context overlap with the same objects or point elsewhere?

Template:

```md
### F3. Cross-Tool Consensus Read

Canonical consensus read:
- `...`

VTRAC-index consensus read:
- `...`

Family consensus read:
- `...`

Cross-tool agreement verdict:
- strongest agreement surface: `canonical / VTRAC lane / family / mixed`
- best match to Part A truth: `...`
- main disagreement or dilution point: `...`
```

---

## F4. Dominant Arena Synthesis Read

Purpose:
- judge what story the arena actually surfaced to the reviewer after aggregation

Centered on:
- `dominant_canonicals`
- `dominant_vtrac_indices`
- `dominant_families`
- `stable_survivor_context`
- `r_consensus_context`

Primary questions:
- what is the arena saying the state is mainly about?
- do the dominant canonical, lane, and family stories agree?
- did the arena surface a meaningful survivor / last-remaining state thesis?
- did the arena preserve a meaningful `R-Consensus` / tail-consensus state condition when one was present?
- if they do not agree, which one is most truthful?

Important distinction:
- this section is not about raw vote existence
- it is about what the arena elevated to the top surface

Template:

```md
### F4. Dominant Arena Synthesis Read

Dominant canonical story:
- `...`

Dominant VTRAC story:
- `...`

Dominant family story:
- `...`

Survivor-state thesis:
- `...`

R-Consensus thesis:
- `...`

Arena surfaced-state thesis:
- `...`

Synthesis judgment:
- `coherent / lane-right but literal-split / family-right but lane-soft / context-biased / mixed / underweighted`
```

---

## F5. VTRAC Literal Watchlist And Split Read

Purpose:
- evaluate one of the arena’s most valuable distinctive surfaces:
  - lane-linked literal neighborhoods

Centered on:
- `vtrac_literal_watchlist`
- `dominant_canonical_split`

Primary questions:
- were the right lane-linked literal neighborhoods preserved?
- did the watchlist tell a truer story than the top canonical table?
- was the dominant canonical on the same lane or split away?

This section matters because many current arena successes are:
- VTRAC-right
- literal-not-yet-promoted enough

Template:

```md
### F5. VTRAC Literal Watchlist And Split Read

Most relevant watchlist lanes:
- `...`

Best candidate-canonical neighborhoods:
- `...`

Split read:
- dominant canonical split?: `yes/no`
- if yes, why it matters: `...`

Watchlist judgment:
- `watchlist clearer than literal summary / watchlist supportive only / watchlist noisy / watchlist not useful here`
```

---

## F6. Context Reinforcement Versus Context-Only Pressure

Purpose:
- judge whether the arena used context correctly at the synthesis level

Centered on:
- `context_reinforced_canonicals`
- `context_only_pressure`

Primary questions:
- which canonicals were reinforced by both string and context layers?
- which canonicals were only context-driven?
- did that distinction look right relative to Part A?

Important guardrail:
- do not deep-dive individual Aux / Control Center mechanics yet
- that belongs in Part G

This section is only about:
- how the arena synthesized context
- not full context semantics

Template:

```md
### F6. Context Reinforcement Versus Context-Only Pressure

Context-reinforced canonicals:
- `...`

Context-only pressure:
- `...`

Arena context-use judgment:
- `reinforcement looked correct / some context-only inflation / mostly clean / heavily mixed / unclear`

Most important implication for Part G:
- `...`
```

---

## F7. State Regime And Contradiction Read

Purpose:
- classify the overall shape of the state according to the arena

Centered on:
- `regime_flags`
- `contradiction_flags`
- `state_regime`

Primary questions:
- is this a double-heavy state?
- is context materially reinforcing the same state story?
- is VTRAC stronger than literal?
- is survivor pressure materially part of the state?
- is there last-remaining or hidden-terminal support?
- is the state split, diluted, or contradictory?
- did the arena correctly describe the shape of the state?

Template:

```md
### F7. State Regime And Contradiction Read

Regime flags:
- `...`

Contradiction flags:
- `...`

State-shape read:
- dominant canonical: `...`
- dominant VTRAC index: `...`
- dominant family: `...`
- survivor pressure: `true/false`
- last_remaining: `true/false`
- hidden_terminal_support: `true/false`
- state regime class: `double-heavy / lane-first / family-first / literal-first / split / diluted / mixed`

Judgment:
- regime labeling was `accurate / partly accurate / too soft / too harsh / misleading`
```

---

## F8. Arena Added Value Read

Purpose:
- answer the most important meta-question of Part F:
  - what did the arena make clearer than the individual tool sections alone?

This is the section that justifies why the arena exists.

Primary questions:
- what new understanding did aggregation create?
- did the arena expose a coherent state thesis that was not obvious tool-by-tool?
- did it clarify a contradiction?
- did it reveal that lane truth was stronger than literal truth?
- did it make context overlap legible in a way the raw tools did not?

Template:

```md
### F8. Arena Added Value Read

What the arena clarified beyond tool-local review:
- `...`

What was newly legible only after aggregation:
- `...`

What still stayed unclear even after aggregation:
- `...`

Added-value verdict:
- `high / meaningful / moderate / narrow / weak`
```

---

## F9. Review Prompts, Arena Judgment, And Handoff

Purpose:
- close the section with a clean arena judgment
- assess whether the arena’s own review prompts pointed the reviewer in the right direction
- hand off cleanly into Part G

Centered on:
- `review_prompts`
- overall arena verdict

Primary questions:
- were the prompts useful?
- did the arena point attention toward the right next review surfaces?
- what does Part G most need to inspect now?

Template:

```md
### F9. Review Prompts, Arena Judgment, And Handoff

Most useful arena review prompts:
- `...`

Prompt quality:
- `helpful / partly helpful / generic / misleading`

Final Part F judgment:
- strongest preserved truth: `...`
- strongest underweighted truth: `...`
- main aggregation gap: `...`
- handoff target for Part G: `...`
```

---

## Part F Analyst Guidance

Good Part F outputs:
- judge the arena as an integrator, not a final literal caller
- distinguish raw cross-tool consensus from surfaced synthesis
- fairly credit lane/family preservation even when literal concentration is weak
- clearly separate context-reinforced truth from context-only pressure
- explain what aggregation added beyond Parts B-E

Bad Part F outputs:
- “top canonical missed, so the arena failed”
- “the arena is just a bundle of files”
- “context appeared anywhere, so the state is reinforced”
- “contradiction flags are present, so the state is unusable”
- “downstream missed, so the arena must have missed too”

Correct Part F posture:
- integration quality first
- lane/family truth second
- context synthesis discipline third
- state-shape diagnosis fourth
- handoff into deeper context review after that

This is especially important for:
- VTRAC-lane-right / literal-weak states
- family-first states
- context-reinforced but split states
- double-heavy or contradiction-heavy states
- cases where the arena added clarity even though it did not directly close the winner

These are often where the arena’s real value lives.

---

## Part G — Aux / Control Center Context

Part G is the per-state context audit.

It is the section where the reviewer should determine:

- which aggregate trackers and context systems actually fired
- which lists, alerts, and context objects were truly available
- what those objects meant in relation to the Part A truth and the Part F arena state thesis
- what was direct, what was reinforcing, and what was only composite / relational
- what was already preserved by the arena
- what still lives only in raw context outputs or heavy truth layers
- what should remain review-only
- what looks like a real structural follow-up for later Brain 2 / final-findings work

This is not the place to decide final budgets or final packs.

It **is** the place to establish whether the broader context layer:

- materially reinforced the state thesis
- surfaced hidden value that current bounded consumers underuse
- or mostly created pressure without enough structural alignment

---

## Part G Inputs

Primary predictive-side context inputs:

- `sharepacks/_predictive/<D>/<STATE>/aux/<STATE>/summary.json`
- `sharepacks/_predictive/<D>/control_center/due_doubles.csv`
- `sharepacks/_predictive/<D>/control_center/vtrac_repeat_watch.csv`
- `sharepacks/_predictive/<D>/control_center/blackapple_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_compound_events.csv`
- `sharepacks/_predictive/<D>/control_center/meta.json`

Primary arena bridge inputs:

- `sharepacks/_predictive/<D>/<STATE>/analysis/aux_control_center_arena*.json`
- `sharepacks/_predictive/<D>/<STATE>/analysis/aux_control_center_arena*.md`
- `aggregated_analysis_arena__tool_only__arena_v0.json`
  - especially the context objects and the Part F handoff

Important arena-era context objects to prioritize:

- `aux_positional_pressure`
- `aux_vtrac_pressure`
- `aux_badge_pressure`
- `aux_pair_band_context`
- `aux_due_doubles_family_pressure`
- `aux_repeat_watch_context`
- `aux_sums_context`
- `aux_blackapple_context`
- `cc_profit_alert_context`
- `cc_compound_event_context`
- `cc_tracker_context`

Important heavy truth / deep-drill layers when needed:

- full Blackapple candidate ledgers inside `summary.json`
- positional shortlist and advanced note surfaces inside `summary.json`
- full profit-alert evidence rows / detailed evidence JSON when available
- boxed VTRAC badge matrix reports and related badge-mining exports
- raw pair / combo / sum tables when the compact surfaces hide an important relationship

Guardrail:
- these heavier layers are valid review surfaces
- they are **not** automatically bounded predictive policy

---

## Part G Reading Rules

1. Start from the Part F handoff, not from a flat list of Aux tables.
2. Read Aux / Control Center first as a **context reinforcement and pressure layer**, not as a replacement for structural string truth.
3. Explicitly separate:
   - direct context support
   - reinforcing context support
   - context-only pressure
   - relational / composite clues
4. Do not confuse:
   - “a list exists”
   with
   - “that list is already fully surfaced and properly used by the current system”
5. Treat alert rows as structured episodes when relevant:
   - current draw
   - same-day carry
   - next-draw / short-decay relevance
6. Keep same-period, opposite-period, and Combined reinforcement explicit when cross-variant context matters.
7. When a board surface looks too thin, check the underlying context summary or arena object before concluding the signal was absent.
8. Preserve the distinction between:
   - review value
   - arena-preservation value
   - bounded predictive use
   - Brain 2 / final-findings value
9. Do not promote a context signal just because it looks clever in one case.
10. Do not flatten composite relationships into direct hits.

---

## Part G Output Shape

Part G should end with:

- one overall context-alignment judgment
- one alert / tracker judgment
- one shortlist / recommended-list judgment
- one direct-vs-composite judgment
- one statement on what is:
  - already used well
  - preserved but under-surfaced
  - preserved but unconsumed
  - only visible in heavy truth layers
  - or deserving a future structural follow-up

Recommended answer style:

- context alignment first
- concrete alert / shortlist specifics second
- hidden-value assessment third
- policy / structural-follow-up judgment fourth

---

## G0. Context File Lock And Review Surface

Purpose:
- lock the exact Aux / Control Center surfaces used in the review
- prevent drift between compact board outputs, state summary JSON, and arena bridge summaries

Template:

```md
### G0. Context File Lock And Review Surface

- Aux summary: `...`
- Due doubles board: `...`
- VTRAC repeat board: `...`
- Blackapple board: `...`
- Profit alerts board: `...`
- Profit compound-events board: `...`
- Control Center meta: `...`
- Aux / CC arena bridge JSON: `...`
- Aux / CC arena bridge MD used?: `yes/no`
- Aggregated arena used for Part F handoff: `...`

Deep-drill layers used?:
- Blackapple full candidate list: `yes/no`
- Positional shortlist + advanced notes: `yes/no`
- Badge matrix / heavy badge reports: `yes/no`
- Raw profit evidence drill-down: `yes/no`
- Other heavy truth layer: `...`

Missing or degraded context surface?:
- `yes/no`

If something is missing, classify the issue:
- `none / review-surface gap / export gap / arena-bridge gap / pipeline gap`
```

---

## G1. Context Truth Alignment Summary

Purpose:
- answer immediately whether the context layer materially reinforced the Part A truth and the Part F state thesis
- stop the section from drifting too early into raw board detail

Primary questions:
- did context reinforce the live state story?
- was the strongest context support direct, lane/family, or composite?
- did the context layer clarify the state, or mainly create background pressure?
- was this a genuinely context-rich state or only a lightly corroborated one?

Helpful verdict buckets:
- context strongly reinforcing
- context reinforcing but still split
- context-rich but mostly composite
- context present but underweighted
- context present but mostly background
- context weak
- context absent

Template:

```md
### G1. Context Truth Alignment Summary

Part A target:
- `...`

Part F handoff target:
- `...`

Context alignment verdict:
- Direct support: `strong / moderate / weak / absent`
- Reinforcing support: `strong / moderate / weak / absent`
- Composite / relational value: `high / medium / low / none`
- Context-only pressure risk: `high / medium / low / none`

Best one-sentence context read:
- `...`

Most important context-layer contribution:
- `...`
```

---

## G2. Profit Alerts And Compound Events

Purpose:
- audit the strongest explicit alert layer in Control Center
- determine which alerts fired, what they implied, and whether they behaved as direct, reinforcing, or composite evidence
- ensure compound-event structure is not lost in flat alert-row reading

Primary surfaces:
- `cc_profit_alert_context`
- `cc_compound_event_context`
- `profit_alerts.csv`
- `profit_compound_events.csv`

Important alert fields to inspect:
- `AlertId`
- `Strength`
- `Suggested`
- `CapLines`
- `DecayDraws`
- `Badges`
- `Canonical`
- `ImpliedSet`
- parsed `Evidence`

Primary questions:
- which `A01-A12` fired for this state?
- which alerts were strongest?
- what combinations / implied sets were actually being signaled?
- did multiple alerts co-fire into a meaningful compound event?
- was the relationship to the winner:
  - direct
  - lane/family
  - composite
  - or absent?
- did the alert appear to be a current-draw signal, a same-day carry, or a short-decay episode?

Template:

```md
### G2. Profit Alerts And Compound Events

Strongest profit alerts:
- `...`

Key alert details:
- Alert IDs fired: `...`
- Strongest canonical / implied set: `...`
- Badges / suggested mode: `...`
- Decay / episode posture: `current / same-day / short-decay / unclear`

Compound-event read:
- Top event: `...`
- Priority / merged rows / linked alerts: `...`
- Did co-fire materially strengthen the case?: `yes/no/mixed`

Winner relationship:
- `direct / lane-family / composite / absent`

Most important profit-alert learning:
- `...`
```

---

## G3. Due Doubles, Mirror Doubles, And Family Pressure

Purpose:
- inspect due-double pressure as a family-pressure and relation-pressure surface, not just a literal overdue list
- preserve the real value of double and mirror-double regimes without forcing them into flat caller language

Primary surfaces:
- `aux_due_doubles_family_pressure`
- `due_doubles.csv`
- related alert overlap:
  - `A02`
  - `A10`

Primary questions:
- what overdue double families were active?
- which variants were strongest?
- did the state show mirror-double or lane-adjacent double pressure?
- was the relationship direct, family-level, mirror-related, VTRAC-related, or only composite?
- was the due-double structure part of the true state thesis or just background noise?

Template:

```md
### G3. Due Doubles, Mirror Doubles, And Family Pressure

Strongest due-double families:
- `...`

Variant posture:
- `Midday / Evening / Combined / cross-variant`

Relationship type:
- `direct / family / mirror-double / VTRAC-related / composite / absent`

Did A02 / A10 materially matter here?:
- `yes/no/mixed`

Most important due-double pressure clue:
- `...`

Main limitation of the current due-double surface:
- `...`
```

---

## G4. VTRAC Repeat And Tracker Context

Purpose:
- inspect the repeat-watch and tracker layer as lane-context and regime-context
- determine whether tracker state aligned with the dominant arena lane or only created background pressure

Primary surfaces:
- `aux_repeat_watch_context`
- `cc_tracker_context`
- `vtrac_repeat_watch.csv`
- related alert overlap:
  - `A09`

Primary questions:
- what was the current index and streak behavior?
- what did the heatboard / hazard view imply?
- did repeat-watch align with the arena’s dominant lane or watchlist?
- was this genuinely useful lane reinforcement, or only a weak tracker-side note?

Template:

```md
### G4. VTRAC Repeat And Tracker Context

Repeat-watch posture:
- Current index / streak: `...`
- Heat / hazard read: `...`
- Last-repeat posture: `...`

Alignment with arena lane story:
- `strong / moderate / weak / absent`

Did A09 or tracker context materially matter?:
- `yes/no/mixed`

Most important repeat / tracker clue:
- `...`
```

---

## G5. Blackapple Alert Status, Triggers, And Recommended Lists

Purpose:
- review Blackapple as an alert-status and recommended-list system, not just a small board caption
- ensure the full recommended list and variant-level signal state are actually inspected when relevant

Primary surfaces:
- `aux_blackapple_context`
- `blackapple_alerts.csv`
- full `summary.json`
  - `blackapple.by_variant.<variant>.candidates`
  - trigger flags
  - scores

Primary questions:
- was the state `OFF`, `WATCH`, or `ALERT`?
- what triggers actually fired?
- what candidate / recommended combos were being surfaced?
- were those candidates aligned across variants?
- did Blackapple reinforce the arena truth, or float independently?
- did any candidate or related family/lane matter under:
  - direct
  - boxed
  - VT-box
  - VT-straight
  review?
- does this case suggest BA needs episode / decay tracking attention?

Template:

```md
### G5. Blackapple Alert Status, Triggers, And Recommended Lists

Blackapple status:
- Score / standing: `OFF / WATCH / ALERT`
- Trigger flags: `...`
- Candidate count: `...`

Recommended-list read:
- Strongest candidate combos: `...`
- Variant agreement: `strong / moderate / weak / absent`
- Did the board view hide stronger list detail than the raw summary?: `yes/no`

Winner relationship:
- `direct / boxed / VT-box / VT-straight / composite / absent`

Decay / episode relevance:
- `high / medium / low / none`

Most important Blackapple learning:
- `...`
```

---

## G6. Positional Pressure, Shortlist, And Advanced Notes

Purpose:
- review positional as a richer pressure and shortlist system, not just a small helper list
- preserve the advanced positional surfaces that earlier simplified readings tended to flatten away

Primary surfaces:
- `aux_positional_pressure`
- `summary.json`
  - `hard_due_by_variant`
  - `shortlist_report.candidates`
  - `shortlist_report.variant_top_digits`
  - `shortlist_report.aggregated_digits`
  - `consensus_notes`
  - `double_pressure_notes`

Primary questions:
- what was the shortlist actually saying?
- what digits / lanes / doubles were most concentrated?
- did advanced positional notes materially reinforce the state story?
- was positional pressure direct, reinforcing, or mostly structural background?
- did the shortlist contain or strongly shoulder the relevant family/VTRAC structure?

Template:

```md
### G6. Positional Pressure, Shortlist, And Advanced Notes

Shortlist posture:
- Strongest shortlist items: `...`
- Aggregated digits / top digits: `...`
- Hard-due posture by variant: `...`

Advanced-note read:
- Consensus notes: `...`
- Double-pressure notes: `...`

Winner / state-story relationship:
- `direct / reinforcing / lane-family / composite / absent`

Most important positional learning:
- `...`
```

---

## G7. Badge, VTRAC Index, Pair, Sums, And Cross-Variant Compound Read

Purpose:
- inspect the broader Aux compound-pressure layer that often contains hidden value
- preserve which badge, pair, sum, and VTRAC-index surfaces were actually active
- force a deliberate read of cross-variant reinforcement when it matters

Primary surfaces:
- `aux_badge_pressure`
- `aux_vtrac_pressure`
- `aux_pair_band_context`
- `aux_sums_context`
- heavy badge matrix reports when needed

Primary questions:
- what badge pressure was active?
- did badge pressure align across Midday, Evening, and Combined?
- what VTRAC overlay / heatboard indices were strongest?
- did pair or sum context materially reinforce the state thesis?
- did cross-variant compounding appear meaningful or only ambient?
- is the most important relationship here direct, reinforcing, or composite?

Template:

```md
### G7. Badge, VTRAC Index, Pair, Sums, And Cross-Variant Compound Read

Badge pressure read:
- `...`

VTRAC overlay / heatboard read:
- `...`

Pair / sums / cross-variant compound read:
- `...`

Most important context family here:
- `badge / VTRAC index / pair-band / sums / cross-variant compound`

Did this layer look:
- `direct / reinforcing / composite / background / absent`

Most important compound-pressure insight:
- `...`
```

---

## G8. Context Reinforcement Versus Context-Only Pressure

Purpose:
- explicitly connect Part G back to Part F’s distinction between context-reinforced truth and context-only pressure
- judge whether the arena’s synthesis-level context reading was semantically correct

Primary surfaces:
- `context_reinforced_canonicals`
- `context_only_pressure`
- relevant Part G findings above

Primary questions:
- which context objects truly reinforced the state thesis?
- which objects were real but only pressure-side?
- did the Part F distinction look correct after deep context review?
- which context surfaces were semantically strongest even if not yet heavily used?

Template:

```md
### G8. Context Reinforcement Versus Context-Only Pressure

What truly reinforced the state thesis:
- `...`

What was mostly context-only pressure:
- `...`

Did Part F’s reinforcement vs pressure distinction hold up?:
- `yes/no/mixed`

Most semantically correct context object:
- `...`
```

---

## G9. Deep-Drill Truth Layers, Hidden Value, And Measurement Gaps

Purpose:
- make the hidden-value question explicit
- identify what is already preserved, what is under-surfaced, and what still needs better measurement
- stop real value from disappearing just because it is not on a flat board

Primary heavy truth / gap targets:
- full Blackapple candidate ledgers
- positional shortlist detail
- heavy badge-matrix exports
- raw profit-alert evidence detail
- compound-event detail
- shortlist / alert / candidate decay-window behavior

Primary questions:
- what valuable material was only visible after a deep-drill?
- what is already preserved in the arena but not surfaced prominently?
- what is running but effectively under-measured?
- what needs a future decay / episode / shortlist-performance harness?

Template:

```md
### G9. Deep-Drill Truth Layers, Hidden Value, And Measurement Gaps

Most important hidden or under-surfaced value:
- `...`

Current status of that value:
- `already preserved / partially surfaced / raw-only / not yet modeled`

Most important measurement gap:
- `...`

Best candidate for future decay / episode / shortlist tracking:
- `...`
```

---

## G10. Consumer, Policy, And Structural Follow-Up Relationship

Purpose:
- separate what the current system already uses from what it merely preserves
- identify what belongs in bounded predictive policy, what belongs in Brain 2, and what should remain review-only for now

Primary bounded consumers / current usage surfaces:
- `aux_positional`
- `aux_vtrac_index_overdue`
- `due_doubles`
- `mirror_pair_closure`
- optional / profile-gated:
  - `profit_alerts`
  - `blackapple`

Primary questions:
- what was already used well by the current system?
- what was preserved but under-surfaced?
- what was preserved but not consumed?
- what needs a richer arena/context bridge?
- what belongs more naturally in Brain 2 / final findings than in Brain 1 scoring?

Helpful conclusion buckets:
- already used well
- preserved and appropriately bounded
- preserved but under-surfaced
- preserved but unconsumed
- needs richer bridge / export
- Brain 2 candidate
- review-only for now

Template:

```md
### G10. Consumer, Policy, And Structural Follow-Up Relationship

What the current system already used well:
- `...`

What the current system preserved but still underuses:
- `...`

Best structural follow-up target:
- `arena/context bridge / Brain 2 overlay / decay harness / shortlist ledger / candidate relationship layer`

Policy / structural verdict:
- `already used well / preserved and appropriately bounded / preserved but under-surfaced / preserved but unconsumed / needs richer bridge / Brain 2 candidate / review-only for now`
```

---

## G11. Aux / Control Center Handoff

Purpose:
- close Part G with the shortest possible context-layer learning statement for later sections

Template:

```md
### G11. Aux / Control Center Handoff

- Strongest context truth: `...`
- Strongest direct context signal: `...`
- Strongest composite / relational context clue: `...`
- Strongest hidden or under-surfaced value: `...`
- Best structural follow-up target: `...`
- Main comparison target for Part H or later Brain 2 work: `...`
```

---

## Part G Analyst Guidance

Good Part G outputs:
- separate direct, reinforcing, and composite relationships cleanly
- inspect recommended lists and shortlists when they matter, not just board captions
- treat due doubles and BA as richer regimes than literal-only callers
- use compound events to understand alert co-fire instead of reading alerts in isolation
- preserve the distinction between review value, arena value, and bounded predictive use
- clearly identify what belongs in later structural follow-up rather than forcing everything into Brain 1

Bad Part G outputs:
- “a context table exists, so the system already uses everything important”
- “an alert fired, so it must be predictive”
- “the board didn’t show the list, so the list doesn’t exist”
- “a clever composite relation should immediately become policy”
- “Aux is noisy, so it does not matter”

Correct Part G posture:
- context reinforcement first
- structured alert / shortlist review second
- hidden-value detection third
- policy / bridge / Brain 2 separation fourth

This is especially important for:
- double-heavy or mirror-heavy states
- states with multiple profit alerts or co-fired compound events
- BA `WATCH` / `ALERT` states
- positional-shortlist states with strong advanced notes
- cases where the context layer was more right relationally than literally

---

## Part H — Downstream Baseline Comparison

Part H judges the current downstream control arm.

This is the section where the reviewer should determine:

- what the existing baseline consumers actually received
- what Candidate Universe preserved
- what Play Card retained under budget
- whether the lane survived
- whether exact closure was lost later
- whether the failure was:
  - upstream truth absence
  - bounded conversion absence
  - Candidate Universe compression
  - Play Card budget squeeze
  - profile / strategy posture
  - or some mixed bottleneck

This section is important because the baseline downstream stack still exists in the branch.

But it must be reviewed in the correct role:

- as the current control arm
- not as the definition of truth
- not as the definition of what the arena “really knew”

---

## Part H Inputs

Primary downstream artifacts:

- `sharepacks/_predictive/<D>/<STATE>/candidate_universe__*.json`
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe__*.md`
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__*.csv`
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__*.md`
- `sharepacks/_predictive/<D>/<STATE>/signals_bundle*.json`
- `sharepacks/_predictive/<D>/<STATE>/play_card__*.json`
- `sharepacks/_predictive/<D>/<STATE>/play_card__*.md`

Helpful predictive/report companions:

- predictive run report
- glass-box trace
- winners digest
- Candidate Universe grades
- Play Card grades
- lane-allocation / conversion casebook reports

Helpful arena-side bridge surfaces:

- `downstream_handoff`
- `review_links`

Guardrail:
- downstream artifacts are decision-layer and selection-layer artifacts
- they are not the truth layer

---

## Part H Reading Rules

1. Start from Parts A-F and G, not from the downstream ranking alone.
2. Treat:
   - Candidate Universe as `what we could play`
   - Play Card as `what we would play`
3. Separate these failure modes explicitly:
   - truth absent before Candidate Universe
   - truth present in Candidate Universe but not strongly surfaced
   - lane retained but exact closure lost
   - Candidate Universe preserved it but Play Card cut it
   - strategy / profile / budget posture de-emphasized it
4. Do not blame the arena for a downstream miss unless the arena truth was genuinely absent.
5. Do not give downstream full credit for truth that only survived accidentally or derived-only.
6. Use `tool_only / mixed / profit_only` or strategy variants only when they materially change the conclusion.
7. Preserve the distinction between:
   - direct evidence
   - bounded conversion
   - budget geometry
   - post-results grading
8. If the downstream layer did well, say so plainly.
9. If the downstream layer missed because it is still the older control arm, say that plainly too.

---

## Part H Output Shape

Part H should end with:

- one Candidate Universe judgment
- one Play Card judgment
- one lane-retention / exact-closure judgment
- one bottleneck classification
- one statement on whether the baseline control arm:
  - already expresses the state well
  - partially expresses it
  - preserves the lane but not the box
  - compresses away too much truth
  - or is simply the wrong layer for this case

Recommended answer style:

- Candidate Universe first
- Play Card and budget squeeze second
- bottleneck classification third
- baseline-control-arm judgment fourth

---

## H0. Downstream File Lock And Control-Arm Surface

Purpose:
- lock the exact downstream artifacts used in the review
- prevent drift between Candidate Universe, evidence view, Play Card, and grade files

Template:

```md
### H0. Downstream File Lock And Control-Arm Surface

- Candidate Universe JSON: `...`
- Candidate Universe MD used?: `yes/no`
- Candidate Universe evidence CSV: `...`
- Candidate Universe evidence MD used?: `yes/no`
- signals_bundle used?: `yes/no`
- If yes, signals_bundle path: `...`
- Play Card JSON: `...`
- Play Card MD used?: `yes/no`

Optional predictive/report companions used:
- Predictive report: `yes/no`
- Glass-box trace: `yes/no`
- Candidate Universe grade: `yes/no`
- Play Card grade: `yes/no`
- Lane-allocation / casebook report: `yes/no`

Downstream profile / strategy under review:
- Profile: `tool_only / mixed / profit_only / other`
- Strategy: `...`
- Budget: `...`

Missing or degraded downstream surface?:
- `yes/no`

If something is missing, classify the issue:
- `none / review-surface gap / predictive artifact gap / grading gap / pipeline gap`
```

---

## H1. Downstream Alignment Summary

Purpose:
- answer immediately how well the current baseline consumers expressed the state truth already established upstream

Primary questions:
- did Candidate Universe preserve the relevant state truth?
- did Play Card retain it under budget?
- was the lane preserved even when exact closure failed?
- is this a clean downstream success, a partial expression, or a conversion squeeze?

Helpful verdict buckets:
- downstream expressed the state well
- Candidate Universe strong, Play Card partial
- lane preserved, exact closure weak
- truth preserved but compressed away
- downstream mostly blind to the real state story
- not enough evidence to judge

Template:

```md
### H1. Downstream Alignment Summary

Part F/G handoff target:
- `...`

Candidate Universe alignment:
- `strong / moderate / weak / absent`

Play Card alignment:
- `strong / moderate / weak / absent`

Lane retention:
- `strong / moderate / weak / absent`

Best one-sentence downstream read:
- `...`

Most important downstream implication:
- `...`
```

---

## H2. Candidate Universe Union And Pack Recall Read

Purpose:
- determine whether the current baseline unbounded pool actually preserved the relevant literal, lane, family, or canonical story

Primary surfaces:
- Candidate Universe JSON / MD
- pack list
- union size
- pack methods and canonicals

Primary questions:
- did Candidate Universe contain the direct winner or winning canonical?
- did it at least contain the right lane, family, or shoulder?
- was there a bounded pack that clearly represented the right story?
- did the pool preserve the truth tightly or only diffusely?

Template:

```md
### H2. Candidate Universe Union And Pack Recall Read

CU union read:
- `direct / lane-family / shoulder-only / diffuse / absent`

Most important preserving packs:
- `...`

Was the state truth preserved tightly or broadly?:
- `tight / moderate / broad / noisy / absent`

Most important Candidate Universe clue:
- `...`
```

---

## H3. Candidate Universe Evidence Provenance And Source-Class Read

Purpose:
- determine what kind of evidence actually carried the preserved truth into Candidate Universe
- prevent accidental crediting of derived-only or downstream-only survival as if it were strong direct evidence

Primary surfaces:
- `candidate_universe_evidence__*.csv`
- `candidate_universe_evidence__*.md`
- source classes:
  - `tool`
  - `control_center`
  - `derived`
  - `other`

Primary questions:
- was the key preserved truth carried by direct tool evidence, control-center context, derived transforms, or a mix?
- was the truth direct-evidence-backed or mostly closure-derived?
- did the provenance match the real upstream explanation of the state?

Template:

```md
### H3. Candidate Universe Evidence Provenance And Source-Class Read

Key provenance class:
- `tool / control_center / derived / mixed / unclear`

Was the preserved truth direct-evidence-backed?:
- `yes/no/mixed`

Most important supporting methods:
- `...`

Most important provenance insight:
- `...`
```

---

## H4. Signals Bundle And Downstream Handoff Adequacy

Purpose:
- judge whether the arena/context layer handed enough of the right state information forward for downstream consumers to have a fair chance

Primary surfaces:
- `signals_bundle*.json`
- arena `downstream_handoff`
- arena `review_links`

Primary questions:
- did the key lane/family/context information actually reach the handoff surface?
- was something important preserved in the arena but not visible to current downstream consumers?
- did the downstream handoff shape itself contribute to compression or blindness?

Template:

```md
### H4. Signals Bundle And Downstream Handoff Adequacy

Downstream handoff adequacy:
- `strong / moderate / weak / absent`

What clearly made it through:
- `...`

What was preserved upstream but poorly surfaced downstream:
- `...`

Most important handoff gap:
- `...`
```

---

## H5. Play Card Budget Squeeze And Retention Read

Purpose:
- inspect what happened when the baseline system was forced to spend a finite budget
- determine whether the key state truth survived the decision-layer squeeze

Primary surfaces:
- Play Card JSON / MD
- strategy
- budget
- ranked candidates
- conversion gate
- VTRAC pack
- reserve behavior when present

Primary questions:
- did Play Card retain the most important state truth?
- did it spend lines in the right lane?
- did budget geometry favor or distort the state story?
- was the miss caused by ranking, lane allocation, or line-depth within lane?

Template:

```md
### H5. Play Card Budget Squeeze And Retention Read

Play Card retention read:
- `direct / lane retained / partial / weak / absent`

Budget posture:
- `appropriate / too tight / too diffuse / misallocated / unclear`

Most important decision-layer behavior:
- `...`

Most important Play Card learning:
- `...`
```

---

## H6. Lane Retention, Exact Closure, And Geometry Diagnosis

Purpose:
- separate “the lane survived” from “the exact box closed”
- identify the geometry-level reason the downstream baseline did or did not finish the job

Primary surfaces:
- glass-box trace
- Candidate Universe grades
- Play Card grades
- lane-allocation reports
- conversion casebooks

Primary questions:
- was the winner lane retained?
- was the exact box or canonical still missed?
- did the downstream layer miss because it lacked:
  - lane breadth
  - lane depth
  - closure conversion
  - doubles-aware geometry
  - or the right final ordering?

Template:

```md
### H6. Lane Retention, Exact Closure, And Geometry Diagnosis

Lane retention:
- `yes/no/mixed`

Exact closure:
- `closed / near / missed`

Geometry diagnosis:
- `lane breadth / lane depth / closure conversion / ordering / mixed / not_applicable`

Most important downstream geometry clue:
- `...`
```

---

## H7. Profile, Strategy, And Ablation Read

Purpose:
- determine whether the downstream result is profile-specific or strategy-specific
- prevent one control-arm posture from being mistaken for a universal downstream truth

Primary surfaces:
- profile under review:
  - `tool_only`
  - `mixed`
  - `profit_only`
- strategy and budget variants when available

Primary questions:
- did another profile or strategy materially express the state better?
- did profit-alert quarantine help or hurt here?
- is this really a downstream structural miss, or mainly a posture choice?

Template:

```md
### H7. Profile, Strategy, And Ablation Read

Profile effect:
- `material / modest / none / unknown`

Strategy effect:
- `material / modest / none / unknown`

Did another posture express the state more honestly?:
- `yes/no/mixed`

Most important profile / strategy insight:
- `...`
```

---

## H8. Bottleneck Classification And Control-Arm Judgment

Purpose:
- classify the most important bottleneck cleanly
- stop the section from ending as a vague “downstream missed”

Helpful bottleneck buckets:
- upstream truth absent
- bounded conversion absent
- Candidate Universe compression
- Play Card squeeze
- lane retained but box missed
- profile / strategy posture
- control arm is simply not expressive enough for this case

Template:

```md
### H8. Bottleneck Classification And Control-Arm Judgment

Main bottleneck:
- `upstream truth absent / bounded conversion absent / CU compression / Play Card squeeze / lane-retained-box-missed / profile-strategy posture / control-arm expressiveness gap / mixed`

How fair is the current control arm to this state?:
- `fair / partly fair / unfair / very limited`

Control-arm judgment:
- `already expresses the state well / partially expresses it / preserves lane but not box / compresses away too much truth / wrong layer for this case`

Most important bottleneck learning:
- `...`
```

---

## H9. Downstream Baseline Handoff

Purpose:
- close Part H with the shortest possible downstream lesson for final synthesis

Template:

```md
### H9. Downstream Baseline Handoff

- Strongest downstream success: `...`
- Strongest downstream miss: `...`
- Most important bottleneck class: `...`
- Best explanation for the miss/hit: `...`
- Main comparison target for Part I: `...`
```

---

## Part H Analyst Guidance

Good Part H outputs:
- separate Candidate Universe from Play Card cleanly
- credit lane retention even when exact closure fails
- distinguish direct evidence from derived-only survival
- identify whether the miss belongs to conversion, selection, budget, or posture
- keep the control arm in its proper role

Bad Part H outputs:
- “Play Card missed, so the analyzers failed”
- “Candidate Universe contained it somewhere, so the baseline worked”
- “derived-only shoulders count the same as direct preservation”
- “one profile is enough to judge all downstream behavior”
- “the baseline is final, so the state must be wrong”

Correct Part H posture:
- control-arm comparison first
- bottleneck diagnosis second
- fairness-to-the-state judgment third
- handoff into final synthesis after that

This is especially important for:
- lane-right / box-miss states
- strong arena states that downstream under-expresses
- states where context is preserved but profit-alert or BA posture is quarantined
- states where line allocation, not evidence absence, appears to be the real issue

---

## Part I — Final Per-State Synthesis

Part I closes the full per-state review.

This is the section where the reviewer should determine:

- what the state actually taught the system
- what Brain 1 preserved correctly
- what the control arm did or did not express
- what should be handed to Brain 2 later
- what deserves future bounded promotion study
- what should explicitly **not** be promoted yet
- what structural follow-up target is most justified

This is not a generic recap.

It is the place where the reviewer should convert the entire review into:

- a clean state verdict
- a Brain 1 lesson
- a Brain 2 handoff
- a promotion / non-promotion judgment
- a structural follow-up target

---

## Part I Inputs

Part I should synthesize:

- Part A winners truth
- Parts B-E tool readings
- Part F arena synthesis judgment
- Part G context judgment
- Part H downstream control-arm judgment

Optional companions:

- bridge / decay readbacks when relevant
- competition / rerank notes when relevant
- board-level crossover notes when results suggest them

Guardrail:
- Part I may infer priorities from earlier sections
- but it should clearly separate:
  - observed
  - interpreted
  - promotable
  - not-yet-promotable

---

## Part I Reading Rules

1. Preserve layer boundaries:
   - winners truth
   - tool evidence
   - arena synthesis
   - context
   - downstream control arm
2. Separate:
   - direct truths
   - lane/family truths
   - composite clues
3. Do not collapse a composite clue into a direct success.
4. Do not propose policy from one interesting case without saying it is provisional.
5. Final synthesis should say both:
   - what the system knew
   - and what it failed to operationalize
6. Brain 2 implications belong here only as a handoff, not a full board-level implementation.
7. Structural follow-up targets should be concrete and sparse, not a dump of every idea.

---

## Part I Output Shape

Part I should end with:

- one final state verdict
- one strongest direct truth
- one strongest lane/family truth
- one strongest composite clue
- one Brain 1 lesson
- one Brain 2 handoff
- one promotion candidate
- one do-not-promote-yet note
- one structural follow-up target

Recommended answer style:

- preserved truth first
- system-layer diagnosis second
- future action third

---

## I0. Final Synthesis Posture And Evidence Lock

Purpose:
- identify which earlier sections drove the final state judgment most strongly
- keep the synthesis tied to evidence instead of impression

Template:

```md
### I0. Final Synthesis Posture And Evidence Lock

Most important earlier sections:
- `Part A / Part B / Part C / Part D / Part E / Part F / Part G / Part H`

Most important artifacts:
- `...`

Confidence in final state synthesis:
- `high / medium / low`

Main reason for that confidence level:
- `...`
```

---

## I1. State Truth Map

Purpose:
- compress the whole state into one clean truth map before making judgments

Primary questions:
- what actually happened?
- what was the strongest structural truth?
- what was the strongest context truth?
- what did downstream actually do with it?

Template:

```md
### I1. State Truth Map

Winner truth:
- `...`

Strongest structural truth:
- `...`

Strongest context truth:
- `...`

Downstream expression of the state:
- `...`

One-sentence state map:
- `...`
```

---

## I2. Preserved Truth Hierarchy

Purpose:
- explicitly rank the different kinds of truth the system preserved

Primary buckets:
- direct preserved truth
- lane/family preserved truth
- composite / relational clue
- hidden or under-surfaced value

Template:

```md
### I2. Preserved Truth Hierarchy

Strongest direct preserved truth:
- `...`

Strongest lane/family preserved truth:
- `...`

Strongest composite clue:
- `...`

Strongest hidden or under-surfaced value:
- `...`
```

---

## I3. Brain 1 Judgment

Purpose:
- state clearly how well the per-state analytical mind performed

Primary questions:
- did the tools preserve the right structure?
- did the arena synthesize it correctly?
- did context reinforce it correctly?

Template:

```md
### I3. Brain 1 Judgment

Tool-layer judgment:
- `strong / moderate / weak / absent`

Arena-synthesis judgment:
- `strong / moderate / weak / absent`

Context-layer judgment:
- `strong / moderate / weak / absent`

Best one-sentence Brain 1 read:
- `...`
```

---

## I4. Downstream Control-Arm Judgment

Purpose:
- summarize, in the shortest clean form, what the current baseline control arm did with the state

Template:

```md
### I4. Downstream Control-Arm Judgment

Candidate Universe judgment:
- `...`

Play Card judgment:
- `...`

Main control-arm bottleneck:
- `...`

Best one-sentence control-arm read:
- `...`
```

---

## I5. Promotion Candidates And Bounded Policy Opportunities

Purpose:
- identify what looks strong enough to justify future bounded promotion study
- keep this distinct from blanket promotion

Primary questions:
- what feature, object, or relation looked repeatedly useful enough to study as policy?
- does it belong in:
  - bounded Brain 1 promotion
  - richer context bridge
  - Brain 2 / final findings
  - or downstream conversion logic?

Template:

```md
### I5. Promotion Candidates And Bounded Policy Opportunities

Best promotion candidate:
- `...`

Likely target layer:
- `Brain 1 bounded promotion / context bridge / Brain 2 / downstream conversion / other`

Why this deserves study:
- `...`

Promotion confidence:
- `high / medium / low / exploratory`
```

---

## I6. Do Not Promote Yet / Residual Risk

Purpose:
- stop the final synthesis from turning every clever observation into policy

Template:

```md
### I6. Do Not Promote Yet / Residual Risk

Interesting but not promotable yet:
- `...`

Why not yet:
- `sample too thin / too composite / too noisy / too costly / not enough recurrence / other`

Main residual risk in interpretation:
- `...`
```

---

## I7. Brain 2 Handoff And Board-Level Implications

Purpose:
- specify what this state should contribute later to board-level ranking, spillover review, and final findings

Primary questions:
- should this state be treated as a clean host, a shared host, an echo, or a composite-interest state?
- is there spillover sensitivity?
- is the state more important as a ranking clue, a shortlist clue, or a final-findings clue?

Template:

```md
### I7. Brain 2 Handoff And Board-Level Implications

Brain 2 posture for this state:
- `clean host / shared host / echo / composite-interest / low-priority`

Spillover / overlap sensitivity:
- `high / medium / low / none`

Most important board-level carry-forward:
- `...`

What Brain 2 should watch for:
- `...`
```

---

## I8. Structural Follow-Up Target

Purpose:
- identify the single most justified system-level follow-up that this state suggests

Helpful target buckets:
- richer arena/context bridge
- deeper context surfacing
- shortlist / recommendation ledger
- decay / episode harness
- Brain 2 relationship layer
- downstream conversion policy
- budget geometry study

Template:

```md
### I8. Structural Follow-Up Target

Best structural follow-up:
- `...`

Target layer:
- `arena/context bridge / heavy-truth surfacing / Brain 2 relationship layer / decay harness / downstream conversion / budget geometry / other`

Why this is the best next follow-up:
- `...`
```

---

## I9. Final Per-State Verdict

Purpose:
- end the review with the shortest, highest-signal conclusion possible

Template:

```md
### I9. Final Per-State Verdict

Final state verdict:
- `...`

If the state was a hit, best explanation:
- `...`

If the state was a miss, best explanation:
- `...`

Most important lesson from this state:
- `...`
```

---

## Part I Analyst Guidance

Good Part I outputs:
- convert the whole review into a real system lesson
- keep direct, lane/family, and composite truths separate
- say what Brain 1 did right even if the control arm failed
- hand something concrete to future Brain 2 work
- nominate at most a few real follow-up targets

Bad Part I outputs:
- “interesting case” with no action
- “promote everything”
- “downstream missed, so nothing worked”
- “Brain 2 should just figure it out later”
- “the case is too complicated to summarize”

Correct Part I posture:
- state truth first
- layer diagnosis second
- promotion / non-promotion judgment third
- Brain 2 and structural handoff fourth

This is especially important for:
- strong Brain 1 / weak control-arm states
- states with high composite value
- states that reveal under-surfaced lists or relationship logic
- states that suggest a real future policy target without proving it completely

---

## Template Status

Current per-state template flow is now:

- `Part A — Winners Environment Lens`
- `Part B — Stable Pattern Extractor`
- `Part C — Digit Reduction`
- `Part D — VTRAC Analyzer`
- `Part E — Hot Zones`
- `Part F — Aggregated Analysis Arena`
- `Part G — Aux / Control Center Context`
- `Part H — Downstream Baseline Comparison`
- `Part I — Final Per-State Synthesis`

Companion workflow:
- `AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- intended for rankings, scoreboard logic, spillover, final findings, and board-wide decision support
