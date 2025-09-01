# Hygiene (one-time; already done if .gitignore contains 'project hygiene')

Tasks (if missing):
1) Ensure root `.gitignore` ends with:
   - data/outputs/**
   - artifacts/**
   - reports/**
   - **/*.cache
2) Ensure `artifacts/.gitignore` contains:
   *
   !.gitignore

Codex: If these lines already exist, do nothing. Show a /diff and stop.
Operator: I will commit and push with GitHub Desktop.