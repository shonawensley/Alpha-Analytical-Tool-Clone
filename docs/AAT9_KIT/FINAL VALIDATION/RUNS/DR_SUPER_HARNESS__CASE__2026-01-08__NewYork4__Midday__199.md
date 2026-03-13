# DR Super Harness Case - 2026-01-08 - NewYork4 - Midday - 199

## 1. Case Header

| Field | Value |
|---|---|
| Date | `2026-01-08` |
| State | `NewYork4` |
| Draw | `Midday` |
| Winner literal | `199` |
| Winner canonical | `199` |
| Winner VTRAC family/index | winners lens `vtrac25`; DR local index `49` |
| Batch label | `B2-F` |
| Reviewer | `Codex` |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | `sharepacks/2026-01-08/NewYork4/winners/NewYork4/NewYork4_vtrac25_winner_199_20260110_034431.html` |
| Winners JSON | `sharepacks/2026-01-08/NewYork4/winners/NewYork4/NewYork4_vtrac25_winner_199_20260110_034431.json` |
| Winners overlay | `sharepacks/2026-01-08/NewYork4/digit_reduction/NewYork4/analyzer_v2/winners/20260110_Midday_winner_overlay.html` |
| Winner stamp | `sharepacks/2026-01-08/NewYork4/digit_reduction/NewYork4/analyzer_v2/winners/20260110_Midday_winner_stamp.json` |
| Winner flags | `sharepacks/2026-01-08/NewYork4/digit_reduction/NewYork4/analyzer_v2/winners/20260110_Midday_winner_flags.csv` |
| Winner hits | `sharepacks/2026-01-08/NewYork4/digit_reduction/NewYork4/analyzer_v2/winners/20260110_Midday_winner_hits.csv` |
| DR per_item | `sharepacks/2026-01-08/NewYork4/digit_reduction/NewYork4/analyzer_v2/NewYork4_analyzer_v2_per_item.csv` |
| DR top_candidates | `sharepacks/2026-01-08/NewYork4/digit_reduction/NewYork4/analyzer_v2/NewYork4_analyzer_v2_top_candidates.csv` |
| Master report | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__NewYork4.md` |

## 2. Truth Lens

### 2.1 Winner read

- This is the second true empty-lens control after `ON 498`.
- Midday winner `199` has:
  - `items_total=0`
  - `exact_any=0`
  - `vtrac_any=0`
  - `drop_* = 0`
  - `family_* = 0`
- The caller still produces an active motif world:
  - `552`, `522`, `524`, `592`, `520`
- That is exactly why this case matters:
  - DR is not simply “silent”
  - it is actively narrating the wrong environment
  - while the true winner environment is absent

### 2.2 Pre- vs post-reduction

- There is no meaningful pre-reduction winner signal.
- There is no meaningful post-reduction winner signal.
- This is a true cold/negative DR day for the actual Midday winner.

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | Midday current-band boxes dominated by `552` | shows what DR *did* focus on instead |
| Key box 2 | none for winner | because the winner is absent from the DR lens |
| Key row 1 | n/a | no winner presence |
| Key row 2 | n/a | no winner presence |

## 3. Grouped Box Read

### Group 1 - Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | `552` dominates. |
| Strongest post-reduction cluster(s) | `552/522/524/592` remain dominant. |
| Repeats across boxes | Yes, but for the wrong family. |
| Repeats across sets | Yes. |
| Repeats across variants | Midday strongest, with some echo into Combined/Evening top candidates. |
| VTRAC convergence | For the wrong family, not for the winner. |
| Currentness / progression quality | Strong — but strongly wrong for the winner. |

### Group 2 - Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | same wrong-family motif world |
| Strongest post-reduction cluster(s) | same |
| Repeats across boxes | yes |
| Repeats across sets | yes |
| Repeats across variants | some echo |
| VTRAC convergence | not toward the winner |
| Current-endpoint importance | Important mainly as proof that current pressure can still be the wrong pressure. |

### Current endpoint emphasis

- This is the kind of case that protects us from over-crediting any DR activity.
- The correct interpretation is:
  - DR is live,
  - but DR is live on the wrong family world.

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| `552` corridor | `255` | competing | repeated Midday current-band boxes | Midday + some echoes | strong repeated-value motif | main wrong-world object | `3` |
| `522 / 524 / 592 / 520` corridor | competing | competing | repeated nearby boxes | Midday | supporting wrong-family cloud | strong but wrong | `2` |
| winner `199` | winner | winner | none | none | none | absent | `0` |

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| winner support | none | none | n/a | absent | absent | none | no | `0` |
| wrong-family `552` world | mixed | own + combined | early-late | strong | strong | medium | no | `3` |

## 6. Row-Downward Repeat Ledger

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| `552` corridor | many | mixed | no | competing | strong wrong-world repetition |
| winner `199` | none | none | n/a | absent | true empty-lens condition |

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| `552` family world | yes | yes | yes | wrong to winner | high | highly active but not useful for the actual winner |
| winner `199` | no | no | no | absent | absent | cold lens |

## 8. Fourth-Variable Candidate Panel

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| none | none | none | none | none | 0 | 0 | n/a | n/a | `0` |

### Fourth-variable notes

- This is not a fourth-variable case.
- It is important precisely because it is empty of winner evidence.

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | Strong, but all in the wrong family world. |
| Mirror-double relation | Secondary. |
| Duplicate depth | High for the wrong family. |
| Same-family double pressure | Not tied to the actual winner. |
| Conversion implication | Important warning: double pressure alone is not enough without winner-lane truth. |

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| mixed reduction paths | clutter in wrong-family world | more wrong-family motifs | yes | This is why empty-lens controls matter. |

## 11. Aux / Control Center Corroboration

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| winners lens | actual winner exists only outside DR lens | direct negative control | high |
| Stable / VTRAC / Hot Zones | compare later to see whether other tools saw the winner | corroboration | medium |
| Aux / CC | not part of DR truth layer | later corroboration | low-medium |

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | The wrong family environment. |
| What did V2 capture but compress too early? | Not the main issue here. |
| What did V2 score weakly but meaningfully? | Nothing for the actual winner. |
| What did V2 miss entirely? | The actual winner environment. |
| Is the issue extraction, scoring, compression, or consumption? | This is a true empty-lens case more than a compression case. |
| What should be salvaged into the arena directly? | `dr_empty_lens` plus the competing-family pressure context. |

## 13. Box Validity Ledger

| Box location | Status | Evidence | Recommended action |
|---|---|---|---|
| Midday `552` current-band boxes | `core` | meaningful wrong-world pressure | keep |
| winner-support boxes | `dead for this case` | none | do not over-credit DR here |

## 14. Decay / Short-Window Register

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| winner presence in DR | no | n/a | n/a | no | no | no | no | true negative control |

## 15. Scoring Factors Summary

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | `0` for winner / `3` for wrong world | important negative-control split |
| Reduction reveal strength | `0` for winner / `3` for wrong world | same |
| Row 1 influence | `0` for winner | absent |
| Row 2 influence | `0` for winner | absent |
| Residual purity | `0` for winner | absent |
| Across-box repetition | `0` for winner / `3` for wrong world | same |
| Across-set repetition | `0` for winner / `3` for wrong world | same |
| Across-variant convergence | `0` for winner / `2` for wrong world | same |
| VTRAC convergence | `0` for winner | absent |
| Duplicate depth | `0` for winner / `3` for wrong world | same |
| Double / mirror-double pressure | `0` for winner / `2` for wrong world | same |
| Fourth-variable confidence | `0` | not applicable |
| Frontier / currentness | `0` for winner / `3` for wrong world | same |

## 16. Integration Decisions

- `Keep`: a true empty-lens control category in the DR arena.
- `Add tracker`: `dr_empty_lens` should remain distinct from “weak trace” and from “caller weak.”
- `Policy note`: not every active DR environment is predictive for the actual winner.
- `Case verdict`: critical negative control; helps prevent us from designing DR Arena v1 as if every active map implies useful winner truth.
