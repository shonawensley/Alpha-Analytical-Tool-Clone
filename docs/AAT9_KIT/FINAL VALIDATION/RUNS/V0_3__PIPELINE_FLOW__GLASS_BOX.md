# v0.3 Glass‑Box Flow (Evidence → CU → Play Card → Grades)

Purpose: make the pipeline mechanically legible so reviews stop turning into jargon spirals.

Scope: **selection-layer only** (tool outputs are treated as evidence; we tune how we *spend* a fixed budget).

SSOT companions:
- Policy (what to trust / what “good” means): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`
- Glossary (metric semantics): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md`
- Portal (everything that exists): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`

---

## The whole system in one diagram

```mermaid
flowchart LR
  H[History date H<br/>(workbook input)] -->|PRE| SP[Sharepack D = H+1<br/>sharepacks/_predictive/D/…<br/>(winner-free evidence snapshot)]
  SP --> CU[Candidate Universe (CU)<br/>“what we could play”<br/>(unbounded pool)]
  CU --> PC[Play Card<br/>“what we would play”<br/>(budgeted cut: B12/B24/B36)]
  PC -->|POST| G[Grading<br/>compare Play Card vs results]
  G --> R[RUNS reports (SSOT)<br/>ladders • scoreboards • casebooks<br/>lane allocation • lane rank]
```

If you remember only one thing:
- **Sharepacks/CU are evidence.**
- **Play Cards are the “predictions” (budgeted selection).**

---

## The v0.3 cadence (PRE vs POST)

PRE builds the winner‑free predictive snapshot:
```bash
python3 scripts/tools/run_v0_3_cycle.py pre \
  --history-date <H> \
  --sharepacks-root sharepacks/_predictive \
  --profile tool_only \
  --stable10 \
  --runs-subdir V0_3 \
  --write-audit-evidence \
  --play-card-write-md \
  --force
```

POST grades once results exist (`data/results/<D>.txt`):
```bash
python3 scripts/tools/run_v0_3_cycle.py post \
  --date <D> \
  --sharepacks-root sharepacks/_predictive \
  --profile tool_only \
  --stable10 \
  --runs-subdir V0_3 \
  --rollup \
  --windowed-auto \
  --force
```

---

## Where the “budget squeeze” actually happens

Budgets are **line caps** in the Play Card:
- **B12/B24/B36 = how many straight 3‑digit combo lines** end up in the Play Card JSON.
- Budgets do *not* change analyzer outputs; budgets only change the **selection cut**.

The core trade (why this is hard) is:
- **Breadth** = how many VTRAC indices (“lanes”) you touch.
- **Depth** = how many lines you buy *within* a lane.

With limited lines (B36), you cannot maximize both simultaneously.

---

## “Lane” in plain English (what the reports mean)

A **lane** is the winner’s **VTRAC index** (shared neighborhood coordinate across tools).

In RUNS reports you’ll see:
- `winner_vtrac_index` = the winner’s lane.
- `vtrac_index_hit` = Play Card touched at least one combo from the winner’s lane.
- `hit_any_inclusive` = “lane retained or better” (strict OR perm OR lane).

Why we measure this:
- If **lane is present but strict misses**, conversion/selection geometry is the lever.
- If **lane is missing in CU**, analyzers/evidence posture is the lever (separate step; not today).

---

## The 5-question “one real example” workflow (repeatable)

Pick one `D` + one `state_key` + one `winner_label` (Midday/Evening/Combined), then answer:

1) What is the winner (straight)?
2) What is the canonical (digits sorted)?
3) What is the winner lane (VTRAC index)?
4) Did the **CU union** touch the lane? (`cu_union_vtrac_index_hit`)
5) Did the **Play Card** retain the lane, and how many lines did it allocate?

### Which files answer those questions (always the same)

Winner lens (condensed; optional but useful):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__WINNERS_DIGEST.md`

Candidate Universe grade (CU union truth; unbounded):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CANDIDATE_UNIVERSE_GRADE__tool_only__stable10.csv`

Play Card grade (what we “predicted”; budgeted):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PLAY_CARD_GRADE__tool_only__stable10.csv`

Lane allocation (how many lanes, how many lines on the winner lane):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<Dfrom>_to_<Dto>__LANE_ALLOCATION__tool_only__stable10__B36__*.csv`

Concrete debug examples (buckets; stops “vibes”):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<Dfrom>_to_<Dto>__CONVERSION_CASEBOOK__tool_only__<strategy>__stable10__B36.md`

Sharepack artifacts (the actual JSON you inspect):
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only__stable10.json`
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__tool_only__stable10.csv`
- `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.json`

---

## 3‑view triangulation (PRE / DECISION / POST)

Use this every time you review a miss/hit so we stop mixing layers:

- **PRE (winners‑free evidence):**
  - Predictive run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>__PREDICTIVE__tool_only.md`
  - Predictive sharepack artifacts: `sharepacks/_predictive/<D>/<STATE>/...`

- **DECISION (the squeeze / “what we would play” under budget):**
  - Glass‑box trace: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__GLASS_BOX_TRACE__<STATE>__<LABEL>__<strategy>__B36__stable10.md`

- **POST (winner‑aware forensics + spec):**
  - MV run report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
  - Winners HTML/JSON: `sharepacks/<D>/<STATE>/winners/<STATE>/*.html`

Important:
- MV is where we write hypotheses/spec (“how we should consume tool evidence”).
- Predictive behavior only changes when we encode those hypotheses into **selection-layer code/policy** and re‑grade.

---

## Start here: Ontario example

This is the “one real example” walkthrough for Ontario, using:
- Window: `D=2026-01-15` (in the Jan gold window)
- Strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail`
- Budget: `B36`

Open:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLASS_BOX_TRACE__ONTARIOCANADA4__2026-01-15.md`

---

## How to scale beyond one state (without drowning)

Once the Ontario walkthrough clicks, scale out in this order:

1) Same date, 2–3 more states across different buckets (from the casebook):
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10__B36.md`
2) Then repeat on the OOS window (proves we’re not overfitting the Jan window):
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail__stable10__B36.md`

Rule: pick **one bucket at a time** (e.g., only `CU_LANE_BUT_PLAY_MISS`) so we’re diagnosing a single failure mode per session.
