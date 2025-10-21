CODEX_READ_FIRST_AAT9_WSL.md

# CODEX READ FIRST — AAT9 (WSL/Ubuntu Optimized)

Follow this sequence each session. Goal: reliable setup, path‑safe execution, and consistent docs.

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

docs/AAT9_KIT/AAT9_KIT_README.md (index)

docs/AAT9_KIT/AAT9_Workflow_Standard.md (workflow)

docs/AAT9_KIT/Practices/AAT9_Coding_Standards.md (path‑safe coding)

docs/AAT9_KIT/Practices/AAT9_Agent_Operating_Rules.md (guardrails)

docs/AAT9_KIT/AAT9_Quickstart_Cheat_Sheet.md (daily flow)

docs/AAT9_KIT/AAT9_Preflight_Reference.md (expected outputs)

docs/AAT9_KIT/AAT9_Diagrams_Guide.md (Mermaid updates)

docs/AAT9_KIT/AAT9_Unified_Changelog.md (how to log)

AGENTS.md (project-specific) and .codex/AGENTS.universal.md (global rules)

WSL alignment notes

Treat repo root as /home/ser/code/Alpha-Analytical-Tool-Clone.

To invoke a Windows PowerShell script from WSL:

powershell.exe -NoProfile -File "$(wslpath -w .)\path\to\script.ps1"

3) Preflight (run now)

Run the PowerShell preflight from Linux using powershell.exe:

powershell.exe -NoProfile -File "$(wslpath -w .)\.codex\preflight.ps1" -State "Connecticut4"


Fix exactly one root cause at a time (cwd/import/data), then re-run.
Preflight must be clean before coding.

(If a helper exists you may also call preflight Connecticut4.)

3.5) Dev Health (optional)

Only toggle Dev Health in the Streamlit UI when explicitly requested.
Skip it during startup if it stalls or isn’t needed for this session.

Linux app launch (when needed):

# optional quick compile check
STREAMLIT_BROWSER=none python3 -m py_compile $(git ls-files '*.py') || true
# run the app
streamlit run src/app.py


Windows .bat launchers are for Windows shells. Inside WSL, prefer streamlit run above.

4) Plan → Implement → Verify → Document

Plan: list files to edit and why; keep diffs minimal.

Implement: use utils.path_handler for outputs; respect data contracts:

Aux/Blackapple → data/cleaned/*_draws.csv (newest‑first strings)

V‑TRAC / Stable / Digit Reduction → combined string tables via utils.path_handler

Verify:

python3 -m py_compile $(git ls-files '*.py') || true
# optional headless boot for 120s:
# STREAMLIT_BROWSER=none streamlit run src/app.py & sleep 120; pkill -f streamlit


Capture logs to .codex/first_boot.log when relevant.

Document: always append to docs/AAT9_KIT/AAT9_Unified_Changelog.md.
Update affected KIT docs/diagrams as needed.

5) Done checklist

App runs from streamlit run src/app.py without path/import errors.

Changes logged in AAT9_Unified_Changelog.md.

Architecture/app‑flow docs updated if wiring changed.

Guardrails & approvals (WSL‑aware)

Never write outside the repo. Never edit Git remotes/config.

Ask before: changing analyzers, pipelines, or app wiring; long‑running jobs.

Allowed without asking: docs under docs/**, .codex/**; python3 -m py_compile; the preflight command.

Path & tool hygiene (WSL)

Use Linux tools: python3, pip3, node, npm, git.

Version check (read‑only):

python3 --version && pip3 --version && node -v && npm -v


Avoid /mnt/c/... for real work.

Convert paths for Windows scripts with:

powershell.exe -NoProfile -File "$(wslpath -w .)\path\to\script.ps1"

Finish signal

When preflight is clean and the Plan is printed, reply: READY (WSL) and proceed within the agreed scope.