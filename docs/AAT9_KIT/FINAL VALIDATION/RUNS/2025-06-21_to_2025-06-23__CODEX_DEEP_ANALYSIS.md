# Codex Deep Analysis — Gold Days Corpus (D=2025‑06‑21..2025‑06‑23)

Purpose: a **Codex‑authored** deep analysis of the same “gold days” package you are running through ChatGPT Pro, so you can compare outputs from two independent reviewers.

Scope (strict):
- Dates `D`: 2025‑06‑21, 2025‑06‑22, 2025‑06‑23 (sharepack folder names).
- States: the 14 tracked states in each sharepack day.
- Evidence sources (SSOT):
  - Frozen evidence: `sharepacks/<D>/...`
  - Filled analysis artifacts: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/...`
- No analyzer changes (Stable / DR / VTRAC / Hot Zones). This is **analysis only**.

Primary contract doc for how to read this corpus:
- `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/gold_days_2025-06-21_to_2025-06-23/MANIFEST.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`

Optional concept lens (matches your training methodology, preserved for context resets):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Pattern_Progression_Primer.md`

---

## Quantitative Baselines (so we don’t “vibe” our way into overfitting)

### Corpus size + completeness

- Total outcomes in scope: **84** (3 days × 14 states × 2 outcomes: Midday + Evening)
- Missing winners in results files: **3 / 84**
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__PuertoRico4.md` (PR missing Midday + Evening line in `data/results/2025-06-22.txt`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__SouthCarolina4.md` (Midday blank in `data/results/2025-06-22.txt`)

Primary corpus surface (already extracted from the run reports):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`

### Environment verdict buckets (from run reports)

These are **normalized buckets** derived from the free‑text “Environment verdict” in `corpus_summary.csv`:

| Bucket | Count |
|---|---:|
| support | 32 |
| strong | 8 |
| mixed | 10 |
| split | 14 |
| weak/noisy | 14 |
| pass | 4 |
| unknown | 2 |

Interpretation:
- `D=2025‑06‑21` contains nearly all the “strong” cases (good positive controls).
- `D=2025‑06‑22` contains most “split” and “pass/tiny hedge” cases (good negative controls and anti‑overfitting training).

### Tool strength proxies (winner placement / rank fractions)

All of the following are extracted from per‑tool `summary.json` files inside sharepacks (not from memory or manual reading):
- Stable: `sharepacks/<D>/<STATE>/stable/<STATE>/summary.json` → `winners[].scores.winner_rank_fraction`
- Hot Zones: `sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.json` → `winners[].top_lanes.winner_rank_fraction`
- VTRAC: `sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.json` → `winner_index_placements[].rank_fraction`
- Digit Reduction: `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/summary.json` → `winners[].top.winner_present` (very strict “top list” lens)

Coverage / “does the tool see the winner at all?”
- Stable `scores.present`: **63 / 81 (77.8%)**
- Hot Zones `top_lanes.present`: **80 / 81 (98.8%)**
- DR `top.winner_present` (strict top list): **2 / 82 (2.4%)** (DR is better treated as a constraint/overlay layer than a direct top‑candidate caller in this corpus)

Rank fraction quantiles (lower is “higher ranked”):

| Tool metric | p10 | median | p90 |
|---|---:|---:|---:|
| Stable winner rank fraction | 0.0197 | 0.2640 | 0.8964 |
| Hot Zones winner rank fraction | 0.1100 | 0.5121 | 0.8290 |
| VTRAC index rank fraction | 0.1143 | 0.4286 | 0.8857 |

Practical takeaway:
- Stable’s winner rank fraction is the strongest single numeric discriminator between “strong” and “weak/noisy” days in this 3‑day corpus.
- Hot Zones nearly always “contains” the winner somewhere, but often mid‑ranked → useful for **lane priors / coverage**, not a standalone caller.
- VTRAC index placement often sits mid‑ranked → valuable as a **structure narrator** and as a “family hedge lens”, not as “always take top index”.

### Control Center / Profit Alerts baseline (Brain‑2, windowed episodes)

Per day totals (from `sharepacks/<D>/control_center/profit_alerts_eval.csv` + `profit_alerts_eval_merged.csv`):

| D | Rows | Candidate | Promoter | Governor | HIT(decay) rows | HIT<=14 rows | HIT_ANY<=14 rows | Merged sets | Merged HIT(decay) | Merged HIT<=14 | Merged HIT_ANY<=14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2025‑06‑21 | 84 | 61 | 19 | 4 | 3 | 5 | 6 | 52 | 2 | 3 | 4 |
| 2025‑06‑22 | 85 | 61 | 15 | 9 | 0 | 1 | 2 | 51 | 0 | 0 | 0 |
| 2025‑06‑23 | 88 | 60 | 21 | 7 | 0 | 1 | 3 | 54 | 0 | 1 | 2 |

Important interpretation rules (prevents “0 hits” panic loops):
- **HIT(decay)** is the primary measurement (row’s own `DecayDraws` window).
- `<=7` / `<=14` are diagnostics (“did it happen within a longer horizon?”), not a reason to retune on 3 days.
- The **merged set view** is the actionable view (co‑firing collapse; don’t count raw rows as “bets”):
  - `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`

---

## Deliverable 1 — Top 10 cross‑day insights (with evidence anchors)

Each insight includes:
1) What it is,
2) Evidence anchors (files you can open),
3) What it implies for the future “superbrain” (without tuning yet).

### 1) Stable is the best early “environment strength” discriminator in this corpus

Observation:
- Median Stable winner rank fraction differs sharply between buckets:
  - `strong` median ≈ **0.055**
  - `weak/noisy` median ≈ **0.889**

Evidence anchors:
- Bucket source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`
- Stable metric source: `sharepacks/<D>/<STATE>/stable/<STATE>/summary.json`
- Concrete positive controls:
  - `sharepacks/2025-06-21/Connecticut4/stable/Connecticut4/summary.json`
  - `sharepacks/2025-06-22/NewJersey4/stable/NewJersey4/summary.json`

Implication for the superbrain:
- Treat Stable’s **rank fraction / score‑to‑top ratio** as an “environment confidence scalar” (not as a standalone caller).
- Use it to control spend tiering and to decide when other lenses (HZ/VTRAC/Aux) get to “matter”.

### 2) True multi‑tool convergence exists, but it is rare — and that rarity is valuable

Observation:
- Only **2 / 81** outcomes show a “triple convergence” proxy simultaneously:
  - Stable rank fraction ≤ 10%
  - Hot Zones rank fraction ≤ 10%
  - VTRAC index rank fraction ≤ 20%

Evidence anchors (the two cases):
- `sharepacks/2025-06-21/Connecticut4/stable/Connecticut4/summary.json`
- `sharepacks/2025-06-21/Connecticut4/hot_zones/Connecticut4/summary.json`
- `sharepacks/2025-06-21/Connecticut4/vtrac/Connecticut4/summary.json`
- `sharepacks/2025-06-22/NewJersey4/stable/NewJersey4/summary.json`
- `sharepacks/2025-06-22/NewJersey4/hot_zones/NewJersey4/summary.json`
- `sharepacks/2025-06-22/NewJersey4/vtrac/NewJersey4/summary.json`

Implication:
- These are your “positive control” episodes for future aggregation design:
  - When they occur, the candidate universe can be extremely small without pretending certainty.
  - When they do **not** occur (most of the time), the superbrain needs a different posture (cheap probes, skip, or broader coverage with caps).

### 3) Hot Zones is a near‑universal “winner containment” lens, but not a rank‑tight caller

Observation:
- Hot Zones contains the winner in top lanes **80 / 81 (98.8%)**.
- But the median rank fraction is ~0.51 → “winner is in there” is common; “winner is near the top” is less common.

Evidence:
- Metric source: `sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.json`
- Example:
  - `sharepacks/2025-06-21/Connecticut4/hot_zones/Connecticut4/summary.json`

Implication:
- Hot Zones should likely be used as:
  - a lane prior / “coverage shaper”, and
  - an intersection partner (e.g., HZ top lanes ∩ Stable survivor clusters),
  rather than “take the #1 lane”.

### 4) VTRAC is a structure narrator; “top index” is not consistently reliable in 3 days

Observation:
- Median VTRAC winner index rank fraction is ~0.43 (winner’s index is often mid‑rank).

Evidence:
- `sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.json` → `winner_index_placements`
- Example:
  - `sharepacks/2025-06-21/Delaware4/vtrac/Delaware4/summary.json`

Implication:
- Treat VTRAC primarily as:
  - a family hedge mechanism (8‑straights lane membership), and
  - a cross‑tool “alignment surface” (does Stable/HZ point into the same lane?),
  rather than a “winner is always in top‑k indices”.

### 5) Digit Reduction’s strict “top candidates” lens rarely contains the winner — so don’t grade DR that way

Observation:
- DR `top.winner_present` is only **2 / 82 (2.4%)** in this corpus.

Evidence:
- DR summary source: `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/summary.json`
- The two cases:
  - `sharepacks/2025-06-21/Connecticut4/digit_reduction/Connecticut4/summary.json` (Midday)
  - `sharepacks/2025-06-22/Florida4/digit_reduction/Florida4/summary.json` (Midday)

Implication:
- DR should be treated as:
  - a digit/value constraint layer,
  - a “boxed vs VT‑boxed pressure” narrator,
  - and an overlay to reduce candidate space,
  not as a strict “top list must contain winner” caller.

### 6) Split days are frequent — the system must support different postures Midday vs Evening

Observation:
- `split` bucket appears **14** times in 84 outcomes (and is concentrated on 2025‑06‑22/23).

Evidence:
- Split examples:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Michigan4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__NewJersey4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Connecticut4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Delaware4.md`

Implication:
- “One state, one verdict” is often too coarse.
- A practical superbrain needs:
  - per‑period decisions (Midday vs Evening),
  - plus a Combined lens to detect cross‑variant structure (but Combined is not an outcome).

### 7) “Stable exact present but low rank” and “dominant‑lane miss” are the two most important negative controls

Observation:
- The corpus repeatedly logs:
  - exact presence without top placement, and
  - strong dominance on a non‑winner lane (“loud miss”).

Evidence anchors:
- Fix‑later rollup: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
- Representative examples:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Delaware4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__NewJersey4.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Connecticut4.md`

Implication:
- These are exactly the examples that prevent the superbrain from “chasing loudness”.
- The aggregator needs explicit “dominant‑lane miss” memory tags (log‑first; no tuning yet).

### 8) Profit Alerts are now a real measurement harness (and should be treated as instrumentation, not a promise)

Observation:
- In merged view across 3 days:
  - 157 merged play‑sets
  - 2 HIT(decay)
  - 6 HIT_ANY<=14 (diagnostic)

Evidence:
- `sharepacks/<D>/control_center/profit_alerts_eval.md`
- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`
- Daily CC run reports:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__CONTROL_CENTER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__CONTROL_CENTER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__CONTROL_CENTER.md`

Implication:
- This is not “wasted time” — it’s the minimal instrumentation you need before expanding corpus.
- The correct posture now is: **add more days**, re‑evaluate, then tune decays/caps with evidence.

### 9) Cross‑variant “bounce” is a real phenomenon — keep it as a diagnostic lens, not a redefinition of outcomes

Observation:
- Outcomes are Midday/Evening only, but cross‑variant actualization matters.
- Profit Alerts explicitly track this with `hit_any_*` columns.

Evidence:
- Charter semantics: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- Evaluator outputs: `sharepacks/<D>/control_center/profit_alerts_eval.csv`

Implication:
- Superbrain design should preserve two parallel lenses:
  - variant‑faithful (“does Midday signal resolve on Midday?”), and
  - cross‑variant (“did it resolve at all within the window?”).

### 10) The corpus already contains enough structure to begin defining a “candidate universe ladder”

Observation:
- Run reports consistently converge on a practical ladder:
  1) Environment/winners lens,
  2) Tool evidence (Stable/HZ/VTRAC),
  3) Aux compounding,
  4) Pack decision,
  5) Fix‑later + synthesis.

Evidence:
- Workflow order: `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`
- Template ordering embodied in every run report under: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`

Implication:
- The “superbrain” is not blocked on new features right now; it’s blocked on:
  - accumulating more day corpora,
  - and synthesizing repeatable rules from the run reports.

---

## Deliverable 2 — Environment taxonomy (4–8 classes you can reuse)

These classes are intended to be:
- descriptive (what you saw),
- auditable (you can point to run reports),
- and stable enough to use for later scoring experiments.

### Class A — Strong convergence (positive controls)
Hallmarks:
- Stable winner rank fraction near the top (≤10%)
- At least one corroborating lens (HZ top lanes, VTRAC top index, Aux repeat/doubles pressure)

Examples:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Ohio4.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Delaware4.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__NewJersey4.md` (Evening)

### Class B — Supportive but noisy (coverage needed)
Hallmarks:
- Some corroboration exists, but multiple competing lanes remain.
- Pack decisions tend to be “playable but cautious”.

Examples:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Connecticut4.md` (Evening)
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__Pennsylvania4.md`

### Class C — Split day (Midday and Evening require different postures)
Hallmarks:
- One outcome is supported, the other behaves like a surprise/low confidence case.

Examples:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Michigan4.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__Connecticut4.md`

### Class D — Dominant‑lane miss (negative controls; don’t chase loudness)
Hallmarks:
- Multiple tools converge strongly, but the winner lands elsewhere.

Examples:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__Connecticut4.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__NewJersey4.md`

### Class E — Weak/noisy / low confidence (pass or tiny hedge)
Hallmarks:
- No clean convergence; high risk of overfitting if forced into a “play”.

Examples:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__OntarioCanada4.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__SouthCarolina4.md`

### Class F — “Strong persistence pressure, but winner not literal”
Hallmarks:
- The environment collapses strongly, but the literal winner sits adjacent / structurally related rather than identical.

Examples:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__OntarioCanada4.md`

---

## Deliverable 3 — Tool performance summary (not tuning; outcome categories only)

### Stable
Strength:
- Best single numeric discriminator for “environment strength”.
Weakness:
- Frequently sees the winner but not always at top ranks → needs corroboration and/or spend tiering.

Where to audit:
- `sharepacks/<D>/<STATE>/stable/<STATE>/summary.json`

### Hot Zones
Strength:
- Almost always “contains” the winner somewhere (good coverage lens).
Weakness:
- Often mid‑rank; if treated as “take top lane”, will overfit.

Where to audit:
- `sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.json`

### VTRAC
Strength:
- Provides a consistent “family lane” structure; good for family hedging and cross‑tool alignment.
Weakness:
- Winner index is frequently mid‑rank in top indices; top‑index‑only play is not supported by this 3‑day baseline.

Where to audit:
- `sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.json`

### Digit Reduction
Strength:
- Useful overlay/constraint narrative (boxed vs VT‑boxed pressure, digit/value pressure).
Weakness:
- Strict “top candidates contains winner” is not the right grading lens (2/82 in this corpus).

Where to audit:
- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/summary.json`

---

## Deliverable 4 — Control Center / Profit Alerts evaluation (Brain‑2)

Primary artifacts (per day):
- Board: `sharepacks/<D>/control_center/profit_alerts.csv`
- Row evaluation: `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- Merged play‑sets: `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv`
- Narrative portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CONTROL_CENTER.md`

Key takeaways from the gold‑day baseline:
- The harness is functioning (deterministic, windowed, set‑based).
- Short‑window hits are currently rare; that is **information**, not a bug.
- The merged set view is the only sane way to interpret “how many plays”, because raw row counts include promoters and co‑firing.

Next best measurement step (no new features):
- Add more “known‑good” days to expand corpus and observe how HIT<=14 behaves by alert type and set size.

---

## Deliverable 5 — Candidate set + coverage implications (evaluation framing only)

From the corpus summary pack decisions:
- The dominant posture across 84 outcomes is **cheap boxed coverage** (canonical boxes), with relatively few explicit “pass” cases (4 outcomes).
- This is rational at the current stage: you are still building the evidence base for what deserves tighter sets.

A safe “candidate universe ladder” to keep using while expanding corpus:
1) Default: small canonical boxes where at least **2 independent lenses** support the same candidate cluster.
2) Escalate to VTRAC lane sets only when:
   - Stable rank fraction is strong (top‑tier), and
   - either HZ or VTRAC corroborates the same lane/cluster.
3) Treat DR as a constraint (digit/value pressure), not as a primary selector.

Evidence surface for these decisions:
- Pack decisions already written in the run reports: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
- Cross‑day summary: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`

---

## Deliverable 6 — Fix‑Now vs Fix‑Later (so we don’t regress into dev loops)

### Fix‑Now (pipeline integrity / contract violations)

None observed that invalidate the gold‑day corpus as a whole.

Known “expected N/A” conditions that must stay explicitly labeled (not treated as corruption):
- Puerto Rico missing results on 2025‑06‑22: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__PuertoRico4.md`
- South Carolina one‑winner day on 2025‑06‑22: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__SouthCarolina4.md`

### Fix‑Later (tuning hypotheses / evaluation improvements)

Use the consolidated index:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`

Cross‑day recurring themes worth prioritizing later (after corpus expansion):
- “Dominant‑lane miss” classification and gating
- “Stable exact present but low rank” confidence tiering
- When Combined‑lens dominance should override weak draw‑specific ladder evidence

---

## Suggested next steps (analysis‑first; no new features required)

If you want the fastest path toward the “superbrain”:

1) Expand corpus (add more days) **before** tuning:
   - More gold‑day sharepacks → repeat this analysis pass → only then adjust gates.
2) Use the environment taxonomy classes to avoid cherry‑picking:
   - Always include positive controls + negative controls in any tuning discussion.
3) Promote only “repeatable across days/states” hypotheses from FIX_LATER into Control Center or aggregator work.

