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

