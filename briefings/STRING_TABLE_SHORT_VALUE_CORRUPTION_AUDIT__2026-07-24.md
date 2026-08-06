# String-Table Short-Value Corruption Audit

Date: 2026-07-24

## Executive Finding

The winner HTML renderer was not inventing leading zeros. The active table
pipeline changed variable-length R2/R4/R6/R8 reduction strings before writing
the table CSV and JSON artifacts. Winner HTML/JSON and multiple analytical
tools then consumed those altered tables.

The defect was row-type confusion:

- Actual draw values are fixed-width Pick 3 values and should be normalized to
  three digits.
- R2/R4/R6/R8 values are variable-length reduction strings and must retain
  their exact source length.
- The shared builder applied three-digit zero-padding to both categories.

The NewJersey4 2026-03-10 example proves the issue:

| Location | Historical workbook | Frozen artifact | Correct fixed artifact |
|---|---:|---:|---:|
| Midday Set3 Draw1 R2 C2/C1 | `7` | `007*` | `7*` |
| Combined Set3 Draw1 R2 C2/C1 | `6` | `006*` | `6*` |
| Combined Set1 Draw1 R2 C3 | `96` | `096**` | `96**` |
| Combined Set1 Draw1 R2 C2/C1 | `9` | `009**` | `9**` |
| Combined Set2 Draw1 R2 C1 | blank | `nan*` | blank |

## Root Cause

The active code path is:

`historical workbook -> cleaned workbook -> extractor -> combined table CSV
-> table JSON -> analytical tools and winner reports`

Two independent defects were found:

1. `src/utils/table_generator.py` zero-padded every numeric value of length
   three or less. It did not restrict padding to `draw_data`.
2. `src/utils/extract_data.py` converted pandas missing values to the literal
   string `nan` before the builder could recognize them as missing.

The first defect dates to commit `9decec98b` on 2025-06-21.

The top-level legacy `utils` path did not contain the same zero-padding loop,
but its extractor could still materialize `nan`, and its hot-zone marker could
create star-only content in blank cells.

## Authoritative Corpus Census

The census compared each frozen predictive table with its prior-day historical
workbook. It did not infer corruption merely from a leading zero, so legitimate
source values such as an actual `096` were not counted as defects.

Scope:

- 34 predictive dates
- 14 states
- 476 state-days
- 239,904 active source pattern cells
- 119,952 expected Set1 structural left blanks, excluded from active-cell totals
- zero missing workbooks, sheets, or frozen table JSON files

Results:

| Classification | Cells | Interpretation |
|---|---:|---|
| Exact nonblank match | 227,194 | Source value was preserved |
| Synthetic zero-padding | 11,792 | One- or two-digit R-pattern gained leading zero(s) |
| Source blank serialized as `nan` | 611 | Legitimate empty/exhausted active cell was represented incorrectly |
| Formula/error source represented as `nan` | 301 | Separate PuertoRico4 source/formula issue on 2026-01-07 and 2026-01-08 |
| Exact active blank | 6 | Blank remained blank |

Synthetic zero-padding affected 4.92 percent of active R-pattern cells. It was
present on every audited date and in every state in aggregate. The concentration
was strongest in the rightmost reduction boxes:

| Column | Padded cells |
|---|---:|
| C1 | 7,580 |
| C2 | 3,448 |
| C3 | 752 |
| C4 | 12 |
| C5-C7 | 0 |

This distribution is consistent with the defect appearing as reduction strings
approach completion.

## Consensus Impact

The source-workbook C1/C2 census found:

- 1,454 suffix-consensus events
- 884 source single-digit events
- 570 source two-digit events
- 1,357 strict equal-value events
- 809 strict one-digit equal events
- 445 strict two-digit equal events
- 89 strict three-digit equal events
- 14 strict four-digit equal events

All 809 strict one-digit consensus events were misclassified by the generated
tables. For example:

`6 / 6 / 6 / 6` became `006 / 006 / 006 / 006`

The R-consensus harness then interpreted that as two-digit `tail06`, not
single-digit `tail6`. The events were generally not deleted, but their identity,
length class, visible form, and any length-dependent interpretation were wrong.
That directly explains why searches for the expected single-digit consensus
forms failed.

## Blast Radius

Directly affected artifacts and consumers:

- Combined string-table CSV files
- Table JSON mirrors
- Winner HTML reports
- Winner JSON reports
- Stable Pattern Extractor
- Digit Reduction
- Hot Zones
- Enhanced VTRAC
- R-consensus harness and rollups

Verified NewJersey4 evidence includes:

- Stable output visibly treating fabricated `006` and `009` as patterns.
- Enhanced VTRAC output containing scored `006`, `007`, `009`, and `054`
  entries derived from altered table cells.
- Hot Zones emitting `009` as a triad candidate.
- Digit Reduction consuming the altered digit strings, so inserted zeros can
  affect reduction evidence even when a report does not display the full cell.

Potentially affected downstream layers:

- Aggregated Analysis Arena
- Translation Sandbox
- Candidate Universe
- Play Cards and portfolio outputs
- Brain 2 artifacts derived from affected Brain 1 evidence

These downstream artifacts are marked potentially contaminated, not universally
invalid. The correct next test is an isolated before/after replay and influence
diff, because a changed upstream cell does not prove every downstream decision
changed.

Not directly affected:

- Aux and Blackapple draw ingestion from `data/cleaned/*_draws.csv`

Those pipelines consume draw CSVs rather than string-table reduction cells.
They can only be affected indirectly if later aggregation combines them with
contaminated Brain 1 evidence.

## Implemented Repair

The source repair is deliberately narrow:

- `src/utils/extract_data.py`
  - Missing cells remain empty.
  - Actual draws remain three-digit normalized.
  - R-pattern values retain source length.
- `src/utils/table_generator.py`
  - Three-digit padding is restricted to `draw_data`.
  - R2/R4/R6/R8 values never gain digits.
  - Textual missing-value tokens are suppressed defensively.
- `utils/extract_data.py`
  - Legacy entry points receive the same missing-value and draw formatting guard.
- `utils/table_generator.py`
  - Blank cells no longer receive star-only hot-zone content.
- `tests/test_table_generation_value_integrity.py`
  - Covers one-digit and two-digit patterns, genuine leading-zero patterns,
    fixed-width draws, single-digit consensus, blank cells, and both import paths.

The repaired NewJersey4 pilot produced:

- 44 restored short pattern cells
- 7 strict C1/C2 equal-value consensus events
- 7 strict single-digit consensus events
- no literal `nan`, `<NA>`, or `None` cells

## Fixed Winner Inventory

Original reports are preserved at:

`reports/stable/winners_by_date`

Corrected reports are generated separately at:

`reports/stable/winners_by_date_fixed`

A sibling tree is used rather than a `fixed` child under `winners_by_date`
because existing consumers may treat every child of the original root as a date.

The fixed inventory:

- reads each prior-day historical workbook directly;
- rebuilds source-faithful in-memory tables;
- uses actual result files for winner selection;
- emits one canonical HTML/JSON pair per date/state/winner;
- embeds repair provenance in each JSON report;
- records per-state short-pattern and consensus integrity counts;
- writes `REBUILD_MANIFEST.json`;
- never overwrites the original reports or frozen predictive sharepacks.

The completed corrected inventory contains:

- 1,100 canonical HTML reports and 1,100 matching JSON reports
- 553 completed state-days across 40 populated date directories
- 2 empty legacy source-date directories recorded in the manifest
- 0 generation failures
- 13,544 source-faithful one- or two-digit R-pattern cells
- 1,605 strict end-box consensus events, including 916 single-digit events
- 0 unmatched HTML/JSON pairs
- 0 literal `nan`, `<NA>`, or `None` table cells

The original inventory remains unchanged at 1,798 HTML reports and 1,689 JSON
reports. The different fixed-report count is intentional: duplicate historical
renderings are consolidated into one canonical report per date, state, and
winner.

## Required Follow-Up

1. Treat existing winner HTML/JSON and frozen table artifacts as unreliable for
   short-pattern length and single-digit consensus interpretation.
2. Use the fixed winner inventory for manual Section A string-table analysis.
3. Run one full predictive day into a new isolated sharepack root and compare
   Stable, Digit Reduction, Hot Zones, VTRAC, R-consensus, Arena, Sandbox,
   Candidate Universe, and Play Cards against the frozen original.
4. Classify each downstream difference as corrected evidence, unchanged output,
   or unrelated noise before deciding how much of the historical predictive
   corpus to regenerate.
5. Add a pipeline invariant that rejects any R-pattern output whose unstarred
   value differs from its extracted source value.

No conclusion from the current audit requires discarding Aux/Blackapple data or
the Deep Review template. However, prior manual string-table findings involving
short end-box values, consensus length, or zero-bearing triads should be checked
against the fixed reports.
