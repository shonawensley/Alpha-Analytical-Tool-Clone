# Hot Zones — v0 Audit (Quantitative)

Purpose: quantify whether **Hot Zones** (as currently consumed in the *prediction layers* / “superbrain surfaces” like Candidate Universe + Play Cards) behaves like:

- a **primary caller** (its top picks hit at meaningful rates), or
- a **supporting corroborator / lane lens** (it often lands in the right VTRAC family, but not the exact straight).

This is an audit of **consumption**, not an analyzer tuning.

Non‑negotiables (v0 synthesis sprint):
- No analyzer edits (Stable/DR/VTRAC/HZ).
- Baseline conclusions use `--profile tool_only` (Profit Alerts quarantined).

---

## Inputs

Window:
- Date range: `2026-01-05` → `2026-01-09`
- States: 14 tracked
- Outcomes: Midday + Evening (Combined excluded as an outcome)

Selection‑layer source (pre‑results triads):
- Predictive Hot Zones triad list: `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<D>_hot_zones_winner_map.json`
  - Note: despite the filename, in predictive packs this is simply a ranked triad list (no real winner exists yet).

Evidence‑layer source (post‑results placement):
- Hot Zones summary: `sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.json`

Quant output:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__QUANT.csv`

---

## What “Hot Zones” means in this audit

### Candidate Universe ingestion (selection layer)

Current Candidate Universe pack:
- `method_id=hot_zones_top`
- Source: `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<D>_hot_zones_winner_map.json` (or fall back to `*_hot_zones_top_lanes.csv`)
- How it is built:
  - take top‑N triads by `score_mean` (default N=8)
  - play mode: `STRAIGHT`

Key implication:
- As currently consumed, Hot Zones is evaluated as a **straight sniping** signal, not a boxed-canonical signal.

### Evidence-level presence (tool output, not selection)

From `sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.json`:
- whether the winner is present in the full top-lanes table (rank fraction / score ratio)
- whether the winner appears in the **top20** “winner_map” triad list (`triad_present`)

---

## Results snapshot (v0 window)

### A) Evidence-level (how often winner is even in Hot Zones’ top20 triad list)

Across the same v0 opportunities (n=138; excludes blank winners):
- Winner in top20 “winner_map” triads: `13/138` (0.0942)
- Winner placement in `top_lanes` table:
  - median `best_rank`: `93` (out of `rows_total=210`)
  - median `winner_rank_fraction`: `0.4429`

Interpretation:
- Winners are usually present in the *full* Hot Zones top-lanes table, but rarely in the **very top** triad list we consume as “what to play”.

### B) Selection-level (what Hot Zones contributes as a top‑caller vs a lane lens)

See: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__QUANT.csv`

| top_n | opps | straight_hit | straight_hit_rate | canonical_hit_rate (BOX‑equiv) | index_hit_rate (non-double opps) | avg_cost_straight | avg_cost_box |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 138 | 1 | 0.0072 | 0.0290 | 0.1691 | 8.0 | 36.899 |
| 12 | 138 | 2 | 0.0145 | 0.0580 | 0.2500 | 12.0 | 55.986 |
| 20 | 138 | 2 | 0.0145 | 0.0942 | 0.3824 | 20.0 | 96.072 |

Notes:
- `canonical_hit_rate (BOX‑equiv)` is a counterfactual: “if we treated top triads as boxed canonicals”.
- `index_hit_rate` excludes doubles/triples (no `vtrac_index`).

Interpretation:
- As a strict straight caller, Hot Zones is very weak at small `top_n`.
- As `top_n` grows, Hot Zones becomes a stronger **index/lane selector**, but that is not the same as a boxed hit.

---

## v0 conclusion (Hot Zones)

1) **Hot Zones is not a reliable straight caller at low top_n** in the v0 window.

2) Hot Zones is useful as:
- a **lane/index lens** (moderate `vtrac_index_hit`), and
- a low-cost contributor to **cross-pack convergence** (votes), not a standalone “play this” list.

Next:
- Case audit: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__CASES.md`
- Feature decisions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__FEATURE_DECISIONS.md`

