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
