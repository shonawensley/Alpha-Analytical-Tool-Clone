# Hygiene (one-time; do nothing if already present)
Tasks (if missing):
1) Ensure root `.gitignore` ends with:
   - data/outputs/**
   - artifacts/**
   - reports/**
   - **/*.cache
2) Ensure `artifacts/.gitignore` contains exactly:
   *
   !.gitignore

Codex:
- If these lines already exist, do nothing. Show a /diff and stop.

Operator:
- Preferred: stage/commit via WSL git (CLI) for large artifact sets; push via GitHub Desktop (optional).

# Repo Info

**WSL repo root (canonical)**: `/home/ser/code/Alpha-Analytical-Tool-Clone`
**GitHub Desktop path (Windows view)**: `\\wsl$\Ubuntu\home\ser\code\Alpha-Analytical-Tool-Clone`

**Remote (origin)**: https://github.com/shonawensley/Alpha-Analytical-Tool-Clone.git  (official repo)

GitHub Desktop note:
- Desktop can freeze on very large commits (sharepacks CSV/JSON/HTML). If so, commit via WSL CLI and use Desktop only to push.

Daily: Commit → Push origin → verify your latest commit appears at the top of the file list on GitHub (Clone repo).
