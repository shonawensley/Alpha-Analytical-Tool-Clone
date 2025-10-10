@echo off
setlocal
REM Optional: activate your venv if used
REM call "%~dp0venv\Scripts\activate.bat"

REM Ensure we run from the repo root regardless of how this BAT is launched
pushd "%~dp0"

REM Run Aux validation guardrail before launching Streamlit
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\tools\validate_aux_all.ps1
if errorlevel 1 (
    echo Aux validation failed. Aborting launch.
    popd
    endlocal
    exit /b 1
)

REM Prevent auto-opening browser (optional)
set STREAMLIT_BROWSER=none

REM Launch the Streamlit UI (all modules, inc. Digit-Reduction and Blackapple)
streamlit run src\app.py

popd
endlocal
