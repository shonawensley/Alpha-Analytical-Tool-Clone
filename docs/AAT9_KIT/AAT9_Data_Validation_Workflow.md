# AAT9 — Data Validation & Sharing Workflow

Purpose: capture the step-by-step loop for generating V-TRAC enhanced analyzer evidence, validating it against Winners Logger outputs, and preparing artifacts for deeper analysis (ChatGPT Pro, human reviewers, or future automation).

## 1. Generate Analyzer Outputs

1. Pick the target states for the run.
2. Refresh the enhanced bundle:
   ```powershell
   python tools/vtrac_enhanced_cli.py --state <STATE>
   ```
3. Run the validator to produce markdown/JSON parity reports:
   ```powershell
   python tools/vtrac_validate.py --state <STATE>
   ```
4. Optional batch summary (recommended each sweep):
   ```powershell
   python tools/vtrac_validate_batch.py --states <STATE1> <STATE2> ...
   ```
   This writes `data/outputs/analysis/vtrac_validation/matrix.csv` and `findings.md`.

5. Generate share bundle (summaries + compact report + optional ZIP):
   ```powershell
   python TOOLS/run_vtrac_share_bundle.py
   ```
   This refreshes:
   - `summary.md` / `summary.csv`
   - `vtrac_compact_report.json` / `vtrac_compact_report.csv` (config-aware scorer)
   - `vtrac_validation_full_payload.zip` (optional all-in-one archive)
   - Uses `configs/vtrac_score_config.json` for weights/priors; tweak as needed per run.

## 2. Where Artifacts Live

- Enhanced analyzer bundles:
  `data/outputs/analysis/vtrac/<STATE>/<STATE>_vtrac_enhanced_<TIMESTAMP>.json`
- Validator reports:
  `data/outputs/analysis/vtrac_validation/<STATE>/validation_report.{md,json}`
- Batch summary:
  `data/outputs/analysis/vtrac_validation/matrix.csv`
  `data/outputs/analysis/vtrac_validation/findings.md`
- Compact scoring outputs:
  `data/outputs/analysis/vtrac_validation/vtrac_compact_report.{json,csv}`
- Share bundle ZIP:
  `data/outputs/analysis/vtrac_validation/vtrac_validation_full_payload.zip`

These directories are safe to delete and regenerate, but keep the most recent run committed when sharing with downstream reviewers.

## 3. Hand-Off Options

| Option | How | Pros | Cons |
|--------|-----|------|------|
| Commit & push | `git add data/outputs/...` → `git commit` → `git push` | GitHub raw URLs work with ChatGPT Pro / agents; versioned history | Repo grows if every run is committed. Consider keeping only summaries or using a dedicated branch |
| Zip & upload | `Compress-Archive -Path data\outputs\analysis\vtrac_validation -DestinationPath vtrac_validation.zip` | Single upload across assistants; can bundle multiple runs | Must re-zip after re-run; download/extract step |
| Targeted upload | Drag/drop specific state files (e.g., Florida4 report + bundle + matrix) | Lightweight; easy for ad-hoc reviews | Hits the “5–6 file” limit quickly; manual selection |

**Tip:** When using GitHub URLs, the pattern is:
```
https://raw.githubusercontent.com/<user>/<repo>/<branch>/data/outputs/analysis/vtrac_validation/matrix.csv
```
Repeat for `summary.md`, `summary.csv`, and `vtrac_compact_report.{csv,json}` to give reviewers immediate access.

## 4. What Reviewers Look For

- Hot / super-hot counts vs. Winners expectations
- Consensus flags (columns 1–2) and stable columns (late-box survival)
- Analyzer ↔ Winners signature overlap (`validation_report.md` shows counts + tokens)
- Straight overlap (currently zero unless Winners Logger reports upcoming straights)
- Matrix / findings for cross-state context and anomalies (e.g., “Florida Combined has no 3-value signatures, expected because cells collapse to two digits”)

## 5. Iteration Loop

1. Produce bundles + validator reports (Section 1)
2. Provide artifacts using one of the hand-off options (Section 3)
3. Capture observations in `docs/AAT9_KIT/AAT9_Analysis_Insights.md`
4. Adjust weights / logic if needed (e.g., hot boosts, consensus multipliers)
5. Repeat the analysis sweep

Keep `AAT9_Testing_Roadmap.md` updated if new regression coverage is added (e.g., fixtures, new validator assertions).

### Quick checklist (one pass)

- [ ] `python tools/vtrac_enhanced_cli.py --state <STATE>`
- [ ] `python tools/vtrac_validate.py --state <STATE>`
- [ ] `python tools/vtrac_validate_batch.py --states <...>`
- [ ] `python TOOLS/run_vtrac_share_bundle.py` (summary/compact/zip refresh)
- [ ] Review `validation_report.md` overlap & anomalies
- [ ] Update `matrix.csv` / `findings.md` (commit or zip)
- [ ] Note insights in `AAT9_Analysis_Insights.md`
- [ ] Decide next tuning action (weights, docs, regression)

## 6. Aggregator Outlook

Once V-TRAC and the other tools have stable “final outputs,” we can feed their summarized insights into an aggregator that scores an entire draw. Until then:

- Make the validator pass part of every tuning cycle
- Preserve the evidence artifacts so reviewers can compare against Winners data rapidly
- Keep notes in `Analysis_Insights` to build an audit trail of what changed and why

This process keeps the tooling deterministic today while leaving room for future machine-learning enhancements when we have the data to support them.
