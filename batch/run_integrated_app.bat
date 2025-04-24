@echo off
echo Starting Integrated Alpha Analytical Tool...
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run the streamlit app
streamlit run scripts\core\streamlit_app_with_analyzer.py

REM Deactivate virtual environment
call deactivate 