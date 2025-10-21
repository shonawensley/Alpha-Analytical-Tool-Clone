# CODEX READ FIRST — AAT9 (WSL/Ubuntu Optimized)

Follow this sequence each session. Goal: reliable setup, path-safe execution, and consistent docs.

---

## 0) Operating assumptions (WSL/Ubuntu)
- Running inside **Ubuntu on WSL2** (prompt like `ser@…:~$`).
- Project root (CWD) is **`/home/ser/code/Alpha-Analytical-Tool-Clone`**.
  - **Never** work under `/mnt/c/...` (slow I/O and path quirks).
- Windows scripts can be called via `powershell.exe` using `wslpath` to convert paths.

---

## 1) Session setup
- Model preset: **`gpt-5-codex` (High)**. Use Medium for routine edits only.
- Reasoning: high effort; **yolo=false** (ask before destructive changes).

**Force CWD & print-only sanity:**
```bash
cd ~/code/Alpha-Analytical-Tool-Clone
git status -s && git branch -vv && git remote -v && pwd
2) Read these (KIT first)
Read in this order:

docs/AAT9_KIT/AAT9_KIT_README.md

docs/AAT9_KIT/AAT9_Workflow_Standard.md

docs/AAT9_KIT/Practices/AAT9_Coding_Standards.md

docs/AAT9_KIT/Practices/AAT9_Agent_Operating_Rules.md

docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md

docs/AAT9_KIT/AAT9_Preflight_Reference.md

docs/AAT9_KIT/AAT9_Diagrams_Guide.md

docs/AAT9_KIT/AAT9_Unified_Changelog.md

AGENTS.md and .codex/AGENTS.universal.md

WSL alignment:

Treat repo root as /home/ser/code/Alpha-Analytical-Tool-Clone.

To call a Windows PowerShell script from WSL:

bash
Copy code
powershell.exe -NoProfile -File "$(wslpath -w .)\path\to\script.ps1"
3) Preflight (run now)
bash
Copy code
powershell.exe -NoProfile -File "$(wslpath -w .)\.codex\preflight.ps1" -State "Connecticut4"
Fix one root cause at a time (cwd/import/data), then re-run. Preflight must be clean.

3.5) Dev Health (optional)
Only toggle Dev Health in the Streamlit UI when requested.

Linux app launch (when needed):

bash
Copy code
STREAMLIT_BROWSER=none python3 -m py_compile $(git ls-files '*.py') || true
streamlit run src/app.py
4) Plan → Implement → Verify → Document
Plan: list files to edit and why; keep diffs minimal.

Implement: use utils.path_handler; data contracts:

Aux/Blackapple → data/cleaned/*_draws.csv (newest-first strings)

V-TRAC / Stable / Digit Reduction → combined tables via utils.path_handler

Verify:

bash
Copy code
python3 -m py_compile $(git ls-files '*.py') || true
# optional headless boot for 120s:
# STREAMLIT_BROWSER=none streamlit run src/app.py & sleep 120; pkill -f streamlit
Document: append to docs/AAT9_KIT/AAT9_Unified_Changelog.md; update affected docs.

5) Done checklist
App runs from streamlit run src/app.py without path/import errors.

Changes logged in AAT9_Unified_Changelog.md.

Architecture/app-flow docs updated if wiring changed.

Guardrails & approvals (WSL-aware)
Never write outside the repo. Never edit Git remotes/config.

Ask before: changing analyzers/pipelines/wiring; long-running jobs.

Allowed without asking: docs under docs/**, .codex/**; python3 -m py_compile; the preflight above.

Path & tool hygiene (WSL)
Use Linux tools: python3, pip3, node, npm, git.

Version check:

bash
Copy code
python3 --version && pip3 --version && node -v && npm -v
Avoid /mnt/c/.... Convert paths for Windows scripts with:

bash
Copy code
powershell.exe -NoProfile -File "$(wslpath -w .)\path\to\script.ps1"
Finish signal
When preflight is clean and the Plan is printed, reply: READY (WSL) and proceed within the agreed scope.