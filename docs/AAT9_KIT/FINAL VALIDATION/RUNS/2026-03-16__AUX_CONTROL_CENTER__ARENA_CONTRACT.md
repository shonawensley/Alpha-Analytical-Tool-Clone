# Aux + Control Center Arena Contract

Date: `2026-03-16`

## Purpose

Define what `Aux` and `Control Center` should contribute to the analysis arena after the final tool-review phase.

This is a tool-to-arena contract.

It is **not**:

- a candidate-universe contract
- a play-card contract
- a final budget/conversion contract

## Shared Principle

`Aux + Control Center` should feed the arena as:

- structured context
- compound pressure
- regime descriptors
- lane / family support objects

They should **not** be reduced to only the tiny subset that was safest for early candidate-universe conversion.

## Primary Predictive-Side Ingest

### Aux SSOT

- `sharepacks/_predictive/<D>/<STATE>/aux/<STATE>/summary.json`

Primary subtrees to preserve:

- `positional`
- `pairs`
- `doubles`
- `sums`
- `repeat_watch`
- `vtrac`
- `blackapple`

### Control Center SSOT

- `sharepacks/_predictive/<D>/control_center/due_doubles.csv`
- `sharepacks/_predictive/<D>/control_center/vtrac_repeat_watch.csv`
- `sharepacks/_predictive/<D>/control_center/blackapple_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_compound_events.csv`
- `sharepacks/_predictive/<D>/control_center/meta.json`

## Arena Objects To Preserve

### 1. Positional pressure

- `aux_positional_pressure`

Recommended fields:

- hard-due digits
- shortlist families / literals
- variant breadth
- positional currentness
- positional concentration / cleanliness

### 2. VTRAC pressure

- `aux_vtrac_pressure`

Recommended fields:

- overdue indices
- top overlay indices
- heatboard / repeat context
- index breadth
- multi-variant pressure

### 3. Badge pressure

- `aux_badge_pressure`

Recommended fields:

- top pressured indices
- pressure by badge class / severity
- variant breadth
- pair-vs-combo pressure split
- strongest supporting literals / families

### 4. Pair and combo overdue context

- `aux_pair_band_context`

Recommended fields:

- strongest due/hot pairs
- multi-variant repeats
- pair-family / mirror-family relationships
- strongest combo bands
- bridge to VTRAC index neighborhoods

### 5. Due-double family pressure

- `aux_due_doubles_family_pressure`

Recommended fields:

- due-double literals / families
- mirror-pair closure
- single vs double regime hints
- double drought strength
- VTRAC-linked double families where available

### 6. Repeat-watch context

- `aux_repeat_watch_context`

Recommended fields:

- VTRAC repeat streak / hazard
- repeat heat
- last repeat / max streak
- relevant current indices

### 7. Sums context

- `aux_sums_context`

Recommended fields:

- active sums
- root sums
- variant breadth
- links to current families or doubles

### 8. Blackapple context

- `aux_blackapple_context`

Recommended fields:

- alert status
- BA score
- trigger mix
- variant profile
- candidate examples
- candidate count

### 9. Profit-alert context

- `cc_profit_alert_context`

Recommended fields:

- alert count
- alert strengths
- suggested combinations
- badges
- canonical / implied-set linkage
- parsed evidence summary
- state-level alert breadth

### 10. Compound-event context

- `cc_compound_event_context`

Recommended fields:

- top event
- event priority
- watchlist tags
- candidate alert ids
- promoter alert ids
- conflict / promoter context

### 11. Control Center tracker context

- `cc_tracker_context`

Recommended fields:

- due doubles summary
- VTRAC repeat-watch summary
- Blackapple state summary
- any global control-center flags useful for state ranking

## Heavy Artifacts That Should Stay Linked

These are valuable, but too heavy to flatten naively:

- full boxed VTRAC badge matrix / organized badge tables
- raw badge rows by variant / pair / combo
- full pair-status tables
- Blackapple candidate ledgers
- full profit-alert evidence JSON

Recommended policy:

- preserve compact structured arena objects
- keep artifact paths / references so later arena review can drill into the heavy truth layer

## Current Narrow Surfaces That Must Stay Separate

Current predictive selection usage such as:

- `aux_positional`
- `aux_vtrac_index_overdue`
- `mirror_pair_closure`
- `due_doubles`

should remain clearly labeled as:

- bounded predictive conversion methods

They are **not** the full Aux/Control Center arena contract.

## Non-Goals

Do not optimize `Aux + Control Center` toward:

- a tiny direct-caller oracle
- a tiny top-suggestions-only contract
- same-day literal-only evaluation

The right role is:

- context
- compounding
- regime classification
- family/index reinforcement

## Recommended Bounded Finish

If one final implementation slice is taken later, it should be:

- broader structured export/wiring from existing `summary.json + control_center/*.csv`
- not a broad underlying Aux scorer rewrite

## Freeze Criteria

Freeze `Aux + Control Center` for this phase when:

1. the broad arena contract is explicit
2. the narrow candidate-universe subset is clearly separated from the arena contract
3. heavy artifacts are identified as linked truth layers rather than silently discarded
4. any final export slice preserves broader evidence without forcing early conversion policy

At that point, remaining lift should come from the aggregated analysis arena, not more narrow Aux/CC trimming.
