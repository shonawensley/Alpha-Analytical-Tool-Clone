# Stable (String Tables) — v0 Audit (Quantitative)

Purpose: quantify whether **Stable** (as currently consumed in the *prediction layers* / “superbrain surfaces” like Candidate Universe + Play Cards) behaves like:

- a **primary caller** (its top picks hit at meaningful rates), or
- a **supporting corroborator / lane lens** (it often lands in the right VTRAC family, but not the exact canonical).

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

Primary quantitative source (selection‑layer performance):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-0[5-9]__CANDIDATE_UNIVERSE_GRADE__tool_only.csv`

Evidence-level source (what Stable “can see”, regardless of whether we selected it):
- `sharepacks/<D>/<STATE>/stable/<STATE>/summary.json` (from `stable_sharepack_summary.py`)

---

## What “Stable” means in this audit

### Candidate Universe ingestion (selection layer)

Current Candidate Universe pack:
- `method_id=stable_top`
- Source: `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_stable_patterns_scores.csv`
- How it is built:
  - per section (Combined / Midday / Evening): take top‑N canonicals by best Stable score
  - play mode: `BOX` (unique perms per canonical)

Key implication:
- Stable is being evaluated here as a **very narrow top‑caller** (top‑N), not as a broad evidence lens.

### Evidence-level presence (tool output, not selection)

From `sharepacks/<D>/<STATE>/stable/<STATE>/summary.json` (winners evidence):
- `scores.present` and `scores.winner_rank_fraction`
- `compound.present` and `compound.winner_rank_fraction`
- `families.present` and `families.winner_rank_fraction`

This tells us whether Stable *contained* the winner and how high it ranked it internally.

---

## Results snapshot (tool_only, v0 window)

### A) Evidence-level (what Stable contains, regardless of selection)

Across 140 opportunities:
- `scores.present`: `90/140` (0.6429) — winners are often **missing from Stable scores**, but present in families.
- `compound.present`: `90/140` (0.6429)
- `families.present`: `134/140` (0.9571)

Median rank fraction when present (lower is better):
- `scores.winner_rank_fraction`: `0.2360`
- `compound.winner_rank_fraction`: `0.1332`
- `families.winner_rank_fraction`: `0.1620`

Interpretation:
- Stable often “sees” the winning family somewhere, but **rarely ranks the winning canonical near the very top**.

### B) Selection-level (what Stable contributes as a top‑caller)

Selection performance for `method_id=stable_top` depends heavily on `top_n`.

See: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__QUANT.csv`

| top_n | opps | hit_any | hit_any_rate | index_hit_rate (index-defined opps) | avg_total_cost (3 sections) |
|---:|---:|---:|---:|---:|---:|
| 3 | 140 | 2 | 0.0143 | 0.1618 | 30.49 |
| 5 | 140 | 3 | 0.0214 | 0.2500 | 52.94 |
| 10 | 140 | 8 | 0.0571 | 0.3750 | 109.99 |
| 20 | 140 | 20 | 0.1429 | 0.6176 | 232.04 |

Notes:
- `hit_any` here is “winner canonical appears in top‑N canonicals in at least one section”, BOX-expanded.
- `index_hit_rate` excludes triples only (legacy behavior: no `vtrac_index` for triples); doubles are included.
- `avg_total_cost` is the sum of BOX-expanded unique perms per section (Combined+Midday+Evening) for a typical state/day.

Interpretation:
- At strict `top_n=3`, Stable contributes **very few direct hits**.
- As `top_n` grows, Stable becomes a strong **lane/index selector** (index_hit rises), but costs explode if we were to “play it raw”.

---

## v0 conclusion (Stable)

1) **Stable is not behaving like a reliable “top‑caller” at low top_n**, but it *is* a useful lane/index lens.

2) The immediate “profitability-safe” move is **not** “increase Stable top_n” (too expensive), but:
- treat Stable as a contributor to **cross-pack convergence** (votes),
- and focus on “index hit → box hit conversion” via bounded closures (handled elsewhere in v0.2).

Next:
- Case audit (near misses + “should-have-hit” evidence): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__CASES.md`
- Feature decisions (what Stable outputs should feed v0.2 surfaces): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__FEATURE_DECISIONS.md`
