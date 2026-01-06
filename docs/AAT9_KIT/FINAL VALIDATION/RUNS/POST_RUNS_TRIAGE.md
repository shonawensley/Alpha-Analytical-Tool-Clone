# Post Runs Triage (Gold Days 2025‑06‑21 → 2025‑06‑23)

Purpose: consolidate “post‑run negative observations” into a single SSOT view so we can clearly separate:

- **Pipeline / semantics bugs** (Fix‑Now; distort reality)
- **Tool outcomes** (not bugs; learn from them)
- **Fix‑Later tuning ideas** (do not implement until we have more days)

This triage is deliberately **evidence‑linked** so future context resets don’t restart debates.

## Status Legend

- **Closed**: verified resolved (or prevented) in current gold‑day corpus.
- **Closed (misframed)**: not a defect; expected behavior or a terminology issue.
- **Fixed (forward)**: fixed in code for future days; existing sharepacks are not retro‑rewritten.
- **Needs human check**: requires a quick manual sanity check (usually around input provenance).
- **Fix‑Later**: tuning/strategy; don’t treat as correctness work.

## Source Set (Post Runs package)

Note: several `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/*.md` files are actually Word `.docx` content. The readable copies are:

- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/_extracted_txt/CHAT1_1.txt`
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/_extracted_txt/chat1_2.txt`
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/_extracted_txt/chat1_3.txt`
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/_extracted_txt/chat1_AAT9 Gold Days 2025 Analysis Research.txt`
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/_extracted_txt/chat2_1.txt`
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/_extracted_txt/chat2_2.txt`
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/_extracted_txt/chat2_3_runsinsights.txt`
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/_extracted_txt/chat2_4runsinsights.txt`
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/_extracted_txt/CODEX_ANALYSIS.txt`

Local fix summaries derived from those sources:

- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/fix_report.md`
- `docs/AAT9_KIT/FINAL VALIDATION/POST RUNS/fix_report_feedback.md`

## “Truth” Surfaces (where to validate)

- Gold‑days corpus audit: `reports/audit/sharepacks_audit_gold_days.md`
- Fix‑Now execution list: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md`
- Fix‑Later index (auto‑extracted from filled run reports): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_LATER_INDEX.md`

## Triage Table (claims → status)

| Claim / Concern | Status | What it really is | Evidence / Where to check |
|---|---|---|---|
| **“Québec shows up inside PuertoRico winners/DR”** | Closed | Results parsing ambiguity (tab/extra‑token issues) caused cross‑state contamination in reporting. | `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md` (FN‑001) · Spot check: no `Québec` strings in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-21__PuertoRico4.md` / `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2025-06-23__PuertoRico4.md` |
| **Puerto Rico missing on some days (ex: 2025‑06‑22)** | Closed | Expected missing results line; should be skipped, not treated as “miss.” | Audit SKIPS in `reports/audit/sharepacks_audit_gold_days.md` · FN‑003 in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md` |
| **One‑winner day semantics (Midday blank, Evening present)** | Closed | Results file semantics; summaries/validators must preserve which period is missing. | FN‑002 in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md` · `data/results/2025-06-22.txt` (`South Carolina\t\t675`) |
| **Hot Zones “winner_not_in_winner_map” = tool is broken** | Closed (misframed) | `winner_map` is a **Top‑N snapshot**, not an exhaustive list; the winner can be present in per‑lane/top‑lanes while absent from `winner_map`. | Example: `sharepacks/2025-06-21/NorthCarolina4/hot_zones/NorthCarolina4/summary.json` shows `top_lanes.present=true` with `best_rank`, and explains `winner_map` scope. |
| **Stable “missing Combined patterns / dropped winners”** | Closed (misframed) + guardrail | The gold‑day sharepacks contain Stable sections `Midday/Evening/Combined`. Historical “missing” notes likely came from naming/path drift during earlier runs. Current build prevents silent “zero Stable output” by failing fast. | Evidence: `sharepacks/2025-06-21/OntarioCanada4/stable/OntarioCanada4/OntarioCanada4_stable_patterns_scores.csv` has `section` values `Combined/Evening/Midday` · Corpus audit PASS in `reports/audit/sharepacks_audit_gold_days.md` · Guardrails in `scripts/tools/freeze_sharepack_day.py` (fails fast if required artifacts missing). |
| **Winner logging loses literal vs canonical (e.g., 032 becomes 023 only)** | Closed | Winners lens + summaries carry both `literal` and `canonical`; earlier false negatives were mostly **leading‑zero dtype** issues in summarizers/validators, not loss of the winner itself. | Example: `sharepacks/2025-06-21/Florida4/stable/Florida4/summary.json` winners include `literal` + `canonical` · See “leading zeros” item below. |
| **Leading‑zero corruption (033 → 33) causes false “missing winner” alarms** | Closed | Evaluation scripts reading CSV with dtype inference, not analyzer failure. | Fixed in scripts/tools summarizers/validators (dtype=str); cross‑check with Florida box `033` cases. |
| **Aux draws and tables drift (wrong workbook snapshot)** | Closed | A real integrity risk; now guarded by strict alignment validator + sharepack provenance. | `scripts/tools/validate_tables_aux_alignment.py` is required guardrail (see FN‑004) · PASS in `reports/audit/sharepacks_audit_gold_days.md`. |
| **Profit Alerts output malformed candidates (non‑Pick‑3 canonicals)** | Closed | Export/eval contract issue; candidates must be gradeable objects. | Profit alerts rows validated on gold days (0 malformed canonicals) · See `sharepacks/<D>/control_center/profit_alerts.csv`. |
| **Ohio `nan**` in Combined tables** | Fixed (forward) | Table generator hygiene: avoid decorating NaN/empty cells with marker symbols. Existing sharepacks remain as‑is. | FN‑005 in `docs/AAT9_KIT/FINAL VALIDATION/RUNS/FIX_NOW_LEDGER.md` · Code in `src/utils/table_generator.py` (future builds). |
| **Ontario DR Evening overlay “missing flags/hits” (winner 616)** | Closed (misframed) | Tool outcome edge case: `winner_stamp.items_total=0` means there are no overlay items to stamp; missing/empty files should not be treated as corruption. | `sharepacks/2025-06-22/OntarioCanada4/digit_reduction/OntarioCanada4/summary.json` shows Evening `items_total=0`. |
| **Ontario “off‑by‑one” draw boundary (678 vs 617 confusion)** | Closed (misframed) | Comparing frozen sharepack draws to live `data/cleaned/draws` after workbook swaps creates false mismatch alarms. Always validate against the **sharepack’s** aux/draws snapshot for that day. | Compare within sharepack only: `sharepacks/<D>/<STATE>/aux/draws/*_draws.csv` + `data/results/<D>.txt`. Avoid using live draws unless you are rebuilding that day. |

## Human Verification Checklist (for new “gold day” additions)

Use this when you add a new history workbook H + results day D:

0) Quick workbook sanity (preflight): confirm the history workbook is actually “H”
   - Pick a sentinel state (New York is a good one) and confirm the newest extracted draws match the winners in `data/results/<H>.txt`.
   - If the newest draw in the workbook matches `data/results/<H+2>.txt`, the workbook is misdated and any `sharepacks/<D=H+1>/` built from it will be tainted.

1) Run the corpus audit on the new day (and scan WARN/FAIL):  
   `python3 scripts/tools/audit_sharepacks_corpus.py --dates D`
2) Verify provenance: `sharepacks/<D>/README.md` and `sharepacks/<D>/*/aux/*/summary.json` should cite the correct H workbook path.
3) Validate tables ↔ aux alignment (strict):  
   `python3 scripts/tools/validate_tables_aux_alignment.py --date D --strict`
4) If a state is missing in `data/results/<D>.txt`, mark it **expected N/A** (skip grading), not a miss.
5) Do not compare sharepacks to live caches unless you are deliberately rebuilding that day.
