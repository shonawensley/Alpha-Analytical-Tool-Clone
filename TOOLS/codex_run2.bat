@echo off
setlocal EnableExtensions
set "ROOT=C:\dev\Alpha-Analytical-Tool"
cd /d "%ROOT%"

rem --- print codex version so you know which CLI is running ---
where codex
codex --version
echo.

rem --- copy the AAT9 boot line so you can paste it into Codex chat ---
set "LINE=Read briefings\CODEX_READ_FIRST_AAT9.md and follow it exactly. Select model preset gpt-5-codex (High), run preflight + Dev Health, then reply: READY."
powershell -NoProfile -Command "Set-Clipboard -Value '%LINE%'" 2>nul || echo %LINE%|clip
echo [AAT9] Boot line copied to clipboard.
echo.

rem --- launch codex (fallback to npx if PATH is missing) ---
codex --version >nul 2>&1
if errorlevel 1 (
  echo [WARN] 'codex' not on PATH; launching via npx...
  npx @openai/codex@latest
) else (
  codex
)

endlocal
