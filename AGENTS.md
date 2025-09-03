Codex Agent Operating Rules (Project-Specific)

Project root: C:\dev\Alpha-Analytical-Tool

Purpose: Eliminate workingâ€‘directory mistakes, keep changes surgical, and protect nonâ€‘Aux pipelines while we implement features like Blackapple.

Core Principles

- Always run from repo root: Every command and patch must execute with the working directory set to the project root. Never operate relative to C:\Windows\System32.
- Minimal diffs: Small, targeted edits; never refactor broadly without an explicit task and plan.
- Guard pipelines: Do not touch combined stringâ€‘table extraction or readers (Vâ€‘TRAC, Stable Pattern, Digit Reduction) unless explicitly requested. Blackapple and Aux work only consume CSV draws under data/cleaned.
- Ask before change: Show the plan and intended diffs; pause before destructive actions.

Path Preflight (must run/verify before changes)

- CWD gate: Ensure the shell is at C:\dev\Alpha-Analytical-Tool (use .codex/always_root.ps1 or pushd "%~dp0").
- Import check: python -c "import modules.blackapple as ba; print(ba.__file__)" should point inside the repo.
- Data presence: Verify data/cleaned/*_draws.csv exist for target states; print which file will be used.
- Log location: Confirm .codex/first_boot.log is the headless boot target when testing.

Working Directory Discipline

- Shell commands: Always pass workdir=C:\dev\Alpha-Analytical-Tool (or pushd "%~dp0" in .bat) before running tools.
- Patches: When using apply_patch, ensure the process runs from repo root; never let patches target System32.
- Scripts: Prefer .codex/always_root.ps1 to set the working dir for any adâ€‘hoc runs.

Path & Imports Hygiene

- Streamlit entry (src/app.py) already bootstraps PROJECT_ROOT onto sys.path; keep it.
- BAT launchers must pushd to repo root, then call: streamlit run src\app.py
- Never rely on the current shellâ€™s default CWD; make it explicit.

Data Source Rules

- Aux & Blackapple draws: Only read data/cleaned/*_draws.csv (newestâ€‘first List[str]).
- Do not read the *_cleaned.xlsx stringâ€‘table files for BA; those belong to other analytical tools.
- Show a small caption with the actual draw source path and count for validation.

Execution & Logging

- Headless boot: STREAMLIT_BROWSER=none; timebox to 120s; capture logs to .codex/first_boot.log; stop the job cleanly.
- Diagnostics: Print ENTRY and (optional) CWD in the Streamlit sidebar during development.

Safety & Approvals

- yolo=false mindset: Confirm before writes or commands that change state. Prefer readâ€‘only exploration first.
- Never write outside the repo; never touch remotes or Git settings unless instructed.

Quality Settings

- Reasoning effort: High. Plan â†’ implement â†’ verify. Show diffs and log tails when relevant.
- Determinism: Pure functions for analyzers; cache I/O results with sensible TTLs.

Checklist Before Any Edit

1) Confirm cwd == C:\dev\Alpha-Analytical-Tool (or use .codex/always_root.ps1)
2) Run quick sanity: git status -s, git branch -vv, git remote -v (printâ€‘only)
3) State the exact files to change and why; show the minimal diffs
4) After change, validate via smoke/headless boot and share the log tail

Do Not Edit (Unless Task Says So)

- core_legacy/**
- Combined table extraction logic and its stringâ€‘table readers
- Git remotes, repo config

OK To Edit (Taskâ€‘scoped)

- modules/** (new modules, e.g., blackapple, aux_loaders)
- src/app.py (minimal pageâ€‘level wiring only)
- scripts/** (smoke tests, helpers)
- briefings/** (docs)

Blast Radius & Change Containment

- Scope discipline: Only touch files explicitly in scope for the current task. Do not edit working tools or pipelines outside that scope.
- Default read‑only: Prefer adding new modules/helpers over modifying shared code. If a hook is needed, keep it minimal and reversible.
- UI gating: New features render behind existing buttons/toggles; never break existing pages on import failure (use try/except with user‑friendly captions).
- Soft‑failure first: On missing data/imports, show a caption/warning instead of raising; log details to .codex/first_boot.log during validation.
- Rapid revert: Keep diffs small so any regression can be undone quickly.
