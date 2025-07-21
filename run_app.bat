@echo off
REM ── Activate your v-env if you normally do ─────────────
REM call ".\venv\Scripts\activate.bat"

REM ── Launch the Streamlit UI (all modules, inc. Digit-Reduction) ──
streamlit run src/app.py

REM ── Keep the window open so you can read logs ──────────
pause 