# AAT9 — Security & Secrets Checklist

## Before Commit/Delivery
- Review diffs for accidental credentials, API keys, tokens, or PII.
- Ensure logs do not contain sensitive local paths or environment details beyond what’s needed (preflight output is acceptable).
- Verify imports resolve to in‑repo files (no unintended site‑packages shadowing).

## Data Handling
- Read draws and tables only from project data roots (`data/cleaned`, `data/outputs`).
- Do not upload raw data or outputs to external services unless explicitly approved.

## Scripts & Execution
- Never run commands that change Git remotes or repo config.
- Keep timeboxed headless runs; avoid spawning long‑running background jobs.

