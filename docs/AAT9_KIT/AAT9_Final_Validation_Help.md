# AAT9 Final Validation – Hands-On Guide (Tables → Winners → DR Batch)

Purpose: A single reference for running historical/backtest examples safely and repeatably (fresh tables, day-ahead results, winners HTML/JSON, and Digit Reduction outputs). Use this when swapping Excel workbooks and generating analysis artifacts for reverse-engineering wins.

Repo root (WSL): `/home/ser/code/Alpha-Analytical-Tool-Clone`

Tracked states (tables present): CT, DE, FL, IN, MI, NJ, NY, NC, OH, OntarioCanada, PA, PR, SC, VA. (GA/TX not tracked; skip to avoid errors.)

Related SOPs/refs:
- Tables: `docs/AAT9_KIT/AAT9_String_Table_Testing.md`
- Preflight/guards: `docs/AAT9_KIT/AAT9_Master_Validation_Preflight.md`, `docs/AAT9_KIT/AAT9_Batch_Workflow_SOP.md`
- Lean outputs per tool: `docs/AAT9_KIT/AAT9_Analyzer_Lean_Outputs.md` (Digit Reduction notes below)
- Quick validation helpers:
  - Table naming check (no file changes): `PYTHONPATH=.:src python3 scripts/tools/validate_tables_naming.py --json-out tables_naming.json`
  - Stable winners-in-spotlight check: `PYTHONPATH=.:src python3 scripts/tools/validate_stable_winners.py --sharepack sharepacks/<DATE>/<STATE>/stable/<STATE>`
  - Stable sharepack summarizer (Markdown/JSON for Part 2): `python3 scripts/tools/stable_sharepack_summary.py --sharepack sharepacks/<DATE>/<STATE>/stable/<STATE> --md-out summary.md --json-out summary.json`
    - Paste the Markdown into Part 2 before answering the tool questions; it already shows canonical mapping, per-output evidence, 4-criteria counts, and coverage gaps.
  - Digit Reduction winner check: `PYTHONPATH=.:src python3 scripts/tools/validate_dr_winners.py --sharepack sharepacks/<DATE>/<STATE>/digit_reduction/<STATE>`
  - Digit Reduction sharepack summarizer: `python3 scripts/tools/dr_sharepack_summary.py --sharepack sharepacks/<DATE>/<STATE>/digit_reduction/<STATE> --md-out summary.md --json-out summary.json`
    - Paste the Markdown into Part 2 before answering; includes per-output labels (flags/hits/per_item/top/reducer) and canonical mapping.
  - V-TRAC sharepack summarizer: `python3 scripts/tools/vtrac_sharepack_summary.py --sharepack sharepacks/<DATE>/<STATE>/vtrac/<STATE> --md-out summary.md --json-out summary.json`
    - Analyzer-only bundle: lists top indices/straights and section summaries with source labels (from enhanced JSON). If winner_map/flags are present in a bundle, extend the summarizer to include them.

---

## Master Validation Docs — Quick Index

When starting a new master validation session, use this file as ENTRY, then fan out to:

- **Core wiring & workflow**
  - `docs/AAT9_KIT/AAT9_KIT_README.md`
  - `docs/AAT9_KIT/AAT9_Workflow_Standard.md`
  - `docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md`
  - `docs/AAT9_KIT/AAT9_Master_Validation_Preflight.md`
  - `docs/AAT9_KIT/AAT9_Data_Validation_Workflow.md`
  - `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`
  - `docs/AAT9_KIT/AAT9_Macro_Roadmap.md`

- **Tool analysis logs**
  - Digit Reduction: `docs/AAT9_KIT/AAT9_Digit_Analysis_Log_Part2.md`
  - Stable Pattern: `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md`
  - V-TRAC Analyzer: `docs/AAT9_KIT/AAT9_VTRAC_Analyzer_Analysis_Log.md`
  - Hot Zones: `docs/AAT9_KIT/AAT9_Hot_Zones_Validation_Log.md`

- **Roadmaps / checkpoints / cross-tool insights**
  - `docs/AAT9_KIT/AAT9_Aux_Roadmap.md`
  - `docs/AAT9_KIT/AAT9_Checkpoint_Log.md`
  - `docs/AAT9_KIT/AAT9_Unified_Changelog.md`
  - `docs/AAT9_KIT/AAT9_Analysis_Insights.md`

- **Central winners / aggregator**
  - `docs/AAT9_KIT/AAT9_Winners_Module.md`
  - `docs/AAT9_KIT/AAT9_Winners_VTrac_Report.md`

- **Onboarding / high-level context**
  - `docs/AAT9_KIT/HUMAN_READ_FIRST_AAT9.md`
  - `docs/AAT9_KIT/AAT9_Onboarding_Compass.md`

For deeper module-architecture context (optional but useful when designing the aggregator), see:
- `docs/AAT9_DOCS/ARCHITECTURE_AAT9.md`
- `docs/AAT9_DOCS/module_A_stable_extractor.md`
- `docs/AAT9_DOCS/module_B_digit_reduction.md`
- `docs/AAT9_DOCS/module_C_hot_zones.md`
- `docs/AAT9_DOCS/module_D_aggregator.md`
- `docs/AAT9_DOCS/AAT9_Roadmap_2025-09-03_Winners_Logging_and_Health.md`

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
   - Guard check: Set1/Draw1 in Combined_Combined matches the **history** workbook’s most recent draw; results will always be history+1 day (so we never reuse stale tables).
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

### DR outputs vs. sharepacks (multi-day runs)
- Live DR outputs under `data/outputs/analysis/digit_reduction/<STATE>/…` always reflect the **latest** run for that state (they are not date-versioned on disk).
- For multi‑workbook backtests or when you want a permanent snapshot per day, use dated DR sharepacks under `sharepacks/DR_<RESULTS_DATE>/`:
  - Each sharepack contains reducer/analyzer/overlay outputs per state plus the matching winners HTML/JSON, and a `manifest.json` recording `history_date` and `results_date`.
  - When comparing different Excel files/dates, prefer reading from these sharepacks instead of assuming `data/outputs/analysis/digit_reduction/<STATE>` holds multiple days at once.
  - If you re-run DR for a given date, it is safe; live outputs are overwritten, while existing sharepacks remain as historical snapshots.

## Minimal Manual QA (per run)
- Tables fresh? Manifest timestamp matches history file; Combined_Combined present for tracked states.
- Day-ahead rule? Results date = history date + 1; winners HTML/JSON present under that results date.
- DR complete? Training JSON exists; analyzer `per_item/top/meta` exist; overlays present. No errors in batch printout.

## Pointers
- WSL canonical paths: repo root `/home/ser/code/Alpha-Analytical-Tool-Clone`, GitHub Desktop view `\\wsl$\\Ubuntu\\home\\ser\\code\\Alpha-Analytical-Tool-Clone`.
- Docs with more detail: `docs/AAT9_KIT/AAT9_String_Table_Testing.md`, `docs/AAT9_KIT/AAT9_Master_Validation_Preflight.md`, `docs/AAT9_KIT/AAT9_Digit_Analysis_Log.md`.
- Extended Set1 ladder (Draw2–Draw7 cols 6→1) is ON by default (`AAT9_DR_EXTENDED_SET1=1`). Leave ON unless troubleshooting.
- Stage 1 tables/JSON are the single source of truth for **all** tools (Stable, V‑TRAC, Digit Reduction, Aux, Hot Zones). When swapping Excel workbooks, always re-run Stage 1 before any tool/batch so every analyzer sees fresh datasets. For Aux/compound features that operate on draws (not tables), ensure the draws were generated from the same history workbook/date used here before comparing outputs.

---

## Aggregator TODO / Hooks to Review (for Master Validation Kickoff)

There are small “hooks” and follow-ups scattered across the KIT and AAT9_DOCS that are relevant when designing the final aggregator / master validation. At the start of a new master validation session:

1. **Scan the following for “Next / Follow-ups / TODO” sections:**
   - `docs/AAT9_KIT/AAT9_Analysis_Insights.md`
   - `docs/AAT9_KIT/AAT9_Digit_Analysis_Log_Part2.md`
   - `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md`
   - `docs/AAT9_KIT/AAT9_VTRAC_Analyzer_Analysis_Log.md`
   - `docs/AAT9_KIT/AAT9_Hot_Zones_Validation_Log.md`
   - `docs/AAT9_KIT/AAT9_Aux_Roadmap.md`
   - `docs/AAT9_KIT/AAT9_Checkpoint_Log.md`
   - `docs/AAT9_DOCS/AAT9_Roadmap_2025-09-03_Winners_Logging_and_Health.md`

2. **Build a small “Open hooks to consider in aggregator” list**, including for example:
   - Aux V-TRAC index summary (“which index is due”) based on `cached_aux_analysis(state)["vstat"]` and thresholds in `core/aux_config.py` (can become both a UI summary and an Aux feature via `aux_features.extract`).
   - Any Stable/V-TRAC/Hot Zones cross-signals that were explicitly called out (e.g., shared VT families, late-column overlaps, or common “hot zones” across tools).

3. **Use that list during aggregator design** to decide which of these hooks should:
   - Become explicit features in each tool’s lean outputs or Aux feature extractor.
   - Be surfaced in Control Center UI (summaries like “which index is due”, “which state is in a prime environment today”).

This kickoff step means you don’t have to remember every micro-insight from past sessions; instead, the relevant hooks are gathered into a short TODO list that can be addressed systematically as you wire the master validation and final workflow.

***CLARIFYING WORKFLOW PROCESSES FOR FASTSTART****


Read all requested KIT docs. Key takeaways for running and backtesting efficiently (and why the Ontario run failed mid-way):

  - History → results: Use the one-day-ahead rule (history 2025-06-20 → results 2025-06-21). The easiest path is the one-shot wrapper run_history_and_results.py (Master Validation Preflight), which activates the history workbook,
    rebuilds tables/JSON, and generates winners HTML/JSON in one go (CT/FL guard check included).
  - Tables are the SSOT: always rebuild via run_tables_with_guard.py when you swap a Pick3StatsC4 workbook. Verify tables_manifest.json and Set1/Draw1 cols in Combined CSV. Winners must be generated from the matching results
    file.
  - Batch SOP: In app, paste the full winners list and toggle tools (winners logger, Stable, DR, etc.). Headless equivalents: run_stable_from_results.py, generate_winners_from_results.py, DR batch runner, VTRAC share bundle, Hot
    Zones CLI. Use bundle stamps for stable/DR bundles.
  - Lean outputs per tool (what to collect in sharepack):
      - DR: per_item/top/meta + stacked HTML; overlays/winners flags are optional diagnostics; training logs required.
      - Stable: scores/families/compound/metrics + winner spotlight CSVs.
      - VTRAC: compact report + analyzer bundle (lean pass pending); share bundle via run_vtrac_share_bundle.py.
      - Hot Zones: per_lane/top_lanes/meta + winner_map.
      - Winners logger (centralized module is the goal): per-date winners map/flags/HTML in reports/stable/winners_by_date/<DATE>/.
  - Guardrails/pitfalls: canonical paths via utils.path_handler; Aux/BA draw-only; no GA/TX tables; use preflight; acceptance/tests cover loaders, batch runner, doubles/variants, etc.
  - Quickstart/verification: table swap checklist + Set1 guard; batch workflow SOP mirrors production; testing roadmap lists available smokes/acceptance.

  For the Ontario run: I rebuilt tables and winners (2025-06-21 results) and ran DR across all states (GA/TX missing tables as expected). Stable failed for Ontario because run_stable_from_results defaulted to label
  “OntarioCanada”; the results file uses “Ontario”. Re-run with --results-label Ontario after tables/winners are set; collect Stable outputs into the sharepack. Next, run VTRAC and Hot Zones for Ontario, then assemble
  sharepacks/2025-06-21/OntarioCanada4/ with tables/JSON, winners HTML/JSON, DR (per_item/top/meta + overlays), Stable bundle, VTRAC compact/analyzer, and Hot Zones lane maps.

  If you want, I’ll re-run Ontario end-to-end now using the one-shot wrapper, then individual tool CLIs (Stable with --results-label Ontario, VTRAC bundle, Hot Zones CLI) and package the sharepack.


› OK would you say now you have a much clearer understanding of how to run all these processes after reviewing those documents ? It seems you do Obviously you can probably understand my frustration of having to waste a lot of
  context just to get you to understand that now I'm trying to figure out a way avoid that in the future Can you do me a quick favor and review the master validation documents like anything was like final validation wording in
  it I thought that we had tried to find a way to ensure that could be like shortcuts to understanding this and if that's not the ideal way maybe there's gotta be like something that can be written in the final validation hulk
  about which documents should be reviewed to make this more efficient do you get what I mean by this ? Please consider this and provide your comprehensive feedback


• Yes—after the doc sweep I’m confident on running all the core processes (tables/JSON, winners, batch tools, lean outputs, sharepacks). I get the frustration on context churn. There are already “shortcut” docs, but I can tighten
  them further so future sessions don’t need the full tour.

  Current best shortcuts:

  - ENTRY: docs/AAT9_KIT/AAT9_Final_Validation_Help.md (quick index + Stage 1/2/3 commands).
  - Checklist: docs/AAT9_KIT/AAT9_Final_Validation_Checklist.md (guards, day-ahead rule, DR live vs sharepack).
  - Batch SOP: docs/AAT9_KIT/AAT9_Batch_Workflow_SOP.md (swap workbook → tables → results → batch → outputs).
  - Lean outputs: docs/AAT9_KIT/AAT9_Analyzer_Lean_Outputs.md (what to collect per tool).
  - Table swap/guards: docs/AAT9_KIT/AAT9_Table_Swap_Verification.md + AAT9_Master_Validation_Preflight.md.
  - Quickstart: docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md (paths, commands, common checks).

  What I’d suggest to make this even lighter:

  - Add a 1–2 page “Master Validation Faststart” section inside AAT9_Final_Validation_Help.md that simply lists:
      1. One-shot command (run_history_and_results.py --history-date YYYY-MM-DD).
      2. If manual: tables cmd, winners cmd, batch cmds (Stable with --results-label when state name differs), DR batch snippet, VTRAC bundle, Hot Zones CLI.
      3. What to put in a sharepack (per tool, per date, per state).
      4. Links to the lean outputs spec and batch SOP for detail.
  - Keep a tiny “Resets Pack” list at the top of AAT9_Final_Validation_Checklist.md naming just the 4–5 docs above so we don’t re-read everything.
  - Add a note in Final Validation Help about state label mismatches (e.g., --results-label Ontario for OntarioCanada4) to avoid the Stable miss we just hit.

  If you want, I can edit Final_Validation_Help/Checklist to include that Faststart and doc list so future sessions jump in without burning context.

Faststart addendum (to use directly)

- One-shot, recommended: `PYTHONPATH=.:src python3 scripts/tools/run_history_and_results.py --history-date YYYY-MM-DD` (activates workbook, rebuilds tables/JSON, generates winners day-ahead).  
- Manual steps if needed:  
  1) Tables: `PYTHONPATH=.:src python3 scripts/tools/run_tables_with_guard.py --history-file Pick3StatsC4_YYYY-MM-DD.xlsm`  
  2) Winners: `PYTHONPATH=.:src python3 scripts/tools/generate_winners_from_results.py --results-file data/results/YYYY-MM-DD.txt --out-dir reports/stable/winners_by_date/YYYY-MM-DD/`  
  3) Stable (when state label differs, pass `--results-label`, e.g., `Ontario`): `PYTHONPATH=.:src python3 scripts/tools/run_stable_from_results.py --state <STATE> --results-file ... [--results-label LABEL] [--write-bundle]`  
  4) DR batch: run the inline snippet in this doc (AAT9_DR_EXTENDED_SET1=1) with the winners file.  
  5) VTRAC bundle: `python TOOLS/run_vtrac_share_bundle.py` (refreshes compact report/summary).  
  6) Hot Zones: `python scripts/hot_zones/run_hot_zones_cli.py --state <STATE> --date YYYY-MM-DD --json data/outputs/json_tables/<STATE>_tables.json --out-dir data/outputs/analysis/hot_zones/<STATE>`.
- Sharepack contents (per date/state): tables CSV + JSON tables; winners HTML/JSON; DR per_item/top/meta (+ overlays if captured) + training log; Stable scores/families/compound/metrics + winner spotlight; VTRAC compact/analyzer bundle; Hot Zones per_lane/top_lanes/meta + winner_map.
- Resets pack (docs to skim after a context reset):  
  - AAT9_Final_Validation_Help.md (this file)  
  - AAT9_Final_Validation_Checklist.md (guards/day-ahead/DR live vs sharepack)  
  - AAT9_Batch_Workflow_SOP.md (swap → tables → results → batch → outputs)  
  - AAT9_Analyzer_Lean_Outputs.md (what to collect)  
  - AAT9_Table_Swap_Verification.md + AAT9_Master_Validation_Preflight.md (Set1 guard, manifests)  
  - AAT9_Quickstart_Cheat_Sheet.md (paths/commands)
- Label mismatch note: if the results file uses a label that differs from the state key (e.g., “Ontario” vs “OntarioCanada4”), pass `--results-label` to Stable so winners are found; reuse the same results file for DR/VTRAC/Hot Zones.
