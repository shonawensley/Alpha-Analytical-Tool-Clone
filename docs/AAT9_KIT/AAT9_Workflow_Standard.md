# AAT9 — Workflow Standard (Agents & Devs)

Purpose: A clear, repeatable process for implementing changes safely, updating docs/diagrams consistently, and logging updates in one place.

## 0) Read‑First (once per session)
- KIT README: `docs/AAT9_KIT/AAT9_KIT_README.md`
- Architecture & Dir Layout: `docs/AAT9_DOCS/AAT9_Architecture_Dir_Layout_2025-09-06.md`
- Quickstart Cheat Sheet: `docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md`
- Preflight Reference: `docs/AAT9_KIT/AAT9_Preflight_Reference.md`

## 1) Preflight & Sanity
- Run: `powershell -NoProfile -File .codex/preflight.ps1 -State "<State>"`
- Confirm in‑repo imports and draws CSV inventory.
- If anything looks off, fix environment/paths before coding.

## 2) Plan (small, explicit)
- State the exact files to change and why.
- Keep diffs minimal; avoid refactors unless explicitly requested.
- For cleanup, prefer archive‑first moves with a manifest; no deletions.

## 3) Implement (path‑safe)
- Use `utils.path_handler` for all outputs.
- Aux/BA read only `data/cleaned/*_draws.csv`; other tools read combined tables via helpers.
- Pure functions; avoid `os.chdir`; use `pathlib.Path` joins.
- UI: soft‑fail (captions/warnings) instead of raising.

## 4) Verify
- Compile: `python -m py_compile` on changed files.
- Import probes for key modules (show `__file__`).
- Optional: headless boot with log → `.codex/first_boot.log`.

## 5) Update Documentation (always)
- Unified Changelog: `docs/AAT9_KIT/AAT9_Unified_Changelog.md`
  - Entry format: `YYYY‑MM‑DD — Category — Summary — Impact — Files/Refs`
- Checkpoint Log (detailed notes): `docs/AAT9_KIT/AAT9_Checkpoint_Log.md`
  - One short section per change with context, rationale, links
- Affected docs by change type:
  - Structure/paths: update Architecture & Dir Layout; add/adjust Mermaid diagram.
  - Page wiring/data contracts: update App Flow Addendum; note page names and inputs/outputs.
  - New tool/module: add a short “Data Contracts & Where It Lives” block in a relevant doc; link from KIT README.
  - Preflight behavior: update Preflight Reference with example output.
  - Diagrams: follow AAT9_Diagrams_Guide; embed Mermaid blocks in the doc itself.

## 6) Handoff / PR Notes
- Summarize what changed in 5–8 bullets.
- Paste the Changelog entry.
- Include links to updated docs/sections and screenshots/log tails when relevant.

## 7) Templates (copy‑paste)
- Changelog entry:
  - `YYYY‑MM‑DD — <Category> — <Summary> — <Impact> — Files: <paths>; Refs: <docs/sections>`
- Commit/Delivery notes:
  - Goal
  - Files touched
  - Validation (compile/import/smoke)
  - Docs updated (links)
  - Risks/Follow‑ups

## 9) Trigger Phrase
- “document and process” → Agents execute the Post‑Implementation Checklist and return a concise report with links.

## 8) Golden Rules (AAT9)
- Run from repo root; never rely on `C:\Windows\System32` defaults.
- Never change remotes or repo config.
- Keep BA draws‑only; don’t mix combined string‑tables with Aux/BA.
- Keep changes reversible and documented.
