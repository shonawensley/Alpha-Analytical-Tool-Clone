# Delta (1‑page) — Classic Codex Deep Analysis → Crossroads “Truth Layer”

Purpose: explain **what changed**, **what it unlocked**, and **why this is progress** (not “more jargon”).

---

## TL;DR

- **Classic Codex Deep Analysis** answers: *“Do the tools touch the winning environment?”* (winner‑aware, proxy / presence / lane signals).
- **Crossroads Truth Layer** answers: *“Given that signal exists, do we retain it under B36 and convert it?”* (glass‑box, selection‑layer, bucketed failure modes).

The Crossroads work did **not** replace Classic analysis — it finished it by adding the missing **decision/compression** visibility.

---

## What Classic Codex Deep Analysis was (and why it was valuable)

Classic window reports (e.g. `...__CODEX_DEEP_ANALYSIS.md`) are a **post‑results reviewer**:

- treats tools as **signal / containment lenses** (Stable / Hot Zones / VTRAC / Aux),
- reports **proxy strength** (presence / placement / “winner lane touched”),
- is great for building the correct mental model: **signal ≠ selection**.

Example classic window:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-21__CODEX_DEEP_ANALYSIS.md`

### The limit (why it still felt like “we should be winning more”)

Classic analysis can show “signal exists” while “predictions are weak” because it does not fully decompose:

- what Candidate Universe (CU) contained,
- what the Play Card actually played under a budget,
- whether a miss happened **before** or **during** the budget cut.

So you were forced to infer the squeeze mentally.

---

## What Crossroads added (the missing truth layer)

Crossroads is a **glass‑box selection audit** with analyzers held stable:

- posture locked: `tool_only` + `stable10`
- budget locked: **B36 only**
- objective locked: **isolation‑first** (reduce “lane was in CU but dropped by Play Card”)
- guardrail: **OOS strict must not regress**
- constraint: **no analyzer edits** (selection‑layer only)

### The new instrumentation (why it ends loops)

Crossroads makes misses explicit via buckets:

- `CU_MISS` → the winner lane wasn’t in CU
- `CU_LANE_BUT_PLAY_MISS` → lane was in CU, but dropped by Play Card
- `CU_EXACT_BUT_PLAY_MISS` → exact winner was in CU, but dropped by Play Card

Plus: lane allocation and winner‑lane‑rank reporting:

- *“How far down the ranked lanes is the actual winner lane?”*
- *“How many lines did we allocate to the winner lane?”*

Core docs:
- flow map: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PIPELINE_FLOW__GLASS_BOX.md`
- policy SSOT: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`

---

## What this unlocked (the breakthrough)

You can now say, with receipts, **where the project is actually failing**:

- CU lane presence is high, but **B36 lane retention is materially lower**
- the dominant bottleneck becomes a measurable rate: **`CU_LANE_BUT_PLAY_MISS`**
- winner lanes are **shoulder‑heavy**, so “top few lanes only” policies are structurally brittle
- strict hits are “depth events” (in the current baseline, strict usually requires meaningful **within‑lane depth**)

Synthesis memo:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md`

Winner lane rank receipts:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36.md`

---

## What Crossroads invalidated (so we stop burning weeks)

- “High proxy hit rates” ≠ “we should be winning” unless selection **retains** the signal under budget.
- “Just add depth” isn’t automatically good if it’s purchased by collapsing breadth (dropping lanes).
- Analyzer edits before selection is instrumented are guesswork; Crossroads makes analyzer edits **earned** later.

---

## Your fastest re‑entry (3 files + 2 cases)

If you want the “I get it now” moment without drowning:

1) Resume card:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__SAVEPOINT__CROSSROADS__2026-02-13.md`
2) Case matrix:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CROSSROADS_CASE_MATRIX__2026-01-15.csv`
3) Cases index:
   - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`

Then open:
- **Case 3** (`CU_LANE_BUT_PLAY_MISS`) → the squeeze failure
- **Case 5** (strict‑hit anatomy) → what “conversion success” actually looks like

---

## How this connects back to “gold integration”

Classic deep analysis tells you **where the signal lives** (tool roles + convergence).
Crossroads tells you **whether the system can execute on that signal under budget**.

That’s the correct sequence for “integrate gold without lying to ourselves”:

1) lock evidence posture,
2) instrument selection failure modes,
3) iterate selection policy with promotion gates,
4) only then earn analyzer edits.

