# AAT9 — Unified Changelog

Conventions: YYYY‑MM‑DD — Category — Summary — Impact — Files/Refs

## 2025‑09‑06 — Cleanup — Archive legacy launchers/entrypoints — Safer surface
- Impact: No runtime changes; older scripts moved under `archived/2025-09-06/` with manifest
- Files: `archived/2025-09-06/ARCHIVE_MANIFEST.md`
- Note: `run_app.bat` + `src/app.py` remain canonical

## 2025‑09‑06 — Tooling — Added preflight script — Faster path/import triage
- File: `.codex/preflight.ps1`
- Use: `powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"`

## 2025‑09‑06 — Docs — Architecture & App Flow Addendum — Canonical setup
- Files: `docs/AAT9_DOCS/AAT9_Architecture_Dir_Layout_2025-09-06.md`, `docs/AAT9_DOCS/AAT9_App_Flow_Addendum_2025-09-06.md`
- Includes: directory tree, data contracts, Mermaid diagram, guardrails

## 2025‑09‑06 — Hygiene — Forwarder for legacy path handler — Single source of truth
- File: `src/utils/path_handler.py` → re‑exports `utils.path_handler`
- Advantage: avoids duplicate logic/signature drift

## 2025‑09‑06 — Docs — KIT created — Curated entrypoint for AAT9
- Folder: `docs/AAT9_KIT/*`
- Includes: KIT README, Quickstart, AI Guide, Preflight Ref, Unified Changelog, Diagrams Guide

## 2025‑09‑06 — Pipeline — Tables pipeline runner + Control Center UI (optional)
- Files: `src/core/pipeline_runner.py`; `src/app.py` (Control Center expander)
- Adds: Upload Pick3StatsC4.xlsm and “Generate Tables” (clean → extract → generate)
- Writes: `data/cleaned/<State>_cleaned.xlsx`; `data/outputs/tables/<STATE>/..._combined.csv`
- Safe: path_handler SSOT; no auto‑run; soft‑fail captions; pages keep reusing outputs

## 2025‑09‑07 — Imports — SSOT bootstrap for canonical utils
- Files: `src/app.py`
- Fix: Enforce top‑level `utils` package binding early to prevent `src\utils` shadowing
- Why: Streamlit/sys.path order could resolve `utils` to `src\utils`, causing `ImportError/NameError`
- Safe: small, surgical import bootstrap; no behavior change to pages

## 2025‑09‑07 — Aux — Pairs display bands & captions
- Files: `src/app.py` (Aux page)
- Change: Mutually‑exclusive bands (red highest) for repeating/non‑repeating; Top‑5 repeating coloring aligned; thresholds caption uses ASCII ">="
- Why: Old labels used overlapping checks (red ≥ 71 and blue ≥ 107) causing confusion; this is display‑only; calculations unchanged

## 2025‑09‑07 — V‑Trac — Big table badges
- Files: `src/app.py` (Aux page)
- Change: Red Top‑10 overdue rows show badge with "rank (draws_since)"; preserves green (recent)
- Why: Align big table with the small “Index Hits” table; display‑only

## 2025‑09‑07 — Digit Reduction — Stacked report + training exports
- Files: `src/core/module_b_digit_reduction.py` (orchestrator), `src/app.py` (page wiring)
- Adds: Stacked HTML report embed checkbox; training CSV/JSON with structural fields and export compaction (analysis unchanged)
- Outputs: `data/outputs/analysis/digit_reduction/<STATE>/{...report.html, ...report_stacked.html, ...scores.csv}`;
  `training/{...steps.csv, ...logs.json}` with guidance and schema

## 2025‑09‑07 — Winners — V‑Trac winner report (index panels)
- Files: `src/core/winners_vtrac_report.py`, `src/app.py` (Control Center expander)
- Adds: single‑state, per‑winner HTML export showing Midday/Evening/Combined index panels
  - Purple = index stable‑pattern combos; Green = straight permutations of the winning number
- Writes: `data/outputs/winners/<YYYY‑MM‑DD>/vtrac_reports/<STATE>/<STATE>_vtrac<index>_winner_<timestamp>.html`
- Notes: table‑agnostic (safe for states missing string‑tables); later can overlay table‑driven details
