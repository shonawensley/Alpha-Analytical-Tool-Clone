@echo off
setlocal EnableExtensions EnableDelayedExpansion

REM Timestamp for tag/commit
for /f %%i in ('powershell -NoProfile -ExecutionPolicy Bypass -Command "(Get-Date).ToString('yyyyMMdd_HHmmss')"') do set TS=%%i

REM Stage all changes
git add -A

REM Commit with message (use args if provided)
set MSG=%*
if "%MSG%"=="" set MSG=checkpoint %TS%
git commit -m "%MSG%"

REM Create annotated tag
set TAG=v-checkpoint-%TS%
git tag -a %TAG% -m "%MSG%"

REM Push branch and tags (non-interactive if credentials cached)
git push origin HEAD
git push origin --tags

echo Created checkpoint tag %TAG% with message: %MSG%
endlocal

