@echo off
setlocal enabledelayedexpansion

REM Safe Git checkpoint script for Windows/PowerShell shells
REM Usage: save_checkpoint.bat "your message here"

set "MSG=%*"
if "%MSG%"=="" set "MSG=checkpoint: autosave"

echo [checkpoint] Starting at %DATE% %TIME%

REM Ensure we are inside a git repo
git rev-parse --is-inside-work-tree >NUL 2>&1 || (
  echo [checkpoint] Not a git repository. Aborting.
  exit /b 1
)

REM Ensure user identity is set (non-interactive)
git config user.name >NUL 2>&1 || git config user.name "shona wensley"
git config user.email >NUL 2>&1 || git config user.email "shonawensley@gmail.com"

REM Prevent interactive prompts from hanging
set GIT_TERMINAL_PROMPT=0

echo [checkpoint] Staging changes...
git add -A

echo [checkpoint] Committing (no-verify)...
git commit --no-verify -m "%MSG%" || echo [checkpoint] Nothing to commit

echo [checkpoint] Pushing to origin/main...
git push origin main

echo [checkpoint] Done at %DATE% %TIME%
exit /b 0


