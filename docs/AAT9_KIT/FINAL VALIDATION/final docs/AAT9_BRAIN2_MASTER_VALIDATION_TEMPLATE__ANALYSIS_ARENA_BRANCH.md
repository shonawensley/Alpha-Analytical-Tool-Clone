# AAT9 Brain 2 Master Validation Template — Analysis Arena Branch

Date: `2026-03-26`

## Purpose

This is the board-level Master Validation companion for the analysis-arena
branch.

It exists to review a gold day from the full-day, across-states, aggregate
perspective after:

- per-state Master Validation work exists
- Brain 2 runtime artifacts exist
- results truth exists

Use this template to answer:

- how good was the board scoreboard and ranking?
- how much of the day's real power lived in shared complexes across states?
- which aggregate trackers mattered?
- how well did due doubles, mirror doubles, profit alerts, compound events,
  and Blackapple actually perform?
- what did Brain 2, shadow DPL, and the control arm preserve or suppress?
- what should later translators and budgeting eventually learn from this day?

This template is not:

- the pre-results Brain 2 operating template
- final combination forming
- final budgeting/waging logic

The clean split is:

- per-state Master Validation template =
  `Brain 1 + post-results deep learning per state`
- Brain 2 runtime template =
  `board review, ranking, and operating posture`
- Brain 2 Master Validation template =
  `post-results aggregate reverse-engineering and scoreboard learning`

---

## Governing Principle

The most important Brain 2 Master Validation rule is:

- **grade the board as a board, not as five isolated state reports**

That means this template should:

- compare ranking against actual board truth
- study cross-state carryover and shared complexes
- measure the aggregate trackers across the whole day
- separate host states from echoes
- preserve what the board learned before later translator and budgeting work

It should not:

- redo the full per-state deep truth read from scratch
- collapse back into only one state's story
- pretend control-arm outputs are the arena branch's truth
- force exact combination logic where only aggregate learning is justified

---

## Relationship To Other Layers

### Brain 1

Brain 1 remains the per-state truth engine.

This template assumes Brain 1 already answered:

- what local state truth existed
- what the arena preserved
- what context mattered
- what the state-level downstream comparison showed

### Brain 2 Runtime

The runtime Brain 2 layer already emits:

- board review bundle
- board scoreboard
- spillover overlay
- shadow DPL summary

This template grades those artifacts after results.

### Brain 2A / Control Center

Control Center remains the state-local aggregate/event layer, but this
template also reads its full-day tables when needed:

- profit alerts
- compound events
- due doubles
- Blackapple
- repeat / tracker boards

### Translation Sandbox

This template should use translation sandbox artifacts as a learning surface,
not as active translator proof.

### Control Arm

Candidate Universe / Play Card / B12-B24-B36 remain:

- downstream baseline/control-arm outputs
- useful for comparison
- not the definition of arena truth

---

## Scope Model

This template has two scopes and should say which scope each section uses.

### Board Scope

Use when grading:

- board scoreboard
- ranked states
- spillover
- shadow DPL
- board roles
- translation sandbox board-learning

### Full-Day Tracker Scope

Use when grading:

- due doubles across all states
- Blackapple states outside the top board
- profit alerts / compound events across the day
- all daily doubles and mirror doubles

This distinction is mandatory.

Some of the most important aggregate lessons will come from states that were
not the top Brain 2 targets.

---

## Inputs

Primary board-runtime inputs:

- `board_review_bundle__*.md/.json`
- `board_scoreboard__*.md/.json`
- `board_spillover_overlay__*.md/.json`
- `shadow_decision_policy__*.md/.json`
- translation sandbox day manifest

Primary state-level inputs:

- completed per-state Master Validation summaries when available
- per-state Part I outputs
- per-state aggregated analysis arenas
- per-state translation sandbox seeds

Primary full-day raw inputs:

- predictive sharepack control-center tables
- predictive sharepack aux summaries
- winners / results truth for the full day

Important sharepack reminder:

- the sharepack remains the frozen day snapshot
- Brain 2 receipts are derived aggregate/runtime artifacts on top of that
- this template should lock both when reviewing a day

Suggested raw tables to lock when present:

- `sharepacks/<D>/control_center/profit_alerts.csv`
- `sharepacks/<D>/control_center/compound_events.csv`
- `sharepacks/<D>/control_center/due_doubles*.csv`
- Blackapple summary artifacts under predictive state folders
- repeat-watch / tracker artifacts if exported

---

## Reading Rules

1. Start from actual day truth, not only scoreboard rank.
2. Grade the board as a whole, not one state at a time.
3. Separate:
   - board scope
   - full-day tracker scope
4. Distinguish:
   - host value
   - echo value
   - carryover/shared-complex value
   - tracker-only value
5. Grade due doubles twice:
   - ranked-table performance
   - all actual doubles/mirror doubles on the day
6. Do not let one exact-hit outcome erase a structurally correct board read.
7. Do not let one tracker-rich state rewrite the whole board if it was only
   weakly supported elsewhere.
8. Use translation sandbox learning capture to preserve future translator
   value, not to pretend translators already exist.
9. Keep budgeting out of scope.

---

## Output Shape

A good Brain 2 Master Validation report should end with:

- one board-outcome map
- one scoreboard/ranking verdict
- one cross-state shared-complex verdict
- one aggregate-tracker verdict
- one doubles/mirror-doubles verdict
- one shadow-DPL verdict
- one translation-learning handoff
- one control-arm comparison
- one final promotion / follow-up target

---

## Part A — File Lock And Scope

Purpose:

- lock the exact board/runtime/sharepack truth being reviewed
- separate board-scope vs full-day tracker-scope inputs

Template:

```md
### Part A — File Lock And Scope

- Results date: `...`
- Review mode: `post-results`
- Target draw focus: `midday / evening / full-day`

Board artifacts used:
- board review bundle: `...`
- board scoreboard: `...`
- board spillover overlay: `...`
- shadow DPL: `...`
- translation sandbox day manifest: `...`

Per-state artifacts consulted:
- `...`

Full-day sharepack tracker artifacts consulted:
- `...`
- `...`
- `...`

Scope notes:
- board scope states: `...`
- full-day tracker scope coverage: `all states / subset`
- any missing board/tracker artifacts: `...`
```

---

## Part B — Board Outcome Map

Purpose:

- map the actual day outcome before grading the board
- show which states actually carried the day structurally

Primary questions:

- which states converted meaningful truth?
- which states produced the actual strongest structural receipts?
- which board states were real hosts vs mostly echoes?
- did the day actualize one shared pending complex across multiple states?

Template:

```md
### Part B — Board Outcome Map

Actual strongest day states:
1. `STATE` — `why`
2. `STATE` — `why`
3. `STATE` — `why`

States that actually converted meaningful structure:
- `...`

States that were mostly echo / shoulder / ambient only:
- `...`

Day-level structural class:
- `single clean host / shared pending complex / split board / tracker-rich mixed day / other`

Most important truth-side board insight:
- `...`
```

---

## Part C — Scoreboard And Ranking Evaluation

Purpose:

- evaluate the aggregate scoreboard and rankings against actual outcomes

Mandatory questions:

- where did actual converting states rank?
- did `top_primary_target` convert?
- did `secondary_target` convert?
- did `best_clean_host` deserve the label?
- did `highest_context_support_state` matter?
- were `tight_core`, `watch_only`, and `echo_only` buckets appropriate?
- did overlap penalties suppress a true host?

Template:

```md
### Part C — Scoreboard And Ranking Evaluation

Top scoreboard rows that mattered:
- `...`

Highest-converting actual state rank(s):
- `...`

Board verdict field checks:
- top_primary_target: `correct / mixed / poor`
- secondary_target: `correct / mixed / poor`
- best_clean_host: `correct / mixed / poor`
- highest_context_support_state: `correct / mixed / poor`

Bucket quality:
- tight_core: `...`
- watch_only: `...`
- echo_only: `...`

Did the scoreboard ranking help or distort the day?:
- `...`

Most important scoreboard lesson:
- `...`
```

---

## Part D — Shared Complexes, Carryover, And Spillover

Purpose:

- grade the advanced Brain 2 value of cross-state shared pending complexes

Primary questions:

- did the day contain one or more shared pending complexes?
- was a lane/family/VTRAC/double complex strongly pending across several top
  states?
- did one state actualize a pattern that was visibly live across multiple top
  states?
- should the board have treated the complex more globally?

Template:

```md
### Part D — Shared Complexes, Carryover, And Spillover

Most important shared complexes:
- `STATE A / STATE B / STATE C` — `shared lane/family/double/VTRAC/alert complex`

Most important host state:
- `...`

Most important echo state:
- `...`

Most important cross-state carryover receipt:
- `...`

Did the board correctly treat the day as a shared pending complex?:
- `yes / partly / no`

Most important spillover lesson:
- `...`
```

---

## Part E — Aggregate Tracker Inventory

Purpose:

- inventory the board-wide tracker posture before drilling into specific tables

Primary surfaces:

- profit alerts
- compound events
- Blackapple
- due doubles
- repeat / VTRAC tracker posture

Template:

```md
### Part E — Aggregate Tracker Inventory

Most important board-scope tracker states:
- `...`

Most important full-day tracker states outside the board:
- `...`

Aggregate tracker posture:
- profit alerts: `...`
- compound events: `...`
- Blackapple: `...`
- due doubles: `...`
- repeat / tracker: `...`

Did tracker posture materially explain the day?:
- `yes / mixed / no`

Most important aggregate-tracker insight:
- `...`
```

---

## Part F — Profit Alerts And Special Compound Events

Purpose:

- evaluate alert tables and special compound-event tracking at the board level

Mandatory questions:

- which states had the strongest alert posture?
- which alert IDs mattered?
- which implied sets converted?
- which states had special compound events?
- did alert-rich states become real board targets, useful echoes, or noise?
- did alert relationships create meaningful cross-state receipts?

Template:

```md
### Part F — Profit Alerts And Special Compound Events

Highest-value alert states:
- `...`

Most important alert IDs:
- `...`

Implied-set conversions:
- `...`

Most important special compound events:
- `...`

Alert-rich but structurally weak states:
- `...`

Did profit alerts / compound events materially improve Brain 2?:
- `yes / mixed / no`

Most important alert-layer lesson:
- `...`
```

---

## Part G — Blackapple Board Review

Purpose:

- evaluate Blackapple across the day, especially `WATCH` and `ALERT` states

Mandatory questions:

- which states were `OFF / WATCH / ALERT`?
- for `ALERT` states, did recommended combinations get preserved?
- did BA recommendations convert directly, indirectly, or not at all?
- did BA alert states outperform board expectations?
- were there important BA states outside the top board?

Template:

```md
### Part G — Blackapple Board Review

BA `ALERT` states:
- `...`

BA `WATCH` states that mattered:
- `...`

Important BA recommendation carries:
- `...`

States where BA looked stronger than the board gave credit for:
- `...`

Did BA function mainly as:
- `host indicator / echo amplifier / shortlist helper / noise / mixed`

Most important BA lesson:
- `...`
```

---

## Part H — Due Doubles Ranked-State Evaluation

Purpose:

- evaluate the ranked due-doubles board/table against the day's outcomes

Scope rule:

- include all states with `draws_since_double >= 3`
- treat double and mirror-double actualization as valid tracked outcomes

Mandatory questions:

- how did the top due states perform?
- how did states at the `3 draws missing double` threshold perform?
- which due families / examples converted?
- was conversion literal double, mirror double, or related-family pressure?

Template:

```md
### Part H — Due Doubles Ranked-State Evaluation

Ranked due states reviewed (>= 3 draws missing double):
- `...`

Top due states that converted:
- `...`

Top due states that failed:
- `...`

Threshold states (`3 draws missing`) that converted:
- `...`

Important due families / examples that converted:
- `...`

Conversion class:
- literal double: `...`
- mirror double: `...`
- related-family / pressure conversion: `...`

Most important due-doubles ranking lesson:
- `...`
```

---

## Part I — All Daily Doubles And Mirror Doubles Evidence Audit

Purpose:

- evaluate all actual daily doubles / mirror doubles, even outside the due
  rankings

Mandatory questions:

- what were all doubles / mirror doubles for the day?
- what evidence existed for each one?
- was the evidence strong, medium, or weak?
- what kind of evidence supported them?

Suggested evidence grade rubric:

- `strong`
  - due-double posture plus at least two meaningful reinforcements
- `medium`
  - due-double posture or mirror-double posture plus one meaningful
    reinforcement
- `weak`
  - mostly hindsight-visible or only shallowly supported

Template:

```md
### Part I — All Daily Doubles And Mirror Doubles Evidence Audit

Daily doubles / mirror doubles reviewed:
- `STATE` — `result` — `double / mirror double` — evidence `strong / medium / weak`
- `STATE` — `result` — `...`

Support sources used:
- due-doubles board: `...`
- arena dominant clusters: `...`
- positional / BA / profit alerts / survivor / consensus: `...`

Most important strong-evidence double:
- `...`

Most important weak-evidence double:
- `...`

Most important doubles / mirror-doubles lesson:
- `...`
```

---

## Part J — Shadow DPL And Board Posture Evaluation

Purpose:

- grade shadow DPL as the aggregate posture bridge

Primary questions:

- did `PLAY / WATCH / SKIP` behave intelligently?
- did `mode` look sensible?
- did `cap_class` look too timid, too loose, or about right?
- were reason codes aligned with actual board truth?
- did DPL correctly separate hosts from echoes?

Template:

```md
### Part J — Shadow DPL And Board Posture Evaluation

Play states:
- `...`

Watch states that should maybe have been play:
- `...`

Play states that were overpromoted:
- `...`

Mode / cap quality:
- `...`

Most important useful reason codes:
- `...`

Most important misleading reason codes:
- `...`

Most important DPL lesson:
- `...`
```

---

## Part K — Translation Sandbox / Combination Learning Capture

Purpose:

- capture near-final combination intelligence without claiming active
  combination logic exists yet

Primary questions:

- what boxed themes repeated across top states?
- what straight themes existed, if any?
- what VT-box themes were clearly stronger than literal closure?
- which shortlist surfaces carried through across multiple states?
- what did the board preserve that the control arm compressed away?

Template:

```md
### Part K — Translation Sandbox / Combination Learning Capture

Strongest boxed themes across the day:
- `...`

Strongest straight themes across the day:
- `...`

Strongest VT-box themes across the day:
- `...`

Most important repeated shortlist carries:
- positional: `...`
- Blackapple: `...`
- profit-alert implied clusters: `...`
- due-double family carries: `...`

Most important preserved-not-budgeted cluster:
- `...`

Strongest translator-learning note:
- `...`
```

---

## Part L — Control-Arm Comparison

Purpose:

- compare the arena branch against the current downstream baseline/control arm

Primary questions:

- what did Candidate Universe preserve?
- what did Play Card keep or cut?
- where did B12/B24/B36 still help?
- where did the control arm suppress real arena truth?

Guardrail:

- this section is comparative only
- do not let it redefine the board truth already established above

Template:

```md
### Part L — Control-Arm Comparison

Control-arm outputs reviewed:
- Candidate Universe: `...`
- Play Card: `...`
- B12/B24/B36 behavior: `...`

Most important control-arm success:
- `...`

Most important control-arm suppression:
- `...`

Did the control arm outperform, underperform, or mostly lag Brain 2 truth?:
- `...`

Most important control-arm lesson:
- `...`
```

---

## Part M — Final Board Lessons And Promotions

Purpose:

- end with the aggregate lessons that should shape the branch

Template:

```md
### Part M — Final Board Lessons And Promotions

Strongest board-level insight:
- `...`

Strongest tracker insight:
- `...`

Strongest cross-state carryover insight:
- `...`

Strongest doubles / mirror-doubles insight:
- `...`

Strongest translation-learning insight:
- `...`

One thing that deserves later promotion:
- `...`

One thing that should remain research-only for now:
- `...`

One structural follow-up target:
- `...`

One thing to watch on the next fresh runs:
- `...`
```

---

## Recommended Companion Docs

- `AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- `AAT9_DECISION_POLICY_LAYER__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md`

---

## Status

This document is the post-results aggregate-learning companion for the current
analysis-arena branch.

It should be used:

- after per-state Master Validation work
- after Brain 2 board receipts exist
- before later translator and budgeting work is promoted
