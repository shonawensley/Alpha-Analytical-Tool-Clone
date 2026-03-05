# AAT9 DEEP EXAMPLE REVIEW ANALYSIS

Purpose: a single, human-friendly place to log what we learn from **casepack** deep dives (what the system *knew* pre-draw, what happened post-draw, and what we should change next).

This is not meant to replace the casepacks. Casepacks stay the “1‑click receipts.” This file is the **running analysis notebook**.

Related:
- Resume bookmark: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__BOOKMARK__CASEPACK_EXAMPLE_REVIEW.md`
- Casepacks index: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/README.md`

---

## Mission (macro)

This deep-dive phase is about turning “we have lots of tools + artifacts” into a **disciplined Superbrain**:

- Use real examples to learn what the system *already* sees (Candidate Universe + Winners evidence), and where it loses conversion (Play Cards / budgeting).
- Keep what’s structurally good (tool modules, artifacts, receipts) and re-steer what’s weak (selection policy, extraction emphasis, scoring logic).
- Capture **universal pattern-recognition rules** (not tied to one state/day) so Superbrain can apply them everywhere.

---

## Universal Analytical Power Notes (running list)

These are “rules of the game” we want Superbrain to respect. Add to this list as we learn.

### 1) 3‑value patterns are not “3 digits”

From `tasks/TRAINING_Q.txt`:

- A “3 value pattern” can be:
  - 3 unique digits (example: `361`)
  - doubles/triples (example: `266`, `74444`)
  - extended clusters that still reduce to 3 unique digits (example: `336611`)
  - **3 VTRAC groups** (mirror-pairs) even if the raw cluster shows more than 3 unique digits
    - Example idea: `9224466` still reduces to 3 VTRAC groups because `9↔4`.
- Heuristic: “more digits inside the same 3‑value pattern” often means the pattern is stronger (more structure is holding together).

### 2) Stability has two meanings (both matter)

Also from `tasks/TRAINING_Q.txt`:

- **Vertical stability**: within an R2/R4/R6/R8 “box”, does the pattern hold (boxed or straight)?
- **Horizontal stability**: as you move across columns (7→1), does the pattern persist through reductions?

### 3) Digit Reduction logic is about revealing what’s lingering (not deleting what’s pending)

From `tasks/TRAINING_Q.txt`:

- Three elimination modes (conceptually):
  - eliminate exact digits
  - eliminate occurrence w/ mirror awareness (prefer digit, else mirror)
  - eliminate both digit + mirror occurrences
- Use both “own” draw and “combined” draw digits as reduction inputs (captures cross-variant carryover).
- Use **transit digits** (remove 1 digit at a time) to avoid accidentally deleting the pending pattern.

### 4) Convergence beats any single signal (Superbrain = synergy engine)

From `tasks/IMPORTANT_SUPERBRAIN_GUIDE.txt`:

- The best candidates are touched by multiple independent subsystems:
  - cross-tool overlap (Stable + DR + VTRAC + Hot Zones)
  - cross-variant agreement (Midday/Evening/Combined)
  - cross-set persistence (Set3→Set2→Set1)
- Strings lead (candidate invention); Aux compounds (confirm/gate/boost/spend-control).

### 5) Winners HTML is an “evidence lens”; Superbrain must learn the same pattern language

- Winners HTML/JSON surfaces patterns that “count” even when the literal 3-digit winner is not sitting cleanly in one cell.
- Key concept to keep in mind during reviews: **clutter-digit removal** and **3‑VTRAC signature** can make an ugly long cluster analytically equivalent to a lane’s winning structure (even if the exact triple isn’t present as a substring).

### 6) Stable already “sees” long clusters; the missing piece is converting them into gradeable candidates

- In Stable raw scores (`*_stable_patterns_scores.csv`), many high-signal patterns are **4–7 digits long** and already carry:
  - `family_id` (VTRAC lane), and
  - `orders_modal_value` (dominant internal ordering).
- Current extraction contract (stable10 / `stable_top`):
  - Built in `scripts/tools/create_candidate_universe.py` (`_parse_stable_top`).
  - Reads `*_stable_patterns_scores.csv`.
  - Filters to **3-digit canonicals only** (anything longer than 3 digits is ignored; no long→triad conversion).
  - Picks top‑N per section by **max score** across all Set/Draw/Column rows for that canonical.
  - Converts picked canonicals into a BOX pack via **unique permutation expansion**.
- In `stable10`, the default Stable pack (`stable_top`) only extracts **top‑N 3‑digit canonicals** (because they are immediately playable/gradeable).
- So the high-value Superbrain opportunity is a bounded conversion step:
  - long cluster → lane vote, and/or
  - long cluster → small derived playable set (index closure / triad extraction),
  without exploding cost.

### 7) Two universal “gold sources”: late columns, or lingering long-box patterns

From `tasks/GOLDEN_RULES_T.txt` (and consistent with training):

- A) Often the winner neighborhood can be isolated **late in the strings** (survivor patterns / “3‑digit repeat” feel) near Columns `2→1`.
- B) Often the winner neighborhood is **lingering inside a longer string arena** (the Long-String / DR boxes) and needs “reveal” logic (Digit Reduction / clutter removal) to become obvious.

Practical implication: treat “late-column survivors” and “long-box lingerers” as equally valid upstream evidence sources.

### 8) “Survivor strength” is measurable: less clutter, more persistence, more structure

- A pattern that remains in a box with **less clutter** is stronger than a pattern that’s buried.
- Reward both:
  - **vertical stability** (R2/R4/R6/R8 coverage inside a box), and
  - **horizontal stability** (persistence across Columns `7→1`).
- When reviewing Stable/DR evidence, look for: “Is this pattern holding together across multiple boxes/columns, or is it a one-off?”

### 9) Always evaluate per-variant first; convergence comes second

From `tasks/GOLDEN_RULES_T.txt` + `tasks/IMPORTANT_SUPERBRAIN_GUIDE.txt`:

- Score/interpret patterns **inside each variant** (Midday / Evening / Combined) first.
- Then add **cross-variant convergence** as a boost (agreement makes it more credible, and helps budgeting).

### 10) Never mix up “evidence recall” with “budget conversion”

This is the core discipline from `tasks/REGROUP.txt`:

- Evidence recall: “Did Candidate Universe contain the winner lane / canonical?”
- Conversion: “Did the Play Card (B12/B24/B36) keep that lane and spend meaningful depth inside it?”

If conversion is lossy, it can make upstream tools look “bad” even when they were pointing at the right neighborhood.

### 11) Budget geometry matters: depth inside a lane is what converts lane hits into strict hits

From `tasks/REGROUP.txt` (plain English):

- Under B36, most non-top lanes often get **~1 line** of spend.
- If you only get 1 line inside the correct lane, strict conversion is hard; if you get 4–6 lines inside the correct lane, strict conversion becomes realistic.

Practical implication: if we can’t widen spend, we can still improve results by making the **1 line** we buy inside a lane smarter (inside-lane member choice / bounded closure).

### 12) Long-string arenas should be evaluated pre- and post-reduction

From `tasks/GOLDEN_RULES_T.txt`:

- Long-string boxes should be treated like their own “mini-world”:
  - evaluate what’s present **before** reduction,
  - and what becomes clearer **after** reduction (recent-draw digit elimination).

### 13) Pattern order is information (permutation clues → VTRAC straights)

From `tasks/GOLDEN_RULES_T.txt`:

- The **ordering** of a surviving cluster (ex: Stable `orders_modal_value`) is a real clue, not noise.
- It’s one of the main bridges from “boxed family / lane hit” → “straight hit on a low set” (VTRAC straight optimization).

---

## How To Use This Doc (simple)

1) Pick a casepack from the index.
2) Open its `MANIFEST.md` and follow the “Open order”.
3) Fill one “Case Entry” below (copy/paste the template).
4) If we identify a fix: write it as a **hypothesis + smallest test** (so we don’t thrash).

---

## Standard Outcome Labels (keep it consistent)

Use 1 primary label per case (optional secondary labels after).

- `HIT_STRICT` — exact straight hit (winner appears exactly).
- `HIT_BOXED` — exact boxed hit (winner digits appear in any order).
- `HIT_VTRAC_LANE` — winner’s VTRAC index is retained (but not necessarily the member).
- `MISS_LANE_DROP` — winner’s lane got **0 lines** in the budgeted surface (ex: B36).
- `MISS_MEMBER_WITHIN_LANE` — lane retained, but money spent on the wrong member(s).
- `MISS_EVIDENCE_GAP` — winner lane wasn’t meaningfully present in Candidate Universe (upstream miss).

---

## What We’re Usually Trying To Answer

### A) Did we “see it” upstream?
- Did Candidate Universe contain the **winner lane**?
- Did Candidate Universe contain the **winner canonical**?

### B) If we saw it, where did we lose it?
- Did B36 drop the lane entirely? (lane-drop)
- Or did B36 keep the lane but choose the wrong member(s)? (within-lane)

### C) What’s the cheapest *specific* improvement?
- Add/adjust **lane retention** rules? (prevent lane-drop)
- Add/adjust **within-lane closure / member selection** rules? (prevent within-lane miss)
- Adjust ranking/triage so we spend attention/budget where conversion is plausible?

---

## Case Entries

### Case Entry Template (copy/paste)

#### Case: `<ID>` — `<STATE>` — `D=<YYYY-MM-DD>` — `<Midday|Evening>` — winner `<###>`

**Links (SSOT receipts)**
- Casepack manifest: `<path>`
- Winners HTML: `<path>`
- MV run report: `<path>`
- Predictive Play Card (baseline): `<path>`
- Predictive Candidate Universe: `<path>`
- Predictive Aux summary: `<path>`
- Results line: `<path>`

**Facts (no interpretation)**
- Winner: `<###>` | canonical: `<###>` | VTRAC idx: `<#>`
- CU: lane present? `<yes/no>` | canonical present? `<yes/no>` | notable: `<1-2 facts>`
- B12/B24/B36: lane present? `<yes/no>` | canonical present? `<yes/no>` | notable: `<1-2 facts>`
- Outcome label: `<one of the labels above>`

**Environment notes (from Winners HTML/JSON)**
- Digit Reduction: any “Long-string (DR) box” evidence that matters? `<yes/no + 1 line>`
- Stable persistence: top patterns / repeats that look meaningful? `<1-3 bullets>`
- Hot Zones: any lane dominance signals? `<1-2 bullets>`

**Universal analytical power notes (if any)**
- `<1–5 bullets that generalize beyond this case>`

**My interpretation (plain English)**
- `<2–6 sentences>`

**Hypothesis (what to change)**
- Proposed change: `<1 sentence>`
- Why it should help: `<1–2 sentences>`
- Smallest test: `<what to re-run / what artifact should change>`

**Open questions**
- `<only if needed>`

---

## Seed Cases (already packaged)

### C035 — NewYork4 — D=2026-01-06 — Evening — winner `342`

- Casepack manifest: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/casepack__C035__NewYork4__2026-01-06/MANIFEST.md`
- Primary label (expected): `MISS_LANE_DROP`

#### Case: `C035` — `NewYork4` — `D=2026-01-06` — `Evening` — winner `342`

**Links (SSOT receipts)**
- Casepack manifest: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/casepack__C035__NewYork4__2026-01-06/MANIFEST.md`
- Winners HTML: `sharepacks/2026-01-06/NewYork4/winners/NewYork4/NewYork4_vtrac30_winner_342_20260107_052308.html`
- MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-06__NewYork4.md`
- Predictive Candidate Universe: `sharepacks/_predictive/2026-01-06/NewYork4/candidate_universe__tool_only__stable10.json`
- CU evidence (why a combo exists): `sharepacks/_predictive/2026-01-06/NewYork4/candidate_universe_evidence__tool_only__stable10.csv`
- Predictive Play Card (baseline): `sharepacks/_predictive/2026-01-06/NewYork4/play_card__tool_only__stable10.md`
- Stable raw scores (pre-results): `sharepacks/_predictive/2026-01-06/NewYork4/stable/NewYork4/NewYork4_stable_patterns_scores.csv`
- Results line: `data/results/2026-01-06.txt`

**Facts (no interpretation)**
- Winner: `342` | canonical: `234` | VTRAC idx: `30`
- CU lane members present (idx30): `379` only (no `234/239/248/289/347/478/789`)
  - Receipt: `sharepacks/_predictive/2026-01-06/NewYork4/candidate_universe_evidence__tool_only__stable10.csv:99` (`canonical=379` via `method_id=hot_zones_top`)
- Play Card (baseline): `379` does not survive into the final surfaces (it is absent from B36)
- Outcome label: `MISS_LANE_DROP`

**Environment notes (from Winners HTML + Stable raw scores)**
- Winners HTML shows long-string/lingering lane-30 structure in Evening long boxes (example substring: `29688447`), where `847` is highlighted as a family-member clue.
- Stable raw scores show lane-30 long clusters pre-results (examples):
  - `canonical=447788` / `canonical=44788` with `orders_modal_value=88447*` and `family_id=30`
    - Receipt: `sharepacks/_predictive/2026-01-06/NewYork4/stable/NewYork4/NewYork4_stable_patterns_scores.csv:2343`
    - Receipt: `sharepacks/_predictive/2026-01-06/NewYork4/stable/NewYork4/NewYork4_stable_patterns_scores.csv:2868`
  - `canonical=2234` with `orders_modal_value=3224` (matches the “clutter digit removal” intuition) and `family_id=30`
    - Receipt: `sharepacks/_predictive/2026-01-06/NewYork4/stable/NewYork4/NewYork4_stable_patterns_scores.csv:527`

**My interpretation (plain English)**
- This case reads like: the environment is “talking” in lane-30 long clusters, but our default extraction path only turns **top‑N 3‑digit Stable canonicals** into candidates.
- Result: CU gets a single idx30 member (`379` from Hot Zones), and the Play Card drops it because it lacks cross-pack support.

**Hypothesis (what to change)**
- Proposed change: add a bounded “Stable long-box → lane vote / closure” derived pack so lane-30 evidence can become a small playable set (instead of being trapped in long clusters).
- Smallest test: re-run candidate universe + play card for this day/state and confirm CU gains multiple idx30 members (not just `379`) and B36 retains ≥1 idx30 line.

### C036 — Delaware4 — D=2026-01-02 — Evening — winner `076`

- Casepack manifest: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/casepack__C036__Delaware4__2026-01-02/MANIFEST.md`
- Primary label (expected): `MISS_MEMBER_WITHIN_LANE`
