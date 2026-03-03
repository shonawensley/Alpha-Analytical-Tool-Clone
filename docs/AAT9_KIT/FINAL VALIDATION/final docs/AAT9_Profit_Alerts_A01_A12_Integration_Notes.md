# AAT9 Profit Alerts (A01–A12) — Integration Notes (Brain‑2 / Control Center)

Purpose: keep the A01–A12 “profitability trackers” implementation **practical, measurable, and drift‑proof** by treating them as **deterministic alert rows** (log/display first; no wagering engine).

SSOT evaluation docs (read these first):
- Evaluation charter (variants/decay semantics): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- Grading matrix (per‑AID “what is a hit”, candidate vs promoter): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`

## Mandatory source docs (inventory)

### Phase 1 (core spec + implementation guidance)
- [x] `tasks/12_trackers_advice.txt` (advisory notes; stresses “trackerize first”)
- [x] `tasks/12_TRACKERS_FEEDBACK.txt` (advisory notes; flags schema/path conflicts)
- [x] `docs/AAT9_KIT/FINAL VALIDATION/AAT9 Architecture and Master Validation Framework.md` (conceptual; treat as non‑SSOT)
- [x] `docs/AAT9_KIT/FINAL VALIDATION/12 PART PROFIT.md` (primary spec for A01–A12 rules + schema)
- [x] `docs/AAT9_KIT/FINAL VALIDATION/12 PART PROFIT PART 2.md` (deep dive build packs; notably A07 split/tilt)

### Phase 2 (Control Center + Final Validation wiring)
- [x] `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Workflow_Control_Center.md` (SSOT for Brain‑2 export + schema)
- [x] `docs/AAT9_KIT/FINAL VALIDATION/FINAL_VALIDATION_TEMPC.md` (template philosophy; not SSOT for code)
- [x] `docs/AAT9_KIT/FINAL VALIDATION/deepresearch_trackers.txt` (advisory; may contain speculation)
- [x] `docs/AAT9_KIT/FINAL VALIDATION/advice_trackers.txt` (implementation hints)
- [x] `docs/AAT9_KIT/FINAL VALIDATION/final docs/final_validation_control.md` (conceptual; treat as non‑SSOT)
- [x] `tasks/INSTALL_12TRACKERS.txt` (very long “plan”; treat as advisory unless corroborated by SSOT)

## Phase 1 takeaways (what’s “real” vs “advisory”)

### 1) The clearest SSOT spec is `12 PART PROFIT.md`

It explicitly defines:

- The existence of the 12 alerts: “The Twelve ‘Can’t Skip’ Alerts (A01..A12)”.
- A shared **alert row** contract (fields + strength + caps + decay + evidence JSON).
- Default caps/decay per alert (spend discipline).
- A recommended Control Center “Alerts panel” layout (rank by strength, then cheapest).
- Starter `config/alerts.yml` blocks per alert (intended to be tuneable without code).

### 2) Output contract conflict exists in the non‑SSOT notes

Two different “daily alerts output” paths appear across notes:

- `data/outputs/alerts/<STATE>/<YYYY-MM-DD>.csv` (explicitly present in `12 PART PROFIT.md`)
- `reports/control_center/daily_alerts/<DATE>/alerts.csv` (appears in `tasks/12_TRACKERS_FEEDBACK.txt`)

This must be resolved before coding so all writers/readers/UI/exporters agree.

**Important repo reality:** Control Center already has a frozen alert schema for snapshots:

- JSON schema: `reports/control_center/alert_schema.json` (required keys: `id`, `state`, `variant`, `date`, `hits`; optional `strength`, `status`, `evidence`; additional fields allowed).
- Snapshot runner: `scripts/tools/cc_sanity_snapshot.py` emits `reports/control_center/cc_snapshot_<ts>.{json,csv,md,...}` and validates alert rows via `scripts/checks/test_cc_snapshot_schema.py`.
- Sharepack‑aligned Brain‑2 export: `scripts/tools/export_control_center_sharepack.py --date <D>` writes frozen outputs under `sharepacks/<D>/control_center/`.

So the “profit alerts contract” should be aligned to the existing Control Center schema, even if the older Profit spec mentions a different on‑disk CSV location.

### 3) Practical v0 scope (strong consensus across docs)

Implement A01–A12 as:

- deterministic event detectors
- emitting rows to a stable schema
- displayed/aggregated in Control Center as alerts

Do **not** implement the advanced “profit manager / betting engine” yet.

## Extracted spec (quick reference)

### A01–A12 list (names as in `12 PART PROFIT.md`)

- A01 — Dual‑Tail Consensus + 3‑Value Support
- A02 — Single‑Tail Consensus + Doubles Bias
- A03 — Cross‑Variant Consensus (≥2 of Mid/Even/Comb)
- A04 — Set‑Persistence Carry (Set2→Set1) on a 3‑Value
- A05 — Horizontal Straight Drift (perm=1 across columns)
- A06 — Long‑String DR Survivor + 3‑Value
- A07 — Mirror Echo (last‑draw mirror in R2 tails); routes/splits overlays
- A08 — Remaining Pairs (BA 27–29) Full‑Foundation Box
- A09 — Top V‑TRAC Index Repeat Risk
- A10 — State‑Level Due‑Doubles (Top‑3)
- A11 — Hot‑Zone × Consensus Overlap
- A12 — Permutation Clamp (low order entropy across R‑rows)

### Shared alert row fields (from `12 PART PROFIT.md`)

`12 PART PROFIT.md` describes an alert row schema with fields including:

- `alert_id` (A01..A12)
- `state`
- contextual fields like `section`, `set`, `draw`, `col`, `canonical`
- `strength` (1..5)
- `suggested_kind` (BOX / STR8_8 / STR8_3 / STR8_4of8 / SKIP)
- `cap_lines`
- `decay_in_draws`
- `venue_default`
- `evidence_json` (compact JSON of the flags used)
- `created_at`

## Phase 2 (next) — what we still need to confirm

- Where profit alerts should live for **Final Validation** (sharepack‑aligned export vs live paths).
- How to surface them in Brain‑2 artifacts alongside existing exports (BA, due doubles, vtrac repeat watch).
- How Final Validation docs want us to validate “pipeline integrity vs tool outcome” for profit alerts.

## Proposed v0 contract (recommended)

For Master Validation / sharepack evaluation, treat profit alerts as **Brain‑2 frozen artifacts**:

- Compute from the frozen sharepack day folder (no live drift).
- Write under `sharepacks/<D>/control_center/` alongside existing Brain‑2 exports:
  - `profit_alerts.csv`
  - `profit_alerts.md`
  - `profit_compound_events.csv` (shadow-only derived triage; “watchlist co-fire environments”)
  - `profit_compound_events.md`
  - (optional) `profit_alerts.json` (machine‑readable list of rows)
- Keep Control Center’s existing snapshot schema stable (`reports/control_center/alert_schema.json`). Profit alerts do not need to change that schema; they can be exported as a separate board first, then (optionally) promoted into a unified alerts feed later.

Watchlist SSOT:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Compound_Events_Watchlist.md`

### Revamp v2 contract notes (important)

- For `Suggested=BOX` candidate/governor rows, exports are now strictly membership-based:
  - `Canonical` is the **sorted** 3-digit family label (e.g., `259`).
  - `ImpliedSet` is always exported as the explicit permutation list (so the evaluator never “derives perms”).
- A08 (promoter) rows now include base-candidate pointers in `Evidence` (so audits can see what it is promoting).
- A11 (governor) rows are always gradeable and include star fields in `Evidence` (e.g., `star_level`, `a11_star_score`).

## Using sharepacks to mine examples (high‑leverage)

One sharepack day folder is already a “mini corpus”: ~14 states × the same workflow surfaces.

Use that to:

- Find at least one **positive** and one **near‑miss negative** example for each A01–A12.
- Turn those into test fixtures / regression checks (so future changes don’t drift).
- Sanity‑check that alert rates are not “state‑specific weirdness” by looking across states on the same day, then confirm across multiple days to avoid overfitting.

## Regression guard (recommended)

After any Profit Alerts change, validate the sharepack contract:
```bash
python3 scripts/tools/validate_profit_alerts_contract.py --start <D1> --end <D2>
```

---

## Decisions / Contracts (SSOT — do not drift)

These rules must be treated as “workflow contract” so future context resets don’t re‑litigate semantics:

### 1) Outcomes vs lens

- **Only Midday/Evening are gradeable outcomes.**
- **Combined is an analytic lens**, not a third draw.

Canonical reference: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`

### 2) Decay windows are measured in draw-steps (not calendar days)

- Draw-step = one real outcome event (Midday or Evening) for the state.
- Midday alerts step through Midday only; Evening alerts step through Evening only.
- Combined alerts step through the real outcome sequence Midday→Evening→Midday… (two chances/day when present).
- Missing periods are **skipped** (do not consume a step); insufficient future results = **CENSORED** (unknown, not failure).

### 3) Evaluation is windowed-first (strict is diagnostic)

- Primary metric: hit within the row’s `DecayDraws`.
- Secondary diagnostics: hit within `7` and `14` draw-steps.
- Strict (D-only) is a diagnostic, not the primary scorecard.

### 4) Pick-3 canonical correctness

- Profit Alerts must only surface **Pick‑3 actionable** candidates:
  - `Canonical` must be 3-digit (boxed evaluation) or `-` when not applicable.
  - `orders_modal_value` (when used) must be a 3-digit literal.

The exporter filters out non-Pick‑3 Stable rows when building A05/A12 candidates.

### 5) Where evaluation artifacts live (sharepack-aligned)

For a given results date `D`:
```bash
python3 scripts/tools/evaluate_profit_alerts.py --date <D>
```

Outputs:
- `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- `sharepacks/<D>/control_center/profit_alerts_eval.md`
- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv` (deduped play‑sets; avoids double counting)
