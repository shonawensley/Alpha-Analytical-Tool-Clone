@echo off
echo ======================================
echo Advanced V-TRAC Analysis Tool
echo ======================================
echo This tool provides enhanced analytical features with weighted metrics
echo.

rem Change to the script's directory
cd /d "%~dp0"

rem Run the Streamlit app using a different port to avoid conflicts
call streamlit run scripts/advanced_vtrac_analyzer.py --server.port 8509

echo.
echo Advanced analysis complete.
pause 