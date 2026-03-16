# VTRAC + Hot Zones Assessment

Date: `2026-03-16`

## Executive Read

The latest materials support a strong, favorable conclusion:

- `VTRAC Analyzer` is close to a freeze / contract-finalization state
- `Hot Zones` is close to a deterministic extractor / validator-finalization state
- neither tool should be pushed further as a small top-N standalone caller
- the remaining high-value work is to preserve their best evidence for the analysis arena

This is a good stopping shape, not a disappointing one.

## Why Reviewing Them Together Makes Sense

These tools are related but not redundant.

They read the same winner corridor from different angles:

- `VTRAC Analyzer`
  - lane / family / VT-straight semantics
- `Hot Zones`
  - late-tail pressure, vertical support, and Set1 funnel location

The shared winners HTML truth layer makes them ideal for a paired assessment:

- exact winner path
- VTRAC winner path
- cross-variant echoes
- hot/superhot zones
- late-column survivorship

## Core Findings

### 1. Both tools are stronger as lane/environment lenses than as direct callers

This is the most consistent theme across the timeline, feature decisions, case audits, and current code paths.

For both tools:

- direct low-top-N straight calling is weak
- winner neighborhood / lane correctness is materially stronger
- the best usage is therefore as arena evidence, not as isolated oracle picks

This is true in:

- `VTRAC_V0__AUDIT__QUANT`
- `HOT_ZONES_V0__AUDIT__QUANT`
- the later Hot Zones weight sweeps
- the VTRAC lane-lift notes

### 2. VTRAC Analyzer already has most of the right semantic cues

The important VTRAC insights already explored or partially hardened are:

- recency lane
- VT-only lane
- straight-lane quality
- cross-section echo
- hot/superhot support
- stable columns / right-column stability
- consensus rescue / lane rescue attempts
- top-indices-by-state as a lane summary

The main lesson from the later tuning notes is:

- the analyzer is not empty
- the scorer kept hitting diminishing returns when forced to act like a top-caller
- the highest-value remaining step is contract clarity, not more rescue thrashing

### 3. Hot Zones now looks structurally trustworthy

The Hot Zones work appears to have crossed the most important engineering threshold:

- deterministic ordering
- selective guard behavior
- strong winner-lens validation on the June gold cases

The significant remaining observations are not “the tool is broken.”
They are:

- it is best treated as a pressure / lane lens
- not as a strict tiny top-N straight caller
- its strongest value sits in:
  - late survivors
  - superhot/funnel pressure
  - vertical support
  - col1 arrival
  - VT-only lane / VT-straight context

### 4. The current predictive consumption is still narrower than the tools’ true value

Current predictive usage confirms the older concern:

- `Hot Zones` is mainly consumed as top triads
- `VTRAC` is mainly consumed as top straights / top indices

That is useful, but it does not yet fully express their best analytical value.

So the key next step is not another broad analyzer rewrite.
It is:

- defining the best arena-facing contract from what these tools already know

## Tool-by-Tool Assessment

## VTRAC Analyzer

### What is already valuable

- `indices_ranked`
- `straights_ranked`
- `top_indices_by_state` when compact outputs are present
- per-straight reasons
- lane recency / hot support / cross-section echo semantics
- winners HTML as the audit lens

### What seems less valuable now

- further overlap-vs-rescue weight thrashing inside the scorer
- trying to force VTRAC into a reliable tiny top-k straight oracle

### Best remaining finish

- finalize the lean/arena contract
- clarify canonical artifacts
- possibly add one loud smoke validator for the compact report contract
- then freeze

### Assessment call

`VTRAC` is at a handoff boundary.
The remaining value is mainly in how the arena consumes it.

## Hot Zones

### What is already valuable

- `*_hot_zones_top_lanes.csv`
- `*_hot_zones_meta.json`
- evidence tags like:
  - `col1`
  - `funnel_precol1`
  - `straight_lane`
  - `vt_only_lane`
  - `superhot_set1`
  - vertical tags
- late-tail / hot / superhot counts
- vertical support and span fields

### What seems less valuable now

- more weight sweeps trying to create a stable top-k lift
- treating the tool as a final caller instead of a pressure lens

### Best remaining finish

- finalize the lean ingest contract
- add a compact validator/digest layer so reviews stop depending on heavy raw artifacts
- then freeze

### Assessment call

`Hot Zones` is also at a handoff boundary, but its remaining work is more validator/digest-oriented than scorer-oriented.

## Shared Arena Meaning

The most important shared conclusion is:

- `VTRAC` should contribute lane semantics
- `Hot Zones` should contribute pressure / survivorship semantics

Together they form a richer truth object than either alone:

- where the winner corridor is
- how strong that corridor’s VTRAC lane is
- how it tightens into Set1 / late columns
- how much cross-variant support it has

That is exactly the kind of evidence the aggregated analysis arena should preserve.

## Residual Gaps

The remaining gaps now look like this:

### VTRAC

- contract clarity
- compact-output / arena-feed clarity
- avoid reopening lane-lift loops unless one bounded new hypothesis appears from the later arena review

### Hot Zones

- compact digest / validator output
- a cleaner arena ingest contract
- avoid more direct-caller tuning

## Final Judgment

The current materials do **not** argue for another broad optimization cycle inside either tool.

They argue for:

1. artifact-first confirmation
2. explicit arena-feed contracts
3. one bounded finish per tool if needed
4. freeze both
5. move to the aggregated analysis arena

That is the healthy stopping path.

## Validation Reality Check

The remaining bounded-closeout tooling is largely already present in the repo:

- `scripts/tools/validate_vtrac_compact_report.py`
- `scripts/tools/hot_zones_sharepack_summary.py`

Smoke runs on representative gold-day artifacts were favorable:

- VTRAC compact reports for `2025-06-21` and `2025-12-31` were present and non-empty
- Hot Zones sharepack summaries for `Virginia4 2025-06-21` and `Florida4 2026-01-03` confirmed winner presence plus rich evidence tags inside the current lean artifacts

So the final finish for these tools should be interpreted as:

- contract / handoff clarity
- validator usage clarity
- freeze discipline

not:

- another broad analyzer rescue cycle
