@echo off
echo ==================================
echo Installing Required Packages
echo ==================================
echo.

rem Activate virtual environment if it exists
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo Virtual environment activated.
) else (
    echo Using system Python.
)

echo.
echo Installing seaborn package...
pip install seaborn

echo.
echo Installing matplotlib package...
pip install matplotlib

echo.
echo All packages have been installed.
echo.
echo You can now run the test app by double-clicking on run_test_app.bat
echo.
pause 