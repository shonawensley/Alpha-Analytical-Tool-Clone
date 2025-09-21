## 2025-09-21 02:00 (UTC) - Aux staging restore

- Context: Aux began failing after the Sept-16 cleanup because the rich boxed VTRAC reference (legacy) was archived. Lazily imported modules fell back to the slim canonical API, so Aux lost `BOXED_LABEL_LOOKUP` and returned empty tables.
- Change:
  - Hardened `_aux_working_first()` (stages working modules for full run; restores sys.path and prior bindings).
  - Converted staged imports to relative (`scripts/auxiliary/working/modules/*`).
  - Updated refactored bootstrap to locate legacy assets and register them before loading Aux helpers.
  - Removed ad-hoc sys.path tweaks in refactored helpers; added smoke script `scripts/checks/smoke_aux_vtrac.py`.
  - Added Aux staging manifest + doc hooks (Quickstart, Live Wiring, Pitfalls).
- Rationale: Keep Aux draws-only flow stable while maintaining the canonical VTRAC API for Winners and other pages.
- Impact: Aux runs again (boxed VTRAC grid + overdue panels), Dev Health shows staged bindings, quick smoke script catches regressions.
- Files/Refs: src/app.py; scripts/auxiliary/working/modules/{analyze_pairs.py,run_process.py}; modules/module_d_auxiliary_tools/refactored/{bootstrap_imports.py,boxed_vtrac.py,indicators.py}; scripts/checks/smoke_aux_vtrac.py; docs/AAT9_DOCS/AAT9_Aux_Staging_Manifest.md; Quickstart/LW/Pitfalls updates.
- Follow-ups: Optional - remove duplicate legacy copies once archive-only loader is validated; consider compat shim so Aux can consume canonical API long-term.

## 2025-09-19 20:30 (UTC)  Stable Pattern Modal Scoring + Families

- Context: Needed richer Stable outputs (permutation density, family grouping, winner spotlights) to prep for training and operational use.
- Change:
  - Updated analyser to count permutation/repeat density, modal straights, debug columns, and consensus tails using digits-only logic.
  - Added post-pass family aggregator + YAML weights; winner spotlight CSVs generated when winners provided.
  - Extended Streamlit UI with winners input, family/spotlight download links, and dev health prints for engine/YAML.
- Rationale: Improves scoring fidelity and exposes structured outputs for downstream analysis without touching other tools.
- Impact: New CSVs under data/outputs/analysis/patterns/<STATE>/ (families + optional spotlight); Stable page now accepts winners list; Stable UI shows quick links + preview for the families frame.
- Files/Refs: alpha_analytical/stable/{__init__.py,feature_config.yml,post_pass_families.py,winner_family_spotlight.py}, alpha_analytical/vtrac/, src/core/stable_pattern_extractor.py, src/app.py, docs/AAT9_KIT/important/stable_pattern_AAT9.txt.
- Follow-ups: Consider cross-section/progression bonuses (post_pass_families) and unit tests for rep3 helper.
## 2025-09-19 01:05 (UTC)  Stable Pattern Archive Cleanup

- Context: Multiple legacy Stable Pattern runners/tests were still in the repo, creating confusion about which extractor feeds the integrated app.
- Change:
  - Archived root BATs, scripts/archive/* demos, scripts/utils_old/* helpers, historical `data/outputs/stable_patterns/`, and the legacy pytest into `archived/2025-09-19_stable_cleanup/` with a manifest.
  - Added Stable Dev Health details so the page prints engine + feature_config paths.
  - Updated KIT docs/changelog to reference the canonical chain and archive location.
- Rationale: Eliminates duplicate entry points while keeping references available; Dev Health now confirms bindings explicitly.
- Impact: No runtime change  Streamlit uses `src/core/stable_pattern_extractor.py` ? `alpha_analytical/stable/__init__.py`; legacy assets are preserved for reference.
- Files/Refs: archived/2025-09-19_stable_cleanup/*, src/app.py, docs/AAT9_KIT/important/stable_pattern_AAT9.txt, docs/AAT9_DOCS/stable_pattern_master_guide_AAT9.md, docs/AAT9_KIT/AAT9_Unified_Changelog.md.
- Follow-ups: None required; restore specific runners from archive only if a CLI is needed.
# AAT9 — Checkpoint Log (Running, Detailed Notes)

Purpose: A single, date‑tagged log for deeper explanations, context, and rationale that complement the Unified Changelog. Use this when you (or AI) want to capture more than a one‑line changelog entry.

How to update
- Append a new section at the top.
- Use the template below; keep entries concise but explanatory.
- Link to relevant files, PR notes, logs, and diagrams.

Template
```
## YYYY‑MM‑DD HH:MM (TZ) — Title

- Context: one‑paragraph background
- Change: what changed (bullets)
- Rationale: why this improves stability/clarity/UX
- Impact: runtime behavior, workflows, or docs affected
- Files/Refs: file paths, doc sections, diagrams
- Follow‑ups: next steps if any
```

---

## 2025‑09‑06 12:00 (UTC) — Preflight Tables Check + Startup Docs

- Context: We standardized AAT9 startup (KIT + preflight) and wanted a quick, opt‑in validation for combined tables when working on Stable/DR/V‑TRAC.
- Change:
  - Added `-CheckTables` to `.codex/preflight.ps1` to list `data/outputs/tables` state dirs and confirm a specific state dir exists.
  - Added `docs/AAT9_KIT/HUMAN_READ_FIRST_AAT9.md` with simple operator instructions.
  - Added Codex boot doc `briefings/CODEX_READ_FIRST_AAT9.md` and a clipboard helper `TOOLS/codex_start_aat9.bat`.
- Rationale: Keeps preflight fast by default; adds a quick on‑demand tables sanity check; standardizes session startup for both humans and agents.
- Impact: No runtime changes; faster diagnosis when working on combined‑tables pages.
- Files/Refs:
  - `.codex/preflight.ps1` (new flags)
  - `docs/AAT9_KIT/HUMAN_READ_FIRST_AAT9.md`
  - `briefings/CODEX_READ_FIRST_AAT9.md`, `TOOLS/codex_start_aat9.bat`
  - KIT index: `docs/AAT9_KIT/AAT9_KIT_README.md`
- Follow‑ups: Consider Phase‑2 Aux audit after new Aux tools land.

## 2025‑09‑06 13:30 (UTC) — Tables Pipeline Runner + Control Center UI

- Context: Daily workflow uploads a fresh Pick3StatsC4.xlsm and regenerates combined tables; we needed a safe way to run this in‑app when needed.
- Change:
  - Added `src/core/pipeline_runner.py` (pure functions) that cleans → extracts → builds combined tables.
  - Wired an optional “Tables Pipeline” expander in Control Center to upload Excel and run the pipeline.
- Rationale: Keep pipeline runnable from the app, but only on demand; reuse outputs across pages; no recompute on render.
- Impact: No changes to existing pages; optional UI only. Outputs stored under `data/cleaned` and `data/outputs/tables`.
- Files/Refs: `src/core/pipeline_runner.py`, `src/app.py` (Control Center section), `docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md`
- Follow‑ups: None required; Phase‑2 Aux audit deferred until after new Aux tools are added.

## 2025‑09‑07 10:10 (UTC) — Import Shadowing (utils) → SSOT Bootstrap

- Context: Intermittent startup errors (`ImportError: cannot import name get_cleaned_data_dir` or `NameError: Path is not defined`) after adding optional pipeline UI. Data/layout were fine; errors stemmed from module resolution.
- Root Cause: Two packages named `utils` exist (`/utils` canonical, `/src/utils` legacy). When Streamlit sys.path had `src` before project root, absolute imports (`from utils.path_handler ...`) bound to `src\utils` first, triggering a circular forwarder and partial module.
- Fix: Add a small SSOT import bootstrap at the very top of `src/app.py`:
  - Insert project root at sys.path[0].
  - Evict premature `utils`/`src.utils` bindings if they resolve under `/src/utils`.
  - Import and pin `utils.path_handler` from the top‑level package.
- Impact: Deterministic binding to canonical `utils`; no behavior changes to pages/pipeline.
- Files: `src/app.py`; docs updated: KEEPERS.md, Pitfalls.
- Follow‑ups: None — structural rename of `src/utils` not required now.

## 2025‑09‑07 12:20 (UTC) — Aux Pairs Bands (Display‑Only)

- Context: Overdue pairs lists used overlapping bands (e.g., repeating red ≥ 71 and blue ≥ 107), causing label confusion. Policy: red is the highest threshold.
- Change: Mutually‑exclusive bands (display‑only) with red highest:
  - Repeating: red ≥ 107; blue 71..106; purple 25..70
  - Non‑repeating: red ≥ 56; blue 37..55; purple 25..36
- Caption updated to ASCII ">=" to avoid mojibake. Top‑5 repeating color mapping aligned; list still sorted by draws_since.
- Impact: No calculation changes; UI buckets and captions now match policy.

## 2025‑09‑07 12:40 (UTC) — V‑Trac Big Table: Badge Shows Draws‑Since

- Context: Small “Index Hits” shows draws_since; big table should show it too for Top‑10 red rows.
- Change: Red rows now use badge "rank (draws_since)"; green rows unchanged.
- Impact: Display‑only; keeps small/big table alignment.

## 2025‑09‑07 13:00 (UTC) — Digit Reduction: Stacked Report + Training Exports

- Context: Need training‑friendly exports and stacked view for better screenshots; analysis unchanged.
- Change:
  - Added stacked report HTML and checkbox in page to embed it.
  - Added training CSV/JSON exports under `.../training/` with structural fields, ranks, guidance, and export‑only compaction.
- Outputs:
  - `data/outputs/analysis/digit_reduction/<STATE>/<STATE>digit_reduction_report.html`
  - `.../<STATE>digit_reduction_report_stacked.html`
  - `.../<STATE>digit_reduction_scores.csv`
  - `.../training/<STATE>digit_reduction_steps.csv`
  - `.../training/<STATE>digit_reduction_logs.json`
- Impact: No changes to reduction algorithms or tabbed HTML; only exports and optional embed.

## 2025‑09‑07 14:10 (UTC) — Winners Logger: V‑Trac Winner Report (Index Panels)

- Context: Need a per‑state, per‑winner visual export for external training; older runs had correct “vtrac_reports” HTML under winners.
- Change: Added an index‑based report generator and UI expander in Control Center:
  - Inputs: State, 3‑digit winner
  - Renders 3 panels (Midday/Evening/Combined) with:
    - Purple: stable‑pattern combos for the winner’s index
    - Green: straight permutations of the winner
  - Writes to: `data/outputs/winners/<YYYY‑MM‑DD>/vtrac_reports/<STATE>/<STATE>_vtrac<index>_winner_<timestamp>.html`
- Impact: Does not require string‑tables; safe for states whose tables aren’t mapped yet. Later we can overlay table‑driven details.
- Files: `src/core/winners_vtrac_report.py`, `src/app.py`
## 2025-09-16 16:00 (UTC) — Winners Full Report + Aux V‑TRAC Restore

- Context: The Aux tools rely on a staged V‑TRAC reference under `scripts/auxiliary/working/modules/` while the integrated app should use a canonical `modules/*`. A deleted staged `vtrac_reference.py` broke Aux; the Winners Logger (full) also failed due to imports resolving to the staged package and a missing canonical API. Goal: restore Aux, add a canonical V‑TRAC API, and enable a table‑aware analyzer‑style Winners Full report (3 panes, purple index + green straights) without touching analyzer internals.
- Change:
  - Restored staged Aux reference: `scripts/auxiliary/working/modules/vtrac_reference.py` (exports restored; draws‑only Aux unaffected).
  - Added canonical API: `modules/vtrac_reference.py` exporting `get_vtrac_index`, `get_index_set`, `get_index_straights` (backed by analyzer utilities).
  - Implemented full builder: `modules/winner_report_full.py` (reads three combined tables, renders analyzer‑style 3‑pane HTML via analyzer renderer, applies green straights overlay, writes to `data/outputs/analysis/winners/<STATE>/...`).
  - Wired Control Center tile: “Winners Logger (Analyzer‑style full report)” now accepts Midday/Evening and generates one HTML per input; compact tile unchanged.
  - Import hygiene: ensured non‑Aux pages bind `modules/*` to the project tree, not the staged Aux path; added a robust import fallback in the full tile.
- Rationale: Cleanly separates Aux (staged) from the integrated app (canonical), removes import collisions, and reuses the established pipeline tables to produce the expected analyzer‑style Winners view. The canonical API gives non‑Aux code a single, stable entrypoint, reducing drift.
- Impact:
  - Aux tools: working again; no change to draws‑only behavior.
  - Winners Full tile: produces analyzer‑style HTML under `data/outputs/analysis/winners/<STATE>/...` with purple index coverage + green straights overlay; compact tile remains as a safe fallback when tables are missing.
  - No changes to analyzer internals or other tools; string‑safe CSV reads for new reporting prevent token coercion.
- Files/Refs:
  - Code: `modules/vtrac_reference.py`, `modules/winner_report_full.py`, `src/app.py` (full tile wiring), staged `scripts/auxiliary/working/modules/vtrac_reference.py` (restored)
  - Docs: `docs/AAT9_KIT/AAT9_Winners_VTrac_Report.md` (usage/paths), `docs/AAT9_KIT/AAT9_Live_Wiring_and_Data_Paths.md` (I/O mapping), `briefings/PITFALLS.txt` (import SSOT + string‑safe IO), `docs/AAT9_KIT/AAT9_Preflight_Reference.md` (tip for tables)
- Follow‑ups:
  - Optional: unify all tools on `modules/vtrac_reference.py` over time; keep Aux staged shim as a re‑export when you’re ready to retire duplicates.
  - Optional: move full report renderer to `src/reporting/` with a template; today’s builder already mirrors analyzer layout.
  - Add a tiny smoke CLI to generate a winners full report outside Streamlit if desired.

## 2025-09-17 21:00 (UTC) — Aux Draws Pipeline + Legacy Archive

- Context: Combined Aux features relied on historical folders (`adapters_old_module`, `legacy_2`, assorted scripts) and drew from `data/cleaned/*_draws.csv`. We now have a canonical extractor + Control Center exporter, so clutter was causing confusion and file-lock issues when rebuilding Midday/Evening draws.
- Change:
  - Added `scripts/auxiliary/generate_draws_csv.py` and Control Center "Aux Draws Pipeline" expander. Both write Combined/Midday/Evening CSVs to `data/cleaned/draws/` (combined enabled by default).
  - Loader (`modules/aux_loaders.load_state_draws`) prefers `data/cleaned/draws/` with fallback to legacy location so existing Aux/BA logic stays on combined.
  - Archived unused Aux packages (`modules/module_d_auxiliary_tools/{adapters_old_module,legacy_2}`) and legacy helper scripts under `archived/2025-09-17_aux_legacy/` with a README.
  - Documented the refactored surface in `modules/module_d_auxiliary_tools/refactored/README.md`.
- Impact:
  - Daily flow: run tables pipeline (if needed) then run Aux Draws Pipeline to refresh combined + Midday/Evening files.
  - Combined Aux features remain untouched; Midday/Evening ready for future wiring.
  - Less risk of grabbing stale modules; clearer directory layout for new contributors.
- Follow-ups:
  - Remove the leftover `data/cleaned/Connecticut_Midday_draws.csv` once Excel releases the file lock.
  - When ready, wire Midday/Evening into Control Center doubles + Blackapple (combined stays the baseline).
  - Consider retiring `scripts/auxiliary/working/` once staged modules are no longer needed by the Aux page.


