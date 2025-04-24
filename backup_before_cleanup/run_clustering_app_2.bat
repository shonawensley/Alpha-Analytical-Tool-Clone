@echo off
echo ===========================================
echo            Clustering App 2
echo ===========================================
echo This tool provides enhanced V-TRAC analysis with clustering analysis
echo.

rem Change to the script's directory
cd /d "%~dp0"

rem Activate virtual environment
call .venv\Scripts\activate.bat

rem Clear port if needed
taskkill /F /IM streamlit.exe /T >nul 2>&1

echo Starting application...

rem Direct command to run Streamlit
streamlit run scripts/clustering_app_2.py --server.port 8521

pause 