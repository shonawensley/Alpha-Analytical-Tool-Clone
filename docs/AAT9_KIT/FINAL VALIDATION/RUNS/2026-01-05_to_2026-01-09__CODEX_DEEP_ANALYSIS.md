# Codex Deep Analysis — Jan Window (D=2026‑01‑05..2026‑01‑09)

Purpose: a **Codex‑authored** deep analysis of the 5‑day Jan window so you can compare:
- the **filled Master Validation run reports** (per‑state + per‑day),
- the cross‑day **range pack** rollups/lenses,
- and the **predictive grading** (Candidate Universe / Play Cards),
without drifting into overfitting or prematurely changing analyzers.

Scope (strict):
- Dates `D` (sharepack folder names): `2026-01-05` → `2026-01-09`
- States per day: 14 tracked states under `sharepacks/<D>/...`
- Outcomes: **Midday + Evening** (Combined is a *lens only*)
- Evidence sources (SSOT):
  - Frozen evidence: `sharepacks/<D>/...`
  - Filled analysis artifacts: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/...`
- No analyzer changes (Stable / Digit Reduction / VTRAC / Hot Zones). This is **analysis only**.

Primary reading portals (in order):
- RUNS portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- Analysis navigator: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
- This range’s synthesis: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_SYNTHESIS.md`

Range pack (generated rollups/lenses):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_DASHBOARD.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__PROFIT_ALERTS_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONTROL_CENTER_ROLLUP.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CROSS_VARIANT_REPORT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__DR_LENS_REPORT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__MIRROR_DOUBLE_FREQUENCY.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__RESULTS_HORIZON.md`

Predictive grading (pre‑results artifacts graded post‑results):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup.md`

---

## Quantitative baselines (so we don’t “vibe” our way into tuning)

### Corpus size + missing winners

- Expected outcomes: **140** (5 days × 14 states × 2 outcomes)
- Outcomes with winners: **138 / 140**
- Missing winners: **2 / 140**, both on `D=2026-01-06` for `PuertoRico4` (Midday + Evening)
  - Run report rows still exist (evidence is captured), but grading is N/A for those outcomes.

### Environment buckets (from run reports)

These buckets are derived from `env_verdict` in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv` for this window:

| D | strong | support | weak/noisy | unknown | total |
|---|---:|---:|---:|---:|---:|
| 2026-01-05 | 8 | 18 | 2 | 0 | 28 |
| 2026-01-06 | 12 | 10 | 4 | 2 | 28 |
| 2026-01-07 | 10 | 18 | 0 | 0 | 28 |
| 2026-01-08 | 12 | 12 | 4 | 0 | 28 |
| 2026-01-09 | 16 | 12 | 0 | 0 | 28 |

Interpretation:
- This window includes both **clean “strong” days** and **weak/noisy days** (good for anti‑overfit posture learning).
- `2026-01-09` is a strong-heavy day (16/28 tagged strong).

### Tool presence / containment (not performance claims)

From the dashboard:
- Stable families present: **134/138 (97.1%)**
- Hot Zones top lanes present: **135/138 (97.8%)**
- VTRAC winner index in top10: **35/138 (25.4%)**
- DR “strict top candidates contain winner”: **5/138 (3.6%)**
- Winner VTRAC signature has repeat (mirror/double-space): **74/138 (53.6%)**

Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_DASHBOARD.md`

### Cross‑variant bounce is real in this window

Stable “where did the best evidence come from?” distribution:
- same period: **52/138 (37.7%)**
- other period (cross‑variant bounce): **50/138 (36.2%)**
- Combined lens: **32/138 (23.2%)**

Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CROSS_VARIANT_REPORT.md`

This is why “Combined is a lens” is not optional: it’s frequently the best *evidence section*, even when the graded outcome is Midday/Evening.

### Results horizon (why “CENSORED” increases near the end)

This window has results files only through `D=2026-01-09`, so forward-looking evaluators (Profit Alerts) will show more **CENSORED** episodes on later `D`s.

Evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__RESULTS_HORIZON.md`

---

## Predictive layer baselines (Candidate Universe + Play Cards)

This 5‑day window already has:
- a gradeable pre‑results playset per state/day (`candidate_universe.json` in predictive sharepacks),
- and budgeted selection cuts (“play cards”),
graded later into RUNS.

### Candidate Universe rollup (method_id × play_mode)

High-level (do not over-read; sample is 5 days):
- `union` has the highest hit rates (expected: it’s the broad union view, not a budgeted selection).
- Packs that are designed as **low-cost closures** (e.g., due doubles + mirror-double expansions) show non-zero box hits, but at low base rates.

Evidence:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup.md`

### Play Cards (budgeted “what would I actually play?” experiments)

Baseline for this window (rows are outcomes; budgets are small controlled experiments):
- Midday: best hit_any is **0.0580** at B36 (4 hits / 69 Midday outcomes).
- Evening: best hit_any is **0.0500** at B24/B36 across strategies (3 hits / 60 Evening outcomes).

Evidence:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup.md`

Interpretation:
- This is the correct place to run “tight budget” competitions: it’s deterministic, gradeable, and doesn’t overwrite any evidence.
- The numbers are not “good/bad” yet; they are a **measurement baseline** for future iteration (more days needed).

---

## What looks most “study-worthy” (not rules)

### 1) Convergence cases (4-lens alignment)

These are outcomes where all 4 convergence lenses fired:
- Stable top 10% rank fraction
- Hot Zones top 20% rank fraction
- VTRAC winner index in top10
- DR best_area<=3

Evidence (top cases table):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CONVERGENCE_CASES.md`

Recommended “read these first” study targets:
- `2026-01-05 NewYork4 Midday 080`
- `2026-01-07 Florida4 Midday 434`
- `2026-01-07 Florida4 Evening 963`
- `2026-01-09 NewJersey4 Evening 028`
- `2026-01-09 Pennsylvania4 Evening 014`

### 2) Mirror/double-space prevalence is high

In this window:
- literal doubles are **29.7%** of winners,
- but mirror-repeat VTRAC signatures occur in **53.6%** of winners.

Evidence:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__MIRROR_DOUBLE_FREQUENCY.md`

Superbrain implication (still Fix‑Later): “mirror-double-ish” is a **measurable primitive**, and it’s showing up frequently enough to justify deeper auditing in larger corpora.

---

## What I would do next (keeps progress linear, avoids circles)

### 1) Keep collecting paired days (BEFORE + AFTER)

For each new history workbook `H` you provide:
- Build predictive BEFORE snapshot: `sharepacks/_predictive/<D>/...` (`D=H+1`)
- Generate Candidate Universe + Play Cards (gradeable pre‑results artifacts)
- Once results exist, build AFTER snapshot: `sharepacks/<D>/...` + fill RUNS
- Grade (writes to RUNS only), then regenerate range pack rollups

### 2) Use range pack + convergence cases to drive “synthesis days”

Instead of reading 70 state reports in order:
- pick 3–5 convergence cases from `__CONVERGENCE_CASES.md`,
- read their state run reports + the day synthesis,
- then write 1–2 new primitives into `docs/AAT9_KIT/FINAL VALIDATION/final docs/SUPERBRAIN_PRIMITIVES.md`.

### 3) Do not tune analyzers from this window

This is still a small sample (and Profit Alerts episodes are horizon‑limited near the end date).
Treat this doc as:
- baseline measurement,
- study-case selection,
- and a guardrail against “moving goalposts”.

