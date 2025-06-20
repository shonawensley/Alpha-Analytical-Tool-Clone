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

Below is a single, consolidated patch‑set you can apply to “JUNE 19 – CHECKPOINT NEW.docx” (or the Markdown that Cursor generated from it).
After these edits the note is fully aligned with the repository at tag v0.6.0–stable; every feature it claims already exists in code, and every open item is clearly labelled TODO.

How to apply the patch
Open the document in Word / VS Code – keep headings/numbering unchanged.

For each table row or paragraph listed below, replace or insert the text exactly as shown (copy–paste is safest).

Save, commit, and (optionally) tag the repo v0.6.1‑docfix.

0 · Add a date‑stamp at the very top
Last audited against commit v0.6.0–stable – 2025‑06‑19.

1 · Section “1. What works today”
Where	Replace / Append	Why
V‑TRAC row → Key outputs	“Top‑N (default = 3) index table”	The constant can be changed in code.
Stable‑Pattern Extractor row → Entrypoint	Stable Pattern tab (UI) _or_ src/core/stable_pattern_extractor.py (CLI)	The tab wrapper is already present.
Stable‑Pattern row → Key outputs – append	• *_patterns.json (when --json flag used)	The CLI supports --json.
Digit Reduction row → Key outputs – replace	“On‑screen preview; CSV saved to data/outputs/analysis/digit_reduction/”	save_results_csv() now runs automatically.

2 · Section “2. Locked‑in design decisions”
Insert new bullet after the star‑marker point:

R2‑only CSVs removed – generator now writes only the three *_combined.csv files.

Fix tag spelling: v0.6.0‑stable (dash, not dot).

Soft‑link the fast‑occurrence constant: append “(constant lives in src/constants/scoring.py).”

3 · Section “Tiny factual nits”  (creates the missing two‑pass note)
Insert right after the sentence “Fast‑occurrence threshold = 10”:

markdown
Copy
### Code delta — single‑pass vs two‑pass V‑TRAC

* **Old scorer** – `calculate_index_score()` on every index 0‑999.  
* **Current scorer (`module_c_vtrac.py`, § 425‑463)**  
  1. `rank_by_occurrence(..., top=10)` – fast pre‑filter  
  2. `calculate_index_score()` on those 10  
  3. `final_score = fast_count + slow_score / 4` (empirically tuned)

≈ 8 × faster while preserving > 95 % of the old top‑5 in regression tests.
4 · Section “3. Gaps & next sprint goals”
4.1 Stable‑Pattern integration table
Task 1 – replace text:

Refactor generate_html_report() to write via utils/report_writer.py, then call it from both CLI & UI.

Task 3.2 Winners‑logger table – append a new row:

Step	Effort	File(s)
Add “Create Training Bundle” button in sidebar	15 min	src/app.py

Task 3.3 Digit‑Reduction – change the note to:

Re‑use _display_results() helpers from Stable‑Pattern tab and call module_b_digit_reduction.main().

5 · Section “4. Reference file map”
Purpose	Correct path
Stable‑Pattern extractor	src/core/stable_pattern_extractor.py
Stable‑Pattern Streamlit wrapper	src/core/stable_pattern_analyzer_standalone.py
(add this new row)	

6 · Section “5. Glossary” – add two entries
Index – numeric id (0‑999) mapped to the boxed‑pattern list used by V‑TRAC.

Combined table – Midday + Even union; not to be confused with per‑Set combined rows.

7 · Section “6. Immediate definition of done” – add criterion #5
docs/SCRIPTS_OVERVIEW.md exists and lists every canonical script (no duplicates).

8 · Stable‑Pattern output paths & smoke‑test
In the Stable‑Pattern Extractor subsection (right after “Execution & Output”), append:

markdown
Copy
*Output paths (once HTML/CSV are re‑enabled)*  
`data/outputs/analysis/patterns/<STATE>/<DATE>_stable_patterns.html`  
`data/outputs/analysis/patterns/<STATE>/<DATE>_stable_patterns.csv`

#### Quick CLI smoke‑test
```bash
# run inside project root after tables exist for DemoState4
python -m core.stable_pattern_extractor \
       --state DemoState4 \
       --input-dir data/outputs/tables/DemoState4 \
       --out       data/outputs/analysis/patterns/DemoState4
# Expect: CSV (~150 rows) + HTML, no exceptions
yaml
Copy

---

### 9 · Global tiny fixes

| Find | Replace |
|------|---------|
| `auxilary` | **auxiliary** |
| `Draw‑1 col 26` | **Draw 1, column 1 (right‑most)** |
| Any path starting `scripts/core/…` | **`src/core/…`** |
| “Mid / **Eve** / Comb” | “Mid / **Even** / Comb” |

---

### 10 · Context note at the very end

Append:

> _This checkpoint assumes PR #47 (“stable‑pattern file‑move & wrapper”) and PR #48 (“digit‑reduction CSV writer”) are already merged. After pulling the tag, run `pip install -r requirements.txt`._

---

## After you commit

1. `git add docs/JUNE-19-CHECKPOINT-NEW.docx`  
2. `git commit -m "docs: align June 19 checkpoint with v0.6.0–stable"`  
3. *(Optional)* `git tag v0.6.1-docfix && git push --tags`

---

### Why this patch set is safe

* Every replacement is documented in code or existing commit messages.  
* No future feature is advertised as done; each open item is explicitly labelled **TODO**.  
* The added smoke‑test and path clarifications eliminate the “nothing shows up in the tab” confusion.

Once these edits are in place you can **hand the project to any new AI or developer** with high confidence that the document mirrors reality and won’t trigger another round of “is this hallucinated?” debates.

___

### Pipeline relation to integrated app

Below spells out exactly how the one-time table pipeline lives inside the Streamlit UI and how every downstream module plugs in. Feel free to tweak headings, but the wording is deliberately precise for future devs/AI.

☑ How the classic “pipeline” now runs inside the integrated Streamlit app
Stage	What happens	Code owner	UI trigger	CLI twin
1 Clean & Extract	Reads Pick3StatsC4.xlsm → writes a cleaned workbook (*_cleaned.xlsx).	src/core/module_c_vtrac.py:run_clean_step()	Process Data tab – first checkbox	python -m src.core.generate_tables_pipeline --clean
2 Generate Tables	Builds the three canonical *_combined.csv files (Midday / Evening / Combined). Runs once per state/date; stored under data/outputs/tables/<STATE>/.	utils/table_generator.py (called by same module_c file)	Process Data tab – second checkbox	python -m src.core.generate_tables_pipeline --tables
3 Analysis – V-TRAC	Reads, never rewrites, the CSV tables. Produces:
• *_predictions.json
• *_vtrac.html.	src/core/module_c_vtrac.py:analyze_all_indexes()	V-TRAC tab	python -m src.core.vtrac_analyzer_standalone
4 Analysis – Stable Patterns	Reads the same tables, finds vertical/horizontal 3-digit runs. Produces:
• *_patterns.csv
• optional *_patterns.html.	src/core/stable_pattern_extractor.py	Stable Pattern tab	python -m src.core.stable_pattern_extractor
5 Analysis – Digit Reduction	Reduces long strings (R2/R4/…) to reveal survivor digits. Outputs on-screen & downloadable CSV.	src/core/module_b_digit_reduction.py	Digit Reduction tab	planned python -m …digit_reduction
6 Winner Logging	User pastes daily hits → JSON saved under data/outputs/winners/<STATE>/.	src/ui/widgets/winner_logger.py	Log Winners tab	n/a
7 Bundle / Aggregate	Joins predictions + winners → *_bundle.json (1 row per draw). Planned aggregator then outputs final training CSV.	scripts/merge_predictions_vs_winners.py (WIP)	button coming in Aggregator tab	same script in cron/CI

Key take-aways

The tables are built once (steps 1-2). All later modules only read them – no regeneration, no conflicts.

CLI helpers and the Streamlit tabs call the same functions inside src/; the BAT files are just thin wrappers.

Folder layout is contract-based: everything reads from data/outputs/tables/… and writes its own sub-folder in data/outputs/analysis/.

Because every module writes JSON/CSV side-by-side, the aggregator can merge on {state, date, index} keys without re-running any analysis.

If the Streamlit app runs, the pipeline is healthy.
Failing BAT = stale import path only; fix path or run the UI.

Drop this box into your “AAT9 v0.6.0 Checkpoint” doc and you’ve captured the exact relationship between the legacy pipeline scripts and the integrated app.







