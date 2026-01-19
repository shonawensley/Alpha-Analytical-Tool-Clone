# SUPERBRAIN v0.2 — Defaults + Scoring (Tool‑First, Additive)

Purpose: lock the first “stable” defaults after the v0 synthesis sprint so:
- predictive runs are **tool-first by default** (Profit Alerts quarantined),
- selection surfaces are deterministic and explainable,
- we can resume new days without drifting into “vibes” or plan thrash.

Non‑negotiables (carry forward):
- Do not change analyzers (Stable/DR/VTRAC/HZ) or combined-table extraction/readers during v0.2.
- Predictive packs (`sharepacks/_predictive/<D>/`) must remain winners‑free.
- Grading writes only to RUNS (never into predictive sharepacks).

Read first:
- v0 sprint + ablation results: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__SYNTHESIS_SPRINT.md`
- Gold capture ledger: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- DR consumption decisions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__FEATURE_DECISIONS.md`
- Aux consumption decisions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_V0__FEATURE_DECISIONS.md`
- Stable consumption decisions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/STABLE_V0__FEATURE_DECISIONS.md`
- Hot Zones consumption decisions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_V0__FEATURE_DECISIONS.md`
- VTRAC consumption decisions: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/VTRAC_V0__FEATURE_DECISIONS.md`
- Aux badge-matrix audit/export: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/AUX_VTRAC_BADGE_MATRIX__AUDIT.md`

---

## 1) v0.2 defaults (what to run)

### 1.1 Predictive (“before”) snapshot build

From repo root:
```bash
export PYTHONPATH=.:src
python3 scripts/tools/run_predictive_day.py --history-date <H>
```

### 1.2 Candidate Universe (gradeable playset) — tool‑first baseline

Default posture:
- `--profile tool_only` (Profit Alerts excluded)
- `--top-n-dr 0` (DR “top candidates” demoted; see DR feature decisions)

```bash
python3 scripts/tools/create_candidate_universe.py \
  --date <D> \
  --sharepacks-root sharepacks/_predictive \
  --profile tool_only \
  --top-n-dr 0 \
  --force
```

Optional (research-only; not part of v0.2 defaults):
- Hot Zones index-closure pack (bounded BOX expansion from dominant Hot Zones index votes):
  - `--hot-zones-index-closure --hot-zones-index-closure-boxed-canonicals 2`
  - Current measured result in the Jan window shows no lift; keep it off unless you are explicitly experimenting:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/HOT_ZONES_INDEX_CLOSURE__EXPERIMENT__2026-01-05_to_2026-01-09.md`
- Digit Reduction envelope packs (bounded BOX packs from DR steps trace; v0.3 prework):
  - `--dr-envelope-boxed-canonicals 2`
  - Measured summary across v0 windows:
    - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_ENVELOPE_PACK__EXPERIMENT__TOP2.md`

### 1.3 Play Cards (budgeted cuts) — tool‑first baseline

```bash
python3 scripts/tools/create_play_card.py \
  --date <D> \
  --sharepacks-root sharepacks/_predictive \
  --profile tool_only \
  --force
```

### 1.4 Portfolio (cross‑state triage) — tool‑first ranking

```bash
python3 scripts/tools/create_predictive_portfolio_report.py \
  --date <D> \
  --sharepacks-root sharepacks/_predictive \
  --profile tool_only \
  --rank-by tool_first \
  --force
```

Optional (research-only): generate `mixed` and `profit_only` artifacts to keep the ablation honest.

---

## 2) v0.2 “state strength” scoring (what it means)

We do **not** claim this predicts hit rate. This is a deterministic triage score to decide:
- which states deserve deeper human review,
- where to spend budget/attention during competitions.

### 2.1 Primary metric: Candidate Universe convergence

The portfolio’s `CU top support` is the v0.2 convergence proxy:
- computed as the maximum number of packs that support the same canonical triad (`canonicals` vote per pack).
- shown as `N:AAA BBB ...` (up to 3 canonicals tied at the top).

Interpretation:
- higher support ⇒ more cross-method agreement.
- still not a “hit probability”, but it is the cleanest “superbrain-like” signal we can surface without tuning analyzers.

### 2.2 Secondary metric: Candidate Universe breadth

`CU union` is the total unique combos in the union.
- smaller union ⇒ tighter playset / less dispersion.

### 2.3 Tiebreakers

- `Due doubles (canonicals)` / `due_doubles_count` (compact closure opportunities)
- `CU packs` (more evidence sources present, but only as a weak tiebreaker)

### 2.4 Ranking rule (tool_first)

Current v0.2 portfolio sort order:
1) higher `CU top support` (descending)
2) smaller `CU union` (ascending)
3) higher `due_doubles_count` (descending)
4) higher `CU packs` (descending)

---

## 3) What is explicitly *not* in v0.2 scoring yet

- Profit Alerts are not used as default selection signal (they remain measurable via `--profile mixed/profit_only`).
- Aux boxed VTRAC badge-matrix density is not yet compounded into the score (export exists; mining it into “gold” is the next step).
- Any analyzer tuning (Stable/DR/VTRAC/HZ) is deferred until we have a larger graded corpus.
