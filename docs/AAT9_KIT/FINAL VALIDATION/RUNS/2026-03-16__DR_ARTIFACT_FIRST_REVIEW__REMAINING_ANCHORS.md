# DR Artifact-First Review — Remaining Anchors

Date: `2026-03-16`

## Purpose

Review the strongest remaining DR promotion-gap anchors directly against:

- winner HTML / JSON artifacts
- current DR arena surfaces
- frozen gold-day audit ranks

The goal is to decide whether:

1. there is still one more real DR-local rule worth coding, or
2. DR has reached a strong enough handoff point for the aggregated analysis-arena phase

This review uses the current DR keeper stack:

- `dr_vtrac_lane_gateway`
- `dr_vtrac_cluster_strength`
- `dr_assigned_box_vtrac_strength`
- `dr_vtrac_fusion_strength`

## Review Set

High-signal anchors reviewed:

1. `2026-01-04 / Indiana4 / Midday / 813 / VT 23`
2. `2025-12-31 / Virginia4 / Evening / 636 / VT 18`
3. `2026-01-01 / Delaware4 / Midday / 149 / VT 25`
4. `2026-01-09 / Connecticut4 / Midday / 234 / VT 30`
5. `2025-12-30 / Florida4 / Midday / 377 / VT 27`
6. `2026-01-08 / Delaware4 / Evening / 031 / VT 8`

These were chosen to cover:

- buried but assigned-box rescued
- visible but still awkward
- still-missed cases with strong winners-table signal

## Anchor Findings

### 1. Indiana4 Midday `813` / VT `23`

Artifacts:

- [winner.html](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2026-01-04/Indiana4/winners/Indiana4/Indiana4_vtrac23_winner_813_20260105_055131.html)
- [winner.json](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2026-01-04/Indiana4/winners/Indiana4/Indiana4_vtrac23_winner_813_20260105_055131.json)
- [overlay](/home/ser/code/Alpha-Analytical-Tool-Clone/data/outputs/analysis/digit_reduction/Indiana4/analyzer_v2/winners/20260105_Midday_winner_overlay.html)

What the artifact shows:

- all 3 variants are heavily tagged
- all 4 rowtypes (`R2/R4/R6/R8`) are involved
- long-string rows are active in every variant
- the dominant winner-family permutations are all same-index `VT 23` forms:
  - `688`
  - `886`
  - `881`
  - `188`
  - `138`
  - `836`

Current DR read:

- `assigned_box rank = 1`
- `fusion rank = 5`
- `best visible = 1`
- gateway/cluster are stolen by another compact world

Classification:

- **not a meaningful remaining DR-local miss**

Reason:

- DR is already feeding the correct winner lane into the arena strongly enough through assigned-box
- this is now mainly a downstream interpretation / handoff question, not a reason for more DR rewriting

### 2. Virginia4 Evening `636` / VT `18`

Artifacts:

- [winner.html](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2025-12-31/Virginia4/winners/Virginia4/Virginia4_vtrac18_winner_636_20260105_052216.html)
- [winner.json](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2025-12-31/Virginia4/winners/Virginia4/Virginia4_vtrac18_winner_636_20260105_052216.json)
- [overlay](/home/ser/code/Alpha-Analytical-Tool-Clone/data/outputs/analysis/digit_reduction/Virginia4/analyzer_v2/winners/20260105_Evening_winner_overlay.html)

What the artifact shows:

- heavy family/winner tagging across all 3 variants
- long-string rows active in every variant
- dominant winner-family permutations are all `VT 18`:
  - `113`
  - `811`
  - `681`
  - `136`

Current DR read:

- `assigned_box rank = 1`
- `fusion rank = 7`
- `best visible = 1`

Classification:

- **not a meaningful remaining DR-local miss**

Reason:

- same story as `Indiana 813`
- the correct winner lane is already preserved in a useful arena surface

### 3. Delaware4 Midday `149` / VT `25`

Artifacts:

- [winner.html](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2026-01-01/Delaware4/winners/Delaware4/Delaware4_vtrac25_winner_149_20260105_053359.html)
- [winner.json](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2026-01-01/Delaware4/winners/Delaware4/Delaware4_vtrac25_winner_149_20260105_053359.json)
- [overlay](/home/ser/code/Alpha-Analytical-Tool-Clone/data/outputs/analysis/digit_reduction/Delaware4/analyzer_v2/winners/20260105_Midday_winner_overlay.html)

What the artifact shows:

- broad tagged activity across all 3 variants
- dominant same-index family is `VT 25` through:
  - `441`
  - `144`
  - `199`

Current DR read:

- `cluster rank = 9`
- `best visible = 9`
- assigned-box is weaker here

Classification:

- **weak remaining DR issue at most**

Reason:

- DR is already making the correct lane visible
- awkward literal-family presentation remains, but this is no longer a strong reason for another DR batch

## Residual DR-Local Gap Class

The following anchors are the strongest evidence that a small residual DR-local miss class still exists.

### 4. Connecticut4 Midday `234` / VT `30`

Artifacts:

- [winner.html](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2026-01-09/Connecticut4/winners/Connecticut4/Connecticut4_vtrac30_winner_234_20260110_035031.html)
- [winner.json](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2026-01-09/Connecticut4/winners/Connecticut4/Connecticut4_vtrac30_winner_234_20260110_035031.json)
- [overlay](/home/ser/code/Alpha-Analytical-Tool-Clone/data/outputs/analysis/digit_reduction/Connecticut4/analyzer_v2/winners/20260110_Midday_winner_overlay.html)

What the artifact shows:

- strong family-gap activity across all 3 variants
- long-string rows are active in all variants
- dominant winner-lane permutations are all `VT 30`:
  - `932`
  - `298`
  - `892`
  - `982`
  - `798`

Current DR read:

- gateway top lanes are `28 / 15 / 25`
- cluster top lanes are `28 / 15 / 31`
- assigned-box top lanes are `15 / 18 / 28`
- winner lane `VT 30` is not visible in the top DR surfaces

Classification:

- **real residual DR-local miss**

### 5. Florida4 Midday `377` / VT `27`

Artifacts:

- [winner.html](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2025-12-30/Florida4/winners/Florida4/Florida4_vtrac27_winner_377_20260105_051152.html)
- [winner.json](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2025-12-30/Florida4/winners/Florida4/Florida4_vtrac27_winner_377_20260105_051152.json)
- [overlay](/home/ser/code/Alpha-Analytical-Tool-Clone/data/outputs/analysis/digit_reduction/Florida4/analyzer_v2/winners/20260105_Midday_winner_overlay.html)

What the artifact shows:

- all 3 variants have tagged family activity
- long-string rows are active in every variant
- dominant winner-lane permutations are all `VT 27`:
  - `877`
  - `377`
  - `773`
  - `778`

Current DR read:

- gateway top lanes are `12 / 5 / 6`
- cluster top lanes are `12 / 23 / 5`
- assigned-box top lanes are `23 / 8 / 32`
- winner lane `VT 27` is not preserved in the top DR surfaces

Classification:

- **real residual DR-local miss**

### 6. Delaware4 Evening `031` / VT `8`

Artifacts:

- [winner.html](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2026-01-08/Delaware4/winners/Delaware4/Delaware4_vtrac8_winner_031_20260110_034418.html)
- [winner.json](/home/ser/code/Alpha-Analytical-Tool-Clone/sharepacks/2026-01-08/Delaware4/winners/Delaware4/Delaware4_vtrac8_winner_031_20260110_034418.json)
- [overlay](/home/ser/code/Alpha-Analytical-Tool-Clone/data/outputs/analysis/digit_reduction/Delaware4/analyzer_v2/winners/20260110_Evening_winner_overlay.html)

What the artifact shows:

- heavy family-gap activity across all 3 variants
- long-string rows active in every variant
- dominant winner-lane permutations are all `VT 8`:
  - `013`
  - `103`
  - `068`
  - `810`
  - `018`
  - `153`

Current DR read:

- gateway top lanes are `15 / 12 / 3`
- cluster top lanes are `15 / 12 / 3`
- assigned-box top lanes are `18 / 15 / 6`
- winner lane `VT 8` is not visible in the top DR surfaces

Classification:

- **real residual DR-local miss**

## What The Residual Misses Have In Common

The strongest remaining DR-local misses are **not** random.

They share a narrower pattern:

1. winner artifacts show a strong **same-index permutation swarm**
2. that swarm is visible across multiple variants and rowtypes
3. long-string activity is present
4. but predictive DR surfaces still prefer other compact lanes
5. neither assigned-box nor cluster/gateway preserves the correct lane strongly enough

Examples:

- `CT 234` -> `932 / 298 / 892 / 982`
- `FL 377` -> `877 / 377 / 773 / 778`
- `DE 031` -> `013 / 103 / 068 / 810 / 018 / 153`

This is different from the already-solved buried regime where assigned-box now recovers the lane successfully.

## Interpretation

This review supports two conclusions at once.

### Conclusion A

The newer DR work was real progress.

Why:

- `Indiana 813`
- `Virginia 636`
- and similar buried anchors

are no longer persuasive reasons for more DR rewriting.
The assigned-box surface already turned them into useful arena evidence.

### Conclusion B

There is still a small residual DR-local miss class.

But it is now much narrower:

- **same-index permutation swarms that the predictive DR rows do not preserve strongly enough**

This is a much cleaner ending point than previous DR cycles.

## Recommendation

My recommendation is:

1. **do not start another broad DR tuning loop**
2. treat the current 4-surface DR package as the keeper baseline
3. if one more DR batch is done at all, it should be only:
   - a bounded prototype aimed at this specific permutation-swarm miss class
4. otherwise, DR is strong enough to hand off and move to the next tools before the aggregated analysis-arena phase

## Practical Stop / Go Read

### `Go one last DR batch` only if:

- we want to test a very narrow `same-index permutation swarm` idea
- and we are willing to reject it quickly if the frozen benchmark does not move

### `Freeze DR now` if:

- we want the best overall project momentum
- we want to move to the remaining tools
- and we accept that the current DR package is already a much stronger arena feed than before

## My Current Lean

I lean slightly toward:

- **freeze DR after this review unless we specifically want one tiny permutation-swarm prototype**

Reason:

- the main buried breakthrough already landed
- fusion already gave a modest final lift
- the remaining DR-local gap is now narrow enough that forcing more DR work risks diminishing returns
