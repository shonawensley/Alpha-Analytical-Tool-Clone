# Codex Deep Analysis — Gold Days Corpus (D=2025‑12‑30..2026‑01‑04)

Purpose: a **Codex‑authored** deep analysis of the 6‑day “gold corpus expansion” so you can compare:
- the **structured Run Reports** (per‑state + Control Center),
- with an **independent synthesis** that highlights repeatable patterns and anti‑overfit guardrails,
- and suggests **superbrain/aggregator primitives** without changing any analyzers.

Scope (strict):
- Dates `D` (sharepack folder names): `2025-12-30`, `2025-12-31`, `2026-01-01`, `2026-01-02`, `2026-01-03`, `2026-01-04`
- States per day: 14 tracked state folders under `sharepacks/<D>/...`
- Outcomes: **Midday + Evening** (Combined is a *lens only*; it is used for cross‑variant structure, not graded as an outcome)
- Evidence sources (SSOT):
  - Frozen evidence: `sharepacks/<D>/...`
  - Filled analysis artifacts: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/...`
- No analyzer changes (Stable / Digit Reduction / VTRAC / Hot Zones). This is **analysis only**.

Primary contract doc for reading this corpus:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/gold_days_2025-12-30_to_2026-01-04/MANIFEST.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`

Optional concept lens (matches the “pattern progression” training philosophy, preserved for context resets):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Pattern_Progression_Primer.md`

---

## Quantitative Baselines (so we don’t “vibe” our way into overfitting)

### Corpus size + completeness

- Total outcomes in scope: **168** (6 days × 14 states × 2 outcomes)
- Missing winners: **5 / 168**
  - Puerto Rico missing both outcomes on:
    - D=2026‑01‑01: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__PuertoRico4.md`
    - D=2026‑01‑04: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__PuertoRico4.md`
  - South Carolina Midday missing on:
    - D=2026‑01‑04: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__SouthCarolina4.md`

Ground truth for “what winner was graded” per day:
- `sharepacks/<D>/control_center/meta.json`

### Environment verdict buckets (from run reports)

These are **normalized buckets** derived from the “Environment verdict” field captured in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`:

| Bucket | Count |
|---|---:|
| strong | 80 |
| support | 58 |
| weak/noisy | 26 |
| unknown (no winners) | 4 |

Env buckets by day (this is the single best “anti‑overfit” view in the whole corpus):

| D | strong | support | weak/noisy | unknown |
|---|---:|---:|---:|---:|
| 2025-12-30 | 14 | 10 | 4 | 0 |
| 2025-12-31 | 24 | 2 | 2 | 0 |
| 2026-01-01 | 18 | 8 | 0 | 2 |
| 2026-01-02 | 8 | 20 | 0 | 0 |
| 2026-01-03 | 16 | 12 | 0 | 0 |
| 2026-01-04 | 0 | 6 | 20 | 2 |

Interpretation:
- **2025‑12‑31 is a “positive control day”** (24/28 outcomes are tagged strong).
- **2026‑01‑04 is a “negative control day”** (20/28 outcomes are tagged weak/noisy, and it includes missing winners).
- That spread is exactly what you want before you start compressing/tuning: it forces the future superbrain to learn *posture shifts* instead of chasing one “always works” heuristic.

### Tool strength proxies (winner placement / rank fractions)

These come from per‑tool `summary.json` files inside sharepacks (not from manual eyeballing):

- Stable: `sharepacks/<D>/<STATE>/stable/<STATE>/summary.json` → `winners[].scores.winner_rank_fraction`
- Hot Zones: `sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.json` → `winners[].top_lanes.winner_rank_fraction`
- VTRAC: `sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.json` → `winner_index_placements[].rank_fraction`
- Digit Reduction: `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/summary.json` → `winners[].top.winner_present` (strict “top list” lens)

Coverage / “does the tool see the winner at all?” (only outcomes with an actual winner; n=163):

- Stable `scores.present`: **125 / 163 (76.7%)**
- Hot Zones `top_lanes.present`: **162 / 163 (99.4%)**
- VTRAC winner index placement present: **162 / 163 (99.4%)**
  - Missing case: `sharepacks/2025-12-30/Virginia4/vtrac/Virginia4/summary.json` has no placement row for winner `888` (Midday).
- Digit Reduction `top.winner_present` (strict top list): **8 / 163 (4.9%)**

Stable “exact” hits (as recorded by Stable’s winner spotlight metrics; n=163):
- Stable `metrics_hits.exact_boxed`: **105 / 163**
- Stable `metrics_hits.exact_straight`: **100 / 163**

Rank fraction quantiles (lower = better ranked; only computed when the tool reports `present=true` for that lens):

| Tool metric | p10 | median | p90 |
|---|---:|---:|---:|
| Stable winner rank fraction | 0.033 | 0.340 | 0.915 |
| Hot Zones winner rank fraction | 0.124 | 0.505 | 0.894 |
| VTRAC index rank fraction | 0.114 | 0.457 | 0.857 |

Practical takeaway:
- Stable remains your strongest single numeric discriminator for “how tight did the corpus get?” but it’s not “always top‑k”.
- Hot Zones is a near‑universal containment lens, but frequently mid‑rank → best used to shape coverage, not as a single caller.
- VTRAC index rank is often mid‑rank → best treated as a structure narrator + family hedge lens.
- DR strict top list rarely contains the winner → it’s better treated as an overlay/constraint lens than a standalone caller.

### Convergence frequency (how often multiple lenses are simultaneously “tight”)

Simple convergence proxy (per outcome, using rank‑fraction thresholds):
- Stable `winner_rank_fraction ≤ 10%` (stable present): **25 / 163**
- Hot Zones `winner_rank_fraction ≤ 10%` (HZ present): **14 / 163**
- VTRAC `rank_fraction ≤ 20%`: **31 / 163**

Pairwise / triple convergence counts:
- Stable & Hot Zones tight: **5 / 163**
- Stable & VTRAC tight: **9 / 163**
- Hot Zones & VTRAC tight: **4 / 163**
- **Stable & Hot Zones & VTRAC tight**: **4 / 163**

The 4 “triple convergence” examples (high‑value positive controls for superbrain logic):
- D=2025‑12‑31 NewYork4 Evening winner `116`
  - `sharepacks/2025-12-31/NewYork4/stable/NewYork4/summary.json`
  - `sharepacks/2025-12-31/NewYork4/hot_zones/NewYork4/summary.json`
  - `sharepacks/2025-12-31/NewYork4/vtrac/NewYork4/summary.json`
- D=2025‑12‑31 Virginia4 Evening winner `636`
  - `sharepacks/2025-12-31/Virginia4/stable/Virginia4/summary.json`
  - `sharepacks/2025-12-31/Virginia4/hot_zones/Virginia4/summary.json`
  - `sharepacks/2025-12-31/Virginia4/vtrac/Virginia4/summary.json`
- D=2026‑01‑02 PuertoRico4 Midday winner `144`
  - `sharepacks/2026-01-02/PuertoRico4/stable/PuertoRico4/summary.json`
  - `sharepacks/2026-01-02/PuertoRico4/hot_zones/PuertoRico4/summary.json`
  - `sharepacks/2026-01-02/PuertoRico4/vtrac/PuertoRico4/summary.json`
- D=2026‑01‑03 Pennsylvania4 Evening winner `909`
  - `sharepacks/2026-01-03/Pennsylvania4/stable/Pennsylvania4/summary.json`
  - `sharepacks/2026-01-03/Pennsylvania4/hot_zones/Pennsylvania4/summary.json`
  - `sharepacks/2026-01-03/Pennsylvania4/vtrac/Pennsylvania4/summary.json`

Use these as your “anchor examples” when you start formalizing the aggregator contract: they show what it looks like when independent lenses all compress at once.

---

## Control Center / Profit Alerts (Brain‑2) — baseline behavior in this 6‑day block

The Profit Alerts system is not a promise; it’s **instrumentation**:
- It surfaces candidate/overlay rows.
- It evaluates them as **episodes** with draw‑step windows (DecayDraws primary; <=7/<=14 diagnostics).
- It produces a deduped merged view (co‑firing collapse) so you don’t misread “row volume” as “bet volume”.

Evidence:
- Raw rows: `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- Merged sets: `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`
- Human scan: `sharepacks/<D>/control_center/profit_alerts_eval.md`

Important caveat (for interpreting Jan 2026): the last days have higher **CENSORED** counts because the evaluation window looks forward across results files; if future `data/results/*.txt` files are missing, the episode can’t be fully graded.

Profit alerts (raw) by day:

| D | rows | candidate | promoter | governor | HIT(decay) | HIT<=7 | HIT<=14 | HIT_ANY(decay) | HIT_ANY<=14 | CENSORED |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025-12-30 | 72 | 53 | 15 | 4 | 0 | 1 | 3 | 0 | 3 | 0 |
| 2025-12-31 | 69 | 53 | 14 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 2026-01-01 | 70 | 54 | 12 | 4 | 0 | 2 | 2 | 0 | 2 | 1 |
| 2026-01-02 | 64 | 46 | 16 | 2 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2026-01-03 | 66 | 51 | 11 | 4 | 1 | 1 | 1 | 1 | 1 | 15 |
| 2026-01-04 | 67 | 52 | 11 | 4 | 0 | 0 | 0 | 0 | 0 | 44 |

Profit alerts (merged play‑sets) by day:

| D | merged_sets | HIT(decay) | HIT<=7 | HIT<=14 | HIT_ANY(decay) | HIT_ANY<=14 | CENSORED |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2025-12-30 | 44 | 0 | 1 | 2 | 0 | 2 | 0 |
| 2025-12-31 | 48 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2026-01-01 | 49 | 0 | 1 | 1 | 0 | 1 | 1 |
| 2026-01-02 | 40 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2026-01-03 | 47 | 1 | 1 | 1 | 1 | 1 | 12 |
| 2026-01-04 | 46 | 0 | 0 | 0 | 0 | 0 | 37 |

Interpretation:
- This corpus is still too small (and too censored on the last day) to make “profitability” claims.
- What it *does* provide is a **correct measurement baseline** and a way to compare:
  - “tool‑driven candidate packs” (Brain‑1),
  - vs “cross‑state alert episodes” (Brain‑2),
  without semantic drift.

---

## Top 10 cross‑day insights (evidence‑linked; no tuning)

### 1) You already have the correct anti‑overfit posture baked in: day classes are real

The 6‑day block contains both:
- strong positive controls (D=2025‑12‑31), and
- strong negative controls (D=2026‑01‑04).

Evidence:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`

Superbrain implication:
- The aggregator must learn to **change posture** by environment (skip / tiny hedge / broad coverage) rather than “always take the loudest lane”.

### 2) Stable is often a containment lens, not just a “caller” — and this corpus has enough variation to prove it

Stable `scores.present` is ~77% across outcomes with winners, but rank fractions are widely distributed (median ~0.34; p90 ~0.92).

Evidence:
- Stable summaries under `sharepacks/<D>/<STATE>/stable/<STATE>/summary.json`

Superbrain implication:
- You’ll likely want to treat Stable as:
  - a **containment detector** (“winner is in the stable structure at all”), and
  - a **strength gauge** (rank_fraction / score deltas),
  not a binary “it worked / it failed”.

### 3) Hot Zones is the most consistent “winner containment” lens in the corpus

Hot Zones contains the winner in top lanes in 162/163 outcomes with winners.

Evidence:
- `sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.json`

Superbrain implication:
- Use Hot Zones as a **coverage shaper** and intersection partner (HZ lanes ∩ Stable survivors) rather than expecting it to isolate a single line.

### 4) VTRAC is strongest as a family hedge narrator (8‑lane), and it’s convergent when it matters most

Median VTRAC index rank fraction is ~0.46; it’s often mid‑ranked.
But when it converges tightly with Stable/HZ, those are rare, high‑value episodes.

Evidence:
- `sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.json`
- The “triple convergence” list above (4 examples).

Superbrain implication:
- Use VTRAC mostly to:
  - define small “family sets” (8‑lane; boxed vs straight considerations),
  - narrate structure across variants,
  - and gate “confidence posture” when it also aligns with Stable/HZ.

### 5) Digit Reduction is working as a constraint/overlay lens, not a strict top‑candidate caller

DR strict top‑candidate presence is only 8/163.
That’s not “DR is broken”; it’s “DR’s top list is not the right grading lens for its role”.

Evidence:
- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/summary.json`

Superbrain implication:
- Use DR to:
  - constrain digit pools / reductions,
  - narrate VT‑boxed pressure,
  - and intersect with other candidate universes,
  rather than expecting the winner in the strict top list.

### 6) Cross‑variant thinking is already being applied everywhere — that’s good and should be preserved

Every state outcome in this 6‑day block is tagged as having cross‑variant consideration (`cross_variant_mentioned=1` in the corpus summary).

Evidence:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`

Superbrain implication:
- Keep the SSOT rule: Midday/Evening are outcomes; Combined is a lens.
- Keep the analysis rule: Combined and cross‑variant reinforcement should influence **pack selection posture**, not redefine outcomes.

### 7) State‑level “difficulty” appears heterogeneous — treat that as training data, not a bug

Across 12 outcomes/state (6 days × 2):
- OntarioCanada4 has 4 weak/noisy outcomes (more than most).
- Pennsylvania4 and SouthCarolina4 also have 4 weak/noisy outcomes.
- NorthCarolina4 has 8 strong outcomes and 0 weak/noisy in this block.

Evidence:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv` (group by state)

Superbrain implication:
- This is a natural place for later “state priors” (not now): some states may demand more hedging, or show different cross‑variant behavior.

### 8) Profit Alerts are now correctly evaluable, and the next lever is corpus size (not semantics)

Over 6 days, merged play‑sets show:
- HIT(decay): 1
- HIT<=14: 4
- HIT_ANY<=14: 5
…with heavy censoring on the last day due to missing future results.

Evidence:
- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`

Superbrain implication:
- Do not retune alerts on 6 days.
- Use this as an instrumentation baseline, then add days (and results files) so time‑to‑hit distributions become meaningful.

### 9) Data-quality anomalies are minimal in this block, and the remaining ones are explicit (not silent)

Examples:
- Puerto Rico missing winners on certain days.
- South Carolina Midday missing on one day.
- VTRAC missing one placement row (Virginia4 Midday 888) — likely a tool-output corner case.

Evidence:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__PuertoRico4.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__SouthCarolina4.md`
- `sharepacks/2025-12-30/Virginia4/vtrac/Virginia4/summary.json`

Superbrain implication:
- These are “expected N/A” or explicit corner cases. They should not block corpus expansion.

### 10) The right “profitability” primitive is already present: episodes + windows + cost units (no wagering engine required)

You can stay rigorous without writing a betting system:
- For every candidate set, log: `set_size`, `window_steps`, `time_to_hit_steps`, and derive unitless “cost units”.
- Then later, plug in payout tables to compute EV.

Evidence anchors:
- Profit alerts evaluator outputs already include: `implied_set_size`, `decay_draws`, `time_to_hit_steps`.
  - `sharepacks/<D>/control_center/profit_alerts_eval.csv`

Superbrain implication:
- Build the aggregator around **episode evaluation** and **caps**, not per‑draw certainty.

---

## What I would do next (no new code required)

1) Keep expanding the corpus (more known‑good workbooks + results files), then freeze days.
2) Continue filling run reports (state + Control Center) as the primary analysis surface.
3) Re-run the corpus export and this analysis doc periodically to:
   - recompute baselines,
   - identify new environment classes,
   - and surface the most stable “superbrain primitives”.

If you want a single command-driven posture: treat “new days” as a data collection campaign, and treat “tool tuning” as a separate campaign that only begins after you have a materially larger sample size.

