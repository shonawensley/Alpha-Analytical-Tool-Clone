# Digit Reduction — v0 Study Queue (Harness-driven)

Purpose: a bounded, high-signal queue of DR cases to study using the winners HTML + DR overlay artifacts.

Selection logic (frozen corpus metrics):
- **Buried-but-present**: DR long-string lens is active (`items_total>0`), winner is **not** in DR top-candidates, but the DR stamp/flags show strong winner presence (`dr_stamp_exact_any` / `dr_flags_dr_win_vt_boxed` / `dr_stamp_vtrac_any`).
- **Empty lens**: DR long-string lens produced `items_total=0` (to verify whether this is environment or a correctness issue).

Data source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_tool_metrics.csv`
Windows: 2025-06-21→23, 2025-12-30→2026-01-04, 2026-01-05→09 (Midday/Evening only)

Evidence pointers (for any row):
- Winners HTML/JSON (environment lens): `sharepacks/<D>/<STATE>/winners/<STATE>/*.html`
- DR overlay + stamps/hits: `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/winners/`
- DR pre-results caller surface: `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_top_candidates.csv`
- Master Validation report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`

## A) Buried-but-present (top 30)

| D | State | Period | Winner | Canon | idx | items_total | exact_any | vt_boxed_any | vtrac_any |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 2026-01-09 | OntarioCanada4 | Evening | 104 | 014 | 9 | 240 | 204 | 6 | 240 |
| 2026-01-08 | Florida4 | Midday | 429 | 249 | 31 | 210 | 200 | 60 | 208 |
| 2026-01-07 | Michigan4 | Evening | 616 | 166 | 16 | 167 | 158 | 167 | 167 |
| 2026-01-02 | NorthCarolina4 | Midday | 033 | 033 | 13 | 264 | 156 | 170 | 264 |
| 2025-12-31 | Delaware4 | Evening | 337 | 337 | 29 | 200 | 144 | 22 | 200 |
| 2025-06-21 | Pennsylvania4 | Midday | 667 | 667 | 17 | 172 | 120 | 135 | 172 |
| 2026-01-07 | Delaware4 | Evening | 922 | 229 | 28 | 180 | 120 | 42 | 180 |
| 2025-06-23 | Indiana4 | Midday | 110 | 011 | 6 | 121 | 120 | 1 | 120 |
| 2025-12-31 | Virginia4 | Midday | 686 | 668 | 18 | 328 | 108 | 34 | 324 |
| 2025-06-21 | OntarioCanada4 | Midday | 678 | 678 | 21 | 112 | 108 | 9 | 112 |
| 2026-01-02 | PuertoRico4 | Midday | 144 | 144 | 25 | 108 | 108 | 2 | 108 |
| 2026-01-06 | Michigan4 | Midday | 618 | 168 | 18 | 216 | 95 | 25 | 216 |
| 2026-01-02 | SouthCarolina4 | Midday | 308 | 038 | 13 | 121 | 93 | 49 | 121 |
| 2026-01-07 | Florida4 | Midday | 434 | 344 | 34 | 117 | 91 | 51 | 104 |
| 2025-06-22 | NewJersey4 | Evening | 887 | 788 | 29 | 296 | 85 | 285 | 193 |
| 2026-01-01 | Delaware4 | Midday | 149 | 149 | 25 | 312 | 84 | 303 | 312 |
| 2025-06-21 | Indiana4 | Midday | 565 | 556 | 2 | 277 | 82 | 265 | 234 |
| 2025-06-21 | Ohio4 | Evening | 868 | 688 | 23 | 180 | 84 | 3 | 180 |
| 2026-01-02 | NewJersey4 | Evening | 331 | 133 | 23 | 132 | 72 | 40 | 132 |
| 2025-06-23 | NewYork4 | Evening | 767 | 677 | 20 | 94 | 72 | 22 | 94 |
| 2025-06-23 | Connecticut4 | Midday | 130 | 013 | 8 | 94 | 72 | 10 | 92 |
| 2025-12-31 | Virginia4 | Evening | 636 | 366 | 18 | 252 | 72 | 0 | 252 |
| 2025-06-23 | Pennsylvania4 | Evening | 040 | 004 | 5 | 96 | 72 | 0 | 84 |
| 2026-01-03 | Connecticut4 | Evening | 181 | 118 | 18 | 108 | 68 | 13 | 108 |
| 2026-01-03 | Florida4 | Evening | 611 | 116 | 16 | 66 | 66 | 54 | 66 |
| 2025-06-23 | NewJersey4 | Midday | 106 | 016 | 6 | 173 | 64 | 77 | 134 |
| 2025-06-23 | NewYork4 | Midday | 638 | 368 | 23 | 252 | 60 | 73 | 252 |
| 2025-06-23 | NorthCarolina4 | Evening | 145 | 145 | 9 | 112 | 60 | 24 | 97 |
| 2026-01-07 | SouthCarolina4 | Evening | 336 | 336 | 23 | 228 | 60 | 2 | 228 |
| 2026-01-04 | NorthCarolina4 | Evening | 887 | 788 | 29 | 98 | 60 | 2 | 98 |

## B) Empty-lens (sample 30)

| D | State | Period | Winner | Canon | idx | items_total |
|---|---|---|---:|---:|---:|---:|
| 2025-06-21 | Virginia4 | Midday | 473 | 347 | 30 | 0 |
| 2025-06-22 | OntarioCanada4 | Evening | 616 | 166 | 16 | 0 |
| 2025-12-30 | NorthCarolina4 | Evening | 879 | 789 | 30 | 0 |
| 2025-12-31 | NewYork4 | Evening | 116 | 116 | 16 | 0 |
| 2025-12-31 | OntarioCanada4 | Evening | 932 | 239 | 30 | 0 |
| 2026-01-01 | Delaware4 | Evening | 937 | 379 | 30 | 0 |
| 2026-01-01 | NewYork4 | Evening | 174 | 147 | 22 | 0 |
| 2026-01-02 | Indiana4 | Evening | 359 | 359 | 14 | 0 |
| 2026-01-02 | Michigan4 | Evening | 523 | 235 | 11 | 0 |
| 2026-01-02 | NewYork4 | Evening | 256 | 256 | 7 | 0 |
| 2026-01-04 | Delaware4 | Evening | 269 | 269 | 22 | 0 |
| 2026-01-04 | Michigan4 | Evening | 324 | 234 | 30 | 0 |
| 2026-01-04 | Michigan4 | Midday | 539 | 359 | 14 | 0 |
| 2026-01-04 | NewYork4 | Midday | 793 | 379 | 30 | 0 |
| 2026-01-04 | OntarioCanada4 | Midday | 958 | 589 | 14 | 0 |
| 2026-01-05 | Michigan4 | Evening | 772 | 277 | 26 | 0 |
| 2026-01-05 | NewJersey4 | Evening | 694 | 469 | 25 | 0 |
| 2026-01-05 | OntarioCanada4 | Midday | 555 | 555 | - | 0 |
| 2026-01-06 | Connecticut4 | Midday | 576 | 567 | 7 | 0 |
| 2026-01-06 | Michigan4 | Evening | 578 | 578 | 11 | 0 |
| 2026-01-06 | Ohio4 | Evening | 064 | 046 | 9 | 0 |
| 2026-01-08 | NewYork4 | Midday | 199 | 199 | 25 | 0 |
| 2026-01-08 | OntarioCanada4 | Evening | 498 | 489 | 34 | 0 |
| 2026-01-08 | SouthCarolina4 | Midday | 277 | 277 | 26 | 0 |
| 2026-01-09 | Michigan4 | Evening | 273 | 237 | 27 | 0 |
| 2026-01-09 | Michigan4 | Midday | 842 | 248 | 30 | 0 |
| 2026-01-09 | OntarioCanada4 | Midday | 772 | 277 | 26 | 0 |
