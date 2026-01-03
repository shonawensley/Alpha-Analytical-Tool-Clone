# Corpus Synthesis — D=2025-06-21..2025-06-23 (3-day starter corpus)

Scope
- Days (D): `2025-06-21`, `2025-06-22`, `2025-06-23`
- History workbooks (H): `D-1` per day
- States per day: 14 tracked states
- Total run reports: 42 state reports (14 × 3)
- Outcomes: Midday + Evening (Combined is a lens only; used for cross-variant structure and tags)

Pointers
- Run report progress index: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
- Day syntheses:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__DAY_SYNTHESIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__DAY_SYNTHESIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__DAY_SYNTHESIS.md`

---

## Executive Summary (what this 3-day corpus already teaches)

- You now have a real “starter corpus” that contains:
  - strong positive controls (clean convergence days),
  - split-channel days (Midday and Evening behave differently), and
  - negative controls (dominant lane convergence that does not resolve to winners).
- This is exactly the mix you want before building any scoring/weights: it forces you to separate:
  - pipeline integrity (artifacts exist, alignment passes) vs
  - tool outcome (did it isolate the winner, or did it isolate something else convincingly?).

---

## Cross-day patterns to carry forward (hypotheses, not rules yet)

1) VTRAC as a frequent “structure narrator”
- Across the three days, VTRAC-family structure and VT-straight tagging show up repeatedly in state narratives as either:
  - the primary driver (index rank + structure tags), or
  - the cleanest “family hedge” when other tools are noisy.

2) Stable as confirmatory (often deep)
- Stable frequently “sees” winners (exact present) but does not always elevate them to top ranks.
- This keeps showing up as a repeatable posture: Stable alone is often not enough to justify broad spend without corroboration, but it is valuable confirmation inside a multi-tool stack.

3) Cross-variant carry is real and should be preserved in scoring
- Winners are often visible (tags/structure) in a different variant lens than the draw they hit.
- This supports the core AAT9 methodology: Combined-lens structure and cross-variant evidence must remain first-class in later aggregation, not treated as “noise.”

4) Negative controls are loud and necessary
- The corpus already contains clear “dominant lane miss” patterns: multiple tools converge strongly on a non-winner cluster.
- These days are not failures; they are the training examples that will keep you from overfitting to whatever is loudest in a single run.

---

## Data-quality / workflow flags (do not confuse with tool performance)

- `D=2025-06-22` has missing results for `PuertoRico4`, and a one-winner-day scenario for `SouthCarolina4`. These must be treated as N/A for grading.
- Some DR overlay/winner-mapping anomalies are logged in run reports (and are consolidated in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md` once generated).

---

## Recommended next step (highest ROI, lowest risk)

- Continue filling templates for the next corpus days only after you:
  1) keep adding day syntheses, and
  2) keep centralizing fix-later anomalies so they do not get lost.

This keeps you in “evidence-first” mode until the dataset is large enough to justify real scoring work.

