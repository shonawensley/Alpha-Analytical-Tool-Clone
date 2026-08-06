# Deleted-Path Reconciliation

This receipt covers the 25 tracked paths that are absent from the working tree
at this checkpoint.

## Result

- Every deleted path has a content-equivalent successor after normalizing only
  CRLF/LF line endings.
- `tasks/important_insights.txt` was found under four renamed copies; one is
  promoted here as the representative successor.
- The deleted `tasks/positional_tool.md` and
  `tasks/positional_research.md` were duplicate content. The relocated
  `positional_research.md` preserves that content, while the relocated
  `positional_tool.md` is a later expanded document and is also snapshotted.
- The empty `New Text Document.txt` is preserved for exact auditability even
  though it carries no research content.

`DELETION_RECONCILIATION.tsv` records the one-to-one evidence. The promoted
files under `snapshots/legacy_relocations/` are immutable copies; their ignored
`tasks/` sources were not edited or moved.

## Git Policy

This audit makes the deletions recoverable and reviewable. It does not, by
itself, authorize mixing them into an unrelated source-code commit. Deletion
recording remains a dedicated documentation/provenance commit.
