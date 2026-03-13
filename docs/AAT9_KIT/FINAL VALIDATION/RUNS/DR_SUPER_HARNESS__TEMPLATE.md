# Digit Reduction Super Harness Template

Purpose: reusable template for deep DR example analysis.

Use this template with:

- winners HTML / JSON
- DR winners overlay
- DR `winner_flags.csv` / `winner_hits.csv`
- DR `steps.csv`
- Analyzer V2 `per_item` / `top_candidates`
- relevant Aux / Control Center artifacts

Keep this structured.
Do not let it become a pure narrative dump.

---

## 1. Case Header

| Field | Value |
|---|---|
| Date | |
| State | |
| Draw | |
| Winner literal | |
| Winner canonical | |
| Winner VTRAC family/index | |
| Seed case label | |
| Reviewer | |

### Source receipts

| Artifact | Path / note |
|---|---|
| Winners HTML | |
| Winners JSON | |
| Winners overlay | |
| Winner flags | |
| Winner hits | |
| DR steps CSV | |
| DR per_item | |
| DR top_candidates | |
| Aux summary | |
| Other relevant receipts | |

---

## 2. Truth Lens

### 2.1 Winner read

- What family / lane / cluster actually won?
- Was the win more exact-boxed, exact-straight, VT-boxed, or VT-straight in character?
- Which parts of the winners HTML/JSON are the strongest receipts?

### 2.2 Pre- vs post-reduction

- Was the winner family visible before reduction?
- Was it only made obvious after reduction?
- Was it strong in both?

### 2.3 Most important boxes / rows

| Type | Location | Why it matters |
|---|---|---|
| Key box 1 | |
| Key box 2 | |
| Key row 1 | |
| Key row 2 | |

---

## 3. Grouped Box Read

### Group 1 — Upper long-string band (`7/6/5` style zone)

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | |
| Strongest post-reduction cluster(s) | |
| Repeats across boxes | |
| Repeats across sets | |
| Repeats across variants | |
| VTRAC convergence | |
| Currentness / progression quality | |

### Group 2 — Staircase / current-day ladder

| Signal | Notes |
|---|---|
| Strongest pre-reduction cluster(s) | |
| Strongest post-reduction cluster(s) | |
| Repeats across boxes | |
| Repeats across sets | |
| Repeats across variants | |
| VTRAC convergence | |
| Current-endpoint importance | |

### Current endpoint emphasis

- What is happening in the most current long-string endpoint?
- Which patterns are progressing into it?
- Does it act as a true frontier / arrival box in this case?

---

## 4. Pre-Reduction Cluster Ledger

| Cluster | Canon / family | VTRAC | Boxes | Variants | Depth / extra digits | Stability notes | Score / rating |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

---

## 5. Reduction Reveal Ledger

| Reveal object | Method | Own / combined / transit | Row | Before | After | Purity gain | Only-remaining / near-pure | Score / rating |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

---

## 6. Row-Downward Repeat Ledger

Treat row-downward repeats as a DR-native repeat class.

| Pattern | Rows repeated | Method(s) | Same family? | Winner relation | Strength / notes |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

---

## 7. Cross-Box / Cross-Variant Convergence Ledger

| Pattern / family | Across boxes | Across sets | Across variants | VTRAC relation | Currentness | Strength / notes |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

---

## 8. Fourth-Variable Candidate Panel

Only include bounded, evidence-backed candidates.

| Core anchor | Anchor type | Core VTRAC | Lingering extra digit | Lingering extra VTRAC digit | Support count | Duplicate depth | Closure neighborhood | Added cost | Confidence |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

### Fourth-variable notes

- Why is this extra variable real rather than random clutter?
- Is it recurring across methods / rows / boxes / variants?
- Is it current enough to matter?

---

## 9. Doubles / Mirror-Double Pressure

| Signal | Evidence |
|---|---|
| Repeated-value anchors | |
| Mirror-double relation | |
| Duplicate depth | |
| Same-family double pressure | |
| Conversion implication | |

---

## 10. Transit-Digit Reveal Read

| Transit digit / value | What it removed | What it revealed | Was the revealed pattern repeated elsewhere? | Strength / notes |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

---

## 11. Aux / Control Center Corroboration

Keep this as corroboration, not truth.

| Source | Relevant finding | Match to DR cluster/family | Importance |
|---|---|---|---|
| Aux positional shortlist | | | |
| Aux VTRAC overlay | | | |
| Due doubles | | | |
| Badge pressure | | | |
| Blackapple | | | |
| Other | | | |

---

## 12. Analyzer V2 Salvage Audit

| Question | Answer |
|---|---|
| What did V2 already capture well? | |
| What did V2 capture but compress too early? | |
| What did V2 score weakly but meaningfully? | |
| What did V2 miss entirely? | |
| Is the issue extraction, scoring, compression, or consumption? | |
| What should be salvaged into the arena directly? | |

---

## 13. Box Validity Ledger

Use this to stop ad hoc mapping drift.

| Box location | Status (`core` / `supportive` / `experimental` / `disputed` / `dead_or_na`) | Evidence | Recommended action |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

---

## 14. Decay / Short-Window Register

Track whether the notable DR indicators resolve within a short draw window.

| Indicator | Same draw | Next 2 draws | Next 3 days | Exact boxed | Exact straight | VT boxed | VT straight | Notes |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

---

## 15. Scoring Factors Summary

Rate the case-level quality of the main DR evidence classes.

| Factor | Rating (`0-3`) | Notes |
|---|---|---|
| Pre-reduction cluster strength | | |
| Reduction reveal strength | | |
| Row 1 influence | | |
| Row 2 influence | | |
| Residual purity | | |
| Across-box repetition | | |
| Across-set repetition | | |
| Across-variant convergence | | |
| VTRAC convergence | | |
| Duplicate depth | | |
| Double / mirror-double pressure | | |
| Fourth-variable confidence | | |
| Frontier / currentness | | |
| Permutation clue strength | | |
| Aux / CC corroboration | | |

---

## 16. Integration Decisions

| Type | Item | Decision | Why |
|---|---|---|---|
| Rule | | | |
| Tracker | | | |
| Tool change | | | |
| Arena field | | | |
| Policy / test | | | |

### Immediate takeaways

- What is the most important thing this case teaches?
- What should be implemented next because of it?
- What should be observed across more cases before editing?

---

## 17. Final Case Verdict

### DR role in this case

- Was DR mainly:
  - pre-cluster evidence,
  - reveal evidence,
  - lane/gateway evidence,
  - fourth-variable evidence,
  - double-pressure evidence,
  - or some combination?

### Best concise summary

- One short paragraph on what this case proves about Digit Reduction.
