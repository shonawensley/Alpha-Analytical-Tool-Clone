# Git Stabilization Completion

Date: 2026-08-06
Branch: `checkpoint/deep-review-extraction-v1-2026-08-05`
Pushed head before this record: `4a5c05c3`
Policy: preservation first; no reset, bulk deletion, worktree removal, or remote/config change

## Accepted Commit Chain

- `176b3571` preserves the Deep Review and Extraction checkpoint.
- `8a6b45f3` preserves variable-length R2/R4/R6/R8 values without synthetic zero padding.
- `8c43aa37` separates ordered VTRAC-straight and boxed-VTRAC semantics.
- `e281b0a7` through `9021946e` preserve lossless AUX, positional, due-doubles, and AUX CORE evidence.
- `141d5d98` adds review-only VTRAC corridor evidence without runtime score or rank changes.
- `415d4f86` and `9beb23ce` add bounded shadow candidate-slate experiments.
- `e0a19df0` locks the corrected Extraction Zone 1 and Zone 2 coordinate contract.
- `8ceabdc8` and `acbb8a8a` add verified Gold Day packaging and RUNS_2 navigation tools.
- `ccd10d13` adds bounded R-pattern provenance and replay-comparison tools.
- `4a5c05c3` adds an Analysis Arena availability audit with an explicit claim boundary.

## Verification

- Affected regression suite: `94 passed` across 15 test modules.
- Corrected Zone 1: 108 cells per case.
- Corrected Zone 2: 192 cells per case, with no Set2 cells, no Set1/Draw1 cells, and no N/A Set1/Draw3/C6 cell.
- R-pattern comparison: 28 outcomes, 344 synthetic zero removals, 42 strict consensus locations, and zero source-only-to-current table-cell changes.
- Analysis Arena audit smoke: 97 contract features across 15 dates and 14 states; 7,294 artifact-manifest rows.
- Provenance smoke confirmed `cc_sanity_snapshot.py` is absent from the accepted runtime patch and snapshot.
- `modules.blackapple` imports from this repository.
- Cleaned draw inputs are present under `data/cleaned/draws/` (53 `*_draws.csv` files).

## Claim Boundaries

- Winner-aware joins and corridor evidence are post-result diagnostics and receive no frozen predictive credit.
- Analysis Arena `explicit` and `folded` statuses prove availability and navigability only. They do not prove synthesis consumption, calibration, independent convergence, ranking influence, promotion, translation, or predictive value.
- Shadow slates are experiments, not standard cadence or live scoring behavior.
- Gold Day 1 remains a post-result mechanism-discovery corpus, not an accepted predictive baseline.

## Intentionally Deferred Inventory

- 210 modified predictive Markdown reports are retained as an unaudited presentation refresh.
- `REVIEW_INDEX.md`, `REVIEW_MANIFEST.json`, and two final-doc drafts remain unaccepted working outputs.
- `scripts/tools/cc_sanity_snapshot.py` remains quarantined because its proposed `vt_straight_hit` check is self-referential.
- 25 tracked task-path deletions remain unstaged. Their content is preserved and reconciled in this checkpoint.
- 7,236 untracked generated files remain outside Git: 4,744 under `docs/`, 1,271 under `sharepacks/`, 1,204 under `.codex/`, and 17 under `data/`.
- All secondary worktrees remain preserved and are documented in `WORKTREE_AUDIT.md`.

These items are not lost and are not accepted runtime changes. They require a later, category-specific decision; they must not be swept into one commit or removed merely to make `git status` visually clean.

## Resume Point

The repository now has a pushed, reviewable branch containing the accepted repairs and bounded review infrastructure. Resume product work from the dual-workflow checkpoint: keep the Template Workflow and Extraction Zone workflow separate until corrected blind/reveal Gold Day evidence is ready for their planned analysis-stage reunion.
