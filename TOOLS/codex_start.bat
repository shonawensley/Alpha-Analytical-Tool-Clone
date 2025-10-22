@echo off
setlocal
set ROOT=C:\dev\Alpha-Analytical-Tool
set BOOT=%ROOT%\briefings\codex_boot.md

if not exist "%ROOT%\.git" (
  echo [ERROR] Repo not found at %ROOT%
  pause
  exit /b 1
)

pushd "%ROOT%"
echo === Repo quick status ===
git status -s
git branch -vv
git remote -v
echo =========================
echo.

REM Open the universal boot file so you can review/tweak it
if exist "%BOOT%" start "" notepad "%BOOT%"

REM Put a clean one-liner into your clipboard to paste into Codex
powershell -NoLogo -NoProfile -Command ^
  Set-Clipboard -Value 'Read briefings\codex_boot.md and follow it exactly. After config + quick checks, reply: READY.'

echo Copied to clipboard:
echo Read briefings\codex_boot.md and follow it exactly. After config + quick checks, reply: READY.
echo.
echo Now paste that into Codex chat. When Codex replies READY, give it your task file path.
popd
pause
