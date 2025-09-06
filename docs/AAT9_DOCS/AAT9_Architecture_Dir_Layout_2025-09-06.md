# AAT9 – Architecture & Directory Layout (2025-09-06)

Purpose: Document the canonical structure, launch paths, data contracts, and safety guardrails for the integrated Streamlit app so contributors and AIs can extend it without path drift.

## Goals
- Keep the integrated app stable: entry, imports, and data roots are explicit and consistent.
- Reduce confusion: archive legacy runners and define one canonical layout.
- Enable growth: clear places for new modules/tools with minimal coupling.

## Canonical Launch & Entry
- Launcher: `run_app.bat` (pushd to repo root; `streamlit run src\app.py`).
- Entry file: `src/app.py` (routes to pages: V‑TRAC, Stable, Digit Reduction, Auxiliary Tools, Control Center).

## Data Contracts (by page)
- V‑TRAC, Stable Pattern, Digit Reduction
  - Inputs: combined tables under `tables/` or `data/outputs/tables/<STATE>/` via `utils.path_handler`.
  - Outputs: analysis artifacts under `data/outputs/analysis/<tool>/<STATE>/`.
- Auxiliary Tools + Blackapple
  - Inputs: `data/cleaned/*_draws.csv` (draws only; newest‑first).
  - Strictly do not read string‑table Excel for Aux/BA.
- Control Center
  - Inputs: scans `data/cleaned/*_draws.csv` across states for doubles + BA summary.

## Canonical Directory Layout
```
repo_root/
├─ src/
│  ├─ app.py                     # Streamlit entry
│  └─ core/                      # Thin wrappers called by pages
│     ├─ stable_pattern_extractor.py
│     ├─ module_b_digit_reduction.py
│     └─ module_c_vtrac.py       # (if present)
├─ modules/
│  ├─ blackapple.py              # BA logic (draws‑only)
│  ├─ aux_loaders.py             # robust draws CSV loader
│  └─ module_d_auxiliary_tools/  # optional sums, etc.
├─ alpha_analytical/
│  └─ stable/
│     ├─ __init__.py             # YAML‑weighted canonical extractor
│     └─ feature_config.yml      # scoring weights/config
├─ utils/
│  └─ path_handler.py            # single source for output/data dirs
├─ data/
│  ├─ original/
│  ├─ cleaned/                   # *_draws.csv per state (Aux/BA/Control Center)
│  └─ outputs/
│     ├─ tables/<STATE>/         # combined tables consumed by V‑TRAC/Stable/DR
│     └─ analysis/
│        ├─ patterns/<STATE>/
│        ├─ digit_reduction/<STATE>/
│        └─ vtrac/<STATE>/       # optional home for V‑TRAC artifacts
├─ .codex/
│  └─ preflight.ps1              # quick environment/import/data check
└─ docs/AAT9_DOCS/               # AAT9 documents
```

## Invariants & Guardrails
- Always run from repo root. BATs `pushd` to root explicitly.
- Import sources must resolve to files inside the repo:
  - `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`.
- Aux/BA read only `data/cleaned/*_draws.csv`. Combined pipeline artifacts are for V‑TRAC/Stable/DR.
- Keep the BA absolute‑path loader in `src/app.py` to avoid `modules` package collisions.

## Preflight (Windows)
- Script: `.codex/preflight.ps1` (optional but recommended).
- What it prints:
  - CWD, Python interpreter path.
  - Import locations for `utils.path_handler`, `modules.blackapple`, `modules.aux_loaders`, `alpha_analytical.stable`.
  - `data/cleaned/*_draws.csv` inventory; optional `-State "Florida4"` to resolve a specific CSV and count.
- Example:
  ```powershell
  powershell -NoProfile -File .codex/preflight.ps1 -State "Connecticut4"
  ```

## Live Wiring Details
- Stable Pattern (UI → wrapper → canonical)
  - `src/app.py` → `src/core/stable_pattern_extractor.py` → `alpha_analytical/stable`.
  - Outputs to `data/outputs/analysis/patterns/<STATE>/`.
- Auxiliary Tools
  - `modules.aux_loaders.load_state_draws(state)` resolves `*_draws.csv` robustly.
  - BA: `modules.blackapple` computes score/triggers/candidates purely from draws.
- V‑TRAC, Digit Reduction
  - Read combined tables via `utils.path_handler` directory helpers.

## Diagram (Data Flow)
```mermaid
flowchart TB
  subgraph Pipeline[Combined Tables Pipeline]
    A[data/original/Pick3StatsC4.xlsm]
    A -->|extract/clean/build| T[tables/ (state tables)]
  end

  subgraph AppPages[Streamlit App Pages]
    V[V‑TRAC]
    S[Stable Pattern]
    D[Digit Reduction]
    X[Auxiliary Tools]
    C[Control Center]
  end

  T --> V
  T --> S
  T --> D

  subgraph Draws[Per‑state Draw CSVs]
    DC[data/cleaned/*_draws.csv]
  end

  DC --> X
  DC --> C
```

## Archive Notes
- Legacy runners and old entrypoints moved to `archived/2025-09-06/` with `ARCHIVE_MANIFEST.md`.
- No deletions performed; all moves are reversible.

## Developer Checklist (Quick)
- Launch via `run_app.bat` from repo root.
- If anything looks off, run `.codex/preflight.ps1` and enable the in‑app “System Health” expander.
- Write new analyzers as pure functions; read from canonical dirs and write under `data/outputs/analysis/...`.
- Keep diffs small; prefer archive‑first to refactor‑first when cleaning.

