# Predictive Report Rewrite Audit

Scope: the 210 modified Markdown files under the March 9-23 predictive review
window.

## Findings

- All 210 files have the same diff shape: 24 added lines and 24 removed lines.
- A mechanical normalization of the new absolute clickable links back to the
  prior inline-code path format reproduces the committed file exactly for all
  210 reports.
- No candidate, score, VTRAC, tool, state, date, or analytical narrative value
  changed in this batch.
- The batch is nevertheless not a current deterministic regeneration. A fresh
  report from the validated generator now includes the Brain 2 receipt fields
  `display_order`, `legacy_rank`, `analytical_rank`, and
  `rank_integrity=INVALID_STATIC_ORDER`; the rewritten reports still contain
  the older static `rank` line.

## Disposition

Status: `QUARANTINED_STALE_PRESENTATION_REFRESH`.

The 210 report changes, `REVIEW_INDEX.md`, and the timestamp-only
`REVIEW_MANIFEST.json` refresh must not enter the research-checkpoint or source
commits. They remain untouched in the working tree until the window package is
deliberately regenerated from an accepted generator and evidence baseline.

This is a provenance/generation mismatch, not evidence that the underlying
predictive datasets were recalculated incorrectly.
