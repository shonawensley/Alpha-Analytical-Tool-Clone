# AAT9 — Task Template (Paste into ticket/brief)

## Goal
- One sentence on the desired outcome.

## Scope (files/areas)
- Files to change:
- Files explicitly out of scope:

## Plan (small steps)
1) …
2) …
3) …

## Data Contracts (if applicable)
- Reads: draws / combined tables / other
- Writes: `data/outputs/analysis/<tool>/<STATE>/…`

## Validation
- Preflight: `.codex/preflight.ps1 -State "…"`
- Compile: `python -m py_compile <files>`
- Import probes: resolve `__file__` in key modules
- Optional headless boot: log tail from `.codex/first_boot.log`

## Documentation to Update
- Changelog (KIT): add entry
- Architecture & Dir Layout (if paths/dirs change)
- App Flow Addendum (if page wiring/contracts change)
- Preflight Reference (if preflight behavior changes)

## Risks & Revert
- Risks:
- Revert steps:

## Done When
- [ ] App launches from `run_app.bat`
- [ ] Pages render without path errors
- [ ] Tests/checks above pass
- [ ] Docs updated (links pasted here)
- [ ] Changelog entry added

