# Aux Coverage + Legend (Final Validation / Sharepacks)

Purpose: confirm what Aux signals are already captured in SSOT sharepacks today, how to interpret them (legend), and what is *not* yet exported as a sharepack artifact.

This is a **reporting/contract** document only. It does not change analyzers.

---

## 0) Where Aux lives in sharepacks

Per-state Aux snapshot + summary:
- `sharepacks/<ROOT>/<D>/<STATE>/aux/draws/*.csv` (draw snapshots)
- `sharepacks/<ROOT>/<D>/<STATE>/aux/<STATE>/summary.json` (machine-readable)
- `sharepacks/<ROOT>/<D>/<STATE>/aux/<STATE>/summary.md` (human-readable)

Where:
- `<ROOT>` is usually `sharepacks/` (post-results SSOT) or `sharepacks/_predictive/` (pre-results snapshot).
- `<D>` is the results/sharepack date.

Important: Aux is **draws-only**. In predictive packs it must remain winners-free.

---

## 1) Pair overdue (“red/blue/purple”) — what it means

Source: `alpha_analytical/control_center/aux_validation.py` (via `collect_pair_stats_for_state()`).

In `summary.json`:
- `pairs.by_variant.<variant>.status` maps pair → color severity:
  - `red` = “very late”
  - `blue` = “late”
  - `purple` = “pending” (>=25)

This is the “Any Position Box” pair model: each draw contributes the unordered internal pairs `(P1P2, P2P3, P1P3)` and doubles contribute the repeating pair (e.g., `AA`).

---

## 2) “Due Doubles” board (Control Center) — what it is and how to read it

Artifacts:
- `sharepacks/<ROOT>/<D>/control_center/due_doubles.csv`
- `sharepacks/<ROOT>/<D>/control_center/due_doubles.md`

This board is a **cross-variant, sharepack-aligned** summary of *boxed doubles* grouped into **VTRAC double families** (e.g., `0/5-1/6`, `3/8-4/9`), not “vtrac_index”.

Each family cell contains combos with compact tokens like:
- `566(RE:1000)`

Legend for the token:
- `566` = canonical boxed double (sorted digits)
- `R` / `B` = severity from Aux thresholds:
  - `R` = very late (>= `COMBO_DOUBLE_VERY_LATE`, typically 1000)
  - `B` = late (>= `COMBO_DOUBLE_LATE`, typically 667)
- `C/M/E` = which variant’s draw stream produced the severity (Combined/Midday/Evening)
- `:1000` = draws-since (within that variant stream)

Important disambiguation:
- **VTRAC double family** labels (e.g., `0/5-1/6`) are groupings of canonical doubles derived from the VTRAC reference table’s “Doubles” section.
- They are *not* the same as **vtrac_index** (1–35). One family can span many indices.

---

## 3) VTRAC index overlay/heatboard — what we have today

In `summary.json`:
- `vtrac.overlay_by_variant.<variant>`: top overdue indices by draws-since (windowed scan)
- `vtrac.heatboard_by_variant.<variant>`: hazard/avg-gap style metrics by index (windowed scan)

This is the right “index-level” primitive for compounding later (e.g., “index 16 is overdue in both Combined and Evening”).

---

## 4) What is *not* currently exported (and why you might remember it)

Older Aux UX and research docs describe a “boxed VTRAC combination chart” that visually decorates *many combos inside an index* with pair/due/symbol badges.

Today, sharepacks capture:
- **index-level** status (overlay/heatboard),
- **pair-level** overdue buckets,
- **double-family** due-doubles groupings,
- and a bounded **positional shortlist** (top candidates + tags).

We still do **not** export a full “all-combos-in-each-index with symbol overlays” chart *into sharepacks* (to keep sharepacks focused on frozen evidence).

However, we **do** export a sharepack-derived version into RUNS (reporting-only) via:
- `python3 scripts/tools/create_aux_vtrac_badge_matrix_report.py --date <D> [--sharepacks-root sharepacks/_predictive]`
  - Outputs:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__AUX_VTRAC_BADGE_MATRIX.md`
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__AUX_VTRAC_BADGE_MATRIX.csv`

---

## 5) Safe validators (already in repo)

- Tables vs Aux alignment (sharepack mode):
  - `python3 scripts/tools/validate_tables_aux_alignment.py --date <D> --state <STATE> --strict`

This ensures the string tables and Aux draw snapshots describe the same “world snapshot” for the day.

---

## 6) Fix-later ideas (do not implement during pipeline hardening)

- Candidate Universe “horizon grading” (carryover / N-draw window scoring) once the baseline corpus is stable.
- Optional: compound the boxed VTRAC badge-matrix export into v0.2 scoring once we’ve mined enough gold entries to justify it.
