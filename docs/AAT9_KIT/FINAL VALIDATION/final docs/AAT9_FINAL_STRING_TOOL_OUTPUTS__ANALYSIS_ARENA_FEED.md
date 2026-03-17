# AAT9 Final String Tool Outputs -> Analysis Arena Feed

Date: `2026-03-16`

## Purpose

This document is the canonical semantic reference for what the **string-table analysis tools**
should feed into the aggregated analysis arena.

It is intentionally more comprehensive than the lean-output spec.

The lean-output spec answers:

- what files exist
- which file is the canonical predictive artifact
- what the tool's broad role is

This document answers the next-level question:

- **what evidence classes, scoring parts, rollups, and semantic objects from each tool
  should be preserved in the arena, why they matter, and how they should be treated**

That means this document is:

- tool-semantic
- arena-oriented
- comprehensive by design

It is **not**:

- a play-card contract
- a narrow candidate-universe policy
- a budget document

## Current Fill Status

| Tool | Status in this document |
|---|---|
| `Stable Pattern Extractor` | `complete` |
| `Digit Reduction` | `pending next pass` |
| `VTRAC Analyzer` | `pending next pass` |
| `Hot Zones` | `pending next pass` |

The intent is to complete this one tool at a time so no important evidence class is lost.

---

## Stable Pattern Extractor

## 1. Current Role

`Stable` should now be understood as:

- a family/lane preservation tool
- a pattern-compounding tool
- a survivor/frontier tool
- a hidden-family and transformation clue tool

It should **not** be judged mainly as:

- a tiny top-N direct caller

This is the most important Stable conclusion from the final sweep.

The final Stable read is:

- Stable is often strong at **containing the right family/lane/corridor**
- Stable is much weaker when forced into a tiny exact-canonical caller role
- therefore the arena must preserve the richer Stable evidence, not only `stable_top`

## 2. Canonical Predictive Sources

Stable's predictive-side sources are:

- `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_stable_patterns_scores.csv`
- `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_stable_patterns_families.csv`
- `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_stable_patterns_compound.csv`
- `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_metrics.json`

Stable's arena artifact is:

- `sharepacks/_predictive/<D>/<STATE>/analysis/stable_arena*.json`
- `sharepacks/_predictive/<D>/<STATE>/analysis/stable_arena*.md`

Stable's current bounded conversion surfaces in Candidate Universe are:

- `stable_top`
- `stable_compound_top`
- `stable_family_vote`
- `stable_family_vote_v2`
- `stable_last_remaining`

These conversion surfaces are important, but they are **not** the full Stable arena contract.

## 3. Audit-Only / Winners Lens

Stable's winners / truth-layer artifacts should remain available for:

- post-results explanation
- example review
- calibration
- aggregation learning

Important truth-layer artifacts:

- `winner_family_spotlight_raw.csv`
- `winner_family_spotlight_families.csv`
- Stable winners HTML / JSON
- `metrics.json` winner placement fields

These are not predictive inputs.
They are the truth lens that justified the final Stable arena design.

## 4. Stable's Final Predictive Meaning

Stable contributes all of the following to the aggregated arena:

- canonical pattern evidence
- family evidence
- compound evidence
- progression evidence
- survivor/frontier evidence
- hidden-family reveal evidence
- order / transform / VT-straight evidence
- long-cluster evidence
- hot / mirror / consensus corroboration

The crucial design rule is:

- **preserve first, rank later**

The old failure mode was narrowing Stable too early.

## 5. Stable Raw Evidence Families To Preserve

Stable has four main predictive evidence layers:

1. row-level pattern evidence
2. compound canonical rollups
3. family box / family rollups
4. metrics / winner-placement context

### 5.1 Row-Level Pattern Evidence

Source:

- `*_stable_patterns_scores.csv`

Primary semantic role:

- the most granular predictive Stable evidence
- shows exactly what pattern/canonical is alive, where, and why

Core row fields that should be preserved or remain reachable:

| Field / family | Meaning in the arena |
|---|---|
| `section`, `Set`, `Draw`, `Column` | location and currentness context |
| `Canonical` | the literal/canonical pattern being scored |
| `family_id` | Stable family / lane identity |
| `score` | row-level total Stable strength |
| `why`, `why_tags` | human-readable explanation tags |
| `rows` | row-type footprint (`R2/R4/R6/R8/...`) |
| `type` | row class / pattern style |
| `hot` | hot-level context |
| `orders_modal_value`, `orders_modal_rows` | modal order / permutation clue |

#### Row score parts

These are the main score-part families from the Stable arena code and should be treated as first-class semantic evidence:

| Score part | Arena meaning |
|---|---|
| `score_cov` | coverage / breadth of pattern support |
| `score_hpr` | horizontal persistence / repeat behavior |
| `score_perm` | permutation / order-space support |
| `score_repeat` | repeated-structure reinforcement |
| `score_straight` | direct straight-style evidence |
| `score_single` | single-left / reduced residue support |
| `score_cons` | consensus reinforcement |
| `score_hot` | hot / hot2 pressure |
| `score_mirror` | mirror-family support |
| `score_dom` | dominant-last / dominant-pair style support |
| `score_len` | long-cluster / length-related support |
| `score_hidden` | hidden-family / clutter-reveal support |
| `score_vtrac_straight` | VT-straight style support |
| `score_persistence_set` | set-chain persistence |
| `score_persistence_draw` | draw-chain persistence |
| `score_double_mirror` | double-mirror support |

These should not be collapsed to one scalar if we want the arena to reason well later.

#### Row flags

These flags are distinct evidence classes, not just implementation debris:

| Flag | Meaning |
|---|---|
| `straight2`, `straight3` | straight-style support shape |
| `single_left` | reduced residue / single-left condition |
| `cons_full`, `cons_3v`, `cons_stub` | consensus strength variants |
| `dom_last`, `dom_pair` | dominant-last / dominant-pair cues |
| `hidden3v` | hidden 3-value structure present |
| `double_mirror` | double-mirror relation present |

#### Row counts

These are useful for later aggregation and should remain preserved:

| Count field | Meaning |
|---|---|
| `perm_count_in_box` | permutation density in the box |
| `repeat_extras_in_box` | repeat pressure in the box |
| `horizontal_persistence_repeat` | repeat persistence across progression |
| `persistence_set_count` | set-chain depth |
| `persistence_draw_run` | draw-chain depth |

### 5.2 Compound Canonical Rollups

Source:

- `*_stable_patterns_compound.csv`

Primary semantic role:

- answers what became stronger when multiple row-level clues are compounded

Key fields:

| Field | Meaning |
|---|---|
| `compound_score` | compounded canonical strength |
| `base_max_score` | strongest single-row baseline for comparison |
| `set_chain_depth` | set-chain persistence |
| `draw_chain_depth` | draw-chain persistence |
| `rows_covered` | breadth of row support |
| `funnel_precol1` | pressure reaching the pre-col1 funnel |
| `vt_only_lane` | lane pressure that is more VTRAC/family than literal |
| `hot1_count`, `hot2_count` | hot / superhot compounding |
| `col1_hits` | col1 arrival / current-frontier strength |
| `consensus_hits` | consensus reinforcement |
| `hidden3v_hits` | hidden-family contribution |
| `vtrac_straight_hits` | VT-straight contribution |
| `double_mirror_hits` | double-mirror contribution |
| `compound_why`, `compound_why_tags` | compact explanation of what compounded |

Compound context is important because Stable frequently knows more in the compounded environment than in raw top-canonical ranking.

### 5.3 Family Box / Family Rollups

Source:

- `*_stable_patterns_families.csv`

Primary semantic role:

- the strongest Stable lane/family preservation layer

This is one of the most important Stable truths:

- even when Stable misses the exact winner canonical,
- it often preserves the winning family/lane well

Important family fields:

| Field | Meaning |
|---|---|
| `family_score` / `family_score_total` | total family strength |
| `family_score_max` | strongest single family box/row contribution |
| `best_compound_score` / `best_compound_score_max` | best compound linkage into that family |
| `top_canonicals` | strongest canonicals inside the family |
| `top_modal_orders` | strongest modal orders inside the family |
| `last_remaining_3v` / `last_remaining_count` | survivor / last-remaining evidence |
| `progression_flag` / `progression_count` | progression behavior |
| `any_dom_last`, `any_consensus`, `any_hidden3v`, `any_vtrac_straight` | family-level corroborator counts |

#### Family breakdown sums

These family-level parts should be preserved because they are richer than one family total:

| Breakdown field | Arena meaning |
|---|---|
| `fam_cov` | family coverage support |
| `fam_hpr` | family horizontal persistence / repeat support |
| `fam_perm` | family permutation support |
| `fam_repeat` | family repeat reinforcement |
| `fam_cons` | family consensus support |
| `fam_hot` | family hot pressure |
| `fam_straight2`, `fam_straight3` | family straight-style support |
| `fam_doubles` | double-led family support |
| `fam_vtrac` | VTRAC-linked family support |
| `fam_hidden` | hidden-family support |
| `fam_double_mirror` | double-mirror support |
| `fam_persistence` | family persistence support |
| `fam_section_bonus` | section-context bonus |
| `fam_progression_bonus` | progression bonus |
| `fam_last_remaining_bonus` | last-remaining survivor bonus |

### 5.4 Metrics / Winner-Placement Context

Source:

- `*_metrics.json`

Primary semantic role:

- tool health
- winner placement diagnostics
- audit/truth context

Important metrics fields:

| Field | Meaning |
|---|---|
| `total_patterns`, `total_families` | tool breadth / density |
| `compression_ratio` | shape of Stable compression |
| `avg_top_hot_density` | hotness density context |
| `health` | tool health status |
| `winner_family_best_rank`, `best_compound_rank` | winner-placement diagnostics |
| `winner_hits` | exact straight / exact box / VT-box results |
| `signals.hot2_bias`, `signals.consensus_of_consensus` | diagnostic signals worth preserving in context |

Metrics are mainly for audit and calibration, not direct promotion.

## 6. Stable Arena Objects That Should Feed The Aggregated Arena

The Stable arena artifact is the most important predictive-to-arena bridge.

Source:

- `analysis/stable_arena*.json`

### 6.1 `top_row_patterns`

Primary meaning:

- strongest row-level Stable patterns by section

Why it matters:

- preserves literal pattern evidence before compression
- carries score parts, flags, counts, modal order, and row location
- includes hidden-family reveal and order-transform hints

Important preserved fields:

- `canonical`
- `score`
- `family_id`
- `locator`
- `why_tags`
- `score_breakdown`
- `flags`
- `counts`
- `modal_order`
- `source_cells`
- `hidden_family_reveal`
- `order_transform_hints`

### 6.2 `pattern_ledgers_top`

Primary meaning:

- canonical-level rollups across rows/boxes/columns

Why it matters:

- this is where Stable becomes much more than a top-row list
- it captures breadth, compounding, frontier arrival, family mix, and semantic summaries

Important preserved fields:

- `score_total`, `score_max`, `score_mean`
- `row_hits`, `box_count`, `set_count`, `draw_count`, `column_count`
- `span`
- `dominant_family_id`
- `family_ids`
- `top_why_tags`
- `top_modal_orders`
- `flag_counts`
- `hot_counts`
- `frontier_summary`
- `score_breakdown_sums`
- `score_breakdown_max`
- `score_breakdown_peaks`
- `top_box_contributions`
- `compound_context`
- `hidden_family_reveal_summary`
- `order_transform_summary`
- `example_rows`

This is one of the strongest Stable arena objects and should be treated as first-class aggregation input.

### 6.3 `top_compound_patterns`

Primary meaning:

- strongest compounded canonicals by section

Why it matters:

- explicitly preserves the compounded view instead of forcing later aggregation to reconstruct it indirectly

Important fields:

- `compound_score`
- `base_max_score`
- `set_chain_depth`
- `draw_chain_depth`
- `funnel_precol1`
- `vt_only_lane`
- `hot1_count`, `hot2_count`
- `col1_hits`
- `consensus_hits`
- `hidden3v_hits`
- `vtrac_straight_hits`
- `double_mirror_hits`
- `compound_why_tags`

### 6.4 `family_rollups_top`

Primary meaning:

- section-level family/lane rollups

Why it matters:

- this is the main Stable lane/family preservation surface
- it is the core reason Stable should not be judged only by tiny top-canonical accuracy

Important fields:

- `family_score_total`
- `family_score_max`
- `best_compound_score_max`
- `box_count`, `set_count`, `draw_count`, `column_count`
- `last_remaining_count`
- `progression_count`
- `dom_last_count`
- `consensus_count`
- `hidden3v_count`
- `vtrac_straight_count`
- `top_canonicals`
- `top_modal_orders`
- `breakdown_sums`
- `hidden_family_reveal_summary`
- `order_transform_summary`

### 6.5 `survivor_frontiers`

Primary meaning:

- where late/frontier survivor structure is still alive

Why it matters:

- survivor/frontier behavior is a primary predictive evidence class
- Stable must preserve it explicitly

Important fields:

- `frontier_column`
- `stable_box_rows`
- `frontier_family_count`
- `is_single_family`
- `family_ids`
- `entries`

This object matters a lot for later:

- col2 -> col1 tightening
- last surviving lane checks
- current-frontier alignment

### 6.6 `metrics_summary`

Primary meaning:

- compact health + winner-placement context

Why it matters:

- good for arena diagnostics
- good for example review
- should not be mistaken for a direct ranking surface

## 7. Stable-Specific Advanced Evidence Objects

These are the most important nuanced Stable additions from the final sweep.

### 7.1 Hidden-family / clutter-reveal

Status:

- **preserved in the arena**
- **inspection-oriented**
- **not yet promotion-ready by itself**

Why it matters:

- winner families can hide inside long cluttered strings
- winners artifacts showed this clearly
- Stable predictive artifacts already contained some of this truth, but not clearly enough

Current preserved surfaces:

- row-level `hidden_family_reveal`
- ledger/family `hidden_family_reveal_summary`
- source literals / source locators / fragments / anchors / reveal scores

What it means:

- Stable can explain **how** a family was being revealed inside longer strings

Important guardrail:

- keep it broad in the arena
- do **not** force it into a narrow direct promotion gate yet

### 7.2 Order / transform / VT-straight hints

Status:

- **preserved in the arena**
- **inspection-oriented**
- **bounded conversion experiments exist**
- **not yet a global promotion rule**

Why it matters:

- pattern order and transformation corridors are real
- Example 1 / `C035` made this explicit
- Stable often knows more about the winner corridor than the literal ranking suggests

Current preserved surfaces:

- row-level `order_transform_hints`
- ledger/family `order_transform_summary`
- transform seeds
- transform methods
- example transforms
- modal order support

Important transform families already preserved:

- `direct_perms`
- `vt8_expand_ordered`
- `pair_mirror_third_12`
- `double_mirror_single_6`
- `double_mirror_double_6`

Important guardrail:

- keep these in the arena now
- let later aggregated-arena learning decide what threshold or use case is actually predictive

### 7.3 Compounding ledger / box provenance

Status:

- **fully active arena evidence**

Why it matters:

- compounding must be inspectable
- otherwise later scoring cannot tell whether Stable is strong because of one row or because of a real multi-box progression

Current preserved surfaces include:

- `top_box_contributions`
- `score_breakdown_peaks`
- `compound_context`
- `frontier_summary`
- `example_rows`

This is a strong Stable contribution and should be used later in aggregation.

### 7.4 Survivor frontiers

Status:

- **fully active arena evidence**

Why it matters:

- lingering / surviving patterns are primary predictive evidence
- frontier arrival is part of currentness

Stable should remain the main string-tool source for:

- survivor-frontier inventory
- frontier-family cleanliness
- col1/col2 arrival logic

## 8. Stable Bounded Conversion Surfaces

These are important, but they are **not** the core Stable arena feed.

They belong in the “conversion helper” category.

| Method | Role | Current judgment |
|---|---|---|
| `stable_top` | top canonicals per section, BOX-expanded | keep as a bounded lens, not as a standalone oracle |
| `stable_compound_top` | bounded compound-based canonical pack | useful conversion helper, not the full Stable truth |
| `stable_family_vote` | legacy family-lane pack | bounded family preservation |
| `stable_family_vote_v2` | richer bounded family-lane rescue using arena evidence | worth keeping; meaningful preservation lift |
| `stable_last_remaining` | survivor/last-remaining bounded pack | useful bounded closure helper |

### `stable_family_vote_v2`

This deserves special mention because it was the main final Stable promotion improvement.

Why it matters:

- it rescued real family/lane preservation that the old top-family cut dropped
- it used richer Stable arena evidence instead of just raw family max

Primary promotion signals used:

- `family_score_total`
- `family_score_max`
- `best_compound_score_max`
- progression / survivor counts
- current/frontier counts, especially `Set1` + `Col1/Col2`
- arena-vs-legacy rank lift

Secondary corroborators:

- hidden-family reveal density
- order / transform density

Important judgment:

- worth keeping as a bounded conversion helper
- still not the same thing as the Stable arena contract itself

## 9. Stable's Final Strengths

Stable is strongest when treated as:

- a family/lane containment tool
- a compounding tool
- a survivor/frontier tool
- a hidden-family reveal tool
- a transform / VT-straight clue tool

Stable is especially powerful for:

- preserving the right family even when the winner canonical is absent
- surfacing long-cluster structure
- showing late/frontier behavior
- exposing transformation corridors around a family/lane

## 10. Stable's Final Non-Goals

Do **not** force Stable into:

- “top-3 canonicals should win often”
- one-scalar ranking only
- hidden-family reveal as an immediate production gate
- order-transform as an immediate production gate

Those are the wrong targets for this stage.

## 11. Stable -> Aggregated Arena Guidance

Later aggregated arena work should treat Stable as contributing:

- family / lane correctness
- compounding quality
- survivor/frontier pressure
- hidden-family recovery
- order / transform corridor clues

Good future aggregation questions:

- Does DR agree with Stable's lane/family story?
- Do VTRAC and Stable point to the same lane?
- Do Hot Zones confirm Stable's frontier arrival and Set1 tightening?
- Does Aux / Control Center confirm the same family via doubles, mirrors, badges, or profit alerts?

Stable should often be one of the main answers to:

- what family is really alive?
- what corridor is really surviving?
- what pattern cluster has the best progression quality?

## 12. Final Stable Judgment

Stable is wrapped for this phase as:

- a strong arena evidence producer
- not a tiny direct-caller oracle

The major Stable work that must remain visible in the aggregated arena is:

- row evidence
- compound ledgers
- family rollups
- survivor frontiers
- hidden-family reveal
- order / transform hints
- bounded family-lane rescue context

If these are preserved and later compared/fused correctly, Stable remains one of the strongest foundational string-tool feeds in AAT9.

## 13. Stable References

Primary references used for this Stable section:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Analyzer_Lean_Outputs.md`
- `scripts/tools/stable_arena.py`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_ANALYSIS_ARENA_INTEGRATION_QUEUE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-11__STABLE_FAMILY_VOTE_V2__VALIDATION.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__FEATURE_DECISIONS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__QUANT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__CASES.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_DEEP_EXAMPLE_REVIEW_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/SUPERBRAIN_PRIMITIVES.md`
