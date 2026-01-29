# v0.3 Predictive Glossary (tool_only)

Purpose: a single-page glossary so we stop spiraling on “what does this metric mean?” during reviews.

If you feel lost, start with:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`

---

## Core time variables

- **H** = history workbook date (“what we knew”; input day)
- **D** = results date (“what happened”; sharepack folder day)  
  **Rule:** `D = H + 1`

---

## Core layers (do not mix these up)

- **Sharepacks** = frozen evidence snapshot (`sharepacks/_predictive/<D>/...`). Winner-free at PRE time.
- **RUNS** = review/grades layer (CSV/MD under `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`).
- **Candidate Universe (CU)** = unbounded pool (“what we could play”) built from tool evidence packs.
- **Play Card** = budgeted selection (“what we would play”) produced by a named strategy at a fixed budget.

Budgets:
- **B12/B24/B36** = *line count* in the Play Card. Budgets are selection cuts, not tool behavior.

---

## Canonical vs straight vs boxed

- **Winner** (straight) = the exact 3-digit string (e.g., `950`).
- **Canonical** = digits sorted (boxed identity), 3-digit text (e.g., `950` → canonical `059`).
- **Permutation hit (“perm hit”)** = any permutation of the winner canonical appears (e.g., any of `059 095 509 590 905 950`).
- **Strict boxed hit (“box closure”)** = all permutations of a canonical are present in the Play Card (6 lines for most canonicals).

Excel note: canonicals must be treated as 3-char text (`"028"`, not `28`) to avoid leading-zero confusion.

---

## The 3 hit contracts (strict vs lane vs inclusive)

These are emitted by the Play Card grader (`scripts/tools/grade_play_card.py`), and used by ladder/scoreboard reports.

- **Strict**: `hit_any`
  - `straight_hit` = exact winner is in the card
  - `box_hit` = strict box closure for the winner canonical is present
  - `hit_any = straight_hit OR box_hit`

- **Lane signal**: `vtrac_index_hit`
  - Means the card contains at least one combo from the winner’s VTRAC index (“touched the neighborhood”).

- **Inclusive coverage**: `hit_any_inclusive`
  - “Did we retain the lane or better?”
  - Computed as: `straight_hit OR canon_hit_any_perm OR vtrac_index_hit`

Important: **`hit_any_inclusive` is not strict**. It is the “coverage contract”.

---

## Pack vs filler (multi-pack strategies)

Many B36 strategies have a `vtrac_pack` section in the Play Card JSON.

- **Pack** = combos inserted by the strategy as “pack semantics” (often VTRAC display/member packs)
- **Filler** = convergence top-ups after pack insertion (if any)

Key bridge metrics:
- **`pack_correct`** = chosen pack index equals winner index (single-pack correctness)
- **`pack_any_correct`** = winner index is among the multi-pack indices (multi-pack correctness)
- **`pack_straight_hit`** = exact winner appears inside the pack combos
- **`pack_box_hit`** = winner canonical perm-hit inside the pack combos (not strict box closure)

---

## Ladder / scoreboard buckets (where did it break?)

Defined in `scripts/tools/create_conversion_ladder_report.py`:

- **HIT_INCLUSIVE**: Play Card retained the lane or better (`hit_any_inclusive=1`)
- **CU_EXACT_BUT_PLAY_MISS**: CU had the exact/perm winner, but Play Card lost it
- **CU_LANE_BUT_PLAY_MISS**: CU touched winner lane, but Play Card lost it
- **CU_MISS**: CU did not have the winner (exact or lane)
- **CENSORED**: `winner_missing=1` (unknown outcome; do not count as misses)

---

## “Stable10”

**stable10** is a Candidate Universe posture: it sets `--top-n-stable 10` when building the CU.

It improves recall (lane/coverage) so downstream selection can work.

---

## “Spine4 + index tail” (current B36 default)

Strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail`

Meaning:
- **Spine**: deep pack semantics for the top ~4 ranked indices (where strict hits were coming from)
- **Tail**: spend remaining budget touching additional ranked indices (often 1 line per index)

This is designed to reduce `CU_LANE_BUT_PLAY_MISS` without sacrificing strict hits from the spine.

