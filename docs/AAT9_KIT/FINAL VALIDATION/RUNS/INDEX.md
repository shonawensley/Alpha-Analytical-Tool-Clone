# Master Validation — Run Report Index (Progress Tracker)

Purpose: avoid “where are we?” drift when context resets. This file tracks which state run reports are **filled** vs **still scaffolds** for each results date `D`.

Definitions:
- `D` = results date (folder name under `sharepacks/`)
- `D-1` = history workbook date used to build the tables/strings used to predict `D` (see `sharepacks/<D>/README.md`)

Status legend:
- `DONE` = report is filled (no `- Q1: …` scaffold placeholders remain)
- `TODO` = report exists but still has scaffold placeholders
- `SCAFFOLD` = generated helper file; do not treat as a filled report

Quick status checks (repo root):
```bash
# Which reports for a day still have scaffold placeholders?
rg -l -g '2025-06-22__*.md' -- "- Q1: …" "docs/AAT9_KIT/FINAL VALIDATION/RUNS" | sort

# Confirm day sharepack mapping is correct (H → D)
sed -n '1,40p' "sharepacks/2025-06-22/README.md"
```

---

## D=2025-06-21 (H=2025-06-20)

- DONE `2025-06-21__CONTROL_CENTER.md`
- DONE `2025-06-21__Connecticut4.md`
- DONE `2025-06-21__Delaware4.md`
- DONE `2025-06-21__Florida4.md`
- DONE `2025-06-21__Indiana4.md`
- DONE `2025-06-21__Michigan4.md`
- DONE `2025-06-21__NewJersey4.md`
- DONE `2025-06-21__NewYork4.md`
- DONE `2025-06-21__NorthCarolina4.md`
- DONE `2025-06-21__Ohio4.md`
- DONE `2025-06-21__OntarioCanada4.md`
- DONE `2025-06-21__Pennsylvania4.md`
- DONE `2025-06-21__PuertoRico4.md`
- DONE `2025-06-21__SouthCarolina4.md`
- DONE `2025-06-21__Virginia4.md`
- SCAFFOLD `2025-06-21__OntarioCanada4__generated.md`

## D=2025-06-22 (H=2025-06-21)

- DONE `2025-06-22__CONTROL_CENTER.md`
- DONE `2025-06-22__Connecticut4.md`
- DONE `2025-06-22__Delaware4.md`
- DONE `2025-06-22__Florida4.md`
- DONE `2025-06-22__Indiana4.md`
- DONE `2025-06-22__Michigan4.md`
- DONE `2025-06-22__NewJersey4.md`
- DONE `2025-06-22__NewYork4.md`
- DONE `2025-06-22__NorthCarolina4.md`
- DONE `2025-06-22__Ohio4.md`
- DONE `2025-06-22__OntarioCanada4.md`
- DONE `2025-06-22__Pennsylvania4.md`
- DONE `2025-06-22__PuertoRico4.md`
- DONE `2025-06-22__SouthCarolina4.md`
- DONE `2025-06-22__Virginia4.md`

## D=2025-06-23 (H=2025-06-22)

- DONE `2025-06-23__CONTROL_CENTER.md`
- DONE `2025-06-23__Connecticut4.md`
- DONE `2025-06-23__Delaware4.md`
- DONE `2025-06-23__Florida4.md`
- DONE `2025-06-23__Indiana4.md`
- DONE `2025-06-23__Michigan4.md`
- DONE `2025-06-23__NewJersey4.md`
- DONE `2025-06-23__NewYork4.md`
- DONE `2025-06-23__NorthCarolina4.md`
- DONE `2025-06-23__Ohio4.md`
- DONE `2025-06-23__OntarioCanada4.md`
- DONE `2025-06-23__Pennsylvania4.md`
- DONE `2025-06-23__PuertoRico4.md`
- DONE `2025-06-23__SouthCarolina4.md`
- DONE `2025-06-23__Virginia4.md`
