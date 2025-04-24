@echo off
:: run_vtrac_analyzer_standalone.bat
:: Runs the standalone V-TRAC analyzer Streamlit app.
:: This script ONLY performs analysis on existing tables.
:: It assumes tables have already been generated (e.g., using generate_tables_pipeline.bat).
:: This is Step 2 of the ideal workflow.

echo ================================================
echo = Running Standalone V-TRAC Analyzer         =
echo ================================================
echo.

:: Change directory to the location of this batch file (project root)
cd /d "%~dp0"

:: Activate the Python virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment.
    pause
    exit /b 1
)

echo Starting the Standalone V-TRAC Analyzer app...
echo Loading script: scripts/core/vtrac_analyzer_standalone.py
streamlit run scripts/core/vtrac_analyzer_standalone.py

if %errorlevel% neq 0 (
    echo [ERROR] The Streamlit app encountered an error.
) else (
    echo Streamlit app closed.
)

:: Deactivate environment (optional)
:: call deactivate

echo.
echo Press any key to exit...
pause > nul 