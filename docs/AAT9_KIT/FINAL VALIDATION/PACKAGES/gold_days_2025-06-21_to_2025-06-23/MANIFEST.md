# Gold Days Research Pack — Manifest (2025‑06‑21 → 2025‑06‑23)

This manifest defines the intended scope of the “gold days” corpus. Everything listed here is either:
- frozen evidence under `sharepacks/<D>/...`, or
- filled analysis artifacts under `docs/AAT9_KIT/FINAL VALIDATION/RUNS/...`.

Dates:
- D=2025‑06‑21 (history workbook H≈2025‑06‑20)
- D=2025‑06‑22 (H≈2025‑06‑21)
- D=2025‑06‑23 (H≈2025‑06‑22)

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
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CORPUS_SYNTHESIS.md`

Per-day portals (Brain‑2 + Brain‑1):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__CONTROL_CENTER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__DAY_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__CONTROL_CENTER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__DAY_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__CONTROL_CENTER.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__DAY_SYNTHESIS.md`

Per-state run reports:
- All files matching:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__*.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-22__*.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__*.md`
- Note: `__CONTROL_CENTER.md` and `__DAY_SYNTHESIS.md` are included above explicitly.

## 3) Sharepacks (frozen evidence; audit surface)

Day roots:
- `sharepacks/2025-06-21/`
- `sharepacks/2025-06-22/`
- `sharepacks/2025-06-23/`

Provenance / day mapping:
- `sharepacks/2025-06-21/README.md`
- `sharepacks/2025-06-22/README.md`
- `sharepacks/2025-06-23/README.md`

Global VTRAC aggregator feeds (used by validation + synthesis):
- `sharepacks/2025-06-21/vtrac_compact_report.json`
- `sharepacks/2025-06-22/vtrac_compact_report.json`
- `sharepacks/2025-06-23/vtrac_compact_report.json`

Brain‑2 frozen Control Center bundles (per day):
- `sharepacks/2025-06-21/control_center/`
- `sharepacks/2025-06-22/control_center/`
- `sharepacks/2025-06-23/control_center/`

Per-state evidence folders (all tracked states):
- `sharepacks/<D>/<STATE>/winners/<STATE>/...`
- `sharepacks/<D>/<STATE>/stable/<STATE>/...`
- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/...`
- `sharepacks/<D>/<STATE>/vtrac/<STATE>/...`
- `sharepacks/<D>/<STATE>/hot_zones/<STATE>/...`
- `sharepacks/<D>/<STATE>/aux/<STATE>/...`

## 4) Results files (window evaluation depends on having future days)

- `data/results/2025-06-21.txt`
- `data/results/2025-06-22.txt`
- `data/results/2025-06-23.txt`
- (Optional, if present) additional `data/results/2025-06-24..2025-07-06.txt` to reduce censoring for window evaluation.
