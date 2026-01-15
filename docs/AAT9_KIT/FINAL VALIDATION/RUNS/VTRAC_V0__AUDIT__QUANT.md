# VTRAC Enhanced — v0 Audit (Quantitative)

Purpose: quantify whether **VTRAC Enhanced** (as currently consumed in the *prediction layers* / “superbrain surfaces” like Candidate Universe + Play Cards) behaves like:

- a **primary caller** (its top straights hit at meaningful rates), or
- a **supporting corroborator / lane lens** (it often lands in the right VTRAC index family, but not the exact canonical/straight).

This is an audit of **consumption**, not analyzer tuning.

Non‑negotiables (v0 synthesis sprint):
- No analyzer edits (Stable/DR/VTRAC/HZ).
- Baseline conclusions use `--profile tool_only` (Profit Alerts quarantined).

---

## Inputs

Window:
- Date range: `2026-01-05` → `2026-01-09`
- States: 14 tracked
- Outcomes: Midday + Evening (Combined excluded as an outcome)

Selection‑layer source (pre‑results bundle):
- Enhanced JSON: `sharepacks/_predictive/<D>/<STATE>/vtrac/<STATE>/<STATE>_vtrac_enhanced_*.json`

Evidence‑layer source (post‑results placement):
- VTRAC summary: `sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.json` (`winner_index_placements`)

Quant output:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__QUANT.csv`

---

## What “VTRAC Enhanced” means in this audit

### Candidate Universe ingestion (selection layer)

Current Candidate Universe pack:
- `method_id=vtrac_enhanced_top`
- Source: `straights_ranked` from the enhanced JSON bundle
- How it is built:
  - take top‑N ranked straights (default N=8), dedupe, sort
  - play mode: `STRAIGHT`

Key implication:
- As currently consumed, VTRAC Enhanced is evaluated as **straight sniping**.

### Evidence-level placement (index ranking, not straight picks)

From `sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.json`:
- `winner_index_placements` provides the winner’s VTRAC index rank among 35 indices (rank fraction + score ratio).

This captures “was VTRAC right about the rail?” even when the top‑N straights miss.

---

## Results snapshot (v0 window)

### A) Evidence-level (winner index placement)

Across non-double opportunities (n=136):
- Winner index ranked in top‑3: `12/136` (0.0882)
- Winner index ranked in top‑10: `35/136` (0.2574)
- Median winner index rank fraction: `0.5143`

Interpretation:
- In v0, VTRAC Enhanced is not consistently ranking the winning index near the top, but it does land in the correct index neighborhood sometimes.

### B) Selection-level (top-N straights)

See: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__QUANT.csv`

| top_n | opps | straight_hit | straight_hit_rate | canonical_hit_rate (BOX‑equiv) | index_hit_rate (non-double opps) | avg_cost_straight | avg_cost_box |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 138 | 1 | 0.0072 | 0.0145 | 0.1176 | 8.0 | 27.304 |
| 12 | 138 | 1 | 0.0072 | 0.0290 | 0.1618 | 12.0 | 39.043 |
| 20 | 138 | 2 | 0.0145 | 0.0507 | 0.2059 | 20.0 | 62.870 |

Notes:
- `canonical_hit_rate (BOX‑equiv)` is counterfactual: “if we treated the top straights’ canonicals as boxed”.
- `index_hit_rate` excludes doubles/triples (no `vtrac_index`).

Interpretation:
- As a strict straight caller, VTRAC Enhanced is weak at low `top_n`.
- As `top_n` grows, it becomes a more useful index lens, but costs rise (especially if boxed).

---

## v0 conclusion (VTRAC Enhanced)

1) **VTRAC Enhanced top‑N straights are not a reliable direct caller** in the v0 window.

2) The primary measurable value is:
- “index correctness” (lane lens), and
- contributions to cross-pack convergence (votes),
not raw straight hit rate.

Next:
- Case audit: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__CASES.md`
- Feature decisions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__FEATURE_DECISIONS.md`

