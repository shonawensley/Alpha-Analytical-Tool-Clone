# Stable Family Vote V2 Validation

Date: `2026-03-11`

Purpose: validate the first bounded `Priority 4` promotion rule that lets Stable family/lane evidence survive beyond the legacy `family_score_max` cut without widening packs destructively.

## What Changed

- Added `stable_family_vote_v2` to [`scripts/tools/create_candidate_universe.py`](/home/ser/code/Alpha-Analytical-Tool-Clone/scripts/tools/create_candidate_universe.py).
- Kept legacy `stable_family_vote` unchanged.
- `stable_family_vote_v2` is:
  - default-off,
  - bounded by the existing lane cost cap,
  - limited to extra family promotions beyond the legacy top-family cut,
  - driven by richer arena evidence rather than raw family max only.

Primary promotion signals:
- `family_score_total`
- `family_score_max`
- `best_compound_score_max`
- progression / survivor counts
- current/frontier counts, especially `Set1` + `Col1/Col2`
- arena-vs-legacy rank lift

Secondary corroborators:
- hidden-family reveal density
- order / transform density

## 4-Case Gate

Command shape:

```bash
python3 scripts/tools/create_candidate_universe.py \
  --date <D> \
  --sharepacks-root sharepacks/_predictive \
  --profile tool_only \
  --experiment-tag stable_family_vote_v2_review \
  --top-n-stable 3 \
  --top-n-stable-families 3 \
  --top-n-stable-families-v2 1 \
  --stable-lane-closure-max-cost-units 12 \
  --write-stable-arena \
  --force
```

Reviewed cases:
- `C035 / 2026-01-06 / NewYork4`
- `C036 / 2026-01-02 / Delaware4`
- `2026-01-09 / Pennsylvania4`
- `2026-01-08 / NorthCarolina4`

Findings:

1. `C035 / NewYork4 / Evening 342` is a true rescue.
   - Baseline `stable10` CU did not carry boxed canonical `234`.
   - `stable_family_vote_v2` promoted `Evening family 30` with canonicals `234` and `478`.
   - Result:
     - baseline box = `0`
     - v2 box = `1`
     - baseline stable-family lane hit = `0`
     - v2 lane hit = `1`

2. `C036 / Delaware4` does not get a fake rescue.
   - Baseline already preserved both midday and evening winners in the broader CU.
   - `stable_family_vote_v2` did not create a misleading win story.
   - This is good: the slice is not pretending to solve a within-lane problem it does not actually solve.

3. `Pennsylvania4 / 2026-01-09` shows a bounded lane rescue.
   - Midday winner `811` already boxed via baseline CU, but the new promoted `Combined family 18` adds the correct lane explicitly.
   - This is a “lane rescue without needing a new box rescue.”

4. `NorthCarolina4 / 2026-01-08` stays noisy.
   - No midday or evening rescue.
   - This is also good: the rule did not manufacture a fake fix in the noisy control.

## January Window Harness

Harness:
- dates: `2026-01-01` through `2026-01-09`
- root: `sharepacks/_predictive`
- profile: `tool_only`
- baseline comparison: existing `candidate_universe__tool_only__stable10.json`
- v2 comparison: `candidate_universe__tool_only__stable_family_vote_v2_harness.json`

Evaluable events:
- `245`

Scorecard:

| Metric | Baseline `stable10` | With `stable_family_vote_v2` | Delta |
|---|---:|---:|---:|
| exact hits in CU union | 50 | 64 | +14 |
| boxed hits in CU union | 63 | 75 | +12 |
| winner family present in Stable family-vote packs | 0 | 23 | +23 |
| exact rescues vs baseline | - | 19 | +19 |
| boxed rescues vs baseline | - | 18 | +18 |
| lane-only rescues (family hit, no box hit) | - | 13 | +13 |

Containment:
- still `39` packs per state CU in this harness setup
- the new method adds only one extra bounded family-lane pack per variant/section
- no pack explosion was observed

Representative rescues:
- `2026-01-03 / NewYork4 / Midday / 243` -> canonical `234`, family `30`
- `2026-01-06 / NewYork4 / Evening / 342` -> canonical `234`, family `30`
- `2026-01-06 / NewJersey4 / Evening / 942`
- `2026-01-05 / OntarioCanada4 / Evening / 797`
- `2026-01-09 / Delaware4 / Midday / 843`

Representative lane-only rescues:
- `2026-01-02 / NewYork4 / Evening / 256`
- `2026-01-03 / NewJersey4 / Midday / 293`
- `2026-01-03 / OntarioCanada4 / Midday / 968`
- `2026-01-07 / Pennsylvania4 / Evening / 263`

Interpretation:
- This slice is doing what it was supposed to do:
  - rescue winner families and some boxed winners that the legacy top-family cut dropped,
  - while staying bounded enough to avoid obvious pack explosion.
- It is not the final conversion answer.
  - The presence of `13` lane-only rescues means the rule is improving preservation faster than it is improving within-lane closure.
  - That is acceptable for this stage because `Priority 4` was a promotion/preservation task, not a full closure redesign.

## Main Takeaways

- `stable_family_vote_v2` is worth keeping.
- The most important design move was giving the scorer an explicit `arena rank lift vs legacy rank` term.
  - That made the rule prefer true rescue families like `NewYork4 family 30` instead of merely strong excluded families.
- Hidden-family reveal and order-transform features were useful as corroborators, not primary gates.
- The slice improved recall/preservation in a measurable way and stayed bounded.

## Recommended Next Move

Move to the next approved development slice:
- `TOOL-008`
- `ARENA-010`
- pair-anchor + lingering fourth-variable closure

Reason:
- Stable promotion is now materially better.
- The biggest remaining gap is no longer “did we preserve the right lane?”
- It is increasingly “how do we close cheaply around the right structural core once we have it?”
