# Final Validation Workflow — Changelog (Master Validation)

Purpose: log **workflow-level** changes, “bumpy items”, and follow-ups discovered while running the Master Validation templates (Parts 1–5). This is the place to capture “fix later” items so they don’t get lost across Codex context resets.

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
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`

### Part 3: Aux evidence dump + prompts

- Added a formal Part 3 section to the master template (Aux signals across Combined/Midday/Evening + convergence + expense/mode question).
- Added an Aux sharepack summarizer that snapshots draw CSVs into the sharepack and emits `summary.md`/`summary.json` for paste-ready evidence (no screenshots required).
- Files:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
  - `scripts/tools/aux_sharepack_summary.py`

### Drift guards: tables↔aux alignment (why sentinel checks exist)

- Problem observed: it is possible for **tables** (`data/outputs/tables/...`) and **aux draws** (`data/cleaned/draws/...`) to describe different “world snapshots” after workbook swaps/rebuilds. This can silently invalidate analysis runs.
- Fix: add a fast validator that compares “newest draws” in tables vs aux draws and fails fast on mismatch.
- Files:
  - `scripts/tools/validate_tables_aux_alignment.py`
- How it’s used (two modes):
  - **Live workspace guard** (mutable outputs): `python3 scripts/tools/validate_tables_aux_alignment.py --state <STATE>`
  - **Master Validation guard** (sharepack snapshots): `python3 scripts/tools/validate_tables_aux_alignment.py --date <D> --state <STATE> --strict`
- Why we default to “check a couple states” in preflight:
  - Preflight should be **fast enough that you actually run it**, so it uses sentinel states (CT/FL) to catch systemic drift.
  - This catches global “wrong workbook / stale tables / stale aux draws” problems, but it does **not** guarantee every state is healthy (state-specific issues can still exist).
  - Recommended escalation:
    - Quick: CT/FL sentinel checks (default).
    - Targeted: run alignment for the specific state you are analyzing that day.
    - Full sweep (optional): iterate all tracked states when debugging or before a large batch.

### Run report safety + Part 3 wiring

- Run report generator now includes Part 3 scaffolding and Aux sharepack pointers.
- It refuses to overwrite an existing filled run report unless `--force` is provided (prevents accidental loss of answers).
- Files:
  - `scripts/tools/create_master_validation_run_report.py`

### Blackapple robustness (Aux dependency)

- Fix: prevent a crash when draw streams contain `"000"` placeholders (e.g., missing values normalized by loaders) by allowing root-sum `0` in the internal root tracking map.
- File:
  - `modules/blackapple.py`

---

## 2025-12-17

### Part 4–5: add the “translation layer” + final summary to the master template

- Problem observed: after completing Parts 1–3, there was no canonical way to:
  - freeze a small “candidate universe” per draw (Midday/Evening),
  - map candidates to coverage modes (perm-only vs boxed vs VT-boxed vs VT-straight), and
  - end runs with a consistent “what matters” wrap-up.
- Fix: add **Part 4** (candidate universe + evidence vectors + coverage mapping + pack decision) and **Part 5** (summary + fix-now vs fix-later + next run) to the master template.
- Files:
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

### Run report generator: scaffold Parts 4–5

- Fix: extend the run report generator to scaffold Part 4 + Part 5 so new sessions don’t have to manually add those sections.
- Files:
  - `scripts/tools/create_master_validation_run_report.py`

---

## 2025-12-20

### Brain‑2: export Control Center into sharepacks (drift-proof)

- Added a sharepack-aligned Control Center exporter so Brain‑2 artifacts are frozen alongside Brain‑1 under `sharepacks/<D>/...`.
- Command: `python3 scripts/tools/export_control_center_sharepack.py --date <D>`
- Outputs: `sharepacks/<D>/control_center/` (Blackapple, Due Doubles, VTRAC Repeat Watch + README/meta/report).
- Files:
  - `scripts/tools/export_control_center_sharepack.py`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`
