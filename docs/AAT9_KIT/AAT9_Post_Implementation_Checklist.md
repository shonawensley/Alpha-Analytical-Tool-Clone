# AAT9 — Post‑Implementation Checklist

Use this checklist at the end of a feature/fix to finalize deliverables and keep docs in sync. You can say “document and process” to prompt an AI to execute these steps.

## Steps
- Validation
  - [ ] `python -m py_compile` on changed files
  - [ ] Import probes: key modules resolve to in‑repo files
  - [ ] Optional headless boot (120s) with log tail from `.codex/first_boot.log`
  - [ ] Optional preflight with `-CheckTables` if Stable/DR/V‑TRAC touched
- Documentation & Logging
  - [ ] Unified Changelog: add a meaningful one‑line entry with category + impact
  - [ ] Checkpoint Log: add a brief, structured note with context, rationale, links
  - [ ] Architecture/App Flow: update if directory layout or page wiring changed
  - [ ] Diagrams (Mermaid): update blocks where flows/paths changed
- Handoff
  - [ ] Short summary (what changed, why, proof) and links to updated docs

## Trigger Phrase
- Say: “document and process”
  - Agents should run the steps above, then summarize changes + provide links/log tail.

