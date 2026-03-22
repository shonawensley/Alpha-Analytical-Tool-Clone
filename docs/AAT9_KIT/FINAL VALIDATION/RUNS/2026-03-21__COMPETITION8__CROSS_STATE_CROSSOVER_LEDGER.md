# Competition 8 Cross-State Crossover Ledger

Date: `2026-03-21`  
Board: `Connecticut4`, `OntarioCanada4`, `Virginia4`, `NewJersey4`, `NorthCarolina4`  
Midday truth:

- `Connecticut4 -> 954`
- `OntarioCanada4 -> 148`
- `Virginia4 -> 940`
- `NewJersey4 -> 992`
- `NorthCarolina4 -> 550`

## Purpose

This ledger records the first explicit board-level crossover read from a live-style arena competition.

The key point is:

- several live family complexes were trapped correctly
- but they resolved in neighboring strong states rather than the state where the family first looked most playable

This is not a state-label bug.
It is a board-level relationship phenomenon.

## Relationship Types

Use these labels when reviewing crossover behavior:

- `direct-local`
  - the state’s own predictive surfaces directly contained the winner
- `direct-cross-state`
  - another target state’s predictive surfaces directly contained the winner
- `lane/family`
  - another state did not contain the exact literal, but did contain the winner’s box family or VTRAC lane
- `composite`
  - no single surface directly contained the winner, but multiple live findings together plausibly implied it

Important guardrail:

- `composite` is a real review class
- it is not the same as a direct hit
- it should be preserved separately until a future relationship layer can test it properly

## Board-Level Shared Complexes

The strongest repeated cross-state family overlaps on this board were:

- `NewJersey4 <-> NorthCarolina4`
  - VTRAC `15`: `049 / 445 / 599`
  - VTRAC `35`: `499 / 994`
- `NewJersey4 <-> OntarioCanada4`
  - VTRAC `1`: `005 / 055 / 550`
  - VTRAC `5`: `455 / 554 / 559`
- `Connecticut4 <-> NewJersey4`
  - VTRAC `4`: `003 / 355`
- `Connecticut4 <-> Virginia4`
  - VTRAC `28`: `224`
  - VTRAC `21`: `678`

This is why the board felt tightly related even though the states were different draws:

- multiple states were converging onto the same small family neighborhoods
- especially in double-heavy and mirror-heavy corridors

## Midday Winner Readback

### Connecticut4 -> `954`

Winner facts:

- canonical box family: `459`
- VTRAC index: `15`

Observed:

- no direct local arena watchlist catch
- no direct cross-state watchlist catch
- no direct profit-alert catch

Important composite hypothesis:

- `Connecticut4` had `A10 099 DBL/RANK1`
- its implied set was only `099 / 909 / 990`
- `990` shares VTRAC `15` with `954`

Current judgment:

- `composite`, not direct
- this is a real example of an overdue-double alert that may need a second-stage VTRAC-family interpretation instead of straight-only grading

Evening implication:

- Connecticut did not consume its own main `113 / 136 / 366 / 668` core
- but it did reveal a missed relationship class around doubled anchors and same-index shoulder conversion

### OntarioCanada4 -> `148`

Winner facts:

- canonical box family: `148`
- VTRAC index: `24`

Observed:

- no direct local watchlist catch
- no direct cross-state watchlist catch
- no direct profit-alert catch

Important composite hypothesis:

- `OntarioCanada4` had local profit-alerts:
  - `A04 368 PERSIST/BA`
  - `A10 044 DBL/RANK3`
- this does not directly produce `148`
- but it is a plausible example of:
  - one live lane / persistence object
  - plus one live doubled anchor
  - combining into a result the current system does not yet explicitly assemble

Current judgment:

- `composite`, weak-to-moderate confidence
- useful as a future relationship-study case, not as a current direct credit

Evening implication:

- Ontario still reads as the weakest state-local extractor on this board
- but it remains useful as a relationship-study state because its misses look structured rather than random

### Virginia4 -> `940`

Winner facts:

- canonical box family: `049`
- VTRAC index: `15`

Observed:

- no direct local Virginia watchlist catch
- direct cross-state profit-alert catch:
  - `NewJersey4 Evening A04 049`
  - implied set: `049 / 094 / 409 / 490 / 904 / 940`

Current judgment:

- `direct-cross-state`

Evening implication:

- Virginia’s original evening core `225 / 022 / 255 / 259 / 224 / 229` remained mostly unspent after Midday
- this is why Virginia moved up in the evening rerank

### NewJersey4 -> `992`

Winner facts:

- canonical box family: `299`
- VTRAC index: `31`

Observed:

- direct cross-state watchlist catch:
  - `NorthCarolina4`
  - watchlist lane `31 => 299 / 992 / 924 / 249`
- North Carolina also had strong local support on `299 / 249`

Current judgment:

- `direct-cross-state`

Evening implication:

- New Jersey itself still kept strong untouched compression for evening
- but the `299 / 992` lane should be treated as already consumed in the board-level rerank

### NorthCarolina4 -> `550`

Winner facts:

- canonical box family: `055`
- VTRAC index: `1`

Observed:

- direct cross-state watchlist catch:
  - `NewJersey4` lane `1 => 005 / 055 / 550 / 500`
  - `OntarioCanada4` lane `1 => 055 / 550 / 005`
- no direct local North Carolina alert caught `550`

Current judgment:

- `direct-cross-state`

Evening implication:

- North Carolina stayed strong structurally
- but its own strongest local evening advantage shifted away from the already-fired `055 / 005` crossover family

## Profit Alert Relationships

Strongest direct profit-alert relationship on the board:

- `Virginia4 Midday 940`
  - matched `NewJersey4 Evening A04 049`
  - this is the clearest example of a cross-state profit-alert hit

Strongest structural but not direct profit-alert relationships:

- `Connecticut4 A10 099 DBL/RANK1`
  - likely wants a later same-index shoulder interpretation
- `OntarioCanada4 A04 368` plus `A10 044`
  - likely wants a later composite relation study, not direct grading

Important guardrail:

- direct alert hits and composite relation hypotheses should not be scored the same way

## What This Ledger Proves

Competition 8 proves a real system need:

- per-state arena analysis is not enough by itself
- after per-state synthesis, the board needs a second layer that can compare top states against each other

The missing layer should explicitly model:

- shared VTRAC lanes across states
- shared box families across states
- shared profit-alert implied sets
- spent vs unspent families after Midday
- direct vs lane/family vs composite relationships

## Immediate Design Consequence

The next layer should not be buried inside:

- Stable
- DR
- VTRAC
- Hot Zones
- or the base Control Center alert IDs

Instead it should become a new board-level object:

- `board spillover overlay`
- or `final findings relationship layer`

That layer should sit between:

- per-state arena synthesis
- and later combination-forming / final-pack assembly

## Evening Relationship Addendum

Later evening truth added two more useful board-study cases:

- `Connecticut4 -> 394`
- `NewJersey4 -> 950`

These are important because they strengthen the need for a relationship layer without falsely inflating direct-hit credit.

### Connecticut4 -> `394`

Observed local building blocks:

- `A10 099 DBL/RANK1`
  - implied set `099 / 909 / 990`
- `A12 355 PERM/CLAMP`
  - implied set `503 / 508 / 553 / 558`
- arena VTRAC watchlists:
  - `15 => 440 / 044 / 099`
  - `4 => 355 / 003`

Current judgment:

- `composite`

Why:

- no single pre-result surface directly contained `394`
- but the board did preserve a plausible doubled-anchor and key-digit chain:
  - `99`
  - `55`
  - plus a live `3`
  - inside active same-index / shoulder neighborhoods

This is exactly the kind of relation that should be studied later rather than promoted prematurely.

### NewJersey4 -> `950`

Observed local building blocks:

- VTRAC `15`
  - `049 / 459 / 445 / 044 / 599`
- VTRAC `5`
  - `559 / 004 / 455 / 554 / 009`
- VTRAC `4`
  - `003 / 355 / 053 / 508 / 805 / 035 / 558`
- final NJ emphasis already favored:
  - `455 / 559 / 445 / 499 / 344 / 003`

Current judgment:

- `lane/family-to-composite`

Why:

- this was not a direct literal catch
- but it does look like a mirror-double / lane-shoulder conversion inside a live New Jersey family environment

## Consequence For Review Method

Competition 8 now supports a stronger review distinction:

- `direct`
- `lane/family`
- `lane/family-to-composite`
- `composite`

That finer separation is useful because:

- it avoids pretending relational cases were direct hits
- but it also avoids throwing away real structural closeness as if it were random noise
