# DR Super Harness Case - 2026-01-08 - OntarioCanada4 - Evening - 498

## 1. Case Header

| Field | Value |
|---|---|
| Date | `2026-01-08` |
| State | `OntarioCanada4` |
| Draw | `Evening` |
| Winner literal | `498` |
| Winner canonical | `489` |
| Winner VTRAC family/index | winners lens `vtrac34` |
| Seed case label | `SEED-E` |
| Reviewer | `Codex` |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac34_winner_498_20260110_034440.html` |
| Winners JSON | `sharepacks/2026-01-08/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac34_winner_498_20260110_034440.json` |
| Winners overlay | `sharepacks/2026-01-08/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/winners/20260110_Evening_winner_overlay.html` |
| Winner stamp | `sharepacks/2026-01-08/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/winners/20260110_Evening_winner_stamp.json` |
| Winner flags | `sharepacks/2026-01-08/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/winners/20260110_Evening_winner_flags.csv` |
| Winner hits | `sharepacks/2026-01-08/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/winners/20260110_Evening_winner_hits.csv` |
| DR per_item | `sharepacks/2026-01-08/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/OntarioCanada4_analyzer_v2_per_item.csv` |
| DR top_candidates | `sharepacks/2026-01-08/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/OntarioCanada4_analyzer_v2_top_candidates.csv` |
| Master report | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-08__OntarioCanada4.md` |

## 2. Truth Lens

### 2.1 Winner read

- This is the noisy / empty-lens control case.
- DR Evening stamp is completely empty:
  - `items_total=0`
  - `exact_any=0`
  - `vtrac_any=0`
  - `drop_exact_any=0`
  - `drop_vtrac_any=0`
- Stable still isolates the evening winner exactly, so this is not a truth failure.
- It is a DR-lens failure or a mapped-box coverage failure.

### 2.2 Pre- vs post-reduction

- No DR evidence exists for the evening winner in the current mapped-box lens.
- That makes this case necessary for:
  - the box-validity study
  - the "empty lens vs true noise vs missing region" discussion

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | none in Evening DR lens | The absence itself is the point. |
| Key box 2 | Combined support zones from `022` | Useful contrast: DR is active elsewhere in the day, just not where the evening winner lives. |
| Key row 1 | n/a | No evening DR rows were generated. |
| Key row 2 | n/a | No evening DR rows were generated. |

## 3. Grouped Box Read

### Group 1 - Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | none for Evening winner |
| Strongest post-reduction cluster(s) | none |
| Repeats across boxes | none |
| Repeats across sets | none |
| Repeats across variants | not for the evening winner |
| VTRAC convergence | none |
| Currentness / progression quality | none |

### Group 2 - Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | none for the evening winner |
| Strongest post-reduction cluster(s) | none |
| Repeats across boxes | none |
| Repeats across sets | none |
| Repeats across variants | none |
| VTRAC convergence | none |
| Current-endpoint importance | unresolved because the lens is empty |

### Current endpoint emphasis

- This is the exact case type that keeps us honest.
- We should not auto-assume every winner is sitting inside the current mapped DR windows in a useful way.

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| none for Evening winner | n/a | n/a | n/a | n/a | n/a | empty lens | `0` |

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| none | n/a | n/a | n/a | n/a | n/a | none | none | `0` |

## 6. Row-Downward Repeat Ledger

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| none | n/a | n/a | n/a | none | Empty-lens control. |

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| Evening winner family | none | none | none | none | none | This is the control result we need. |

## 8. Fourth-Variable Candidate Panel

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| none | n/a | n/a | n/a | n/a | 0 | 0 | n/a | n/a | `0` |

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | none for the evening winner inside DR |
| Mirror-double relation | none |
| Duplicate depth | none |
| Same-family double pressure | none |
| Conversion implication | none; this is a null DR case |

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| none | none | none | no | This is an empty-lens control, not a reveal case. |

## 11. Aux / Control Center Corroboration

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| Stable | Winner exists exactly in Stable despite DR being empty. | none | high contrast value |
| VTRAC enhanced | winner index is low-ranked | none | moderate |
| Aux / CC | may explain playability later, but not relevant to DR emptiness | none | low |

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | Nothing useful for the Evening winner. |
| What did V2 capture but compress too early? | Not the main issue here. |
| What did V2 score weakly but meaningfully? | Nothing obvious in the DR lens for this winner. |
| What did V2 miss entirely? | The entire evening winner environment. |
| Is the issue extraction, scoring, compression, or consumption? | Could be mapping/extraction or a genuinely empty DR environment; this is exactly why the case is in the seed set. |
| What should be salvaged into the arena directly? | The fact that DR is empty should itself be preserved as a meaningful negative/control signal. |

## 13. Box Validity Ledger

| Box location | Status | Evidence | Recommended action |
|---|---|---|---|
| Evening mapped DR windows as a set | `disputed` | no items for the winner at all | re-test through broader seed set before changing mappings |

## 14. Decay / Short-Window Register

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| DR lens emptiness | yes | n/a | n/a | no | no | no | no | Useful as a negative-control class. |

## 15. Scoring Factors Summary

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | `0` | Empty. |
| Reduction reveal strength | `0` | Empty. |
| Row 1 influence | `0` | Empty. |
| Row 2 influence | `0` | Empty. |
| Residual purity | `0` | Empty. |
| Across-box repetition | `0` | Empty. |
| Across-set repetition | `0` | Empty. |
| Across-variant convergence | `0` | Empty for the winner. |
| VTRAC convergence | `0` | Empty. |
| Duplicate depth | `0` | Empty. |
| Double / mirror-double pressure | `0` | Empty. |
| Fourth-variable confidence | `0` | Empty. |
| Frontier / currentness | `0` | Empty. |

## 16. Integration Decisions

- `Keep`: explicit empty-lens classification as a first-class DR result.
- `Add tracker`: empty-lens rate by box group and by variant.
- `Add arena field`: negative-control / no-signal DR state.
- `Policy note`: do not over-credit DR on days where the tool simply did not see the winner environment.
- `Case verdict`: this is the control case needed to keep the super-harness honest and to ground the mapped-box validity study.
