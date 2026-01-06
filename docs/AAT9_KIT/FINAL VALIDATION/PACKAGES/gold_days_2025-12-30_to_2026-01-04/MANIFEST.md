# Gold Days Research Pack — Manifest (2025‑12‑30 → 2026‑01‑04)

This manifest defines the intended scope of the 6‑day corpus expansion. Everything listed here is either:
- frozen evidence under `sharepacks/<D>/...`, or
- filled analysis artifacts under `docs/AAT9_KIT/FINAL VALIDATION/RUNS/...`.

Dates:
- D=2025‑12‑30 (history workbook H≈2025‑12‑29)
- D=2025‑12‑31 (H≈2025‑12‑30)
- D=2026‑01‑01 (H≈2025‑12‑31)
- D=2026‑01‑02 (H≈2026‑01‑01)
- D=2026‑01‑03 (H≈2026‑01‑02)
- D=2026‑01‑04 (H≈2026‑01‑03)

## 1) SSOT workflow docs (read first)

- `briefings/CODEX_READ_FIRST_AAT9_WSL_2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Analysis_Navigator.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Pattern_Progression_Primer.md` (concept training lens; optional)

Control Center / trackers semantics:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Control_Center_Daily_Template.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`

## 2) RUNS (analysis artifacts; primary review surface)

Progress + navigation:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/README.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`

Corpus-level synthesis:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_SYNTHESIS.md`

Per-day portals (Brain‑2 + Brain‑1):
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

Per-state run reports:
- All files matching:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30__*.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-31__*.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01__*.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-02__*.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-03__*.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-04__*.md`
- Note: `__CONTROL_CENTER.md` and `__DAY_SYNTHESIS.md` are included above explicitly.

## 3) Sharepacks (frozen evidence; audit surface)

Day roots:
- `sharepacks/2025-12-30/`
- `sharepacks/2025-12-31/`
- `sharepacks/2026-01-01/`
- `sharepacks/2026-01-02/`
- `sharepacks/2026-01-03/`
- `sharepacks/2026-01-04/`

Per-day validators (used by validation + synthesis):
- `sharepacks/2025-12-30/vtrac_compact_report.json`
- `sharepacks/2025-12-31/vtrac_compact_report.json`
- `sharepacks/2026-01-01/vtrac_compact_report.json`
- `sharepacks/2026-01-02/vtrac_compact_report.json`
- `sharepacks/2026-01-03/vtrac_compact_report.json`
- `sharepacks/2026-01-04/vtrac_compact_report.json`

Brain‑2 frozen Control Center bundles (per day):
- `sharepacks/2025-12-30/control_center/`
- `sharepacks/2025-12-31/control_center/`
- `sharepacks/2026-01-01/control_center/`
- `sharepacks/2026-01-02/control_center/`
- `sharepacks/2026-01-03/control_center/`
- `sharepacks/2026-01-04/control_center/`

Per-state evidence folders (all tracked states):
- `sharepacks/<D>/<STATE>/winners/<STATE>/...`
- `sharepacks/<D>/<STATE>/stable/<STATE>/...`
- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/...`
- `sharepacks/<D>/<STATE>/vtrac/<STATE>/...`
- `sharepacks/<D>/<STATE>/hot_zones/<STATE>/...`
- `sharepacks/<D>/<STATE>/aux/<STATE>/...`

## 4) Results files (window evaluation depends on having future days)

- `data/results/2025-12-30.txt`
- `data/results/2025-12-31.txt`
- `data/results/2026-01-01.txt`
- `data/results/2026-01-02.txt`
- `data/results/2026-01-03.txt`
- `data/results/2026-01-04.txt`

If additional future results files exist, include them in review to reduce censoring in Profit Alerts episode evaluation.
