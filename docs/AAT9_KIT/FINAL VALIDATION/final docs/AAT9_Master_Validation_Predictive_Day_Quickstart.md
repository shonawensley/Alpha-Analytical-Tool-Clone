# Master Validation — Predictive Day Quickstart (No Results Yet)

Purpose: run the “day build” workflow against a Pick3StatsC4 history workbook **without** having results/winners yet (i.e., how the system runs live), while still producing a **frozen snapshot** you can review/share later.

This produces a **predictive sharepack** under `sharepacks/_predictive/<D>/...` that contains:
- Brain‑1 per‑state artifacts (tables/json + Stable/DR/Hot Zones/VTRAC enhanced + Aux snapshot)
- Brain‑2 Control Center export (boards) using a **placeholder results file**
- arena-era board review outputs (overlay + scoreboard + shadow DPL + board bundle)
- translation sandbox seeds for later translator learning

It does **not** produce:
- Winners HTML/JSON (Part A)
- Profit Alerts evaluation (`profit_alerts_eval.*`) (requires future results files)
- VTRAC validation reports (requires winners lens)

Definitions:
- **H** = history workbook date
- **D** = “next day” results date (**D = H + 1 day**) (folder name under the predictive sharepacks root)

---

## 0) Safety preflight

From repo root:
```bash
pwd
git status -s
```

Important: this workflow **mutates live output folders** while it runs (tables/JSON + analyzer outputs), but it freezes everything into an isolated predictive sharepack root so the snapshot is drift‑proof.

---

## 1) Fast path vs deep path (choose one)

### Fast path (recommended; ~10–15 minutes)
Run the arena-era cadence wrapper end-to-end and write a runtime receipt under `RUNS_2/ANALYSIS_ARENA/`:
```bash
python3 scripts/tools/run_analysis_arena_cycle.py pre --history-date <H> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --top-n-stable 10 --write-audit-evidence --play-card-write-md --force
```

What you get:
- Predictive sharepack snapshot: `sharepacks/_predictive/<D>/...` (winners-free)
- Arena board-review receipt family: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/ANALYSIS_ARENA/`
- Control-arm outputs remain in the predictive sharepack as baseline comparison surfaces

Current arena-era companion references:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/PORTAL.md`

### Deep path (step-by-step; slower but flexible)
Follow sections 2–5 below if you want manual control (profiles, per-step runs, etc.).

## 2) Build the predictive pack (deep path; granular commands)

Recommended (analysis-arena cadence wrapper; logs a RUNS receipt and runs the whole pre-results chain):
```bash
python3 scripts/tools/run_analysis_arena_cycle.py pre --history-date <H> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --top-n-stable 10 --force
```

Optional: run multiple history days in one go (writes a range receipt; per-day receipts by default):
```bash
python3 scripts/tools/run_analysis_arena_cycle.py pre-range --start-history-date <H0> --end-history-date <H1> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --top-n-stable 10 --force
```

Run:
```bash
PYTHONPATH=.:src python3 scripts/tools/run_predictive_day.py --history-date <H>
```

Example:
```bash
PYTHONPATH=.:src python3 scripts/tools/run_predictive_day.py --history-date 2026-01-06
```

Output:
- `sharepacks/_predictive/<D>/`
- `sharepacks/_predictive/<D>/control_center/`
- `sharepacks/_predictive/<D>/results_placeholder.txt` (tab header only)

Notes:
- `run_predictive_day.py` freezes via `scripts/tools/freeze_sharepack_day.py` with `--skip-global-vtrac --skip-winners` to avoid copying winners-dependent artifacts into predictive packs (e.g., `validation_report.*` and the `winners/` lens when results already exist).
- Control Center export uses `--results-file sharepacks/_predictive/<D>/results_placeholder.txt` so the boards render without needing real winners.

---

## 3) Optional: subset states (faster)

```bash
PYTHONPATH=.:src python3 scripts/tools/run_predictive_day.py --history-date <H> --states Florida4 NewYork4
```

---

## 4) Generate gradeable predictions (Candidate Universe) + a predictive run report

Important current posture:
- the arena-era wrapper already runs:
  - board review
  - shadow DPL
  - Candidate Universe
  - Play Card
  - translation sandbox seed capture
- Candidate Universe and Play Card remain the current downstream **control arm**, not the definition of arena truth

After the predictive sharepack exists, generate the **Candidate Universe** (the explicit, gradeable “playset”):

```bash
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive
```

Notes:
- Candidate Universe is **profiled** (Profit Alerts quarantine is expressed via `--profile`).
- Default generation posture is `tool_only` (Profit Alerts excluded), so the default output is:
  - `sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only.json`
- The `mixed` profile (includes Profit Alerts) writes the unsuffixed file:
  - `sharepacks/_predictive/<D>/<STATE>/candidate_universe.json`

```bash
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --profile mixed
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --profile profit_only
```

Optional (experimental): enable due-doubles–seeded mirror-pair closure packs (mirror-double conversion):
```bash
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --mirror-pair-closure-due-doubles-pairs 2 --top-n-mirror-pair-closure-due-doubles 2
```

Optional: also write a small human-readable summary next to the JSON:
```bash
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --write-md
```

Optional (recommended for audit/debug): also write an “evidence view” next to Candidate Universe
(makes it explicit what came from tools/boards vs what is derived):
```bash
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --write-evidence
```

Optional: generate budgeted “Play Cards” (e.g., 12/24/36 combos) from Candidate Universe (what to play now):
```bash
python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --budgets 12,24,36
```

Optional: generate Play Cards for an ablation profile:
```bash
python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --profile mixed --budgets 12,24,36
```

Optional: also write a small human-readable Play Card summary next to the JSON:
```bash
python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --budgets 12,24,36 --write-md
```

Optional: create an arena-native per-state predictive run report (for human notes):

```bash
python3 scripts/tools/create_predictive_run_report.py --date <D> --state <STATE> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0
```
Default output:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/PREDICTIVE/<D>__<STATE>__PREDICTIVE__tool_only__arena_v0.md`

Optional: create an arena-native cross-state predictive portfolio triage report (fast “what to review/play” surface):

```bash
python3 scripts/tools/create_predictive_portfolio_report.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0
```
Default output:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/PREDICTIVE/<D>__PREDICTIVE_PORTFOLIO__tool_only__arena_v0.md`

Optional: portfolio report for an ablation profile:
```bash
python3 scripts/tools/create_predictive_portfolio_report.py --date <D> --sharepacks-root sharepacks/_predictive --profile mixed --experiment-tag arena_v0
```

---

## 5) How to “upgrade” a predictive pack once results exist

Once `data/results/<D>.txt` exists, run the normal full‑day workflow (Brain‑1 + winners lens + Brain‑2 + windowed Profit Alerts evaluation) using:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Build_Full_Day_Quickstart.md`

You can still keep the predictive pack as the “what we knew pre-results” snapshot for later comparison.

Recommended (v0.3 cadence wrapper; grades + rollups; writes only to RUNS):
```bash
python3 scripts/tools/run_v0_3_cycle.py post --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --runs-subdir V0_3 --rollup --force
```

Optional: grade a date range (writes a range receipt; per-day receipts by default). If you add `--windowed-auto`, it will only run N=5 grading when enough contiguous results files exist (avoids partial windows):
```bash
python3 scripts/tools/run_v0_3_cycle.py post-range --start-date <D0> --end-date <D1> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag arena_v0 --runs-subdir V0_3 --rollup --windowed-auto --force
```

Then grade Candidate Universe (writes only to RUNS; keeps predictive sharepacks immutable):

```bash
python3 scripts/tools/grade_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive
```

Optional: grade Candidate Universe for an ablation profile:
```bash
python3 scripts/tools/grade_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only
```

Grade Play Cards (writes only to RUNS):
```bash
python3 scripts/tools/grade_play_card.py --date <D> --sharepacks-root sharepacks/_predictive
```

Optional: grade Play Cards for an ablation profile:
```bash
python3 scripts/tools/grade_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only
```
