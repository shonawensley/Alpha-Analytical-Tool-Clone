# Aux — v0 Audit (Quantitative)

Purpose: quantify whether **Aux** (as currently *consumed in selection layers* like Candidate Universe / Play Cards) behaves like:

- a **primary caller** (direct hits at meaningful rates), or
- a **supporting corroborator / lane lens** (often lands in the right VTRAC family or canonical, but not as a precise straight).

This is an audit of **consumption**, not a change to Aux or any analyzers.

Non‑negotiables (v0 synthesis sprint):
- No analyzer edits (Stable/DR/VTRAC/HZ).
- Baseline conclusions use `--profile tool_only` (Profit Alerts quarantined).

---

## Inputs

Window:
- Date range: `2026-01-05` → `2026-01-09`
- States: 14 tracked
- Outcomes: Midday + Evening (Combined excluded as an outcome)
- Measured opportunities (non‑blank winners): **138**

Quant outputs:
- Candidate Universe method-level summary (tool_only): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__QUANT.csv`
- Raw Aux signal rates (top‑K overlaps): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__SIGNALS__QUANT.csv`

---

## What “Aux” means in this audit

### A) Candidate Universe ingestion (selection layer)

These are the **Aux-derived / Aux-seeded** method families currently present in the tool-only Candidate Universe:

- `method_id=aux_positional` (from Aux positional shortlist; consumed as `STRAIGHT`)
- `method_id=aux_vtrac_index_overdue` (from Aux VTRAC overdue overlay; consumed as `STRAIGHT` “index closure” canonicals)
- `method_id=mirror_pair_closure` (derived from Aux aggregated digits; consumed as `BOX`)
- Control Center “Aux-derived” board packs:
  - `method_id=due_doubles` (grouped by VTRAC double families; consumed as `BOX`)
  - `method_id=due_doubles_mirror_single` / `method_id=due_doubles_mirror_double` (bounded mirror-double expansions; consumed as `BOX`)

Important interpretation:
- `hit_any` is **as-consumed** (e.g., `STRAIGHT` packs only count literal hits).
- `canon_hit` is the **BOX‑equivalent** hit rate (“if we boxed the canonicals surfaced by this method”), which is how the grade tool’s `union` row behaves (best‑case across all packs).

### B) Raw Aux signals (environment evidence)

Aux also emits rich evidence that is **not necessarily ingested** as predictive packs yet:
- pairs (repeat + non-repeat), sums, blackapple candidates, etc.

These are quantified as **overlap rates** against winners (not “predictions”).

---

## Results snapshot (tool_only, 2026‑01‑05..09)

From `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__QUANT.csv`:

| method_id | opps | hit_any | hit_any_rate | canon_hit_rate | index_hit_rate |
|---|---:|---:|---:|---:|---:|
| aux_vtrac_index_overdue | 138 | 9 | 0.0652 | 0.0652 | 0.0652 |
| mirror_pair_closure | 138 | 5 | 0.0362 | 0.0362 | 0.1159 |
| due_doubles | 138 | 2 | 0.0145 | 0.0145 | 0.0942 |
| due_doubles_mirror_single | 138 | 3 | 0.0217 | 0.0217 | 0.0290 |
| due_doubles_mirror_double | 138 | 1 | 0.0072 | 0.0072 | 0.0290 |
| aux_positional | 138 | 1 | 0.0072 | 0.0435 | 0.2391 |
| union (best-case) | 138 | 32 | 0.2319 | 0.2319 | 0.6667 |

Key takeaways:
- `aux_positional` is **very weak as a strict straight caller**, but has meaningful **box‑equivalent** coverage and strong **index/lane** association.
- `aux_vtrac_index_overdue` is one of the strongest single **tool-only** lane/closure signals in this window.
- `mirror_pair_closure` is the most effective “conversion helper” among the bounded packs (stronger than due-doubles mirror expansions in this window).

---

## Unique contribution (box‑equivalent, v0 window)

If we treat methods as “box-equivalent canonicals” (the same best‑case lens as the `union` row), Aux-derived methods are responsible for a meaningful fraction of the union hits:

- Union box‑equivalent hits: `32/138`
- Union box‑equivalent hits **without Aux-derived methods**: `19/138`
- **Delta attributable to Aux**: `+13` box‑equivalent hits

Breakdown (box‑equivalent):
- Aux only: `13`
- Non‑Aux only: `11`
- Both: `8`
- Neither: `106`

Interpretation:
- Aux is not “noise”; it provides *unique canonical coverage* that other tools do not always surface.
- But this is still not proof of “predictive superiority”; it’s evidence Aux belongs in the superbrain surfaces as a **bounded corroborator**.

---

## Raw Aux evidence overlaps (support signals, not predictions)

From `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__SIGNALS__QUANT.csv` (selected rows):

- Positional shortlist:
  - straight hit rate is low at small top‑N (top10: `1/138`).
  - box‑equivalent improves with N (top10: `6/138`, top16: `10/138`).
- VTRAC overdue overlay:
  - winner’s VTRAC index appears in top5 overdue indices ~9–10% of the time (non‑double winners only).
- Pairs (top10):
  - overlaps are high (~35–50%), which likely reflects “pairs are common” rather than a sharp predictor.
- Sums + Blackapple:
  - overlaps are low in this window and should be treated as weak, optional evidence until proven otherwise.

---

## Next (links)

- Case audit (why/when Aux helps vs misleads): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__CASES.md`
- Feature decisions (what Aux outputs become v0.2 inputs): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__FEATURE_DECISIONS.md`
