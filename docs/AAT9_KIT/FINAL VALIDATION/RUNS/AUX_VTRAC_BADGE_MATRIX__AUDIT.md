# Aux — Boxed VTRAC Badge Matrix (Parity Audit + Export Plan)

Purpose: reconcile the “Windows-app style” boxed VTRAC index chart (35× row table with per-combo badges) with what we export today into SSOT sharepacks, then add a **reporting-only** export so this signal can be measured/compounded in v0.2 without touching analyzers.

Non‑negotiables (v0 synthesis):
- Do **not** change analyzers (Stable/DR/VTRAC/HZ) or combined-table extraction/readers.
- Do **not** modify post-results SSOT sharepacks (`sharepacks/<D>/...`) during synthesis.
- Predictive sharepacks (`sharepacks/_predictive/<D>/...`) must remain winners‑free.

---

## 1) What we already capture (today)

Sharepack-local Aux evidence (per state):
- `sharepacks/<ROOT>/<D>/<STATE>/aux/<STATE>/summary.json` and `summary.md`
  - Pair overdue status buckets per variant: `pairs.by_variant.<variant>.status`
  - VTRAC index overlay/heatboard per variant: `vtrac.overlay_top`, `vtrac.heatboard_top`
- Draw snapshots (the reproducible “world” Aux ran on): `sharepacks/<ROOT>/<D>/<STATE>/aux/draws/*.csv`

Control Center board (day-level, cross-state):
- `sharepacks/<ROOT>/<D>/control_center/due_doubles.csv` / `.md`
  - Grouped by **VTRAC double families** (e.g., `0/5-1/6`), not `vtrac_index` (1–35).

Reference contract:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Aux_Coverage_And_Legend.md`

---

## 2) What is *not* exported today (the gap)

We do **not** export the “boxed VTRAC badge matrix” into sharepacks/RUNS, i.e.:
- for each **vtrac_index 1–35**, show the index’s **boxed canonicals** (Singles/Doubles from the boxed VTRAC reference)
- decorate each combo with:
  - pair-color badges (R/B/P from overdue pair logic)
  - combo “late/very-late” badges (blue-square / red-circle style thresholds)
  - (optional) index row highlights (top recent / top overdue)

This was a major UX surface in the older Aux module and is exactly the “8-combo index closure” lens you’ve been describing.

---

## 3) Why this matters for Superbrain v0 → v0.2

The core question is measurable:

“Do indices with dense badge pressure (multiple R/B combos) compound across variants (C/M/E) and convert into more boxed hits when combined with string-table evidence?”

We cannot answer that cleanly until the badge matrix is exported as a repeatable artifact (same philosophy as Candidate Universe/Play Cards: **evidence → artifact → grade**).

---

## 4) Where the functionality already exists (code hooks)

The badge logic already exists in Aux modules:
- Pair → combo color helper:
  - `modules/analyze_pairs.py:get_combo_color`
- Boxed VTRAC per-index statuses:
  - `modules/analyze_pairs.py:get_vtrac_statuses` (returns per-index singles/doubles combo statuses + recent/overdue index rank)
- (UI-oriented) HTML table generator:
  - `modules/module_d_auxiliary_tools/refactored/boxed_vtrac.py:generate_boxed_vtrac_table`

The missing piece is simply: **export** this into RUNS (reporting-only).

---

## 5) Export plan (reporting-only; no analyzer changes)

New script:
- `scripts/tools/create_aux_vtrac_badge_matrix_report.py`

Contract:
- Reads only sharepack-local Aux draw snapshots (`sharepacks/<ROOT>/<D>/<STATE>/aux/draws/*.csv`).
- Computes badge matrix per variant (Combined/Midday/Evening) using `get_vtrac_statuses(...)`.
- Writes only to RUNS (default):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__AUX_VTRAC_BADGE_MATRIX.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__AUX_VTRAC_BADGE_MATRIX.csv`

Legend (proposed report encoding):
- Pair color (from overdue pairs): `R`=very late, `B`=late, `P`=pending
- Combo DS threshold badges:
  - `RC` = red circle (very late combo DS threshold)
  - `BS` = blue square (late combo DS threshold)

---

## 6) Next action after export exists

Once the export is available for the v0 window (2026‑01‑05→2026‑01‑09), mine “gold”:
- pick cases where:
  - index overlay is high (overdue) AND
  - badge density is high (many R/B combos) AND
  - we still had index_hit_only misses
- capture those as GOLD entries and decide whether the badge-matrix signal becomes:
  - a state-level gating signal (“play day / pass day”), and/or
  - a candidate-level boost (index-first closure), and/or
  - a selection-budget allocator (play card tiering).

