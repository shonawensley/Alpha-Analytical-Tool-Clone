# AAT9 Translator Architecture — Analysis Arena Branch

Date: `2026-03-23`

## Purpose

Define how the arena branch should translate approved decision posture into bounded play geometry.

This document exists to stop the old failure mode where:

- broad findings
- many historical methods
- and budget pressure

all collapsed into one rigid downstream pack model.

The branch should now use translators as:

- bounded, mode-specific conversion layers
- called only after the Decision Policy Layer chooses posture, mode, and cap class

---

## Placement

Recommended order:

1. `Brain 1`
2. `Brain 2A`
3. `Brain 2B`
4. `Decision Policy Layer`
5. `Translators`
6. `Budget / Waging`

Translators belong:

- after evidence and posture are established
- before economics

They are not:

- analytical engines
- budget managers
- alert systems

---

## Governing Rules

1. Translators may not invent analytical truth.
2. Translators may only consume DPL-approved clusters.
3. Translators must remain mode-specific.
4. Translators should prefer the smallest rational set that still respects the approved mode and cap class.
5. Translators should emit transparent reason codes and overlaps.

---

## Required Translator Families

### 1. Boxed Translator

Purpose:

- isolate the strongest boxed hit geometry

Main use cases:

- strong family / lane truth
- literal order uncertainty
- VTRAC boxed opportunity
- double / mirror-double family closure

Likely inputs:

- primary canonical / family cluster
- VTRAC boxed family
- double / mirror-double support
- lingering support digits when explicitly justified
- survivor / frontier support

Likely outputs:

- boxed canonical list
- grouped family closures
- overlap notes
- total coverage count
- translator reason codes

### 2. Straight Translator

Purpose:

- isolate the strongest order-sensitive geometry

Main use cases:

- tight permutation lanes
- ordered persistence
- VTRAC straight-lane structure
- clean in-table permutation evidence

Likely inputs:

- literal triads
- observed in-table permutations
- ordered lane persistence
- VTRAC straight lane
- straight-specific alert reinforcement

Likely outputs:

- straight list
- permutation subset notes
- VTRAC straight lane references
- total coverage count
- translator reason codes

### 3. VT Box Translator

Purpose:

- handle the specific case where the lane/index truth is stronger than literal closure

Main use cases:

- lane-right, literal-broad states
- strong same-index neighborhood
- boxed-family trapping where exact literal is still unclear

This translator should stay separate from generic boxed translation so it remains measurable.

### 4. Consensus Trial Translator

Purpose:

- preserve the ability to test specialized consensus-driven translation without polluting all other flows

Main use cases:

- tail-consensus / R-consensus event present
- nearby support digits are preserved
- consensus is strong enough to justify experimental bounded translation

This should remain trial/research-first until validated.

---

## Translator Inputs

Translators should only read bounded DPL-approved surfaces.

Required input bundle:

- `posture`
- `mode`
- `cap_class`
- `primary_cluster`
- `secondary_cluster`
- `translator_route`
- `reason_codes`

Useful analytical support:

- candidate evidence graph slice
- VTRAC lane members
- boxed canonical family members
- in-table permutation observations
- consensus support fields when present

---

## Translator Outputs

Each translator should emit a compact, reviewable object.

Recommended shape:

```json
{
  "translator": "boxed|straight|vt_box|consensus_trial",
  "state_key": "STATE",
  "mode": "boxed|perm_only|vt_box|vt_straight|hybrid",
  "primary_cluster": "string",
  "members": ["..."],
  "overlap_groups": ["..."],
  "coverage_count": 0,
  "cap_class": "low|medium|high",
  "reason_codes": ["..."],
  "notes": ["..."]
}
```

---

## What Translators Must Not Do

1. Pull in wide unrelated shoulders because of anxiety
2. Force every old method into the same run
3. Smuggle budgeting logic into coverage selection
4. Treat every consensus event as universally actionable
5. Override `PLAY / WATCH / SKIP`

---

## Relationship To Baseline Control Arm

Current legacy downstream outputs should remain:

- baseline/control comparison targets

They are useful for:

- benchmarking
- showing what older compression logic would have done

They are not:

- the conceptual center of the arena branch
- the definition of translator behavior

This means the branch can compare:

- legacy control-arm compression
- new translator outputs

without mixing their roles.

---

## Summary

The translator layer should be:

- downstream
- bounded
- mode-specific
- measurable

Its job is not to think.

Its job is to convert already-approved state decisions into the smallest rational candidate geometry for the chosen mode.
