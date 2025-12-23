# Master Validation — Build + Freeze Full‑Day Sharepacks (From Scratch)

Purpose: let a brand‑new Codex/AI session (zero context) take a **specific Pick3StatsC4 history workbook** and produce a **drift‑proof full day snapshot**:
- Brain‑1 per‑state sharepacks under `sharepacks/<D>/<STATE>/...`
- Brain‑2 Control Center export under `sharepacks/<D>/control_center/`
- Optional: run‑report scaffolds under `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`

Use this when you want to “set up the day” for later template filling.

If `sharepacks/<D>/` already exists and you only want to fill templates, use:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Evaluate_Only_Quickstart.md`

Definitions:
- **H** = history workbook date (workbook contains draws through end of H)
- **D** = results/winners date (**D = H + 1 day**)

Example: Pick3StatsC4 `H=2025-06-20` → results `D=2025-06-21` → sharepacks live under `sharepacks/2025-06-21/`.

---

## 0) Session safety + preflight

From repo root:
```bash
pwd
git status -s
```

Read (fast, high-signal):
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/FINAL_WORKFLOW_ARCHITECTURE_AAT9.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Master_Validation_Preflight.md`

Tracked states (tables exist; skip GA/TX):
CT, DE, FL, IN, MI, NJ, NY, NC, OH, OntarioCanada, PA, PR, SC, VA
(SSOT: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`)

---

## 1) Select the workbook + results inputs (H → D)

1) Confirm the history workbook exists:
- Either naming is accepted in `data/history/`:
  - `data/history/Pick3StatsC4_<YYYY-MM-DD>.xlsm`
  - `data/history/Pick3StatsC4_<YYYY_MM_DD>.xlsm`

2) Confirm the day‑ahead results file exists:
- `data/results/<D>.txt`

If you’re starting from a results date D and unsure of H:
- `H = D - 1 day`

---

## 2) Build the “world snapshot” (tables/JSON + winners guard)

Recommended one‑shot wrapper (enforces day‑ahead rule and performs CT/FL sanity checks):
```bash
PYTHONPATH=.:src python3 scripts/tools/run_history_and_results.py --history-date <H> --regen-aux-draws
```

This will (see the preflight doc for details):
- activate the workbook into `data/original/Pick3StatsC4.xlsm`
- rebuild tables + JSON
- generate winners HTML/JSON under `reports/stable/winners_by_date/<D>/`
- write a run log JSON under `reports/stable/validation_logs/validation_<D>.json`

Stop if this step fails. Do not run analyzers on stale tables.

---

## 3) Run Brain‑1 tools (live outputs)

### 3.1 Digit Reduction (batch via results file)
Use the batch snippet in:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Final_Validation_Help.md`

Important: live DR outputs are overwritten by the next run/date. Freeze to sharepacks immediately after a successful run.

### 3.2 Stable (per state; winners pulled from results file)
Run Stable per tracked state using `scripts/tools/run_stable_from_results.py`.

Results label overrides (Stable only):
- `NewJersey4` → `"New Jersey"`
- `NewYork4` → `"New York"`
- `NorthCarolina4` → `"North Carolina"`
- `OntarioCanada4` → `"Ontario"`
- `PuertoRico4` → `"Puerto Rico"`
- `SouthCarolina4` → `"South Carolina"`
(Source: `scripts/tools/build_stable_sharepacks.py`)

Example:
```bash
PYTHONPATH=.:src python3 scripts/tools/run_stable_from_results.py \
  --state OntarioCanada4 \
  --results-file data/results/<D>.txt \
  --results-label Ontario \
  --min-occ 1 \
  --write-bundle
```

Batch example (recommended; applies label overrides automatically):
```bash
D=2025-06-21
states=(Connecticut4 Delaware4 Florida4 Indiana4 Michigan4 NewJersey4 NewYork4 NorthCarolina4 Ohio4 OntarioCanada4 Pennsylvania4 PuertoRico4 SouthCarolina4 Virginia4)

declare -A LABEL_OVERRIDE=(
  [NewJersey4]="New Jersey"
  [NewYork4]="New York"
  [NorthCarolina4]="North Carolina"
  [OntarioCanada4]="Ontario"
  [PuertoRico4]="Puerto Rico"
  [SouthCarolina4]="South Carolina"
)

for S in "${states[@]}"; do
  extra=()
  if [[ -n "${LABEL_OVERRIDE[$S]:-}" ]]; then
    extra=(--results-label "${LABEL_OVERRIDE[$S]}")
  fi
  PYTHONPATH=.:src python3 scripts/tools/run_stable_from_results.py \
    --state "$S" \
    --results-file "data/results/$D.txt" \
    --min-occ 1 \
    --write-bundle \
    "${extra[@]}"
done
```

### 3.3 VTRAC enhanced + validator + day bundle
Important: validate against the **date-scoped winners lens** under `reports/stable/winners_by_date/<D>/<STATE>/`.
The legacy `data/outputs/winners/` cache can be stale and can produce empty/invalid `vtrac_compact_report.*` if used accidentally.

Per state:
```bash
python3 TOOLS/vtrac_enhanced_cli.py --state <STATE>
python3 TOOLS/vtrac_validate.py --state <STATE> --winners-dir reports/stable/winners_by_date/<D>/<STATE>
```

Then rebuild day‑level VTRAC share artifacts:
```bash
python3 TOOLS/run_vtrac_share_bundle.py
```

Batch example:
```bash
states=(Connecticut4 Delaware4 Florida4 Indiana4 Michigan4 NewJersey4 NewYork4 NorthCarolina4 Ohio4 OntarioCanada4 Pennsylvania4 PuertoRico4 SouthCarolina4 Virginia4)
for S in "${states[@]}"; do
  python3 TOOLS/vtrac_enhanced_cli.py --state "$S"
  python3 TOOLS/vtrac_validate.py --state "$S" --winners-dir "reports/stable/winners_by_date/$D/$S"
done
python3 TOOLS/run_vtrac_share_bundle.py
```

### 3.4 Hot Zones (per state)
```bash
PYTHONPATH=.:src python3 scripts/hot_zones/run_hot_zones_cli.py \
  --state <STATE> \
  --date <D> \
  --json data/outputs/json_tables/<STATE>_tables.json \
  --out-dir data/outputs/analysis/hot_zones/<STATE>
```

Batch example:
```bash
D=2025-06-21
states=(Connecticut4 Delaware4 Florida4 Indiana4 Michigan4 NewJersey4 NewYork4 NorthCarolina4 Ohio4 OntarioCanada4 Pennsylvania4 PuertoRico4 SouthCarolina4 Virginia4)
for S in "${states[@]}"; do
  PYTHONPATH=.:src python3 scripts/hot_zones/run_hot_zones_cli.py \
    --state "$S" \
    --date "$D" \
    --json "data/outputs/json_tables/${S}_tables.json" \
    --out-dir "data/outputs/analysis/hot_zones/$S"
done
```

---

## 4) Freeze Brain‑1 into sharepacks/<D>/ (full‑day snapshot)

Safety rule:
- If `sharepacks/<D>/` already exists and contains artifacts, treat it as immutable. Do not overwrite it silently. Either pick a new date folder (for a re-run) or intentionally archive/remove it first.

### Recommended (multi‑day safe): use the freezer script

If you have run more than one day in this repo, the live output folders can contain multiple historical artifacts (especially Digit Reduction overlays and Hot Zones winner maps). In that case, **do not** use a naive `cp -a .../.` copy; it will drag stale files into the new day sharepack.

Use the safe freezer:
```bash
python3 scripts/tools/freeze_sharepack_day.py --date <D>
```

This copies only the lean, day‑relevant files into `sharepacks/<D>/...` and avoids cross‑day contamination.

### Manual copy (single‑day / clean-output only)

If you are running in a clean workspace (or you just want to do this manually), copy the live outputs into the sharepack layout:

Required inputs (live → sharepack):
- Tables: `data/outputs/tables/<STATE>/{Combined_Combined,Midday_Combined,Evening_Combined}.csv` → `sharepacks/<D>/<STATE>/tables/`
- JSON tables: `data/outputs/json_tables/<STATE>_tables.json` → `sharepacks/<D>/<STATE>/json/<STATE>_tables.json`
- Winners lens: `reports/stable/winners_by_date/<D>/<STATE>/` → `sharepacks/<D>/<STATE>/winners/<STATE>/`
- Stable: `data/outputs/analysis/patterns/<STATE>/` → `sharepacks/<D>/<STATE>/stable/<STATE>/`
- Digit Reduction: `data/outputs/analysis/digit_reduction/<STATE>/` → `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/`
- VTRAC:
  - Enhanced: `data/outputs/analysis/vtrac/<STATE>/` → `sharepacks/<D>/<STATE>/vtrac/<STATE>/`
  - Validation: `data/outputs/analysis/vtrac_validation/<STATE>/validation_report.{json,md}` → `sharepacks/<D>/<STATE>/vtrac/<STATE>/`
- Hot Zones: `data/outputs/analysis/hot_zones/<STATE>/` → `sharepacks/<D>/<STATE>/hot_zones/<STATE>/`

Day‑level VTRAC artifacts (copy once per day):
- `data/outputs/analysis/vtrac_validation/summary.{md,csv}` → `sharepacks/<D>/`
- `data/outputs/analysis/vtrac_validation/vtrac_compact_report.{json,csv}` → `sharepacks/<D>/`
- Optional: `data/outputs/analysis/vtrac_validation/*.zip` → `sharepacks/<D>/`

Batch copy example (safe: creates folders, copies files; does not delete anything):
```bash
D=2025-06-21
if [[ -d "sharepacks/$D" ]] && [[ -n "$(ls -A "sharepacks/$D" 2>/dev/null)" ]]; then
  echo "[ABORT] sharepacks/$D already exists and is non-empty; refusing to overwrite."
  exit 1
fi
mkdir -p "sharepacks/$D"

states=(Connecticut4 Delaware4 Florida4 Indiana4 Michigan4 NewJersey4 NewYork4 NorthCarolina4 Ohio4 OntarioCanada4 Pennsylvania4 PuertoRico4 SouthCarolina4 Virginia4)

for S in "${states[@]}"; do
  mkdir -p "sharepacks/$D/$S"/{tables,json}
  mkdir -p "sharepacks/$D/$S/winners/$S"
  mkdir -p "sharepacks/$D/$S/stable/$S" "sharepacks/$D/$S/digit_reduction/$S" "sharepacks/$D/$S/vtrac/$S" "sharepacks/$D/$S/hot_zones/$S"

  cp -a "data/outputs/tables/$S/Combined_Combined.csv" "sharepacks/$D/$S/tables/"
  cp -a "data/outputs/tables/$S/Midday_Combined.csv" "sharepacks/$D/$S/tables/"
  cp -a "data/outputs/tables/$S/Evening_Combined.csv" "sharepacks/$D/$S/tables/"
  cp -a "data/outputs/json_tables/${S}_tables.json" "sharepacks/$D/$S/json/${S}_tables.json"

  cp -a "reports/stable/winners_by_date/$D/$S/." "sharepacks/$D/$S/winners/$S/"
  cp -a "data/outputs/analysis/patterns/$S/." "sharepacks/$D/$S/stable/$S/"
  cp -a "data/outputs/analysis/digit_reduction/$S/." "sharepacks/$D/$S/digit_reduction/$S/"
  cp -a "data/outputs/analysis/vtrac/$S/." "sharepacks/$D/$S/vtrac/$S/"
  cp -a "data/outputs/analysis/vtrac_validation/$S/validation_report.json" "sharepacks/$D/$S/vtrac/$S/" || true
  cp -a "data/outputs/analysis/vtrac_validation/$S/validation_report.md" "sharepacks/$D/$S/vtrac/$S/" || true
  cp -a "data/outputs/analysis/hot_zones/$S/." "sharepacks/$D/$S/hot_zones/$S/"
done

cp -a data/outputs/analysis/vtrac_validation/summary.md "sharepacks/$D/summary.md" || true
cp -a data/outputs/analysis/vtrac_validation/summary.csv "sharepacks/$D/summary.csv" || true
cp -a data/outputs/analysis/vtrac_validation/vtrac_compact_report.json "sharepacks/$D/" || true
cp -a data/outputs/analysis/vtrac_validation/vtrac_compact_report.csv "sharepacks/$D/" || true
cp -a data/outputs/analysis/vtrac_validation/*.zip "sharepacks/$D/" || true
```

After freezing, validate the compact report:
```bash
python3 scripts/tools/validate_vtrac_compact_report.py --date <D>
```

---

## 5) Freeze Aux (Part 3) into the sharepack (history‑aligned; no drift)

Aux must align to the same history workbook that produced the tables (H).

Per state (writes into `sharepacks/<D>/<STATE>/aux/...`):
```bash
python3 scripts/tools/aux_sharepack_summary.py \
  --date <D> \
  --state <STATE> \
  --excel data/history/Pick3StatsC4_<H>.xlsm  # use the exact filename that exists (YYYY-MM-DD or YYYY_MM_DD)
```

Batch example:
```bash
D=2025-06-21
H_FILE="data/history/Pick3StatsC4_2025_06_20.xlsm"  # or Pick3StatsC4_2025-06-20.xlsm (use the one that exists)
states=(Connecticut4 Delaware4 Florida4 Indiana4 Michigan4 NewJersey4 NewYork4 NorthCarolina4 Ohio4 OntarioCanada4 Pennsylvania4 PuertoRico4 SouthCarolina4 Virginia4)
for S in "${states[@]}"; do
  python3 scripts/tools/aux_sharepack_summary.py \
    --date "$D" \
    --state "$S" \
    --excel "$H_FILE"
done
```

Sanity check (sharepack mode; strict):
```bash
python3 scripts/tools/validate_tables_aux_alignment.py --date <D> --state <STATE> --strict
```

---

## 6) Freeze Brain‑2 / Control Center into the same sharepack day folder

Once per day:
```bash
python3 scripts/tools/export_control_center_sharepack.py --date <D>
```

Outputs land under:
- `sharepacks/<D>/control_center/`

---

## 7) (Optional but recommended) Generate paste‑ready evidence blocks + run‑report scaffolds

Per state, generate per‑tool `summary.md` blocks inside the sharepack so later sessions don’t need raw files:
- Stable: `scripts/tools/stable_sharepack_summary.py`
- DR: `scripts/tools/dr_sharepack_summary.py`
- VTRAC: `scripts/tools/vtrac_sharepack_summary.py`
- Hot Zones: `scripts/tools/hot_zones_sharepack_summary.py`
(Commands and output paths: see the Evaluate‑Only quickstart.)

Optional validation helpers (interpretation matters):
- **Pipeline / wiring failures (Fix‑Now):** missing required artifacts, `validate_tables_aux_alignment.py` failures (drift), empty `vtrac_compact_report.json`.
- **Tool outcomes (record):** a tool can “miss” the winner even when artifacts are correct (this is evaluation signal, not corruption).
  - Stable: `PYTHONPATH=.:src python3 scripts/tools/validate_stable_winners.py --sharepack sharepacks/<D>/<STATE>/stable/<STATE>` (prints `NOTE` for “no exact hit”; fails only on mismatch)
  - DR: `PYTHONPATH=.:src python3 scripts/tools/validate_dr_winners.py --sharepack sharepacks/<D>/<STATE>/digit_reduction/<STATE>` (internal consistency vs stamp)
  - Hot Zones: `python3 scripts/tools/validate_hot_zones_winners.py --sharepack sharepacks/<D>/<STATE>/hot_zones/<STATE>` (coverage/performance; failure often means “Hot Zones didn’t isolate winner”)

Then scaffold the run report (what you actually fill/share):
```bash
python3 scripts/tools/create_master_validation_run_report.py --date <D> --state <STATE>
```

---

## Definition of Done (full‑day ready for template filling)

For the day folder `sharepacks/<D>/`:
- Per‑state folders exist for the tracked states and contain: tables/json/winners + all tool bundles + aux snapshot.
- Day‑level VTRAC artifacts exist and validate: `sharepacks/<D>/vtrac_compact_report.json` is non‑empty.
- Brain‑2 export exists: `sharepacks/<D>/control_center/README.md`.
- (Optional) Run reports are scaffolded under `docs/AAT9_KIT/FINAL VALIDATION/RUNS/`.
