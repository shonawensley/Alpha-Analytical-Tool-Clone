@echo off
echo ========================================
echo V-TRAC TABLE TEST APPLICATION
echo ========================================
echo This is a simplified test version to verify
echo that the V-TRAC table displays correctly.
echo.

REM Change to script directory
cd /d "%~dp0"

REM Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo No virtual environment found, running with system Python...
)

REM Run the Streamlit app
echo Starting Streamlit app...
streamlit run scripts/auxiliary/vtrac_test.py

echo.
echo Application closed.
pause 