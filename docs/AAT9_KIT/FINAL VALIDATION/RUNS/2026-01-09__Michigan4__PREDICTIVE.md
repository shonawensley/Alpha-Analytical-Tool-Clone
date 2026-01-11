# Predictive Run Report — Michigan4 — D=2026-01-09 (H=2026-01-08)

Purpose
- Capture a **pre-results** snapshot analysis for one state/day.
- Keep predictions gradeable via `candidate_universe.json` (do not mix in winners artifacts).

Scope
- Results date (D): `2026-01-09`
- History workbook date (H): `2026-01-08` (usually D-1)
- Predictive sharepack root: `sharepacks/_predictive`
- Sharepack state dir: `sharepacks/_predictive/2026-01-09/Michigan4`

---

## Candidate Universe (gradeable predictions)

- Candidate Universe: `sharepacks/_predictive/2026-01-09/Michigan4/candidate_universe.json`
- Packs: `30`; union combos: `120`
- contains_winners_artifacts: `False`
- Pack list (id → mode → cost):
  - `aux_positional_shortlist` → `STRAIGHT` → `10`
  - `aux_vtrac_index_overdue:Combined:idx=32` → `STRAIGHT` → `6`
  - `aux_vtrac_index_overdue:Combined:idx=35` → `STRAIGHT` → `6`
  - `aux_vtrac_index_overdue:Evening:idx=32` → `STRAIGHT` → `6`
  - `aux_vtrac_index_overdue:Evening:idx=35` → `STRAIGHT` → `6`
  - `aux_vtrac_index_overdue:Midday:idx=26` → `STRAIGHT` → `6`
  - `aux_vtrac_index_overdue:Midday:idx=35` → `STRAIGHT` → `6`
  - `combo_pack:PackA_vt8:seed=124` → `STRAIGHT` → `8`
  - `combo_pack:PackB_mirror3rd:seed=124` → `STRAIGHT` → `12`
  - `combo_pack:R-perm-4:envelope` → `STRAIGHT` → `16`
  - `combo_pack:consensus_double_9:trigger=1:keys=942` → `MIXED` → `9`
  - `digit_reduction_top:Combined` → `STRAIGHT` → `2`
  - `digit_reduction_top:Evening` → `STRAIGHT` → `3`
  - `digit_reduction_top:Midday` → `STRAIGHT` → `2`
  - `due_doubles:Combined` → `BOX` → `12`
  - `due_doubles:Evening` → `BOX` → `12`
  - `due_doubles:Midday` → `BOX` → `12`
  - `due_doubles_mirror_double:Combined:seed=112` → `BOX` → `6`
  - `due_doubles_mirror_double:Evening:seed=112` → `BOX` → `6`
  - `due_doubles_mirror_double:Midday:seed=112` → `BOX` → `6`
  - … (10 more)

## Evidence pointers (sharepack-local)

- Sharepack state README: `sharepacks/_predictive/2026-01-09/Michigan4/README.md`
- Candidate Universe: `sharepacks/_predictive/2026-01-09/Michigan4/candidate_universe.json`
- Control Center portal dir: `sharepacks/_predictive/2026-01-09/control_center`
- Profit Alerts: `sharepacks/_predictive/2026-01-09/control_center/profit_alerts.csv`
- Due Doubles: `sharepacks/_predictive/2026-01-09/control_center/due_doubles.csv`
- VTRAC Repeat Watch: `sharepacks/_predictive/2026-01-09/control_center/vtrac_repeat_watch.csv`
- Stable scores: `sharepacks/_predictive/2026-01-09/Michigan4/stable/Michigan4/Michigan4_stable_patterns_scores.csv`
- Stable report: `sharepacks/_predictive/2026-01-09/Michigan4/stable/Michigan4/Michigan4_stable_patterns_report.html`
- Digit Reduction report: `sharepacks/_predictive/2026-01-09/Michigan4/digit_reduction/Michigan4/Michigan4_digit_reduction_report.html`
- DR Analyzer V2 top: `sharepacks/_predictive/2026-01-09/Michigan4/digit_reduction/Michigan4/analyzer_v2/Michigan4_analyzer_v2_top_candidates.csv`
- Hot Zones top lanes: `sharepacks/_predictive/2026-01-09/Michigan4/hot_zones/Michigan4/Michigan4_hot_zones_top_lanes.csv`
- Aux summary: `sharepacks/_predictive/2026-01-09/Michigan4/aux/Michigan4/summary.md`

## Analyst notes (fill in)

- What is the strongest evidence cluster (Stable/DR/VTRAC/HZ/Aux/Profit Alerts)?
- Which pack(s) do you actually want to play (budgeted, boxed-first)?
- Any cross-variant notes (Midday vs Evening), without treating Combined as an outcome?
- Any anomalies (missing artifacts, suspicious drift, etc.)?
