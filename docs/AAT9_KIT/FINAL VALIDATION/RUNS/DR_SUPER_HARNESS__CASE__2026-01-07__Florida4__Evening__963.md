# DR Super Harness Case - 2026-01-07 - Florida4 - Evening - 963

## 1. Case Header

| Field | Value |
|---|---|
| Date | `2026-01-07` |
| State | `Florida4` |
| Draw | `Evening` |
| Winner literal | `963` |
| Winner canonical | `369` |
| Winner VTRAC family/index | winners lens `vtrac24`; DR local index `44` |
| Seed case label | `SEED-C` |
| Reviewer | `Codex` |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | `sharepacks/2026-01-07/Florida4/winners/Florida4/Florida4_vtrac24_winner_963_20260110_033415.html` |
| Winners JSON | `sharepacks/2026-01-07/Florida4/winners/Florida4/Florida4_vtrac24_winner_963_20260110_033415.json` |
| Winners overlay | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/winners/20260110_Evening_winner_overlay.html` |
| Winner stamp | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/winners/20260110_Evening_winner_stamp.json` |
| Winner flags | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/winners/20260110_Evening_winner_flags.csv` |
| Winner hits | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/winners/20260110_Evening_winner_hits.csv` |
| DR per_item | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/Florida4_analyzer_v2_per_item.csv` |
| DR top_candidates | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/Florida4_analyzer_v2_top_candidates.csv` |
| Master report | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Florida4.md` |

## 2. Truth Lens

### 2.1 Winner read

- This is the clearest early DR VTRAC-gateway case.
- DR stamp for Evening winner `963` says:
  - `items_total=90`
  - `exact_any=0`
  - `vtrac_any=90`
  - `drop_vtrac_any=2`
  - `vt_boxed=6`
- So DR is not seeing the literal winner as an exact cluster at all.
- It is seeing the winner purely through family/VTRAC structure.

### 2.2 Pre- vs post-reduction

- Pre-reduction VTRAC family presence is the real signal.
- Reduction contributes almost nothing literal:
  - `drop_exact_any=0`
  - `drop_vtrac_any=2`
- This is exactly the case type that proves DR should not be judged as a literal caller first.

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | `LS1 / Evening / Set3 / Draw1 / Col7` | First stamped VTRAC hit surface for the winner family. |
| Key box 2 | `LS1 / Evening / Set3 / Draw1 / Col6` | Repeats the same VTRAC lane immediately beside the first box. |
| Key row 1 | earliest VTRAC step `0` in the stamp | Shows the lane is already alive before meaningful reduction. |
| Key row 2 | drop-VTRAC row at step `2` | Useful only as a minor corroborator, not the main truth. |

## 3. Grouped Box Read

### Group 1 - Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | VTRAC-family lane is active from the start in `LS1`, especially `Set3 / Draw1 / Col7` and `Col6`. |
| Strongest post-reduction cluster(s) | Weak. Reduction is not the main source of truth here. |
| Repeats across boxes | Yes, inside the same upper-band slice. |
| Repeats across sets | Some support, but the decisive story is immediate lane presence. |
| Repeats across variants | Secondary. This case is mostly a single-variant VTRAC-lane proof case. |
| VTRAC convergence | Perfect on the stamp: `90/90`. |
| Currentness / progression quality | Good enough, but the lane evidence matters more than the exact endpoint. |

### Group 2 - Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | Not the main signal. |
| Strongest post-reduction cluster(s) | Weak. |
| Repeats across boxes | Limited. |
| Repeats across sets | Limited. |
| Repeats across variants | Limited. |
| VTRAC convergence | Present only as support. |
| Current-endpoint importance | Lower than Group 1 for this case. |

### Current endpoint emphasis

- This case should stop us from forcing all DR value into current-endpoint exactness.
- The important thing here is that DR traps the right lane, not the exact literal.

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| winner VTRAC lane | family around `963` / `913` / `468` etc. | direct winner family | `LS1 Set3 Draw1 Col7`, `Col6` | Evening | family-only | strongest evidence in the case | `3` |
| top caller proxies | `552`, `544`, `522` | not the winner lane | multiple | Evening/Combined | repeated-value heavy | good example of caller distraction | `2` |

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| winner VTRAC lane | mixed | own + combined | early | family already alive | still family alive | low | no | `1` |
| drop-VTRAC support | sparse | mixed | later | little | slight lane reinforcement | low | no | `1` |

## 6. Row-Downward Repeat Ledger

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| winner VTRAC lane | multiple | mixed | yes | direct | Strong enough to matter even without exact-literal support. |
| `552/544` caller corridor | multiple | mixed | no | distracting | Good evidence that DR can score the wrong literal while keeping the right lane alive underneath. |

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| winner VTRAC family | yes | some | limited | perfect | medium | This is the main reason the case was selected. |
| `552/544` repeated-value corridor | yes | yes | yes | weak to winner | medium-high | Important competing object; good future negative comparison for the harness. |

## 8. Fourth-Variable Candidate Panel

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| winner VTRAC lane | VTRAC-family anchor | direct | not yet isolated | not yet isolated | broad lane support | low | not the right first case | n/a | low |

### Fourth-variable notes

- Not the best case for fourth-variable learning.
- This case is more valuable as proof that VTRAC-lane truth can exist without exact-literal truth.

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | Strong, but mostly in competing patterns `552/544/522`. |
| Mirror-double relation | Present in the distracting caller corridor. |
| Duplicate depth | High in the wrong caller surface. |
| Same-family double pressure | Low for the actual winning lane. |
| Conversion implication | Important negative lesson: duplicate depth alone should not outrank pure winner-lane VTRAC truth. |

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| limited transit effect | little | slight VTRAC reinforcement only | minimally | Not a reduction-first case. |

## 11. Aux / Control Center Corroboration

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| Stable | Exact-boxed support exists even though DR exact surface is absent. | direct family corroboration | high |
| VTRAC enhanced | winner index ranks near the top | direct | high |
| Aux / CC | useful later, but not needed to prove the DR point here | supportive only | low-medium |

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | Winner-family VTRAC lane presence. |
| What did V2 capture but compress too early? | The distinction between "right VTRAC lane" and "wrong literal pattern." |
| What did V2 score weakly but meaningfully? | The lane itself, because no strong exact-literal object existed. |
| What did V2 miss entirely? | An arena-ready object for lane truth without exact truth. |
| Is the issue extraction, scoring, compression, or consumption? | Mostly compression/consumption. |
| What should be salvaged into the arena directly? | VTRAC-gateway ledgers, lane-only confidence, and competing-literal penalty context. |

## 13. Box Validity Ledger

| Box location | Status | Evidence | Recommended action |
|---|---|---|---|
| `LS1 / Evening / Set3 / Draw1 / Col7` | `core` | earliest direct VTRAC-lane receipt | keep |
| `LS1 / Evening / Set3 / Draw1 / Col6` | `core` | adjacent repeat of the same lane | keep |
| late reduction-only rows | `supportive` | minor corroboration only | keep but low-weight |

## 14. Decay / Short-Window Register

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| lane-only VTRAC truth | yes | n/a | n/a | no | no | yes | no | This is the archetypal VT-boxed DR case. |

## 15. Scoring Factors Summary

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | `2` | Family lane is strong, literal cluster is not. |
| Reduction reveal strength | `1` | Minimal. |
| Row 1 influence | `3` | Lane is present immediately. |
| Row 2 influence | `1` | Only slight corroboration. |
| Residual purity | `0` | Not a purity case. |
| Across-box repetition | `2` | Good inside Group 1. |
| Across-set repetition | `1` | Modest. |
| Across-variant convergence | `1` | Secondary. |
| VTRAC convergence | `3` | Perfect on the stamp. |
| Duplicate depth | `2` | High, but mostly in the wrong caller corridor. |
| Double / mirror-double pressure | `2` | Strong negative/competing factor. |
| Fourth-variable confidence | `0` | Not the right case for it. |
| Frontier / currentness | `2` | Present, but not the main story. |

## 16. Integration Decisions

- `Keep`: explicit VTRAC-gateway classification as a DR truth type.
- `Add tracker`: competing-literal vs winning-lane split.
- `Add arena field`: lane-only confidence when `exact_any=0` but `vtrac_any` is dominant.
- `Policy note`: repeated-value caller patterns should not automatically outrank a perfect winner-lane trace.
- `Case verdict`: this is the anchor case for proving DR should feed family/lane truth into the arena, not just literal top-candidate lists.
