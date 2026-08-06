# Authoritative Extraction Zone Contract

This contract supersedes the contaminated Gold Day 1 Zone 2 renderer mapping.
It applies independently to Midday, Evening, and Combined variants and to the
R2, R4, R6, and R8 rows of each eligible box.

## Zone 1: Historical Feeder Corridor

Per variant:

- Set3 / Draw1 / C7-C5
- Set2 / Draw1 / C7-C5
- Set1 / Draw1 / C7-C5

Count: 9 coordinates x 4 R rows x 3 variants = 108 cells.

## Zone 2: Set1 Progression And Current Frontier

Per variant:

- Set1 / Draw2 / C6-C4
- Set1 / Draw3 / C5-C2
- Set1 / Draw4 / C4-C2
- Set1 / Draw5 / C3-C1
- Set1 / Draw6 / C2-C1
- Set1 / Draw7 / C1

Count: 16 coordinates x 4 R rows x 3 variants = 192 cells.

## Invariants

- Zone 1 and Zone 2 overlap is zero.
- Set1 / Draw1 is Zone 1 only.
- Zone 2 contains no Set2 cell.
- Set1 / Draw3 / C6 is structural N/A and must be rejected.
- Total fixed-zone count is 300 cells.
- A count-only validation is insufficient; exact semantic coordinates must be
  tested.

## Zone 3

Zone 3 is not a fixed rectangle. It represents typed survivor, repeat,
maturity, bridge, collapse, re-entry, hidden-core, consensus-finish, and
double/mirror events elsewhere in the valid table. Unmarked cells may support
Zone 3 analysis but receive no Zone 1 or Zone 2 credit.
