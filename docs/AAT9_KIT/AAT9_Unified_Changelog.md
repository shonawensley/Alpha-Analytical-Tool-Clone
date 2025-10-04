## 2025-10-03 - Positional shortlist hardening (pos_5)\n- Impact: Applied the pos_5 checklist by dialing SSOT defaults (pool=6, max_internal=64), clarifying All-Variant consensus labels, reusing Control Center V-TRAC caches, and adding regression tests for repeat-endcap, lane concordance, and union pool coverage.\n- Files: src/app.py, src/core/aux_config.py, modules/module_d_auxiliary_tools/refactored/positional_tool.py, tests/test_positional_shortlist.py.\n\n## 2025-10-02 - Positional tracker shortlist revamp\n- Impact: Aux Positional Tracker now reads a SSOT shortlist config, exposes tuning controls, folds in repeat-endcap/lane concordance seeds, and adds V-TRAC index/family boosts with evidence-rich rows that stay in sync with Control Center.\n- Files: src/app.py, modules/module_d_auxiliary_tools/refactored/positional_tool.py, src/core/aux_config.py, tests/test_positional_shortlist.py.\n\n## 2025-10-02 - Aux heatboard & sums metadata
- Impact: Control Center now renders Top-5 V-TRAC double families with consistent HTML badges, both Control Center and Aux expose a hazard-based "V-TRAC Heatboard" for quick index pressure scans, and sums stats capture `deficit`/`z_tail` for future scoring.
- Files: src/app.py, modules/module_d_auxiliary_tools/refactored/sums_analysis.py, src/core/vtrac_families.py, tests/test_vtrac_families.py.

## 2025-10-01 - V-TRAC Analyzer - tables reader & health
- Impact: V-TRAC now reads the pipeline's combined tables, adds preflight/system-health info, clears stale caches, and no longer exposes the legacy mini-pipeline controls.
- Files: `src/app.py`, `src/core/module_c_vtrac.py`.

## 2025-10-01 - Digit Reduction - training log guardrails
- Impact: Reducer now writes `digit_reduction/<STATE>/training/<STATE>_digit_reduction_log.json` deterministically, analyzer tolerates blank fields, and the Streamlit tab adds preflight checks plus DEV overlay guards to prevent blank screens.
- Files: `src/app.py`, `src/core/module_b_digit_reduction.py`, `alpha_analytical/digit_reduction/analyzer_v2/{io.py,pipeline.py}`.

## 2025-10-01 - V-TRAC UI sanitization
- Impact: Replaced emoji/en dash UI markers with ASCII-only text so the Mojibake guard stays green and the page renders without warnings.
- Files: src/core/module_c_vtrac.py.


## 2025-10-02 - Aux SSOT windows & V-TRAC repeat watch
- Impact: Added core/aux_config.py as the single source of truth for Aux windows/thresholds, surfaced the values in UI captions/dev health, unified the V-TRAC overlay for the working table and index hits, and introduced a Control Center repeat watch panel backed by new overlay helpers.
- Files: src/app.py, src/core/aux_config.py, scripts/auxiliary/working/modules/analyze_pairs.py, 	ests/test_analyze_pairs_semantics.py.


## 2025-10-02 - Aux SSOT follow-up (UI + smoke)
- Impact: Replaced the overdue-threshold info panel with a safe join using the SSOT constants and added a fallback in the staged analyze_pairs module so Aux smokes import core/aux_config even when launched from scripts/.
- Files: src/app.py, scripts/auxiliary/working/modules/analyze_pairs.py.
## 2025-10-02 - Aux roadmap doc
- Impact: Created `docs/AAT9_KIT/AAT9_Aux_Roadmap.md` to capture the current Aux baseline, Phase-1B follow-ups, and deferred goals with references to AUX_WATCH/BIG_PICTURE/FIX_80 so future sessions can ramp quickly.
- Files: docs/AAT9_KIT/AAT9_Aux_Roadmap.md, docs/AAT9_KIT/AAT9_Checkpoint_Log.md.


## 2025-10-02 - Control Center V-TRAC double families
- Impact: Replaced the due-doubles pair/combination columns with Top-5 V-TRAC double family strips (severity + variant tags) and surfaced the same rankings on the Aux page with a family column.
- Files: src/app.py, src/core/vtrac_families.py, docs/AAT9_KIT/AAT9_Aux_Roadmap.md.


