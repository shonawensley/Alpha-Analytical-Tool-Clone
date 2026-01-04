# Pattern Progression Primer (R2/R4/R6/R8 + columns 7→1 + VTRAC lanes)

Purpose: preserve the “deep” pattern‑recognition training (so it survives context resets) in a short, SSOT‑friendly form that is compatible with the Master Validation workflow and sharepacks.

Scope:
- Conceptual/interpretation guide (how to read the pattern environment).
- Not a wagering engine and not a “tune weights” doc.
- Use this alongside the sharepack evidence + run reports.

Related SSOT:
- Review order (prevents rabbit holes): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
- Contracts/semantics: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`

---

## 1) The mental model: a 4×N pattern progression grid per variant

You have three string tables per state/day:
- **Midday**
- **Evening**
- **Combined** (a lens / environment view; not a third outcome stream)

Each table is a progression of **columns** (most commonly **7→1**, where 7 is older and 1 is the most recent prior draw):

- Each **column** represents one draw step in the lookback window.
- As you move **left → right**, strings are progressively reduced by digits from prior outcomes.

Within each column you have **four rows** (the vertical stack):
- **R2**, **R4**, **R6**, **R8**

Key rule from the training guides:
- **R2/R4/R6/R8 are not “progressive reductions.”** They are different pool/arrangement variations of the same underlying digit universe. The analysis comes from:
  - **Vertical structure** (within the column: R2↔R4↔R6↔R8 agreement),
  - **Horizontal structure** (across columns: how patterns persist/develop toward the right).

---

## 2) Two core concepts: persistence + convergence

### A) Persistence (structure that “survives”)

Persistence is when a substring/pattern:
- stays visible as you move toward the rightmost columns (closer to Column 1), and/or
- stays visible across multiple R‑rows within a column.

In practice, persistence looks like:
- 3–4 digit clusters that remain present across multiple columns,
- repeated “tail” fragments that keep showing up as strings shrink,
- stable ordered patterns that don’t disappear when you apply the next reduction step.

### B) Convergence (independent lenses point to the same thing)

Convergence is when **multiple independent views** reinforce the same candidate space:
- within the same variant (Midday only) across R2/R4/R6/R8,
- across variants (Midday ↔ Evening ↔ Combined),
- across tool lenses (Stable / VTRAC / Hot Zones / Digit Reduction / Aux) agreeing on the same lane/cluster.

This is the highest‑value “signal class” for Master Validation: it’s not one tool “calling a number,” it’s the environment collapsing toward a shared candidate lane.

---

## 3) “Golden” 3‑value / 3‑digit clusters

The training guides emphasize a practical visual milestone:
- when strings reduce down to **3–4 digits**, and
- a **3‑digit repeat** emerges (especially near the rightmost columns),
that is a strong candidate formation event.

How to interpret safely in Master Validation:
- Treat this as an **environment cue** (“the space collapsed”) not as a guarantee.
- Look for **cross‑confirmation** (another R‑row, another column, another variant, or another tool) before promoting it to a pack decision.

---

## 4) Consensus (explicit definition used in training)

Consensus is a specific convergence pattern near the end of the table:

- Check **Column 1 or Column 2** (rightmost).
- If **all four rows** (R2, R4, R6, R8) share the **same 1–2 digit substring** in that column, that is “consensus”.

Examples:
- `7 / 7 / 7 / 7`
- `44 / 44 / 44 / 44`

Why it matters:
- It implies the structure has converged on a finishing digit (or pair) and you should treat any stable/persistent clusters in that environment as “high attention.”

Special note:
- Consensus can be a **doubles trigger** (e.g., repeated `7` suggests “7‑something” pressure, especially when other digits are also stable).

---

## 5) VTRAC lanes: treat “8 straights” as a set (not a single number)

The training docs lean heavily on the idea that:
- mirror transformations are structural, and
- VTRAC turns a number into a family (“lane”) of related outcomes.

Operationally in this codebase:
- A **VTRAC index corresponds to 8 straight combinations** (a lane).
- Therefore, any analysis that points at a VTRAC lane should be graded as **set membership**:
  - winner ∈ {8 straights of the lane}
  - not “one canonical equals the winner”

This is now reflected in how Profit Alerts and Control Center evaluations are structured (set‑based evaluation).

Reference:
- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`

---

## 6) Permutations, canonical vs literal, and why “strings lead”

Practical discipline rules (important for correctness):

- **Literal** is the exact draw text (e.g., `033`).
- **Canonical** is the sorted digits (e.g., `033` canonical = `033`, `517` canonical = `157`).
- For boxed evaluations, canonical equality is the simplest invariant.

Permutation counts (useful intuition):
- Singles have up to 6 permutations (box set size up to 6).
- Doubles have 3 permutations (e.g., `244 / 424 / 442`).

Method hierarchy (mirrors the workflow):
- **Strings lead**: the string tables define the base environment.
- **Aux compounds**: adds pressure/structure information (repeat watch, doubles pressure, BA indicators, etc.).
- Tools are used to extract/present evidence from those same underlying structures.

---

## 7) Profit framing (keep it measurable, not magical)

The most useful “profitability” primitive during Master Validation is not “will it hit next draw?” but:

- treat a signal as an **episode** with a window (DecayDraws, plus diagnostics like <=7 and <=14 draw‑steps),
- treat actionable outputs as **sets** (BOX set, VTRAC 8‑lane, clamped subsets),
- log:
  - set_size,
  - window_steps,
  - hit_within_window,
  - time_to_hit_steps (if any),
  - and a unitless cost proxy (set_size × window_steps).

This avoids overfitting and preserves your “hit‑rates within a timeframe” framing.

---

## 8) How to use this primer while filling templates

Recommended usage:

1) Start with the winners lens (Part A): what did the environment look like?
2) Use Part 2 (tools) to document: which lenses converged, which didn’t, and at what strength.
3) Use Part 3 (Aux) to capture compounding signals that reinforce or contradict the base.
4) Synthesize into a pack decision (Part 4) only after documenting convergence/persistence.
5) Log “fix later” vs “tool outcome” explicitly so you don’t spiral.

If you feel lost while reviewing a day:
- use the deterministic order in `AAT9_Master_Validation_Analysis_Navigator.md`.

---

## 9) Common pitfalls (the ones that create false panic)

- **Column indexing confusion:** the training guides discuss 9 draws in places; the modern workflow is centered on **7→1**.
- **Combined confusion:** Combined is not a third outcome stream; it’s an environment lens.
- **Leading zeros:** always treat Pick‑3 literals/canonicals as 3‑digit strings (`033` must not become `33`).
- **Pipeline vs tool outcome:** “miss” does not mean “broken.” If artifacts exist and alignment passes, a miss is a measurement.

