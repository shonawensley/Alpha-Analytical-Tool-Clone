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
| `Digit Reduction` | `complete` |
| `VTRAC Analyzer` | `complete` |
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

---

## Digit Reduction

## 1. Current Role

`Digit Reduction` should now be understood as:

- a structured reduction-trace evidence tool
- a pre-reduction cluster and reveal-quality tool
- a VTRAC-lane / corridor preservation tool
- a buried assigned-box lane discovery tool
- a bounded promotion helper for winner-lane visibility

It should **not** be judged mainly as:

- a tiny top-candidate literal caller
- a top-3-only direct winner oracle
- a fully solved final-combination selector

This is the most important DR conclusion from the final sweep.

The final DR read is:

- DR often already contains the right winner-family / VTRAC lane
- the main historical failure was collapsing that truth too early
- therefore the arena must preserve both the raw DR structure and the newer promotion surfaces, not just `top_candidates`

## 2. Canonical Predictive Sources

DR's canonical predictive-side brain bundle is:

- `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_per_item.csv`
- `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_top_candidates.csv`
- `data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_meta.json`
- `data/outputs/analysis/digit_reduction/<STATE>/training/<STATE>_digit_reduction_steps.csv`
- `data/outputs/analysis/digit_reduction/<STATE>/training/<STATE>_digit_reduction_logs.json`

DR's predictive arena artifact is:

- `sharepacks/_predictive/<D>/<STATE>/analysis/dr_arena*.json`
- `sharepacks/_predictive/<D>/<STATE>/analysis/dr_arena*.md`

Current downstream bounded helper packs still exist in Candidate Universe:

- `digit_reduction_analyzer_v2`
- `digit_reduction_envelope_steps`
- `digit_reduction_dr004`
- `digit_reduction_dr004_index`

These helpers remain useful, but they are **not** the full DR arena contract.

## 3. Audit-Only / Winners Lens

DR's truth-layer / audit surfaces should remain available for:

- post-results explanation
- gold-day review
- example anchoring
- promotion-gap diagnosis
- later aggregated-arena learning

Important DR truth / audit artifacts:

- winners HTML / overlay / JSON / stamps
- `scripts/tools/audit_dr_gold_day.py`
- `scripts/tools/compare_dr_promotion_anchor_groups.py`
- `scripts/tools/export_dr_promotion_gap_casepack.py`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-15__DR_GOLD_DAY_AUDIT__SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__DR_ARTIFACT_FIRST_REVIEW__REMAINING_ANCHORS.md`

These are not predictive inputs.
They are the truth lens that justified the final DR arena design.

## 4. DR's Final Predictive Meaning

DR contributes all of the following to the aggregated arena:

- family-trace evidence
- lane-only / VT-only evidence
- compact-literal and double-pressure evidence
- corridor evidence
- empty-vs-active discrimination
- pre-reduction cluster evidence
- reveal / purity evidence
- row-repeat and final-survival evidence
- fourth-variable / before-core evidence
- assigned-box buried-lane evidence
- bounded VTRAC promotion evidence

The crucial design rule is:

- **preserve first, promote later**

The old failure mode was collapsing DR to literal candidates too early.

## 5. DR Raw Evidence Families To Preserve

DR has four main predictive evidence layers:

1. Analyzer V2 row-level evidence
2. Analyzer V2 top-candidate family rollups
3. training / reduction progression evidence
4. meta / policy / diagnostics context

### 5.1 Analyzer V2 Row-Level Evidence

Source:

- `<STATE>_analyzer_v2_per_item.csv`

Primary semantic role:

- the most granular predictive DR evidence
- shows what family/pattern survived, how it reduced, and where it is living in the tables

Core row families that should be preserved or remain reachable:

| Field / family | Meaning in the arena |
|---|---|
| `variant`, `set_rank`, `draw_rank`, `col_rank`, `area_rank`, `method`, `mode`, `area` | exact location and currentness context |
| `pattern`, `family_id`, `box_id`, `final_value` | literal/family/assigned-box identity |
| `score`, `score_raw`, `score_v2`, `lockscore_v2` | DR row strength at different scoring stages |
| `final_linear`, `final_prob`, `lockscore_prob`, `lock_decision` | end-of-row confidence / lock context |
| `vt_only_lane`, `funnel_precol1`, `set1_terminal` | lane-only and current-frontier semantics |
| `ls_col_42`, `ls2_lane` | long-string column / lane context |
| `cluster_echo_count`, `variant_echo_count`, `set_echo_count` | repetition / convergence across boxes and variants |
| `box_family_density`, `dup_bonus`, `residual_purity` | compactness, duplicate pressure, and reveal cleanliness |
| `persistence_exact_score`, `persistence_vtrac_score` | literal vs VTRAC persistence comparison |
| `match_types`, `reasons_json` | semantic explanation tags |
| `dr.win_*` flags | audit-only winner-placement context |

#### Row score / structure families

These families are the main predictive DR row clues and should remain visible to the arena:

| Evidence family | Arena meaning |
|---|---|
| earliest-arrival / step behavior | how early the candidate family stabilizes under reduction |
| persistence | whether the candidate family survives multiple steps / segments |
| box density | whether the family is actually distributed across assigned boxes |
| cluster echoes | whether the same family/pattern repeats across locations |
| variant / set echoes | whether the same story is repeating across `Combined/Midday/Evening` or set chains |
| residual purity | whether clutter is being stripped away cleanly |
| literal vs VTRAC persistence split | whether the row is more exact-literal or more lane/family-led |
| currentness / frontier flags | whether the row is pressing into Set1 / Col1 / pre-Col1 |

These should not be collapsed into one scalar if we want the arena to reason well later.

### 5.2 Analyzer V2 Top-Candidate Family Rollups

Source:

- `<STATE>_analyzer_v2_top_candidates.csv`

Primary semantic role:

- bounded family rollups summarizing what Analyzer V2 would currently surface as direct candidates

Key fields:

| Field | Meaning |
|---|---|
| `rank` | bounded caller ordering, not the full arena truth |
| `best_pattern` | literal representative inside the family |
| `family_id` | family / lane identity |
| `score_v2` | aggregate bounded score |
| support counts | breadth of supporting traces |
| `evidence_tags` | compact semantic tags |
| `steps_summary` | compressed progression summary |
| `match_types` | `exact`, `vtrac`, `family_vtrac`, `drop_vtrac` taxonomy |

Important judgment:

- this file is still useful
- but it should be treated as a bounded caller/helper surface, not the canonical DR arena truth

### 5.3 Training / Reduction Progression Evidence

Sources:

- `<STATE>_digit_reduction_steps.csv`
- `<STATE>_digit_reduction_logs.json`

Primary semantic role:

- this is where DR becomes much richer than candidate ranking
- it preserves how values shrink, when a 3-value core appears, and what survives before/after that reveal

Important progression families that should remain preserved or reconstructable:

| Evidence family | Meaning |
|---|---|
| step-0 / precluster state | the larger pre-reduction pool before reveal |
| `first_3value_step` | when the row first becomes core-like |
| `last_change_step` | how long the row stays stable |
| `final_value` | terminal reduction result |
| before-core vs core comparison | reveal / clutter-removal semantics |
| repeated 3-value rows | row-repeat / final-survival evidence |
| same core with extra digits | fourth-variable / hidden-extra evidence |
| location + area + method + mode | provenance of the reduction path |

This layer is the main source for:

- `precluster_ledger`
- `reduction_reveal_ledger`
- `row_repeat_and_final_survival`
- `box_validity_ledger`
- `fourth_variable_candidates`

### 5.4 Meta / Policy / Diagnostics Context

Sources:

- `<STATE>_analyzer_v2_meta.json`
- the mirrored `meta` section in `dr_arena*.json`

Primary semantic role:

- tool health
- config integrity
- audit context

Important fields:

| Field | Meaning |
|---|---|
| `cluster_scan` | cluster-scan settings and assumptions |
| `scoring_v2` | scoring configuration |
| `lockscore` | lockscore policy context |
| `policy` | analyzer policy / diagnostics flags |
| `inputs_hash` | reproducibility / frozen input identity |

Meta is primarily for audit and calibration, not direct promotion.

## 6. DR Arena Objects That Should Feed The Aggregated Arena

The DR arena artifact is the most important predictive-to-arena bridge.

Source:

- `analysis/dr_arena*.json`

### 6.1 `summary`

Primary meaning:

- compact section-level health and context

Why it matters:

- gives later aggregation the shape of the DR environment before reading detailed objects

Important preserved fields:

- `per_item_rows`
- `raw_exposure_count`
- `path_summary_count`
- `top_candidate_rows`
- `training_locations`
- `unique_patterns`
- `unique_families`
- `max_score_v2`
- `top_candidate_preview`

### 6.2 `dr_trace_strength`

Primary meaning:

- strongest family-level DR traces by section

Why it matters:

- preserves the main family story before lane-only and VTRAC promotion layers are applied

Important preserved fields:

- `family_id`
- `trace_rank`
- `trace_score`
- `score_total`, `score_max`
- `rows`, `box_count`
- `currentness_max`, `currentness_avg`
- `variant_echo_max`, `set_echo_max`
- `top_patterns`
- `sample_locators`
- `why_tags`

### 6.3 `dr_lane_only_confidence`

Primary meaning:

- rows/families that are more VTRAC-lane-led than exact-literal-led

Why it matters:

- one of the major DR truths is that the right lane is often alive before the literal is clean

Important preserved fields:

- `family_id`
- `lane_confidence_score`
- `vtrac_bias_total`
- `vt_only_rows`
- `box_family_density_max`
- `cluster_echo_max`
- `currentness_max`
- `lane_confidence_reason`
- `top_patterns`

### 6.4 `dr_competing_literal_pressure`

Primary meaning:

- compact literal rivals that can steal attention from the correct lane

Why it matters:

- this is the main “wrong compact attractor” lens
- it should be preserved so later arena reasoning can compare correct lane truth vs noisy literal sharpness

Important preserved fields:

- `pattern`
- `pressure_score`
- `score_total`, `score_max`
- `rows`, `box_count`
- `dup_bonus_total`, `dup_bonus_max`
- `funnel_rows`, `set1_terminal_rows`
- `top_candidate_ranks`
- `family_id`
- `mirror_pattern`
- `vtrac_signature`

### 6.5 `dr_double_pressure`

Primary meaning:

- duplicate / double-led compact literal pressure

Why it matters:

- doubles are a meaningful DR-specific rival family and often shape the local corridor

Important preserved fields:

- `pattern`
- `double_score`
- `duplicate_depth`
- `mirror_pattern`
- `rows`, `box_count`
- `dup_bonus_total`
- `family_id`
- `vtrac_signature`

### 6.6 `dr_corridor_strength`

Primary meaning:

- DR’s predictive-side corridor model

Why it matters:

- this is the clean predictive home for current-day corridors, family neighborhoods, compact-double corridors, and VTRAC corridors

Important preserved fields:

- `family_id`
- `corridor_strength_score`
- `corridor_scope`
- `corridor_band`
- `corridor_variant_profile`
- `raw_exposure_count`
- `path_summary_count`
- `neighbor_box_support`
- `consecutive_box_progression`
- `family_neighborhood_saturation`
- `family_asymmetry_inside_corridor`
- `currentness_max`
- `top_patterns`
- `sample_locators`

Important scope meanings:

| Scope | Meaning |
|---|---|
| `exact_corridor` | literal/family corridor is narrow and exact-led |
| `family_neighborhood` | several nearby family members are alive together |
| `compact_double_corridor` | double-driven compact corridor |
| `vtrac_corridor` | corridor is lane-led and more VTRAC than literal |

Important band meanings:

| Band | Meaning |
|---|---|
| `set1_current_day` | corridor is pressing into current-day / Set1 frontier |
| `7_6_5_band` | corridor is living deeper in the older column band |
| `mixed` | corridor is spread across both |

### 6.7 `dr_empty_lens`

Primary meaning:

- whether DR is truly empty, structurally alive but low-trust, or positively alive

Why it matters:

- this fixed one of the biggest DR interpretation failures

Important preserved fields:

- `classification`
- `is_sparse`
- `confidence`
- `positive_signal_score`
- `reasons`
- `cold_location_count`
- `cold_ratio`
- `raw_exposure_count`
- `path_summary_count`

Important classifications:

| Class | Meaning |
|---|---|
| `true_empty` | genuinely sparse / dead environment |
| `active_low_trust` | environment is alive but weak, messy, or under-revealed |
| `positive_trace` | environment is structurally live and worth preserving strongly |

### 6.8 `dr_structural_signals`

Primary meaning:

- compact section-level structural truth derived from progression and reveal ledgers

Why it matters:

- this is where several example-review insights were absorbed without exploding the schema

Important preserved fields:

- `raw_exposure_count`
- `path_summary_count`
- `early_activation_strength`
- `early_activation_hits`
- `consecutive_box_progression`
- `neighbor_box_support`
- `family_neighborhood_saturation`
- `family_asymmetry_inside_corridor`
- `core_vs_clutter_transit_score`
- `reveal_purity`
- `pre_reduction_cluster_strength`
- `candidate_preview_count`
- `overlay_summary_mismatch`

This object should remain broad; it is a major DR contribution to the aggregated arena.

### 6.9 `dr_vtrac_lane_gateway`

Primary meaning:

- first structured VTRAC-lane aggregation over DR family, pattern, candidate, and corridor evidence

Why it matters:

- this was the first successful attempt to promote lane semantics without collapsing DR to literal ranking

Important preserved fields:

- `vtrac_index`
- `gateway_score`
- `member_count`
- `rows_total`, `box_total`
- `candidate_count`
- `candidate_rank_bonus`
- `vt_only_rows`
- `vtrac_bias_total`
- `currentness_max`
- `corridor_strength_max`
- `top_families`
- `top_patterns`
- `scope_mix`
- `band_mix`
- `why_tags`

### 6.10 `dr_vtrac_cluster_strength`

Primary meaning:

- richer winner-lane aggregation across trace, lane, corridor, gateway, double, row-repeat, and fourth-variable evidence

Why it matters:

- this became the main visible-lane promotion keeper

Important preserved fields:

- `vtrac_index`
- `cluster_score`
- `raw_cluster_score`
- `cluster_adjustment`
- `support_class_count`
- `support_classes`
- `member_family_count`
- `member_pattern_count`
- score components:
  - `trace_score_component`
  - `lane_score_component`
  - `corridor_score_component`
  - `gateway_score_component`
  - `double_score_component`
  - `row_repeat_score_component`
  - `fourth_score_component`
- `currentness_max`
- `top_families`
- `top_patterns`
- `scope_mix`
- `band_mix`
- `why_tags`

Important judgment:

- keep this as a strong arena object
- do not mistake it for a final combination selector

### 6.11 `dr_assigned_box_vtrac_strength`

Primary meaning:

- winner-lane isolation directly from long assigned-box strings and bounded final-value windows

Why it matters:

- this was the first strong buried-regime breakthrough
- it validated the assigned-box / long-string thesis directly

Important preserved fields:

- `vtrac_index`
- `assigned_box_score`
- `row_count`
- `box_count`
- `column_count`
- `window_count`
- `currentness_max`
- `box_pair_agree_max`
- `cluster_echo_max`
- `variant_echo_max`
- `top_windows`
- `top_boxes`
- `column_mix`
- `method_mix`
- `mode_mix`
- `why_tags`

Important guardrail:

- the `3-digit windows` are only a VTRAC-mapping lens inside the longer assigned-box strings
- they do **not** replace the longer cluster/progression truth

### 6.12 `dr_vtrac_fusion_strength`

Primary meaning:

- bounded agreement / rescue fusion across gateway, cluster, and assigned-box

Why it matters:

- it gave a modest but real final lift without flattening the open arena model

Important preserved fields:

- `vtrac_index`
- `fusion_score`
- `agreement_bonus`
- `rescue_bonus`
- `penalty`
- `gateway_rank`, `cluster_rank`, `assigned_box_rank`
- score components:
  - `gateway_score_component`
  - `cluster_score_component`
  - `assigned_box_score_component`
- `box_rows`
- `box_count`
- `column_count`
- `box_currentness_max`
- `box_cluster_echo_max`
- `box_variant_echo_max`
- `top_families`
- `top_patterns`
- `top_windows`
- `why_tags`

Important judgment:

- keep it as a bounded helper surface
- do not let it replace assigned-box or cluster as the core evidence sources

### 6.13 `dr_row_repeat_and_final_survival`

Primary meaning:

- repeated 3-value-like rows and terminal survival objects

Why it matters:

- row-repeat / terminal survival is one of DR’s most important progression clues

Important preserved fields:

- `value`
- `rows_repeated`
- `location_count`
- `terminal_hits`
- `currentness_max`
- `score`
- `top_methods`
- `top_modes`
- `top_sections`
- `examples`
- `is_duplicate_pattern`
- `vtrac_signature`

### 6.14 `precluster_ledger`

Primary meaning:

- strongest pre-reduction cluster states before the first 3-value-like reveal

Why it matters:

- this preserves the “bigger truth before reveal” that many DR examples depended on

Important preserved fields:

- `location`
- `step0_value`
- `step0_length`
- `step0_unique_digits`
- `first_3value_step`
- `last_change_step`
- `final_value`
- `currentness_score`
- `precluster_score`

### 6.15 `reduction_reveal_ledger`

Primary meaning:

- reveal quality from the step just before the first 3-value core to the core itself

Why it matters:

- this is the main predictive-side home for clutter-removal and purity-gain reasoning

Important preserved fields:

- `location`
- `core_step`
- `before_value`
- `core_value`
- `final_value`
- `purity_gain`
- `reveal_score`
- `currentness_score`

### 6.16 `box_validity_ledger`

Primary meaning:

- location-level inventory of where valid 3-value reveals exist and how current they are

Why it matters:

- this is one of the best sources for box-progression, currentness, and neighbor-box structure

Important preserved fields:

- `location`
- `set`
- `draw`
- `column`
- `first_3value_step`
- `last_change_step`
- `steps_total`
- `final_value`
- `has_3value_reveal`
- `currentness_score`

### 6.17 `fourth_variable_candidates`

Primary meaning:

- cases where one or two “extra” digits sit just outside a core 3-value pattern

Why it matters:

- this preserves a controlled version of the “hidden behind one digit / extra variable” idea

Important preserved fields:

- `core_value`
- `extra_digits`
- `extra_vtrac_digits`
- `support_count`
- `location_count`
- `currentness_max`
- `score`
- `top_methods`
- `top_modes`
- `top_sections`
- `examples`

## 7. DR-Specific Advanced Evidence Objects And Final Learnings

These are the most important nuanced DR additions from the final sweep.

### 7.1 `dr_empty_lens` and the false-empty split

Status:

- **fully active arena evidence**
- **major keeper**

Why it matters:

- the old sparse/not-sparse framing was not good enough
- Virginia `473` and later examples showed many rows were “false empty,” not dead

Current preserved distinction:

- `true_empty`
- `active_low_trust`
- `positive_trace`

Important guardrail:

- aggregated arena work should use this as context and confidence
- not as a hard delete gate by itself

### 7.2 Corridor / structural model

Status:

- **fully active arena evidence**

Why it matters:

- this is where the major example-review lessons were absorbed without blowing up the schema

This layer now preserves:

- current-day exact corridors
- family-neighborhood saturation
- compact corridor-inside-family
- progression quality
- neighbor-box support
- core-vs-clutter transit

### 7.3 Assigned-box buried-lane discovery

Status:

- **fully active arena evidence**
- **major keeper**

Why it matters:

- the winner-aware lab proved many buried misses were really assigned-box lane-isolation misses
- this was the first strong buried-regime breakthrough

Important judgment:

- the arena should preserve this surface broadly
- later aggregation can decide when it should outweigh more visible but noisier literal surfaces

### 7.4 Bounded VTRAC fusion

Status:

- **kept**
- **modest bounded helper**
- **not a replacement surface**

Why it matters:

- agreement between assigned-box and cluster/gateway is real
- guarded rescue is sometimes real

Important guardrail:

- do not expand this into another giant retuning loop

### 7.5 Winner-artifact-first process shift

Status:

- **methodological keeper**

Why it matters:

- this was the process change that finished DR well

The effective loop was:

1. freeze multi-window gold-day benchmarks
2. inspect winners HTML / overlay directly
3. compare winner corridor vs losing attractor
4. derive explicit scoring hypotheses
5. rerun the same frozen windows
6. keep or reject the bounded change

This process matters because it produced:

- assigned-box discovery
- broader top-band interpretation instead of narrow `top3` panic
- cleaner rejection of weak rerankers

## 8. DR Bounded Downstream Helper Surfaces

These are important, but they are **not** the core DR arena feed.

They belong in the “conversion helper” category.

| Method | Role | Current judgment |
|---|---|---|
| `digit_reduction_analyzer_v2` | bounded top-candidate direct pack from Analyzer V2 | keep as a helper, not the full DR truth |
| `digit_reduction_envelope_steps` | early-step / reduced-pool BOX helper | useful bounded experiment/helper |
| `digit_reduction_dr004` | segment-pool / breadth / cross-variant BOX helper | useful bounded helper, not the arena contract |
| `digit_reduction_dr004_index` | one-per-index gateway BOX helper | useful bounded index helper |

Important judgment:

- these helpers remain useful for downstream experimentation
- but the aggregated arena should reason from the richer DR evidence first

## 9. DR's Final Strengths

DR is strongest when treated as:

- a reduction-trace evidence tool
- a lane/corridor preservation tool
- a reveal-quality / clutter-removal tool
- a buried assigned-box lane-discovery tool
- a bounded promotion helper for winner-lane visibility

DR is especially powerful for:

- preserving the right VTRAC lane even when the literal stays noisy
- separating live-but-low-trust from truly empty
- showing how a 3-value core emerged
- exposing row-repeat / final-survival structure
- showing when the winner-family corridor is living inside assigned boxes

## 10. DR's Final Non-Goals

Do **not** force DR into:

- “top-3 candidates should win often”
- one-scalar literal ranking only
- another open-ended generic reranker loop
- forced replacement of assigned-box / cluster by fusion
- broad retuning just because a narrow residual miss class remains

Those are the wrong targets for this stage.

## 11. DR -> Aggregated Arena Guidance

Later aggregated arena work should treat DR as contributing:

- reduction-path truth
- lane/corridor correctness
- clutter-vs-core transition quality
- row-repeat / terminal survival
- buried assigned-box winner-lane evidence
- bounded promotion signals about whether that lane is becoming visible

Good future aggregation questions:

- Does Stable agree with DR’s family/lane story?
- Does VTRAC agree with DR’s promoted or buried lane?
- Do Hot Zones confirm the same corridor through vertical pressure and col1/col2 tightening?
- Do Aux / Control Center features reinforce the same family via doubles, badges, due pressure, or alerts?
- Are assigned-box lane and other tool signals converging on the same VTRAC neighborhood?

DR should often be one of the main answers to:

- what lane is alive even if the literal is messy?
- is this environment truly dead or just under-revealed?
- where did the 3-value core actually come from?
- is the winner-family corridor being hidden inside the assigned boxes?

## 12. Final DR Judgment

DR is wrapped for this phase as:

- a strong arena evidence producer
- not a tiny direct-caller oracle

The major DR work that must remain visible in the aggregated arena is:

- row-level reduction evidence
- family and pattern aggregates
- corridor and structural signals
- empty-lens distinctions
- row-repeat / final-survival evidence
- precluster and reveal ledgers
- assigned-box buried-lane discovery
- bounded VTRAC promotion / fusion context

If these are preserved and later compared/fused correctly, DR remains one of the most important foundational string-tool feeds in AAT9.

The remaining true DR-local gap is now narrow:

- same-index permutation-swarm cases

That is no longer a broad reason to reopen DR.

## 13. DR References

Primary references used for this DR section:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Analyzer_Lean_Outputs.md`
- `scripts/tools/dr_arena.py`
- `scripts/tools/audit_dr_gold_day.py`
- `scripts/tools/compare_dr_promotion_anchor_groups.py`
- `scripts/tools/export_dr_promotion_gap_casepack.py`
- `scripts/tools/create_candidate_universe.py`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_ANALYSIS_ARENA_INTEGRATION_QUEUE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_ARENA_V1_1__LOCK_IN.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-15__DR_GOLD_DAY_AUDIT__SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__DR_WRAP_UP__HANDOFF.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__DR_ARTIFACT_FIRST_REVIEW__REMAINING_ANCHORS.md`

---

## VTRAC Analyzer

## 1. Current Role

`VTRAC Analyzer` should now be understood as:

- a lane / index evidence tool
- a straight-neighborhood witness tool
- a cross-section corroboration tool
- a right-column / stable-column context tool
- a mask-drop, mirror, and double-support clue tool

It should **not** be judged mainly as:

- a tiny top-k direct straight caller
- a standalone exact-winner oracle
- a substitute for later cross-tool aggregation

This is the most important VTRAC conclusion from the final sweep.

The final VTRAC read is:

- VTRAC is strongest when preserving the correct winner lane / neighborhood
- VTRAC loses value when forced into a tiny direct-caller role
- therefore the arena must preserve both the semantic rollups and the concrete descriptor families that make those rollups inspectable

## 2. Canonical Predictive Sources

VTRAC's canonical predictive-side state bundles are:

- `sharepacks/_predictive/<D>/<STATE>/vtrac/<STATE>/<STATE>_vtrac_enhanced_*.json`

VTRAC's canonical global compact layer is:

- `sharepacks/<D>/vtrac_compact_report.json`
- `sharepacks/<D>/vtrac_compact_report.csv`

Important judgment:

- the enhanced JSON is the state-level predictive SSOT
- the compact report is the global aggregator-style feed artifact
- there is **not** currently a dedicated standalone `vtrac_arena*.json`
- so the aggregated arena should preserve VTRAC by ingesting from these predictive artifacts or future mirrored arena exports, not by narrowing VTRAC to a tiny helper pack

Current downstream bounded helper surfaces in Candidate Universe are:

- `vtrac_top_straights`
- `signals_bundle.vtrac_enhanced.top_indices`
- `signals_bundle.vtrac_enhanced.top_straights`

These bounded surfaces are useful, but they are **not** the full VTRAC arena contract.

## 3. Audit-Only / Winners Lens

VTRAC's truth-layer / audit surfaces should remain available for:

- post-results explanation
- gold-day review
- winner-lane confirmation
- same-index neighborhood review
- later aggregated-arena learning

Important VTRAC truth / audit artifacts:

- winners HTML / analyzer-style winners overlays
- winners JSON / winner placement diagnostics
- `scripts/tools/validate_vtrac_compact_report.py`
- compact-report validation summaries
- winner-layer pattern families:
  - `pattern_occurrence`
  - `pattern_persistence`
  - `pattern_stability`
  - `straight_counts`

These are not predictive inputs.
They are the truth lens that justified the final VTRAC arena design.

## 4. VTRAC's Final Predictive Meaning

VTRAC contributes all of the following to the aggregated arena:

- ranked index / lane evidence
- ranked straight witnesses inside those lanes
- cross-section echo
- hot / superhot lane support
- consensus-col1 / consensus-col2 rescue context
- right-column / stable-column context
- mask-drop reveal clues
- mirror and double-support clues
- same-index neighborhood structure
- section-led vs state-led lane balance

The crucial design rule is:

- **preserve first, compress later**

The old failure mode was collapsing VTRAC too early into small top-straight lists.

## 5. VTRAC Raw Evidence Families To Preserve

VTRAC has five main predictive evidence layers:

1. ranked index / lane evidence
2. ranked straight-neighborhood evidence
3. section summary evidence
4. compact global descriptor evidence
5. telemetry / validator context

### 5.1 Ranked Index / Lane Evidence

Source:

- `<STATE>_vtrac_enhanced_*.json`
  - `indices_ranked`

Primary semantic role:

- the most direct predictive VTRAC lane inventory
- shows which VTRAC indices are alive, how strong they are, and what straight witnesses sit inside them

Core lane fields that should be preserved or remain reachable:

| Field / family | Meaning in the arena |
|---|---|
| `indices_ranked[].index` | VTRAC lane identity |
| `indices_ranked[].score` | lane strength at the state level |
| `indices_ranked[].evidence` | human-readable lane evidence tags |
| `indices_ranked[].straights` | example straights supporting the lane |

Important judgment:

- this is lane truth, not a direct pick list
- the arena should preserve both the ranked index and the evidence families behind it

### 5.2 Ranked Straight-Neighborhood Evidence

Sources:

- `<STATE>_vtrac_enhanced_*.json`
  - `straights_ranked`
  - `top_straights`

Primary semantic role:

- bounded straight witnesses living inside the lane environment
- useful for showing how the lane is expressing itself, including same-index asymmetry and shoulder activity

Core straight fields that should be preserved or remain reachable:

| Field / family | Meaning in the arena |
|---|---|
| `straights_ranked[].straight` | literal straight witness |
| `straights_ranked[].index` | VTRAC lane that straight belongs to |
| `straights_ranked[].score` | straight witness strength |
| `straights_ranked[].reasons` | why that straight is being surfaced |
| `top_straights` | compact straight witness list |

Important judgment:

- the point is not “top-k straights should directly win often”
- the point is that the straight list exposes the lane neighborhood and the internal shape of the winner lane

### 5.3 Section Summary Evidence

Source:

- `<STATE>_vtrac_enhanced_*.json`
  - `section_summaries`

Primary semantic role:

- cross-section corroboration
- right-column and hot/superhot context
- per-section lane pressure shape

Important fields:

| Field | Meaning |
|---|---|
| `section_summaries.<section>.hot_count` | hot pressure in that section |
| `section_summaries.<section>.superhot_count` | superhot pressure in that section |
| `section_summaries.<section>.consensus_col1` | current-frontier consensus reinforcement |
| `section_summaries.<section>.consensus_col2` | pre-frontier consensus reinforcement |
| `section_summaries.<section>.stable_columns` | stable/right-column footprint |
| `section_summaries.<section>.top_box_signatures` | dominant box / lane signatures |
| `section_summaries.<section>.ring_votes` | section-level lane votes |
| `section_summaries.<section>.analyzer_metrics.indices_considered` | section breadth / lane inventory |
| `section_summaries.<section>.analyzer_metrics.mask_drop_count` | mask-drop reveal density |
| `section_summaries.<section>.analyzer_metrics.reduction_hits` | reduction-linked support |
| `section_summaries.<section>.analyzer_metrics.mirror_supported` | mirror support present |
| `section_summaries.<section>.analyzer_metrics.double_hits` | double support present |
| `section_summaries.<section>.analyzer_metrics.top_straights` | strongest straight witnesses inside the section |

These section summaries are one of the main reasons VTRAC should be treated as a cross-variant lane lens instead of a narrow top-straight caller.

### 5.4 Compact Global Descriptor Evidence

Sources:

- `sharepacks/<D>/vtrac_compact_report.json`
- `sharepacks/<D>/vtrac_compact_report.csv`

Primary semantic role:

- a compact, global, aggregator-style VTRAC descriptor layer across states
- a very useful bridge between the deeper enhanced JSON bundles and the later aggregated arena

Important fields:

| Field | Meaning |
|---|---|
| `overlap` | degree of cross-section overlap behind the lane |
| `stable_cols_count`, `stable_cols` | right-column / stable-column concentration |
| `consensus_col1`, `consensus_col2` | frontier and pre-frontier rescue context |
| `cross_section_echo` | lane repeating across sections |
| `hot_count`, `superhot_count` | hot / superhot lane support |
| `mask_drop` | masked / clutter-drop reveal context |
| `mirror_supported` | mirror corroboration |
| `double_hits` | double corroboration |
| `confidence_score` | compact global confidence |
| `tier`, `flags` | compact classification / interpretation helpers |
| `top_tokens`, `recommended_tokens` | key lane descriptors / recommended tokens |
| `top_straights` | compact straight witness list |
| `section_prior`, `state_prior` | section-led vs state-led pressure hints |
| `why` | compact human-readable explanation |
| `source` | provenance / source-path context |

Important judgment:

- this compact layer should be preserved as a concrete descriptor family
- it is not just a debugging export
- it is also not a replacement for the deeper enhanced JSON

### 5.5 Telemetry / Validator Context

Sources:

- `<STATE>_vtrac_enhanced_*.json`
  - `telemetry`
- `scripts/tools/validate_vtrac_compact_report.py`

Primary semantic role:

- tool health
- scorer / mask context
- reproducibility
- validator-level sanity

Important fields:

| Field | Meaning |
|---|---|
| `telemetry.weights` | scoring-weight provenance |
| `telemetry.mask_digits` | mask / reveal configuration context |
| compact-report `states`, `sections`, `scorer_version` | non-empty global aggregator-feed validation |

This layer is primarily for audit and calibration, not direct promotion.

## 6. VTRAC Arena Objects That Should Feed The Aggregated Arena

VTRAC does not currently have a dedicated standalone predictive `vtrac_arena*.json`.

So the aggregated arena should preserve the following semantic objects as rollups
over the raw evidence families above.

Important guardrail:

- these semantic objects should **not** replace the concrete payload families
- they should sit on top of them

### 6.1 `cross_variant_lane_strength`

Primary meaning:

- how strongly the same VTRAC lane is alive across sections / variants

Why it matters:

- this is the core VTRAC contribution
- it preserves lane correctness before later aggregation narrows anything

It should be backed by:

- `indices_ranked`
- `cross_section_echo`
- `ring_votes`
- section-level lane summaries

### 6.2 `right_column_lane_stability`

Primary meaning:

- right-column / stable-column support behind a lane

Why it matters:

- winners review repeatedly showed right-column stability is part of why certain lanes deserve attention

It should be backed by:

- `stable_cols_count`
- `stable_cols`
- `section_summaries.<section>.stable_columns`
- consensus-col1 / consensus-col2 context when relevant

### 6.3 `vt_only_lane_confidence`

Primary meaning:

- confidence that the lane is alive even if the literal expression is still noisy

Why it matters:

- this keeps VTRAC in its correct role as a lane-neighborhood lens rather than a literal-only caller

It should be backed by:

- `indices_ranked[].score`
- `indices_ranked[].evidence`
- section priors
- same-index straight neighborhood shape

### 6.4 `straight_lane_quality`

Primary meaning:

- how convincing the bounded straight witnesses are inside the lane

Why it matters:

- the straight list matters, but as witness structure inside the lane, not as a top-k oracle

It should be backed by:

- `straights_ranked`
- `top_straights`
- section-summary `top_straights`
- straight reasons

### 6.5 `lane_dominance`

Primary meaning:

- whether one lane is truly dominating, or whether the environment is flatter / noisier

Why it matters:

- later aggregation needs to know whether VTRAC is speaking clearly or only softly

It should be backed by:

- ranked-index score gaps
- `overlap`
- `confidence_score`
- `tier`, `flags`
- section/state priors

### 6.6 `section_lead_profile`

Primary meaning:

- whether the lane is Combined-led, Midday-led, Evening-led, or broadly shared

Why it matters:

- this is one of VTRAC’s distinctive environment clues
- it helps later aggregation understand timing/currentness shape without forcing a narrow caller policy

It should be backed by:

- `section_summaries`
- `section_prior`
- `state_prior`
- `ring_votes`

### 6.7 `mask_drop_lane_reveal`

Primary meaning:

- whether clutter-drop / mask logic is helping reveal the lane

Why it matters:

- this is one of the important “winner was there but partly hidden” clues

It should be backed by:

- `mask_drop`
- `telemetry.mask_digits`
- `mask_drop_count`
- related index / straight evidence

### 6.8 `mirror_double_lane_support`

Primary meaning:

- whether mirror and double behavior are reinforcing the lane

Why it matters:

- mirror/double support is often part of why a lane is structurally persuasive even before a literal surfaces cleanly

It should be backed by:

- `mirror_supported`
- `double_hits`
- section analyzer metrics
- straight witness reasons when present

## 7. VTRAC-Specific Advanced Evidence Objects And Final Learnings

These are the most important nuanced VTRAC conclusions from the final sweep and the artifact-first confirmation.

### 7.1 Same-index neighborhood structure

Status:

- **fully preserved in the arena contract**
- **not reducible to one lane boolean**

Why it matters:

- winner artifacts showed that strong lanes often contain internal asymmetry
- one or two same-index straights can dominate while others are only shoulder support

Important examples:

- `Virginia4 473` / index `30`
- `Florida4 611` / index `16`

Important guardrail:

- keep same-index straight neighborhoods visible
- do **not** collapse them to “lane alive / lane dead”

### 7.2 Compact descriptor layer

Status:

- **fully preserved in the arena contract**
- **major keeper**

Why it matters:

- the compact report is the cleanest cross-state/global VTRAC descriptor surface
- it gives later aggregation a practical bridge without reopening the full analyzer bundle first

Important judgment:

- preserve the compact descriptor families
- do not demote them to throwaway debug output

### 7.3 Winners-lens correspondence

Status:

- **audit-only**
- **methodological keeper**

Why it matters:

- winner-layer families like `pattern_occurrence`, `pattern_persistence`, `pattern_stability`, and `straight_counts` were the truth layer that justified the predictive contract

Important guardrail:

- keep those winner families outside predictive mode
- use them for review, confirmation, and future aggregation learning

### 7.4 Winner-artifact-first confirmation

Status:

- **methodological keeper**

Why it matters:

- the `2026-03-17` confirmation pass showed the earlier VTRAC handoff was directionally right but too compressed
- the correct fix was broader contract preservation, not another scorer loop

This matters because it established:

- no broad retune was justified
- more concrete payload families needed to be preserved
- VTRAC is ready for arena handoff when treated as a semantic lane feed

## 8. VTRAC Bounded Downstream Helper Surfaces

These are important, but they are **not** the core VTRAC arena feed.

They belong in the “conversion helper / bounded consumer” category.

| Method | Role | Current judgment |
|---|---|---|
| `vtrac_top_straights` | bounded straight pack from `straights_ranked` | keep as a helper, not the full VTRAC truth |
| `signals_bundle.vtrac_enhanced.top_indices` | compact top-index signals for later bundle fusion | keep as a bounded bundle surface |
| `signals_bundle.vtrac_enhanced.top_straights` | compact straight witnesses for later bundle fusion | keep as a bounded bundle surface |

Important judgment:

- these helpers remain useful for downstream experimentation
- but the aggregated arena should reason from the richer VTRAC evidence first

## 9. VTRAC's Final Strengths

VTRAC is strongest when treated as:

- a lane / index correctness tool
- a same-index straight-neighborhood tool
- a cross-section corroboration tool
- a right-column / hot / superhot descriptor tool
- a mask-drop / mirror / double support clue tool

VTRAC is especially powerful for:

- preserving the right winner lane even when literal callers stay noisy
- showing same-index neighborhood asymmetry
- showing section-led vs state-led lane pressure
- exposing right-column and hot/superhot reinforcement
- giving later aggregation a compact but meaningful lane descriptor layer

## 10. VTRAC's Final Non-Goals

Do **not** force VTRAC into:

- “top-k straights should directly win often”
- another broad overlap-vs-rescue scorer retune loop
- replacement of later cross-tool aggregation
- collapsing the compact descriptor layer into one scalar
- treating winners-layer stats as predictive inputs

Those are the wrong targets for this stage.

## 11. VTRAC -> Aggregated Arena Guidance

Later aggregated arena work should treat VTRAC as contributing:

- lane correctness
- same-index neighborhood structure
- right-column stability
- hot/superhot lane support
- section-lead timing/currentness shape
- mask-drop / mirror / double corroboration
- compact global descriptors that make the lane legible across states

Good future aggregation questions:

- Does Stable agree with the same family/lane neighborhood VTRAC is surfacing?
- Does DR's buried assigned-box lane story match the VTRAC lane?
- Does Hot Zones show pressure surviving in the same lane neighborhood?
- When VTRAC lane quality is high but literal candidates are mixed, which other tools confirm the lane rather than the literal?

VTRAC should often be one of the main answers to:

- what lane / family neighborhood is actually alive?
- is the lane being reinforced in the right columns and sections?
- are the strongest straight witnesses clustered coherently inside the lane?
- is the lane being revealed by mask-drop, mirror, or double support?

## 12. Final VTRAC Judgment

VTRAC is wrapped for this phase as:

- a strong arena lane-semantics producer
- not a tiny direct-caller oracle

The major VTRAC work that must remain visible in the aggregated arena is:

- ranked indices and ranked straights
- section summaries
- compact descriptor families
- same-index neighborhood structure
- right-column and hot/superhot context
- mask-drop, mirror, and double corroboration
- audit-only winner correspondence

If these are preserved and later compared/fused correctly, VTRAC remains one of the main string-tool sources for understanding the correct winner neighborhood.

The remaining true VTRAC-local gap is now narrow:

- arena consumption and later cross-tool use

That is no longer a broad reason to reopen VTRAC scoring.

## 13. VTRAC References

Primary references used for this VTRAC section:

- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Analyzer_Lean_Outputs.md`
- `scripts/tools/create_candidate_universe.py`
- `scripts/tools/validate_vtrac_compact_report.py`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__VTRAC__HANDOFF.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__VTRAC_HOTZ__ASSESSMENT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__VTRAC_HOTZ__ARENA_CONTRACT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-17__VTRAC_HOTZ__ARTIFACT_FIRST_CONFIRMATION.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_ANALYSIS_ARENA_INTEGRATION_QUEUE.md`
