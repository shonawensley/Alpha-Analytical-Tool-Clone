@echo off
REM Copies the Codex boot instruction to your clipboard
powershell -NoProfile -Command ^
  "Set-Clipboard -Value 'Read briefings\\CODEX_READ_THIS.md and follow it exactly. After config + quick checks, reply: READY.'"

echo Boot line copied to clipboard. Paste into Codex chat.


