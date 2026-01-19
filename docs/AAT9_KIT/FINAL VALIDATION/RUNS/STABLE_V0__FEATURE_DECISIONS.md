# Stable — v0 Feature Decisions (Inputs to v0.2)

Purpose: convert the Stable v0 audit into explicit, **actionable consumption rules** for the superbrain layers (Candidate Universe / Play Cards), without touching analyzers yet.

This is the “keep/demote/eval-only” decision table.

Read first:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__QUANT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__CASES.md`
- `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md` (background on Stable scoring intent)

Non‑negotiables:
- Analyzer logic stays frozen during v0 synthesis.
- Predictive packs stay winners‑free; evaluation-only artifacts must not become predictive inputs.
- Baseline conclusions use `--profile tool_only` (Profit Alerts quarantined).

---

## Summary conclusion (v0)

In the v0 Jan window (`2026-01-05..2026-01-09`, 14 states, Midday+Evening):

- Stable is strong at **containing the winning family** somewhere (evidence-level `families.present=134/140`), but weak as a strict **top-caller** for exact canonicals at small `top_n`.
- As currently consumed (`method_id=stable_top`, top‑N canonicals per section, BOX-expanded), Stable behaves more like an **index/lane lens** than a reliable “top-3 caller”.

So the v0.2 posture is:
- Stable remains a **kept predictive input** (because it is inexpensive at low `top_n` and provides useful convergence votes),
- but it should not be treated as a standalone “play this and expect a hit” signal.

---

## Decision table (v0.2 consumption)

Legend:
- **Keep (predictive input)**: allowed to directly create packs / influence play cards.
- **Demote (support-only)**: allowed as evidence/boosts, but should not generate “top picks” by itself.
- **Eval-only**: keep only for post-results analysis/diagnostics; never use in predictive mode.

| Stable output / signal | Current role | v0 evidence | v0.2 decision | Notes / implementation hook |
|---|---|---|---|---|
| Stable “top canonicals” from `*_stable_patterns_scores.csv` | Candidate Universe pack (`method_id=stable_top`, BOX) | `top_n=3` hit_any `2/140` but index-hit (index-defined opps; excludes triples) `22/136`; increasing `top_n` increases hits but explodes cost | **Keep** | Keep in tool-only baseline, but treat as a lane/index lens. Default stays `--top-n-stable=3` unless explicitly testing higher `top_n`. |
| Stable compound leaderboard (`*_stable_patterns_compound.csv`) | Not used as packs | Evidence-level `compound.present=90/140`; median `compound.winner_rank_fraction≈0.133` | **Demote** | v0.3 candidate pack idea: mine *bounded* digit pools / index votes from compound (not “top 20 boxed canonicals”). Defer until after HZ/VTRAC audits. |
| Stable families leaderboard (`*_stable_patterns_families.csv`) | Not used as packs | Evidence-level `families.present=134/140`; median `families.winner_rank_fraction≈0.162` | **Demote** | High-value evidence for “index correctness” even when canonical misses. v0.3 idea: family→index vote (bounded) to support index-hit → box-hit conversion. |
| Stable metrics (`*_metrics.json`) | Not used as predictive input | Useful for tool health + winner placement diagnostics | **Eval-only** | Keep for auditing and for “why it missed” explanations; do not translate directly into picks yet. |
| Winner spotlight files (`*_winner_family_spotlight_*.csv`) | Post-results evaluation | Winners-dependent artifacts | **Eval-only** | Never include in predictive packs; keep in SSOT sharepacks and RUNS for post-hoc learning. |
| Stable winners HTML/JSON lens (reports/stable/winners_by_date/…) | Post-results environment lens | Winners-dependent artifacts | **Eval-only** | Same: environment reading + reverse engineering only. |

---

## v0.2 “minimal-change” rule (recommended)

To keep v0.2 stable while we audit other tools:

1) Keep Stable as a Candidate Universe input at the current default:
   - `--top-n-stable=3` (tool-only baseline)
2) Do **not** increase Stable `top_n` globally yet (too expensive and risks “wide noise”).
3) Use Stable primarily as:
   - a convergence voter (“does another tool agree?”),
   - and an index/lane lens (“are we in the right neighborhood?”).

After Hot Zones + VTRAC audits are complete, we can revisit:
- play-card method weights (Stable may be overweighted relative to its direct hit rate),
- bounded “index closure” packs seeded by Stable evidence (selection-layer only).

---

## What this does *not* decide yet (defer)

- Any changes to Stable scoring/weights/features.
- Any expansion of Stable ingestion beyond `stable_top` (compound/families mining).
- Any horizon/carryover grading semantics.

Those are v0.3+ items once v0.2 defaults are stable and other tool audits are complete.
