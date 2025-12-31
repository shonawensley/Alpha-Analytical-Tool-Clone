# Master Validation — Evaluate‑Only Quickstart (Sharepacks Already Built)

Purpose: let a brand‑new Codex/AI session with **zero context** pick an existing frozen day sharepack and produce **filled run reports** (the “template answers”) without rerunning pipelines or sharing hundreds of raw outputs.

Assumption: `sharepacks/<D>/` already exists and is treated as the immutable day snapshot.

Definitions:
- **D** = results/winners date (folder name under `sharepacks/`)
- **D‑1** = history workbook date that produced the tables/strings used to predict D

If you do **not** already have `sharepacks/<D>/`, stop and use:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Preflight.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`

---

## 0) Session safety (do this first)

From repo root:
```bash
pwd
git status -s
```

Hard rule for evaluate‑only mode:
- Do **not** run table rebuilds or analyzers (they mutate live outputs and can confuse you).
- Only read from `sharepacks/<D>/...` and write **derived summaries** into the same sharepack if needed (deterministic `summary.md` blocks).

---

## 1) Pick your target (D + state)

1) Choose the sharepack day folder (results date D), e.g.:
```bash
ls -la sharepacks/2025-06-21
```

2) Confirm day mapping is correct (it spells out D‑1 → D):
- `sharepacks/<D>/README.md`

3) Choose a tracked state folder (examples): `Connecticut4`, `Florida4`, `OntarioCanada4`, etc.

Tracked state list (SSOT for master validation): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`

---

## 2) Quick deterministic validations (no guessing)

These catch the common “it looks right but is misaligned” failures.

0) (Optional, recommended for confidence) Audit multiple sharepack days at once:
```bash
python3 scripts/tools/audit_sharepacks_corpus.py --dates 2025-06-21 2025-06-22 2025-06-23
# Writes a single report under: reports/audit/sharepacks_audit_<timestamp>.md
```

1) Global VTRAC aggregator feed exists and is non‑empty:
```bash
python3 scripts/tools/validate_vtrac_compact_report.py --date <D>
```

2) Tables ↔ Aux draws alignment for this state (sharepack mode; strict):
```bash
python3 scripts/tools/validate_tables_aux_alignment.py --date <D> --state <STATE> --strict
```

3) Tool winners sanity (sharepack mode):
```bash
PYTHONPATH=.:src python3 scripts/tools/validate_stable_winners.py --sharepack sharepacks/<D>/<STATE>/stable/<STATE>
PYTHONPATH=.:src python3 scripts/tools/validate_dr_winners.py --sharepack sharepacks/<D>/<STATE>/digit_reduction/<STATE>
python3 scripts/tools/validate_hot_zones_winners.py --sharepack sharepacks/<D>/<STATE>/hot_zones/<STATE>
```

Interpretation (important):
- **Pipeline / wiring failure (Fix‑Now):** missing required artifacts, or `validate_tables_aux_alignment.py` fails (world snapshot drift).
- **Tool outcome (record):** `validate_hot_zones_winners.py` can fail simply because Hot Zones didn’t isolate the winner (performance signal), even when the pipeline is fine.
- `validate_stable_winners.py` prints `NOTE` for “no exact hit”; it fails only on artifact mismatch.
- **Leading zeros / dtype inference:** treat Pick‑3 literals/triads/canonicals as 3‑digit strings; a naive CSV read can coerce `033 → 33` and create false “missing winner” alarms. Prefer the repo’s summarizers/validators.

If you hit a real Fix‑Now failure: stop and log it in
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/WORKFLOW_CHANGELOG.md`

---

## 2.5) Profit Alerts evaluation (Brain‑2 windowed scoring)

Profit Alerts A01–A12 live under the day sharepack Control Center export:
- `sharepacks/<D>/control_center/profit_alerts.csv`

Primary evaluation is **hit within DecayDraws draw-steps** (not “D-only”). Run:
- Contract: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`
- Per‑AID grading matrix (prevents “graded the wrong object”): `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Grading_Matrix.md`
```bash
python3 scripts/tools/evaluate_profit_alerts.py --date <D>
```

Outputs:
- `sharepacks/<D>/control_center/profit_alerts_eval.md`
- `sharepacks/<D>/control_center/profit_alerts_eval.csv`
- `sharepacks/<D>/control_center/profit_alerts_eval_merged.csv` (deduped play‑sets)

Notes:
- `profit_alerts_eval.csv` reports both the **variant-faithful** hit lens and an **any-outcome (cross-variant)** diagnostic lens (`hit_any_*`) so Midday alerts resolving on Evening (and vice versa) are explicitly counted.

If future `data/results/<D+k>.txt` files are not present yet, episodes will be marked `CENSORED` (unknown), not failed.

## 3) Ensure “paste‑ready” evidence blocks exist (summary.md)

Goal: the run report should contain compact evidence blocks so you don’t paste raw CSV/JSON.

If a `summary.md` is missing (or you want to refresh it), write it directly into the sharepack folder.

Stable (Part 2 evidence block):
```bash
python3 scripts/tools/stable_sharepack_summary.py \
  --sharepack sharepacks/<D>/<STATE>/stable/<STATE> \
  --md-out sharepacks/<D>/<STATE>/stable/<STATE>/summary.md \
  --json-out sharepacks/<D>/<STATE>/stable/<STATE>/summary.json
```

Digit Reduction:
```bash
python3 scripts/tools/dr_sharepack_summary.py \
  --sharepack sharepacks/<D>/<STATE>/digit_reduction/<STATE> \
  --md-out sharepacks/<D>/<STATE>/digit_reduction/<STATE>/summary.md \
  --json-out sharepacks/<D>/<STATE>/digit_reduction/<STATE>/summary.json
```

VTRAC:
```bash
python3 scripts/tools/vtrac_sharepack_summary.py \
  --sharepack sharepacks/<D>/<STATE>/vtrac/<STATE> \
  --md-out sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.md \
  --json-out sharepacks/<D>/<STATE>/vtrac/<STATE>/summary.json
```

Hot Zones:
```bash
python3 scripts/tools/hot_zones_sharepack_summary.py \
  --sharepack sharepacks/<D>/<STATE>/hot_zones/<STATE> \
  --md-out sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.md \
  --json-out sharepacks/<D>/<STATE>/hot_zones/<STATE>/summary.json
```

Aux (Part 3 evidence block; preferred history‑aligned):
```bash
python3 scripts/tools/aux_sharepack_summary.py \
  --date <D> \
  --state <STATE> \
  --excel data/history/Pick3StatsC4_<D-1>.xlsm
```

Notes:
- `aux_sharepack_summary.py` writes into:
  - `sharepacks/<D>/<STATE>/aux/<STATE>/summary.md`
  - `sharepacks/<D>/<STATE>/aux/<STATE>/summary.json`
- Use `--excel` when you have the D‑1 workbook so Aux snapshots cannot drift after workbook swaps.

---

## 4) Generate the per‑run report scaffold (this is what you fill/share)

Important ordering:
- Generate summaries first (Step 3), then generate the run report so it embeds them.

Command:
```bash
python3 scripts/tools/create_master_validation_run_report.py --date <D> --state <STATE>
```

Output (default):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/<D>__<STATE>.md`

If the file already exists, do **not** overwrite it (it contains answers).
- Either paste updated `summary.md` blocks manually, or write a new run report file using `--out`.

---

## 5) Fill the run report (how evidence blocks + questions fit together)

Key idea:
- The `summary.md` blocks are **evidence extraction** (facts, ranks, counts, file stamps).
- The questions in the run report are **analysis/synthesis** you still must answer.

Recommended fill order:
1) **Part A (environment lens):** open the winners HTML/JSON under `sharepacks/<D>/<STATE>/winners/<STATE>/` and answer the Part A prompts (no tool scores).
   - If the winners JSON is too large to paste/share, generate a digest: `python3 scripts/tools/winners_json_digest.py --winners-dir sharepacks/<D>/<STATE>/winners/<STATE>`
2) **Part 2 (tools):** for each tool, read the embedded summarizer block and answer Q1–Q10 using that evidence (cite ranks/why‑tags/coverage).
3) **Part 3 (Aux):** paste/verify the Aux summary block, then answer Q1–Q10 (variant convergence, doubles pressure, repeat watch, etc.).
4) **Part 4 (pack decision):** synthesize candidates + coverage mode (boxed vs VT‑boxed vs VT‑straight, etc.). Use `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD` for mapping.
5) **Part 5 (summary):** “what mattered”, misses/conflicts, Fix‑Now vs Fix‑Later.

Global memory (don’t lose insights):
- Append Fix‑Later items to: `docs/AAT9_KIT/FINAL VALIDATION/final docs/WORKFLOW_CHANGELOG.md`

---

## 6) Optional: Brain‑2 / Control Center review for the day (already frozen)

Day‑level Control Center export (Brain‑2):
- `sharepacks/<D>/control_center/`
  - Boards: `blackapple_alerts.*`, `due_doubles.*`, `vtrac_repeat_watch.*`, `profit_alerts.*`

If missing, regenerate (sharepack‑aligned; drift‑proof):
```bash
python3 scripts/tools/export_control_center_sharepack.py --date <D>
```
