# DR Arena v1 - Parity Audit

Purpose: compare the first automated `DR Arena v1` outputs against the 11 fully reviewed DR super-harness cases before scaling into broader validation.

This is the first answer to:

- did the automated arena preserve the same evidence classes the manual harness identified?
- where is the arena already aligned?
- where is it still too weak or too broad?

Related:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_ARENA_V1__INTEGRATION_PLAN.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-13__DR_SUPER_HARNESS__SEED_FINDINGS__ROUND2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-13__DR_SUPER_HARNESS__BATCH2_FINDINGS.md`

---

## Scope

Cases audited:

1. `2026-01-09 / NewJersey4 / Evening / 028`
2. `2026-01-07 / Florida4 / Evening / 963`
3. `2026-01-08 / OntarioCanada4 / Evening / 498`
4. `2026-01-07 / Florida4 / Midday / 434`
5. `2026-01-02 / NorthCarolina4 / Midday / 033`
6. `2025-06-23 / NewYork4 / Midday / 638`
7. `2026-01-06 / NewJersey4 / Evening / 942`
8. `2026-01-09 / OntarioCanada4 / Evening / 104`
9. `2026-01-07 / Michigan4 / Evening / 616`
10. `2025-06-21 / Pennsylvania4 / Midday / 667`
11. `2026-01-08 / NewYork4 / Midday / 199`

Audit artifacts:
- predictive cases: `sharepacks/_predictive/<D>/<STATE>/analysis/dr_arena__tool_only__dr_arena_v1_parity.json`
- June historical cases:
  - `sharepacks/2025-06-23/NewYork4/analysis/dr_arena__historical__dr_arena_v1_parity.json`
  - `sharepacks/2025-06-21/Pennsylvania4/analysis/dr_arena__historical__dr_arena_v1_parity.json`

---

## Verdict Summary

The overall parity result is good enough to scale.

- `9/11` cases aligned well enough with the manual harness to treat the arena contract as basically correct.
- `2/11` cases exposed the same main weakness:
  - `dr_empty_lens` is too conservative and under-calls true negative-control / no-signal days.

That means:

- `DR Arena v1` is already useful.
- we should continue with broader validation before changing DR extraction.
- the first likely `v1.1` arena refinement is `dr_empty_lens`, not a weight retune or analyzer rewrite.

---

## Case-by-Case Read

| Case | Manual truth class | Arena parity | Most important note |
|---|---|---|---|
| `NJ 028` | trace strong / caller weak | `good` | Arena preserved strong trace, strong competing-literal pressure, and meaningful fourth-variable support. |
| `FL 963` | lane-only / VTRAC gateway | `good` | Arena preserved strong lane-only confidence and competing repeated-value pressure without pretending exact literal support was the main truth. |
| `ON 498` | empty-lens / negative control | `weak` | Arena did not mark the section as sparse enough; this is the clearest `dr_empty_lens` miss. |
| `FL 434` | doubles / repeated-value pressure | `good` | Arena preserved double pressure and fourth-variable support in the same kind of environment the harness called out. |
| `NC 033` | row-repeat / final-survival | `good` | Arena preserved row-repeat / final-survival as a distinct surface instead of burying it in top-candidate compression. |
| `NY 638` | buried-but-present / competing literal | `good` | Arena preserved the rival motif pressure instead of flattening everything into one “best pattern” answer. |
| `NJ 942` | lane-only / buried trace | `good` | Arena preserved the lane-first reality and did not force exact-literal support to be the only interpretation. |
| `ON 104` | buried-trace positive | `good` | Arena preserved the environment as active and distinct from the empty Ontario control. |
| `MI 616` | double-pressure + final-survival | `good` | Arena preserved both double pressure and strong row-repeat/final-survival pressure. |
| `PA 667` | doubles / repeated-value pressure | `good` | Arena preserved the same doubles-regime truth seen in the manual case and in later competition analysis. |
| `NY 199` | empty-lens / negative control | `weak` | Same weakness as `ON 498`: arena still emitted active surfaces when the harness judged the map to be a real control. |

---

## What matched well

### 1. DR trace vs caller compression

The arena is correctly preserving “winner environment exists even if caller surface routes elsewhere” cases.

Strong examples:
- `NJ 028`
- `NY 638`
- `NJ 942`
- `ON 104`

This is the biggest success of v1.

### 2. Lane-only / VTRAC-gateway truth

The arena is preserving family/lane structure as its own object instead of requiring literal caller success first.

Strong examples:
- `FL 963`
- `NJ 942`

This means the arena is already better aligned with DR’s real job than the old `top_candidates` surface.

### 3. Doubles / repeated-value pressure

The arena is preserving doubles and repeated-value environments in a way that agrees with the manual harness.

Strong examples:
- `FL 434`
- `MI 616`
- `PA 667`

That is important because doubles/mirror-doubles have repeatedly shown up as one of the system’s strongest predictive regimes.

### 4. Row-repeat / final-survival

The arena is also preserving a DR-specific “row-downward repeat / final survival” class.

Strong examples:
- `NC 033`
- `MI 616`

This is one of the most valuable things the harness clarified, and it survived the jump into structured output.

---

## What did not match well

### `dr_empty_lens`

This is the main weak surface right now.

The two clearest negative controls:
- `ON 498`
- `NY 199`

were still emitted as active, non-sparse sections by `DR Arena v1`.

That means v1 currently distinguishes:
- “active trace”
- “lane truth”
- “double pressure”
- “row-repeat / survival”

better than it distinguishes:
- “true no-signal environment”

This is not a reason to reject the arena.
It is a reason to refine the empty-control logic before using DR arena outputs too aggressively in downstream policy.

---

## Most likely reason the empty-lens surface is weak

Current v1 is too permissive because it treats any of these as sufficient to avoid sparse classification:

- non-empty trace families
- precluster ledger entries
- reveal ledger entries
- not-all-cold locations

The parity read suggests that this is not enough.

Likely fix direction:
- separate `active but low-trust` from `true positive`
- factor in stronger negative-control conditions like:
  - low items total
  - low reveal purity
  - weak current-band relevance
  - low lane confidence
  - weak final-survival
  - weak cross-method concentration

In other words:
- `dr_empty_lens` should become more discriminative
- not just less empty

---

## Parity conclusion

`DR Arena v1` passed the parity stage.

Why:
- it preserved the most important manual harness truths across the majority of cases
- it made the same evidence classes visible automatically
- it did not require DR extraction or caller changes to become useful

But it also gave us a clear next refinement target:

**the first likely arena-only calibration is `dr_empty_lens`, not DR weight retuning and not Analyzer V3.**

---

## Immediate implication for the next phase

This parity result supports the next workflow:

1. broaden the validation inventory,
2. keep DR extraction frozen,
3. use the larger batch to stress the arena surfaces at scale,
4. especially pressure-test:
   - `dr_empty_lens`
   - `dr_competing_literal_pressure`
   - `dr_double_pressure`
   - `dr_row_repeat_and_final_survival`

Only after that should we decide:
- whether the first consumer change is enough,
- whether `v1.1` arena calibration is needed first,
- or whether true `V2`/`V3` analyzer pressure has become strong enough.
