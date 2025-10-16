@echo off
REM Copies the AAT9 startup instruction to your clipboard
setlocal
set LINE=Read briefings\CODEX_READ_FIRST_AAT9.md and follow it exactly. Select model preset gpt-5-codex (High), run preflight + Dev Health, then reply: READY.
powershell -NoProfile -Command "Set-Clipboard -Value '%LINE%'"
echo Boot line copied to clipboard. Paste into Codex chat.
endlocal
