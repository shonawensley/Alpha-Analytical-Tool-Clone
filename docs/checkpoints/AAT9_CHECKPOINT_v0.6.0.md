# AAT9 Checkpoint v0.6.0 — Integrated Streamlit App Baseline
_Last audited: 2025-06-18_

---

## 1. What works today

| Pillar | Entrypoint | Consumes | Key outputs | Output folder |
|--------|------------|----------|-------------|---------------|
| **Data Build** | `generate_tables_pipeline.bat` <br>or **Process Data** tab | `Pick3StatsC4.xlsm` | 3 `*_combined.csv` per state (Mid / Eve / Comb) | `data/outputs/tables/<STATE>/` |
| **V‑TRAC Analyzer** | **V‑TRAC** tab | the three CSV tables | • Top‑3 index table<br>• HTML report(s)<br>• `*_predictions.json` | `data/outputs/analysis/vtrac/`<br>`data/outputs/predictions/` |
| **Stable‑Pattern Extractor** | `run_stable_pattern_extractor.bat` (CLI) | the three CSV tables | • `*_patterns.csv` (flat list)<br>• _optional_ HTML heat‑map (see § 3.1) | `data/outputs/analysis/patterns/` |
| **Digit Reduction** | **Digit Reduction** tab | same CSV tables | On‑screen table (+ "Download CSV") | (none yet) |
| **Hot‑Zones** | stub in code | – | `{ "zones": [] }` | – |

All modules **only read** from the combined‑table folder; no one regenerates or rewrites those files.

---

## 2. Locked‑in design decisions

* Single pipeline (Excel → cleaned xlsx → `*_combined.csv` → analysis tools).  
* Folder conventions centralised in `utils/path_handler.py`.  
* Star markers: `*` = hot, `**` = super‑hot (Draw‑1 col 26).  
* **V‑TRAC** now uses a two‑pass scorer (fast occurrence filter ➜ weighted scorer) – 8× speed‑up.  
* Every successful rescue is tagged; last stable tag = **v0.6.0‑stable**.  

---

## 3. Gaps & next sprint goals (0.7 milestone)

### 3.1 Stable‑Pattern integration
| Step | Effort | File(s) |
|------|--------|---------|
| Re‑enable `generate_html_report()` call (currently commented) | 10 min | `src/core/module_a_stable_patterns.py` |
| Write HTML + CSV to `data/outputs/analysis/patterns/<STATE>/<DATE>_*` | 10 min | same |
| In Streamlit "Stable Pattern" tab: list available HTML/CSV and embed with `st.components.v1.html()` | 0.5 h | `src/app.py` |

### 3.2 Winners logger merge
| Step | Effort | File(s) |
|------|--------|---------|
| Convert pasted draws ➜ JSON (`data/outputs/winners/<STATE>/YYYY‑MM‑DD.json`) | done | `module_c_vtrac.py` |
| **NEW:** `merge_predictions_vs_winners.py` – join predictions + winners ➜ training bundle | 1 day | `scripts/` |

### 3.3 Digit‑Reduction UI wiring  
Copy the Stable‑Pattern tab skeleton; call `module_b_digit_reduction.main()`. (≈ 1 h)

### 3.4 Smoke‑test & CI  
Add `tests/test_smoke_pipeline.py` that: generate tables → run V‑TRAC & Stable → assert JSON/CSV exist. Hook into GitHub Actions. (≈ 0.5 day)

---

## 4. Reference file map

| Purpose | Path |
|---------|------|
| V‑TRAC scorer | `src/core/module_c_vtrac.py` |
| Stable‑Pattern extractor | `src/core/module_a_stable_patterns.py` |
| Digit Reduction (Methods A‑E & T) | `src/core/module_b_digit_reduction.py` |
| Table generator | `utils/table_generator.py` |
| Scoring constants | `src/constants/scoring.py` |
| Archived legacy scripts | `archive/legacy_scripts/` |

---

## 5. Glossary (one‑liner refresh)

* **Box** – one of seven right‑aligned columns (7 = oldest, 1 = newest).  
* **Set1/2/3** – sub‑tables (Set1 = latest local data).  
* **RowType** – R2 / R4 / R6 / R8 = how many digits survive reduction.  
* **Hot‑zone** – cell marked `*` or `**`; parsed by `utils/hotzone.py`.  
* **Stable pattern** – digit sequence appearing ≥ N times across sets/draws with no break.  

---

## 6. Immediate "definition of done" for v0.7.0

1. Stable‑Pattern tab shows its HTML/CSV for at least one state.  
2. `*_bundle.json` (predictions + winners) produced for that state/day.  
3. End‑to‑end smoke‑test passes in CI.  
4. Tag `v0.7.0‑stable` and append changes to `docs/CHANGELOG_CORE.md`.

*After v0.7 the backlog is: real Hot‑Zones logic → Aggregator MVP → first ML prototype.* 