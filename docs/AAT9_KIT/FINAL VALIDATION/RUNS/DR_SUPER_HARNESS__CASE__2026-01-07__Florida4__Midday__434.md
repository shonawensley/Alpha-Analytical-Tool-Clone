# DR Super Harness Case - 2026-01-07 - Florida4 - Midday - 434

## 1. Case Header

| Field | Value |
|---|---|
| Date | `2026-01-07` |
| State | `Florida4` |
| Draw | `Midday` |
| Winner literal | `434` |
| Winner canonical | `344` |
| Winner VTRAC family/index | winners lens `vtrac34` |
| Seed case label | `SEED-B` |
| Reviewer | `Codex` |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | `sharepacks/2026-01-07/Florida4/winners/Florida4/Florida4_vtrac34_winner_434_20260110_033415.html` |
| Winners JSON | `sharepacks/2026-01-07/Florida4/winners/Florida4/Florida4_vtrac34_winner_434_20260110_033415.json` |
| Winners overlay | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/winners/20260110_Midday_winner_overlay.html` |
| Winner stamp | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/winners/20260110_Midday_winner_stamp.json` |
| Winner flags | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/winners/20260110_Midday_winner_flags.csv` |
| Winner hits | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/winners/20260110_Midday_winner_hits.csv` |
| DR per_item | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/Florida4_analyzer_v2_per_item.csv` |
| DR top_candidates | `sharepacks/2026-01-07/Florida4/digit_reduction/Florida4/analyzer_v2/Florida4_analyzer_v2_top_candidates.csv` |
| Master report | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-07__Florida4.md` |

## 2. Truth Lens

### 2.1 Winner read

- This is the strongest early doubles / repeated-value pressure case in the seed set.
- DR stamp for Midday winner `434` says:
  - `items_total=117`
  - `exact_any=91`
  - `vtrac_any=104`
  - `drop_exact_any=47`
  - `drop_vtrac_any=73`
  - `family_vtrac_any=50`
  - `vt_boxed=51`
- So the DR world clearly contains the winner, but the caller surface still does not promote it.
- The important twist is that the local high-score objects are not the literal winner:
  - top per-item surfaces are dominated by `544` and `559`
  - both sit in winner-related rows and carry repeated-value pressure

### 2.2 Pre- vs post-reduction

- Winner evidence is strong both before and after reduction.
- This is one of the first seed cases where reduction is genuinely helping:
  - `drop_exact_any=47`
  - `drop_vtrac_any=73`
- So unlike the pure VTRAC-lane case, this one gives a real reveal story too.

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | `LS1 / Midday / Set2 / Draw1 / Col7` | Strongest early winner-related box with direct exact/VTRAC/drop/family support. |
| Key box 2 | `LS1 / Midday / Set1 / Draw5 / Col2` | Strong repeated-value box carrying `559` with large cluster echo count. |
| Key row 1 | earliest exact step `0`, earliest VTRAC step `0` | Winner family is already alive before strong reduction kicks in. |
| Key row 2 | early drop-exact step `1` | Reduction begins enhancing the environment quickly instead of only late. |

## 3. Grouped Box Read

### Group 1 - Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | `544` at `Set2 / Draw1 / Col7`, then `559` cluster at `Set1 / Draw5 / Col2-3`. |
| Strongest post-reduction cluster(s) | Same regions become more supportive through `drop_exact` and `drop_vtrac`. |
| Repeats across boxes | Yes, especially around the `559` corridor. |
| Repeats across sets | Yes; the case spans `Set2 -> Set1`. |
| Repeats across variants | Supportive, but Midday is the true center. |
| VTRAC convergence | Strong. |
| Currentness / progression quality | Good; the case progresses into more current boxes while keeping duplicate pressure. |

### Group 2 - Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | Supportive, not primary. |
| Strongest post-reduction cluster(s) | Some relevance through reveal enhancement. |
| Repeats across boxes | Moderate. |
| Repeats across sets | Moderate. |
| Repeats across variants | Secondary. |
| VTRAC convergence | Present as support. |
| Current-endpoint importance | Useful, but the richer story still begins in Group 1. |

### Current endpoint emphasis

- This case suggests DR should not treat repeated-value pressure as mere clutter.
- The environment looks like:
  - true winner family alive
  - plus strong repeated-value / mirror-like neighbor structures
  - plus meaningful reduction enhancement

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| `544` | `445` | winner-related in trace | `LS1 Set2 Draw1 Col7` | Midday | repeated-value anchor | strongest early exact/VTRAC/drop/family support | `3` |
| `559` | `559` | winner-related in trace | `LS1 Set1 Draw5 Col1-3` | Midday | repeated-value anchor, high echo count | strongest cluster-repeat object | `3` |
| winner family `344` | direct winner canon | direct | widespread in trace | Midday + Combined support | exact family truth | clearly present, weakly caller-promoted | `3` |

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| winner family support | mixed | own + combined | early | family already active | gets cleaner via early drop-exact and drop-VTRAC | medium-high | near-pure in some box paths | `3` |
| `559` repeated-value corridor | A/E/B | own + combined | early-mid | broad repeated-value cluster | reduction keeps it alive instead of killing it | medium | no | `2` |

## 6. Row-Downward Repeat Ledger

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| `559` corridor | many | mixed | not literal winner, but related in winner-support rows | strong | Best doubles/repeated-value object in the seed set so far. |
| winner family `344` support | many | mixed | yes | very strong | This is the core truth that the caller surface under-promotes. |

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| winner family `344` | yes | yes | some | strong | high | The exact truth layer is real. |
| `544/559` repeated-value corridor | yes | yes | limited | supportive | high | Very important for doubles / mirror-double interpretation. |

## 8. Fourth-Variable Candidate Panel

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| winner family `344` | family / repeated-value core | direct | likely `5` | possible family-neighbor carry | moderate | high | `344/544/559` style neighborhood | low | medium |

### Fourth-variable notes

- This is not yet a clean proof case for fourth-variable expansion.
- It does strongly suggest that:
  - repeated-value pressure can sit around the winning core
  - and may deserve its own bounded closure treatment later

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | Strong through `544` and especially `559`. |
| Mirror-double relation | Strong enough to treat as a real regime clue. |
| Duplicate depth | High; repeated-value structures are central to the case. |
| Same-family double pressure | Present as support around the winning core. |
| Conversion implication | This is the first seed case strongly arguing for a dedicated doubles / mirror-double DR scoring channel. |

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| recent-draw reduction mix | clutter around the winner-support boxes | cleaner winner-family and repeated-value support | yes | Good real example of reduction enhancing visibility rather than merely filtering. |

## 11. Aux / Control Center Corroboration

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| Stable | Exact-boxed and exact-straight support on `434/344` | direct | high |
| VTRAC enhanced | winner index ranks near the top | direct | high |
| Aux / CC | useful later for closure policy, but not needed for the core DR lesson | supportive only | low-medium |

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | Winner-family truth, repeated-value pressure, and reveal enhancement. |
| What did V2 capture but compress too early? | The relationship between winner family `344` and the repeated-value neighbor corridor `544/559`. |
| What did V2 score weakly but meaningfully? | Family-level support that sits under strong duplicate pressure. |
| What did V2 miss entirely? | A clean arena object for doubles/mirror-double pressure that supports, rather than competes with, the winning core. |
| Is the issue extraction, scoring, compression, or consumption? | Mostly compression/consumption. |
| What should be salvaged into the arena directly? | Repeated-value anchors, duplicate depth, reveal-enhanced support, and bounded fourth-variable candidates. |

## 13. Box Validity Ledger

| Box location | Status | Evidence | Recommended action |
|---|---|---|---|
| `LS1 / Midday / Set2 / Draw1 / Col7` | `core` | strongest early winner-support box | keep |
| `LS1 / Midday / Set1 / Draw5 / Col2` | `core` | highest-value repeated-value corridor | keep |
| `LS1 / Midday / Set1 / Draw5 / Col3` | `core` | echo of the same repeated-value corridor | keep |

## 14. Decay / Short-Window Register

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| repeated-value + winner-core pressure | yes | n/a | n/a | yes | yes | yes | no | Good same-draw doubles-regime example. |

## 15. Scoring Factors Summary

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | `3` | Strong. |
| Reduction reveal strength | `3` | Strongest reveal case in the seed set so far. |
| Row 1 influence | `3` | Winner truth starts early. |
| Row 2 influence | `2` | Good support. |
| Residual purity | `2` | Better than the first cases, though still not final-pure. |
| Across-box repetition | `3` | Strong. |
| Across-set repetition | `3` | Strong. |
| Across-variant convergence | `1` | Secondary. |
| VTRAC convergence | `3` | Strong. |
| Duplicate depth | `3` | Main feature of the case. |
| Double / mirror-double pressure | `3` | Main feature of the case. |
| Fourth-variable confidence | `2` | Suggestive, but not yet decisive. |
| Frontier / currentness | `2` | Good. |

## 16. Integration Decisions

- `Keep`: repeated-value / mirror-double pressure as a first-class DR evidence type.
- `Add tracker`: distinguish supportive repeated-value pressure from competing wrong-literal pressure.
- `Add arena field`: duplicate-depth / double-pressure ledger.
- `Policy note`: strong repeated-value corridors should not be discarded as clutter; they often explain why DR is close even when the exact caller fails.
- `Case verdict`: this is the anchor doubles / mirror-double seed case for DR Arena v1.
