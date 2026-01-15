# Hot Zones — v0 Feature Decisions (Inputs to v0.2)

Purpose: convert the Hot Zones v0 audit into explicit, **actionable consumption rules** for the superbrain layers (Candidate Universe / Play Cards), without touching analyzers yet.

Read first:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__QUANT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__CASES.md`
- `docs/AAT9_KIT/AAT9_Hot_Zones_Validation_Log.md` (background)

Non‑negotiables:
- Analyzer logic stays frozen during v0 synthesis.
- Predictive packs stay winners‑free; evaluation-only artifacts must not become predictive inputs.
- Baseline conclusions use `--profile tool_only` (Profit Alerts quarantined).

---

## Summary conclusion (v0)

In the v0 Jan window (`2026-01-05..2026-01-09`), Hot Zones as currently consumed (`method_id=hot_zones_top`, top‑N triads, `STRAIGHT`) is:
- weak as a strict straight caller at low `top_n`, but
- moderately useful as an index/lane lens (`vtrac_index_hit` rises as `top_n` grows).

So the v0.2 posture is:
- keep Hot Zones as a **predictive input**, but treat it as **support/lane evidence**, not a primary caller.

---

## Decision table (v0.2 consumption)

Legend:
- **Keep (predictive input)**: allowed to directly create packs / influence play cards.
- **Demote (support-only)**: allowed as evidence/boosts, but should not generate “top picks” by itself.
- **Eval-only**: keep only for post-results analysis/diagnostics; never use in predictive mode.

| Hot Zones output / signal | Current role | v0 evidence | v0.2 decision | Notes / implementation hook |
|---|---|---|---|---|
| Predictive triad list (`<D>_hot_zones_winner_map.json`) → `method_id=hot_zones_top` | Candidate Universe pack (STRAIGHT, top‑N) | `top_n=8`: straight_hit `1/138`; index_hit `23/136` | **Keep** | Keep at `--top-n-hot-zones=8` in tool-only baseline. Treat as convergence votes + lane lens; not “play it raw”. |
| Hot Zones “BOX-equivalent” canonicalization of top triads (counterfactual) | Not implemented | Canonical hit improves (e.g., `top_n=8`: `4/138`) but cost rises (`avg_cost_box≈36.9`) | **Demote (research-only)** | v0.3 idea: add an optional derived pack (`hot_zones_top_box_equiv`) gated behind a flag so we can measure conversion of “box-correct” cases without replacing the straight pack. |
| Post-results summary (`sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.json`) | Evaluation + RUNS evidence | Winner usually present in full top-lanes table, rarely in top20 triads | **Eval-only** | Use for auditing “why it missed” and for environment classification; never as predictive input. |
| Winner map hits/notes (`winner_map.triad_present`, `top_lanes.best_rank`) | Post-results diagnostics | Case sets show sensitivity to top_n | **Eval-only** | Feed into gold entries as “index-hit vs canonical-hit” exemplars; do not treat as prediction. |

---

## v0.2 “minimal-change” rule (recommended)

To keep v0.2 stable while we audit VTRAC:

1) Keep Hot Zones in Candidate Universe at the current default:
   - `--top-n-hot-zones=8` (tool-only baseline)
2) Do not “promote” Hot Zones to BOX-equivalent by default yet.
3) Use Hot Zones primarily as:
   - a low-cost contributor to convergence (votes),
   - an index/lane lens to identify “neighborhood correctness”.

After the VTRAC audit, revisit:
- whether Hot Zones should remain STRAIGHT-only or gain an optional BOX-equivalent derived pack (additive, not replacement),
- play-card weighting (Hot Zones may be underweighted or correctly low; decide after VTRAC audit).

---

## What this does *not* decide yet (defer)

- Any changes to Hot Zones scoring/weights/features inside the analyzer.
- Any “top lanes” consumption beyond the current triad list.

Those are v0.3+ items once v0.2 defaults are stable.

