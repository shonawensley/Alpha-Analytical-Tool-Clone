# DR Super Harness Case - 2025-06-23 - NewYork4 - Midday - 638

## 1. Case Header

| Field | Value |
|---|---|
| Date | `2025-06-23` |
| State | `NewYork4` |
| Draw | `Midday` |
| Winner literal | `638` |
| Winner canonical | `368` |
| Winner VTRAC family/index | winners lens `vtrac23`; DR local index `43` |
| Batch label | `B2-A` |
| Reviewer | `Codex` |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | `sharepacks/2025-06-23/NewYork4/winners/NewYork4/NewYork4_vtrac23_winner_638_20251223_052055.html` |
| Winners JSON | `sharepacks/2025-06-23/NewYork4/winners/NewYork4/NewYork4_vtrac23_winner_638_20251223_052055.json` |
| Winners overlay | `sharepacks/2025-06-23/NewYork4/digit_reduction/NewYork4/analyzer_v2/winners/20251223_Midday_winner_overlay.html` |
| Winner stamp | `sharepacks/2025-06-23/NewYork4/digit_reduction/NewYork4/analyzer_v2/winners/20251223_Midday_winner_stamp.json` |
| Winner flags | `sharepacks/2025-06-23/NewYork4/digit_reduction/NewYork4/analyzer_v2/winners/20251223_Midday_winner_flags.csv` |
| Winner hits | `sharepacks/2025-06-23/NewYork4/digit_reduction/NewYork4/analyzer_v2/winners/20251223_Midday_winner_hits.csv` |
| DR per_item | `sharepacks/2025-06-23/NewYork4/digit_reduction/NewYork4/analyzer_v2/NewYork4_analyzer_v2_per_item.csv` |
| DR top_candidates | `sharepacks/2025-06-23/NewYork4/digit_reduction/NewYork4/analyzer_v2/NewYork4_analyzer_v2_top_candidates.csv` |
| Master report | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__NewYork4.md` |

## 2. Truth Lens

### 2.1 Winner read

- This is a strong buried-but-present DR case from the June window.
- The winner `638` is heavily present in DR trace space:
  - `items_total=252`
  - `exact_any=60`
  - `vtrac_any=252`
  - `drop_vtrac_any=107`
  - `family_vtrac_any=5`
- But DR does not promote the winner canonical into top-candidate output:
  - `winner_triads_as_candidates=False`
  - `winner_best_rank=None`
- This makes the case a good counterpart to `NJ 028`:
  - here the exact object is genuinely alive,
  - but the caller still routes attention into a different literal cluster family (`994`, `559`, `554`, `543`).

### 2.2 Pre- vs post-reduction

- The strongest DR truth here is still pre-/in-trace presence rather than final-collapse purity.
- Reduction does add meaningful support:
  - `drop_vtrac_any=107`
- But the final rows do not collapse to the literal winner.

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | `Midday / Set1 / Draw5 / Col2` | Area-rank 1 box with strongest recurring top motif family. Useful because the tool prefers `994` there instead of the winner. |
| Key box 2 | `Midday / Set1 / Draw6 / Col1-2` | Same high-pressure zone where the caller keeps preferring non-winner motifs over the actual buried winner. |
| Key row 1 | earliest exact/vtrac = `0` | Winner family is present immediately, not manufactured late. |
| Key row 2 | `drop_vtrac` supportive rows | Important because the reduction layer keeps supporting the winner VTRAC family even while the caller misses it. |

## 3. Grouped Box Read

### Group 1 - Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | The environment is dense and high-pressure, but the caller over-focuses on `994` / `559` / `554` style motifs instead of the winner canonical `368`. |
| Strongest post-reduction cluster(s) | Reduction preserves strong winner-family VTRAC support even when it does not surface `368` directly. |
| Repeats across boxes | Yes; the competing motif family repeats across multiple high-rank boxes. |
| Repeats across sets | Yes, especially in the Set1 current band. |
| Repeats across variants | Midday is the main DR truth surface; Combined is also highly supportive in the report summary. |
| VTRAC convergence | Extremely strong. `vtrac_any=252/252`. |
| Currentness / progression quality | Strong current-band pressure, but the current band is narrating the wrong literal family in the caller output. |

### Group 2 - Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | Supportive, but not the main reason the case matters. |
| Strongest post-reduction cluster(s) | Useful mainly through VTRAC support, not literal collapse. |
| Repeats across boxes | Present, but secondary to the Group 1 story. |
| Repeats across sets | Some carry. |
| Repeats across variants | Midday strongest, Combined supportive. |
| VTRAC convergence | Strong, but expressed mostly as family presence rather than exact object clarity. |
| Current-endpoint importance | Important as a control against over-crediting any current ladder motif that happens to repeat. |

### Current endpoint emphasis

- This case is primarily about:
  - strong trace support for the true winner family,
  - competing literal pressure from the wrong motif family,
  - and a caller surface that cannot separate those two conditions.

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| `994` corridor | `499` | competing | repeated Set1 high-rank boxes | Midday + Combined | compact repeated motif | dominates caller output but is not the winner family | `3` |
| `559 / 554 / 543` corridor | `559 / 455 / 345` | competing/supportive noise | mixed high-rank boxes | Combined + Evening | compact motifs | strong competing literal pressure | `2` |
| winner family `368` lane | `368` / VTRAC lane `23` | winner | broad trace surface | Midday + Combined | less visibly isolated as a literal cluster | present in trace but compressed away by the caller | `3` |

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| winner VTRAC lane | mixed | own + combined | early-mid | broad trace support | still broad after reduction | medium | no | `2` |
| competing `994` motif | mixed | own + combined | early | strong motif pressure | remains very strong | high | no | `3` |

## 6. Row-Downward Repeat Ledger

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| `994` corridor | repeated heavily in top per-item rows | mixed | no | competing | Shows the exact shape of the compression problem. |
| winner VTRAC lane `23` | repeated across trace rows | mixed | yes | strong | Present across many rows but not elevated as a caller object. |

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| winner family `368` / idx23 | yes | yes | yes (Midday strongest, Combined supportive) | very strong | high | The true buried winner world. |
| `994` competing motif | yes | yes | yes | weak to winner | high | The false literal attractor that current V2 favors. |

## 8. Fourth-Variable Candidate Panel

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| `368` lane | buried core | winner lane | not isolated yet | not isolated yet | broad | low | not ready | n/a | low |

### Fourth-variable notes

- This is not the strongest fourth-variable case.
- It is more important as a “competing literal pressure” case:
  - the winner family is real,
  - but one rival motif family steals the caller surface.

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | Present in competing motifs (`994`, `559`, `554`). |
| Mirror-double relation | Secondary. |
| Duplicate depth | Moderate in the competing family. |
| Same-family double pressure | Not the main winner story. |
| Conversion implication | Important because it shows DR may overweight compact repeated motifs against the true winner lane. |

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| mixed recent-draw elimination | some clutter | stronger VTRAC-family support | yes | Helpful, but still not enough to rescue the winner into top candidates. |

## 11. Aux / Control Center Corroboration

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| Winners lens | strong tag-based support for `638` even without substring support | direct | high |
| Stable | exact boxed/straight present but deep | direct | medium |
| VTRAC enhanced | Midday winner idx23 is only modestly supported | partial | medium |
| Aux / CC | not primary for this DR read | supportive only | low-medium |

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | The winner lane is strongly present in exact/VTRAC trace counts and appears immediately. |
| What did V2 capture but compress too early? | The difference between buried winner-lane truth and the competing `994` motif that dominates the caller surface. |
| What did V2 score weakly but meaningfully? | Winner-family trace support and reduction-backed VTRAC persistence. |
| What did V2 miss entirely? | An evidence object representing “strong lane truth but competing literal attractor.” |
| Is the issue extraction, scoring, compression, or consumption? | Mainly scoring/compression/consumption. |
| What should be salvaged into the arena directly? | `dr_competing_literal_pressure` beside `dr_trace_strength` and `dr_lane_only_confidence`. |

## 13. Box Validity Ledger

| Box location | Status | Evidence | Recommended action |
|---|---|---|---|
| `Midday / Set1 / Draw5 / Col2` | `core` | repeated top-rank motif pressure | keep |
| `Midday / Set1 / Draw6 / Col1` | `core` | repeated competing motif in the current band | keep |
| `Midday / Set1 / Draw6 / Col2` | `core` | same current-band pressure pattern | keep |

## 14. Decay / Short-Window Register

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| buried winner-lane truth | yes | n/a | n/a | yes in truth layer | no | yes | no | Strong same-draw buried-family case. |

## 15. Scoring Factors Summary

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | `3` | Winner lane and competing motif both strong. |
| Reduction reveal strength | `2` | Reduction helps family visibility but does not isolate final literal. |
| Row 1 influence | `3` | Earliest presence is immediate. |
| Row 2 influence | `2` | Supportive. |
| Residual purity | `1` | Not a final-pure case. |
| Across-box repetition | `3` | Strong. |
| Across-set repetition | `2` | Present. |
| Across-variant convergence | `2` | Midday strongest, Combined supportive. |
| VTRAC convergence | `3` | Full-trace VTRAC contact. |
| Duplicate depth | `2` | Competing motif family benefits from repeated-value pressure. |
| Double / mirror-double pressure | `1` | Secondary. |
| Fourth-variable confidence | `0` | Not the main lesson here. |
| Frontier / currentness | `3` | Current Set1 band is very active, but can still point at the wrong literal family. |

## 16. Integration Decisions

- `Keep`: DR as a trace/lane evidence tool.
- `Add tracker`: explicit `dr_competing_literal_pressure` to separate winner-lane truth from the wrong high-pressure motif family.
- `Add arena field`: current-band motif rivalry object so the arena can say “winner lane is alive, but `994` is stealing the literal caller surface.”
- `Policy note`: do not interpret current-band repetition as automatically predictive of the correct literal when the winner lane is only visible at the VTRAC/family level.
- `Case verdict`: strong buried-but-present case from an older window; valuable because it proves the seed-round pattern is not January-only and sharpens the need for a competing-literal DR arena field.
