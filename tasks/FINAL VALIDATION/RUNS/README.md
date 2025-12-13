# Master Validation — Run Reports

This folder stores **filled, per‑example** master validation reports so we don’t lose track across sessions.

- The canonical question template lives in: `tasks/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
- A run report is a *snapshot for one state + one history date* with:
  - Links to the sharepack artifacts
  - Embedded per‑tool summarizer Markdown blocks (Stable/DR/VTRAC/Hot Zones)
  - Placeholders to fill Part A + Part 2 answers in one place

Generate a new run report (recommended):
```bash
python3 scripts/tools/create_master_validation_run_report.py --date YYYY-MM-DD --state OntarioCanada4
```

Default output:
`tasks/FINAL VALIDATION/RUNS/YYYY-MM-DD__<STATE>.md`
