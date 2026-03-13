# DR Super Harness Case - 2026-01-02 - NorthCarolina4 - Midday - 033

## 1. Case Header

| Field | Value |
|---|---|
| Date | `2026-01-02` |
| State | `NorthCarolina4` |
| Draw | `Midday` |
| Winner literal | `033` |
| Winner canonical | `033` |
| Winner VTRAC family/index | winners lens `vtrac13` |
| Seed case label | `SEED-D` |
| Reviewer | `Codex` |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac13_winner_033_20260105_070916.html` |
| Winners JSON | `sharepacks/2026-01-02/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac13_winner_033_20260105_070916.json` |
| Winners overlay | `sharepacks/2026-01-02/NorthCarolina4/digit_reduction/NorthCarolina4/analyzer_v2/winners/20260102_Midday_winner_overlay.html` |
| Winner stamp | `sharepacks/2026-01-02/NorthCarolina4/digit_reduction/NorthCarolina4/analyzer_v2/winners/20260102_Midday_winner_stamp.json` |
| Winner flags | `sharepacks/2026-01-02/NorthCarolina4/digit_reduction/NorthCarolina4/analyzer_v2/winners/20260102_Midday_winner_flags.csv` |
| Winner hits | `sharepacks/2026-01-02/NorthCarolina4/digit_reduction/NorthCarolina4/analyzer_v2/winners/20260102_Midday_winner_hits.csv` |
| DR per_item | `sharepacks/2026-01-02/NorthCarolina4/digit_reduction/NorthCarolina4/analyzer_v2/NorthCarolina4_analyzer_v2_per_item.csv` |
| DR top_candidates | `sharepacks/2026-01-02/NorthCarolina4/digit_reduction/NorthCarolina4/analyzer_v2/NorthCarolina4_analyzer_v2_top_candidates.csv` |
| Master report | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__NorthCarolina4.md` |

## 2. Truth Lens

### 2.1 Winner read

- This is the strongest early row-repeat / final-survival case in the seed set.
- DR stamp for Midday winner `033` says:
  - `items_total=264`
  - `exact_any=156`
  - `exact_final=13`
  - `vtrac_any=264`
  - `vtrac_final=13`
  - `vt_boxed=170`
- So unlike the earlier cases, DR actually reaches final exact winner states in a meaningful number of rows.
- But the top-candidate surface still fails to present the winner directly.

### 2.2 Pre- vs post-reduction

- This case has strong evidence in both channels.
- Earliest signal:
  - `earliest exact = 1`
  - `earliest vtrac = 0`
- Later support:
  - `exact_final=13`
  - `vtrac_final=13`
- So this is one of the clearest seed cases showing:
  - pre-reduction family truth
  - plus true reduction-driven survival into final winner states

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | `LS1 / Midday / Set1 / Draw3 / Col4` | Highest-scoring winner-related row, part of the strongest repeated corridor. |
| Key box 2 | `LS1 / Midday / Set1 / Draw3 / Col2` | Same corridor repeated within the same draw cluster. |
| Key row 1 | earliest VTRAC step `0` | Winner family is alive immediately. |
| Key row 2 | exact/final survival rows | This is one of the few seed cases where DR reaches real `exact_final` hits. |

## 3. Grouped Box Read

### Group 1 - Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | `922` corridor dominates early winner-related rows. |
| Strongest post-reduction cluster(s) | Same corridor continues to support final survival. |
| Repeats across boxes | Very strong. |
| Repeats across sets | Strong enough to matter. |
| Repeats across variants | Supportive, but Midday is still the main truth. |
| VTRAC convergence | Perfectly strong. |
| Currentness / progression quality | Strong; this case is very current and row-progressive. |

### Group 2 - Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | Supportive. |
| Strongest post-reduction cluster(s) | Helpful, especially around final survival. |
| Repeats across boxes | Moderate. |
| Repeats across sets | Moderate. |
| Repeats across variants | Secondary. |
| VTRAC convergence | Strong but not unique to this group. |
| Current-endpoint importance | More meaningful here than in the first cases because exact final states actually exist. |

### Current endpoint emphasis

- This is the first seed case strongly arguing that row-downward and near-endpoint survival deserve their own DR ledger.
- The winner is not just "in the trace"; it survives to final states.

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| `922` corridor | `229` | winner-related in trace | `Set1 Draw3 Col2-5`, nearby rows | Midday + Combined support | compact repeated corridor | strongest repeat object in the case | `3` |
| `992` corridor | `299` | winner-related in trace | `Set1 Draw5` and nearby | Midday | compact repeated corridor | strong secondary repeat object | `2` |
| winner family `033` | direct winner canon | direct | widely present | Midday + Combined | exact family truth | survives into final rows | `3` |

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| winner family survival | mixed | own + combined | mid-late | broad winner-family truth | `exact_final=13` | high | yes, in a real subset of rows | `3` |
| `922` corridor | A-dominant | own + combined | early-mid | broad corridor | remains strongest structural guide | medium | no | `2` |

## 6. Row-Downward Repeat Ledger

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| `922` corridor | many | mixed | yes | strong | Best row-repeat case in the seed set. |
| final winner `033` survival | multiple final rows | mixed | yes | direct | Very important because it proves DR can really end at the winner state. |

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| winner family `033` | yes | yes | yes, with Combined support | direct | high | Strong winner-family truth. |
| `922/992` corridor | yes | yes | some | supportive | high | Important because it seems to act like a structural guide rather than the literal answer. |

## 8. Fourth-Variable Candidate Panel

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| winner family `033` | exact/family core | direct | possible `2` / `9` family-neighbor corridor | possible related VTRAC neighbor | moderate | medium | `033` alongside `922/992` support family | low-medium | medium |

### Fourth-variable notes

- This is not yet a fully solved fourth-variable case.
- But it is the first seed case where the concept looks materially relevant:
  - a true winner core survives to final rows
  - while a strong adjacent structural corridor (`922/992`) keeps repeating around it
- That is exactly the kind of relation the later bounded closure logic may need to describe.

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | Present through `922/992`. |
| Mirror-double relation | Supportive. |
| Duplicate depth | Moderate. |
| Same-family double pressure | Supportive, not dominant. |
| Conversion implication | Less of a doubles-only case than Florida 434, but still useful for closure-neighborhood thinking. |

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| mixed recent-draw reduction | clutter around winner-family rows | repeated winner-family survival into final states | yes | Stronger than in earlier cases because the reveal reaches real final hits. |

## 11. Aux / Control Center Corroboration

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| Stable | Exact-boxed and exact-straight winner support | direct | high |
| VTRAC enhanced | winner index still viable | direct | medium-high |
| Aux / CC | useful later, but not required to prove the DR row-repeat lesson | supportive only | low-medium |

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | Winner-family truth, strong repeated corridor support, and real final survival. |
| What did V2 capture but compress too early? | The relationship between the repeating `922/992` structural corridor and the actual final winner `033`. |
| What did V2 score weakly but meaningfully? | The distinction between guide-corridor patterns and true final-survival patterns. |
| What did V2 miss entirely? | A clean arena object for row-downward survival and likely fourth-variable / adjacent-corridor support. |
| Is the issue extraction, scoring, compression, or consumption? | Mostly compression/consumption. |
| What should be salvaged into the arena directly? | Final-survival counts, row-repeat strength, guide-corridor objects, and fourth-variable candidate support. |

## 13. Box Validity Ledger

| Box location | Status | Evidence | Recommended action |
|---|---|---|---|
| `LS1 / Midday / Set1 / Draw3 / Col4` | `core` | strongest winner-related row | keep |
| `LS1 / Midday / Set1 / Draw3 / Col2` | `core` | same corridor repeated in nearby box | keep |
| `LS1 / Midday / Set1 / Draw5 / Col2` | `supportive` | secondary `992` corridor | keep |

## 14. Decay / Short-Window Register

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| row-repeat plus final survival | yes | n/a | n/a | yes | not needed for the DR lesson | yes | no | Strong same-draw DR success archetype. |

## 15. Scoring Factors Summary

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | `3` | Strong. |
| Reduction reveal strength | `3` | Strong because it reaches final winner states. |
| Row 1 influence | `2` | Strong early lane truth. |
| Row 2 influence | `3` | Important because later rows actually survive to final hits. |
| Residual purity | `3` | Strongest purity/final-survival case in the seed set so far. |
| Across-box repetition | `3` | Strong. |
| Across-set repetition | `2` | Strong enough. |
| Across-variant convergence | `2` | Helpful through Combined. |
| VTRAC convergence | `3` | Strong. |
| Duplicate depth | `2` | Moderate. |
| Double / mirror-double pressure | `2` | Supportive. |
| Fourth-variable confidence | `2` | First case where it looks meaningfully plausible. |
| Frontier / currentness | `3` | Very strong. |

## 16. Integration Decisions

- `Keep`: row-downward repetition and final-survival as first-class DR evidence classes.
- `Add tracker`: guide-corridor vs final-winner survival distinction.
- `Add arena field`: final-survival ledger and row-repeat strength.
- `Policy note`: this kind of case argues for DR as a bounded closure helper, not just an environment lens.
- `Case verdict`: this is the anchor seed case for row-repeat, final-survival, and early fourth-variable design discussion.
