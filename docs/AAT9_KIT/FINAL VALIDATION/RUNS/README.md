# Master Validation — Run Reports

This folder stores **filled, per‑example** master validation reports so we don’t lose track across sessions.

- Start-here portal (fast navigation): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- Progress tracker (which reports are filled): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
- Optional per-day cross-state synthesis (aggregates the 14 state reports for one day): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD__DAY_SYNTHESIS.md`
- Per-day Control Center run report (Brain-2, built from `sharepacks/<D>/control_center/`): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD__CONTROL_CENTER.md`
- Optional cross-day corpus synthesis (aggregates multiple day syntheses): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__CORPUS_SYNTHESIS.md`
- Optional cross-day corpus dashboard + study cases (fast orientation; not tuning rules):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__CORPUS_DASHBOARD.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__CONVERGENCE_CASES.md` (+ `.csv`)
- Optional cross-day lenses (quantification, not betting advice):
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__CROSS_VARIANT_REPORT.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__MIRROR_DOUBLE_FREQUENCY.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__DR_LENS_REPORT.md`
- Optional results-horizon helper (explains CENSORED episode tails): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__RESULTS_HORIZON.md`
- Optional cross-day Brain-2 rollups:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__CONTROL_CENTER_ROLLUP.md` (+ `.csv`)
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__PROFIT_ALERTS_ROLLUP.md` (+ `.csv`)
- Optional cross-day Codex deep analysis (parallel reviewer output): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__CODEX_DEEP_ANALYSIS.md`
- Auto-exported corpus summary (one row per day/state/period): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`
- Auto-extracted Fix-later index (from filled run reports): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
- Post-runs triage (claims → fixed vs misframed vs fix-later): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/POST_RUNS_TRIAGE.md`
- Fix-now execution ledger (pipeline/semantics bugs only): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`

- The canonical question template lives in: `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
- A run report is a *snapshot for one state + one results/sharepack date* with:
  - Links to the sharepack artifacts
  - Embedded per‑tool summarizer Markdown blocks (Stable/DR/VTRAC/Hot Zones) + Aux
  - Placeholders to fill Parts A–5 in one place

Generate a new run report (recommended):
```bash
python3 scripts/tools/create_master_validation_run_report.py --date YYYY-MM-DD --state OntarioCanada4
```

Default output:
`docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD__<STATE>.md`

Fill placeholders in an existing run report (safe, evidence-only):
```bash
python3 scripts/tools/fill_master_validation_run_report.py --date YYYY-MM-DD --state OntarioCanada4
```

Optional: normalize Part 5 into the multi-line SSOT format (required for `export_master_validation_corpus.py` parsing):
```bash
python3 scripts/tools/fill_master_validation_run_report.py --date YYYY-MM-DD --state OntarioCanada4 --normalize-part5
```

Generate a per-day Control Center run report (Brain-2, sharepack-aligned):
```bash
python3 scripts/tools/create_control_center_daily_run_report.py --date YYYY-MM-DD
```

Default output:
`docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD__CONTROL_CENTER.md`

Generate a per-day cross-state synthesis stub (Brain-1, optional but recommended):
```bash
python3 scripts/tools/create_day_synthesis_run_report.py --date YYYY-MM-DD
```

Default output:
`docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD__DAY_SYNTHESIS.md`
