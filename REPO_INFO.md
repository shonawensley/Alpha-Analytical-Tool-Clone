# Repo Info

**Local folder (WSL)**: /home/ser/code/Alpha-Analytical-Tool-Clone  
**Windows access**: \\wsl$\Ubuntu-22.04\home\ser\code\Alpha-Analytical-Tool-Clone (Explorer → copy path)  
**Legacy folder**: C:\dev\Alpha-Analytical-Tool (keep only as an archive/backup)

**Remote (origin)**: https://github.com/shonawensley/Alpha-Analytical-Tool-Clone.git  (official repo for both WSL + Windows)

**Git workflow**
- Run every git command from the WSL repo root; `pwd` should print `/home/ser/code/Alpha-Analytical-Tool-Clone`.
- Use GitHub Desktop (pointed at the WSL path) for push/pull, or push from WSL once PAT auth is confirmed.
- Quick health checks: `git status -sb`, `git branch -vv`, `git remote -v` before/after commits.

## AAT9 KIT (Curated Docs)
- Start here: docs/AAT9_KIT/AAT9_KIT_README.md (Quickstart, Workflow, Practices, Changelog)
- Canonical app entry: run_app.bat -> streamlit run src\\app.py (repo root)
- Preflight: powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"

Daily: Commit → Push origin → verify the latest commit appears at the top of the file list on GitHub.

