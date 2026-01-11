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

## D=2025-12-30 (H=2025-12-29)

- DONE `2025-12-30__CONTROL_CENTER.md`
- DONE `2025-12-30__Connecticut4.md`
- DONE `2025-12-30__Delaware4.md`
- DONE `2025-12-30__Florida4.md`
- DONE `2025-12-30__Indiana4.md`
- DONE `2025-12-30__Michigan4.md`
- DONE `2025-12-30__NewJersey4.md`
- DONE `2025-12-30__NewYork4.md`
- DONE `2025-12-30__NorthCarolina4.md`
- DONE `2025-12-30__Ohio4.md`
- DONE `2025-12-30__OntarioCanada4.md`
- DONE `2025-12-30__Pennsylvania4.md`
- DONE `2025-12-30__PuertoRico4.md`
- DONE `2025-12-30__SouthCarolina4.md`
- DONE `2025-12-30__Virginia4.md`

## D=2025-12-31 (H=2025-12-30)

- DONE `2025-12-31__CONTROL_CENTER.md`
- DONE `2025-12-31__Connecticut4.md`
- DONE `2025-12-31__Delaware4.md`
- DONE `2025-12-31__Florida4.md`
- DONE `2025-12-31__Indiana4.md`
- DONE `2025-12-31__Michigan4.md`
- DONE `2025-12-31__NewJersey4.md`
- DONE `2025-12-31__NewYork4.md`
- DONE `2025-12-31__NorthCarolina4.md`
- DONE `2025-12-31__Ohio4.md`
- DONE `2025-12-31__OntarioCanada4.md`
- DONE `2025-12-31__Pennsylvania4.md`
- DONE `2025-12-31__PuertoRico4.md`
- DONE `2025-12-31__SouthCarolina4.md`
- DONE `2025-12-31__Virginia4.md`

## D=2026-01-01 (H=2025-12-31)

- DONE `2026-01-01__CONTROL_CENTER.md`
- DONE `2026-01-01__Connecticut4.md`
- DONE `2026-01-01__Delaware4.md`
- DONE `2026-01-01__Florida4.md`
- DONE `2026-01-01__Indiana4.md`
- DONE `2026-01-01__Michigan4.md`
- DONE `2026-01-01__NewJersey4.md`
- DONE `2026-01-01__NewYork4.md`
- DONE `2026-01-01__NorthCarolina4.md`
- DONE `2026-01-01__Ohio4.md`
- DONE `2026-01-01__OntarioCanada4.md`
- DONE `2026-01-01__Pennsylvania4.md`
- DONE `2026-01-01__PuertoRico4.md`
- DONE `2026-01-01__SouthCarolina4.md`
- DONE `2026-01-01__Virginia4.md`

## D=2026-01-02 (H=2026-01-01)

- DONE `2026-01-02__CONTROL_CENTER.md`
- DONE `2026-01-02__Connecticut4.md`
- DONE `2026-01-02__Delaware4.md`
- DONE `2026-01-02__Florida4.md`
- DONE `2026-01-02__Indiana4.md`
- DONE `2026-01-02__Michigan4.md`
- DONE `2026-01-02__NewJersey4.md`
- DONE `2026-01-02__NewYork4.md`
- DONE `2026-01-02__NorthCarolina4.md`
- DONE `2026-01-02__Ohio4.md`
- DONE `2026-01-02__OntarioCanada4.md`
- DONE `2026-01-02__Pennsylvania4.md`
- DONE `2026-01-02__PuertoRico4.md`
- DONE `2026-01-02__SouthCarolina4.md`
- DONE `2026-01-02__Virginia4.md`

## D=2026-01-03 (H=2026-01-02)

- DONE `2026-01-03__CONTROL_CENTER.md`
- DONE `2026-01-03__Connecticut4.md`
- DONE `2026-01-03__Delaware4.md`
- DONE `2026-01-03__Florida4.md`
- DONE `2026-01-03__Indiana4.md`
- DONE `2026-01-03__Michigan4.md`
- DONE `2026-01-03__NewJersey4.md`
- DONE `2026-01-03__NewYork4.md`
- DONE `2026-01-03__NorthCarolina4.md`
- DONE `2026-01-03__Ohio4.md`
- DONE `2026-01-03__OntarioCanada4.md`
- DONE `2026-01-03__Pennsylvania4.md`
- DONE `2026-01-03__PuertoRico4.md`
- DONE `2026-01-03__SouthCarolina4.md`
- DONE `2026-01-03__Virginia4.md`

## D=2026-01-04 (H=2026-01-03)

- DONE `2026-01-04__CONTROL_CENTER.md`
- DONE `2026-01-04__Connecticut4.md`
- DONE `2026-01-04__Delaware4.md`
- DONE `2026-01-04__Florida4.md`
- DONE `2026-01-04__Indiana4.md`
- DONE `2026-01-04__Michigan4.md`
- DONE `2026-01-04__NewJersey4.md`
- DONE `2026-01-04__NewYork4.md`
- DONE `2026-01-04__NorthCarolina4.md`
- DONE `2026-01-04__Ohio4.md`
- DONE `2026-01-04__OntarioCanada4.md`
- DONE `2026-01-04__Pennsylvania4.md`
- DONE `2026-01-04__PuertoRico4.md`
- DONE `2026-01-04__SouthCarolina4.md`
- DONE `2026-01-04__Virginia4.md`

## D=2026-01-05 (H=2026-01-04)

- DONE `2026-01-05__CONTROL_CENTER.md`
- DONE `2026-01-05__Connecticut4.md`
- DONE `2026-01-05__Delaware4.md`
- DONE `2026-01-05__Florida4.md`
- DONE `2026-01-05__Indiana4.md`
- DONE `2026-01-05__Michigan4.md`
- DONE `2026-01-05__NewJersey4.md`
- DONE `2026-01-05__NewYork4.md`
- DONE `2026-01-05__NorthCarolina4.md`
- DONE `2026-01-05__Ohio4.md`
- DONE `2026-01-05__OntarioCanada4.md`
- DONE `2026-01-05__Pennsylvania4.md`
- DONE `2026-01-05__PuertoRico4.md`
- DONE `2026-01-05__SouthCarolina4.md`
- DONE `2026-01-05__Virginia4.md`

## D=2026-01-06 (H=2026-01-05)

- DONE `2026-01-06__CONTROL_CENTER.md`
- DONE `2026-01-06__Connecticut4.md`
- DONE `2026-01-06__Delaware4.md`
- DONE `2026-01-06__Florida4.md`
- DONE `2026-01-06__Indiana4.md`
- DONE `2026-01-06__Michigan4.md`
- DONE `2026-01-06__NewJersey4.md`
- DONE `2026-01-06__NewYork4.md`
- DONE `2026-01-06__NorthCarolina4.md`
- DONE `2026-01-06__Ohio4.md`
- DONE `2026-01-06__OntarioCanada4.md`
- DONE `2026-01-06__Pennsylvania4.md`
- DONE `2026-01-06__PuertoRico4.md`
- DONE `2026-01-06__SouthCarolina4.md`
- DONE `2026-01-06__Virginia4.md`

## D=2026-01-07 (H=2026-01-06)

- DONE `2026-01-07__CONTROL_CENTER.md`
- DONE `2026-01-07__Connecticut4.md`
- DONE `2026-01-07__Delaware4.md`
- DONE `2026-01-07__Florida4.md`
- DONE `2026-01-07__Indiana4.md`
- DONE `2026-01-07__Michigan4.md`
- DONE `2026-01-07__NewJersey4.md`
- DONE `2026-01-07__NewYork4.md`
- DONE `2026-01-07__NorthCarolina4.md`
- DONE `2026-01-07__Ohio4.md`
- DONE `2026-01-07__OntarioCanada4.md`
- DONE `2026-01-07__Pennsylvania4.md`
- DONE `2026-01-07__PuertoRico4.md`
- DONE `2026-01-07__SouthCarolina4.md`
- DONE `2026-01-07__Virginia4.md`

## D=2026-01-08 (H=2026-01-07)

- DONE `2026-01-08__CONTROL_CENTER.md`
- DONE `2026-01-08__Connecticut4.md`
- DONE `2026-01-08__Delaware4.md`
- DONE `2026-01-08__Florida4.md`
- DONE `2026-01-08__Indiana4.md`
- DONE `2026-01-08__Michigan4.md`
- DONE `2026-01-08__NewJersey4.md`
- DONE `2026-01-08__NewYork4.md`
- DONE `2026-01-08__NorthCarolina4.md`
- DONE `2026-01-08__Ohio4.md`
- DONE `2026-01-08__OntarioCanada4.md`
- DONE `2026-01-08__Pennsylvania4.md`
- DONE `2026-01-08__PuertoRico4.md`
- DONE `2026-01-08__SouthCarolina4.md`
- DONE `2026-01-08__Virginia4.md`

## D=2026-01-09 (H=2026-01-08)

- DONE `2026-01-09__CONTROL_CENTER.md`
- DONE `2026-01-09__Connecticut4.md`
- DONE `2026-01-09__Delaware4.md`
- DONE `2026-01-09__Florida4.md`
- DONE `2026-01-09__Indiana4.md`
- DONE `2026-01-09__Michigan4.md`
- DONE `2026-01-09__NewJersey4.md`
- DONE `2026-01-09__NewYork4.md`
- DONE `2026-01-09__NorthCarolina4.md`
- DONE `2026-01-09__Ohio4.md`
- DONE `2026-01-09__OntarioCanada4.md`
- DONE `2026-01-09__Pennsylvania4.md`
- DONE `2026-01-09__PuertoRico4.md`
- DONE `2026-01-09__SouthCarolina4.md`
- DONE `2026-01-09__Virginia4.md`
