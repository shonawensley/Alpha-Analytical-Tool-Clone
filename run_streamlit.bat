@echo off
REM Launch the Streamlit app from the repo root.
REM Uses explicit pushd to avoid CWD mistakes.

pushd "%~dp0"

set PORT=8501
set STREAMLIT_BROWSER=none

echo Starting Streamlit on http://localhost:%PORT% ...
streamlit run src\app.py --server.address 0.0.0.0 --server.port %PORT%

popd
