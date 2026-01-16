# SUPERBRAIN v0 — Synthesis Sprint (Profit Alerts Ablation)

Purpose: pause new runs and extract “gold” from the existing corpus, while isolating whether **Profit Alerts** are helping or polluting by running a clean **ablation**.

Non‑negotiables:
- Do not change analyzers (Stable/DR/VTRAC/Hot Zones) or combined-table extraction/readers.
- Do not modify sharepacks/<D>/ SSOT during this sprint.
- Predictive packs remain winners‑free; grading writes only to RUNS.

---

## v0 Corpus Windows (frozen inputs)

These are the existing “range packs” that define our v0 analysis surface:

- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CORPUS_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CORPUS_SYNTHESIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CORPUS_SYNTHESIS.md`

Related Codex cross-day reviewers:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21_to_2025-06-23__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-12-30_to_2026-01-04__CODEX_DEEP_ANALYSIS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-05_to_2026-01-09__CODEX_DEEP_ANALYSIS.md`

Primary navigation:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/INDEX.md`

---

## Profit Alerts “Quarantine” (Ablation Profiles)

We do not delete Profit Alerts during synthesis. We measure them.

Profiles (CLI `--profile`):
- `tool_only` (default): excludes Profit Alerts packs from Candidate Universe and Play Cards.
- `mixed`: includes Profit Alerts packs + non-profit packs (explicit; use only for ablation comparison).
- `profit_only`: includes Profit Alerts packs only (no other packs; no derived combo packs).

File naming convention (inside sharepacks):
- Candidate Universe:
  - `candidate_universe.json` (mixed; legacy filename)
  - `candidate_universe__tool_only.json`
  - `candidate_universe__profit_only.json`
- Play Cards:
  - `play_card.json` (mixed; legacy filename)
  - `play_card__tool_only.json`
  - `play_card__profit_only.json`

Grade outputs (in RUNS):
- Candidate Universe:
  - `<D>__CANDIDATE_UNIVERSE_GRADE.csv` (mixed)
  - `<D>__CANDIDATE_UNIVERSE_GRADE__tool_only.csv`
  - `<D>__CANDIDATE_UNIVERSE_GRADE__profit_only.csv`
- Play Cards:
  - `<D>__PLAY_CARD_GRADE.csv` (mixed)
  - `<D>__PLAY_CARD_GRADE__tool_only.csv`
  - `<D>__PLAY_CARD_GRADE__profit_only.csv`

Rollups:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/candidate_universe_rollup__<profile>.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/play_card_rollup__<profile>.md`

---

## Commands (v0 predictive window: 2026‑01‑05 → 2026‑01‑09)

All commands run from repo root with `PYTHONPATH=.:src` exported.

Generate Candidate Universe + Play Cards (tool-only):
```bash
export PYTHONPATH=.:src
for D in 2026-01-05 2026-01-06 2026-01-07 2026-01-08 2026-01-09; do
  python3 scripts/tools/create_candidate_universe.py --date "$D" --sharepacks-root sharepacks/_predictive --profile tool_only
  python3 scripts/tools/create_play_card.py --date "$D" --sharepacks-root sharepacks/_predictive --profile tool_only
done
```

Grade tool-only (writes only to RUNS):
```bash
export PYTHONPATH=.:src
for D in 2026-01-05 2026-01-06 2026-01-07 2026-01-08 2026-01-09; do
  python3 scripts/tools/grade_candidate_universe.py --date "$D" --sharepacks-root sharepacks/_predictive --profile tool_only --force
  python3 scripts/tools/grade_play_card.py --date "$D" --sharepacks-root sharepacks/_predictive --profile tool_only --force
done
python3 scripts/tools/rollup_candidate_universe_corpus.py --profile tool_only
python3 scripts/tools/rollup_play_card_corpus.py --profile tool_only
```

Repeat with `--profile profit_only` to measure Profit Alerts alone.

Predictive portfolio (cross-state triage) is also profile-aware:
```bash
python3 scripts/tools/create_predictive_portfolio_report.py --date 2026-01-09 --sharepacks-root sharepacks/_predictive --profile tool_only
```

---

## Results Snapshot (v0 Jan window; 2026-01-05 → 2026-01-09)

These are empirical rollups from the v0 window (14 tracked states × 5 days × Midday/Evening).

Candidate Universe union hit rates:
- `mixed` (Profit Alerts included): Evening `hit_any=0.2174`, Midday `hit_any=0.2609` (`candidate_universe_rollup.md`)
- `tool_only` (Profit Alerts excluded): Evening `hit_any=0.2029`, Midday `hit_any=0.2609` (`candidate_universe_rollup__tool_only.md`)
- `profit_only` (Profit Alerts only): Evening `hit_any=0.0145`, Midday `hit_any=0.0145` (`candidate_universe_rollup__profit_only.md`)

Play Card hit rates (best strategy/budget per profile):
- `mixed`: Evening best `hit_any=0.0435`, Midday best `hit_any=0.0725` (`play_card_rollup.md`)
- `tool_only`: Evening best `hit_any=0.0435`, Midday best `hit_any=0.0725` (`play_card_rollup__tool_only.md`)
- `profit_only`: Evening best `hit_any=0.0145`, Midday best `hit_any=0.0145` (`play_card_rollup__profit_only.md`)

Interpretation (v0 only; do not overfit):
- Profit Alerts alone (`profit_only`) are extremely weak in this window.
- `tool_only` performs essentially the same as `mixed` for Play Cards, and only slightly lower for the Candidate Universe union.
- This supports “quarantine without deletion”: keep Profit Alerts available, but do not let them dominate selection until they prove incremental value on larger windows.
