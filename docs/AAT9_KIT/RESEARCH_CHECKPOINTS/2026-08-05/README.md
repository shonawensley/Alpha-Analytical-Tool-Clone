# Deep Review And Extraction Pre-V2 Checkpoint

Date: 2026-08-05
Preservation completed: 2026-08-06
Status: immutable research checkpoint, not a runtime release

This checkpoint freezes the point between the contaminated first Extraction
Gold Day and implementation of Extraction V2. It also preserves the separate
Template Workflow checkpoint so the two research lanes can later reunite.

## Start Here

1. [`CHECKPOINT_STATUS.md`](CHECKPOINT_STATUS.md)
2. [`AUTHORITATIVE_EXTRACTION_ZONE_CONTRACT.md`](AUTHORITATIVE_EXTRACTION_ZONE_CONTRACT.md)
3. [`DUAL_WORKFLOW_REUNION.md`](DUAL_WORKFLOW_REUNION.md)
4. [`SOURCE_MANIFEST.tsv`](SOURCE_MANIFEST.tsv)
5. [`DELETION_RECONCILIATION.md`](DELETION_RECONCILIATION.md)
6. [`GENERATED_REPORT_AUDIT.md`](GENERATED_REPORT_AUDIT.md)
7. [`WORKTREE_AUDIT.md`](WORKTREE_AUDIT.md)
8. [`BULK_ARTIFACT_POINTERS.tsv`](BULK_ARTIFACT_POINTERS.tsv)
9. [`SNAPSHOT_SHA256.txt`](SNAPSHOT_SHA256.txt)

## Durable Snapshots

The `snapshots/` directory contains byte-preserved copies of the current
workflow checkpoint, extraction training and example logs, Deep Review journal
and changelog, V2 plan sources, external Gold Day 1 review, key theory notes,
and compact package manifests.

The legacy relocation snapshots preserve content that had been reorganized
under ignored `tasks/` paths. Their mapping and equivalence checks are in
`DELETION_RECONCILIATION.tsv`.

The original files remain in place. These copies are immutable checkpoint
evidence and must not be treated as independently maintained live documents.

## Explicit Boundary

- No runtime behavior is promoted here.
- No Analysis Arena, Template, Candidate Universe, Play Card, scoring,
  profitability, state-allocation, or wagering behavior is changed here.
- Gold Day 1 is not an accepted predictive baseline.
- Extraction V2 implementation is not part of this checkpoint.
