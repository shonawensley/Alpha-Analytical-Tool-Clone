# Master Validation — Predictive Day Quickstart (No Results Yet)

Purpose: run the “day build” workflow against a Pick3StatsC4 history workbook **without** having results/winners yet (i.e., how the system runs live), while still producing a **frozen snapshot** you can review/share later.

This produces a **predictive sharepack** under `sharepacks/_predictive/<D>/...` that contains:
- Brain‑1 per‑state artifacts (tables/json + Stable/DR/Hot Zones/VTRAC enhanced + Aux snapshot)
- Brain‑2 Control Center export (boards) using a **placeholder results file**

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

## 1) Build the predictive pack (one command)

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

## 2) Optional: subset states (faster)

```bash
PYTHONPATH=.:src python3 scripts/tools/run_predictive_day.py --history-date <H> --states Florida4 NewYork4
```

---

## 3) Generate gradeable predictions (Candidate Universe) + a predictive run report

After the predictive sharepack exists, generate the **Candidate Universe** (the explicit, gradeable “playset”):

```bash
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive
```

Optional: Profit Alerts quarantine (ablation profiles; additive, does not delete anything):
- `mixed` (default): current behavior (includes Profit Alerts packs)
- `tool_only`: excludes Profit Alerts packs
- `profit_only`: Profit Alerts packs only

```bash
python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only
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

Optional: generate budgeted “Play Cards” (e.g., 12/24/36 combos) from Candidate Universe (what to play now):
```bash
python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --budgets 12,24,36
```

Optional: generate Play Cards for an ablation profile:
```bash
python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --budgets 12,24,36
```

Optional: also write a small human-readable Play Card summary next to the JSON:
```bash
python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --budgets 12,24,36 --write-md
```

Optional: create a per-state predictive run report scaffold (for human notes):

```bash
python3 scripts/tools/create_predictive_run_report.py --date <D> --state <STATE> --sharepacks-root sharepacks/_predictive
```

Optional: create a cross-state predictive portfolio triage report (fast “what to review/play” surface):

```bash
python3 scripts/tools/create_predictive_portfolio_report.py --date <D> --sharepacks-root sharepacks/_predictive
```

Optional: portfolio report for an ablation profile:
```bash
python3 scripts/tools/create_predictive_portfolio_report.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only
```

---

## 4) How to “upgrade” a predictive pack once results exist

Once `data/results/<D>.txt` exists, run the normal full‑day workflow (Brain‑1 + winners lens + Brain‑2 + windowed Profit Alerts evaluation) using:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Build_Full_Day_Quickstart.md`

You can still keep the predictive pack as the “what we knew pre-results” snapshot for later comparison.

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
