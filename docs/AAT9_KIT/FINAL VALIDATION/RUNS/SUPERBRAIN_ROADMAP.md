# SUPERBRAIN Roadmap (Macro Plan — v0 → v0.2 → v0.3)

Purpose: keep the project “followable” on a macro level (no spirals), even when context resets, by making the workflow, decision points, and artifacts explicit.

This roadmap is intentionally **procedural**: it tells you what to do next, what “done” means, and where each decision is recorded.

---

## 0) The system in 4 layers (so it stops feeling random)

1) **Evidence (immutable snapshots)**
- Predictive “before” snapshot (no winners): `sharepacks/_predictive/<D>/...`
- Post-results “after” snapshot (winners allowed): `sharepacks/<D>/...`

2) **Evaluation (reverse-engineer wins)**
- Master Validation per-state report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
- Day portals: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__WINNERS_DIGEST.md`, `.../<D>__DAY_SYNTHESIS.md`, `.../<D>__CONTROL_CENTER.md`

3) **Prediction surfaces (deterministic “superbrain v0”, not ML)**
- Candidate Universe (gradeable playset): `sharepacks/_predictive/<D>/<STATE>/candidate_universe{__profile}.json`
- Play Card (budgeted cut): `sharepacks/_predictive/<D>/<STATE>/play_card{__profile}.json`
- Portfolio (cross-state triage): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__PREDICTIVE_PORTFOLIO__tool_only.md`

4) **Change control (nothing gets lost)**
- Fix-now defects (pipeline correctness): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`
- Fix-later hypotheses (unproven ideas): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`
- “Gold” entries (repeatable, hit-linked, bounded actions): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
- v0.2 defaults (what the system does by default): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`

---

## 1) Key definitions (budget + profiles)

### 1.1 Profiles (Profit Alerts quarantine via ablation)

- `tool_only` (default posture): excludes Profit Alerts from Candidate Universe / Play Cards / grading / rollups / portfolio.
- `mixed`: includes Profit Alerts (explicit; use only for ablation comparison).
- `profit_only`: Profit Alerts only (measurement of incremental value).

Reference: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__SYNTHESIS_SPRINT.md`

### 1.2 Budget (“B12/B24/B36”)

Budget lives only in **Play Cards**, and it is measured in **combo lines** (3-digit straight lines), not “canonicals”.

- `B12` = 12 combo lines total
- `B24` = 24 combo lines total
- `B36` = 36 combo lines total

Important: competitions don’t “set” budget. Budget is an explicit CLI parameter and can be generated/graded for multiple budgets independently.

---

## 2) Where we are right now

- v0 corpus windows exist and are your stable “training” set:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CORPUS_SYNTHESIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_SYNTHESIS.md`
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_SYNTHESIS.md`
- Tool consumption audits exist (quant → cases → feature decisions) for DR/Aux/Stable/Hot Zones/VTRAC (see `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`).
- Profit Alerts are quarantined by default via `tool_only`.

Status handoffs (survive resets):
- `tasks/CODEX_HANDOFF__V0_SYNTHESIS_STATUS.md`
- `tasks/CODEX_HANDOFF__POWER_OFF.md`

---

## 3) Phase A — Close v0.2 (make it a reproducible baseline)

Goal: stop debating “what are we doing?” by locking the baseline knobs.

Decisions to lock (write into `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`):
- Default profile: `tool_only`
- Default DR consumption: `--top-n-dr 0`
- Default Play Card budget(s): pick one as the official baseline (recommendation: start with `B12` as the “tight budget” baseline and grade B24/B36 in parallel).
- Default Play Card strategy (recommendation: `play_box_first` unless evidence says otherwise).
- Primary metric to optimize first:
  - `hit_any` under budget (cost-controlled correctness), and/or
  - `box_hit` under budget (boxed-first focus),
  - track `vtrac_index_hit_only` as a “near miss” decomposition (do not optimize for it directly).

Definition of done:
- Baseline commands + defaults are explicit and agreed.
- Rollups exist for the baseline (`docs/.../RUNS/*rollup__tool_only.*`).

---

## 4) Phase B — Out-of-sample window (prove v0.2 isn’t storytelling)

Goal: run 3–5 new days **after** the v0 window using v0.2 defaults and grade them.

Workflow (per day):
1) Predictive BEFORE snapshot (winner-free):
   - `python3 scripts/tools/run_predictive_day.py --history-date <H>`
2) Generate predictive artifacts (tool_only baseline):
   - `python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --top-n-dr 0 --force`
   - `python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --force`
   - `python3 scripts/tools/create_predictive_portfolio_report.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --rank-by tool_first --force`
3) After results exist: build AFTER snapshot + Master Validation + grade:
   - Full-day build (see “Build Full Day” quickstart in final docs)
   - `python3 scripts/tools/grade_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --force`
   - `python3 scripts/tools/grade_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --force`
   - Rollups (tool_only)

Definition of done:
- The new window produces rollup deltas.
- Any new “gold” entries are written as **bounded actions** (selection-layer changes), not analyzer tuning.

---

## 5) Phase C — Selection-layer experiments (additive only)

Goal: add experiments that can be graded and rolled back safely (no analyzer edits).

Allowed experiments:
- Portfolio ranking changes (state triage only).
- New Play Card strategies/budgets (e.g., a conditional “conversion slot” only when evidence is strong).
- New candidate packs that are **read-only** derivations of existing evidence (bounded closure packs).

Rules:
- Every experiment must be:
  - named (strategy/method_id),
  - measurable (shows up in grade CSV columns),
  - logged (GOLD entry + Fix-Later if needed),
  - compared against the baseline via rollups.

---

## 6) Phase D — v0.3 Analyzer edits (real tool fixes, but evidence-gated)

Goal: fix true tool correctness issues and/or implement proven improvements.

We do not “never change tools”; we just avoid changing them while the selection layer is still unstable.

v0.3 entry criteria:
- The issue is either:
  - Fix-now correctness (broken output, schema/parsing issue, missing artifacts), or
  - A repeated, measured improvement hypothesis that survives out-of-sample testing.

Mechanism:
- Create a single backlog doc (“nothing gets missed”) listing each proposed analyzer edit with:
  - evidence links (RUNS + winners lens),
  - expected measurable impact,
  - regression plan (which windows must not regress),
  - status (proposed / approved / implemented / validated).

Until that backlog exists, don’t tune analyzers.

---

## 7) Where to start when you feel lost

1) `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
2) `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`
3) `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md`
4) `tasks/CODEX_HANDOFF__V0_SYNTHESIS_STATUS.md`

