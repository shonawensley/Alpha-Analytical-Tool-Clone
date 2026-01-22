# Conditional Conversion Study Queue — 2025-06-21 → 2025-06-23

- generated_at: `2026-01-22T06:48:38.142855+00:00`
- experiment_tag: `condconv_v3`
- sharepacks_root: `sharepacks`
- baseline: `play_box_first/B12`
- test: `conversion_box_first_conditional_lenient_presetB/B12`
- rows_with_deltas: `4`

## Cases (only rows where baseline vs test differs)

| date | state | label | winner | hit_any | perm_hit | vtrac_hit | ext_hit | winners_json | winner_summary | cu_recall |
|---|---|---|---|---:|---:|---:|---:|---|---|---|
| 2025-06-22 | NorthCarolina4 | Evening | 153 | 0→0 | 0→0 | 0→1 | 0→1 | `sharepacks/2025-06-22/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac8_winner_153_20251221_222126.json` | idx=8 | winner=153 | top_occ=153:11, 815:9, 568:7, 013:3, 068:3 | CU:straight=Y canon=Y union=164 |
| 2025-06-23 | Florida4 | Midday | 665 | 0→0 | 0→0 | 0→1 | 0→1 | `sharepacks/2025-06-23/Florida4/winners/Florida4/Florida4_vtrac6_winner_665_20251223_052045.json` | idx=6 | winner=665 | top_occ=011:6, 665:5, 066:4, 566:3, 016:0 | CU:straight=N canon=Y union=170 |
| 2025-06-23 | NewJersey4 | Evening | 152 | 0→0 | 0→0 | 0→1 | 0→1 | `sharepacks/2025-06-23/NewJersey4/winners/NewJersey4/NewJersey4_vtrac7_winner_152_20251223_052054.json` | idx=7 | winner=152 | top_occ=175:9, 170:8, 201:6, 625:6, 701:6 | CU:straight=N canon=Y union=141 |
| 2025-06-23 | PuertoRico4 | Midday | 858 | 0→0 | 0→0 | 0→1 | 0→1 | `sharepacks/2025-06-23/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac13_winner_858_20251223_052108.json` | idx=13 | winner=858 | top_occ=083:8, 038:5, 088:2, 033:0, 303:0 | CU:straight=N canon=N union=185 |

## Per-case artifact pointers

### 2025-06-22 — NorthCarolina4 — Evening — winner 153
- winners_json: `sharepacks/2025-06-22/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac8_winner_153_20251221_222126.json`
- tables_json: `sharepacks/2025-06-22/NorthCarolina4/json/NorthCarolina4_tables.json`
- candidate_universe: `sharepacks/2025-06-22/NorthCarolina4/candidate_universe__tool_only__condconv_v3.json`
- play_card: `sharepacks/2025-06-22/NorthCarolina4/play_card__tool_only__condconv_v3.json`

### 2025-06-23 — Florida4 — Midday — winner 665
- winners_json: `sharepacks/2025-06-23/Florida4/winners/Florida4/Florida4_vtrac6_winner_665_20251223_052045.json`
- tables_json: `sharepacks/2025-06-23/Florida4/json/Florida4_tables.json`
- candidate_universe: `sharepacks/2025-06-23/Florida4/candidate_universe__tool_only__condconv_v3.json`
- play_card: `sharepacks/2025-06-23/Florida4/play_card__tool_only__condconv_v3.json`

### 2025-06-23 — NewJersey4 — Evening — winner 152
- winners_json: `sharepacks/2025-06-23/NewJersey4/winners/NewJersey4/NewJersey4_vtrac7_winner_152_20251223_052054.json`
- tables_json: `sharepacks/2025-06-23/NewJersey4/json/NewJersey4_tables.json`
- candidate_universe: `sharepacks/2025-06-23/NewJersey4/candidate_universe__tool_only__condconv_v3.json`
- play_card: `sharepacks/2025-06-23/NewJersey4/play_card__tool_only__condconv_v3.json`

### 2025-06-23 — PuertoRico4 — Midday — winner 858
- winners_json: `sharepacks/2025-06-23/PuertoRico4/winners/PuertoRico4/PuertoRico4_vtrac13_winner_858_20251223_052108.json`
- tables_json: `sharepacks/2025-06-23/PuertoRico4/json/PuertoRico4_tables.json`
- candidate_universe: `sharepacks/2025-06-23/PuertoRico4/candidate_universe__tool_only__condconv_v3.json`
- play_card: `sharepacks/2025-06-23/PuertoRico4/play_card__tool_only__condconv_v3.json`
