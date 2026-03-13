# DR Super Harness Case - 2026-01-09 - NewJersey4 - Evening - 028

## 1. Case Header

| Field | Value |
|---|---|
| Date | `2026-01-09` |
| State | `NewJersey4` |
| Draw | `Evening` |
| Winner literal | `028` |
| Winner canonical | `028` |
| Winner VTRAC family/index | winners lens `vtrac11`; DR local index `13` |
| Seed case label | `SEED-A` |
| Reviewer | `Codex` |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | `sharepacks/2026-01-09/NewJersey4/winners/NewJersey4/NewJersey4_vtrac11_winner_028_20260110_035047.html` |
| Winners JSON | `sharepacks/2026-01-09/NewJersey4/winners/NewJersey4/NewJersey4_vtrac11_winner_028_20260110_035047.json` |
| Winners overlay | `sharepacks/2026-01-09/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/winners/20260110_Evening_winner_overlay.html` |
| Winner stamp | `sharepacks/2026-01-09/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/winners/20260110_Evening_winner_stamp.json` |
| Winner flags | `sharepacks/2026-01-09/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/winners/20260110_Evening_winner_flags.csv` |
| Winner hits | `sharepacks/2026-01-09/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/winners/20260110_Evening_winner_hits.csv` |
| DR per_item | `sharepacks/2026-01-09/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/NewJersey4_analyzer_v2_per_item.csv` |
| DR top_candidates | `sharepacks/2026-01-09/NewJersey4/digit_reduction/NewJersey4/analyzer_v2/NewJersey4_analyzer_v2_top_candidates.csv` |
| Master report | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__NewJersey4.md` |

## 2. Truth Lens

### 2.1 Winner read

- This is a strong buried-but-present DR case.
- DR stamp says the Evening winner `028` is heavily present in the trace:
  - `items_total=162`
  - `exact_any=133`
  - `vtrac_any=159`
  - `drop_exact_any=50`
  - `drop_vtrac_any=65`
- But DR does not isolate the exact winner as a usable caller output:
  - `exact_final=0`
  - `vtrac_final=0`
  - `winner_present=True` in top-candidates only at a very weak rank surface from the old audit posture
- This makes the case ideal for checking whether the harness properly separates:
  - strong trace presence
  - from weak final-caller promotion

### 2.2 Pre- vs post-reduction

- Winner family is visible both pre-reduction and through reduction.
- The stronger evidence class is still pre-/in-trace presence rather than clean final collapse.
- Reduction helps, but it does not narrow to the literal winner by the end of the current pipeline.

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | `LS1 / Evening / Set3 / Draw1 / Col5` | Earliest stamped exact+VTRAC hit surface for the winner family. |
| Key box 2 | `LS1 / Evening / Set2 / Draw1 / Col5` | Repeats the same family corridor one set later, which is exactly the kind of persistence DR should preserve. |
| Key row 1 | earliest step `0` for exact and VTRAC in the stamp | Tells us the winner family is present immediately rather than being manufactured late. |
| Key row 2 | drop-VTRAC supportive rows (`drop_vtrac_any=65`) | Important because reduction still reveals and supports the family even when the final caller misses. |

## 3. Grouped Box Read

### Group 1 - Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | `992`, `922` dominate the local DR surface while still matching the winner's exact/VTRAC family flags. |
| Strongest post-reduction cluster(s) | `922` gets stronger as a reduction-support object via `drop_vtrac`. |
| Repeats across boxes | Same `992/922` family cluster repeats across `Set3 -> Set2`. |
| Repeats across sets | Yes; strongest evidence is not isolated to one box. |
| Repeats across variants | Primary read is still Evening-local, but Combined also carries heavy winner-family presence. |
| VTRAC convergence | Very strong; `vtrac_any=159/162`. |
| Currentness / progression quality | Good. The family is already alive at step 0 and persists into more current rows. |

### Group 2 - Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | Weaker than Group 1 in this first read. |
| Strongest post-reduction cluster(s) | Supportive, but not the dominant story. |
| Repeats across boxes | Present, but secondary to the Group 1 corridor. |
| Repeats across sets | Some carry, but not the strongest evidence in this case. |
| Repeats across variants | Mainly supportive through Combined. |
| VTRAC convergence | Present, but not where the case earns its strongest identity. |
| Current-endpoint importance | Useful later, but the main buried-family story is already established above. |

### Current endpoint emphasis

- This case is less about a single clean endpoint and more about repeated family presence that never gets promoted correctly.
- That makes it a very good seed case for `trace vs caller` rather than `frontier-only` interpretation.

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| `992` | `299` | winner-family related in trace | `LS1 Set3 Draw1 Col5`, `LS1 Set3 Draw1 Col6` | Evening | compact cluster | immediate exact/VTRAC presence | `3` |
| `922` | `229` | winner-family related in trace | `LS1 Set3 Draw1 Col4`, `LS1 Set2 Draw1 Col5` | Evening | compact cluster | repeated across sets and supports drop-VTRAC | `3` |
| broader family lane | winner family `028` / `023` / `078` / `528` etc. | very strong | widespread | Evening + Combined | family-presence, not literal | heavy stamp counts prove it is alive | `3` |

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| winner-family support | mixed | own + combined | early | broad family presence | still family-supportive after reduction | medium | no | `2` |
| `922` family support | A/C/T | own | early-mid | broad cluster | clearer VTRAC support | medium | near-pure in repeated rows | `2` |

## 6. Row-Downward Repeat Ledger

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| `922` / `992` corridor | repeated across early rows and sets | `A`, `C`, `T` | yes | strong | This is the main evidence class the old caller surface flattened. |
| winner-family VTRAC lane | many rows | mixed | yes | very strong | The family is broadly alive even when literal exact collapse fails. |

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| winner family around `028` | yes | yes | yes (Evening strongest, Combined supportive) | very strong | high | This is the main reason the case was chosen. |
| `922/992` proxy corridor | yes | yes | limited | strong | medium-high | Valuable because it shows DR can be on the right family while ranking the wrong literal. |

## 8. Fourth-Variable Candidate Panel

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| `028` family lane | family anchor | winner VTRAC family | not yet isolated | not yet isolated | broad | low | not promoted yet | n/a | low |

### Fourth-variable notes

- This is not the best first example for proving a fourth-variable pattern.
- It is better as a trace-vs-caller compression case.

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | Present in competing proxy clusters like `992/922`, but not the main reason this winner matters. |
| Mirror-double relation | Secondary. |
| Duplicate depth | Moderate in the proxy clusters. |
| Same-family double pressure | Not the primary signal. |
| Conversion implication | Useful later, but not the main lesson from this case. |

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| recent-draw elimination in mixed methods | some clutter around the winner-family lane | stronger family persistence, especially in drop-VTRAC support | yes | Worth tracking, but not yet clean enough to call "only remaining in box". |

## 11. Aux / Control Center Corroboration

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| Stable | Evening `028` exact boxed + exact straight | direct | high |
| VTRAC enhanced | winner family still a real lane | family corroboration | high |
| Aux / CC | not primary for this DR case | supportive only | low-medium |

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | Very strong winner-family presence across exact/VTRAC trace counts. |
| What did V2 capture but compress too early? | The repeated `992/922` family corridor and the broader `028` family lane. |
| What did V2 score weakly but meaningfully? | Family-level persistence that never made it into a strong caller output. |
| What did V2 miss entirely? | A usable evidence object separating family-presence from literal top-candidate ranking. |
| Is the issue extraction, scoring, compression, or consumption? | Mainly compression/consumption. |
| What should be salvaged into the arena directly? | Pre-reduction cluster ledgers, repeated proxy corridors, and the family-presence vs caller-miss split. |

## 13. Box Validity Ledger

| Box location | Status | Evidence | Recommended action |
|---|---|---|---|
| `LS1 / Evening / Set3 / Draw1 / Col5` | `core` | earliest exact/VTRAC presence | keep |
| `LS1 / Evening / Set3 / Draw1 / Col4` | `core` | repeated `922` support with drop-VTRAC | keep |
| `LS1 / Evening / Set2 / Draw1 / Col5` | `core` | repeated winner-family support one set later | keep |

## 14. Decay / Short-Window Register

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| buried family lane | yes | n/a | n/a | yes in truth layer | yes in truth layer | yes | no | Strong same-draw case. |

## 15. Scoring Factors Summary

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | `3` | Very strong trace presence. |
| Reduction reveal strength | `2` | Helpful, but not enough to isolate final exact. |
| Row 1 influence | `3` | Earliest presence is immediate. |
| Row 2 influence | `2` | Still supportive. |
| Residual purity | `1` | Not a final-pure case. |
| Across-box repetition | `3` | Very strong. |
| Across-set repetition | `3` | Very strong. |
| Across-variant convergence | `2` | Evening strongest, Combined supportive. |
| VTRAC convergence | `3` | `159/162` is the main clue. |
| Duplicate depth | `1` | Secondary. |
| Double / mirror-double pressure | `1` | Secondary. |
| Fourth-variable confidence | `0` | Not the right case for it. |
| Frontier / currentness | `2` | Present, but not a pure frontier-only case. |

## 16. Integration Decisions

- `Keep`: DR as a strong family/trace evidence tool.
- `Add tracker`: explicit "trace strong, caller weak" classification.
- `Add arena field`: family-proxy corridor object so clusters like `992/922` can support `028` instead of competing blindly against it.
- `Policy note`: do not judge this case through top-candidate rank alone.
- `Case verdict`: this is a first-class buried-but-present rescue case and should remain one of the anchor examples for DR Arena v1.
