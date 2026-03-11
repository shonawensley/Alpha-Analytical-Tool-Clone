# AAT9 DEEP EXAMPLE REVIEW ANALYSIS

Purpose: a single, human-friendly place to log what we learn from **casepack** deep dives (what the system *knew* pre-draw, what happened post-draw, and what we should change next).

This is not meant to replace the casepacks. Casepacks stay the “1‑click receipts.” This file is the **running analysis notebook**.

Related:
- Resume bookmark: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__BOOKMARK__CASEPACK_EXAMPLE_REVIEW.md`
- Casepacks index: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/README.md`
- Live integration queue: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AAT9_ANALYSIS_ARENA_INTEGRATION_QUEUE.md`
- Competition postmortem: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-09__COMPETITION_POSTMORTEM__analysis_arena_branch.md`

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
- Implementation status:
  - `order_transform_v1` is now wired into Stable Arena as an observability slice.
  - It preserves bounded transform recipes from modal orders and hidden fragments, including direct perms, VT8, and pair-mirror-third transforms.
  - Current guardrail: keep it as an inspection surface until calibration across positive and noisy controls shows what transform thresholds are predictive rather than merely descriptive.

### 14) We are optimizing extraction quality, not demanding a winner every draw

- The goal is **optimal extraction and interpretation** of real upstream evidence.
- We should expect plenty of draws where the environment is too noisy or too expensive to isolate a winner rationally.
- Success is not “force a winner every day”; success is “surface the strongest, most actionable evidence honestly.”

### 15) State ranking should reflect predictive quality, not just signal volume

- Cross-state ranking should favor states with the **best evidence quality**:
  - stronger convergence,
  - tighter / cleaner lanes,
  - better cost-to-coverage geometry,
  - more credible conversion potential.
- This means “top state” should really mean “best current predictive value per unit of risk/expense,” not “most alerts” or “most raw patterns.”

### 16) Long-term profitability comes from selective play and expense control

- The real target is **profitability / token accumulation over time**, not raw hit count.
- That pushes Superbrain toward:
  - finding the most favorable environments,
  - preferring the cheapest rational play mode,
  - and skipping or downgrading noisy states when the path to conversion is weak.

### 17) Open investigation: hidden winner-family patterns inside clutter digits

- We need to investigate whether the predictive system is truly using the same “hidden pattern behind clutter digits” logic that appears in Winners HTML/JSON.
- Example teaching case: `2026-01-06 NewYork4 342 / VTRAC 30`
  - Winners HTML highlights family-30 structure inside long strings like `29688447`, `66877059324`, and related family fragments (`347`, `324`, `243`).
  - Stable predictive artifacts already preserve some of the downstream family evidence (`family_id=30`, long canonicals like `4788`, `277889`, `447788`), but they do **not** currently preserve the full cell-level “how the hidden family was revealed” explanation.
- Investigation target:
  - preserve source cell text / source literal when relevant,
  - preserve family-fragment hits inside long strings,
  - and test whether this should become a first-class predictive feature rather than a post-results-only winners artifact.
- Implementation status:
  - `hidden_reveal_v1` is now wired into Stable Arena as an observability slice.
  - It preserves source literals / locators and surfaces row-level hidden-family evidence plus family/pattern rollup summaries.
  - Current guardrail: keep it as an inspection surface until calibration across positive and noisy controls shows what threshold is predictive rather than merely descriptive.

### 18) Lingering / surviving patterns are a primary predictive evidence class

- The system must explicitly preserve, surface, and score lingering structures before downstream projection or budgeting.
- Highest-value lingering evidence includes:
  - repeats,
  - late/frontier survivors,
  - VTRAC-related echoes,
  - cross-variant reinforcement,
  - and long clusters that keep holding the same structural family.

### 19) Think in winner family / transformation corridor, not only literal winner presence

- Many important cases are not mainly saying “here is the exact winner.”
- They are saying something closer to:
  - here is the winner family,
  - here is the progression corridor,
  - here are the order / permutation transformations still alive around that family.

### 20) Arena learning comes before serious combination-forming redesign

- Do not let the old rushed combination layer define what evidence the arena should keep.
- First preserve the best evidence classes.
- Then learn what should later be scored, forwarded, trapped, or budgeted.

### 21) Ranking must eventually correlate with predictive value over time

- This is a design north star now, not an immediate pass/fail gate for the current Stable-first slice.
- We should eventually expect stronger-ranked states to trend toward stronger predictive value / hit rates over time.
- But we should only treat that as a hard validation gate after more arena fields and more tool feeds are in place.

### 22) The analysis arena is an evidence stage, not a hidden play-card prefilter

- The arena should first preserve the strongest evidence classes from each tool.
- It should not quietly collapse back into an early B12/B24/B36-style narrowing step.
- The point is to preserve, inspect, compare, and only later decide what deserves forwarding.

### 23) Tool-by-tool arena feeding is the correct build order

- Build the arena one tool at a time:
  - Stable,
  - Digit Reduction,
  - Hot Zones,
  - VTRAC analyzer,
  - Aux / Control Center context.
- For each tool, ask:
  - what valuable evidence should it add,
  - what was missing before,
  - and what should now be preserved or promoted.

### 24) Do not judge downstream profitability before arena fidelity

- Before discussing profitability, final ranking, or final combination-forming for a tool slice, answer:
  - what did the winners lens show,
  - what did the arena preserve,
  - what did the old path lose,
  - and what exact evidence did this tool now add.
- Profitability remains the long-term goal, but arena fidelity is the immediate gate.

### 25) Observe compounding before retuning feature weights

- Before changing feature weights, make the compounding ledger visible.
- We need to be able to see, per pattern and per variant:
  - how many mini-progressions contributed,
  - which feature parts contributed,
  - how totals and peaks were formed,
  - and which rows / boxes / spans actually created the final score.
- Otherwise we cannot tell whether a feature is weak, under-consumed, or merely hidden by later projection.

### 26) Top-N is a summary surface, not the system’s truth model

- Top-5 / top-10 displays are useful for human review.
- They should not be treated as the full truth of what the extractor or arena preserved.
- The richer underlying evidence must remain available even when the display surface is intentionally small.

### 27) Do not force every new phenomenon into the legacy tool boundaries

- If a new evidence type does not fit cleanly inside Stable, DR, Hot Zones, or the VTRAC analyzer, we should be willing to create a new focused tool for it.
- The goal is not “tool purity.”
- The goal is:
  - clear extraction semantics,
  - low blast radius,
  - clean arena inputs,
  - and easier validation on examples.

### 28) Brain 1 and Brain 2 should stay distinct

- `Brain 1` = the per-state analysis arena:
  - tools extract the strongest evidence they can from that state’s string-table environment,
  - the arena preserves and scores that evidence,
  - and the system learns what the state is really saying.
- `Brain 2` = the cross-state macro lens:
  - compare all states,
  - rank which environments are worth attention or money,
  - and apply profitability / expense-control logic.
- They should inform each other, but they should not be collapsed into one rushed layer.

### 29) Grade ticket performance separately from arena performance

- A live ticket can miss even when the arena already preserved the winner meaningfully.
- For development, we need to track both:
  - what the ticket hit,
  - what the arena preserved,
  - and what the candidate universe already carried pre-results.
- Otherwise we hide real progress inside a bad final conversion.

### 30) Doubles / mirror-doubles are a distinct predictive regime

- Current evidence suggests the system is often strongest in double-heavy and mirror-double-heavy environments.
- These states are also cheaper to close because the relevant VTRAC families are smaller.
- Do not collapse doubles-driven states and 6-way single states into one undifferentiated ranking / promotion policy.

### 31) A strong pair-anchor plus one lingering fourth variable is a real closure principle

- Often the system isolates the right pair / mirror-pair skeleton, but the final winner resolves as:
  - the double itself,
  - the mirror-double family,
  - or that same structural core plus one recurring extra digit / VTRAC-pair digit.
- This means the predictive object is often not just one canonical; it is a bounded closure set around:
  - a strong pair-anchor,
  - mirror-pair space,
  - and one extra lingering variable.

### 32) Same-day midday-to-evening transition is first-class evidence

- Midday results should not be treated as an afterthought in evening competitions.
- They can matter in two opposite ways:
  - `carry-forward / repetition` pressure,
  - `reduction / elimination` pressure.
- The system should eventually score both instead of relying on ad hoc manual judgment.

### 33) Family-lane promotion should reward arena rank-lift, not raw family max alone

- The `stable_family_vote_v2` validation made one thing very clear:
  - the rescue families we care about are often **not** the best `family_score_max` families,
  - they are the families whose rank improves materially when richer arena evidence is included.
- That means a good promotion rule should care about:
  - legacy rank,
  - arena rank,
  - and the size of that lift,
  not just whether a family is generically “strong.”
- This is what allowed Example 1 / `C035` to promote `Evening family 30` instead of merely promoting another already-strong excluded family.

---

## Stable Family Vote V2 Validation (2026-03-11)

Related:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-11__STABLE_FAMILY_VOTE_V2__VALIDATION.md`

What landed:
- `stable_family_vote_v2` is now the first bounded Stable family-lane promotion rule that consumes richer arena evidence rather than raw family max alone.
- It stays additive:
  - legacy `stable_family_vote` is untouched,
  - the new rule is default-off,
  - and it adds only one extra bounded family-lane pack per variant/section.

Most important result:
- `C035 / 2026-01-06 / NewYork4 / Evening 342` is now a true rescue case.
  - baseline `stable10` CU missed boxed canonical `234`
  - `stable_family_vote_v2` promotes `Evening family 30`
  - the v2 CU now contains boxed `234`

Control read:
- `C036 / Delaware4` did not get a fake rescue.
- `2026-01-09 / Pennsylvania4` gained a bounded lane rescue without pretending to solve every closure problem.
- `2026-01-08 / NorthCarolina4` stayed noisy and was not falsely “fixed.”

January harness headline:
- On `245` evaluable winner events across `2026-01-01 .. 2026-01-09`, the v2 rule improved:
  - exact hits from `50 -> 64`
  - boxed hits from `63 -> 75`
  - Stable family-lane hits from `0 -> 23`
- It also produced:
  - `19` exact rescues
  - `18` boxed rescues
  - `13` lane-only rescues

Interpretation:
- This slice improved preservation/promotion materially.
- It did not solve within-lane closure completely.
- That is acceptable, because this slice was meant to rescue strong families that were being cut too narrowly, not finish the entire closure problem.

Development consequence:
- Stable family-lane promotion is now strong enough to stop being the top open blocker.
- The next most valuable slice is pair-anchor + lingering fourth-variable closure.

---

## How To Use This Doc (simple)

1) Pick a casepack from the index.
2) Open its `MANIFEST.md` and follow the “Open order”.
3) Fill one “Case Entry” below (copy/paste the template).
4) If we identify a fix: write it as a **hypothesis + smallest test** (so we don’t thrash).
5) Log every important actionable item to the live integration queue:
   - `rule`
   - `tracker`
   - `tool`
   - `arena`
   - `policy`
   - `test`

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

## Competition 2026-03-09 Distilled Takeaways

Reference:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-09__COMPETITION_POSTMORTEM__analysis_arena_branch.md`

What should remain in durable memory from this competition:

- The ticket missed more than the arena did.
  - `Ontario 559` and `Connecticut 019/091` were already preserved in the arena / candidate universe pre-results.
  - Those were conversion / promotion misses, not pure evidence misses.
- `NewJersey` and `NewYork` were true evening evidence misses.
  - The favored rails were wrong for the final evening outcome.
- Midday relevance was real:
  - `NewJersey` midday `617` was preserved in the arena as canonical `167`.
  - `Connecticut` midday `917` likely signaled a same-day carry / permutation relationship into evening `091`.
  - `NorthCarolina` midday `855` matched the selected family-4 corridor by VTRAC, even without an exact boxed hit.
- The competition reinforced that doubles / mirror-doubles and small family-closure neighborhoods remain one of the system's strongest practical strengths.
- The competition also surfaced a stronger closure principle:
  - when the system isolates the right pair-anchor or double-pressure core,
  - the missing piece is often one lingering fourth variable rather than a totally different lane.

Development meaning:

- preserve `ticket grading` and `arena grading` separately
- add midday-to-evening transition scoring
- keep doubles / mirror-doubles as a first-class regime
- eventually let the arena preserve pair-anchor plus fourth-variable closure objects explicitly

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
