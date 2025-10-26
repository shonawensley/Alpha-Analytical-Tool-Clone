# CODEX READ THIS — AAT9 (WSL / Ubuntu Canonical)

**This document supersedes any Windows‑first startup docs.**  
All development happens in **WSL**. The only Windows touchpoint is **GitHub Desktop** pushing from the WSL path.

---

## 0) Canonical paths & repo sanity

- **Repo root (CWD, canonical):** `/home/ser/code/Alpha-Analytical-Tool-Clone`
- **GitHub Desktop path (Windows view of the same tree):** `\\wsl$\Ubuntu\home\ser\code\Alpha-Analytical-Tool-Clone`
- **Remote (origin):** `https://github.com/shonawensley/Alpha-Analytical-Tool-Clone.git`

**Print‑only sanity (no writes):**
```bash
cd ~/code/Alpha-Analytical-Tool-Clone
git status -s && git branch -vv && git remote -v && pwd
1) Reading order (AAT9 KIT first)

docs/AAT9_KIT/AAT9_KIT_README.md

docs/AAT9_KIT/AAT9_Workflow_Standard.md

docs/AAT9_KIT/Practices/AAT9_Coding_Standards.md

docs/AAT9_KIT/Practices/AAT9_Agent_Operating_Rules.md

docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md

docs/AAT9_KIT/AAT9_Preflight_Reference.md

docs/AAT9_KIT/AAT9_Diagrams_Guide.md

docs/AAT9_KIT/AAT9_Unified_Changelog.md

AGENTS.md, .codex/AGENTS.universal.md

Data contracts recap (enforced in code & docs):

Aux / Blackapple → data/cleaned/*_draws.csv (draws‑only).

V‑TRAC / Stable / Digit Reduction → combined tables via utils.path_handler
(e.g., data/outputs/tables/<STATE>/ or tables/<STATE>/).

“Combined” is baseline; “Midday/Evening” are additive variants surfaced alongside.

2) WSL alignment & PowerShell bridging

Always treat the repo root as: /home/ser/code/Alpha-Analytical-Tool-Clone

To call a Windows PowerShell script from WSL (only when necessary):

powershell.exe -NoProfile -File "$(wslpath -w .)\path\to\script.ps1"


If pushing from Windows, use GitHub Desktop on:

\\wsl$\Ubuntu\home\ser\code\Alpha-Analytical-Tool-Clone

3) Preflight (run when requested)

From WSL:

powershell.exe -NoProfile -File "$(wslpath -w .)\.codex\preflight.ps1" -State "Connecticut4"


Fix a single root cause at a time (cwd/import/data), then re‑run.
When preflight is clean and the Plan is printed, reply READY (WSL).

4) Plan → Implement → Verify → Document (the loop)

Plan (short, explicit): files to touch and why; keep diffs minimal.

Implement: follow utils.path_handler; respect the data‑contract rules.

Verify: compile + optional smoke boot

python3 -m py_compile $(git ls-files '*.py') || true
# optional: 120s headless boot
# STREAMLIT_BROWSER=none streamlit run src/app.py & sleep 120; pkill -f streamlit


Document: always append to

docs/AAT9_KIT/AAT9_Unified_Changelog.md (one line, concise)

and any affected KIT docs.

5) Git workflow (Desktop only)

Edit in WSL; commit/push in GitHub Desktop (same WSL path).

Local checkpoint (only if asked; no editor popup):

git add -A
git commit -m "checkpoint: WSL startup doc finalized"
# prefer pushing in GitHub Desktop


Never edit Git remotes/config. Never write outside the repo.

6) Guardrails (for Codex)

Allowed without asking:

Read/list anywhere inside the repo

Edit under docs/**, .codex/** (docs, logs, images)

python3 -m py_compile, the preflight command above

Ask first:

Edits under src/**, modules/**, utils/**, alpha_analytical/**

Any Streamlit run beyond the optional 120s smoke boot

Any Git operation beyond read‑only status printouts

Never:

Change origin or any remotes

Write outside the repository tree

7) Troubleshooting quickies

VS Code shows old changes but Desktop is clean? VS Code Git noise—Desktop is the source of truth.
Push/commit feels “stuck”? Clear stale flows/locks then return to Desktop:

[ -f .git/index.lock ] && rm -f .git/index.lock
git rebase --abort 2>/dev/null || true
git merge  --abort 2>/dev/null || true
git am     --abort 2>/dev/null || true
git cherry-pick --abort 2>/dev/null || true
git status -sb

8) Finish signal

When the Plan is printed and Preflight is clean, reply:

READY (WSL)