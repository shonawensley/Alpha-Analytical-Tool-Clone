Codex Optimal Workflow (This Repository)

Banner: For the curated, up‑to‑date AAT9 documentation and workflow, see docs/AAT9_KIT/AAT9_KIT_README.md.

Purpose: A practical, repeatable flow Codex follows in this repo. Pairs with .codex/AGENTS.universal.md and AGENTS.md.

0) Ground Rules (always)
- CWD: C:\dev\Alpha-Analytical-Tool (use .codex/always_root.ps1 or pushd "%~dp0").
- Writes only inside the repo; scratch/logs go to .codex/.
- Reasoning effort high; show small diffs; ask before state changes.
- Guard pipelines: do not touch combined stringâ€‘table extraction unless explicitly requested.

1) Startup & Sanity`n`nPath Preflight (must pass before coding)`n`n- Run .codex/always_root.ps1; confirm CWD is the repo root.`n- Run import check: python -c "import modules.blackapple as ba; print(ba.__file__)".`n- List data/cleaned/*_draws.csv; confirm the expected file per state.
- Read briefings/CODEX_READ_THIS.md â†’ run briefings/codex_boot.md steps (printâ€‘only):
  - git status -s; git branch -vv; git remote -v (confirm origin).
- Check hygiene (briefings/hygiene_apply.md) â€” print diffs only if needed.
- Read recent AAT9 checkpoints in docs/AAT9_DOCS (esp. 2025â€‘09â€‘01) for context.

2) Plan
- Extract deliverables + file list to add/modify.
- Write a oneâ€‘screen plan with minimal edits (surgical), including where to wire UI.
- Confirm scope and guardrails (no refactors; no pipeline changes).

3) Implement (small diffs)
- Create/modify only the targeted files (e.g., modules/blackapple.py, modules/aux_loaders.py, src/app.py UI hooks, scripts/smoke/*).
- Ensure imports/paths are robust (PROJECT_ROOT on sys.path; BATs pushd to root).
- For Aux/BA: consume only data/cleaned/*_draws.csv; never use *_cleaned.xlsx.

4) Validate`n`nFirst Failure Policy`n`n- Stop at the first real error (cwd/import/data/port). Apply a minimal, targeted fix, then re-run the preflight/validation.
- Smoke tests first (python -m scripts.smoke.<name>) to confirm imports + core logic.
- Headless boot Streamlit (120s timebox) with logs to .codex/first_boot.log; stop cleanly.
- If a failure appears, propose the smallest fix for the first error only; retry.

5) Show Work
- Provide a concise changeset summary (files added/modified, key functions),
  a short log tail, and a manual test checklist.
- Include proof snippets (e.g., panel/table render confirmed, draw source caption path).

6) Troubleshooting Cheatsheet
- Import errors: ensure cwd is root; verify modules/__init__.py; insert PROJECT_ROOT on sys.path at entry; add fallback import inside the specific page block.
- Missing data: verify data/cleaned/*_draws.csv exist; show a helpful warning in UI when not present.
- Port in use: bump port (8502) and reâ€‘run; keep timebox.

7) Do / Donâ€™t
- Do: Keep diffs minimal; cache heavy I/O with st.cache_data; print the draw source path in BA panels.
- Donâ€™t: Change combined stringâ€‘table logic or refactor unrelated modules.

8) Delivery
- Stop after a green headless boot and UI confirmation. Await operator review/commit.


