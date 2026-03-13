# DR Super Harness Case - 2026-01-07 - Michigan4 - Evening - 616

## 1. Case Header

| Field | Value |
|---|---|
| Date | `2026-01-07` |
| State | `Michigan4` |
| Draw | `Evening` |
| Winner literal | `616` |
| Winner canonical | `166` |
| Winner VTRAC family/index | winners lens `vtrac16`; DR local index `31` |
| Batch label | `B2-D` |
| Reviewer | `Codex` |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | `sharepacks/2026-01-07/Michigan4/winners/Michigan4/Michigan4_vtrac16_winner_616_20260110_033422.html` |
| Winners JSON | `sharepacks/2026-01-07/Michigan4/winners/Michigan4/Michigan4_vtrac16_winner_616_20260110_033422.json` |
| Winners overlay | `sharepacks/2026-01-07/Michigan4/digit_reduction/Michigan4/analyzer_v2/winners/20260110_Evening_winner_overlay.html` |
| Winner stamp | `sharepacks/2026-01-07/Michigan4/digit_reduction/Michigan4/analyzer_v2/winners/20260110_Evening_winner_stamp.json` |
| Winner flags | `sharepacks/2026-01-07/Michigan4/digit_reduction/Michigan4/analyzer_v2/winners/20260110_Evening_winner_flags.csv` |
| Winner hits | `sharepacks/2026-01-07/Michigan4/digit_reduction/Michigan4/analyzer_v2/winners/20260110_Evening_winner_hits.csv` |
| DR per_item | `sharepacks/2026-01-07/Michigan4/digit_reduction/Michigan4/analyzer_v2/Michigan4_analyzer_v2_per_item.csv` |
| DR top_candidates | `sharepacks/2026-01-07/Michigan4/digit_reduction/Michigan4/analyzer_v2/Michigan4_analyzer_v2_top_candidates.csv` |
| Master report | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Michigan4.md` |

## 2. Truth Lens

### 2.1 Winner read

- This is one of the strongest doubles / mirror-double DR cases in the whole reviewed set.
- The Evening winner `616` has:
  - `items_total=167`
  - `exact_any=158`
  - `exact_final=96`
  - `vtrac_any=167`
  - `vtrac_final=102`
  - `drop_exact_final=78`
  - `drop_vtrac_final=78`
  - `family_vtrac_final=102`
- This is critical:
  - DR is not only seeing the lane,
  - it is seeing a great deal of final-survival truth,
  - and it still does not promote the winner into top candidates.
- So this is beyond “trace strong / caller weak.”
- It is closer to:
  - `final-survival strong / caller still blind`.

### 2.2 Pre- vs post-reduction

- Both are strong.
- Pre-reduction exact and VTRAC presence are already high.
- Post-reduction and final-survival counts are also high.
- That makes this one of the best current proofs that the caller surface is too narrow, even when DR has already effectively trapped the winner environment.

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | Evening winner rows across the overlay | huge exact/VTRAC/final support |
| Key box 2 | repeated reduction-final rows | show that the winner survives all the way down |
| Key row 1 | earliest exact/vtrac = `0/0` | immediate |
| Key row 2 | final rows with exact/VTRAC retention | strongest proof of final-survival truth |

## 3. Grouped Box Read

### Group 1 - Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | winner double family `166/616/661` is very strong in truth, but the caller prefers `590`, `900`, `559`. |
| Strongest post-reduction cluster(s) | winner family remains strong all the way into final rows. |
| Repeats across boxes | Yes. |
| Repeats across sets | Yes. |
| Repeats across variants | Evening is the main truth surface. |
| VTRAC convergence | Maximal in this case. |
| Currentness / progression quality | Strong. |

### Group 2 - Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | Supportive. |
| Strongest post-reduction cluster(s) | Very strong because the winner survives late. |
| Repeats across boxes | Present. |
| Repeats across sets | Present. |
| Repeats across variants | Some support, but Evening dominates. |
| VTRAC convergence | Strong. |
| Current-endpoint importance | Higher than many other cases because final-survival is part of the story. |

### Current endpoint emphasis

- This is one of the strongest DR examples for:
  - row-downward repetition,
  - final-survival truth,
  - and double/mirror-double pressure.

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| winner double family `166/616/661` | direct winner family | winner lane | broad Evening trace surface | Evening | strong repeated-value anchor | major truth object | `3` |
| `590/900/559` corridor | competing | competing | top caller output | Evening | compact competing motifs | shows caller distortion | `2` |

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| winner exact/VTRAC survival | mixed | own + combined | early-late | already strong | remains strong through final rows | high | near-pure at many rows | `3` |
| competing caller motifs | mixed | own | early | present | remain present | medium | no | `2` |

## 6. Row-Downward Repeat Ledger

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| winner family `166/616/661` | many | mixed | yes | extremely strong | This is the strongest row-repeat/final-survival case in the reviewed batch so far. |
| competing `590/900/559` motifs | repeated | mixed | no | competing | Still attractive to caller despite weaker truth value. |

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| winner family `166` | yes | yes | mainly Evening | extremely strong | high | strong same-draw truth |
| competing motif family | yes | some | local | weak | medium | not the actual winner family |

## 8. Fourth-Variable Candidate Panel

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| `166/616` core | double anchor | winner lane | maybe `9/0/5` in competitors | not promoted | broad | high | not yet formalized | low | medium |

### Fourth-variable notes

- This is not the cleanest “add one extra digit” case yet.
- But it is a powerful demonstration that:
  - repeated-value winner cores can survive to final rows,
  - while unrelated repeated-value motifs still capture the caller surface.

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | Central to the case. |
| Mirror-double relation | Strongly relevant. |
| Duplicate depth | High. |
| Same-family double pressure | Extremely strong. |
| Conversion implication | This is the clearest current case for a dedicated `dr_double_pressure` surface. |

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| mixed recent-draw elimination | clutter around the winner double family | a winner family that survives all the way to final rows | yes | Very strong. |

## 11. Aux / Control Center Corroboration

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| winners lens | direct `616` truth | direct | high |
| Stable / VTRAC | likely strong support for the same family | supportive | medium-high |
| Aux / CC | use as corroboration later | supportive | medium |

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | Almost everything except caller promotion: exact, VTRAC, final-survival, and family-VTRAC truth. |
| What did V2 capture but compress too early? | The winner double core relative to the wrong caller motifs. |
| What did V2 score weakly but meaningfully? | The actual caller object should have been much stronger given the final-survival counts. |
| What did V2 miss entirely? | A direct final-survival evidence surface that can override wrong motif attraction. |
| Is the issue extraction, scoring, compression, or consumption? | Scoring/compression/consumption, not extraction. |
| What should be salvaged into the arena directly? | `dr_double_pressure` and `dr_row_repeat_and_final_survival`. |

## 13. Box Validity Ledger

| Box location | Status | Evidence | Recommended action |
|---|---|---|---|
| Evening winner-support rows | `core` | strongest final-survival truth | keep |
| competing caller motif boxes | `supportive` | useful for rival-pressure reading | keep |

## 14. Decay / Short-Window Register

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| double-core final survival | yes | n/a | n/a | yes | yes | yes | yes | strongest same-draw DR truth in the batch so far |

## 15. Scoring Factors Summary

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | `3` | Extremely strong. |
| Reduction reveal strength | `3` | Extremely strong. |
| Row 1 influence | `3` | Immediate. |
| Row 2 influence | `3` | Strong. |
| Residual purity | `3` | Strong final-survival evidence. |
| Across-box repetition | `3` | Strong. |
| Across-set repetition | `3` | Strong. |
| Across-variant convergence | `1` | More local. |
| VTRAC convergence | `3` | Extremely strong. |
| Duplicate depth | `3` | Central. |
| Double / mirror-double pressure | `3` | Central. |
| Fourth-variable confidence | `1` | Maybe later, but not the main lesson. |
| Frontier / currentness | `3` | Strong. |

## 16. Integration Decisions

- `Keep`: DR as a double-pressure / final-survival evidence tool.
- `Add tracker`: strong final-survival cases where winner survives but caller still misses.
- `Add arena field`: `dr_row_repeat_and_final_survival`.
- `Add arena field`: `dr_double_pressure`.
- `Policy note`: if DR final-survival is this strong, later consumption should not treat the case like a weak DR day.
- `Case verdict`: one of the most important anchor cases in the entire DR harness so far.
