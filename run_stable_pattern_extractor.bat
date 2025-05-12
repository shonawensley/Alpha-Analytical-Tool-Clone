@echo off
set "SCRIPT_DIR=%~dp0"

set "STATE_NAME=Indiana4"
set "INPUT_DIR=%SCRIPT_DIR%data\outputs\tables\%STATE_NAME%"
set "MIDDAY_FILE=%INPUT_DIR%\%STATE_NAME%_Midday_combined.csv"
set "EVENING_FILE=%INPUT_DIR%\%STATE_NAME%_Evening_combined.csv"
set "COMBINED_FILE=%INPUT_DIR%\%STATE_NAME%_Combined_combined.csv"

set "OUTPUT_DIR=%SCRIPT_DIR%data\outputs\stable_patterns"
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"
set "HTML_OUTPUT=%OUTPUT_DIR%\%STATE_NAME%_stable_patterns_report.html"
set "CSV_OUTPUT=%OUTPUT_DIR%\%STATE_NAME%_stable_patterns_scores.csv"

echo === Stable Pattern Extractor ===
python "%SCRIPT_DIR%scripts\tools\stable_pattern_extractor.py" ^
    --files "%MIDDAY_FILE%" "%EVENING_FILE%" "%COMBINED_FILE%" ^
    --html "%HTML_OUTPUT%" ^
    --csv  "%CSV_OUTPUT%"
pause