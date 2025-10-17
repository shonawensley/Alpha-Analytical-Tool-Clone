# AAT9 Testing Roadmap

This document tracks the automated verification layers that protect AAT9. Treat it as the single source of truth for which flows are covered, what scripts to run, and what remains on the backlog.

## 1. Acceptance Suite (pytest)
- Harness: `scripts/run_acceptance.py` (PowerShell wrapper: `scripts/run_acceptance.ps1`)
- Markers:
  - `acceptance` - full end-to-end scenarios.
  - `smoke` - fast subset used by pre-commit.
- Current coverage:
  - `tests/acceptance/test_positional_delaware.py` - validates the Aux positional shortlist for Delaware (repeat-endcap 545, top combos).
  - `tests/acceptance/test_control_center_doubles.py` - verifies Streamlit renders per-variant doubles tokens for the Connecticut/Florida snapshot (no merged C/M/E badges).
  - `tests/acceptance/test_digit_reduction_delaware.py::test_digit_reduction_pipeline_delaware` - runs reducer + analyzer on Delaware fixtures and checks score/artifact outputs.
  - `tests/acceptance/test_digit_reduction_delaware.py::test_digit_reduction_winner_overlay_delaware` - exercises the batch overlay to ensure maps, flags, and stamp JSON land beside analyzer outputs.
- Unit regression:
  - tests/test_vtrac_family_ranker_regression.py keeps the doubles-family ranker aligned with the CT/FL snapshot (no merged badges, unseen handling).
  - tests/test_aux_loaders_variants.py locks the combined/midday/evening file resolution logic.
  - tests/test_vtrac_matchers.py verifies winner/family hits plus VT-straight strict/value-block spans.
  - tests/test_winners_renderer.py checks the legend/classes rendered in the analyzer-style report.
  - tests/test_draw_catalog.py locks the draw snapshot hashing and newest-first double detection used by Control Center due-doubles + positional hard-due cues.
- tests/test_long_string_overlay.py ensures the long-string Digit-Reduction windows stay highlighted in the V-TRAC tables.
- tests/test_batch_runner.py keeps the Pick3StatsC4 state parser aligned with the Control Center batch workflow.
- tests/test_draws_refresh.py ensures the Control Center draw purge removes the expected CSVs before regeneration.
- tests/test_aux_validation.py covers Aux double thresholds, pair severity, multi-variant alerts, family badge extraction, repeat-watch streaks, positional hard-due flags, V-TRAC overlays/heatboard stats, and sums analytics.
- tests/test_digit_training_bundle.py locks the Analyzer V2 training bundle defaults (Midday/Evening) plus the Combined opt-in and error handling for missing artifacts.
- tests/test_stable_doubles_adjacency_negative.py ensures Stable doubles support only fires when consensus digits share a column, protecting the Control Center evidence bus from false positives.
- tests/test_vtrac_evidence.py + tests/test_vtrac_enhanced_basic.py cover the shared V-TRAC evidence layer and enhanced analyzer scoring (top index straight rationale). CLI smoke: `python tools/vtrac_enhanced_cli.py --state SampleState --tables-root tests/fixtures/vtrac --analysis-root tests/fixtures/tmp_out`.
- Batch smoke (optional): use the helper script in `analysis_2` (“temp_run_vtrac.py”) to iterate all states and refresh `data/outputs/analysis/vtrac/analysis_summary.json` (top 5 indices/straights per state).


- Pending additions:
  - V-TRAC analyzer render path (uses combined tables only).
  - Blackapple alert flow (ensures triggers/candidates render for a known state).
  - Control Center state toggle stress case.`r`n- Re-verify due-doubles combination tagging so M/E/C flags only light up when the combo is actually late in that variant (current tables still show every combo with all three tags).

## 2. Stress Harnesses
- `scripts/tools/stress_positional.py`
  - Replays the positional analyzer multiple times using fixtures or live draws, logging throughput to spot regressions.
- Next candidates:
  - Digit Reduction pipeline stress (re-run reducer/analyzer with varying states).
  - Control Center state toggle spam (simulate rapid UI interactions).

## 3. Mutation Testing
- Entry point: `scripts/tools/mutate_positional.py` (wraps `mutmut` against the shortlist scorer).
- Status: optional manual run; install with `pip install mutmut` before use.
- Future scope: expand to other high-risk modules once acceptance coverage stabilises.

## 4. Pre-commit Hooks
- Config: `.pre-commit-config.yaml`
  - `py-compile` - runs `py_compile` on staged Python files.
  - `pytest-smoke` - invokes `scripts/run_acceptance.py --marker smoke` with `--maxfail 1`.
- Install locally with `pre-commit install`.

## 5. Health Helpers (still required)
- `.codex/preflight.ps1` - environment sanity before coding (add `-CheckDoubles` after data refreshes to run the doubles audit).
- Streamlit Dev Health expanders - confirm module bindings and data sources.
- `python scripts/health/check_doubles_variants.py [--state STATE]` - post-import audit for missing variant files, unseen-overdue combos, or merged badges. Set `AAT9_RUN_DOUBLES_HEALTH=1` to enable this audit inside the pre-commit smoke hook.

## 6. Backlog / TODOs
- Acceptance scenarios for each major module (see section 1 Pending additions).
- Broaden digit reduction acceptance fixtures beyond Delaware (more states, overlay expectations).
- Promote enhanced V-TRAC analyzer after A/B versus legacy; wire Control Center toggles to consume JSON summaries.
- Evaluate browser-level smoke tests (Playwright) once core flows are locked.

Keep this file up to date whenever you add or expand tests so future sessions know the current safety net.















