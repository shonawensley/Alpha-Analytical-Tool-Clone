# Digit-Reduction Module   *AAT9 v1.0*  
*(docs/DR_Spec_AAT9.md)*

## 1  Purpose
Reduce each selected **R2 long string** by subtracting recent Pick-3 draw digits, using several distinct “reduction methods.”  
The surviving characters reveal *persistent* numeric patterns that feed later analytics (stable-pattern extractor, hot-zones scoring, etc.).

## 2  Inputs
| Source | Path/Key | Notes |
|--------|----------|-------|
| **Combined-table CSVs** | `tables/<STATE>/<Section>_combined.csv` | One row per Set/Draw/RowType. |
| **R2 string locations** | Area-1 → Set3/2/1 Draw-1 col 7 6 5  <br>Area-2 → Set1 Draw-4 col 3 & Draw-6 col 1 | Hard-coded in extractor helpers. |
| **Draw digit lists** | Last 7 draws from Set1 → Draw-data row (columns 1-7) | Provided in two modes: *own* (section only) and *combined* (interleaved Midday/Evening). |
| **Mirror map** | `MIRROR_MAP` (0↔5, 1↔6, 2↔7, 3↔8, 4↔9) | Global constant. |

## 3  Outputs
* **HTML report** `outputs/digit_reduction_<timestamp>.html`  
  – one tab per method × draw-mode, showing mini-tables of each R2 string’s progression.  
* *(optional)* JSON snapshot (currently commented-out).

## 4  Reduction methods (code: `long_string_reducer_part1.py`)
| Label | Nickname (docs/UI) | Rule set | Example<br>(orig `559922086`, draw `234`) |
|-------|--------------------|----------|-------------------------------------------|
| **A** | *Exact-all* | Delete **all** copies of each exact draw digit. | → `559906` |
| **B** | *Exact-else-mirror (all)* | For each draw digit *d*: if *d* present, remove all *d*; else remove all copies of its mirror. | → `550` |
| **C** | *Exact + Mirror (all)* | Remove all copies of *d* **and** its mirror, unconditionally. | → `50` |
| **D** | *Transit (single-mirror)* | Remove all *d*; then remove **one** mirror copy (if present). | → `55906` |
| **E** | *Single-hit legacy* | Remove **one** exact copy; else **one** mirror copy. | → `5599206` |
| **T** | *Adaptive transit* (target length = 3) | 1) Remove all exact digits.<br>2) If result longer than target, peel mirrors (all copies) **in draw order** until string ≤ 3 chars. | → `559` |

*All removals are case-insensitive (strings are digits only).*

## 5  Internal flow
1. **Load data** – `--csv_dir tables/…` invokes `load_csv_directory()`  
2. **Extract targets** – `extract_r2_strings_area[1|2]()` builds location → string map.  
3. **Gather draw sequences** – `get_draw_lists_for_section()` returns `[own, combined]`.  
4. **Iterate reductions** – `run_reduction_progression()` applies selected `method_x` for up to 7 draws (or until empty).  
5. **Render** – `build_full_html()` assembles tables; 🌐 navigation bar toggles method/mode.

## 6  CLI usage
```bash
python long_string_reducer_part2.py \
       --csv_dir data/outputs/tables/OntarioCanada4 \
       --out outputs/
Output: outputs/digit_reduction_20250525_142233.html

7 File map (module only)
arduino
Copy
Edit
long_string_reducer/
├─ long_string_reducer_part1.py   # core helpers + reduction funcs
├─ long_string_reducer_part2.py   # runner + HTML writer
└─ outputs/                       # HTML + optional JSON
8 Assumptions / limitations
Works only with the combined-table CSV layout produced by the upstream pipeline.

Sandbox has no external I/O; all data must live in repo.

Draw history limited to 7 columns; change get_draw_lists_for_section if future tables widen.

Method T target length hard-coded (=3). Modify parameter in call if needed.

9 Changelog (AAT9)
Date	By	Version	Notes
2025-05-25	S. Wesley / ChatGPT	v1.0	First stable spec – Digit Reduction complete.

yaml
Copy
Edit

---  
*When this file is in the repo, let me know and we’ll move on to the cheat-sheet.*