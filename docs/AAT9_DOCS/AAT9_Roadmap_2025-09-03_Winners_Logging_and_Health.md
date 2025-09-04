# AAT9 — Roadmap 2025‑09‑03 — Winners Logging & Health Helpers

Purpose

Document the near‑term plan to (1) stabilize and observe the integrated app via small, read‑only “System Health” helpers; (2) start logging winners and raw outputs in a consistent structure so we can learn from real runs; and (3) prepare for a lightweight hybrid‑ML pass that learns how to combine tool signals.

What’s Working Now (Baseline)

- Control Center shows “Blackapple Alerts (All States)” with coherent status/score/triggers and examples. Full candidates (12) are viewable via expanders.
- BA uses per‑state draws CSVs under data/cleaned/*_draws.csv (CSV‑only; no Excel mix‑ups).
- BA imports are isolated via an absolute‑path loader to avoid modules name collisions.
- Deterministic launch via BAT at project root is in place.

System Health Helpers (Read‑Only, DEV‑Gated)

Why: Prevent “mystery bugs.” Show cwd, module paths, and data resolution so path/import/data issues are visible.

Pattern (per page):
- Env: `cwd`, Python exe, sys.path length
- Modules: `__file__` for key modules (e.g., blackapple, analyze_pairs, vtrac_reference)
- Data: expected inputs summary
  - Control Center/Aux: count of data/cleaned/*_draws.csv; chosen CSV for the selected state + row count
  - V‑TRAC/Stable/DR (later): expected input dirs under tables/ + existence/size hints

Where:
- Control Center: added (dev only)
- Auxiliary Tools: add same expander (dev only)
- Optional later: V‑TRAC / Stable Pattern / Digit Reduction pages
- Optional dedicated “System Health” page

Gating:
- Sidebar toggle “Show Dev Health” (off by default) or APP_DEV=1 env var

Docs:
- BA Module and Aux Official docs briefly explain the expander and CLI preflight (.codex/preflight.ps1) and what “green” looks like.

Winners Logging MVP (Near‑Term)

Goal: Capture structured evidence per run so we can validate and iterate.

Directory Layout:
- `runs/YYYY-MM-DD/<run_id>/`
  - `control_center.json` — BA rows + (optional) doubles table snapshot
  - `per_state/<State>/ba.json` — full BA result dict for that state
  - `metadata.json` — app version, thresholds, config flags
- `winners/YYYY-MM-DD/<State>_<Draw>.json`
  - `{ state, draw, date, vtrac_index (if known), ba: { score, status, triggers, in_candidates, tags }, … }`

UX in app:
- A small “Log Winner” action (State, Draw, Date/Run ID inputs)
- On click: write the above JSONs; generate a simple Markdown “AI report”:
  - Did Control Center fire (ALERT/WATCH)?
  - Did BA include the winner? With which tags?
  - (Optionally) V‑TRAC/Stable/Reduction highlights if quickly available or linked

Hybrid‑ML (Later, Beginner‑Friendly)

- Log features now: BA score/status/triggers; V‑TRAC signals; Stable/DR counts; Control Center doubles ranks
- Aggregator (phase 2): Combine these features into a composite score (weighted sum) and calibrate manually
- Small supervised model later (logistic/GBM) to learn better weights from historical runs

Guardrails & Determinism

- Launch: BAT with `pushd "%~dp0"`, optional `set "PYTHONPATH=%CD%"`, activate venv, `streamlit run src\app.py`
- Imports: BA uses absolute‑path loader; avoid global sys.path hacking
- Data contracts: BA consumes only `data/cleaned/*_draws.csv`; combined string‑tables feed other tools
- Preflight: `.codex/preflight.ps1 -State "<State>"` before big changes

Near‑Term Tasks (small, safe)

1) Add Aux page “System Health” expander (DEV‑gated) mirroring Control Center
2) Append brief “System Health & Preflight” sections to BA and Aux docs
3) Draft a “Winners Logging Spec” doc with JSON shapes and examples

Later

- Optional: System Health expanders on V‑TRAC/Stable/DR
- Winner logging automation for daily runs
- Aggregator module and small ML fit (offline) once enough evidence is logged

