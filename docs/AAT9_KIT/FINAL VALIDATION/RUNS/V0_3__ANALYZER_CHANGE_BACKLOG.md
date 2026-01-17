# v0.3 — Analyzer Change Backlog (Stable / Digit Reduction / Hot Zones / VTRAC)

Purpose: maintain a **single, deduped inventory** of proposed *analyzer* changes so we can go tool‑by‑tool later without losing anything or accidentally overfitting.

Key principle: **v0.2 is selection-layer only** (Candidate Universe / Play Cards / Portfolio defaults). v0.3 is where we consider **analyzer edits** (Stable/DR/HZ/VTRAC) *after* evidence is collected and gates are defined.

Read first (orientation + current defaults):
- RUNS portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- v0.2 defaults: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
- Gold ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- Fix-now vs fix-later: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`

Non‑negotiables:
- Predictive packs stay winners‑free: `sharepacks/_predictive/<D>/...`
- Post-results sharepacks stay immutable SSOT: `sharepacks/<D>/...`
- Any analyzer change must be **measured** (before/after) on the same windows and must not regress “positive controls”.

---

## Status taxonomy (keep it operational)

- **Proposed**: plausible improvement with evidence pointers; not yet reproduced as a measurable delta.
- **Needs Repro**: we suspect a correctness/scoring issue but need a minimal reproduction and acceptance test.
- **Ready**: narrow change + clear regression protocol + clear expected delta.
- **Implemented (Unvalidated)**: code changed, but not yet re-scored across windows.
- **Implemented (Validated)**: change improves metrics and passes non-regression.
- **Rejected / Deferred**: good idea but too costly/no lift, or moved to selection-layer instead.

---

## Regression protocol (what “prove it” means)

### Windows (baseline corpus)
- 3‑day: `2025-06-21 → 2025-06-23`
- 6‑day: `2025-12-30 → 2026-01-04`
- 5‑day (Jan): `2026-01-05 → 2026-01-09`

### Metrics (selection-layer scoreboard; do not invent new ones mid-test)
- Candidate Universe grades: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__CANDIDATE_UNIVERSE_GRADE__tool_only.{md,csv}`
- Play Card grades: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PLAY_CARD_GRADE__tool_only.{md,csv}`
- Rollups: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__tool_only.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__tool_only.md`

### Guardrails (avoid “moving the goalposts”)
- If a change targets “index_hit → box_hit conversion”, measure `vtrac_index_hit_only` reduction without reducing `box_hit`.
- If a change increases candidate pool size/cost, record that explicitly; do not treat “hit_any up because we went wider” as a win.

---

## Coverage + traceability rules (so nothing gets missed)

This backlog is intentionally **bounded**: we do not reread 70+ state templates to “hunt ideas.” We treat the following as the canonical, high-signal extraction surfaces and require explicit traceability.

### Sources scanned (authoritative → supplementary)

Authoritative (RUNS / SSOT conclusions):
- Fix-now defects: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`
- Fix-later hypotheses: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
- Tool audits (quant → cases → feature decisions):
  - Stable: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__QUANT.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__CASES.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__FEATURE_DECISIONS.md`
  - Digit Reduction: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__QUANT.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__CASES.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`
  - Hot Zones: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__QUANT.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__AUDIT__CASES.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__FEATURE_DECISIONS.md`
  - VTRAC: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__QUANT.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__AUDIT__CASES.md`, `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__FEATURE_DECISIONS.md`
- Gold ledger (selection-layer actions; only feeds v0.3 if it implies a true analyzer edit): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`

Supplementary (design intent / historical tuning notes; never authoritative alone):
- Stable: `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md`
- Digit Reduction: `docs/AAT9_KIT/AAT9_Digit_Analysis_Log.md`, `docs/AAT9_KIT/AAT9_Digit_Analysis_Log_Part2.md`
- Hot Zones: `docs/AAT9_KIT/AAT9_Hot_Zones_Validation_Log.md`
- VTRAC: `docs/AAT9_KIT/AAT9_VTRAC_Analyzer_Analysis_Log.md`
- DR intent notes: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__DESIGN_INTENT.md` + supporting `tasks/*` notes when needed

### Item inclusion rule (strict)

Every backlog item MUST include at least one “evidence pointer” to one of:
- a Fix‑Now ledger row,
- a Fix‑Later index entry,
- a tool audit case row (from `*_V0__AUDIT__CASES.md`),
- or a specific Master Validation state report that contains a concrete “tool should change” note.

If an item only exists in a historical/self-optimization log:
- Keep it, but set status to **Needs Repro**, and add a “Repro plan” that points to which RUNS window/date/state will be used to validate it.

### Non-goals (keep us sane)

- Do not treat “ideas inside state templates” as analyzer edits by default. Most of those are **selection-layer** and belong in v0.2 (Gold + Defaults).
- Do not add Profit Alerts-driven changes here. Profit Alerts are quarantined by default and evaluated only via ablation profiles.

---

## Cross-cutting correctness gates (pre-reqs for safe tuning)

### X-001 — Canonicalization & dtype invariants (Pick-3 as strings)
- **Type**: correctness gate
- **Why**: leading zeros and literal↔canonical mapping errors can look like “tool misses”.
- **Evidence**: Master Validation template warnings about dtype/leading zeros (embedded in multiple RUNS state reports); fix-now history includes parsing fixes: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`
- **Expected delta**: fewer false “winner missing” alarms; more trustworthy grading.
- **Status**: Proposed (as a formal gate; many parts already exist informally)

### X-002 — Traceability contract (row→table coordinate always present)
- **Type**: correctness gate
- **Why**: without section/set/draw/col/method/mode, we can’t audit “how it should have scored”.
- **Evidence**: tool logs emphasize traceability (e.g., DR/HZ logs); Master Validation Part-2 structure depends on it.
- **Expected delta**: reduced audit time; fewer “mystery rows”.
- **Status**: Proposed

---

## Stable (String Tables) — analyzer backlog

Primary references:
- `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__AUDIT__QUANT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__FEATURE_DECISIONS.md`

### STABLE-001 — Preserve literal permutations + exact-hit flags in spotlight/export
- **Type**: output/schema improvement (supports evaluation + future training)
- **Problem**: evaluation can lose literal winners when only the canonical is logged (e.g., “858 vs 588”).
- **Evidence**: `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md` (spotlight should include raw rows + exact flags; literal winners in CSV outputs)
- **Expected measurable delta**: none directly (selection unaffected), but major reduction in audit ambiguity and better feature learning later.
- **Status**: Proposed

### STABLE-002 — Reconcile draw-chain / persistence metrics with compound aggregation
- **Type**: scoring correctness / feature plumbing
- **Problem**: compound rollup can collapse row-level chain signals, weakening Set1 col3→col2 cascades.
- **Evidence**: `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md` (compound writer collapses draw chain; reconcile row-level chain metrics)
- **Expected delta**: improved ranking for “column-cascade” winners without broad cost expansion.
- **Status**: Proposed (Needs Repro on a small set of cases)

### STABLE-003 — Increase “VT-straight mid-column” contribution (cols 3–5)
- **Type**: scoring/weights
- **Problem**: VT-heavy winners can appear outside col1/2 but receive minimal compound credit.
- **Evidence**: `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md` (“VT-lane weighting outside column 1”; Ontario/Florida examples)
- **Expected delta**: more stable_top/cross-tool convergence in VT-heavy environments; must not swamp col1 signals.
- **Status**: Proposed

### STABLE-004 — Hidden3v (“stealth core”) scoring lift (bounded)
- **Type**: scoring/weights
- **Problem**: hidden-core wins can be visible but under-ranked.
- **Evidence**: `docs/AAT9_KIT/AAT9_Stable_Analysis_Log.md` (hidden3v wins; consider bump)
- **Expected delta**: improved ranking of stealth wins with minimal widening.
- **Status**: Proposed

---

## Digit Reduction — analyzer backlog

Primary references:
- `docs/AAT9_KIT/AAT9_Digit_Analysis_Log.md`
- `docs/AAT9_KIT/AAT9_Digit_Analysis_Log_Part2.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__DESIGN_INTENT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`

### DR-001 — Persist/earliest-step features must materially influence ranking
- **Type**: scoring/feature weighting
- **Problem**: many wins are abundant in the trace/HTML but rank very low; persistence/early-arrival not rewarded enough.
- **Evidence**: repeated notes in `docs/AAT9_KIT/AAT9_Digit_Analysis_Log.md` (“persistence/earliest metrics need more weight”; LS2-only wins buried)
- **Expected delta**: DR surface becomes a better corroborator/caller *without* increasing candidate count.
- **Status**: Needs Repro (define 10–20 “buried but present” cases + acceptance threshold)

### DR-002 — LS2-only wins: compute & reward LS2 stability correctly (no hard-coding LS2 everywhere)
- **Type**: correctness + weights
- **Problem**: LS2-only environments can be missed; but LS2 should stay modest where inactive.
- **Evidence**: `docs/AAT9_KIT/AAT9_Digit_Analysis_Log.md` (LS2-only wins; “stability metrics computed before scoring”); `docs/AAT9_KIT/AAT9_Digit_Analysis_Log_Part2.md` (do not force LS2 everywhere)
- **Expected delta**: LS2 environments lift; non-LS2 days do not regress.
- **Status**: Proposed

### DR-003 — Expand deterministic DR coverage to adjacent columns (2/4) where repeatedly active
- **Type**: feature expansion (candidate space changes)
- **Problem**: repeated evidence that cols 2/4 host “lead-in” triads not currently assigned.
- **Evidence**: `docs/AAT9_KIT/AAT9_Digit_Analysis_Log.md` (multiple states note columns 2/4 glow repeatedly; “plan to expand DR coverage”)
- **Expected delta**: higher trace coverage; risk: candidate pool explosion → must be gated/bounded.
- **Status**: Proposed (requires strict bounding policy)

### DR-004 — Formal “digit-pool / envelope extractor” (DR as envelope lens, not top-3 caller)
- **Type**: new deterministic transform
- **Problem**: “best_pattern top candidates” is a weak caller; DR’s value is in digit pools + convergence.
- **Evidence**: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__DESIGN_INTENT.md`; `tasks/REDUCTION_THOUGHTS.txt` (digit pools, repetition, cross-variant convergence)
- **Expected delta**: DR becomes useful input for bounded combination packs (measurable via CU/PlayCard).
- **Status**: Proposed (v0.3 feature; careful anti-leakage)

---

## Hot Zones — analyzer backlog

Primary references:
- `docs/AAT9_KIT/AAT9_Hot_Zones_Validation_Log.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__FEATURE_DECISIONS.md`

### HOTZ-001 — Guard/selective injection policy (avoid noisy pools; keep literal winners in top ranks)
- **Type**: candidate pool control + scoring
- **Problem**: broad guards can bloat pools so winners land rank 40–50 and disappear from top maps.
- **Evidence**: `docs/AAT9_KIT/AAT9_Hot_Zones_Validation_Log.md` (guard too broad; “stop weight fiddling until guard is selective”; “design Set1 column guard”)
- **Expected delta**: preserve EB/VB coverage while keeping pool size bounded; improve top‑20 visibility.
- **Status**: Needs Repro (define narrow guard and verify across a small window)

### HOTZ-002 — Deterministic tie-break using guard/literal signals
- **Type**: scoring determinism
- **Problem**: tie-heavy scores make weight tweaks unstable; tie-break should use guard_hits/literal_hits.
- **Evidence**: `docs/AAT9_KIT/AAT9_Hot_Zones_Validation_Log.md` (sort by -score_max, -guard_hits, -literal_hits, -score_mean)
- **Expected delta**: stable ranks across runs; less temptation to over-tune weights.
- **Status**: Proposed

### HOTZ-003 — VT-only lane weighting calibration (bounded)
- **Type**: weights
- **Problem**: VB-only group suggests VT-only lanes need more weight, but must avoid regressions.
- **Evidence**: `docs/AAT9_KIT/AAT9_Hot_Zones_Validation_Log.md` (VB-only list; tune w_vt_only_lane, rebalance w_col1_arrival)
- **Expected delta**: more VT-heavy winners rise into top lanes without broad pool inflation.
- **Status**: Proposed

---

## VTRAC Enhanced — analyzer backlog

Primary references:
- `docs/AAT9_KIT/AAT9_VTRAC_Analyzer_Analysis_Log.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__FEATURE_DECISIONS.md`

### VTRAC-001 — Cross-variant echo + persistence weighting (superhot repeats)
- **Type**: weights
- **Problem**: cross-variant superhot repeats and right-column persistence are repeatedly cited as underweighted.
- **Evidence**: `docs/AAT9_KIT/AAT9_VTRAC_Analyzer_Analysis_Log.md` (action items across many entries)
- **Expected delta**: better ranking of “environment-correct” lanes; must not overfit overlap gates.
- **Status**: Proposed

### VTRAC-002 — Lane bump for repeats into Set1 col1/2 (ordered repeats)
- **Type**: weights/feature emphasis
- **Problem**: repeats landing in Set1 col1/2 are high-signal but not always lifted.
- **Evidence**: `docs/AAT9_KIT/AAT9_VTRAC_Analyzer_Analysis_Log.md` (lane bump for repeats into Set1 col1; ordered repeats)
- **Expected delta**: better “caller” behavior in strong ladder environments.
- **Status**: Proposed

### VTRAC-003 — Overlap gate review (avoid suppressing strong stability runs)
- **Type**: correctness/weights
- **Problem**: overlap=0 can suppress otherwise strong evidence; needs careful handling.
- **Evidence**: `docs/AAT9_KIT/AAT9_VTRAC_Analyzer_Analysis_Log.md` (increase weight even when overlap=0; check overlap gate)
- **Expected delta**: fewer false negatives in stability-heavy environments.
- **Status**: Needs Repro

---

## Notes (what is *not* in this backlog)

- Selection-layer rules (Candidate Universe / Play Cards / Portfolio) live in:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
- Profit Alerts quarantine/removal is handled via profiles/ablation and is not an analyzer edit.
