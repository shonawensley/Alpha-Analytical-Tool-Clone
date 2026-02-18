# Side Review Guide — Artifacts (v0.3 • stable10 • tool_only)

Purpose: let you **review and learn on the side** (in a bounded way) while Codex keeps running **single‑lever selection experiments** without getting trapped in “what do I open?” loops.

This is not a “read everything” list. It’s a **map**: which artifact answers which question, and which 2–3 things to open depending on your available time.

---

## 0) When you *should* jump in (high-value human checkpoints)

I will explicitly flag these moments before proceeding:

- Changing invariants (budget `B36` → something else; `tool_only` → mixed; `stable10` → `stable11`; turning analyzers back on).
- Moving from selection‑layer only → **analyzer edits** (real “tool edits”).
- Promoting a new default policy that materially changes behavior.

Everything else (single‑lever Play Card strategy variants with receipts) can keep running without you.

---

## 1) The artifact map (by “layer”)

Think of the system as: **PRE (evidence) → DECISION (budget cut) → TRUTH (grades) → POST (winner-aware forensics)**.

### PRE (winners‑free: “what did we know before results?”)

**Cross‑state (rank states + see the final picks for the day):**
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO__tool_only.md`
  - Example: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__PREDICTIVE_PORTFOLIO__tool_only.md`
  - What it answers: “Which states looked strongest?” + “What are the B12/B24/B36 plays for each state?”

**Per‑state (predictive report scaffold):**
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>__PREDICTIVE__tool_only.md`
  - Example: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__OntarioCanada4__PREDICTIVE__tool_only.md`
  - What it answers: “Where is the frozen predictive evidence for this state/day?”

**Frozen predictive evidence (the real “glass box” payload):**
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only__stable10.json`
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe_evidence__tool_only__stable10.csv`
- `sharepacks/_predictive/<D>/<STATE>/play_card__tool_only__stable10.json`
- `sharepacks/_predictive/<D>/<STATE>/signals_bundle__tool_only__stable10.json`
  - What it answers: “What candidates exist?” + “Where did they come from?” + “What did the Play Card actually output under B36?”

### DECISION (the “shoe squeeze”: what got cut to fit B36?)

**Single‑outcome glass‑box trace (best first deep example):**
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLASS_BOX_TRACE__ONTARIOCANADA4__2026-01-15.md`
  - What it answers: “Winner → lane → CU → Play Card → bucket” in one narrative.

**Crossroads teaching casebook (5 curated cases):**
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__CROSSROADS_CASE_MATRIX__2026-01-15.csv`
  - What it answers: “Show me one clean example of each failure mode.”

### TRUTH (windowed grades: did it work, and where did mass get lost?)

**Policy SSOT (what is current default + what was promoted/rejected and why):**
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`
  - This doc links directly to the ladder/casebook/alloc reports for the **current default** and key experiments.

**Window scoreboards (the scoreboard is not a state rank; it’s a metric partition):**
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<W>__CONVERSION_SCOREBOARD__tool_only__stable10__...md`
  - Example (Jan window): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__BASELINE.md`
  - What it answers: strict vs inclusive, and buckets like `CU_MISS`, `CU_LANE_BUT_PLAY_MISS`, `CU_EXACT_BUT_PLAY_MISS`.

**Conversion ladder + casebook (clickable “rows that made the scoreboard”):**
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<W>__CONVERSION_LADDER__...csv|md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<W>__CONVERSION_CASEBOOK__...md`
  - What it answers: “Which exact outcomes were in each bucket?”

**Lane allocation + winner lane rank (diagnostics that disambiguate lane ranking vs within‑lane spend):**
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<W>__LANE_ALLOCATION__...md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<W>__WINNER_LANE_RANK__...md`
  - What it answers: “Did we *touch* the winner lane?” + “How many lines went into it?” + “Where does the winner lane sit in the rank distribution?”

**Corpus rollups (broad “how are we doing across many days?”):**
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only__stable10.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__tool_only__stable10.md`
  - What it answers: “Across the whole corpus, what’s our strict/inclusive rates by strategy/budget?”

### POST (winner-aware forensics: “what actually happened?”)

**Master Validation (MV) reports (post‑results narrative, includes tool interpretation lens):**
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
  - Example: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__OntarioCanada4.md`

**Winner HTML/JSON (ground truth + pattern visuals):**
- `sharepacks/<D>/<STATE>/winners/<STATE>/*.html`
  - Example: `sharepacks/2026-01-15/OntarioCanada4/winners/OntarioCanada4/*.html`

---

## 2) What to open depending on how much time you have

### If you have 5 minutes (pure “what did it pick?”)

1) `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO__tool_only.md`
2) Find your state (Ontario) and skim the **B36** line list it prints.

### If you have 30 minutes (see the bottleneck once, clearly)

1) `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PIPELINE_FLOW__GLASS_BOX.md`
2) `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/crossroads_glass_box__2026-01-15/CASES.md`
3) Open only:
   - Case 3 (`CU_LANE_BUT_PLAY_MISS`)
   - Case 5 (strict-hit anatomy)

### If you have 2 hours (one full state/day triangulation)

For Ontario, D=2026‑01‑15:

1) PRE: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__OntarioCanada4__PREDICTIVE__tool_only.md`
2) PRE payload: `sharepacks/_predictive/2026-01-15/OntarioCanada4/candidate_universe_evidence__tool_only__stable10.md`
3) DECISION payload: `sharepacks/_predictive/2026-01-15/OntarioCanada4/play_card__tool_only__stable10.md`
4) TRUTH (window): open the *current default* links from:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`
5) POST: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__OntarioCanada4.md` + winners HTML under `sharepacks/2026-01-15/OntarioCanada4/winners/`

---

## 3) Quick clarifications (so you don’t fight the same war again)

- **Portfolio** ranks *states* for a single day (pre‑results).
- **Scoreboards** rank *strategies* (or summarize a strategy family) across a *window* of outcomes (post‑grade).
- `B12/B24/B36` are **line-count budgets** in the Play Card output (36 means 36 combos printed), not “tool strength”.
- If you feel the urge to “scrap the shoe”: you can scrap *the strategy family* later, but you still need a budgeted cut. The truth-layer artifacts (buckets + receipts) remain useful either way.

