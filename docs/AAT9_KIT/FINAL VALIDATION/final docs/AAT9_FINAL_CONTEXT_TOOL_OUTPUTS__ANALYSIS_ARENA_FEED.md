# AAT9 Final Context Tool Outputs -> Analysis Arena Feed

Date: `2026-03-17`

## Purpose

This document is the canonical semantic reference for what the **context and compound**
systems should feed into the aggregated analysis arena.

It is the companion to:

- `AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`

The string-tool document explains the core structural table truth.
This document explains the broader context layer:

- `Aux`
- `Control Center`
- `Profit Alerts`
- `Due Doubles`
- `Blackapple`
- `VTRAC repeat-watch`
- related pair / combo / badge / sum context

This document answers the question:

- **what context, pressure, and compounding evidence should be preserved in the arena, what it means, and how it should be treated**

That means this document is:

- context-semantic
- arena-oriented
- comprehensive by design

It is **not**:

- a candidate-universe contract
- a play-card contract
- a budget document
- a direct-caller score policy

## Governing Principle

The most important context-layer rule is:

- **Aux / Control Center should reinforce, corroborate, classify, and shape string truth**
- **they should not manufacture string truth that is not structurally present**

That means these systems are mainly supposed to:

- confirm a live family / lane / corridor
- describe regime type
- add pressure/context around the live story
- break ties or upgrade credibility when multiple string stories compete
- preserve sleeper-context objects so later arena review can learn when they matter

They are **not** mainly supposed to:

- create a top candidate out of nothing
- replace the string tools
- brute-force direct-caller behavior

This distinction is critical for later aggregation and scoring.

## Current Fill Status

| Context subsystem | Status in this document |
|---|---|
| `Aux positional + VTRAC overlay pressure` | `complete` |
| `Aux badges / pairs / doubles / sums / repeat watch / Blackapple` | `complete` |
| `Control Center due doubles / repeat watch / Blackapple alerts` | `complete` |
| `Control Center profit alerts / compound events / tracker context` | `complete` |

---

## Aux + Control Center

## 1. Current Role

`Aux + Control Center` should now be understood as:

- the system's broadest predictive context layer
- a compound-pressure and regime-description layer
- a family / lane / index reinforcement layer
- a context-rich alert and tracker layer
- a heavy truth-adjacent layer whose best value is broad preservation before later scoring

It should **not** be judged mainly as:

- a tiny direct-caller oracle
- a literal-only caller
- a substitute for string-tool structural evidence

The final Aux / Control Center read is:

- the current predictive conversion usage is intentionally narrow
- that narrowness was a bounded selection-layer decision, not the final arena contract
- therefore the arena must preserve much more of the structured context these systems already expose

## 2. Canonical Predictive Sources

Aux / Control Center's canonical predictive-side sources are:

### 2.1 Aux SSOT

- `sharepacks/_predictive/<D>/<STATE>/aux/<STATE>/summary.json`

Important Aux subtrees to preserve:

- `positional`
- `pairs`
- `doubles`
- `sums`
- `repeat_watch`
- `vtrac`
- `blackapple`
- `draw_sources`

### 2.2 Control Center SSOT

- `sharepacks/_predictive/<D>/control_center/due_doubles.csv`
- `sharepacks/_predictive/<D>/control_center/vtrac_repeat_watch.csv`
- `sharepacks/_predictive/<D>/control_center/blackapple_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_alerts.csv`
- `sharepacks/_predictive/<D>/control_center/profit_compound_events.csv`
- `sharepacks/_predictive/<D>/control_center/meta.json`

### 2.3 Predictive Arena Bridge

The current predictive-to-arena bridge already exists:

- `sharepacks/_predictive/<D>/<STATE>/analysis/aux_control_center_arena*.json`
- `sharepacks/_predictive/<D>/<STATE>/analysis/aux_control_center_arena*.md`
- signals bundle surface:
  - `tools.aux_control_center_context`

Important judgment:

- this export slice is the right bounded finish for the current phase
- it broadens preservation without forcing new conversion behavior
- it should now be documented as the canonical context-layer arena bridge

## 3. Audit-Only / Truth Layers

Aux / Control Center truth and audit layers should remain available for:

- post-results explanation
- deep badge review
- cross-variant pair/combo review
- Blackapple candidate review
- profit-alert evidence review
- later aggregated-arena learning

Important heavy truth layers:

- full boxed VTRAC badge tables
- raw badge rows by pair / combo / variant
- full pair-status tables
- Blackapple candidate ledgers
- detailed profit-alert evidence JSON

Important judgment:

- not all of these should be flattened into the arena
- but they also should **not** disappear
- the arena should preserve compact structured summaries and leave drill-down paths to these heavier layers

## 4. Aux / Control Center's Final Predictive Meaning

Aux / Control Center contributes all of the following to the aggregated arena:

- positional pressure
- VTRAC overlay / heatboard pressure
- badge-organized index pressure
- pair and combo band pressure
- due-double family pressure
- repeat-watch regime context
- sums / root-sum context
- Blackapple alert context
- profit-alert context
- profit compound-event context
- global tracker / source-count context

The crucial design rule is:

- **preserve broadly, let later aggregation decide how much reinforcement matters**

The old failure mode was narrowing this layer to only the safest early conversion methods.

## 5. Raw Evidence Families To Preserve

Aux / Control Center has seven main predictive evidence layers:

1. positional tracker evidence
2. VTRAC overlay / heatboard evidence
3. pair / double / badge evidence
4. repeat watch / sums / Blackapple evidence
5. Control Center due-doubles and repeat-watch trackers
6. profit alerts and compound events
7. payload metadata / linked truth layers

### 5.1 Positional Tracker Evidence

Source:

- `summary.json`
  - `positional`

Primary semantic role:

- identifies where digit pressure is concentrating
- provides hard-due digits, shortlist families/literals, and positional breadth/currentness

Core fields that should be preserved or remain reachable:

| Field / family | Meaning in the arena |
|---|---|
| `hard_due_by_variant` | variant-level overdue digit pressure |
| `shortlist_report.candidates` | bounded positional shortlist with score/source/tags |
| `shortlist_report.variant_top_digits` | top digits by position/variant |
| `shortlist_report.aggregated_digits` | aggregated positional digit pressure |
| `consensus_notes` | cross-position / cross-variant alignment notes |
| `double_pressure_notes` | positional double-related pressure notes |

Important judgment:

- positional tracker is strongest as pressure/context, not as a literal caller
- the arena should preserve hard-due structure and shortlist context, not just a short literal list

### 5.2 VTRAC Overlay / Heatboard Evidence

Source:

- `summary.json`
  - `vtrac`

Primary semantic role:

- exposes overdue indices and heatboard-style VTRAC pressure within Aux

Core fields that should be preserved or remain reachable:

| Field / family | Meaning in the arena |
|---|---|
| `overlay_top` | top overdue indices by variant |
| `heatboard_top` | top heatboard/repeat-style indices by variant |

Important judgment:

- this is context and reinforcement for live lanes
- not a standalone VTRAC direct-caller replacement

### 5.3 Pair / Double / Badge Evidence

Sources:

- `summary.json`
  - `pairs`
  - `doubles`
- predictive badge-pressure extraction
- linked heavy badge tables

Primary semantic role:

- captures overdue/hot pair-space and combo-space pressure
- organizes badge pressure into analytically useful structures

Core families that should be preserved or remain reachable:

| Field / family | Meaning in the arena |
|---|---|
| `pairs.top_by_variant.repeating` | repeating pair pressure |
| `pairs.top_by_variant.non_repeating` | non-repeating pair pressure |
| `pairs.multi_variant_alerts` | same pair pressuring multiple variants |
| `doubles.top_by_variant` | combo/double pressure |
| `doubles.multi_variant_alerts` | same combo pressuring multiple variants |
| badge index pressure | compressed VTRAC-index badge pressure surface |
| pair/combo severities | badge-class intensity (`red`, `blue`, `purple`, etc.) |

Important judgment:

- badge pressure is under-preserved, not disproven
- the arena should preserve a compact badge-pressure object
- and keep a path to the heavier boxed VTRAC badge matrix for later deep review

### 5.4 Repeat Watch / Sums / Blackapple Evidence

Source:

- `summary.json`
  - `repeat_watch`
  - `sums`
  - `blackapple`

Primary semantic role:

- describes repeat regime, sum regime, and Blackapple alert context inside Aux

Core families that should be preserved or remain reachable:

| Field / family | Meaning in the arena |
|---|---|
| `repeat_watch` | Aux repeat-index regime context |
| `sums.top_by_variant` | active sum/root-sum context |
| `blackapple.by_variant.score` | variant-level BA score |
| `blackapple.by_variant.triggers` | trigger mix (`mirror`, `root_due`, `floating`, `pairs`, `pattern`) |
| `blackapple.by_variant.candidates` | top BA candidate examples/tags |

Important judgment:

- these are classic environment descriptors
- they should remain context objects, not be forced into literal-only conversion behavior

### 5.5 Control Center Tracker Evidence

Sources:

- `due_doubles.csv`
- `vtrac_repeat_watch.csv`
- `blackapple_alerts.csv`

Primary semantic role:

- provides the state-level global trackers and regime summaries that sit alongside the Aux local summary

Core families that should be preserved or remain reachable:

| Field / family | Meaning in the arena |
|---|---|
| `Draws Since Double` | double-drought strength |
| `Family N` rows in `due_doubles.csv` | due-double families and examples |
| `Current Index`, `Current Streak`, `Heat Index`, `Heat Hazard` | repeat-watch regime state |
| `BA-Score`, `Status`, `Triggers`, `#Candidates`, `Examples` | Blackapple alert summary |

Important judgment:

- due doubles and repeat-watch are first-class regime context
- they should not be treated as tiny add-ons

### 5.6 Profit Alerts And Compound Events

Sources:

- `profit_alerts.csv`
- `profit_compound_events.csv`

Primary semantic role:

- structured alerting and state-level event compounding

Core fields that should be preserved or remain reachable:

| Field / family | Meaning in the arena |
|---|---|
| `AlertId` | alert identity |
| `Strength` | alert strength |
| `Suggested` | alert suggestion type |
| `Badges` | alert badge tags |
| `Canonical` | canonical/literal linkage |
| `ImpliedSet` | attached candidate set size |
| `Evidence` | evidence JSON summary / parsed keys |
| `top_event` | compound-event label |
| `priority` | event priority |
| `watchlist_tags` | event tags |
| `candidate_alert_ids`, `promoter_alert_ids` | event alert linkage |
| `strength_max`, `merged_rows_total` | event strength / merge density |

Important judgment:

- profit alerts are much richer than the current narrow predictive usage suggests
- the arena should preserve alert density, breadth, attached combinations, and compound-event context

### 5.7 Payload Metadata / Linked Truth Layers

Source:

- `aux_control_center_arena*.json`

Primary semantic role:

- provenance and contract-level context for the full export

Important fields:

| Field | Meaning |
|---|---|
| `schema_version` | export contract version |
| `results_date`, `history_date`, `profile`, `experiment_tag`, `state_key` | run provenance |
| `inputs`, `inputs_hash` | input traceability |
| `linked_truth_layers` | drill-down references |
| `selection_subset_note.current_conversion_methods` | explicit separation between conversion subset and full arena contract |

This layer is mainly for audit and calibration, not direct promotion.

## 6. Arena Objects That Should Feed The Aggregated Arena

The predictive-side context bridge is:

- `analysis/aux_control_center_arena*.json`

These arena objects are the main context-layer contract.

### 6.1 `aux_positional_pressure`

Primary meaning:

- structured positional digit pressure and shortlist context

Why it matters:

- positional tracker is one of the strongest ways to understand where structure is concentrating without forcing direct-caller behavior

Important preserved fields:

- `hard_due_by_variant`
- `variant_top_digits`
- `aggregated_digits_top`
- `shortlist_top`
- `consensus_notes`
- `double_pressure_notes`

### 6.2 `aux_vtrac_pressure`

Primary meaning:

- VTRAC overlay and heatboard-style context from Aux

Why it matters:

- it reinforces lane/index pressure without replacing string-tool lane semantics

Important preserved fields:

- `overlay_top`
- `heatboard_top`

### 6.3 `aux_badge_pressure`

Primary meaning:

- compact badge-organized pressure object joining index pressure, pair alerts, and combo alerts

Why it matters:

- this is the main current bridge from the heavier badge world into the arena

Important preserved fields:

- `index_pressure`
- `top_pair_alerts`
- `top_combo_alerts`
- `multi_variant_pairs`
- `multi_variant_combos`

Important guardrail:

- badge pressure should mainly reinforce or shape live string truth
- not blindly manufacture promotion by itself

### 6.4 `aux_pair_band_context`

Primary meaning:

- pair-space and band-space overdue/hot context

Why it matters:

- pairs and bands are one of the clearest family/index reinforcement regimes in Aux

Important preserved fields:

- `top_by_variant`
- `multi_variant_top`
- `top_alerts`

### 6.5 `aux_due_doubles_family_pressure`

Primary meaning:

- due-double family regime context

Why it matters:

- due doubles are one of the most important regime descriptors in the whole system

Important preserved fields:

- `max_draws_since_double`
- `by_variant[].draws_since_double`
- `by_variant[].families`

### 6.6 `aux_repeat_watch_context`

Primary meaning:

- repeat-watch regime context from both Aux and Control Center

Why it matters:

- repeat hazards and streaks are environmental context, not tiny filters

Important preserved fields:

- `aux_by_variant`
- `control_center_top`

### 6.7 `aux_sums_context`

Primary meaning:

- sum / root-sum pressure context

Why it matters:

- sums can help later aggregation understand whether multiple live families are sitting inside the same arithmetic regime

Important preserved fields:

- `top_by_variant`

### 6.8 `aux_blackapple_context`

Primary meaning:

- Blackapple alert and trigger context from Aux and Control Center together

Why it matters:

- BA is valuable as alert-state context even when it is not a tiny same-day caller

Important preserved fields:

- `aux_by_variant`
- `control_center_top`

### 6.9 `cc_profit_alert_context`

Primary meaning:

- structured profit-alert environment for the state

Why it matters:

- this is one of the richest context objects for later comparison against live string clusters

Important preserved fields:

- `alert_count`
- `variants`
- `top_alerts`

### 6.10 `cc_compound_event_context`

Primary meaning:

- top compound events, priorities, and alert linkages

Why it matters:

- this is the cleanest state-level event compounding object in Control Center

Important preserved fields:

- `top_events`

### 6.11 `cc_tracker_context`

Primary meaning:

- meta-tracker summary and source inventory

Why it matters:

- later arena review needs to know what tracker surfaces were actually present and how rich the source set was

Important preserved fields:

- `control_center_meta_path`
- `source_counts`

## 7. Context-Specific Advanced Evidence Objects And Final Learnings

These are the most important nuanced context-layer conclusions from the final sweep.

### 7.1 Reinforcement vs manufacture

Status:

- **major keeper**
- **governing interpretation rule**

Why it matters:

- context systems should validate, reinforce, classify, and shape live string truth
- they should not manufacture it

Important guardrail:

- later aggregated-arena scoring should usually treat these objects as corroborative/contextual first
- and only occasionally as sleeper-surfacing evidence when results justify it

### 7.2 Badge pressure is under-preserved, not disproven

Status:

- **major keeper**

Why it matters:

- the current system preserves only a compressed badge-pressure slice
- the full badge matrix and boxed VTRAC badge organization still contain more truth than the current narrow conversion subset

Important guardrail:

- preserve compact badge-pressure objects now
- keep the heavy badge world reachable for future deep review

### 7.3 Positional tracker as pressure/context

Status:

- **major keeper**

Why it matters:

- positional hard-due and shortlist signals matter
- but their best role is pressure/context and corridor support, not literal-only calling

### 7.4 Due doubles and pair-space trackers are regime context

Status:

- **major keeper**

Why it matters:

- due doubles repeatedly behave like a distinct predictive regime
- mirror-pair closure and double-led family pressure should remain visible in the arena

### 7.5 Profit alerts are structured context, not just picks

Status:

- **major keeper**

Why it matters:

- the alerts already contain identity, strength, suggested combinations, badges, canonical links, and event linkage
- that is much richer than the early narrow conversion usage

### 7.6 Blackapple and repeat-watch are environment descriptors

Status:

- **major keeper**

Why it matters:

- BA status and repeat-watch streak/hazard objects help later aggregation understand regime conditions
- they should remain context objects, not tiny direct caller tests

### 7.7 Broad structured preservation beats blind raw dumping

Status:

- **methodological keeper**

Why it matters:

- the right finish is not:
  - narrow top-N trimming
  - or blind raw dumping of every table
- the right finish is:
  - broad structured preservation
  - with linked heavy truth layers for drill-down

## 8. Bounded Downstream Helper Surfaces

These are important, but they are **not** the core context-layer arena feed.

They belong in the “bounded conversion helper” category.

| Method | Role | Current judgment |
|---|---|---|
| `aux_positional` / `aux_positional_shortlist` | bounded positional shortlist pack | keep as a helper, not the full context truth |
| `aux_vtrac_index_overdue` | bounded overdue-index pack from Aux overlay | keep as a helper, not the full VTRAC context |
| `due_doubles` | bounded due-double family pack | keep as a helper, not the full regime context |
| `due_doubles_mirror_single` / `due_doubles_mirror_double` | bounded mirror-double conversion helpers | keep as helpers only |
| `mirror_pair_closure` / `mirror_pair_closure_due_doubles` | bounded mirror-pair closure helpers | keep as helpers only |
| `profit_alerts` | bounded alert-derived combo pack | keep as a helper, not the full alert context |
| `blackapple` | bounded BA-derived combo pack | keep as a helper, not the full BA context |

Important judgment:

- these remain useful downstream experiments
- but they do not define the actual arena contract for this layer

## 9. Aux / Control Center's Final Strengths

Aux / Control Center is strongest when treated as:

- a broad context and compound layer
- a family/index reinforcement layer
- a regime classification layer
- an alert and tracker layer
- a source of structured corroboration for live string truth

It is especially powerful for:

- explaining why one live lane/family is more credible than another
- showing double, mirror, pair, and badge regime pressure
- exposing positional and VTRAC overlay context
- describing repeat-watch and Blackapple alert states
- attaching suggested literals/combinations and event linkage to live states without forcing them to become direct promotion by default

## 10. Aux / Control Center's Final Non-Goals

Do **not** force Aux / Control Center into:

- a tiny direct-caller oracle
- literal-only evaluation
- full replacement of string-tool structural truth
- using the early bounded conversion subset as the whole contract
- blindly adding points to string patterns with no structural support

Those are the wrong targets for this stage.

## 11. Aux / Control Center -> Aggregated Arena Guidance

Later aggregated arena work should treat Aux / Control Center as contributing:

- corroboration
- regime classification
- family/lane pressure
- confidence-shaping context
- alert/event context
- drill-down links to heavier truth layers

Good future aggregation questions:

- Do Aux badges and VTRAC overlays reinforce the same lane the string tools already see?
- Do due doubles and mirror-pair structures point into the same family neighborhood?
- Are profit alerts and compound events attaching themselves to the same canonicals or VTRAC neighborhoods already alive in the string tools?
- Is Blackapple alerting a state that also has strong string-tool convergence, or only noisy context?
- When context is strong but string structure is weak, is that a sleeper pattern or just context without structural truth?

Aux / Control Center should often be one of the main answers to:

- what non-string pressure is reinforcing this live state?
- what regime are we in?
- are doubles, badges, alerts, or repeat conditions confirming the same family/lane?
- how much support should the structural string story receive from the context layer?

## 12. Final Aux / Control Center Judgment

Aux / Control Center is wrapped for this phase as:

- the system's main context / compound / regime producer
- not a tiny direct-caller oracle

The major context-layer work that must remain visible in the aggregated arena is:

- positional pressure
- VTRAC overlay pressure
- badge pressure
- pair and combo band context
- due-double family pressure
- repeat-watch and sums context
- Blackapple context
- profit alerts and compound events
- tracker meta and linked heavy truth layers

If these are preserved and later compared/fused correctly, this layer becomes the arena's main non-string reinforcement and regime-description system.

The remaining true context-local gap is now narrow:

- future heavy truth-layer exports and later aggregated-arena scoring policy

That is no longer a broad reason to reopen narrow tool-local trimming.

## 13. References

Primary references used for this context section:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Analyzer_Lean_Outputs.md`
- `scripts/tools/aux_control_center_arena.py`
- `scripts/tools/create_candidate_universe.py`
- `tests/test_aux_control_center_arena.py`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__AUX_CONTROL_CENTER__ASSESSMENT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__AUX_CONTROL_CENTER__ARENA_CONTRACT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__AUX_CONTROL_CENTER__HANDOFF.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__AUX_CONTROL_CENTER__EXPORT_SLICE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_ANALYSIS_ARENA_INTEGRATION_QUEUE.md`
