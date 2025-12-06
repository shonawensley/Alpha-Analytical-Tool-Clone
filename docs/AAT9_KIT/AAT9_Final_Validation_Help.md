# AAT9 Final Validation – Hands-On Guide (Tables → Winners → DR Batch)

Purpose: A single reference for running historical/backtest examples safely and repeatably (fresh tables, day-ahead results, winners HTML/JSON, and Digit Reduction outputs). Use this when swapping Excel workbooks and generating analysis artifacts for reverse-engineering wins.

Repo root (WSL): `/home/ser/code/Alpha-Analytical-Tool-Clone`

Tracked states (tables present): CT, DE, FL, IN, MI, NJ, NY, NC, OH, OntarioCanada, PA, PR, SC, VA. (GA/TX not tracked; skip to avoid errors.)

Related SOPs/refs:
- Tables: `docs/AAT9_KIT/AAT9_String_Table_Testing.md`
- Preflight/guards: `docs/AAT9_KIT/AAT9_Master_Validation_Preflight.md`, `docs/AAT9_KIT/AAT9_Batch_Workflow_SOP.md`
- Lean outputs per tool: `docs/AAT9_KIT/AAT9_Analyzer_Lean_Outputs.md` (Digit Reduction notes below)

Tool quick index — Digit Reduction
- Entrypoints: reducer `src/core/module_b_digit_reduction.py`; analyzer V2 `alpha_analytical/digit_reduction/analyzer_v2/*`; batch runner `alpha_analytical/control_center/batch_runner.py` (`run_digit_reduction_workflow`).
- Inputs: combined tables under `data/outputs/tables/<STATE>/`; JSON mirrors under `data/outputs/json_tables/<STATE>_tables.json` (tables remain the SSOT for DR). Tracked states only (CT, DE, FL, IN, MI, NJ, NY, NC, OH, OntarioCanada, PA, PR, SC, VA).
- Outputs: reducer HTML/CSV + training (`.../training/<STATE>_digit_reduction_logs.json` required, steps CSV optional); analyzer bundle (`.../analyzer_v2/per_item.csv`, `top_candidates.csv`, `meta.json`, stacked HTML) with `score_v2`/`lockscore_v2`/`final_prob`/`lockscore_prob` populated; overlays under `.../analyzer_v2/winners/`.
- Config highlights: extended ladder ON by default (kill-switch flag); progression feature (`ls2_progress`) emitted with light weights (near=0.02, far=0.01) and adjustable; LS2/VT-only boosts, funnel/ls_col_42 telemetry intact; optional `drop_only_multiplier` guard in `scoring_v2.guards` (default 1.0, currently 0.9) that gently down-weights pure drop-vtrac-only boxes.

## Quick Checklist (per workbook)
1) Stage 0 (CWD sanity): `pwd` → must be repo root. `git status -sb` (print only).
2) Stage 1 (Tables + JSON mirrors):
   - `PYTHONPATH=.:src python3 scripts/tools/run_tables_with_guard.py --history-file Pick3StatsC4_YYYY-MM-DD.xlsm`
   - Confirm manifest: `data/outputs/tables/tables_manifest.json` (mtime/size matches the history workbook).
   - Confirm tables: `data/outputs/tables/<STATE>/{Combined_Combined,Midday_Combined,Evening_Combined}.csv`
   - Confirm JSON mirrors: `data/outputs/json_tables/<STATE>_tables.json`
   - Guard check: Set1/Draw1 in Combined_Combined matches the history date; results will be day+1.
3) Stage 2 (Winners HTML/JSON, day-ahead results):
   - Results file = history date + 1 (e.g., history 2025-06-21 → results `data/results/2025-06-22.txt`).
   - `PYTHONPATH=.:src python3 scripts/tools/generate_winners_from_results.py --results-file data/results/YYYY-MM-DD.txt --out-dir reports/stable/winners_by_date/YYYY-MM-DD/`
   - Verify winners HTML/JSON exist under `reports/stable/winners_by_date/<RESULTS_DATE>/<STATE>/`.
   - Optional sanity: spot-check winners HTML against Combined_Combined Set1/Draw1 sequence for CT/FL.
4) Stage 3 (Digit Reduction batch, extended ladder ON by default):
   - `PYTHONPATH=.:src AAT9_DR_EXTENDED_SET1=1 python3 - <<'PY'`
     ```python
     from pathlib import Path
     from alpha_analytical.control_center.batch_runner import parse_winner_sheet, filter_tracked, run_digit_reduction_workflow
     text = Path("data/results/YYYY-MM-DD.txt").read_text(encoding="utf-8")
     entries = filter_tracked(parse_winner_sheet(text))
     res = run_digit_reduction_workflow(entries,
                                        run_reducer=True,
                                        run_overlay=True,
                                        run_analyzer=True,
                                        run_bundle=False,
                                        mirror_to_winners=True,
                                        include_overlay_html=True)
     print(res)
     ```
   - Expected outputs per state:
     - Reducer: `data/outputs/analysis/digit_reduction/<STATE>/...digit_reduction_report*.html`, `..._scores.csv`
     - Training: `.../training/<STATE>_digit_reduction_logs.json` (required) + steps CSV
     - Analyzer: `.../analyzer_v2/<STATE>_analyzer_v2_{per_item,top_candidates,meta}.csv/json`
     - Overlays: `.../analyzer_v2/winners/` (maps/flags/overlay HTML)
   - If a state errors, check that its tables exist (GA/TX will error because no tables).

## Minimal Manual QA (per run)
- Tables fresh? Manifest timestamp matches history file; Combined_Combined present for tracked states.
- Day-ahead rule? Results date = history date + 1; winners HTML/JSON present under that results date.
- DR complete? Training JSON exists; analyzer `per_item/top/meta` exist; overlays present. No errors in batch printout.

## Pointers
- WSL canonical paths: repo root `/home/ser/code/Alpha-Analytical-Tool-Clone`, GitHub Desktop view `\\wsl$\\Ubuntu\\home\\ser\\code\\Alpha-Analytical-Tool-Clone`.
- Docs with more detail: `docs/AAT9_KIT/AAT9_String_Table_Testing.md`, `docs/AAT9_KIT/AAT9_Master_Validation_Preflight.md`, `docs/AAT9_KIT/AAT9_Digit_Analysis_Log.md`.
- Extended Set1 ladder (Draw2–Draw7 cols 6→1) is ON by default (`AAT9_DR_EXTENDED_SET1=1`). Leave ON unless troubleshooting.
