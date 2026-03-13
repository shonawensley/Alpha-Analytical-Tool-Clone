# DR Super Harness Case - 2026-01-09 - OntarioCanada4 - Evening - 104

## 1. Case Header

| Field | Value |
|---|---|
| Date | `2026-01-09` |
| State | `OntarioCanada4` |
| Draw | `Evening` |
| Winner literal | `104` |
| Winner canonical | `014` |
| Winner VTRAC family/index | winners lens `vtrac9`; DR local index `9` |
| Batch label | `B2-C` |
| Reviewer | `Codex` |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac9_winner_104_20260110_035057.html` |
| Winners JSON | `sharepacks/2026-01-09/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac9_winner_104_20260110_035057.json` |
| Winners overlay | `sharepacks/2026-01-09/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/winners/20260110_Evening_winner_overlay.html` |
| Winner stamp | `sharepacks/2026-01-09/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/winners/20260110_Evening_winner_stamp.json` |
| Winner flags | `sharepacks/2026-01-09/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/winners/20260110_Evening_winner_flags.csv` |
| Winner hits | `sharepacks/2026-01-09/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/winners/20260110_Evening_winner_hits.csv` |
| DR per_item | `sharepacks/2026-01-09/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/OntarioCanada4_analyzer_v2_per_item.csv` |
| DR top_candidates | `sharepacks/2026-01-09/OntarioCanada4/digit_reduction/OntarioCanada4/analyzer_v2/OntarioCanada4_analyzer_v2_top_candidates.csv` |
| Master report | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-09__OntarioCanada4.md` |

## 2. Truth Lens

### 2.1 Winner read

- This is one of the strongest buried-but-present positive cases in the queue.
- The Evening winner `104` has:
  - `items_total=240`
  - `exact_any=204`
  - `vtrac_any=240`
  - `drop_exact_any=24`
  - `drop_vtrac_any=66`
- Yet DR still does not surface the winner as a top candidate:
  - `winner_present=False`
- This case is extremely valuable because the same state also gave us the negative control `ON 498`.
- So Ontario now proves that DR can be:
  - totally empty on one case,
  - and extremely alive-but-compressed on another.

### 2.2 Pre- vs post-reduction

- The winner is already strong before reduction.
- Reduction helps, but the main truth here is not “revealed from nothing.”
- It is “present in trace and still not promoted.”

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | `Evening Set1 current-band boxes scoring as 552/501/559` | Shows where the caller gets pulled away from the winner even though the winner is in trace. |
| Key box 2 | broad Evening trace rows | The winner has very high exact and VTRAC presence. |
| Key row 1 | earliest exact/vtrac = `0/0` | Immediate winner presence. |
| Key row 2 | reduction-backed rows | Useful, but secondary to the pre-reduction presence. |

## 3. Grouped Box Read

### Group 1 - Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | The winner is strongly alive in trace, but the caller prefers `552`, `501`, `559`. |
| Strongest post-reduction cluster(s) | Winner support remains visible but not dominant enough to escape compression. |
| Repeats across boxes | Yes. |
| Repeats across sets | Yes. |
| Repeats across variants | Evening is the positive truth surface; Midday/Combined are empty-lens for the other winner. |
| VTRAC convergence | Very strong for the Evening winner. |
| Currentness / progression quality | High. |

### Group 2 - Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | Supportive but still routed into competing motifs. |
| Strongest post-reduction cluster(s) | Supportive. |
| Repeats across boxes | Present. |
| Repeats across sets | Present. |
| Repeats across variants | Mainly Evening-local for this winner. |
| VTRAC convergence | Strong. |
| Current-endpoint importance | Secondary to the broader trace-vs-caller split. |

### Current endpoint emphasis

- This is another “trace strong / caller weak” case, but with much stronger exact presence than `NJ 942`.
- That makes it a crucial contrast:
  - `NJ 942` = lane-only truth
  - `ON 104` = literal-and-lane truth still not promoted

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| `552` corridor | `255` | competing | repeated current-band boxes | Evening | compact repeated motif | top caller family | `3` |
| `501` corridor | `015` | partially adjacent | repeated current-band boxes | Evening + Combined | compact motif | closer to the winner than `552`, but still not the winner | `2` |
| `559` corridor | `559` | competing | repeated boxes | Evening | compact motif | another competing motif family | `2` |
| winner lane `104/014` | direct winner family | winner | broad trace surface | Evening | literal and lane both alive | still compressed away | `3` |

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| winner exact+lane support | mixed | own + combined | early-mid | already strong | still supportive after reduction | medium | no | `2` |
| `552/501/559` competitor family | mixed | own | early | strong | stays strong | medium | no | `2` |

## 6. Row-Downward Repeat Ledger

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| winner lane `014/104` | repeated broadly | mixed | yes | strong | true buried-positive trace case. |
| `552` corridor | repeated | mixed | no | competing | strongest literal distractor. |

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| winner lane `014` | yes | yes | Evening-focused | very strong | high | strong positive Ontario case |
| `552/501/559` competitor set | yes | yes | some Combined echo | mixed | high | caller pressure family |

## 8. Fourth-Variable Candidate Panel

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| `014` lane | buried exact core | winner lane | not isolated | not isolated | broad | low | not ready | n/a | low |

### Fourth-variable notes

- This is more useful as a buried exact core case than as a fourth-variable case.

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | Strong in the competing `552` family. |
| Mirror-double relation | Secondary. |
| Duplicate depth | Moderate in the distractor family. |
| Same-family double pressure | Not the winner’s main story. |
| Conversion implication | Shows how repeated-value motifs can out-rank a true buried winner family. |

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| mixed reduction paths | some clutter | still-visible winner lane | yes | Helpful but not the main reason the winner is known. |

## 11. Aux / Control Center Corroboration

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| winners / run report | strong Evening truth; Midday/Combined empty-lens for other winner | direct | high |
| Stable / VTRAC / Hot Zones | corroboration only | supportive | medium |
| Aux / CC | not the main driver for this DR read | supportive only | low-medium |

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | Strong exact and VTRAC winner presence in trace. |
| What did V2 capture but compress too early? | The winner lane relative to the competing `552/501/559` family cluster. |
| What did V2 score weakly but meaningfully? | The actual winner literal despite `exact_any=204`. |
| What did V2 miss entirely? | A clear distinction between “winner buried strongly” and “competing literal family dominates caller.” |
| Is the issue extraction, scoring, compression, or consumption? | Compression/consumption, with likely scoring implications. |
| What should be salvaged into the arena directly? | `dr_trace_strength` plus `dr_competing_literal_pressure`. |

## 13. Box Validity Ledger

| Box location | Status | Evidence | Recommended action |
|---|---|---|---|
| Evening current-band `552/501/559` boxes | `core` | major caller pressure region | keep |
| Evening broad trace rows | `core` | strong winner presence | keep |

## 14. Decay / Short-Window Register

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| buried exact+lane truth | yes | n/a | n/a | yes in trace | no | yes | no | Strong same-draw buried-positive case. |

## 15. Scoring Factors Summary

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | `3` | Winner and distractors both strong. |
| Reduction reveal strength | `2` | Supportive, not decisive. |
| Row 1 influence | `3` | Immediate. |
| Row 2 influence | `2` | Supportive. |
| Residual purity | `1` | No final collapse. |
| Across-box repetition | `3` | Strong. |
| Across-set repetition | `3` | Strong. |
| Across-variant convergence | `1` | More local than some other cases. |
| VTRAC convergence | `3` | Strong. |
| Duplicate depth | `2` | Distractor family benefits from repeats. |
| Double / mirror-double pressure | `1` | Secondary. |
| Fourth-variable confidence | `0` | Not the main lesson. |
| Frontier / currentness | `3` | High. |

## 16. Integration Decisions

- `Keep`: DR as a buried-trace evidence tool.
- `Add tracker`: cases where exact buried truth exists but caller still routes to another motif family.
- `Add arena field`: `dr_competing_literal_pressure`.
- `Policy note`: strong buried-exact cases should not be judged only by top-candidate absence.
- `Case verdict`: extremely important positive Ontario case because it pairs directly with `ON 498` and proves DR can be both empty-lens and highly informative depending on the environment.
