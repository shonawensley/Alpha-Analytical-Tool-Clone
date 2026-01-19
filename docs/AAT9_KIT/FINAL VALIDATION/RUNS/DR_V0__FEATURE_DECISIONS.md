# Digit Reduction — v0 Feature Decisions (Inputs to v0.2)

Purpose: convert the DR v0 audit into explicit, **actionable consumption rules** for the superbrain layers (Candidate Universe / Play Cards), without touching analyzers yet.

This is the “keep/demote/remove-as-input” decision table.

Read first:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__DESIGN_INTENT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__QUANT.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__AUDIT__CASES.md`

Non‑negotiables:
- Analyzer logic stays frozen during v0 synthesis.
- Predictive packs stay winners‑free; evaluation-only artifacts must not become predictive inputs.

---

## Summary conclusion (v0)

In the v0 Jan window (`2026-01-05..2026-01-09`, `--profile tool_only`):

- `digit_reduction_analyzer_v2` as currently ingested (top‑N “best_pattern” straights) produced:
  - `hit_any=0/138` (no direct hits)
  - while case studies show DR overlays often contain the winner abundantly.

So the v0.2 posture is:
- DR is **valuable evidence**, but the current “top candidates” caller surface is not.

Additional measurement (cross-window; DR as envelope lens):
- DR envelope harness (from `*_digit_reduction_steps.csv`) shows DR has materially higher **`vtrac_index` gateway visibility** than tight canonical Top‑K visibility:
  - `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DR_V0__ENVELOPE_HARNESS__2026-01-05_to_2026-01-09.md` (and `.csv`)
- This reinforces the same conclusion: DR should be treated as an **envelope/constraint lens**, not as a standalone straight caller.

---

## Decision table (v0.2 consumption)

Legend:
- **Keep (predictive input)**: allowed to directly create packs / influence play cards.
- **Demote (support-only)**: allowed as evidence/boosts, but should not generate “top picks” by itself.
- **Eval-only**: keep only for post-results analysis/diagnostics; never use in predictive mode.

| DR output / signal | Current role | v0 evidence | v0.2 decision | Notes / implementation hook |
|---|---|---|---|---|
| `analyzer_v2_top_candidates.csv` (`best_pattern`) | Candidate Universe pack (`method_id=digit_reduction_analyzer_v2`, STRAIGHT, top‑N) | `hit_any=0/138` in v0 Jan window; repeated case pattern: winner often not present or very low rank | **Demote** | For v0.2 defaults, treat `--top-n-dr=0` in the tool-only baseline (still available for experiments by explicitly setting `--top-n-dr>0`). |
| `analyzer_v2_per_item.csv` (area_rank rows) | Not used as packs | Case audits show it tracks “where DR thinks structure is”, but not reliably “what wins” | **Demote** | Future: use as *evidence pointers* (e.g., early-arrival + persistence scoring), not as candidate list. |
| DR reducer reports + `*_digit_reduction_scores.csv` | Human evidence | Case audits suggest the winner is often visible in the reduction trace even when “top candidates” miss | **Keep (evidence), Demote (as picks)** | v0.3 candidate pack idea: extract digit pools/envelopes + persistence stats and feed bounded combination packs (not “top 3 best_pattern”). |
| DR training logs/steps (`*_steps.csv`, `*_logs.json`) | Human evidence | Useful for “did we reduce correctly?” and for studying early-arrival/persistence | **Keep (evidence)** | Reporting-only harness now uses `*_steps.csv` to grade “envelope” scoring (pre-work for DR‑004). Do not mine these into predictive packs until we define a deterministic “envelope extractor” (v0.3+). |
| Winner overlays/maps/flags/hits (`analyzer_v2/winners/*`) | Post-results evaluation | Critical for auditing DR behavior; must never become predictive input | **Eval-only** | Keep using in Master Validation + this audit; block in predictive packs. |
| `drop_*` and `family_*` flags | Embedded in DR outputs | Often high even when best_pattern misses; indicates DR is lane/structure heavy | **Demote** | Treat as “structure confidence” indicators for later weighting, not pick generation. |

---

## v0.2 “minimal-change” rule (recommended)

To avoid breaking anything while we learn:

1) Keep DR artifacts in sharepacks (no workflow change).
2) Keep DR outputs in Master Validation RUNS (no template change).
3) **Stop treating DR analyzer_v2 top candidates as default pick generators** in tool-only predictive mode:
   - Default: run Candidate Universe with `--profile tool_only --top-n-dr 0`
   - If you want to test DR as caller: explicitly raise `--top-n-dr` and compare grades.

This preserves your “additive, don’t delete evidence” principle while preventing DR’s weak caller surface from dominating selection.

---

## What this does *not* decide yet (defer)

- Any changes to the DR analyzer scoring/logic.
- Any “horizon” grading semantics (carryover scoring across days).
- Any changes to how DR computes its reduction traces.

Those are v0.3+ or “fix-later” items once v0.2 consumption defaults are stable.
