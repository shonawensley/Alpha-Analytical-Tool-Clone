# VTRAC Enhanced — v0 Feature Decisions (Inputs to v0.2)

Purpose: convert the VTRAC v0 audit into explicit, **actionable consumption rules** for the superbrain layers (Candidate Universe / Play Cards), without touching analyzers yet.

Read first:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__QUANT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__CASES.md`
- `docs/AAT9_KIT/AAT9_VTRAC_Analyzer_Analysis_Log.md` (background)

Non‑negotiables:
- Analyzer logic stays frozen during v0 synthesis.
- Predictive packs stay winners‑free; evaluation-only artifacts must not become predictive inputs.
- Baseline conclusions use `--profile tool_only` (Profit Alerts quarantined).

---

## Summary conclusion (v0)

In the v0 Jan window (`2026-01-05..2026-01-09`), VTRAC Enhanced as currently consumed (`method_id=vtrac_enhanced_top`, top‑N straights, `STRAIGHT`) is:
- weak as a strict straight caller at low `top_n`, and
- only moderately useful as an index/lane lens at larger `top_n`.

So the v0.2 posture is:
- keep VTRAC Enhanced as a **predictive input**, but treat it as **support/lane evidence**, not a primary caller.

Winner type handling note (important):
- Doubles are included in `vtrac_index` metrics (indices 1–35).
- Triples intentionally have no `vtrac_index` (legacy behavior).

Measured harness outputs (cross-window; reporting-only):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2025-06-21_to_2025-06-23.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2025-12-30_to_2026-01-04.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_ENHANCED_V0__HARNESS__2026-01-05_to_2026-01-09.md`

---

## Decision table (v0.2 consumption)

Legend:
- **Keep (predictive input)**: allowed to directly create packs / influence play cards.
- **Demote (support-only)**: allowed as evidence/boosts, but should not generate “top picks” by itself.
- **Eval-only**: keep only for post-results analysis/diagnostics; never use in predictive mode.

| VTRAC output / signal | Current role | v0 evidence | v0.2 decision | Notes / implementation hook |
|---|---|---|---|---|
| Enhanced top straights (`straights_ranked` → `method_id=vtrac_enhanced_top`) | Candidate Universe pack (STRAIGHT, top‑N) | `top_n=8`: straight_hit `1/138`; index_hit `16/136` | **Keep** | Keep at `--top-n-vtrac=8` in tool-only baseline, but treat as convergence votes + lane lens. |
| BOX-equivalent canonicalization of top straights (counterfactual) | Not implemented | Canonical hit improves with `top_n`, but still modest | **Demote (research-only)** | v0.3 idea: optional derived pack (`vtrac_enhanced_top_box_equiv`) gated behind a flag; measure conversion without replacing the straight pack. |
| Winner index placement (`winner_index_placements` in `summary.json`) | Post-results evaluation | Useful “rail correctness” diagnostic | **Eval-only** | Use in audits + gold entries to separate index-hit vs canonical-hit; never predictive input. |
| Day-level VTRAC validation reports / compact report bundles | Winners-dependent artifacts | Post-results only | **Eval-only** | Remain SSOT diagnostics; do not copy into predictive packs. |

---

## v0.2 “minimal-change” rule (recommended)

To keep v0.2 stable:

1) Keep VTRAC Enhanced in Candidate Universe at the current default:
   - `--top-n-vtrac=8` (tool-only baseline)
2) Do not expand into index closure packs by default yet.
3) Use VTRAC Enhanced primarily as:
   - a convergence voter,
   - an index correctness lens (“rail hit vs box miss” diagnostics).

After we mine more “index-hit → box-hit conversion” gold entries, revisit:
- whether an *additive* index-closure pack seeded by VTRAC indices should exist (bounded; measurable),
- play-card weighting for VTRAC relative to Stable + Hot Zones.

---

## What this does *not* decide yet (defer)

- Any changes to VTRAC analyzer scoring/logic.
- Any change to VSTRAIGHTS lane generation.

Those are v0.3+ items once v0.2 defaults are stable.
