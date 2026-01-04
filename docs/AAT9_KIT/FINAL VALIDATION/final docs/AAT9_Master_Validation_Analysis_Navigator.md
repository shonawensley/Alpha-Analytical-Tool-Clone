# Master Validation — Analysis Navigator (how to review without getting lost)

Purpose: give you (or a zero‑context Codex session) a **single, deterministic reading order** for analyzing a frozen day snapshot (sharepacks) and the filled run reports, so you can extract insights without drifting into “tool spelunking” or doc loops.

Scope: analysis + navigation only.
- **Do not** change analyzers (Stable/DR/VTRAC/Hot Zones) while following this.
- Prefer reading **only** from `sharepacks/<D>/...` (immutable day snapshot) and `docs/AAT9_KIT/FINAL VALIDATION/RUNS/...` (run reports).

---

## 0) Definitions (the non-negotiables)

- **D** = results/winners date (**sharepack folder name**): `sharepacks/<D>/...`
- **H** = history workbook date (tables/draws “world snapshot”), usually **D‑1**
- **Outcomes** = `Midday` + `Evening` only (real winning draws)
- **Combined** = a lens (not an outcome stream)

Always ground yourself with:
- `sharepacks/<D>/README.md`
- `sharepacks/<D>/control_center/meta.json` (Brain‑2 provenance)
- Concept primer (pattern progression lens): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Pattern_Progression_Primer.md`

---

## 1) What “Done” looks like for a day (so you don’t second‑guess)

For a given D, you should be able to review everything you need from:

- **Brain‑1 (per state) frozen evidence**: `sharepacks/<D>/<STATE>/...`
- **Brain‑2 (Control Center) frozen evidence**: `sharepacks/<D>/control_center/...`
- **Per‑state run reports** (filled answers): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
- **Per‑day summaries**:
  - Brain‑2: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CONTROL_CENTER.md`
  - Brain‑1: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__DAY_SYNTHESIS.md` (optional, but recommended)

If any of those are missing, log it as **Fix‑Now (pipeline/artifacts)**, not as “analysis”.

---

## 2) The canonical review order for one day D (10 steps)

This order is designed to minimize rabbit holes and maximize cross‑tool synthesis.

1) **Pick the day (D)** and open the day portals:
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CONTROL_CENTER.md`
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__DAY_SYNTHESIS.md` (if it exists)

2) **Confirm provenance** (don’t rely on file timestamps):
   - `sharepacks/<D>/README.md`
   - `sharepacks/<D>/control_center/meta.json`

3) **Read Brain‑2 first** (cross‑state “what was in alert / what was playable”):
   - In `<D>__CONTROL_CENTER.md`, scan:
     - Profit Alerts: `HIT(decay)` vs `HIT<=7/<=14` and the merged play‑sets
     - BA / Due Doubles / VTRAC Repeat Watch highlights

4) **Read Brain‑1 day synthesis** (cross‑state environment classes):
   - Identify 2–4 environment “classes” for the day (e.g., convergence days vs noisy days).

5) **Choose 3 states deliberately** (avoid cherry‑picking):
   - 1 “good‑looking” case (clear convergence / interesting CC episode)
   - 1 “bad‑looking” case (tool misses / confusing environment)
   - 1 “weird” case (edge case: PR missing results line, etc.)

6) For each chosen state, open the **run report first** (don’t open raw outputs yet):
   - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
   - Read Parts A–3 (environment → tools → aux) before reading Part 4/5 synthesis.

7) Only if needed, drill into **sharepack evidence** via links in the run report:
   - Winners lens (Part A): `sharepacks/<D>/<STATE>/winners/<STATE>/...`
   - Tool evidence: `sharepacks/<D>/<STATE>/{stable,digit_reduction,vtrac,hot_zones}/...`
   - Aux evidence: `sharepacks/<D>/<STATE>/aux/...`

8) **Classify what you saw** as one of:
   - **Fix‑Now (pipeline correctness)**: missing artifacts, bad inputs, alignment failures
   - **Tool outcome**: tool ran correctly but didn’t isolate the winner (this is evidence)
   - **Hypothesis**: “this pattern class seems profitable / repeatable”

9) **Log learnings in the right place** (so context resets don’t eat them):
   - Fix‑Now / Fix‑Later workflow items: `docs/AAT9_KIT/FINAL VALIDATION/final docs/WORKFLOW_CHANGELOG.md`
   - Per‑day insights: append to the day synthesis (`<D>__DAY_SYNTHESIS.md`)
   - Per‑state insights: add to the relevant run report (`<D>__<STATE>.md`)

10) Stop for the day with a **single sentence thesis**:
   - “On D=<D>, the dominant pattern class was ___; CC’s merged play‑sets produced ___ hits within <=14, mostly via ___.”

---

## 3) Interpretation rules (prevents panic loops)

### 3.1 Pipeline vs tool outcome

- **Pipeline failure** means: the day is not trustworthy (inputs/artifacts wrong).
- **Tool miss** means: the day is trustworthy and the tool didn’t isolate the winner (valuable measurement).

If something “looks wrong”, first ask: “is this a missing artifact, or just a miss?”

### 3.2 Profit Alerts: always read merged view + window diagnostics

- `profit_alerts.csv` is the raw board (lots of rows can fire).
- `profit_alerts_eval.csv` adds episode grading (decay + <=7/<=14 diagnostics).
- `profit_alerts_eval_merged.csv` is the actionable view (deduped play‑sets; avoids double‑counting).

In analysis, start with merged view first.

### 3.3 Combined is a lens (but cross‑variant bounce still matters)

- Combined is not a “third draw”.
- Cross‑variant actualization (a signal “resolves” on the other period) is real; treat it as **diagnostic**, not as a reason to redefine outcomes.

### 3.4 Leading zeros and canonicalization

- Treat Pick‑3 literals as **3‑digit strings** (e.g., `033` is not `33`).
- Many artifacts use canonical form (sorted digits). Always map literal ↔ canonical when comparing.

---

## 4) Context reset / handoff kit (copy/paste)

If a Codex session resets mid‑analysis, do this *first*:

1) Open these SSOT docs:
- `briefings/CODEX_READ_FIRST_AAT9_WSL_2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Pattern_Progression_Primer.md` (concept primer; optional but helpful)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`

2) Then open the day portals:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CONTROL_CENTER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__DAY_SYNTHESIS.md`

3) Use this handoff message:

> We are analyzing results date D=`YYYY-MM-DD`. Do not rebuild tools or touch analyzers. Only read from `sharepacks/<D>/...` and the run reports under `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`. Follow the Analysis Navigator review order, then either (a) fill the next `<D>__<STATE>.md` run report, or (b) extend `<D>__DAY_SYNTHESIS.md`. Log fix‑later items to `docs/AAT9_KIT/FINAL VALIDATION/final docs/WORKFLOW_CHANGELOG.md`.
