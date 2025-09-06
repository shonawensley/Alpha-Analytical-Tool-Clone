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

