# Positional Tracker / AUX CORE Research Log

Opened: 2026-07-28

Purpose: preserve the detailed evidence behind the dedicated Positional AUX CORE
block and any later system integration. This is a research and execution log,
not a production-scoring contract.

## Operating Boundaries

- Frozen draw snapshots are the only inputs to Positional report generation.
- Winners are joined after generation for reverse-engineering and harness grading.
- Exact, canonical-box, VTRAC-box, positional, pair, mirror, and contextual
  evidence remain separate.
- Existing Arena, Candidate Universe, Play Card, scoreboard, and runtime scoring
  are not modified during this research.
- Protected string-table extraction and readers are outside scope.
- An idea appearing in historical Positional notes is not treated as implemented
  until runtime code and an emitted artifact confirm it.

## Authority Inventory

### Historical design and implementation notes

- `tasks/POSITIONAL/positional_research.md`
- `tasks/POSITIONAL/positional_tool.md`
- `tasks/POSITIONAL/optimize_positionaltracker.md`
- `tasks/POSITIONAL/pos_5.txt`
- `tasks/POSITIONAL/position_5.txt`

`positional_research.md` and `positional_tool.md` are byte-identical. They are one
authority stream, not two independent confirmations.

### Native implementation

- `modules/module_d_auxiliary_tools/refactored/positional_tool.py`
- `src/core/aux_config.py`
- `tests/test_positional_shortlist.py`
- `tests/acceptance/test_positional_delaware.py`
- `tests/test_aux_validation.py`

### Export and downstream consumers

- `alpha_analytical/control_center/aux_validation.py`
- `scripts/tools/aux_sharepack_summary.py`
- `scripts/tools/aux_control_center_arena.py`
- `scripts/tools/build_aggregated_analysis_arena.py`
- `scripts/tools/create_candidate_universe.py`
- `scripts/tools/create_play_card.py`
- `scripts/tools/create_translation_sandbox_seed.py`
- Brain 2 / Shadow DPL / compact experimental route artifacts.

### Contracts

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-03-16__AUX_CONTROL_CENTER__ARENA_CONTRACT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md`

## Capability Status Matrix

| Capability | Designed | Native implementation | Sharepack export | Current downstream use |
|---|---|---|---|---|
| Top three digits per position and variant | Yes | Yes | Preserved in `positional_shortlist_report_v2`; legacy top-one field retained | Full grid preserved in Aux/Arena evidence; core synthesis remains bounded |
| Gap, percentile, lag, rank, component scores | Yes | Yes | Preserved in the v2 position grid | Available for review and future role-aware use; not added to generic scores |
| Hard-due position flags | Yes | Yes | Separate hard-due list | Context only |
| Same-position cross-variant consensus | Yes | Yes | Notes + aggregated tags | Indirect through candidate score/tags |
| Same-position mirror consensus | Yes | Yes | Notes + tags | Indirect |
| Double pressure / due-double bonus | Yes | Yes | Notes plus explicit input-availability receipt | Partial; due bonus remains inactive when the normal caller supplies no input |
| Adjacent-position swap / mirror-swap | Yes | Yes | Candidate tags only | Indirect |
| Repeat-endcap candidate construction | Yes | Yes | Source tag only | Candidate survives if selected |
| Lane-concordance construction | Yes | Yes | Source tag only | Candidate survives if selected |
| VTRAC index / family candidate boosts | Yes | Yes | Candidate identity and context availability are preserved; normal sharepack supplies neither optional boost input | Valid candidate VTRAC reaches Arena; optional boost path remains caller-controlled |
| Full candidate ranks, root, VTRAC, evidence | Yes | Yes | Preserved with state-level lineage in v2 | Available in Aux/Arena evidence; Candidate Universe still transforms it |
| State-level 16-line ordered shortlist | Yes | Yes | Preserved in native order; compatibility slice retained | Arena receives the full slate and retains a bounded top slice; Candidate Universe, Play Card, and Sandbox remain separate consumers |
| Exact-position winner grading | Historical research | Not a predictive runtime feature | No | Deep Review/harness responsibility |
| Front/back/endcap pair grading | Historical research | Not a formal runtime output | No | Deep Review/harness responsibility |
| Calibrated Positional contribution to final translation | Proposed | No | No | Deferred pending harness evidence |

## Confirmed Native Behavior

The Positional engine currently:

1. Builds Midday, Evening, and Combined newest-first position streams.
2. Ranks the top three due digits independently for P1, P2, and P3.
3. Computes gap, historical-gap percentile, lag weight, and source-native score
   components.
4. Adds same-variant mirror evidence.
5. Adds exact and mirror same-position consensus across variants.
6. Adds double pressure when a digit or mirror occupies multiple strong
   position/variant cells.
7. Adds adjacent-position swap or mirror-swap evidence.
8. Aggregates digits per position across variants.
9. Forms state-level cartesian, repeat-endcap, and lane-concordance candidate
   seeds.
10. Scores and limits the final ordered shortlist to 16 rows.
11. Can add due-double, VTRAC-index, and VTRAC-family context when callers
    explicitly supply those inputs.

Focused pre-harness test result: `16 passed, 13 deselected`.

## Confirmed Integration Gaps

### Gap P1: top-three grid compressed to top one

`aux_validation.positional_shortlist_report` loops over each position but exports
only `summary.top_digits[0]`. The full top-three position ladder remains in the
native object but is unavailable to frozen sharepack readers.

Impact:

- exact-position support cannot be reconstructed faithfully from the compact
  sharepack;
- rank-two and rank-three cross-variant evidence disappears;
- pair and permutation analysis loses the majority of its source grid.

### Gap P2: candidate evidence fields dropped

The compact candidate payload preserves only `combo`, `score`, `tags`, and
`source`. It drops:

- native rank tuple;
- digital root;
- VTRAC index;
- candidate-construction evidence.

Impact:

- downstream readers cannot explain why a candidate was built;
- VTRAC attribution must be recomputed from the literal;
- native candidate construction cannot be audited from the compact artifact.

### Gap P3: optional context inactive in normal sharepack generation

`aux_sharepack_summary.py` calls `positional_shortlist_report` without
`due_doubles_active`, `vtrac_hot_indices`, or `vtrac_hot_families`.

Impact:

- configured due-double and VTRAC boosts are not exercised in the normal frozen
  sharepack path;
- the Streamlit UI can produce a richer context-aware result than the sharepack;
- those two outputs must not be assumed equivalent.

### Gap P4: compact Arena VTRAC identity can become `-1`

`aux_control_center_arena.py` expects `vtrac_index` on compact candidate rows,
but the preceding sharepack serializer does not emit it.

Impact:

- Positional candidates can still add canonical support;
- Positional VTRAC support may be skipped or rendered as unavailable;
- this is an export/contract handoff defect, not a native analyzer defect.

### Gap P5: zero digit can be rendered as empty

The compact Arena projection uses an `or ""` conversion when rendering digits.
Integer zero is therefore susceptible to becoming an empty string.

Impact:

- zero-based positional pressure may be under-rendered;
- native calculations remain correct;
- downstream display/receipt parity requires explicit zero-safe serialization.

### Gap P6: Candidate Universe loses native scope and order

Candidate Universe:

- reads the Aux summary independently of Aggregated Arena;
- takes a bounded Positional candidate slice;
- labels it `variant=Unknown`;
- assigns `play_mode=STRAIGHT`;
- sorts and de-duplicates the literals.

Impact:

- Positional candidates do enter the realized control-arm branch;
- native rank order and M/E/C synthesis context are lost;
- Candidate Universe is not consuming a lossless Positional candidate object.

### Gap P7: Arena and Candidate Universe are parallel consumers

Aggregated Arena and Candidate Universe independently read Positional/Aux
surfaces. Candidate Universe does not consume the Aggregated Arena Positional
interpretation.

Impact:

- a Play Card Positional hit is control-arm realization, not proof that
  Aggregated Arena promoted Positional evidence;
- the Translation Sandbox is the later comparison join;
- review artifacts must keep branch identity explicit.

### Gap P8: rich position semantics do not drive core synthesis directly

Aggregated Arena consumes bounded Positional candidate/canonical evidence and
preserves selected context, but it does not independently reason over every
position cell, pair lane, mirror receipt, or candidate-construction component.

Impact:

- Positional is used, but not at full semantic depth;
- adding every native row as another vote would create duplication;
- role-aware synthesis must be learned through the harness before promotion.

## Export-Parity Repair Status

Implemented on 2026-07-28 as a bounded compatibility repair:

- `P1 REPAIRED`: `positional_shortlist_report_v2` preserves every native
  top-three row for P1/P2/P3 across Combined, Midday, and Evening while
  retaining the legacy top-one field.
- `P2 REPAIRED`: all native candidate rows retain rank, canonical identity,
  native rank tuple, digital root, VTRAC index, tags, construction evidence,
  source, and state-level lineage.
- `P3 OBSERVABILITY REPAIRED / ACTIVATION UNCHANGED`: the export now records
  whether due-double and VTRAC-hot inputs were supplied and whether any optional
  context was applied. Normal sharepack generation still supplies none of those
  inputs and therefore does not receive an unearned context boost.
- `P4 REPAIRED`: valid native candidate VTRAC indices survive into the Aux
  Control Center Arena projection instead of defaulting to `-1`.
- `P5 REPAIRED`: integer digit zero is serialized explicitly and survives the
  Arena projection.
- `P6 OPEN`: Candidate Universe still sorts/de-duplicates the bounded
  Positional pack and loses native scope/order.
- `P7 ARCHITECTURAL FACT`: Arena and Candidate Universe remain parallel
  consumers.
- `P8 OPEN BY DESIGN`: the richer rows are preserved for Deep Review and
  future role-aware synthesis; they do not become additional generic votes.

Compatibility and containment:

- legacy top-one rows are unchanged;
- legacy candidate combo, score, tags, source, order, and membership are
  unchanged;
- no Positional weight, shortlist construction rule, candidate count, Arena
  vote formula, Candidate Universe behavior, Play Card behavior, state ranking,
  or allocation policy changed.

## AUX CORE Design Interpretation

AUX CORE should become a concentrated evidence product with two synchronized
forms:

1. A human-readable block resource for Deep Review.
2. A machine-readable object retaining source semantics and provenance.

It should:

- preserve full per-variant source rankings;
- expose within-block cross-variant duplicates and VTRAC relationships;
- retain source-native scores without adding incompatible scales together;
- distinguish direct ordered support, canonical-box support, VTRAC territory,
  reinforcement, background context, and contradiction;
- support winner-aware reverse engineering while marking winner joins as
  post-result;
- support future harness tests and system integration without silently becoming
  a final prediction engine.

It should not:

- replace string-table truth;
- manufacture final combinations merely because evidence is available;
- grant multiple votes to permutations or repeated rows from one source;
- change Analysis Arena, Candidate Universe, Play Card, or allocation policy
  before cross-window evidence exists.

## Harness Contract

The Positional harness will use:

- Discovery: June 21-27, 2025.
- Calibration: December 30, 2025 through January 9, 2026.
- Calibration: January 15-22, 2026.
- Holdout: March 9-23, 2026.

The baseline is native all-variant Positional behavior from each frozen Aux draw
snapshot. The following diagnostic profiles are compared without production
promotion:

- no mirror;
- no cross-variant weighting;
- no double pressure;
- no swap;
- no repeat-endcap construction;
- no lane-concordance construction;
- target-variant-only construction;
- target-variant VTRAC context;
- target-variant due-double context.
- forced due-double sensitivity, explicitly marked as an always-on
  counterfactual rather than current trigger behavior.

Measurements remain separated into:

- exact ordered shortlist coverage;
- canonical-box shortlist coverage;
- boxed VTRAC shortlist coverage;
- target-variant exact-position support;
- all-variant same-position support;
- mirror and loose cross-position support;
- front, back, and endcap pair support;
- double-anchor support;
- candidate-width receipts at 3/6/8/10/12/16;
- draw-horizon decay through four result opportunities.

No ablation result is a new production weight. Discovery, calibration, and
holdout remain separately visible.

## Execution Log

### 2026-07-28 - Initial audit

- Confirmed repository root and native Blackapple import.
- Confirmed canonical Deep Example Review journal.
- Confirmed four frozen replay windows and 1,129 unique result events in their
  winner ledgers.
- Confirmed the native Positional implementation and existing tests.
- Confirmed the eight integration gaps documented above.
- Added a lossless read-only adapter and frozen replay harness under
  `scripts/tools/`.
- Runtime scoring and existing downstream consumers remain unchanged.

### 2026-07-28 - Full harness completion

- Focused adapter/harness tests: `4 passed`.
- Existing Positional regression/acceptance tests: `16 passed, 13 deselected`.
- Unique baseline events: `1,129`.
- Profiles: `11`.
- Profile-event rows: `12,419`.
- Decay rows: `2,155`.
- Decay rollup rows: `32`.
- Winner-ledger source rows retained as provenance counts: `35,431`.
- Pre-draw source rows: `28,590`.
- Post-result source rows: `6,841`.
- Skipped or errored events: `0`.
- All `12` manifest-tracked artifact hashes and sizes verified.
- Package artifact fingerprint:
  `2019ca4aa4010903de67f912ef0534ed5c8933e8a504bcc55a09fd3179b06421`.

Baseline width-16 coverage across all events:

- exact: `1.51%`;
- canonical: `6.11%`;
- boxed VTRAC: `34.01%`.

March holdout:

- exact: `2.17%`;
- canonical: `6.28%`;
- boxed VTRAC: `34.54%`;
- target-variant exact-position support: `0.913 / 3`;
- all-variant exact-position support: `1.874 / 3`;
- same-variant front/back/endcap pair support:
  `21.74% / 23.19% / 26.09%`;
- double/triple top-two anchor support: `77.61%`.

Sensitivity findings:

- Cross-variant evidence increased March VTRAC recall relative to the
  no-cross-variant profile, but its canonical effect was mixed.
- Target-variant-only construction lost substantial VTRAC recall.
- Mirror, swap, repeat-endcap, lane, and double-pressure effects were not
  directionally stable across all cohorts.
- The real `>=71` due-double trigger activated in `0 / 1,129` events. Its
  unchanged output is a no-eligible-case result.
- The forced due-double profile confirmed that the code path can alter ranking,
  but its cross-window effect was small and inconsistent.
- Frozen target-variant overdue-VTRAC context did not improve March VTRAC
  recall.
- No profile earns production promotion.

Connecticut4 Evening `091`:

- target-variant exact positions: `1 / 3`;
- all-variant same-position exact positions: `2 / 3`;
- all-variant same-position mirror positions: `1 / 3`;
- cross-variant front-pair position support: yes;
- exact/canonical/VTRAC shortlist match through width 16: no;
- role: `POSITIONAL_REINFORCEMENT`.

### 2026-07-28 - Bounded runtime export-parity repair

- Added the additive `positional_shortlist_report_v2` contract.
- Preserved the full 27-row M/E/C position grid, complete aggregated ladders,
  full ordered candidate slate, candidate VTRAC identity, construction
  evidence, lineage, and explicit optional-context receipts.
- Updated the Aux Control Center Arena projection to preserve those fields and
  serialize zero digits safely.
- Focused regression and acceptance suite: `28 passed`.
- Additional surrounding Aux/Positional suites: `17 passed`; one protected
  legacy bootstrap test remains blocked by its pre-existing unresolved
  top-level `vtrac_reference` import.
- Aggregated Analysis Arena integration test: `1 passed`.
- Frozen Connecticut4 March 9 replay was deterministic with SHA-256
  `f218d2c0e524e9fca94142d50a2d9d691444faf7db2060cf8dad3f2410f65652`.
- Archived and repaired legacy top-one rows matched exactly.
- All `16` archived candidate rows matched on combo, score, tags, source,
  order, and membership.
- Full replay exposed `3` rows in every position cell and preserved digit zero
  in two Evening rows.
- No optional context was silently activated.

### Completed artifacts

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/POSITIONAL_AUX_CORE_HARNESS_V1/START_HERE.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/POSITIONAL_AUX_CORE_HARNESS_V1/POSITIONAL_CONSUMER_CROSSWALK.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/POSITIONAL_AUX_CORE_HARNESS_V1/POSITIONAL_HARNESS_FINDINGS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/POSITIONAL_AUX_CORE_HARNESS_V1/POSITIONAL_AUX_CORE_BLOCK_PROPOSAL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/POSITIONAL_AUX_CORE_HARNESS_V1/POSITIONAL_FEATURE_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/POSITIONAL_AUX_CORE_HARNESS_V1/POSITIONAL_ABLATION_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/POSITIONAL_AUX_CORE_HARNESS_V1/POSITIONAL_ROLLUP.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/POSITIONAL_AUX_CORE_HARNESS_V1/POSITIONAL_DECAY_LEDGER.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/POSITIONAL_AUX_CORE_HARNESS_V1/POSITIONAL_DECAY_ROLLUP.csv`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/POSITIONAL_AUX_CORE_HARNESS_V1/EXAMPLE__2026-03-09__Connecticut4__Evening__091.json`
- `tasks/AUXILIARY_ANALYTICAL_BLOCKS_MOCK__CONNECTICUT4_091.md`, Block 9.

### Containment decision

The Positional block is approved as a Deep Review/AUX CORE evidence resource,
and the bounded export-parity portion is now implemented. The change preserves
native evidence in the normal Aux summary and Arena-facing object without
altering native calculation or selection behavior. No Arena vote formula,
Candidate Universe pack, Play Card strategy, score, state ranking, final
combination, or allocation change was made. Role-aware synthesis and all
promotion decisions remain separate future tasks.
