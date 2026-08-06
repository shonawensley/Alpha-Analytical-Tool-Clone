# Secondary Worktree Audit

No secondary worktree was removed, pruned, reset, cleaned, or rebased.

## Preserved State

| Worktree | Real tracked changes | Checkout/filter churn | Untracked files | Unique files snapshotted |
|---|---:|---:|---:|---:|
| `tmp_deep_review_lab` | 1 | 11 | 2 | 2 |
| `tmp_pre_push_baseline_20260805` | 0 | 11 | 0 | 0 |
| `tmp_pre_push_validation_20260805` | 0 | 11 | 0 | 0 |
| `tmp_rpattern_replay/current` | 11 | 11 | 703 | 47 |
| `tmp_rpattern_replay/source_only` | 4 | 0 | 691 | 48 |

The apparent changes in the checkout/filter column have working bytes identical
to `git show HEAD:<path>`; they are not authored content changes.

## Local Recovery Receipts

The ignored local directory
`.codex/checkpoints/git_stabilization_2026-08-05/worktrees/` contains:

- one binary-capable tracked patch per worktree;
- tracked-file HEAD and working-tree hashes;
- complete untracked-file hashes and main-worktree comparisons;
- copies of every untracked file that is not byte-identical in the main
  worktree; and
- a checksum manifest over the recovery receipts.

Disposition: `PRESERVED_DO_NOT_REMOVE`. Branch pruning, worktree removal, and
large-output cleanup are intentionally deferred until their content is either
promoted or declared reproducible by a separate acceptance decision.
