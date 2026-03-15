# DR Case Decision - Virginia4 Midday 473

Purpose: convert the Virginia4 Midday `473` deep review into an actionable DR design note that directly informs `DR Arena v1.1`, later DR consumer changes, and any eventual `V2` vs `V3` decision.

Related:
- `tasks/EXAMPLE BREAKDOWN.txt`
- `tasks/PRO_TALK8.txt`
- `tasks/DR_BATCH3_REVIEW_PACK/2025-06-21__Virginia4__Midday__473/winner.html`
- `tasks/DR_BATCH3_REVIEW_PACK/2025-06-21__Virginia4__Midday__473/dr_overlay.html`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_ARENA_V1__PARITY_AUDIT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_NEXT_STEP_RECOMMENDATION.md`

---

## Why this case matters

Virginia4 Midday `473` is not important because it is a random miss.

It is important because it exposes the next missing DR layer **after** the recent revamp:

- the current DR stack can already preserve several strong evidence classes,
- but this case shows that a structurally active winner environment can still look empty if we rely too heavily on compressed summary accounting and post-reduction literal matching.

This is exactly the kind of case that tells us what `DR Arena v1.1` must add.

---

## Current classification

Old working read:
- strong control / empty-lens candidate

Updated read:
- `false-empty challenge`
- `active but low-trust`
- `buried-positive family / permutation environment`

This case should **not** be used as a clean no-signal control anymore.

---

## What the current artifacts objectively say

### 1. Winner stamp / current summary accounting

`dr_winner_stamp.json` reports:

- winner = `473`
- canon = `347`
- winner family variants = `423, 428, 473, 478, 923, 928, 973, 978`
- all current summary counts = `0`
- all earliest steps = `-1`

The overlay banner says the same thing:

- `Exact: 0`
- `V-TRAC: 0`
- `Drop Exact: 0`
- `Drop V-TRAC: 0`
- `3-Value Exact: 0`
- `3-Value V-TRAC: 0`

On the compressed DR summary surface, this looks empty.

### 2. Winner HTML says the environment is active

The winner HTML shows repeated structure in the winner neighborhood:

- `3447`
- `8447`
- `2443`
- `40877`
- `70988224`
- explicit `347` appearances in the Midday ladder
- repeated `437` and `734` relationships

The stats section reinforces that the literal winner is the wrong measurement surface:

- `473` occurrences = `0`
- `347` occurrences = `0`
- `437` occurrences = `3`, persistence = `5`
- `734` occurrences = `3`, persistence = `5`
- strongest competing motif = `324`, occurrences = `16`, persistence = `34`

So the case is not empty. The case is structurally alive in a way the compressed DR accounting does not describe well.

### 3. Overlay body contradicts overlay summary

The current overlay body still contains winner-related spans, including:

- exact-labeled `437`
- VTRAC-labeled values such as `599248`, `5992248`, `559922486`, `55992486`

That means this case contains an internal mismatch:

- the overlay header says there were zero hits
- the overlay body still highlights winner-related objects

This is a direct audit issue. It means the current summary layer can under-report or mis-state what the body is actually surfacing.

---

## What the earlier DR revamp already accomplished

This case does **not** invalidate the DR revamp completed so far.

The earlier work already accomplished three major things:

1. Reframed DR correctly
- DR is no longer judged only as a weak top-candidate caller.
- It is now treated as a structural evidence tool.

2. Built the super-harness
- We can now separate:
  - trace-strong / caller-weak cases
  - lane-only cases
  - double-pressure cases
  - row-repeat / final-survival cases
  - true or false controls

3. Built `DR Arena v1`
- DR now preserves structured evidence classes instead of collapsing everything into one `best_pattern`.

That work already held up across parity and broad-screen validation.

So Virginia `473` is **not** proof that the revamp failed.
It is proof that the revamp succeeded far enough to expose the next missing layer clearly.

---

## What this case adds beyond the current revamp

Virginia `473` adds pressure in six specific directions.

### 1. Pre-reduction cluster strength must become first-class

The case shows that strong winner-family evidence can exist **before** reduction in the mapped boxes.

Needed surface:
- `pre_reduction_cluster_strength`

What it should capture:
- cluster density in mapped boxes before any transit-digit elimination
- cross-box persistence
- cross-variant recurrence
- current-day ladder proximity

### 2. Permutation-neighborhood scoring is missing

The actual active object here is not just `473`.
It is the neighborhood around:

- `347`
- `437`
- `734`

Needed surface:
- `permutation_cluster_strength`

What it should capture:
- persistent ordered fragments
- repeated winner permutations
- winner-near straight structures that imply the same boxed truth

### 3. VTRAC-cluster scoring inside stable rows is still too weak

The case reinforces that stable rows can carry VTRAC-family truth even when literal winner counts are zero.

Needed surface:
- `vtrac_cluster_strength`

What it should capture:
- VTRAC-family recurrence inside `R2/R4/R6/R8`
- VTRAC-family progression across mapped boxes
- VTRAC-family persistence across variants

### 4. Reveal purity must be measured explicitly

Your review correctly emphasizes cases where a reduction leaves one family or one cluster dominant, or close to the only meaningful thing remaining in the box.

Needed surface:
- `reveal_purity`

What it should capture:
- concentration after reduction
- whether a cluster becomes the only meaningful survivor
- whether the box gets cleaner in a way that reinforces the same family rather than fragmenting further

### 5. Protected-core reduction should become an experimental pass

This case strongly supports the idea that reduction can destroy the most important core if it is applied blindly.

Needed experimental surface:
- `protected_core_reduction_candidate`

Meaning:
- detect a strong core first from pre-reduction evidence
- then allow one experimental reduction pass that avoids stripping the protected core while still removing likely clutter

This should be treated as a bounded experiment, not a default or hindsight rule.

### 6. Summary-vs-body mismatch needs audit treatment

This case proves we need a direct audit surface when:

- overlay summary says one thing
- body-level highlighted values say something else

Needed audit surface:
- `overlay_summary_mismatch`

This matters both for trust and for later coding work, because it tells us whether the missing problem is:

- extraction
- summarization
- or classification

---

## What this case does not prove

Virginia `473` does **not** by itself prove:

- immediate Analyzer `V3`
- immediate DR extractor rewrite
- broad mapped-box deletion
- broad DR weight retuning
- automatic fourth-variable combo generation

The correct read is narrower:

- current DR evidence preservation is real
- current arena classification is directionally useful
- but the next arena layer still undercaptures a deeper structural class

That means the next move should still be:

1. use this case to refine `DR Arena v1.1`
2. then revisit consumer changes
3. then revisit `V2` vs `V3`

---

## Immediate implications for Batch 3

Virginia `473` should now be used as:

- the anchor `false-empty challenge`
- not the anchor pure control

That changes the meaning of the next calibration step.

`DR Arena v1.1` should now aim to separate:

- `true empty`
- `active but low-trust`
- `positive buried trace`

Virginia `473` belongs in the second bucket, with buried-positive structure.

---

## Immediate implications for coding

This case should directly influence the next DR coding layer in this order:

1. `DR Arena v1.1`
- refine `dr_empty_lens`
- add stronger discrimination for false-empty cases

2. Arena feature expansion
- add or prototype:
  - `pre_reduction_cluster_strength`
  - `permutation_cluster_strength`
  - `vtrac_cluster_strength`
  - `reveal_purity`
  - `overlay_summary_mismatch`

3. Experimental reduction logic
- design, but do not yet productionize:
  - `protected_core_reduction_candidate`

4. Consumer-side DR change
- later use the richer arena evidence rather than reviving old top-candidate ranking

---

## Bottom line

Virginia4 Midday `473` is a very high-value DR case.

Not because it proves the recent revamp was wrong.
Because it proves the recent revamp was useful enough to reveal the next missing structural layer:

- pre-reduction cluster truth
- permutation-neighborhood truth
- reveal purity
- and summary-vs-body mismatch

This is the correct kind of case to push `DR Arena v1.1` forward aggressively and productively.
