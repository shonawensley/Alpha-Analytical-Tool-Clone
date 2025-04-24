@echo off
:: generate_tables_pipeline.bat
:: Runs the Python script to clean data, extract sets, and generate all CSV tables.
:: This is Step 1 of the ideal workflow.

echo ================================================
echo = Running Table Generation Pipeline          =
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

echo Running the pipeline script (scripts/core/generate_tables_pipeline.py)...
echo This may take several minutes depending on the data...
python scripts/core/generate_tables_pipeline.py

if %errorlevel% neq 0 (
    echo [ERROR] The pipeline script encountered an error.
) else (
    echo Pipeline completed successfully.
)

:: Deactivate environment (optional, happens automatically on exit)
:: call deactivate

echo.
echo Press any key to exit...
pause > nul 