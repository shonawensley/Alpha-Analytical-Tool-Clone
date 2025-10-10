# AAT9 ??? Analysis Insights

## Role & Scope
- Captures the analytical signals and pattern-recognition features implemented across AAT9 so every tool can reuse them without re-deriving the wiring.
- Complements `AAT9_Live_Wiring_and_Data_Paths.md` (routes) and `AAT9_Testing_Roadmap.md` (guardrails) by documenting *what* we detect, *why*, and *where* the logic lives.
- Use this doc whenever you add or modify analysis logic in Analyzer V2, Winners, Stable Pattern, Aux scoring, Hot Zones, or future modules.

## Signal Reference

| Signal | Purpose | Implementation | Surfaces | Guardrails | Notes / TODO |
| --- | --- | --- | --- | --- | --- |
| Winner permutations (strict + gap????????1) | Highlight winner digits even with a stray digit in the string. | `modules/vtrac_matchers.collect_spans` (`winner_strict`, `winner_gap`). | Analyzer tables (`src/core/module_c_vtrac.py`), compact winners (`src/core/winners_vtrac_report.py`), full winners report (`modules/winner_report_full.py`). | `tests/test_vtrac_matchers.py::test_analyze_cell_returns_winner_and_family_hits`; smoke `scripts/smoke_winners_logger.py`. | Ensure Stable/Hot Zones import the shared helper instead of substring matching. |
| VT-straight strict | Flag AABB/BBAA runs aligned with the winner????????s VT pair (blue solid). | `modules/vtrac_matchers._vt_straight_spans` strict branch. | Analyzer tables, compact winners, digit-reduction overlay. | `tests/test_vtrac_matchers.py::test_collect_spans_marks_vt_straight_strict`; renderer legend (`tests/test_winners_renderer.py`). | Reuse when Stable extractor formalises three-value runs. |
| VT-straight value-block | Catch straights hidden by a run of foreign digits (blue dashed). | `_vt_straight_spans` tolerant branch. | Same surfaces as above. | `tests/test_vtrac_matchers.py::test_collect_spans_marks_vt_straight_gap`; smoke script. | Watch long-run edge cases (e.g., 9444005) during Stable extractor work. |
| Index-family combos | Highlight VT family hits (purple solid/dashed). | `collect_spans` (`family_strict`, `family_gap`). | Analyzer tables, compact winners, overlay. | Existing matcher assertions; renderer legend test. | Fold into Aux scoring weights when compound features consume family counts. |
| Cross-variant consensus | Keep Combined/Midday/Evening alignment transparent. | `module_c_vtrac.load_state_data`, Control Center dev health. | Analyzer output, Control Center tables, future scoring dashboards. | `tests/test_aux_loaders_variants.py`; preflight table checks. | When Hot Zones ships, ensure per-variant + consensus views follow the same contract. |
| Gap/value tolerance | Formal definition of gap????????1 vs value-block semantics. | `_gap_regex` in matcher, `_vt_straight_spans` tolerant path. | Analyzer/Winners shading, digit-reduction overlay. | VT matcher tests; overlay tests. | Documented here so new modules reuse the same semantics. |
| Due-doubles freshness snapshot | Prevent stale draws-since metrics after CSV updates. | `modules/draw_catalog.scan_draw_files` + Control Center cache in `src/app.py`. | Control Center due-doubles table, positional hard-due trigger. | `tests/test_draw_catalog.py`; preflight doubles audit. | Auto-invalidates when draw files change; keep **Refresh Draw Tables** for manual overrides. |
| Long-string (Digit Reduction) windows | Keep the Digit-Reduction long-string boxes visible during V-TRAC analysis. | `alpha_analytical.digit_reduction.long_string_windows.get_long_string_boxes` + `module_c_vtrac.generate_table_html`. | Analyzer V2 tables, compact winners, full winners reports. | `tests/test_long_string_overlay.py`; `scripts/smoke_winners_logger.py`. | Yellow background and edge identify LS1/LS2 boxes without affecting scoring. |
| Stable pattern bundle | Preserve stable extractor artefacts (scores, families, spotlight) for reproducible training runs. | `run_stable_pattern_extraction(..., write_bundle=True)` + `alpha_analytical.stable.training_bundle.write_training_bundle`. | `data/outputs/analysis/patterns/<STATE>/training_sets/<STAMP>/`. | `tests/test_stable_training_bundle.py`. | Bundle manifest records winners, section counts, family IDs; files copied under `artifacts/`. |
| Three-value pattern handling | Collapse long runs that still represent three values. | Currently implicit via VT mapping; helper TODO. | Stable Extractor (planned), digit-reduction overlay explanations. | N/A | TODO: create normaliser to handle cases like 9444005 consistently. |

_Add rows as new analytical signals land (e.g., Aux compound scoring, Hot Zones heuristics)._ 

## Implementation Crosswalk
- **Shared helpers** - `modules/vtrac_matchers.{build_winner_targets, collect_spans}`. Import these instead of ad-hoc string logic in every module.
- **Highlight styling** - `module_c_vtrac.WINNER_STYLE_BLOCK` defines the official green/blue/purple legend. Compact winners reuse the same classes; future UIs should mirror this block.
- **Download utility** - `src/app._offer_report_download` exposes HTML downloads without relying on Streamlit page routing. Control Center winners tiles already use it.
- **Draw snapshot helper** - `modules/draw_catalog.{scan_draw_files, draws_since_last_double}` feeds the Control Center cache and hard-due flags with newest-first data and snapshot invalidation.
- **Draw purge helper** - `alpha_analytical.control_center.draws_refresh.purge_draw_csvs` removes stale draw CSVs before regeneration so Aux features always read fresh variants.
- **Winners builder import** - `_load_write_winner_full_report()` guarantees we load the project module (not staged Aux). Use before calling `write_winner_full_report()` anywhere else.
- **Training overlay tie-in** - Digit Reduction overlay reads the same span outputs; when adding signals, update both matcher + overlay modules to stay aligned.

## Usage Patterns & Integration Notes
- Call `build_winner_targets(winner, index_family)` once per winner and reuse the returned `WinnerTargets` for all cell highlighting.
- Columns that contain digits (R2/R4/R6/R8 and numeric headers) should pass values through `_highlight_value()` before rendering in HTML.
- Stick with the established CSS class names (`hit-winner`, `hit-vt-straight`, `hit-family`, etc.) so all pages share the same legend.
- Winners logging should record which classes triggered (winner, VT-straight, family) to enrich downstream training bundles.
- Store analysis outputs under `data/outputs/analysis/...` with clear state/variant folders for easy ingestion.

### Training Package Workflow
- Each module should produce: (a) analysis output (HTML/CSV/JSON), (b) winners logging artifact (index family, VT hits, metadata), (c) optional training bundle entry (e.g., `digit_reduction/Analyzer V2/winners`).
- Span metadata (green/blue/purple) must accompany scores so future rules/ML can see which signals fired.
- Digit Reduction overlay already logs these signals; Stable extractor and upcoming modules should emit comparable JSON rows.
- Control Center batch expander (`alpha_analytical.control_center.batch_runner`) parses the Pick3StatsC4 sheet, runs winners logging for every tracked state, and can trigger Stable Pattern training bundles in one click.

## Pending & Future Signals
- Stable Pattern extractor - build a helper that normalises long three-value runs and feeds the matcher.
- Aux compound scoring - define feature keys (e.g., `aux.repeat_watch.hot_index`) and associate them with VT/family hits where relevant.
- Hot Zones module - decide whether to reuse VT-straight highlighting or introduce complementary cues (document here when finalised).
- Profitability dashboard - log which signals were present when a wager passes thresholds so scoring aligns with visual cues.

## Update Log
## 2025-10-09 - Due-doubles snapshot guard
- Impact: Control Center now snapshots draw CSV mtimes/sizes and refreshes the due-doubles table automatically, preventing stale draws-since metrics when data updates.
- Impact: Added `modules/draw_catalog` helpers and regression tests so newest-first detection stays in sync with positional hard-due flags.
- Files: src/app.py, modules/draw_catalog.py, tests/test_draw_catalog.py, briefings/CODEX_READ_FIRST_AAT9.md, docs/AAT9_KIT/{AAT9_Testing_Roadmap.md}.

- 2025-10-08 - Initial version capturing VT-straight integration, Control Center download workflow, and training-package linkage.







- **Aux validation CLI** - scripts/tools/validate_aux_doubles.py now recomputes variant doubles *and* pair windows directly from the draws CSVs, highlighting overdue tokens across Combined/Midday/Evening for quick sanity checks.
- **Aux repeat/positional CLI** - scripts/tools/validate_aux_repeat.py replays repeat-watch streaks and positional hard-due flags from the raw CSV streams so Control Center badges can be verified without Streamlit.
- **Aux V-TRAC/sums CLI** - scripts/tools/validate_aux_vtrac.py surfaces top overdue indexes, heatboard metrics, and sums diagnostics directly from the CSVs, mirroring the Control Center overlays.
