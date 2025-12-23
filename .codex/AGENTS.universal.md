Codex Universal Agent Rules

Scope: These nonâ€‘negotiable rules apply to all work done by Codex in this repository. Projectâ€‘specific guidance may extend these rules but may not relax them.

Nonâ€‘Negotiables

- Working Directory: Always operate from the project root: C:\dev\Alpha-Analytical-Tool. Never run or write from C:\Windows\System32 or any other directory.
- Working Directory: Always operate from the project root: `/home/ser/code/Alpha-Analytical-Tool-Clone` (WSL canonical). Windows view of the same tree: `\\wsl$\Ubuntu\home\ser\code\Alpha-Analytical-Tool-Clone`. Never run or write from `C:\Windows\System32` or any other directory.
- Write Bounds: Never write outside the repo. No temp files outside .codex/ without approval. No edits to Git remotes/config.
- Reasoning Mode: Highâ€‘effort by default. Plan â†’ implement â†’ verify. Show minimal diffs and log tails for meaningful changes.
- Approvals: Ask before executing stateâ€‘changing commands. Prefer readâ€‘only exploration first.
- Minimal Diffs: Keep edits small and targeted. Avoid refactors unless explicitly requested with a plan.
- Path Hygiene: Make cwd explicit in every shell/patch call. For scripts, pushd to repo root before running.
- Logging: Timebox longâ€‘running tasks. Capture app boots to .codex/first_boot.log, then stop the job.

Data Contracts (Highâ€‘Level)

- Combined stringâ€‘tables (for Vâ€‘TRAC / Stable Pattern / Digit Reduction) are separate from Aux draws. Do not conflate them.
- Aux / Blackapple consume only CSV draws under data/cleaned/*_draws.csv (newestâ€‘first strings). Do not rely on *_cleaned.xlsx for BA.

Operational Defaults

- BAT launchers must pushd to the repo root before calling streamlit run src\app.py.
- Streamlit runs headless during automation: set STREAMLIT_BROWSER=none.
- Prefer Python module runs via python -m when addressing import path questions.

Developer Utilities

- .codex/always_root.ps1: Force the shell CWD to the repo root and print it.
- AGENTS.md: Projectâ€‘specific rules and context. Read it with this document.

Enforcement Checklist (before any change)

1) Confirm cwd is the repo root.
2) Print git status/branch/remotes (readâ€‘only).
3) State intended changes and why; ensure scope is minimal.
4) After changes, validate via smoke/headless boot; share logs succinctly.


Path Preflight (before any tests/changes)

- Run .codex/always_root.ps1 to force CWD to the repo root and print it.
- Run a Python import check: python -c "import modules.blackapple as ba, sys; print('BA from:', ba.__file__)"; ensure it points inside the repo.
- List candidate draw CSVs: `ls data/cleaned/*_draws.csv` (WSL) or `dir data\cleaned\*_draws.csv` (Windows). For a given state, confirm the exact file to be used.
- If any step fails, fix the first issue only (cwd/import/data) before proceeding.

Blast Radius (always minimize)

- Only modify files directly required for the task; avoid side effects in unrelated modules/pipelines.
- Favor additive changes (new modules, local hooks) over edits to shared code.
- Guard new imports/paths with try/except and clear UI captions; do not crash pages.
- Keep diffs small and reversible; revert quickly if a regression is observed.
