# AAT9 Brain 2 Template — Analysis Arena Branch

Date: `2026-03-23`

## Purpose

This is the companion board-level template for the analysis-arena branch.

Its job is to review the board as a whole after per-state Brain 1 work exists.

Use it to answer:

- which states are truly strongest today?
- which states are duplicating the same family complex?
- which family complexes already fired?
- which states still hold the cleanest unspent host for the next draw?
- what should be handed to future combination forming and budgeting?

This template is not a replacement for the per-state Master Validation template.

The clean split is:

- per-state template = `Brain 1 + post-results deep learning per state`
- Brain 2 template = `board-level comparison, ranking, spillover, and final findings`

---

## Governing Principle

The most important Brain 2 rule is:

- **reduce board noise without destroying real overlap structure**

That means Brain 2 should:

- compare strong states against each other
- detect shared lanes and shared family complexes
- rank states honestly
- separate clean hosts from shared hosts and echoes
- preserve direct, lane/family, and composite relationships

It should **not**:

- replace Brain 1 local truth
- invent state-local evidence that does not exist
- treat every cross-state echo as a reason to widen every pack
- jump straight into budget mechanics without a clean final-findings layer

---

## Relationship To Other Layers

### Brain 1

Brain 1 is the per-state analytical mind.

It provides:

- tool truth
- arena synthesis
- context reinforcement
- state-level Part I verdicts

### Brain 2A / Control Center

Control Center is best understood as `Brain 2A`.

It already contributes:

- board-style trackers
- alert tables
- state-local aggregate context

But it is still mostly state-local and event-oriented.

The fuller Brain 2 layer is `Brain 2B`, the board-level comparative mind above it.

### Decision Policy Layer

Brain 2 does not directly form combinations.

Its outputs should feed a later Decision Policy Layer that decides:

- `PLAY / WATCH / SKIP`
- `mode`
- `cap class`
- `translator route`

That keeps board review separate from later translation and later budgeting.

### Master Validation

Master Validation teaches Brain 2:

- which cross-state overlaps are real
- which spillovers matter
- which composite relationships recur
- which ranking and final-findings rules deserve later promotion

---

## Brain 2 Modes

This template can be used in 3 board modes:

1. `Pre-day predictive board`
- before any results
- rank states and identify duplicate complexes

2. `Midday -> Evening rerank`
- after Midday, before Evening
- classify spent vs unspent families
- rerank states accordingly

3. `Post-results board review`
- after results exist
- learn what Brain 2 missed or overcounted

The reviewer should always state which mode they are in before using the template.

---

## Inputs

Primary per-state inputs:

- completed per-state Master Validation summaries when available
- per-state Part I outputs
- per-state aggregated arena JSON/MD
- per-state Aux / Control Center context surfaces
- per-state downstream/control-arm summaries when needed

Primary board-level inputs:

- competition memo / board memo
- ranked-state notes
- cross-state crossover / spillover ledgers
- any state-day or review scoreboards relevant to the board
- Control Center cross-state boards:
  - due doubles
  - VTRAC repeat watch
  - Blackapple alerts
  - profit alerts
  - compound events

Future runtime inputs when they exist:

- `board_spillover_overlay__*.json`
- `board_spillover_overlay__*.md`
- final findings relationship artifacts
- dedicated ranking scoreboards

Current runtime companion:

- `scripts/tools/build_board_spillover_overlay.py`
- `scripts/tools/create_board_scoreboard.py`
- `scripts/tools/create_board_review_bundle.py`
- `scripts/tools/create_day_arena_board_review.py`
- first live receipt:
  - `2026-03-21__BOARD_SPILLOVER_OVERLAY__competition8_evening_rerank_after_midday.md`
  - `2026-03-21__BOARD_SCOREBOARD__competition8_evening_rerank_after_midday.md`
  - `2026-03-21__BOARD_REVIEW_BUNDLE__competition8_evening_rerank_after_midday.md`

Guardrail:
- Brain 2 should prefer compact top surfaces and per-state conclusions
- not every raw row from every tool

---

## Reading Rules

1. Start from the best per-state truths already established in Brain 1.
2. Compare states as a board, not as isolated prediction islands.
3. Separate:
   - state strength
   - overlap duplication
   - spent families
   - unspent cores
   - direct vs lane/family vs composite value
4. If 2 states are carrying the same family complex, say so explicitly.
5. Do not count a shared family complex as two independent edges.
6. Treat Midday consumption as a board event, not just a per-state event.
7. Use Brain 2 to narrow intelligently, not widen by anxiety.
8. Do not let composite clues outrank direct local truth without saying so explicitly.
9. Preserve the distinction between:
   - board analysis
   - decision policy
   - final findings
   - combination forming
   - budgeting

---

## Output Shape

A good Brain 2 review should end with:

- one ranked-state table
- one overlap / spillover assessment
- one spent-vs-unspent board read
- one set of state roles
- one final-findings handoff
- one structural follow-up target

Recommended answer style:

- ranked states first
- shared-complexes and spillover second
- state roles and targeting posture third
- final-findings / structural handoff fourth

---

## Part A — Board File Lock And Mode

Purpose:
- lock the exact board, date, and review mode
- prevent drift between per-state conclusions, board artifacts, and results-state updates

Template:

```md
### Part A — Board File Lock And Mode

- Board date: `...`
- Board mode: `pre-day / midday-rerank / post-results`
- Target draw: `...`
- States on board:
  - `...`
  - `...`
  - `...`

Primary board artifacts used:
- `...`
- `...`

Per-state summaries available?:
- `all / most / some / none`

Midday truth available?:
- `yes/no`

If yes, truth source:
- `...`

Board spillover overlay available?:
- `yes/no`

If no, replacement review surface:
- `competition ledger / manual overlap table / other`
```

---

## Part B — Ranked States And Board Triage

Purpose:
- establish the board ranking before overlap logic starts collapsing duplicates
- keep the board readable as a day-level decision problem

Primary questions:
- which states are strongest on their own local truth?
- which states deserve serious attention?
- which states are clearly weak?
- which states are carrying meaningful survivor / frontier / last-remaining posture?
- how confident is the board in each rank?

Template:

```md
### Part B — Ranked States And Board Triage

Ranked states:
1. `STATE` — `why`
2. `STATE` — `why`
3. `STATE` — `why`
4. `STATE` — `why`
5. `STATE` — `why`

Tiering:
- Tier 1: `...`
- Tier 2: `...`
- Tier 3: `...`

Board confidence:
- `high / medium / low`

Most important reason for this ranking:
- `...`
```

---

## Part C — Board Tracker Snapshot

Purpose:
- read the cross-state aggregate tracker posture without redoing the full per-state context audit
- identify which states are carrying the strongest board-level tracker pressure

Primary surfaces:

- due doubles board
- VTRAC repeat-watch board
- Blackapple board
- profit alerts board
- compound events board

Primary questions:
- which states have the strongest tracker pressure?
- which states have BA `ALERT` / `WATCH`?
- which states have strong due-double posture?
- which states have notable alert clusters?
- which states look tracker-rich but structurally weaker?

Template:

```md
### Part C — Board Tracker Snapshot

States with strongest tracker posture:
- `...`

Most important board tracker clusters:
- Due doubles: `...`
- BA status: `...`
- Profit alerts / compounds: `...`
- Repeat / VTRAC tracker: `...`

Did tracker pressure materially support the ranking?:
- `yes/no/mixed`

Most important board-tracker insight:
- `...`
```

---

## Part D — Shared Complexes, Overlap, And Spillover

Purpose:
- identify which states are carrying the same lane/family complexes
- make overlap visible before it silently distorts ranking confidence

Primary questions:
- which states share a VTRAC lane?
- which states share a box family?
- which states share alert-implied sets or context families?
- which states are echoing the same survivor-rich or hidden-terminal complex?
- where is the board most duplicated?

Helpful relationship classes:

- `direct-local`
- `direct-cross-state`
- `lane/family`
- `composite`

Template:

```md
### Part D — Shared Complexes, Overlap, And Spillover

Strongest shared complexes:
- `STATE A <-> STATE B` — `shared lane/family`
- `STATE A <-> STATE B` — `shared alert / context`

Biggest overlap risk:
- `...`

Most important spillover-sensitive state pair:
- `...`

Relationship class distribution:
- direct-local: `...`
- direct-cross-state: `...`
- lane/family: `...`
- composite: `...`

Most important overlap insight:
- `...`
```

---

## Part E — Spent Versus Unspent Family Read

Purpose:
- determine what the board already consumed and what still looks live
- this is especially important in Midday -> Evening reranks

Primary questions:
- which local cores already fired?
- which families fired cross-state?
- which survivor-rich cores still look structurally unspent?
- which states remain clean hosts for the next draw?
- which states are mostly echoes after consumption?

Template:

```md
### Part E — Spent Versus Unspent Family Read

States with clearly spent cores:
- `...`

States with mostly unspent cores:
- `...`

Cross-state spent families:
- `...`

Best clean host after consumption:
- `...`

Most important spent/unspent insight:
- `...`
```

---

## Part F — Final Findings Relationship Classification

Purpose:
- convert the board into a usable relationship view before combination forming
- preserve direct, lane/family, and composite value cleanly

Primary questions:
- which findings are direct?
- which are lane/family only?
- which are composite but still meaningful?
- which states mainly contribute relationships rather than primary host value?

Template:

```md
### Part F — Final Findings Relationship Classification

Direct-local findings:
- `...`

Direct-cross-state findings:
- `...`

Lane/family findings:
- `...`

Composite findings:
- `...`

Most important relationship-layer insight:
- `...`
```

---

## Part G — State Roles And Targeting Posture

Purpose:
- assign each state a board role instead of treating all ranked states the same

Helpful state roles:

- `clean host`
- `shared host`
- `echo`
- `composite-interest`
- `low-priority`

Primary questions:
- which state is the cleanest host?
- which state is strong but duplicated?
- which state is useful only as a shoulder or relationship clue?
- which states should be deprioritized?

Template:

```md
### Part G — State Roles And Targeting Posture

State roles:
- `STATE` — `clean host / shared host / echo / composite-interest / low-priority`
- `STATE` — `...`
- `STATE` — `...`

Best primary target state:
- `...`

Best secondary target state:
- `...`

State that should mainly be treated as an echo or shoulder source:
- `...`

Most important targeting insight:
- `...`
```

---

## Part H — Pre-Combination Handoff

Purpose:
- hand the board to later final findings / combination forming without pretending combination geometry is already solved here

Primary questions:
- what should later pack-building pay attention to?
- what should be tight core only?
- what should only be a small shoulder?
- what should remain watch-only?

Template:

```md
### Part H — Pre-Combination Handoff

Tight-core states:
- `...`

States deserving only small shoulders:
- `...`

Watch-only / clue-only states:
- `...`

Most important findings for later combination forming:
- `...`

Most important thing to avoid:
- `...`
```

---

## Part I — Structural Gaps And Runtime Overlay Needs

Purpose:
- identify what the current board workflow still lacks structurally
- keep the review tied to real future implementation targets

Helpful target buckets:

- board spillover overlay
- shared-lane/shared-family matrix
- spent/unspent family table
- final findings board ledger
- ranking scoreboard
- shortlist/recommendation carry-forward ledger
- decay / episode tracking for board-level alerts

Template:

```md
### Part I — Structural Gaps And Runtime Overlay Needs

Most important missing board artifact:
- `...`

Best runtime overlay target:
- `board spillover overlay / final findings ledger / spent-unspent table / ranking scoreboard / shortlist carry-forward ledger / other`

Most important measurement gap:
- `...`

Why this is the next best Brain 2 follow-up:
- `...`
```

---

## Part J — Final Board Verdict

Purpose:
- end the board review with the shortest high-signal statement possible

Template:

```md
### Part J — Final Board Verdict

Final board read:
- `...`

Best clean host:
- `...`

Biggest overlap / spillover risk:
- `...`

Strongest composite-interest state:
- `...`

Best structural next step:
- `...`
```

---

## Brain 2 Analyst Guidance

Good Brain 2 outputs:

- rank states before overfitting overlap logic
- expose duplicated family complexes clearly
- treat cross-state spillover as a board phenomenon, not a local bug
- separate clean hosts from echoes
- preserve composite findings without inflating them into direct hits
- hand something concrete to later combination forming

Bad Brain 2 outputs:

- “all top states are independently strong”
- “spillover means widen everything”
- “composite clues count the same as direct local truth”
- “Brain 2 should directly decide exact budgets already”
- “one strong local state means the board is solved”

Correct Brain 2 posture:

- ranking first
- overlap reduction second
- spent/unspent diagnosis third
- final findings handoff fourth

This is especially important for:

- double-heavy boards
- mirror-heavy boards
- boards where 2 or more states share the same small lane complex
- Midday -> Evening reranks
- boards where the right family appears, but in the neighboring strong state

---

## Recommended Companion Docs

This template works best alongside:

- `AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
- `AAT9_FINAL_FINDINGS_RELATIONSHIP_LAYER__ARENA_BRANCH.md`
- live competition memos
- crossover / spillover ledgers

---

## Status

This Brain 2 template is a review and operating template.

It is **not** the runtime Brain 2 overlay itself.

The first runtime companion now exists:

- `scripts/tools/build_board_spillover_overlay.py`

Current posture:

- the overlay is `v0`
- useful now for board-level readback and spillover receipts
- the scoreboard consumer is now available as a compact Brain 2 handoff
- the board review bundle is now the cleanest one-step Brain 2 entrypoint
- the day-level orchestration path now exists, so rebuilding Brain 1 arenas and emitting the Brain 2 bundle can happen in one canonical workflow
- richer context hints are now preserved in the board runtime, including Blackapple recommendations, positional notes, compound events, and due-double family examples
- still not the final ranking/autopilot object
- still expected to evolve before it feeds later final findings and combination forming directly

The intended progression is:

1. use this template to review boards consistently
2. refine the spillover overlay, scoreboard, and board bundle from repeated board findings
3. then connect the refined objects to future final findings, combination forming, and budgeting
