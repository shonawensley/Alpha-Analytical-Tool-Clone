# Codex Deep Research Mirror — Crossroads (D=2026‑01‑15; stable10 • tool_only • B36)

Purpose: a Codex-built “deep research” style memo that mirrors the ChatGPT Pro prompt deliverables, using only SSOT artifacts (RUNS + sharepacks). This is designed to be **actionable**: it should end with 1–2 selection-layer changes you can implement + grade, with explicit promotion gates.

Scope:
- **Selection-layer only** (no analyzer edits: Stable / DR / VTRAC / Hot Zones stay treated as evidence producers).
- Posture: `tool_only` + `stable10`
- Budget: **B36 only**
- Baseline strategy under study: `v0_2_default_multi_pack_packheavy_spine4_index_tail`
- North Star: **isolation-first** (reduce `CU_LANE_BUT_PLAY_MISS`)
- Guardrail: **OOS strict B36 must not regress** vs baseline.

Read order (SSOT):
- Flow: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PIPELINE_FLOW__GLASS_BOX.md`
- Glossary: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md`
- Policy: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`
- Crossroads pack v1: `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/README.md`

---

## 1) One‑page plain‑English budget explainer

### What “B36” actually is
`B36` means: the Play Card contains exactly **36 straight 3‑digit combo lines** (e.g., `"598"`).  
It is not bankroll, not ROI, not “number of canonicals”. It is the **line cap** of the selection cut.

Where it lives:
- Play Card JSON: `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.json`

### Where the “prediction” happens
The tools don’t “predict”; they produce evidence. The **prediction surface** is the Play Card:

Evidence snapshot (sharepacks) → Candidate Universe (unbounded pool) → **Play Card (budgeted cut)** → grading.

If you are feeling “we’re squeezing wins into a shoe”, that shoe is the Play Card cut.

### What “lanes” are
A “lane” is the winner’s **VTRAC index** (the shared neighborhood coordinate).  
If the Play Card contains **any** combo from the winner’s VTRAC index, you get `vtrac_index_hit=1`.

### Canonical vs straight (the source of 30% of confusion)
- Winner straight: exact `"950"`
- Winner canonical: digits sorted `"059"`
- Perm-hit: any perm of `"059"` is present
- Strict boxed hit: all perms of `"059"` are present (6 lines for most canonicals)

### Packs / spine / tail (what `spine4_index_tail` means)
In `v0_2_default_multi_pack_packheavy_spine4_index_tail`:
- **Spine**: take the **top 4 ranked indices** and insert a deep VTRAC “display pack” for each.
- **Tail**: use remaining budget to “touch” additional ranked indices with **1 line per lane**.

This is a deliberate breadth/depth trade:
- Spine protects strict conversion (depth events).
- Tail tries to prevent “lane dropped” failures (isolation-first).

Where to see the actual geometry:
- Lane allocation report (Jan window): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`

---

## 2) Truth layer recap (what is actually happening right now)

### In-sample window (Jan gold)
Scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`

Baseline (`spine4_index_tail`) @ B36:
- CU union lane recall: `78.8%`
- Play Card strict (`hit_any`): `5.7%`
- Play Card inclusive coverage (`hit_any_inclusive`): `47.2%`
- `CU_LANE_BUT_PLAY_MISS`: `26.9%`
- `CU_EXACT_BUT_PLAY_MISS`: `4.7%`

### OOS window (guardrail)
Scoreboard: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md`

Baseline (`spine4_index_tail`) @ B36:
- CU union lane recall: `71.0%`
- strict (`hit_any`): `4.1%`
- inclusive (`hit_any_inclusive`): `42.0%`
- `CU_LANE_BUT_PLAY_MISS`: `24.1%`
- `CU_EXACT_BUT_PLAY_MISS`: `4.9%`

Interpretation (the Crossroads answer in one sentence):
> **Evidence is often present (CU lane recall is high), but the B36 selection cut drops too many winner lanes (and strict hits are “depth events” when we do retain the lane).**

---

## 3) Bucket anatomy summary (from the 5 Crossroads cases)

Case index (deterministic): `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`  
Case matrix (single table): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CROSSROADS_CASE_MATRIX__2026-01-15.csv`

### Bucket: `CU_MISS` (evidence did not touch the lane)
Example: Ontario Evening (winner `791`, idx `22`)
- CU union: `vtrac_index_hit=0`
- Play Card: cannot recover it (`hit_any_inclusive=0`)

Mechanical signature:
- You can change Play Card geometry all day and it will not “buy back” a lane that never entered CU.

Action (not in scope for Crossroads v1):
- This is an analyzer/evidence posture lane of work (separate phase; don’t mix into selection experiments).

### Bucket: `CU_LANE_BUT_PLAY_MISS` (lane in CU, dropped by the cut)
Example: NewYork Midday (winner `901`, idx `9`)
- CU union: `vtrac_index_hit=1`
- Play Card: `vtrac_index_hit=0` (lane dropped)
- Winner lane rank (packs-first) is deep (case shows rank `26`)

Mechanical signature:
- Winner lane is in evidence, but outside the ranks the Play Card can afford to cover under B36.

Action (in scope; isolation-first):
- Improve lane retention beyond rank ~15 **without collapsing breadth**.

### Bucket: `CU_EXACT_BUT_PLAY_MISS` (exact was in CU, but we cut it)
Example: Delaware Evening (winner `107`, idx `7`)
- CU union: `hit_any=1` (exact/perm present)
- Play Card: `hit_any=0`, and lane dropped (`vtrac_index_hit=0`)
- Geometry is “spiky” (indices touched only `12`, max lines on one index `8`)

Mechanical signature:
- We had a high-value exact candidate in the pool, but budget geometry + lane selection removed its lane entirely.

Action:
- Reduce the “spiky spine steals tail budget” failure mode so we don’t drop ranked lanes when a spine index has an oversized pack.

### Bucket: `HIT_INCLUSIVE` (lane retained; strict miss)
Example: Ontario Midday (winner `598`, idx `14`)
- CU union lane present, Play Card lane retained
- `winner_lane_lines=1` (tail-depth)

Mechanical signature:
- Evidence + retention succeeded, but within-lane depth was shallow; strict misses are expected.

Action:
- Treat strict misses in this bucket as “depth/candidate choice within lane” problems, not “tool is dead”.

### Strict hit anatomy (still bucketed as `HIT_INCLUSIVE` by the ladder)
Example: NorthCarolina Midday (winner `045`, idx `5`)
- strict `hit_any=1`
- `winner_lane_lines=6` (spine-depth)
- winner lane rank is high enough to be in the spine (case shows ranks `4/5/6`)

Mechanical signature:
- In the current system, strict hits overwhelmingly occur when the winner lane receives **~6+ lines**.

---

## 4) Isolation‑first shoe design memo (what geometry the evidence implies)

### The two facts we now have “on paper”

1) **Spine spikiness collapses breadth.**
From the lane allocation CSV (Jan window):
- When `max_lines_single_index=6`: mean indices touched ≈ `17.0`, inclusive ≈ `55.3%`
- When `max_lines_single_index=8`: mean indices touched ≈ `14.1`, inclusive ≈ `40.7%`

Evidence:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINE4_INDEX_TAIL.csv`

2) **Winners live in the shoulder, not the top 3.**
From winner lane rank (Jan window; evidence ranking, not selection):
- Winner lane rank ≤10 (packs-first): `28.5%`
Meaning: “top few lanes” policies are structurally brittle.

Evidence:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36.md`

### What this implies for B36

At fixed B36, the best isolation-first purchase is:
- Keep a deep spine (so strict can still happen when we *do* choose the right lane),
- but prevent the spine from stealing tail budget unpredictably (spikiness),
- so the tail can reliably touch enough ranked lanes to reduce `CU_LANE_BUT_PLAY_MISS`.

This is a “compression engineering” problem, not a signal problem:
- CU recall is ~71–79% lane-touch.
- Play Cards retain only ~42–47% of those lanes under B36.

---

## 5) Two minimal selection-layer improvements (no analyzers)

These are intentionally small, deterministic, and gradeable.

### Proposal A — “Spine cap” (anti-spike): limit spine packs to a fixed per-index quota

Observation:
- `spine4_index_tail` currently inserts the **full** VTRAC display pack for each spine lane.
- Some display packs are larger (8 lines), which makes the card “spiky” and reduces indices touched.

Change:
- Create a new strategy variant that caps spine insertion at **6 lines per spine index** (or, equivalently, enforces a fixed `spine_total_quota=24`).
- Spend the freed lines on additional tail indices (1 line per lane), preserving the isolation-first goal.

Where to implement:
- `scripts/tools/create_play_card.py` → `_card_v0_2_default_multi_pack_packheavy_spine4_index_tail`

Expected metrics movement (Jan window):
- Improve: `hit_any_inclusive` (coverage contract)
- Improve: `CU_LANE_BUT_PLAY_MISS` (primary objective)
- Possibly regress slightly: `hit_any` (strict), but must pass guardrail OOS.

Promotion gate:
- Jan window: `CU_LANE_BUT_PLAY_MISS` **must drop** vs baseline `26.9%`
- OOS window: strict `hit_any` **must not regress** vs baseline `4.1%`

### Proposal B — “Evidence-first spine” (strict-protect): choose spine lines from CU lane rows before display fallback

Observation:
- Spine lines currently come from the static display pack ordering, not from top-evidence CU rows.
- Strict hits are depth events; if we can get “better 6 lines” in the spine, we may protect strict while still freeing tail breadth (Proposal A).

Change:
- In the spine indices, select up to the quota from `lane_rows[idx]` first (best-evidence combos),
  then backfill with display pack tokens only if needed.
- Keep everything else the same (same indices_ranked, same quotas).

Where to implement:
- `scripts/tools/create_play_card.py` → same function; add a new strategy key so baseline remains unchanged.

Expected metrics movement:
- Improve or maintain: strict `hit_any` (guardrail protection)
- Maintain: `hit_any_inclusive`

Promotion gate:
- Jan window: must not increase `CU_LANE_BUT_PLAY_MISS` (don’t pay strict for breadth loss)
- OOS window: strict must not regress

---

## 6) Top 5 spiral triggers (and the artifact that prevents each)

1) **Confusing tools with predictions**
- Fix: remember “Play Card = prediction”; read `V0_3__PIPELINE_FLOW__GLASS_BOX.md`

2) **Treating inclusive coverage as strict hits**
- Fix: read glossary definitions (`hit_any` vs `hit_any_inclusive`) in `V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md`

3) **Mixing POST forensics into PRE narratives (leakage arguments)**
- Fix: enforce PRE/DECISION/POST triangulation from `V0_3__CROSSROADS_SYNTHESIS__2026-01-15.md`

4) **Forgetting censored outcomes (`winner_missing=1`)**
- Fix: always consult the windowed reports that filter censored outcomes (scoreboards/lane allocation)

5) **Leading-zero canonical confusion (Excel)**
- Fix: treat canonicals as 3-char text; see canonical section in `V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md`

---

## Appendix: the single best “starter loop” (repeatable)

1) Pick a case from `CASES.md`
2) Open:
   - PRE: predictive report
   - DECISION: glass-box trace
   - POST: MV + winners HTML
3) If the case is `CU_LANE_BUT_PLAY_MISS` or `CU_EXACT_BUT_PLAY_MISS`, treat it as a selection-geometry failure and only propose Play Card changes.
4) Encode exactly one strategy variant, regenerate ladder/scoreboard for Jan + OOS, and promote only if it passes the gate.

