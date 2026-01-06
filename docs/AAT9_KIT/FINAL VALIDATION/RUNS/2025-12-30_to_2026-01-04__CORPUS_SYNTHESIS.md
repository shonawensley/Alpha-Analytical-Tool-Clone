# Corpus Synthesis — D=2025-12-30..2026-01-04 (6-day expansion corpus)

Scope
- Days (D): `2025-12-30`, `2025-12-31`, `2026-01-01`, `2026-01-02`, `2026-01-03`, `2026-01-04`
- History workbooks (H): recorded per day in `sharepacks/<D>/control_center/meta.json` (usually `D-1`)
- States per day: 14 tracked states (+ one `CONTROL_CENTER` daily report)
- Total run reports: 84 state reports (14 × 6) + 6 control center reports
- Outcomes: Midday + Evening (Combined is a lens only; used for cross-variant structure and tags)

Pointers
- Run report progress index: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
- Corpus summary (machine-readable): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`
- Fix-later rollup: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
- Per-day portals (Brain‑2 then Brain‑1):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__CONTROL_CENTER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__DAY_SYNTHESIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__CONTROL_CENTER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__DAY_SYNTHESIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__CONTROL_CENTER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__DAY_SYNTHESIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__CONTROL_CENTER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__DAY_SYNTHESIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__CONTROL_CENTER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__DAY_SYNTHESIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__CONTROL_CENTER.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__DAY_SYNTHESIS.md`

---

## Executive Summary (what this corpus is for)

- This is a corpus expansion beyond the original 3 “gold days” starter set (June 2025).
- The value of the expansion is *not* to “prove” an indicator; it is to:
  - reduce overfitting pressure,
  - increase the variety of environments,
  - and give you enough negative controls to keep tuning honest.
- Treat per-tool “misses” as data: the workflow is designed to separate “pipeline integrity” from “tool outcome”.

---

## Data-quality / workflow notes (do not confuse with tool performance)

- Some days may have missing results lines for `PuertoRico4` (expected on some calendars). Those should be treated as N/A for grading, not as tool misses.
- This corpus is intended to be analyzed using:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
  - and the per-day portals listed above.

