@echo OFF
setlocal EnableDelayedExpansion

REM Set console colors for better visibility
color 0F

echo [92m=== Stable Pattern Extractor ===[0m

REM Get the directory of the batch script
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=!SCRIPT_DIR:~0,-1!"

REM Try to activate virtual environment (check both .venv and venv)
set "VENV_ACTIVATED=0"
if exist "!SCRIPT_DIR!\.venv\Scripts\activate.bat" (
    echo [96mActivating virtual environment from .venv...[0m
    call "!SCRIPT_DIR!\.venv\Scripts\activate.bat"
    set "VENV_ACTIVATED=1"
) else if exist "!SCRIPT_DIR!\venv\Scripts\activate.bat" (
    echo [96mActivating virtual environment from venv...[0m
    call "!SCRIPT_DIR!\venv\Scripts\activate.bat"
    set "VENV_ACTIVATED=1"
) else (
    echo [93mWarning: No virtual environment found (.venv or venv)[0m
    echo [93mRunning with system Python - this might fail if dependencies aren't installed globally[0m
)

REM Check if pandas and streamlit are installed
python -c "import pandas" 2>nul
if errorlevel 1 (
    echo [91mError: pandas is not installed. Please run: pip install pandas[0m
    goto :EOF
)
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo [91mError: streamlit is not installed. Please run: pip install streamlit[0m
    goto :EOF
)

REM Define and create output directory
set "OUTPUT_DIR=!SCRIPT_DIR!\data\outputs\stable_patterns"
if not exist "!OUTPUT_DIR!" (
    echo [96mCreating output directory: !OUTPUT_DIR![0m
    mkdir "!OUTPUT_DIR!"
)

REM Define state name and paths (configurable)
set "STATE_NAME=Indiana4"
set "INPUT_DIR=!SCRIPT_DIR!\data\outputs\tables\!STATE_NAME!"

REM Define input files
set "MIDDAY_FILE=!INPUT_DIR!\!STATE_NAME!_Midday_combined.csv"
set "EVENING_FILE=!INPUT_DIR!\!STATE_NAME!_Evening_combined.csv"
set "COMBINED_FILE=!INPUT_DIR!\!STATE_NAME!_Combined_combined.csv"

REM Define output files
set "HTML_OUTPUT=!OUTPUT_DIR!\!STATE_NAME!_stable_patterns_report.html"
set "CSV_OUTPUT=!OUTPUT_DIR!\!STATE_NAME!_stable_patterns_scores.csv"

REM Validate input files exist
set "MISSING_FILES=0"
if not exist "!MIDDAY_FILE!" (
    echo [91mError: Missing Midday file: !MIDDAY_FILE![0m
    set "MISSING_FILES=1"
)
if not exist "!EVENING_FILE!" (
    echo [91mError: Missing Evening file: !EVENING_FILE![0m
    set "MISSING_FILES=1"
)
if not exist "!COMBINED_FILE!" (
    echo [91mError: Missing Combined file: !COMBINED_FILE![0m
    set "MISSING_FILES=1"
)

if !MISSING_FILES! equ 1 (
    echo [91mCannot proceed - missing input files[0m
    goto :EOF
)

echo [96mProcessing files for !STATE_NAME!:[0m
echo   Midday   : !MIDDAY_FILE!
echo   Evening  : !EVENING_FILE!
echo   Combined : !COMBINED_FILE!
echo.

REM Run the pattern extractor
echo [92mRunning Stable Pattern Extractor...[0m
python "!SCRIPT_DIR!\scripts\tools\stable_pattern_extractor.py" ^
    --files "!MIDDAY_FILE!" "!EVENING_FILE!" "!COMBINED_FILE!" ^
    --html "!HTML_OUTPUT!" ^
    --csv "!CSV_OUTPUT!"

if errorlevel 1 (
    echo.
    echo [91mStable Pattern Extractor FAILED[0m
    echo Please check the error messages above
) else (
    echo.
    echo [92mStable Pattern Extractor completed successfully![0m
    echo [96mOutputs:[0m
    echo   HTML Report: !HTML_OUTPUT!
    echo   CSV Scores : !CSV_OUTPUT!
    
    REM Try to open the HTML report automatically
    echo.
    set /p "OPEN_HTML=Would you like to open the HTML report now? (Y/N) "
    if /i "!OPEN_HTML!"=="Y" (
        start "" "!HTML_OUTPUT!"
    )
)

:EOF
echo.
echo [96mPress any key to exit...[0m
pause >nul