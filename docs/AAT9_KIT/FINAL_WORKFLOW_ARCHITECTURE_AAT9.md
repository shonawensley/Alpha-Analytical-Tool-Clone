# FINAL WORKFLOW ARCHITECTURE — AAT9 (Live + Master Validation)

Purpose: give any new Codex session a single “source of truth” for **how AAT9 runs**, how **Master Validation** mirrors the live workflow, and where every critical artifact lives (so we don’t lose time on re-training after context resets).

Repo root (WSL): `/home/ser/code/Alpha-Analytical-Tool-Clone`

Core principles (SSOT):
- **Strings lead, Aux compounds.** String-table tools generate primary candidates; Aux adds *confirmation/gating* and cross-variant convergence.
- **Winners logging is post-results.** Brain outputs must not require knowing winners; grading happens later.
- **Sharepacks are immutable snapshots.** Anything you want to analyze/refer back to must be copied/stamped into `sharepacks/<DATE>/...`.
- **Date alignment matters.** Use the “day-ahead” rule to avoid leakage.
- **Snapshots must agree.** During Master Validation, Aux draw CSVs must be generated/snapshotted from the same history workbook (D‑1) used to build the string tables, otherwise Part 3 can drift.

---

## 0) The two timelines (why validation is “almost the real workflow”)

Definitions:
- **D** = results/winners date.
- **D‑1** = history workbook date (tables/strings built from draws up to the end of D‑1).

Live workflow (today → tomorrow):
- Today: build tables from today’s workbook snapshot
- Tomorrow: winners happen; log grading against yesterday’s predictions

Master Validation (backtest):
- Build tables from a historical workbook snapshot (D‑1)
- Grade against known historical winners (D)

ASCII map (universal viewer):

```
                 (history workbook)                (results/winners)
LIVE:        D (snapshot tables)  ─────────────>   D+1 winners
MASTER:      D-1 (snapshot tables) ────────────>   D winners

Tool brain outputs are produced at the left side.
Winners logging/grading happens only at the right side.
```

---

## 1) Single sources of truth (contracts table)

For operational detail, see: `docs/AAT9_KIT/AAT9_Final_Validation_Help.md`

| Concept | SSOT | Notes |
|---|---|---|
| Sharepack date folder | `sharepacks/<D>/...` | **D is the results/winners date**. |
| History workbook date | workbook selected for the run | Usually **D‑1** when validating sharepacks for D. |
| Winners input file | `data/results/<D>.txt` | Paste/maintain winners list for that results date. |
| String tables (CSV) | `data/outputs/tables/<STATE>/` or sharepack copy | Tools read these; rebuild when swapping workbook. |
| JSON tables | `data/outputs/json_tables/<STATE>_tables.json` or sharepack copy | Hot Zones + other tooling may use JSON. |
| Aux draw CSVs | `data/cleaned/draws/*_draws.csv` | **Aux/BA must read draw CSVs** (not string-table XLSX). |
| Aux draw snapshot (validation) | `sharepacks/<D>/<STATE>/aux/draws/` | For Master Validation Part 3, do not rely on live `data/cleaned/draws/` (it can drift after swaps). |
| Winners overlays (HTML/JSON lens) | `sharepacks/<D>/<STATE>/winners/<STATE>/` | This is Template Part 1 (environment lens). |
| Template answers (filled) | `tasks/FINAL VALIDATION/RUNS/<D>__<STATE>.md` | Don’t write answers into the template file. |

Canonicalization gotcha:
- Many tools work in **canonical** (sorted digits). Example: literal `517` → canonical `157`.
- Always map literal → canonical before filtering/analyzing tool outputs.

4 “hit criteria” (used everywhere):
- Exact straight hit
- Exact boxed hit
- VTRAC boxed hit (family/index)
- VTRAC straight hit (8-straight lane)

Reference decoder ring:
- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`

---

## 2) Directory map (where artifacts live)

### Live mutable outputs (changes when you rerun tools)
- Tables (CSV): `data/outputs/tables/<STATE>/`
- JSON tables: `data/outputs/json_tables/<STATE>_tables.json`
- Tool outputs (varies by tool; see lean outputs doc): `data/outputs/analysis/...` (or tool-specific folders)
- Aux draw CSVs: `data/cleaned/draws/*_draws.csv`

### Frozen analysis snapshots (sharepacks)

Sharepack root:
- `sharepacks/<D>/<STATE>/`

Typical per-state sharepack structure:
- Winners lens: `sharepacks/<D>/<STATE>/winners/<STATE>/`
- Tables snapshot: `sharepacks/<D>/<STATE>/tables/`
- JSON tables snapshot: `sharepacks/<D>/<STATE>/json/<STATE>_tables.json`
- Stable: `sharepacks/<D>/<STATE>/stable/<STATE>/`
- Digit Reduction: `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/`
- VTRAC Analyzer: `sharepacks/<D>/<STATE>/vtrac/<STATE>/`
- Hot Zones: `sharepacks/<D>/<STATE>/hot_zones/<STATE>/`
- Aux (Part 3):
  - Draw snapshot: `sharepacks/<D>/<STATE>/aux/draws/`
  - Aux summary: `sharepacks/<D>/<STATE>/aux/<STATE>/summary.md`

Validation narrative (the file you share across engines):
- `tasks/FINAL VALIDATION/RUNS/<D>__<STATE>.md`

---

## 3) Daily (live) workflow — conceptual

This is the “true final workflow” you’re ultimately building toward.

1) **Select workbook** (Pick3StatsC4 snapshot)
   - Input: `data/original/Pick3StatsC4.xlsm`
2) **Stage 1: rebuild datasets/tables**
   - Output: `data/outputs/tables/<STATE>/...` (3 variants)
   - Output: `data/outputs/json_tables/<STATE>_tables.json` (if enabled)
3) **Run string-table tools (brain outputs)**
   - Stable / Digit Reduction / VTRAC Analyzer / Hot Zones
4) **Run Aux (draw-driven signals)**
   - Positional pressure, repeat-watch, overdue doubles/pairs, sums, Blackapple, etc.
5) **Aggregator / Superbrain** (future)
   - Combine signals, apply gating, produce final candidate list (and play-mode guidance).
6) **End of day: enter winners**
   - Winners logging/grading against earlier brain outputs.
7) **Persist metrics**
   - Log what worked, what didn’t, and the environment traits (future ML optional).

---

## 4) Master Validation workflow — operational (how we run examples now)

Master validation is the same pipeline, but “winners are known”, so we can grade immediately.

Golden rule:
- Always keep D/D‑1 alignment clean and freeze artifacts into a sharepack so later sessions can re-analyze without reruns.

Recommended workflow helpers (no app required):
- Generate run report scaffold (Parts 1–3):  
  - `python3 scripts/tools/create_master_validation_run_report.py --date <D> --state <STATE> --out <FILE>`
- Generate Aux evidence dump (Part 3):  
  - Recommended (history-aligned): `python3 scripts/tools/aux_sharepack_summary.py --date <D> --state <STATE> --excel data/history/Pick3StatsC4_<HISTORY_D-1>.xlsm`
  - Fallback (copies current live `data/cleaned/draws`): `python3 scripts/tools/aux_sharepack_summary.py --date <D> --state <STATE>`

Part-by-part analysis flow:
- **Part 1 (environment lens)**: open winners HTML/JSON (3 variants) and answer Part A.
- **Part 2 (tools)**: paste `summary.md` from each tool (Stable/DR/VTRAC/Hot Zones) and answer Q1–Q10 + 2B synthesis.
- **Part 3 (aux)**: paste Aux `summary.md` and answer Part 3 Q1–Q10 (convergence + expense/mode).

Template file (questions only):
- `tasks/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`

Filled run report (answers live here):
- `tasks/FINAL VALIDATION/RUNS/<D>__<STATE>.md`

Workflow-level “fix later” log:
- `tasks/FINAL VALIDATION/WORKFLOW_CHANGELOG.md`

---

## 5) Tool contracts (brain vs winners) + helper scripts

Lean outputs reference:
- `docs/AAT9_KIT/AAT9_Analyzer_Lean_Outputs.md`

Entry + workflow guardrails:
- `docs/AAT9_KIT/AAT9_Final_Validation_Help.md`

Summarizers (produce paste-ready evidence blocks for Part 2):
- Stable: `python3 scripts/tools/stable_sharepack_summary.py --sharepack sharepacks/<D>/<STATE>/stable/<STATE> --md-out summary.md --json-out summary.json`
- Digit Reduction: `python3 scripts/tools/dr_sharepack_summary.py --sharepack sharepacks/<D>/<STATE>/digit_reduction/<STATE> --md-out summary.md --json-out summary.json`
- VTRAC: `python3 scripts/tools/vtrac_sharepack_summary.py --sharepack sharepacks/<D>/<STATE>/vtrac/<STATE> --md-out summary.md --json-out summary.json`
- Hot Zones: `python3 scripts/tools/hot_zones_sharepack_summary.py --sharepack sharepacks/<D>/<STATE>/hot_zones/<STATE> --md-out summary.md --json-out summary.json`
- Aux (Part 3):
  - Recommended (history-aligned): `python3 scripts/tools/aux_sharepack_summary.py --date <D> --state <STATE> --excel data/history/Pick3StatsC4_<HISTORY_D-1>.xlsm`
  - Fallback: `python3 scripts/tools/aux_sharepack_summary.py --date <D> --state <STATE>`

Validators (fail fast on common “wiring drift”):
- Tables naming: `PYTHONPATH=.:src python3 scripts/tools/validate_tables_naming.py --json-out tables_naming.json`
- Tables↔Aux alignment:
  - Live: `python3 scripts/tools/validate_tables_aux_alignment.py --state <STATE>`
  - Sharepack: `python3 scripts/tools/validate_tables_aux_alignment.py --date <D> --state <STATE> --strict`
- Stable winners present: `PYTHONPATH=.:src python3 scripts/tools/validate_stable_winners.py --sharepack sharepacks/<D>/<STATE>/stable/<STATE>`
- DR winners semantics: `PYTHONPATH=.:src python3 scripts/tools/validate_dr_winners.py --sharepack sharepacks/<D>/<STATE>/digit_reduction/<STATE>`
- Hot Zones winners: `python3 scripts/tools/validate_hot_zones_winners.py --sharepack sharepacks/<D>/<STATE>/hot_zones/<STATE>`
- VTRAC compact report non-empty: `python3 scripts/tools/validate_vtrac_compact_report.py --date <D>`

---

## 6) Known pitfalls / troubleshooting (high-value)

1) **Label mismatch** (Ontario examples)
- Results file may label a state differently than the state key.
- Fix: pass `--results-label` where supported (Stable runner); keep sharepack state folder consistent.

2) **Canonical vs literal mismatch**
- If a tool “missed”, first check whether it uses canonical digits (sorted).

3) **VTRAC compact report exists but empty**
- The file can exist but contain `states=[]` / `sections=[]`. Validate before relying on it.

4) **Aux drift after workbook swaps**
- Aux reads `data/cleaned/draws/` (mutable). Part 3 must snapshot draw CSVs into sharepack to be reproducible.
- For Master Validation, prefer generating the Aux snapshot from the history workbook (D‑1) so it matches the string-table snapshot:
  - `python3 scripts/tools/aux_sharepack_summary.py --date <D> --state <STATE> --excel data/history/Pick3StatsC4_<HISTORY_D-1>.xlsm`
- Quick verification pattern (no “trust me” required):
  - Compare Aux snapshot head (newest draws) vs the string tables’ `Set1,Draw1,draw_data` row (they should match per variant).

5) **Blocked / untracked states**
- Some states are known problematic (e.g., GA/TX) and can be skipped until fixed.

---

## 7) “Start here” quickstart (new session)

1) Read: `docs/AAT9_KIT/AAT9_Final_Validation_Help.md`
2) Read: `tasks/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`
3) Pick a sharepack run report: `tasks/FINAL VALIDATION/RUNS/<D>__<STATE>.md`
4) If Part 3 is missing: run Aux summary (prefer `--excel` if you have the D‑1 history workbook):
   - `python3 scripts/tools/aux_sharepack_summary.py --date <D> --state <STATE> --excel data/history/Pick3StatsC4_<HISTORY_D-1>.xlsm`
5) Continue the template (Parts 1–3), log “fix later” items to: `tasks/FINAL VALIDATION/WORKFLOW_CHANGELOG.md`

Note on Git:
- Codex should avoid git remote operations (push/pull/fetch). Use your manual GitHub Desktop workflow for checkpoints.
