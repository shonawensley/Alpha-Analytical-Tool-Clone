@echo off
setlocal EnableExtensions

rem === Adjust only if your repo root is in a different folder ===
set "ROOT=C:\dev\Alpha-Analytical-Tool"

if not exist "%ROOT%\.git" (
  echo [ERROR] Repo not found at %ROOT%
  pause
  exit /b 1
)

pushd "%ROOT%"
echo === Repo root ===
echo %CD%
echo.

echo === Sanity ===
where node
node -v
npm -v
echo.

echo === Codex on PATH? ===
where codex
codex --version
echo.

rem --- Copy the AAT9 boot line to clipboard (primary) ---
set "LINE=Read briefings\CODEX_READ_FIRST_AAT9.md and follow it exactly. Select model preset gpt-5-codex (High), run preflight + Dev Health, then reply: READY."
powershell -NoProfile -Command "Set-Clipboard -Value '%LINE%'" 2>nul || (
  echo PowerShell clipboard failed; using fallback...
  echo %LINE%|clip
)
echo Boot line copied. Paste it into the new Codex chat.
echo.

echo === Launching Codex (with fallback) ===
rem Try installed codex first; if not found, fall back to npx
codex --version >nul 2>&1
if errorlevel 1 (
  echo codex not found on PATH; using npx fallback...
  npx @openai/codex@latest
) else (
  codex
)

popd
echo.
pause
endlocal
