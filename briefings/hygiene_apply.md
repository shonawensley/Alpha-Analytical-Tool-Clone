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
- I will stage/commit/push in GitHub Desktop.

# Repo Info

**Local folder**: `C:\dev\Alpha-Analytical-Tool`  (you may rename the folder; Desktop uses the folder name)

**Remote (origin)**: https://github.com/shonawensley/Alpha-Analytical-Tool-Clone.git  (official repo)

Use GitHub Desktop for all commit/push/pull.

Daily: Commit → Push origin → verify your latest commit appears at the top of the file list on GitHub (Clone repo).
