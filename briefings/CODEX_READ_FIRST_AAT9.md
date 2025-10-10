# CODEX READ FIRST ??? AAT9 Optimized Startup



Read and follow this sequence exactly before coding. Goal: highest???quality planning, path???safe execution, and consistent documentation/logging.



## 1) Session Setup

- Model preset: select `gpt-5-codex` (High) by default (Pro). Use Medium only when you prefer lower latency.

- Operate with high reasoning, yolo=false mindset (ask before destructive changes).

- Ensure CWD is the repo root: `C:\dev\Alpha-Analytical-Tool`.

- Print???only sanity: `git status -s`, `git branch -vv`, `git remote -v` (no changes to remotes).

- Confirm launch path: `run_app.bat` ??? `streamlit run src\app.py`.



## 2) Read These (KIT first)

- `docs/AAT9_KIT/AAT9_KIT_README.md` (index)

- `docs/AAT9_KIT/AAT9_Workflow_Standard.md` (step???by???step workflow)

- `docs/AAT9_KIT/Practices/AAT9_Coding_Standards.md` (path???safe coding)

- `docs/AAT9_KIT/Practices/AAT9_Agent_Operating_Rules.md` (guardrails)

- `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md` (daily flow)

- `docs/AAT9_KIT/AAT9_Preflight_Reference.md` (expected outputs)

- `docs/AAT9_KIT/AAT9_Diagrams_Guide.md` (Mermaid updates)

- `docs/AAT9_KIT/AAT9_Unified_Changelog.md` (so you know how to log changes)

- Also skim project rules: `AGENTS.md` and `.codex/AGENTS.universal.md`

- Positional / Aux essentials (new engine context):

  - `docs/AAT9_KIT/important/AAT9_Positional_Pressure.md`

  - `docs/AAT9_DOCS/AAT9_Aux_Tools_Official.md`

  - `docs/AAT9_DOCS/AAT9_Blackapple_Module.md`

- Data contracts recap: Aux/BA -> draws CSVs (`data/cleaned/*_draws.csv`); V-TRAC/Stable/DR -> combined tables (`tables/<STATE>/` or `data/outputs/tables/<STATE>/`) via `utils.path_handler`. Combined is baseline; Midday/Evening are additive variants surfaced alongside Combined.
  - Terminology: use "All-Variant (C+M+E)" when referring to consensus across Combined/Midday/Evening; reserve "Combined" for the combined draw stream.



## 3) Preflight

- Run: `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`
- Add `-CheckDoubles` after data refreshes to run the doubles audit automatically.

- After preflight (or before launching Streamlit), run `python scripts/smoke_winners_logger.py` to verify the analyzer-style winners report still renders with highlights.
- Control Center due-doubles now auto-refreshes when draw CSV snapshots change; still click **Refresh Draw Tables** after a bulk data load to clear any manual overrides.
- When regenerating draw CSVs through the Control Center Aux Draws pipeline, keep “Delete existing draw CSVs before writing” checked so the pipeline purges stale files before writing fresh ones.
- After regenerating draws, optionally run python scripts/tools/validate_aux_doubles.py <STATE> [--no-pairs] [--pairs-window N] to confirm the double and pair badges match the raw CSVs.
- Run python scripts/tools/validate_aux_repeat.py <STATE> [--no-positional] [--window 150] to confirm repeat-watch streaks and positional hard-due tags align with the CSVs.
- Run python scripts/tools/validate_aux_vtrac.py <STATE> [--limit 10] [--window 150] to verify V-TRAC overlays, heatboard stats, and sums analytics against the CSVs.

- Confirm imports resolve to in???repo files and that draws CSVs are present.

- Confirm `.codex/first_boot.log` is the headless Streamlit log target before any automated boot.



## 3.5) Dev Health (fast checks in UI)

- Control Center: toggle Dev Health to see key module bindings (path_handler, vtrac_reference, winner_report_full, blackapple, aux_loaders, pipeline_runner) and tables root inventory.

- Winners Full tile: toggle Dev Health to confirm `modules` binding, canonical vtrac_reference path, builder presence, and per???state combined tables existence.

- When touching Aux wiring, skim `docs/AAT9_KIT/important/DETAIL CODEX LOG.txt` for recent guardrails.



## 3.6) Testing Discipline

- Before coding, run `python scripts/run_acceptance.py --marker smoke` (or `scripts/run_acceptance.ps1 --marker smoke`). If it fails, stop and fix the regression.

- For deeper changes, run the full suite: `python scripts/run_acceptance.py`. Add `--with-doubles-health` when you want the variant audit before pytest.



- Acceptance suite now covers:
  - Aux positional shortlist (Delaware) repeat-endcap regression.
  - Control Center doubles families (Connecticut, Florida) using the frozen 1,000-draw snapshot so merged C/M/E badges cannot return.
  - Digit-reduction reducer/analyzer/overlay flows for Delaware and Florida.
  Fixtures live under `tests/fixtures/acceptance/`.
- Unit guardrails: `pytest tests/test_vtrac_family_ranker_regression.py tests/test_aux_loaders_variants.py tests/test_draw_catalog.py tests/test_long_string_overlay.py tests/test_stable_training_bundle.py` after doubles/loader changes.
- Health helper: `python scripts/health/check_doubles_variants.py [--state STATE]` audits live draws (missing variants, unseen-overdue badges, merged tokens).

- Stress helpers live under `scripts/tools/` (e.g., `stress_positional.py`); use them when touching positional logic.

- Mutation harness (`scripts/tools/mutate_positional.py --dry-run`) shows how to invoke mutmut once installed.

- Update `docs/AAT9_KIT/AAT9_Testing_Roadmap.md` whenever you add or amend tests.

- Install pre-commit hooks (`pre-commit install`) so `py_compile` + smoke acceptance run automatically on commit.



## 4) Plan ??? Implement ??? Verify ??? Document

- Plan: small, explicit; state files to change and why; wait for approval if collaborating.

- Implement: minimal diffs; use `utils.path_handler` for outputs; Aux/BA draws???only.

- Verify: `python -m py_compile`, `python scripts/checks/smoke_positional.py`, import probes, optional headless boot (120s) + `.codex/first_boot.log`.

- Document: update KIT docs if affected; always add a Changelog entry.



## 5) Done Checklist

- App launches from `run_app.bat`; pages render without path errors.

- All changes logged in `AAT9_Unified_Changelog.md`.

- If structure/wiring changed, update Architecture/App Flow docs.



## Notes

- Never write outside the repo; do not modify git remotes.

- Archive???first for cleanup; no deletions; keep changes reversible.



## 1.5) Model preset (if available)

- Select the `gpt-5-codex` preset at High or Medium reasoning depending on task:

  - High: complex wiring, refactors, cross-page integrations

  - Medium: day-to-day coding with balanced latency

- If `gpt-5-codex` is not visible, use `gpt-5 high` and enable the dynamic thinking toggle where supported.



Note: If Aux throws legacy import errors, run python scripts/checks/smoke_aux_vtrac.py and confirm the files listed in docs/AAT9_DOCS/AAT9_Aux_Staging_Manifest.md.










#### Training bundles
- After running Digit Reduction and Analyzer V2 + the winners overlay, open the **Analyzer V2 (DEV)** expander and click **Package training bundle**.
- Control Center now has a **Batch winners + training bundles** expander; paste the Pick3StatsC4 winners list there to run the winners logger across all tracked states and optionally fire the Stable Pattern bundle workflow in one click.
- Select your stamp (defaults to the newest overlay), choose whether to include hits CSV / overlay HTML, and optionally create a zip copy.
- Bundles are written to `data/outputs/analysis/digit_reduction/<STATE>/training_sets/<STAMP>/` with a `manifest.json` listing the files.
- Use the **Delete all training bundles** button to clear the folder before a fresh run if desired.




