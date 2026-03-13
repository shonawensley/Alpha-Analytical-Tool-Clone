# DR Super Harness Case - 2026-01-06 - NewJersey4 - Evening - 942

## 1. Case Header

| Field | Value |
|---|---|
| Date | `2026-01-06` |
| State | `NewJersey4` |
| Draw | `Evening` |
| Winner literal | `942` |
| Winner canonical | `249` |
| Winner VTRAC family/index | winners lens `vtrac31`; DR local index `74` |
| Batch label | `B2-B` |
| Reviewer | `Codex` |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | `sharepacks/2026-01-06/NewJersey4/winners/NewJersey4/NewJersey4_vtrac31_winner_942_20260107_052306.html` |
| Winners JSON | `sharepacks/2026-01-06/NewJersey4/winners/NewJersey4/NewJersey4_vtrac31_winner_942_20260107_052306.json` |
| Winners overlay | `sharepacks/2026-01-06/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/winners/20260107_Evening_winner_overlay.html` |
| Winner stamp | `sharepacks/2026-01-06/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/winners/20260107_Evening_winner_stamp.json` |
| Winner flags | `sharepacks/2026-01-06/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/winners/20260107_Evening_winner_flags.csv` |
| Winner hits | `sharepacks/2026-01-06/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/winners/20260107_Evening_winner_hits.csv` |
| DR per_item | `sharepacks/2026-01-06/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/NewJersey4_analyzer_v2_per_item.csv` |
| DR top_candidates | `sharepacks/2026-01-06/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/NewJersey4_analyzer_v2_top_candidates.csv` |
| Master report | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewJersey4.md` |

## 2. Truth Lens

### 2.1 Winner read

- This is one of the strongest lane-only DR truths in the current batch.
- The Evening winner `942` is barely alive as a literal exact object:
  - `exact_any=30`
  - `drop_exact_any=22`
- But the family / VTRAC world is overwhelming:
  - `items_total=252`
  - `vtrac_any=252`
  - `drop_vtrac_any=240`
  - `family_vtrac_any=168`
- DR still fails to elevate the winner into the top-candidate surface:
  - `winner_present=False`
- So this case is ideal for proving that DR can be extremely right on lane while being completely wrong on literal caller output.

### 2.2 Pre- vs post-reduction

- The biggest DR truth here is not literal pre-reduction exactness.
- It is the persistence of the winner lane through:
  - pre-reduction family presence,
  - reduction-backed VTRAC survival,
  - and family-VTRAC carry.
- This is the kind of case where DR should feed the arena as a lane/gateway tool first.

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | `Evening current-band boxes where 992 dominates` | The caller is attracted to `992`, which becomes the main competing literal corridor. |
| Key box 2 | `Evening repeated reduction-support rows` | These preserve the winner VTRAC lane almost completely (`drop_vtrac_any=240`). |
| Key row 1 | earliest exact/vtrac = `0` / `0` in stamp | Winner lane is present immediately. |
| Key row 2 | family-VTRAC-heavy rows | These are the main signal the caller currently flattens. |

## 3. Grouped Box Read

### Group 1 - Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | `992` is the main literal attractor. |
| Strongest post-reduction cluster(s) | Winner lane remains very strong via `drop_vtrac` and `family_vtrac`, even though exact literal support stays secondary. |
| Repeats across boxes | Yes. |
| Repeats across sets | Yes. |
| Repeats across variants | Evening is the main truth surface; Combined / Midday support the broader environment. |
| VTRAC convergence | Maximal in practice: `252/252`. |
| Currentness / progression quality | Very high. This is a current, alive lane case. |

### Group 2 - Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | Supportive but still absorbed into the wrong literal family. |
| Strongest post-reduction cluster(s) | Helpful for lane persistence. |
| Repeats across boxes | Present. |
| Repeats across sets | Present. |
| Repeats across variants | Supportive. |
| VTRAC convergence | Strong. |
| Current-endpoint importance | Secondary to the main lane-only point. |

### Current endpoint emphasis

- The key lesson is not “find the literal winner in the endpoint.”
- It is “recognize when DR is screaming a family lane even though it never cleanly collapses to the right literal.”

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| `992` corridor | `299` | competing | repeated Evening current-band boxes | Evening | compact repeated motif | dominates caller output, not the winner lane | `3` |
| `599` corridor | `599` | competing/supportive | repeated Evening rows | Evening | compact motif | secondary competing literal pressure | `2` |
| winner lane around `249/942` | buried family object | winner lane | broad trace surface | Evening strongest | lane-first, not literal-first | main truth object | `3` |

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| winner lane survival | mixed | own + combined | early-mid | broad family presence | still broad after reduction | medium-high | no | `3` |
| `992` competing motif | mixed | own | early | compact motif | remains strong | medium | no | `2` |

## 6. Row-Downward Repeat Ledger

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| winner lane | many | mixed | yes | very strong | `drop_vtrac_any=240` makes this one of the clearest lane-survival cases. |
| `992` motif | repeated | mixed | no | competing | The main literal distractor. |

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| winner lane `249 / 942` | yes | yes | yes | extremely strong | high | This is the point of the case. |
| `992` literal attractor | yes | yes | mostly local | weak to winner | high | Strong competing literal pressure. |

## 8. Fourth-Variable Candidate Panel

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| winner lane `249/942` | lane-only core | winner lane | not isolated | not isolated | broad | low | not ready | n/a | low |

### Fourth-variable notes

- This is not a primary fourth-variable case.
- It is more important as a lane-only truth case and a `competing literal pressure` case.

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | Present in `992` / `599`. |
| Mirror-double relation | Secondary. |
| Duplicate depth | Moderate in the competing family. |
| Same-family double pressure | Not the winner’s main story. |
| Conversion implication | Useful because it shows repeated-value motifs can steal the caller surface from a stronger winner lane. |

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| mixed recent-draw elimination | clutter around the live lane | stronger VTRAC/family lane survival | yes | Good evidence for scoring lane persistence separately from literal exactness. |

## 11. Aux / Control Center Corroboration

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| Winners lens | live evening winner environment | direct | high |
| Stable / Hot Zones | use as corroboration only | partial | medium |
| Aux / CC | not primary in this DR read | supportive only | low-medium |

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | The winner lane with extreme VTRAC/family persistence. |
| What did V2 capture but compress too early? | The difference between winner-lane truth and `992` literal pressure. |
| What did V2 score weakly but meaningfully? | Exact support for the winner literal itself. |
| What did V2 miss entirely? | A usable lane-only confidence object. |
| Is the issue extraction, scoring, compression, or consumption? | Compression/consumption first, with some scoring implications. |
| What should be salvaged into the arena directly? | `dr_lane_only_confidence`, `dr_trace_strength`, and `dr_competing_literal_pressure`. |

## 13. Box Validity Ledger

| Box location | Status | Evidence | Recommended action |
|---|---|---|---|
| Evening current-band `992` boxes | `core` | repeated top pressure | keep |
| Evening reduction-backed lane boxes | `core` | massive `drop_vtrac` support | keep |

## 14. Decay / Short-Window Register

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| lane-only winner truth | yes | n/a | n/a | weak | weak | strong | no | Very strong same-draw lane case. |

## 15. Scoring Factors Summary

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | `3` | Strong lane truth and strong competing motif. |
| Reduction reveal strength | `3` | Winner lane survives reduction extremely well. |
| Row 1 influence | `3` | Immediate. |
| Row 2 influence | `3` | Strong carry. |
| Residual purity | `1` | Not a literal-pure case. |
| Across-box repetition | `3` | Strong. |
| Across-set repetition | `3` | Strong. |
| Across-variant convergence | `2` | Good support. |
| VTRAC convergence | `3` | Maximal. |
| Duplicate depth | `2` | Competing motifs have repeated-value pressure. |
| Double / mirror-double pressure | `1` | Secondary. |
| Fourth-variable confidence | `0` | Not the main lesson here. |
| Frontier / currentness | `3` | High. |

## 16. Integration Decisions

- `Keep`: DR as a lane-first evidence tool.
- `Add tracker`: lane-only cases where exact support is secondary but family-VTRAC survival is overwhelming.
- `Add arena field`: `dr_lane_only_confidence`.
- `Add arena field`: `dr_competing_literal_pressure`.
- `Policy note`: do not downgrade a case just because exact literal support is light when the lane object is overwhelming.
- `Case verdict`: one of the best positive cases for why DR should feed an arena object richer than `best_pattern`.
