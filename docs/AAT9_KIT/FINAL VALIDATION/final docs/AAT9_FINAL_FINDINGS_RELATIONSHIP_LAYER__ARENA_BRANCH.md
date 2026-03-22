# AAT9 Final Findings Relationship Layer (Arena Branch)

Date: `2026-03-21`

## Purpose

Define the next board-level layer that sits above per-state arena analysis and below advanced combination forming.

This layer exists to preserve and score relationships that are currently real in review, but not yet first-class in the runtime system:

- cross-state spillover
- shared VTRAC lanes across states
- shared doubled / mirrored family complexes
- direct vs lane/family vs composite relationships
- spent vs unspent family behavior after Midday

This is not a replacement for the aggregated arena.
It is the next layer above it.

## Why This Layer Is Needed

Per-state arena analysis is already proving useful for:

- trapping live family/lane structure
- ranking dominant canonicals
- ranking dominant VTRAC indices
- preserving context and watchlist neighborhoods

But competition review now shows a second phenomenon:

- the system can trap a live family correctly
- while the actual hit lands in another strong state carrying the same family complex

That means we now need a board-level answer to:

- where else is this family alive?
- has this family already fired on the board?
- is the local state still the cleanest host for Evening?
- is a clue direct, lane/family, or only composite?

## Placement In The System

Recommended layer order:

1. per-state analyzers
   - Stable
   - Digit Reduction
   - VTRAC
   - Hot Zones
   - Aux / Control Center
2. per-state aggregated analysis arena
3. arena review / state ranking
4. `board spillover overlay` or `final findings relationship layer`
5. advanced final findings
6. combination forming / budgeting / play geometry

The new layer should not be placed:

- inside any one analyzer
- inside the base aggregated arena object
- inside a single Control Center alert

It is a board-level comparative layer.

## Relationship To Combination Forming

This layer is not the same thing as combination forming.

Its job is to preserve and score relationships before combination forming makes pack decisions.

That means:

- analysis discovers what is alive
- the relationship layer classifies how those live objects relate
- combination forming decides what to actually do with the strongest findings

This distinction is important because the old system often jumped too quickly from:

- broad findings
- straight into combination geometry and budgeting

without enough data-driven relationship learning in between.

The arena branch is trying to fix that.

## Relationship To Master Validation

Master Validation should collect evidence for this layer.

In practice that means:

- if a winner was direct, record it
- if a winner was only lane/family visible, record that separately
- if a winner was reachable only through doubled anchors, mirror shoulders, key digits, or same-index conversion, record that as `composite`

That review data is what should later shape:

- final findings policy
- advanced combination forming
- and profitability thresholds

## Governing Rules

### Rule 1

Do not push crossover logic back into local tool scoring too early.

Reason:

- crossover is a board phenomenon
- local analyzers should stay responsible for local structural truth

### Rule 2

Separate these relationship classes explicitly:

- `direct-local`
- `direct-cross-state`
- `lane/family`
- `composite`

Do not merge them into one “soft hit” bucket.

### Rule 3

Composite findings are allowed as review objects before they become policies.

Meaning:

- if `A10 099` plus same-index shoulder explains `954`, preserve that
- but do not grade it as a direct A10 hit until a real relationship rule exists

### Rule 4

Use this layer to reduce noise, not increase it.

Good use:

- detect duplicate state complexes
- identify spent families after Midday
- trim states that are carrying the same family

Bad use:

- endlessly widen every pack because “another state also had it”

### Rule 5

Profit Alerts, Due Doubles, Blackapple, and VTRAC repeat watch may participate in relationship logic, but they remain context objects first.

They should:

- reinforce
- connect
- classify

They should not manufacture final findings without structural support.

## Inputs

The layer should consume compact top surfaces, not every raw row:

### Per-state arena inputs

- `arena_synthesis.dominant_canonicals`
- `arena_synthesis.dominant_vtrac_indices`
- `arena_synthesis.dominant_families`
- `arena_synthesis.vtrac_literal_watchlist`
- `arena_synthesis.context_reinforced_canonicals`
- `arena_synthesis.state_regime`

### Cross-tool relation inputs

- `canonical_consensus_top`
- `vtrac_index_consensus_top`
- `family_consensus_top`

### Context inputs

- Profit Alerts
- Due Doubles
- VTRAC Repeat Watch
- Blackapple
- badge pressure
- VTRAC overlay pressure

### Competition / truth inputs

When results exist:

- Midday winner
- Evening winner
- same-state carry-forward / decay classification

## Required Relationship Classes

### 1. Shared Lane

Definition:

- two states carry the same VTRAC index in their top live surfaces

### 2. Shared Box Family

Definition:

- two states carry the same canonicalized box family in dominant canonicals, watchlists, or alert implied sets

### 3. Alert-Implied Echo

Definition:

- one state’s alert implied set contains another state’s winner or live shoulder

### 4. Spent Family

Definition:

- a family already resolved on Midday and should be de-emphasized for Evening unless the board structure strongly argues for repeat continuation

### 5. Unspent Core

Definition:

- a state’s strongest local core was not consumed by Midday and still looks live for Evening

### 6. Composite Hypothesis

Definition:

- multiple local findings together imply a winner-side relationship not captured by any one direct surface

Examples:

- overdue double canonical + same-index shoulder
- persistence carry + doubled anchor
- VTRAC lane + mirror/double anchor

## Outputs

Recommended artifacts:

- `board_spillover_overlay__<D>__<COMPETITION>.json`
- `board_spillover_overlay__<D>__<COMPETITION>.md`
- optional compact CSV matrix for shared lanes/families

Recommended output fields:

- `state_a`
- `state_b`
- `relationship_type`
- `vtrac_index`
- `canonical_family`
- `source_surface`
- `directness`
- `midday_consumed`
- `still_live_evening`
- `explanation`
- `support_count`

## How It Should Be Used

### For state ranking

Use it to:

- detect duplicated state stories
- avoid ranking two states highly just because they carry the same family
- move up the cleanest unspent host for Evening

### For final findings

Use it to produce:

- `core findings`
- `relationship findings`
- `defensive shoulders`
- `de-emphasized spent families`

### For combination forming

This layer should hand off:

- a cleaner set of final findings
- not raw crossover chaos

It should improve combination forming by:

- removing duplicate family coverage
- preserving the best state host
- adding only bounded relationship shoulders

## What It Should Not Do

It should not:

- replace the aggregated arena
- rewrite analyzers
- directly set budgets
- blindly widen packs
- score every composite clue as a hit

## Recommended Implementation Path

### Phase 1

Research ledger only

- competition-specific crossover ledgers
- direct / lane / composite tagging
- spent vs unspent notes

### Phase 2

Reusable board spillover overlay

- compact state-vs-state matrix
- top shared lanes/families
- explicit Evening rerank hints

### Phase 3

Final findings relationship layer

- formal runtime object feeding advanced combination forming

## Validation Path

This layer should be validated on:

- fresh competitions with Midday -> Evening reranks
- frozen gold-day windows where same-day transition is measurable
- cross-state boards with obvious double/mirror congestion

Primary questions:

- does it improve evening reranks?
- does it reduce duplicate state coverage?
- does it explain cross-state exact hits more cleanly than current local-only review?

## Durable Repo Role

This document exists so the idea is not trapped in chat context.

It should be used alongside:

- `AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md`
- `AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_ANALYSIS_ARENA_INTEGRATION_QUEUE.md`
- `AAT9_ARENA_ANALYSIS_BACKLOG.md`

That is the durable structure:

- stable design note
- live queue
- live backlog
- competition/run receipts
