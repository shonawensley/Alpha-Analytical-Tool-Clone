# Superbrain Primitives (Research Ledger)

Purpose: capture the cross-tool “primitives” we use to form **pre-results** candidate sets, in a way that survives chat resets and can be graded honestly over time.

This doc is **not** a run report and **not** a tool design spec. It’s a shared vocabulary + mapping between:

- **Evidence inputs** (sharepack artifacts)
- **Transforms** (“pack algebra” / combination-forming methods)
- **Candidate Universe packs** (deterministic, gradeable predictions)
- **Grading metrics** (post-results)

Related contracts:
- Candidate Universe schema + rules: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Candidate_Universe_Contract.md`
- Predictive day workflow: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Predictive_Day_Quickstart.md`

---

## Terminology locks (must not drift)

- **Predictive (“before”)**: `sharepacks/_predictive/<D>/...` (no winners; no results)
- **Post-results (“after”)**: `sharepacks/<D>/...` (winners + evaluation allowed)
- **Outcomes**: Midday + Evening only. Combined is a **lens**, not an outcome.
- **Mirror scheme (default)**: `vtrac_pair` (difference‑5 pairing): `0↔5, 1↔6, 2↔7, 3↔8, 4↔9`
- **“VTRAC” disambiguation**:
  - `vtrac_index`: boxed family index (`get_vtrac_index`)
  - `vstraight_lane` / `vstraight_vcode`: positional STR8_8 lane (VSTRAIGHTS semantics)

---

## Primitive → Candidate Universe mapping (current implementation)

The Candidate Universe generator is implemented in:
- `scripts/tools/create_candidate_universe.py`

It emits packs under:
- `sharepacks/_predictive/<D>/<STATE>/candidate_universe.json`

Each pack must include a `transform_chain` so we can later attribute hits to the actual transforms used.

### Control Center primitives

- **Profit Alerts implied set**
  - Evidence: `sharepacks/_predictive/<D>/control_center/profit_alerts.csv`
  - Candidate Universe: `method_id=profit_alerts`
  - Notes: this is the “bet-ready” layer (bounded by CapLines/ImpliedSet). Treat it as a first-class pack.

- **Due Doubles (VTRAC double families)**
  - Evidence: `sharepacks/_predictive/<D>/control_center/due_doubles.csv`
  - Candidate Universe: `method_id=due_doubles` (packs per row/variant: `due_doubles:Combined|Midday|Evening`)
  - Notes:
    - This is grouped by **VTRAC double family** (e.g. `0/5-1/6`), not `vtrac_index` (1–35).
    - Candidate Universe uses a bounded “top-N canonicals” policy and BOX-expands to unique perms so cost stays measurable.
    - Optional derived packs (also bounded): mirror-double expansions from the top due-doubles seed:
      - `method_id=due_doubles_mirror_single` (mirror the single digit)
      - `method_id=due_doubles_mirror_double` (mirror the repeated digit)
    - Optional derived packs (also bounded): mirror-pair closure packs for **mirror-double** conversion:
      - `method_id=mirror_pair_closure` (pair selection + third-digit closure from Aux aggregated digits)
      - `method_id=mirror_pair_closure_due_doubles` (EXPERIMENTAL; pair selection from Due Doubles families; disabled by default)
        - Enable via `create_candidate_universe.py` flags:
          - `--mirror-pair-closure-due-doubles-pairs <N>` (recommended: `2`)
          - `--top-n-mirror-pair-closure-due-doubles <M>` (recommended: `2`)

### Stable patterns primitives

- **Top stable canonicals (per section) → BOX expansion**
  - Evidence: `sharepacks/_predictive/<D>/<STATE>/stable/<STATE>/<STATE>_stable_patterns_scores.csv`
  - Candidate Universe: `method_id=stable_top` (packs per section: Midday/Evening/Combined when present)
  - Transform: `box_expand_unique_perms` (unique permutations of the canonical)
  - Known limitation (important):
    - Stable can sometimes isolate the winner via **families** even when the winner is missing from `patterns_scores.csv` / `patterns_compound.csv`.
    - Example: `2026-01-06 Michigan4 Evening` (Stable families best_rank=1, but gaps include `missing_from_scores`, `missing_from_compound`): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md` (see GOLD-0024).
    - Implication: Candidate Universe may need a future bounded pack sourced from Stable families (selection-layer change, not analyzer tuning).

### Digit Reduction primitives

- **DR Analyzer V2 top candidates (per variant)**
  - Evidence: `sharepacks/_predictive/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/<STATE>_analyzer_v2_top_candidates.csv`
  - Candidate Universe: `method_id=digit_reduction_analyzer_v2`
  - Transform: “use best_pattern per variant” (bounded by top-N)

### VTRAC enhanced primitives

- **VTRAC enhanced top straights**
  - Evidence: `sharepacks/_predictive/<D>/<STATE>/vtrac/<STATE>/<STATE>_vtrac_enhanced_*.json`
  - Candidate Universe: `method_id=vtrac_enhanced_top`
  - Transform: “take top-N `straights_ranked`”
  - Note: these packs frequently produce `vtrac_index_hit_only` (rail correct, canonical wrong). Candidate Universe currently records this via grading; converting it into box hits is a v0.2 selection-layer
    research target (see GOLD-0020, GOLD-0023 in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`).

### Hot Zones primitives

- **Hot Zones top triads**
  - Evidence (preferred): `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<D>_hot_zones_winner_map.json`
  - Evidence (fallback): `sharepacks/_predictive/<D>/<STATE>/hot_zones/<STATE>/<STATE>_hot_zones_top_lanes.csv`
  - Candidate Universe: `method_id=hot_zones_top`
  - Note: the “winner_map” filename is legacy terminology; in predictive mode it is **not** a winners lens.
  - Note: Hot Zones often surfaces the correct **index rail** without the winning canonical (another `vtrac_index_hit_only` driver). Converting this into box hits is a v0.2 selection-layer research target
    (see GOLD-0019, GOLD-0022 in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`).

### Aux primitives

- **Aux positional shortlist (cross-variant tags, double-pressure, mirror-echo)**
  - Evidence: `sharepacks/_predictive/<D>/<STATE>/aux/<STATE>/summary.json`
  - Candidate Universe: `method_id=aux_positional`
  - Notes: Aux is a “structure/pressure” lens; it’s most valuable for narrowing to small, high-pressure sets.

- **Aux VTRAC overdue index closure (boxed-family `vtrac_index`)**
  - Evidence: `sharepacks/_predictive/<D>/<STATE>/aux/<STATE>/summary.json` → `vtrac.overlay_top` (per variant)
  - Candidate Universe: `method_id=aux_vtrac_index_overdue`
  - Transform: take top-N overdue indices per variant and expand each index to its full boxed set (`modules.vtrac_reference.get_index_set`) so the cost is explicit (48 combos per index).

---

## Combination-forming primitives (pack algebra)

These are “bounded transforms” we can apply to an evidence-derived **digit envelope**.

Current generator behavior:
- Derive a pooled envelope (`top4` digits) from candidate universe packs.
- Derive triads via `choose3` from that envelope.
- Emit bounded packs so spend/cost stays measurable.

### Digit envelope (pool)

- Definition: a small digit pool (usually 3–4 digits) meant to represent a “cluster envelope”.
- Candidate Universe: `digit_envelopes[]` + `combo_pack:*`
- Important: the pool must be **pre-results** and must record its sources.

### R-perm-4 (reduced permutation subset)

- Method id: `R-perm-4`
- Transform: `{abc, acb, bca, cba}` (bounded closure)
- Candidate Universe: `pack_id=combo_pack:R-perm-4:envelope`

### Pack A — VT8 expand (ordered)

- Method id: `PackA_vt8`
- Transform: `vt8_expand_ordered(vtrac_pair)` (8 combos, positional)
- Candidate Universe: `pack_id=combo_pack:PackA_vt8:seed=<triad>`

### Pack B — keep pair, mirror third + R-perm-4

- Method id: `PackB_mirror3rd`
- Transform:
  - derive 3 triads by keeping a pair and mirroring the third digit (VTRAC-pair mirror),
  - apply `R-perm-4` to each derived triad (bounded to 12 combos total).
- Candidate Universe: `pack_id=combo_pack:PackB_mirror3rd:seed=<triad>`

### Doubles packs (seed must be a double)

- `doubles_mirror_single`: mirror the single digit (adds a second double triad; 6 perms total)
- `doubles_mirror_double`: mirror the repeated digit (adds a second double triad; 6 perms total)

### Consensus double pack (COMBINATION_FORMING3 “CONSENSUS9”)

- Method id: `consensus_double_9`
- Transform: choose a “trigger digit” (default: Aux aggregated digits with `XVAR-Cons` / `Double-Pressure` tags), build a bounded 9-combo pack around the trigger, and optionally add a small number of stable-derived additions (still bounded).
- Goal: a deterministic, budgetable “consensus double” playset that can be graded honestly over time.

---

## Grading primitives (how we measure)

The Candidate Universe grader is implemented in:
- `scripts/tools/grade_candidate_universe.py`

Outputs:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CANDIDATE_UNIVERSE_GRADE.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CANDIDATE_UNIVERSE_GRADE.md`

Metrics (pack-level):
- `hit_any`: depends on `play_mode` (BOX uses canonical match; STRAIGHT uses literal match)
- `straight_hit`: winner literal is in pack combos
- `box_hit`: winner canonical is in pack canonicals (BOX/MIXED only)
- `vtrac_index_hit`: any combo in the pack shares the winner’s boxed-family `vtrac_index`
- `vtrac_index_hit_only`: lane hit without an exact hit

Important: grading outputs must **never** be written into predictive sharepacks.

### Play Cards (budgeted cuts)

- Generator: `scripts/tools/create_play_card.py`
  - Input: `sharepacks/_predictive/<D>/<STATE>/candidate_universe.json`
  - Output (predictive SSOT): `sharepacks/_predictive/<D>/<STATE>/play_card.json`
  - Strategies:
    - `play_box_first` (prefers full canonical closures)
    - `analysis_prefix` (strict ranked prefix)
  - Budgets are experiments, not “truth”:
    - B12 is intentionally strict and will miss cases that B24/B36 capture.
    - Doubles-heavy days can be especially budget-sensitive (see GOLD-0025 in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`).
- Grader: `scripts/tools/grade_play_card.py`
  - Output (RUNS only): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PLAY_CARD_GRADE.*`

---

## Research practice (how to use this doc)

- Use this as the “taxonomy” layer:
  - when you invent/rename a method, add it here,
  - map it to a Candidate Universe `method_id` + `transform_chain`.
- Keep analyzer changes frozen until the corpus is large enough to avoid overfitting.
