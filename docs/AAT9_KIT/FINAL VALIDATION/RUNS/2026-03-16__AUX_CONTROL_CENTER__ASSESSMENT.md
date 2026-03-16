# Aux + Control Center Assessment

Date: `2026-03-16`

## Executive Read

The current predictive system is too narrow relative to what `Aux` and `Control Center` already know.

That is a design-history issue, not a failure signal.

The narrow predictive-side ingest was a reasonable `v0.2` / early-`v0.3` safety choice for candidate-universe conversion:

- keep only the clearest predictive slices
- avoid exploding packs from noisy compound/context fields
- prove a bounded core first

It should **not** be mistaken for the final analysis-arena contract.

The correct finish for this phase is:

- preserve a much broader structured `Aux + Control Center` evidence layer in the arena
- keep heavy raw artifacts available for review and truth-mining
- avoid collapsing this tool family into tiny direct-caller surfaces

## Why Review Aux + Control Center Together

These are not separate stories.

`Aux` provides:

- positional pressure
- pair / double / sum / VTRAC context
- badge-organized overdue and hot structures
- state-local compound context

`Control Center` provides:

- due doubles
- VTRAC repeat watch
- Blackapple state alerts
- profit alerts
- compound-event promotion / conflict context

Together they form the system's richest non-string-table context layer.

That makes them ideal for a joint arena assessment.

## Core Findings

### 1. Aux already contains much more than the current arena feed preserves

The current predictive Aux summary already carries major evidence classes:

- `positional`
- `pairs`
- `doubles`
- `sums`
- `repeat_watch`
- `vtrac`
- `blackapple`
- `draw_sources`

Representative live artifact:

- `sharepacks/_predictive/2026-03-15/<STATE>/aux/<STATE>/summary.json`

But the current predictive arena consumption largely preserves only:

- positional shortlist
- VTRAC overdue overlay top
- a compact badge-pressure index surface

That is too narrow for the analysis arena.

### 2. Current narrowness was a selection-layer decision, not an arena truth decision

The current candidate-universe path emphasizes:

- `aux_positional`
- `aux_vtrac_index_overdue`
- `mirror_pair_closure`
- `due_doubles`
- limited badge-pressure extraction

That was useful for bounded predictive conversion.

It is **not** the right final contract for the arena, whose job is evidence preservation and inspection before later ranking/conversion policy.

### 3. Badge pressure is under-preserved, not disproven

The history and harness docs are consistent:

- badge pressure has real value
- VTRAC-index badge pressure is often more useful than raw literal badge rows
- the full boxed VTRAC badge matrix is analytically richer than the current compact predictive feed

Important conclusion:

- the current system does not yet preserve badge structure richly enough to let the arena determine what is most predictive

The likely right finish is:

- keep a compact arena-facing badge-pressure object
- also preserve a path to the heavier full badge matrix / boxed VTRAC tables for deep review

### 4. Positional tracker is more valuable as pressure/context than as a literal caller

The timeline and task notes strongly suggest:

- positional hard-due and shortlist signals matter
- positional tracker helps identify where structure is concentrating
- its best value is as context and corridor support, not as a tiny top-caller

That means the arena should preserve:

- hard-due digits
- shortlist families
- positional breadth
- currentness / multi-variant repetition

not just a short literal candidate list.

### 5. Due doubles and pair-space trackers are first-class regime context

The due-doubles work should not be treated as a small add-on.

It is one of the clearest ways the system detects:

- double drought
- family pressure
- mirror-pair closure
- double-led regime type

The arena should preserve both:

- literal due-double families
- VTRAC / mirror-linked double context

This is especially important because competitions repeatedly showed doubles and mirror-doubles behaving as a distinct predictive regime.

### 6. Profit Alerts are much richer than the current narrow ingest suggests

`profit_alerts.csv` already contains:

- alert identity
- strength
- suggested combinations
- badges
- canonical
- implied set
- evidence JSON

`profit_compound_events.csv` already contains:

- state-level compound-event summaries
- promotion / conflict tags
- priority
- supporting alert ids
- watchlist tags

That means the current narrow predictive usage leaves a lot of structured value unused.

For the arena, profit alerts should contribute:

- alert density
- alert breadth
- supported families / canonicals / indices
- compounded state context
- attached candidate literals for comparison against string-table clusters

### 7. Blackapple is also being under-preserved

The current artifacts already expose:

- state status
- BA score
- triggers
- number of candidates
- examples
- per-variant alert context in Aux summary

That is valuable arena context even if Blackapple is not a tiny same-day caller.

The arena should preserve:

- state alert status
- trigger mix
- candidate-family / candidate-literal examples
- variant profile

### 8. VTRAC repeat watch and repeat trackers are strong context objects

`vtrac_repeat_watch.csv` contains:

- current index
- current streak
- heat index
- heat hazard
- last repeat
- max streak

These are classic environment/regime descriptors.

They belong in the arena as context, not as a tiny conversion filter.

### 9. The right posture is broad structured preservation, not a blind raw dump

The user concern is correct:

- it is better to go broader at the arena stage than to prematurely narrow away useful compound context

But a raw dump of every Aux and Control Center table is still not the optimal contract.

The better finish is:

- preserve richer structured evidence objects
- keep heavy artifacts linked / inspectable
- let later arena scoring determine what matters most

That is different from:

- flattening everything into current top-Ns
- or blindly dumping every raw cell into the arena

## Current Predictive Artifacts Worth Preserving

### Aux predictive-side SSOT

- `sharepacks/_predictive/<D>/<STATE>/aux/<STATE>/summary.json`

Most useful subtrees:

- `positional`
- `pairs`
- `doubles`
- `sums`
- `repeat_watch`
- `vtrac`
- `blackapple`

### Control Center predictive-side SSOT

- `sharepacks/_predictive/<D>/control_center/due_doubles.csv`
- `sharepacks/_predictive/<D>/control_center/vtrac_repeat_watch.csv`
- `sharepacks/_predictive/<D>/control_center/blackapple_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_compound_events.csv`
- `sharepacks/_predictive/<D>/control_center/meta.json`

## What The Arena Should Preserve

At a high level, the arena should carry:

- positional pressure
- VTRAC pressure
- badge pressure
- pair / double family context
- due-double regime context
- repeat-watch context
- sums / root-sum context
- Blackapple state context
- profit-alert context
- compound-event context

The exact contract is defined in:

- `2026-03-16__AUX_CONTROL_CENTER__ARENA_CONTRACT.md`

## What Should Remain Heavy / Linked

These artifacts likely should stay available as linked heavy context rather than be flattened aggressively:

- full boxed VTRAC badge matrix / tables
- raw badge rows by pair / combo / variant
- full pair-status tables
- full Blackapple candidate ledgers
- full profit-alert evidence JSON

The arena should preserve compact structured summaries **plus** a path back to these artifacts.

## Final Judgment

`Aux + Control Center` is the clearest remaining example of:

- current predictive consumption being narrower than the tool family's real value

The favorable read is:

- the evidence is already there
- the system does not need a broad underlying Aux rewrite to expose it
- the next correct move is an arena-contract/export decision, not another small direct-caller tuning cycle

## Assessment Call

The right next phase for `Aux + Control Center` is:

1. formalize the broad arena contract
2. keep current narrow candidate-universe usage separate from that contract
3. implement one bounded export/wiring slice later if approved
4. then freeze tool-local tuning and move to aggregated arena analysis
