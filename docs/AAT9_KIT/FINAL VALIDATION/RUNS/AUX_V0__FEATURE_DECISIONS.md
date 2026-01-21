# Aux — v0 Feature Decisions (v0.2 Inputs, Tool‑First)

Purpose: lock how **Aux** should be consumed in v0.2 selection layers (Candidate Universe / Play Cards / Portfolio) without touching analyzers.

This is a **consumption audit** outcome, not a claim that Aux “predicts” winners.

Baseline:
- v0 window: `2026-01-05` → `2026-01-09`
- profile: `tool_only` (Profit Alerts quarantined)
- quantitative evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__QUANT.md`
- case evidence: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__AUDIT__CASES.md`

---

## 1) Decision table (Keep / Demote / Eval‑only)

Legend:
- **Keep**: remains a first-class Candidate Universe input in v0.2 (bounded + deterministic).
- **Demote**: keep, but treat as corroboration/envelope (avoid consuming as “primary straight caller”).
- **Eval‑only**: keep as evidence; do not ingest as candidate packs until it proves incremental value.

| Feature / method_id | Current role | v0 evidence | v0.2 decision | Notes |
|---|---|---|---|---|
| `aux_vtrac_index_overdue` | index-closure pack | strong hit_any among Aux methods (9/138) and contributes multiple Aux-only canon hits | **Keep** | Treat as “bounded closure / lane locator”. Many Aux-only cases still fail in PlayCard B12, so the bottleneck is budget allocation. |
| `mirror_pair_closure` | mirror-pair conversion pack | moderate hit_any (5/138) and acts as conversion helper | **Keep** | Prefer this as an “index→box conversion” helper over adding unbounded closures. |
| `due_doubles` | compact doubles-family closure | low-ish hit_any (2/138) but very cheap and has clear semantic meaning | **Keep** | Grouped by VTRAC double families (see `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Aux_Coverage_And_Legend.md`). |
| `due_doubles_mirror_single` / `due_doubles_mirror_double` | bounded mirror-double expansions | weak in v0 window but cheap and consistent | **Keep (gated)** | Keep, but treat as “doubles-heavy day” helpers; do not overweight vs other tools until corpus grows. |
| `aux_positional` | positional shortlist | extremely weak as strict STRAIGHT caller (1/138), but has meaningful box-equivalent / index association | **Demote** | Treat as a structure/pressure lens or digit-envelope source; avoid presenting it as “10 straight picks”. |
| pairs top-K overlaps (raw Aux) | evidence lens only | high overlap (likely low specificity) | **Eval-only** | Don’t ingest into CU as prediction packs yet. Mine via gold ledger if repeatable “badge matrix density across variants” proves value. |
| sums/root-sums (raw Aux) | evidence lens only | low overlap in v0 window | **Eval-only** | Keep in Aux summary; do not ingest for prediction until proven. |
| Blackapple (raw Aux) | evidence lens only | low overlap in v0 window | **Eval-only** | Same posture as sums/pairs. |

---

## 2) Practical v0.2 implications (what changes, without changing analyzers)

### 2.1 Candidate Universe

Keep Aux packs in Candidate Universe, but treat them as **bounded closure opportunities**, not “final calls”.

This means:
- keep emitting the Aux packs (as today),
- but do not interpret their existence as “we predicted”; interpretation happens after grading.

### 2.2 Play Cards (budgeted)

The case audit shows a consistent pattern:
- Aux packs often contain the correct canonical/index, but B12 frequently does not allocate any budget to them.

Action (v0.2, selection-layer only, stills of evidence):
- treat `aux_vtrac_index_overdue` + `mirror_pair_closure` as eligible for reserved “conversion slots” in Play Cards (Fix‑Later / v0.2 policy discussion), because they are compact and measurably contribute to union coverage.

### 2.3 Portfolio (cross-state triage)

The portfolio already displays:
- `Due doubles (canonicals)`
- CU pack counts and union sizes

v0.2 stance:
- Keep ranking tool-first (see `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`).
- Do not add more raw Aux signals into the ranking yet; mine the badge matrix first.
  - Badge pressure harness (TopK pressure vs TopK overdue): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2026-01-05_to_2026-01-09.md`

---

## 3) Parameter guidance (defaults, not hard rules)

These are “reasonable v0.2 defaults” to keep behavior stable while we collect more graded days:
- `aux_vtrac_index_overdue`: top overdue indices per variant should remain **small** (e.g., top 1–2), because index expansion is expensive.
- `mirror_pair_closure`: keep bounded (pair + top-3 third digits, BOX expand unique perms).
- `due_doubles`: keep top-N small (e.g., top 4 canonicals per variant).

---

## 4) What to revisit in v0.3 (after more graded days)

- If Aux-only canon hit rates remain meaningful but Play Card conversion stays low: adjust budget allocation policy (selection layer), not analyzers.
- If we discover a correctness bug in Aux data wiring (tables↔draw alignment): Fix‑Now, but only if validated by the existing validators.
- After the badge matrix mining is complete, decide whether “badge density across variants” becomes a scored feature in portfolio ranking.
