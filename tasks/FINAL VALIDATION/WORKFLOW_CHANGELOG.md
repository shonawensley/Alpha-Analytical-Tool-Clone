# Final Validation Workflow — Changelog (Master Validation)

Purpose: log **workflow-level** changes, “bumpy items”, and follow-ups discovered while running the Master Validation templates (Parts 1–3). This is the place to capture “fix later” items so they don’t get lost across Codex context resets.

Scope: docs, sharepack helpers (summarizers/validators/run-report generator), and workflow contracts. Avoid changing core analyzers/scorers unless explicitly approved.

---

## 2025-12-13

### Digit Reduction: clarify “any vs final” semantics (SSOT = winner stamp JSON)

- Problem observed: `winner_hits.csv` was misread as if the “winner” must appear in `final_value`. In reality:
  - “Any” matches (e.g., `exact_any`, `vtrac_any`) are reflected in `winner_flags.csv` (`dr_win_*`) and in `*_winner_stamp.json` `counts`.
  - “Final” matches (e.g., `exact_final`, `vtrac_final`) are reflected in `winner_hits.csv` `final_*_match` columns and in `*_winner_stamp.json` `counts`.
  - It is valid for an example to have strong `*_any` counts but **zero** `*_final` counts.
- Impact: Part 2 DR summaries/validators can look “broken” unless the semantics are explicit.
- Fix: update DR summarizer + validator to use `*_winner_stamp.json` as the semantic anchor and to report totals correctly (no `final_value == winner` filtering).
- Files:
  - `scripts/tools/dr_sharepack_summary.py`
  - `scripts/tools/validate_dr_winners.py`

### VTRAC: guard against empty compact report

- Problem observed: `sharepacks/<DATE>/vtrac_compact_report.json` can exist but contain empty `states=[]` and `sections=[]`, which silently breaks aggregator-style reads.
- Fix: add a validator to flag “missing or empty compact report” early in the workflow.
- Files:
  - `scripts/tools/validate_vtrac_compact_report.py`

### Workflow contract clarity

- Clarify that `sharepacks/<DATE>/...` uses the **results/winners date (D)** and the history workbook is typically **D-1**.
- Add “Contract Truth Table” + “Known bumpy semantics” to the entry doc so future sessions don’t have to rediscover these rules.
- Files:
  - `docs/AAT9_KIT/AAT9_Final_Validation_Help.md`

### Part 3: Aux evidence dump + prompts

- Added a formal Part 3 section to the master template (Aux signals across Combined/Midday/Evening + convergence + expense/mode question).
- Added an Aux sharepack summarizer that snapshots draw CSVs into the sharepack and emits `summary.md`/`summary.json` for paste-ready evidence (no screenshots required).
- Files:
  - `tasks/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
  - `scripts/tools/aux_sharepack_summary.py`

### Run report safety + Part 3 wiring

- Run report generator now includes Part 3 scaffolding and Aux sharepack pointers.
- It refuses to overwrite an existing filled run report unless `--force` is provided (prevents accidental loss of answers).
- Files:
  - `scripts/tools/create_master_validation_run_report.py`

### Blackapple robustness (Aux dependency)

- Fix: prevent a crash when draw streams contain `"000"` placeholders (e.g., missing values normalized by loaders) by allowing root-sum `0` in the internal root tracking map.
- File:
  - `modules/blackapple.py`
