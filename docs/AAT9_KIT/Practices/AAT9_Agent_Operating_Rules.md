# AAT9 — Agent Operating Rules (Codex/Claude)

## Non‑Negotiables
- Run from repo root; do not rely on shell defaults.
- Never write outside the repo; logs/scratch go under `.codex/`.
- Don’t change remotes or repo config; commits/pushes via Desktop (if applicable).
- Timebox headless boots to 120s; write logs to `.codex/first_boot.log`; stop cleanly.

## Allowed Edits (default)
- `docs/**`, `briefings/**`, `scripts/**`, `src/**` (task‑scoped wiring), `modules/**` (new modules), `alpha_analytical/**` (stable extractor only as needed).

## Guarded Areas
- Don’t touch combined string‑table readers or core_legacy unless explicitly requested.
- Maintain BA draws‑only separation; do not mix Aux/BA with combined tables.

## Working Discipline
- Plan → implement → verify → document (update Unified Changelog).
- Use small, reversible diffs; propose move maps before structural changes; archive‑first, no deletions.
- For page failures: render soft captions; do not crash the app.

