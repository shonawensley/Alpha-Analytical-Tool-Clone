# AAT9 - Analysis Insights

## Role & Scope
- Captures the analytical signals and pattern-recognition features implemented across AAT9 so every tool can reuse them without re-deriving the wiring.
- Complements `AAT9_Live_Wiring_and_Data_Paths.md` (routes) and `AAT9_Testing_Roadmap.md` (guardrails) by documenting *what* we detect, *why*, and *where* the logic lives.
- Use this doc whenever you add or modify analysis logic in Analyzer V2, Winners, Stable Pattern, Aux scoring, Hot Zones, or future modules.

## Signal Reference

| Signal | Purpose | Implementation | Surfaces | Guardrails | Notes / TODO |
| --- | --- | --- | --- | --- | --- |
| Winner permutations (strict + gap +/- 1) | Highlight winner digits even with a stray digit in the string. | `modules/vtrac_matchers.collect_spans` (`winner_strict`, `winner_gap`). | Analyzer tables (`src/core/module_c_vtrac.py`), compact winners (`src/core/winners_vtrac_report.py`), full winners report (`modules/winner_report_full.py`). | `tests/test_vtrac_matchers.py::test_analyze_cell_returns_winner_and_family_hits`; smoke `scripts/smoke_winners_logger.py`. | Ensure Stable/Hot Zones import the shared helper instead of substring matching. |
| VT-straight strict | Flag AABB/BBAA runs aligned with the winner's VT pair (blue solid). | `modules/vtrac_matchers._vt_straight_spans` strict branch. | Analyzer tables, compact winners, digit-reduction overlay. | `tests/test_vtrac_matchers.py::test_collect_spans_marks_vt_straight_strict`; renderer legend (`tests/test_winners_renderer.py`). | Reuse when Stable extractor formalises three-value runs. |
| VT-straight value-block | Catch straights hidden by a run of foreign digits (blue dashed). | `_vt_straight_spans` tolerant branch. | Same surfaces as above. | `tests/test_vtrac_matchers.py::test_collect_spans_marks_vt_straight_gap`; smoke script. | Watch long-run edge cases (e.g., 9444005) during Stable extractor work. |
| Index-family combos | Highlight VT family hits (purple solid/dashed). | `collect_spans` (`family_strict`, `family_gap`). | Analyzer tables, compact winners, overlay. | Existing matcher assertions; renderer legend test. | Fold into Aux scoring weights when compound features consume family counts. |
| Cross-variant consensus | Keep Combined/Midday/Evening alignment transparent. | `module_c_vtrac.load_state_data`, Control Center Dev Health. | Analyzer output, Control Center tables, future scoring dashboards. | `tests/test_aux_loaders_variants.py`; preflight table checks. | When Hot Zones ships, ensure per-variant and consensus views follow the same contract. |
| Gap/value tolerance | Formal definition of gap +/- 1 vs value-block semantics. | `_gap_regex` in matcher, `_vt_straight_spans` tolerant path. | Analyzer/Winners shading, digit-reduction overlay. | VT matcher tests; overlay tests. | Documented here so new modules reuse the same semantics. |
| Due-doubles freshness snapshot | Prevent stale draws-since metrics after CSV updates. | `modules/draw_catalog.scan_draw_files` + Control Center cache in `src/app.py`. | Control Center due-doubles table, positional hard-due trigger. | `tests/test_draw_catalog.py`; preflight doubles audit. | Auto-invalidates when draw files change; keep **Refresh Draw Tables** for manual overrides. |
| Long-string (Digit Reduction) windows | Keep the digit-reduction long-string boxes visible during V-TRAC analysis. | `alpha_analytical.digit_reduction.long_string_windows.get_long_string_boxes` + `module_c_vtrac.generate_table_html`. | Analyzer V2 tables, compact winners, full winners reports. | `tests/test_long_string_overlay.py`; `scripts/smoke_winners_logger.py`. | Yellow background and edge identify LS1/LS2 boxes without affecting scoring. |
| Stable pattern bundle | Preserve Stable extractor artefacts (scores, families, spotlight) for reproducible training runs. | `run_stable_pattern_extraction(..., write_bundle=True)` + `alpha_analytical.stable.training_bundle.write_training_bundle`. | `data/outputs/analysis/patterns/<STATE>/training_sets/<STAMP>/`. | `tests/test_stable_training_bundle.py`. | Bundle manifest records winners, section counts, family IDs; files copied under `artifacts/`. |
| Stable winners evidence bus | Surface Control Center metrics and enriched winners evidence (family rank, doubles support, row why). | `alpha_analytical.stable.metrics.build_metrics`, `alpha_analytical.stable.winners_enrich.attach_stable_evidence`, batch runner wiring. | Stable success toast, Control Center batch panel, `data/outputs/analysis/patterns/<STATE>/training_sets/<STAMP>/<STATE>_metrics.json`. | `tests/test_stable_doubles_adjacency_negative.py`; manual Control Center smoke. | Metrics JSON logs schema versions; evidence columns remain read-only so Combined highlights stay intact. |
| Digit Reduction training bundle autopack | Package Analyzer V2 core outputs plus Midday/Evening overlays by default (Combined opt-in). | `alpha_analytical.digit_reduction.analyzer_v2.training_bundle.package_training_bundle`. | Control Center batch workflow, `data/outputs/analysis/digit_reduction/<STATE>/training_sets/<STAMP>/`. | `tests/test_digit_training_bundle.py`. | Bundles include per-item/top-candidate CSVs, latest winner maps/flags/stamps, optional hits/overlay, and manifest metadata. |
| Three-value pattern handling | Collapse long runs that still represent three values. | Currently implicit via VT mapping; helper TODO. | Stable extractor (planned), digit-reduction overlay explanations. | N/A | TODO: create normaliser to handle cases like 9444005 consistently. |

_Add rows as new analytical signals land (for example Aux compound scoring, Hot Zones heuristics)._ 

## Implementation Crosswalk
- **Shared helpers** - `modules/vtrac_matchers.{build_winner_targets, collect_spans}`. Import these instead of ad-hoc string logic in every module.
- **Highlight styling** - `module_c_vtrac.WINNER_STYLE_BLOCK` defines the official green/blue/purple legend. Compact winners reuse the same classes; future UIs should mirror this block.
- **Download utility** - `src/app._offer_report_download` exposes HTML downloads without relying on Streamlit page routing. Control Center winners tiles already use it.
- **Draw snapshot helper** - `modules/draw_catalog.{scan_draw_files, draws_since_last_double}` feeds the Control Center cache and hard-due flags with newest-first data and snapshot invalidation.
- **Draw purge helper** - `alpha_analytical.control_center.draws_refresh.purge_draw_csvs` removes stale draw CSVs before regeneration so Aux features always read fresh variants.
- **Winners builder import** - `_load_write_winner_full_report()` guarantees we load the project module (not staged Aux). Use before calling `write_winner_full_report()` anywhere else.
- **Training overlay tie-in** - Digit Reduction overlay reads the same span outputs; when adding signals, update both matcher and overlay modules to stay aligned.

## Usage Patterns & Integration Notes
- Call `build_winner_targets(winner, index_family)` once per winner and reuse the returned `WinnerTargets` for all cell highlighting.
- Columns that contain digits (R2/R4/R6/R8 and numeric headers) should pass values through `_highlight_value()` before rendering in HTML.
- Stick with the established CSS class names (`hit-winner`, `hit-vt-straight`, `hit-family`, etc.) so all pages share the same legend.
- Winners logging should record which classes triggered (winner, VT-straight, family) to enrich downstream training bundles.
- Store analysis outputs under `data/outputs/analysis/...` with clear state/variant folders for easy ingestion.

### Training Package Workflow
- Each module should produce: (a) analysis output (HTML/CSV/JSON), (b) winners logging artifact (index family, VT hits, metadata), (c) optional training bundle entry (for example `digit_reduction/analyzer_v2/winners`).
- Span metadata (green/blue/purple) must accompany scores so future rules or ML can see which signals fired.
- Digit Reduction overlay already logs these signals; Stable extractor and upcoming modules should emit comparable JSON rows.
- Control Center batch expander (`alpha_analytical.control_center.batch_runner`) parses the Pick3StatsC4 sheet, runs winners logging for every tracked state, and can trigger Stable Pattern bundles and the Digit Reduction pipeline (reducer/analyzer/overlay, optional DR bundle) in one click.

## Pending & Future Signals
- Stable Pattern extractor - build a helper that normalises long three-value runs and feeds the matcher.
- Aux compound scoring - define feature keys (for example `aux.repeat_watch.hot_index`) and associate them with VT/family hits where relevant.
- Hot Zones module - decide whether to reuse VT-straight highlighting or introduce complementary cues (document here when finalised).
- Profitability dashboard - log which signals were present when a wager passes thresholds so scoring aligns with visual cues.

## Update Log
### 2025-10-14 - Stable extractor spot-check (June 17 winners: Connecticut4 & Florida4)
- Ran the Control Center batch with the June 17 Pick‑3 outcomes (`894/059` for CT, `572/666` for FL). Stable training bundles (stamp `20251014`) captured the winners list, metrics JSON, and spotlight CSVs without touching non-tracked states.
- Connecticut4: family 34 (winner 894) shows strong straight support (family_score 23, progression True, `fam_straight2=2`, `fam_straight3=4`) and row evidence (`straight|cov1|mirror|hot2`) with boolean fields preserved as nullable types. Winner 059 maps to family 5 (progression False, no doubles); spotlight rows are absent, so low-score winners may be filtered out—worth a future review.
- Florida4: family 33 (winner 572) highlights straight pressure in a single section; family 22 (winner 666) spreads across three sections with progression True yet still no spotlight rows, reinforcing that schema is healthy but spotlight thresholds may need tuning.
- Training bundles under `patterns/<STATE>/training_sets/20251014/` contain the full Stable artefact set (scores, families, spotlight, metrics) with evidence schema/contract versions intact, ready for downstream analysis.

### 2025-10-13 - Stable winners evidence bus
- Impact: Control Center now records Stable metrics JSON, enriches winners evidence (family rank, doubles support, row detail), and exposes per-state expander downloads during batch runs.
- Impact: Stable training bundles include metrics manifests so downstream analysis can track schema versions.
- Files: alpha_analytical/stable/{metrics.py,training_bundle.py,winners_enrich.py}, alpha_analytical/control_center/batch_runner.py, src/app.py, tests/{test_stable_doubles_adjacency_negative.py,test_digit_training_bundle.py}.
### 2025-10-12 - Stable extractor cross-section and progression signals
- Impact: Row payloads now expose `family_id` and rename the horizontal bonus to `horizontal_persistence_repeat`, keeping terminology consistent with future reduction tooling.
- Impact: Family post-pass adds `section_count`, `progression_flag`, and `last_remaining_3v` with configurable weights; Delaware's 277 family and similar doubles now surface via the V-TRAC fallback.
- Impact: Added regression guard `tests/test_vtrac_triples.py` for the 277 + 26 mapping and wired the fallback by V-class code inside `modules.vtrac_reference`.
- Validation snapshots (min_occ=1, min_score=7):
  - **Connecticut4 (281, 835)** - winner families (id 13, 21) reach `section_count = 3`, `progression_flag = True`, and hold Combined/Midday/Evening coverage in the spotlight CSV.
  - **Delaware4 (979, 127)** - both families (20, 31) surface across all three sections with progression flagged; 277 now resolves to family 20.
  - **Indiana4 (174, 702)** - families (10, 22) reside in Combined only, but `progression_flag` toggles on the Set run, confirming the Set-compounding logic.

### 2025-10-09 - Due-doubles snapshot guard
- Impact: Control Center now snapshots draw CSV mtimes/sizes and refreshes the due-doubles table automatically, preventing stale draws-since metrics when data updates.
- Impact: Added `modules/draw_catalog` helpers and regression tests so newest-first detection stays in sync with positional hard-due flags.
- Files: src/app.py, modules/draw_catalog.py, tests/test_draw_catalog.py, briefings/CODEX_READ_FIRST_AAT9.md, docs/AAT9_KIT/{AAT9_Testing_Roadmap.md}.

### 2025-10-08 - Initial version
- Captured VT-straight integration, Control Center download workflow, and training-package linkage.

## Reference CLI Helpers
- **Aux validation CLI** - `scripts/tools/validate_aux_doubles.py` recomputes variant doubles and pair windows directly from the draws CSVs, highlighting overdue tokens across Combined/Midday/Evening.
- **Aux repeat/positional CLI** - `scripts/tools/validate_aux_repeat.py` replays repeat-watch streaks and positional hard-due flags from the raw CSV streams so Control Center badges can be verified without Streamlit.
- **Aux V-TRAC/sums CLI** - `scripts/tools/validate_aux_vtrac.py` surfaces top overdue indexes, heatboard metrics, and sums diagnostics directly from the CSVs, mirroring the Control Center overlays.

### 2025-10-13 - Stable Pattern Extractor (Regression Shield) - Paused
- Row payload now emits per-component score fields (for example `score_cov`, `score_hidden`) and a hidden-by-one flag; YAML gains `doubles_trigger_bonus` / `hidden3v_bonus` placeholders.
- Family summary exports `fam_*` score parts plus placeholders for section/progression bonuses.
- Outstanding: consensus doubles support, section/progression/last_remaining bonuses, metrics writer, regression guard tests/hooks. See `tasks/FIX_122.txt`.
- Files touched: alpha_analytical/stable/{__init__.py,post_pass_families.py,feature_config.yml}, tests/test_stable_contracts.py.

### 2025-10-14 - Stable Pattern Phase Two (Indiana, Michigan, New Jersey, New York)\n- Ran Control Center batch with June 17 winners for Indiana, Michigan, New Jersey, and New York (stamp 20251014). Stable bundles captured the new winners lists plus metrics/spotlight CSVs under patterns/<STATE>/training_sets/20251014/.\n- Indiana4: family 15 (winner 940) and family 23 (winner 188) register scores 5 and 10 in the raw CSV; metrics writer elevates them to 17 after boosts. Winner 188 retains boxed row evidence (oxed|cov3|hp_repeat2|vstr2|perm2|hidden3v) while 940 lacks spotlight rows (row evidence NaN) despite Combined spotlight totals (194 rows overall) hinting the filters exclude that canonical. Winners logger paths (trac15 / trac23) confirm VT alignment. Digit Reduction hits (Midday 74, Evening 24, Combined 276) reinforce Combined dominance.\n- Michigan4: families 18 (winner 618) and 27 (winner 339) highlight straight pressure (fam_straight2 > 0) yet no spotlight rows surfaced; metrics JSON still reports spotlight_rate 1.0, so the score writer is boosting them. Winners logger (trac18 / trac33) and Digit Reduction hits (24/67/195) offer parallel confidence.\n- NewJersey4: families 19 and 24 show modest section coverage (section_count 1) with no doubles support; row evidence absent (NaN). Spotlight totals exist in manifest (276 rows) suggesting canonical matching needs refinement. Winners logger uses trac11/trac22; Digit Reduction hits 20/26/118.\n- NewYork4: families 17 and 8 echo the same pattern—family stats healthy (progression True for 211, fam_straight2>0 for 680) but row-level exports absent. Winners logger trac17/trac8; Digit Reduction hits 84/24/72.\n- Takeaways: family-level features (progression, hidden3v, straight counts) remain active and nullable booleans stay intact. However, spotlight filtering currently suppresses row evidence for these winners; consider revisiting canonical matching or score thresholds so row-level context accompanies the Phase Two bundle outputs.\n
- Scoring feature audit: Verified row-level triggers (mirror, straight2/3, single_left, consensus variants, dom_last, dom_pair, hot, hidden3v, coverage, length, hidden bonus, etc.) using Indiana Combined tables (e.g., Set1/Draw1 column 1) and confirmed they align with the canonical permutations in 	ables/<STATE>/Combined_Combined.csv. Family-level bonuses (coverage, HPR, perm density, consensus, straight2/3, doubles, progression) also score as expected. Features not observed in this dataset—repeat_extras, repetition bonus, section bonus, last_remaining_3v—remain TODO for a targeted scenario.\n
