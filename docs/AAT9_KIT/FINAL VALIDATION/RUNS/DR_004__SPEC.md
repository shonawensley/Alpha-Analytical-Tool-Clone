# Digit Reduction — DR‑004 Spec (Selection-Layer Transform)

Purpose: convert Digit Reduction (DR) **trace evidence** into **bounded, gradeable Candidate Universe packs** that behave like your real method:

- repeat/convergence across locations (boxes/sets/columns),
- early arrival + persistence in the reduction trace,
- cross‑variant convergence (Midday/Evening/Combined),
- optional VTRAC index compression (bounded),
- recent‑draw digit overlap used only as a **negative filter** (penalty; not a hard drop).

This is a **selection-layer** transform (Candidate Universe / Play Cards), not an analyzer-tuning proposal.

## Non‑negotiables

- **No winners leakage**: DR‑004 reads only predictive‑safe artifacts.
- **Deterministic**: same inputs → same outputs.
- **Bounded**: no uncontrolled pool widening; caps are explicit.
- **Additive + default‑off**: enabled only via explicit CLI flags; baseline files remain unchanged via `--experiment-tag`.

## Inputs (predictive-safe)

Per sharepack day + state:

- DR trace steps: `sharepacks/<root>/<D>/<STATE>/digit_reduction/<STATE>/training/<STATE>_digit_reduction_steps.csv`
- Sharepack-local draws snapshot (newest-first): `sharepacks/<root>/<D>/<STATE>/aux/draws/*_draws.csv`
  - Used only for **recency digit overlap penalty**.

No use of (evaluation-only):
- `.../digit_reduction/.../analyzer_v2/winners/*`
- `.../winners/<STATE>/*`

## Evidence model (what we score)

### A) Segment extraction (per “trace lane”)

For each outcome section (`Midday`, `Evening`, optionally `Combined`):

1) Group DR steps rows by a stable trace-lane key:
   - `location` + `method` + `mode` + `area` + `set` + `draw` + `col` (whatever is present in the steps CSV).
2) Sort by `step`.
3) Build **segments** where the digit pool (unique digits of `value`) is constant.
4) Keep only segments where `unique_digits <= 3` (triad-sized pools).

Each segment yields:
- `digits_set`: the unique digits (size 1–3)
- `start_step`, `end_step`, `span = end_step - start_step + 1`
- `first_3value_step` and `last_change_step` from the CSV (used as guardrails/diagnostics)

### B) Pool scoring (across lanes, then across variants)

Each `digits_set` accrues score from each segment using:

- **Early arrival**: earlier `start_step` is higher weight.
- **Persistence**: larger `span` increases weight.
- **Breadth / repeats**: more distinct trace lanes emitting the same `digits_set` increases weight.
- **Cross-variant convergence**:
  - reward pools present in both Midday and Evening;
  - treat Combined as a mild boost (never required).
- **Recency penalty** (optional): penalize pools whose digits appear heavily in the most recent draws (see below).

The output of this stage is a ranked list of `digits_set` pools with total support scores + diagnostics.

### C) Canonical expansion (bounded)

Each `digits_set` expands into boxed canonicals:

- size 3 digits → 1 single canonical + 6 double canonicals (bounded downstream)
- size 2 digits → 2 double canonicals
- size 1 digit → 1 triple canonical

Canonicals inherit pool score (with optional minor type weights):
- triples: smallest cost, but should not dominate unless heavily supported
- doubles: medium cost
- singles: highest cost

Final ranking is over **canonicals**.

## Optional VTRAC index compression (bounded)

For each canonical, compute `vtrac_index` via `modules.vtrac_reference.get_vtrac_index()` (triples return `None` by design).

Optionally:
- aggregate canonical support by index,
- pick top indices,
- within each index, keep only the top N canonicals.

This provides a “gateway lens” pack without widening into full `get_index_set(index)` (48/24/6 straight lines).

## Recent-draw digit penalty (negative filter; optional)

From sharepack-local draws CSV (newest-first):
- collect digits from the most recent `N` draws (default N small, e.g. 2–4)
- compute overlap count with `digits_set`
- apply a penalty proportional to overlap (never hard-drop)

Rationale: helps prefer **pending** digit pools without assuming repeats never happen.

## Outputs (Candidate Universe packs)

### Method + pack ids (proposal)

- `method_id`: `digit_reduction_dr004`
- Packs (play_mode `BOX`):
  - `digit_reduction_dr004:Midday:boxed_topK`
  - `digit_reduction_dr004:Evening:boxed_topK`
  - (optional) `digit_reduction_dr004:Combined:boxed_topK`
  - (optional) `digit_reduction_dr004:index_gateway_topK` (index-compressed canonicals)

### Boundedness knobs (proposal)

Primary:
- `--dr004-boxed-canonicals K` (default 0 = off)

Optional:
- `--dr004-index-boxed-canonicals K_idx` (default 0 = off)
- `--dr004-recent-draws N` (default 0 = disable recency penalty)
- `--dr004-max-cost-units C` (hard cap per pack; cost units = 6/3/1 per canonical boxed)

## Acceptance criteria (regression-gated)

Evaluate across the three frozen windows (tool_only profile):
- `2025-06-21→2025-06-23`
- `2025-12-30→2026-01-04`
- `2026-01-05→2026-01-09`

Primary gate (Candidate Universe union rows):
- Improve `hit_any` and/or `box_hit` versus baseline without unacceptable widening:
  - `avg union cost_units` must not increase beyond the cap you choose,
  - `vtrac_index_hit_only` must not spike (avoid “rail correct, box miss” inflation).

Secondary gate (Play Cards):
- `B12/B24` hit_any should not regress materially versus baseline; any lift is a bonus.

## Case validation queue (10 high-signal “buried-but-present”)

Use `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__STUDY_QUEUE.md` rows as the ground truth queue, and validate DR‑004 behavior using:

- Winners HTML: `sharepacks/<D>/<STATE>/winners/<STATE>/*.html`
- DR winner overlays: `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/winners/`
- Predictive trace inputs: `sharepacks/_predictive/<D>/<STATE>/digit_reduction/<STATE>/training/*_steps.csv`

Top 10 seed cases:

1) `2026-01-09` `OntarioCanada4` `Evening` (winner `104`)
2) `2026-01-08` `Florida4` `Midday` (winner `429`)
3) `2026-01-07` `Michigan4` `Evening` (winner `616`)
4) `2026-01-02` `NorthCarolina4` `Midday` (winner `033`)
5) `2025-12-31` `Delaware4` `Evening` (winner `337`)
6) `2025-06-21` `Pennsylvania4` `Midday` (winner `667`)
7) `2026-01-07` `Delaware4` `Evening` (winner `922`)
8) `2025-06-23` `Indiana4` `Midday` (winner `110`)
9) `2025-12-31` `Virginia4` `Midday` (winner `686`)
10) `2025-06-21` `OntarioCanada4` `Midday` (winner `678`)

## Execution (experiment-safe)

Use the experiment tag to avoid overwriting baseline artifacts:

- Candidate Universe: `python3 scripts/tools/create_candidate_universe.py --date <D> --profile tool_only --experiment-tag dr004_v1 ...`
- Grade CU: `python3 scripts/tools/grade_candidate_universe.py --date <D> --profile tool_only --experiment-tag dr004_v1 ...`
- Create Play Cards: `python3 scripts/tools/create_play_card.py --date <D> --profile tool_only --experiment-tag dr004_v1 ...`
- Grade Play Cards: `python3 scripts/tools/grade_play_card.py --date <D> --profile tool_only --experiment-tag dr004_v1 ...`
- Rollups:
  - `python3 scripts/tools/rollup_candidate_universe_corpus.py --profile tool_only --experiment-tag dr004_v1`
  - `python3 scripts/tools/rollup_play_card_corpus.py --profile tool_only --experiment-tag dr004_v1`

