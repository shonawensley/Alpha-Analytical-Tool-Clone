# Fix‑Now Ledger (Gold Days / Post‑Runs)

Purpose: convert post‑run “negative observations” into an execution list with evidence + acceptance tests, so we can fix correctness issues without spiraling into tuning.

Guiding rule (SSOT): **pipeline integrity ≠ tool outcome**. A tool “missing” a winner can be a legitimate analytic result; a pipeline/semantics bug is when we grade or label the wrong thing, or read the wrong data.

Sources used to seed this ledger (unified):
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/*`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`

## Ledger

| ID | Status | Category | Symptom | Evidence (examples) | Proposed fix | Acceptance test |
|---|---|---|---|---|---|---|
| FN‑001 | Closed | Results parsing / DR overlays | Digit Reduction `Combined` winner sometimes equals a non‑tracked state (e.g., Québec) because the results parser consumes extra digits; also causes confusion on one‑winner days. | `alpha_analytical/control_center/batch_runner.py` (`parse_winner_sheet`, `_collect_digit_reduction_winners`) · `data/results/2025-06-21.txt` / `data/results/2025-06-22.txt` | ✅ Implemented: Control Center results parsing is tab‑aware + diacritic‑robust; removed unsafe DR `Combined` inference from “extra digits”. | Re-run CC batch on gold days: PR/PA `Combined` winner no longer pulls Québec and matches the intended “Combined winner” convention. |
| FN‑002 | Closed | One‑winner days | On days where Midday is blank but Evening exists (e.g., SC 2025‑06‑22), summaries label the sole winner as “Midday”, and other tools may show “Evening unknown”. | `data/results/2025-06-22.txt` (`South Carolina\t\t675`) · `sharepacks/2025-06-22/SouthCarolina4/*/*/summary.json` | ✅ Implemented: summarizers/validators preserve Midday vs Evening from the tabbed results file; DR skips missing periods explicitly. | SC 2025‑06‑22 is represented as `Evening=675` with `Midday` explicitly missing; no “Evening unknown” false alarms. |
| FN‑003 | Closed | Missing results days | Puerto Rico missing from `data/results/2025-06-22.txt` should be treated as explicit “expected N/A”, not corruption. | `data/results/2025-06-22.txt` (no PR line) · `sharepacks/2025-06-22/PuertoRico4/digit_reduction/PuertoRico4/summary.md` | ✅ Implemented: winners-dependent summaries/validators skip grading when the results line is absent. | Validators + run reports treat PR as “missing results (expected)” with no crashes and no cross‑state contamination. |
| FN‑004 | Closed | Alignment guardrail | Aux draws must match the same D‑1 workbook snapshot as tables; drift must be detected early. | `scripts/tools/validate_tables_aux_alignment.py` · Sharepack provenance in `sharepacks/<D>/<STATE>/aux/<STATE>/summary.json` · Gold-days audit: `reports/audit/sharepacks_audit_gold_days.md` | ✅ Implemented: `validate_tables_aux_alignment.py --date <D> --state <STATE> --strict` is documented as a required Master Validation guard in SSOT docs; audit harness runs it in sharepack mode. | Gold-days audit shows `FAIL=0` and strict alignment passes for all tracked states; a failing day produces a clear remediation message (`--regen-aux-draws` path). |
| FN‑005 | Fixed (future) | Table hygiene | `nan**` appears in a Combined table cell for Ohio4 (2025‑06‑22), which is confusing in winners/table lenses. | `sharepacks/2025-06-22/Ohio4/tables/Combined_Combined.csv` (`nan**`) · `sharepacks/2025-06-22/Ohio4/json/Ohio4_tables.json` | ✅ Implemented (future): table generation treats NaN as empty and avoids applying `*`/`**` markers to empty cells. | No `nan**` strings appear in newly generated tables/JSON; existing sharepacks are not retro-rewritten. |
| FN‑006 | Closed | Naming consistency | State naming drift (e.g., Ontario4 vs OntarioCanada4) can cause silent “zero output” bugs if a script globs the wrong label. | Post‑runs notes in `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/*` · `alpha_analytical/control_center/batch_runner.py` (`_PROJECT_STATE_CANDIDATES`) · `scripts/tools/freeze_sharepack_day.py` · Gold-days audit: `reports/audit/sharepacks_audit_gold_days.md` | ✅ Implemented: sharepack freezer now fails fast if required Stable artifacts are missing for a tracked state, with a naming-drift hint. | Attempting to freeze a day where Stable outputs are missing for a tracked state is a hard error (caught during build, not days later). |
| FN‑007 | Closed | DR “0‑item overlay” semantics | When `winner_stamp.items_total=0`, empty `winner_flags.csv`/`winner_hits.csv` were being labeled as “missing” in summaries, which reads like corruption. | Example: `sharepacks/2025-06-22/OntarioCanada4/digit_reduction/OntarioCanada4/summary.json` (Evening winner 616 has `items_total=0`) | ✅ Implemented: DR summary treats empty flags/hits as expected when `items_total=0`. | Running `scripts/tools/dr_sharepack_summary.py` for Ontario 2025‑06‑22 produces `gaps=[]` for Evening when `items_total=0`. |

## Notes / triage rules

- If an item changes *how a tool works*, it is **Fix‑Later** unless it’s demonstrably a correctness bug.
- If an item only changes *reporting/labeling/evaluation semantics*, it is usually **Fix‑Now** (high leverage, low risk).
