# AAT9 Research Checkpoints

This directory contains immutable, curated snapshots of durable research state.
It exists because active working notes under `tasks/` are intentionally ignored
and bulk analytical outputs are too large and volatile for normal Git history.

Each dated checkpoint must:

- preserve source files without moving or rewriting them;
- identify the source path and snapshot path;
- record byte size and SHA-256 receipts;
- distinguish accepted truth, hypotheses, contaminated evidence, and deferred
  work;
- retain only compact manifests and contracts for regenerable bulk artifacts;
- avoid becoming a second live workflow or generated-output directory.

Current checkpoint: [`2026-08-05/`](2026-08-05/README.md).
