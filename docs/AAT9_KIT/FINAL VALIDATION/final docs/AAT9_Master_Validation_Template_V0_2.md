# Master Validation Template — v0.2 Addendum (Training Loop → Selection Decisions)

Purpose: keep Master Validation aligned with the v0.2 “selection + measurement integrity” posture.

This addendum does **not** replace the existing template:
- SSOT template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

It adds a v0.2-oriented “what to link / what to extract” layer so the analysis feeds durable decisions instead of drifting into vibes.

---

## v0.2 mental model (do not blur these)

- Training loop = post-results (winner known):
  - Evidence snapshot: `sharepacks/<D>/<STATE>/...`
  - Human review + grading outputs: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/...`
- Deployment loop = pre-results (winner unknown):
  - Evidence snapshot: `sharepacks/_predictive/<D>/<STATE>/...` (winners-free)
  - Gradeable predictions: Candidate Universe + Play Cards (written inside predictive sharepacks)
  - Grading outputs written only to RUNS.

v0.2 rule:
- Do not “fix” analyzers during the synthesis loop. Convert learnings into bounded selection transforms + harnesses first.

---

## v0.2 additions to include in a run report (recommended)

### 1) Link the navigation SSOTs (so the report survives context resets)

In the per-day/state report, include links to:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`

### 2) Record “lane visibility” vs “playset coverage”

When summarizing tool outputs, keep these distinct:
- `box_hit` (winning canonical is visible somewhere) → conversion opportunity
- `hit_any` (winner is directly covered by the playable set) → selection/budget success

This prevents the common failure mode:
“We were on the right VTRAC index / canonical lane, but the play-card cut didn’t allocate coverage.”

### 3) Use the v0.2 evidence exports when debugging

Candidate Universe evidence view (explicit provenance):
- Written by: `scripts/tools/create_candidate_universe.py --write-evidence`
- Files: `candidate_universe_evidence__<profile>.{csv,md}`

Signals bundle (predictive-safe compact signals for later aggregation):
- Written by: `scripts/tools/create_candidate_universe.py --write-signals-bundle --experiment-tag <TAG>`
- File: `signals_bundle__<profile>__<TAG>.json`

### 4) When Aux is “right but not converting”, capture it explicitly

Aux pressure is an index/lane signal, not a straight caller. In v0.2 we keep it as:
- a measurable, predictive-safe harness output, and
- a candidate for future triage/budget policies.

Primary references:
- Badge pressure harness: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_BADGE_PRESSURE__HARNESS__2026-01-05_to_2026-01-09.md`
- Due Doubles parity audit: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DUE_DOUBLES__PARITY_AUDIT__2026-01-05_to_2026-01-09.md`
- Badge matrix export (late/super‑late combo badges + pair badges; RUNS-only):
  - `python3 scripts/tools/create_aux_vtrac_badge_matrix_report.py --date <D> [--sharepacks-root sharepacks/_predictive]`
  - Outputs: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__AUX_VTRAC_BADGE_MATRIX.{md,csv}`

---

## “Did we miss anything?” (fast answer)

- Coverage ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__COVERAGE_LEDGER.md`
- Portal link audit: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__PORTAL_LINK_AUDIT.md`
