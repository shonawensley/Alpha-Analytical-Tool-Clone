# AAT9 Analysis Arena - Stage 8 Downstream Rebuild Readiness

Date: `2026-04-21`

Status: `design_brief_only`

Runtime effect: none

## Purpose

This document locks the future path from Analysis Arena evidence into the later
Arena-native downstream rebuild:

- candidate object formation
- boxed / straight expression
- budget policy sandboxing
- final readback metrics

It exists to prevent two failure modes:

- forgetting the downstream rebuild vision after Stage 7B
- implementing the rebuild too early from March-only evidence

Stage 8 is not currently active runtime. It is the next architecture phase only
after fresh-window confirmation repeats enough of the March evidence.

## Current Position

The current stopping point is Stage 7B.

Stage 7B means:

- the March evidence chain is organized
- carry-forward items are traceable
- fresh-window requirements are visible
- blockers remain explicit
- the next fresh window can be tested cleanly

Stage 7B does not mean:

- live scoring permission
- live candidate-generation permission
- boxed / straight production permission
- budget rewrite permission
- replacement of old Candidate Universe / Play Card infrastructure

## Required Sequence Before Stage 8 Implementation

The clean sequence is:

1. Run the next fresh window through the established cadence.
2. Regenerate the post-run chain on that fresh evidence, especially Stage 6B through Stage 7B.
3. Compare March Stage 7B against fresh-window Stage 7B.
4. Classify each lane as repeated, weakened, contradicted, changed, blocked, or still research-only.
5. Only then begin Stage 8A as a shadow-only Arena-native candidate object specification.
6. After Stage 8A, proceed to Stage 8B boxed / straight shadow expression and Stage 8C budget policy sandbox, still without replacing old downstream logic.

If work is needed before the next fresh window, it must remain documentation,
contract, or checklist work only.

## Stage 8A - Arena-Native Candidate Object Specification

Stage 8A should define the object that carries evidence from the Arena into
future prediction expression.

It should not create live predictions.

Minimum object fields:

- `candidate_object_id`
- `state_key`
- `draw_slot`
- `canonical`
- `straight_values`
- `vtrac_index`
- `vtrac_straight_lane`
- `expression_permission`
- `primary_lane`
- `support_role`
- `restraint_role`
- `decay_role`
- `bonus_ball_role`
- `source_trace_ids`
- `source_family_trace`
- `lineage_dedup_key`
- `same_day_evidence_summary`
- `decay_evidence_summary`
- `fresh_confirmation_status`
- `denominator_status`
- `false_positive_pressure`
- `pool_pressure`
- `rank_context`
- `blocked_reasons`
- `allowed_next_use`

Core rule:

- the object must explain why a value is present, what lane it belongs to, and
  what it is allowed to influence.

## Stage 8B - Boxed / Straight Shadow Expression Simulator

Stage 8B should consume Stage 8A objects and emit separate shadow expression
sets:

- boxed expression
- straight expression
- VTRAC boxed expression
- VTRAC straight expression
- companion decay/watch expression
- optional bonus-ball research expression

It should not blend these into one pool.

Required separation:

- boxed confidence is not straight confidence
- VTRAC boxed support is not literal boxed support
- decay resolution is not same-day prediction evidence
- support context is not standalone candidate evidence
- old Play Card realization is not Arena-native proof

## Stage 8C - Budget Policy Sandbox

Stage 8C should test economics only after Stage 8A and Stage 8B have clean
shadow outputs.

It should answer:

- what expression types deserve low / medium / high coverage caps?
- when does false-positive pressure make the pool too expensive?
- how do boxed, straight, VTRAC, decay, and bonus-ball lanes score separately?
- where does old budget compression help or hurt as a control arm?

It should not:

- choose analytical truth
- override lane permissions
- treat budget metrics as branch quality
- become live wagering logic

## Entry Gates For Stage 8A

Stage 8A may start only when all of these are true:

- a fresh window has been closed through the standard cadence
- Stage 6B through Stage 7B have been regenerated on that fresh evidence
- March Stage 7B and fresh Stage 7B have been compared
- repeated lanes are separated from weakened, contradicted, and blocked lanes
- Stage 6C rewrite blockers have been reviewed against the fresh result
- Stage 6D restraint findings remain soft-penalty research unless repeated
- Stage 6E support findings remain narrow/paired unless repeated
- decay remains a companion lane, not same-day scoring permission
- old downstream infrastructure remains labeled as control arm / baseline

## Promotion Guardrails

Do not convert these directly into weights:

- `ready_for_fresh_confirmation`
- `ready_but_watch`
- casebook priority
- support-on context
- high decay horizon rate
- VTRAC territory support
- one-window concentration
- old Play Card retention

Do not promote:

- broad support as standalone evidence
- high-pressure restraint as a hard veto
- low-denominator pockets as durable edge
- duplicate-lineage overlap as independent confirmation
- bonus-ball / fireball sidecar results into standard straight / box metrics

## Relationship To Existing DPL And Translator Docs

The older DPL and translator architecture documents remain useful conceptual
references:

- `AAT9_DECISION_POLICY_LAYER__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_TRANSLATOR_ARCHITECTURE__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
- `AAT9_Candidate_Universe_Contract.md`

This Stage 8 readiness brief controls timing.

Those older concepts should not be treated as permission to implement active
downstream behavior until fresh-window Stage 7B comparison clears the required
gates.

## Old Infrastructure Role

Old Candidate Universe / Play Card / budget infrastructure should remain:

- control arm
- baseline comparison
- realization bottleneck diagnostic
- historical benchmark

It should not define:

- Arena truth
- Arena-native candidate object schema
- boxed / straight lane permissions
- future budget policy

## Fresh-Window Readback Questions

After the next fresh window, ask these before Stage 8A:

1. Which March Stage 7B lanes repeated under fresh evidence?
2. Which lanes weakened or inverted?
3. Which lanes stayed promising but concentrated?
4. Which blockers are still active?
5. Which support findings beat meaningful support-off peers again?
6. Which restraint findings support soft penalty rather than hard veto?
7. Which decay findings resolve later without contaminating same-day metrics?
8. Which candidate-expression rows have denominator-safe evidence?
9. Which boxed and straight opportunities need separate objects?
10. Which old downstream failures are real translator opportunities rather than upstream misses?

## Practical Next Action

Until the next fresh window is processed:

- do not implement Stage 8A / 8B / 8C
- keep this document as the downstream rebuild guardrail
- use Stage 7B as the immediate fresh-window pre-flight map
- use the eventual March-vs-fresh comparison as the real trigger for Stage 8A
