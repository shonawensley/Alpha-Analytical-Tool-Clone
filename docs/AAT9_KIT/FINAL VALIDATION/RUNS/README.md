# Master Validation — Run Reports

This folder stores **filled, per‑example** master validation reports so we don’t lose track across sessions.

- Progress tracker (which reports are filled): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`
- Optional per-day cross-state synthesis (aggregates the 14 state reports for one day): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD__DAY_SYNTHESIS.md`
- Per-day Control Center run report (Brain-2, built from `sharepacks/<D>/control_center/`): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD__CONTROL_CENTER.md`
- Optional cross-day corpus synthesis (aggregates multiple day syntheses): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD_to_YYYY-MM-DD__CORPUS_SYNTHESIS.md`
- Auto-exported corpus summary (one row per day/state/period): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv`
- Auto-extracted Fix-later index (from filled run reports): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`

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

Generate a per-day Control Center run report (Brain-2, sharepack-aligned):
```bash
python3 scripts/tools/create_control_center_daily_run_report.py --date YYYY-MM-DD
```

Default output:
`docs/AAT9_KIT/FINAL VALIDATION/RUNS/YYYY-MM-DD__CONTROL_CENTER.md`
