# AAT9 — Planning & Execution Workflow

Combines the “7‑Rule OS” with AAT9’s guardrails for a practical delivery loop.

## 1) Think First
- Read KIT README, Architecture, and relevant docs.
- Run preflight to validate environment and imports.

## 2) Draft a Small Plan
- List exact files to change; keep scope tight.
- Include validation and doc updates you will perform.
- Wait for “Approved” before editing when collaborating.

## 3) Implement Minimal Diffs
- Work path‑safe; use canonical helpers.
- Prefer additive changes; archive legacy rather than delete.

## 4) Verify
- Compile, import‑probe, and optional headless smoke.
- Share log tail and a concise status.

## 5) Document & Log
- Update Unified Changelog with a one‑line summary + impact.
- Update affected docs (Architecture/App Flow/Preflight/Diagrams) as needed.

## 6) Security Pass (lightweight)
- Scan staged diff for accidental secrets/paths.
- Avoid committing credentials or local absolute paths.

## 7) Wrap‑Up & Learn
- Summarize what changed and why.
- Note any pitfalls encountered (update Pitfalls doc if useful).

