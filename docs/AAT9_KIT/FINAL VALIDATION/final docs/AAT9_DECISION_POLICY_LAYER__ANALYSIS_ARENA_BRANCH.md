# AAT9 Decision Policy Layer — Analysis Arena Branch

Date: `2026-03-23`

## Purpose

Define the first action-taking layer that sits:

1. below `Brain 1` per-state analysis
2. below `Brain 2` board comparison
3. above combination translation
4. above later budgeting / waging

This layer exists to answer:

- should this state actually be played?
- what is the primary cluster or lane worth acting on?
- what is the cheapest rational play mode?
- how much coverage class is justified?
- which translator should receive the state next?

The Decision Policy Layer, or `DPL`, is where the rebuilt branch becomes operational without collapsing back into raw conversion.

Current runtime status:

- conceptual architecture is approved
- a first `shadow` runtime receipt now exists at:
  - `scripts/tools/build_shadow_decision_policy.py`
- it currently emits posture/mode/cap-class/translator-route records on top of the Brain 2 overlay/scoreboard stack
- it is intentionally read-only and does not yet control live downstream combination outputs

---

## Why This Layer Is Needed

The arena branch now has:

- strong per-state truth preservation
- strong board-level review and ranking
- improving context and Control Center surfaces

What it does not yet have is a clean bridge between:

- analytical truth
- and concrete downstream action posture

Without this layer, the system tends to drift toward one of two bad states:

1. raw conversion too early
2. budgeting logic becoming the hidden decision-maker

The DPL exists to stop both.

---

## Governing Principle

The DPL should convert evidence into posture, not directly into tickets.

It should decide:

- `PLAY / WATCH / SKIP`
- `mode`
- `cap class`
- `translator route`

It should not decide:

- exact final combinations
- staking size
- progression / martingale-style economics

That keeps the layer disciplined.

---

## Relationship To Other Layers

### Brain 1

Brain 1 is the per-state analytical truth engine.

It provides:

- dominant canonicals
- dominant families
- dominant lanes / indices
- watchlists
- regime flags
- context reinforcement / context-only pressure
- survivor / frontier state

### Brain 2A

Brain 2A is state-local aggregate context.

This is where Control Center style material belongs:

- profit alerts
- compound events
- due doubles
- repeat-watch
- Blackapple standing
- positional shortlist / notes
- Aux compound evidence

### Brain 2B

Brain 2B is board-level comparison.

It provides:

- ranked states
- clean host vs shared host vs echo role
- spillover / overlap context
- spent vs unspent family logic
- board priority

### Translators

Translators are downstream.

They receive a bounded decision from the DPL and turn that into:

- boxed candidate sets
- straight candidate sets
- later special translation sets

### Budget / Waging

Budgeting is later economics.

It should consume:

- DPL posture
- DPL mode
- DPL cap class
- translator outputs

It should not define those things.

---

## Non-Negotiable Rules

1. `Strings lead, Aux compounds`
2. `Environment before candidate`
3. `Mode before combinations`
4. `Cheapest rational play mode wins`
5. `Boxed and straight are separate decision paths`
6. `Consensus is scenario-specific, not universal`
7. `Noise should degrade posture`
8. `Board rank should constrain play`
9. `Budgeting cannot override analytical truth`

---

## The 3 Core DPL Objects

### 1. State-Day Environment Object (`EDO`)

The state-level operating summary.

Required fields should include:

- `state_key`
- `draw_context`
- `environment_strength`
- `dominance_level`
- `noise_level`
- `contradiction_level`
- `cross_variant_convergence`
- `survivor_intensity`
- `frontier_cleanliness`
- `last_remaining_presence`
- `hidden_terminal_support`
- `col2_to_col1_pressure`
- `perm_lane_tightness`
- `context_reinforcement_strength`
- `context_only_pressure_level`
- `tail_consensus_present`
- `tail_consensus_value`
- `decay_status`
- `carryover_status`
- `spent_status`

### 2. Candidate Evidence Graph (`CEG`)

The bounded set of live clusters or candidates with attached evidence.

Each node should be able to represent:

- literal triad
- boxed canonical
- VTRAC family / index
- lane neighborhood

Useful fields per node:

- `candidate_key`
- `literal`
- `canonical`
- `family_key`
- `vtrac_index`
- `vtrac_lane`
- `tool_support_count`
- `tools_found`
- `variant_support_count`
- `variants_found`
- `stable_flags`
- `survivor_flags`
- `last_remaining_profile_class`
- `aux_support_total`
- `aux_support_variants`
- `aux_support_by_variant`
- `alert_links`
- `board_role`
- `reason_codes`

### 3. Decision Record

The actual output of the DPL.

Recommended shape:

```json
{
  "posture": "play|watch|skip",
  "primary_cluster": "string",
  "secondary_cluster": "string|null",
  "mode": "perm_only|boxed|vt_box|vt_straight|hybrid",
  "cap_class": "low|medium|high",
  "translator_route": "boxed|straight|vt_box|consensus_trial|none",
  "board_priority": "tier1|tier2|tier3|none",
  "carryover_action": "new|continue|close|ignore",
  "reason_codes": ["..."],
  "blockers": ["..."]
}
```

---

## Decision Stages

### Stage 0 — Truth Gate

First confirm the inputs are trustworthy.

Questions:

- are required artifacts present?
- is the state predictive-safe?
- is there drift between tables, Aux, and results context?
- is any key source missing or degraded?

If this fails:

- `WATCH` or `SKIP`
- no forced play

### Stage 1 — Environment Gate

Decide whether the state is actually actionable.

Primary checks:

- dominance vs dilution
- clean vs noisy environment
- contradiction pressure
- survivor / frontier quality
- context reinforcement vs context-only pressure
- spent vs unspent state

This stage primarily controls:

- `PLAY`
- `WATCH`
- `SKIP`

### Stage 2 — Cluster Focus

Choose the main object worth acting on.

Rules:

- one primary cluster is preferred
- one secondary shoulder is optional
- avoid wide multi-cluster indecision

This should favor:

- cross-tool agreement
- family/lane coherence
- variant-correct support
- survivor / frontier cleanliness
- Aux convergence
- board-level host quality

### Stage 3 — Mode Election

Choose the cheapest rational play mode.

#### `boxed`

Prefer when:

- family / lane truth is stronger than order truth
- exact order remains diffuse
- VTRAC boxed isolation is strong
- double / mirror-double structure is important

#### `perm_only`

Prefer when:

- in-table permutation evidence is unusually tight
- order persistence is visible
- the state is clean enough to avoid full boxing

#### `vt_box`

Prefer when:

- VTRAC family truth is very strong
- literal closure remains broad
- the state is lane-right more than literal-right

#### `vt_straight`

Prefer when:

- a VTRAC straight lane is unusually clean
- multiple variants support the same lane
- order evidence exists but literal exactness is still family-first

#### `hybrid`

Allow only when:

- there is one clear boxed thesis
- plus one bounded straight thesis
- without exploding coverage

### Stage 4 — Cap Class

Cap class is not money.

It is the allowed coverage geometry.

#### `low`

- clean state
- clean cluster
- clean mode
- minimal expansion

#### `medium`

- strong state with bounded uncertainty
- one shoulder or one expansion family allowed

#### `high`

- still playable but broader closure required
- only justified when the opportunity is still high quality

### Stage 5 — Translator Route

After posture + mode + cap class are chosen, route the state to:

- `boxed`
- `straight`
- `vt_box`
- `consensus_trial`
- `none`

This preserves separation between:

- decision
- translation
- economics

---

## Special Evidence Classes

### Survivors / Frontier

These should be first-class DPL inputs.

Required derived fields should include:

- `survivor_intensity`
- `frontier_cleanliness`
- `late_tail_density`
- `single_left_strength`
- `dominant_last_strength`
- `col2_to_col1_pressure`

These should influence:

- environment gate
- cluster focus
- mode election

### Tail Consensus

Consensus should enter the DPL as:

- event flag
- confidence modifier
- possible translator trigger

Recommended fields:

- `tail_consensus_present`
- `tail_consensus_value`
- `tail_consensus_column`
- `consensus_anchor_digit`
- `nearby_support_digits`
- `consensus_strength_class`
- `consensus_trial_eligible`

It should not yet act as a universal play rule.

### Control Center / Profit Alerts

These are DPL inputs, not a layer above it.

The DPL should ingest:

- alert class
- alert strength
- cap lines
- decay draws
- co-fire context
- direct / reinforcing / composite role

Profit alerts should modify posture and cap class.

They should not invent primary clusters without structural support.

---

## Reason Codes

Every decision should be explainable.

Suggested reason code families:

- `TRUTH_OK`
- `ARTIFACT_GAP`
- `XVAR_CONV_HIGH`
- `FAMILY_DOMINANT`
- `SURV_FRONTIER_CLEAN`
- `PERM_LANE_TIGHT`
- `VT_LANE_STRONG`
- `AUX_CONV_3V`
- `TAIL_CONSENSUS`
- `DOUBLE_PRESSURE`
- `CTX_ONLY`
- `NOISE_HIGH`
- `SPENT_MIDDAY`
- `CARRYOVER_LIVE`
- `BOARD_ECHO`
- `BOARD_CLEAN_HOST`

These matter because the DPL must be reviewable and promotable.

---

## What The DPL Must Not Do

1. Create candidates from raw Aux alone
2. Mix boxed and straight into one undifferentiated mode
3. Use budgeting as the hidden deciding factor
4. Convert all consensus events into automatic combo logic
5. Override board-level duplicate-state discipline
6. Inflate noisy states out of fear

---

## Phase Plan

### Phase 1 — Shadow DPL

The DPL emits:

- posture
- mode
- cap class
- reason codes

But it does not control downstream behavior yet.

Purpose:

- compare DPL judgments to current baseline/control outputs
- learn thresholds

### Phase 2 — Bounded DPL

The DPL may control:

- posture
- mode
- translator route

But translators stay conservative and baseline control arm remains visible.

### Phase 3 — Active DPL

The DPL becomes the operational bridge into:

- boxed translator
- straight translator
- later special translators

Budgeting still remains a later layer.

---

## Summary

The DPL should be the branch’s first deterministic action layer.

Its job is simple:

- protect the system from premature conversion
- preserve the distinction between analysis and action
- choose the cheapest rational play mode
- hand clean, bounded instructions to later translators

That is the safest and most powerful next layer for the analysis-arena branch.
