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
