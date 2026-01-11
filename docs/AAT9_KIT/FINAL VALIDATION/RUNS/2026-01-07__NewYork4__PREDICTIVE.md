# Predictive Run Report — NewYork4 — D=2026-01-07 (H=2026-01-06)

Purpose
- Capture a **pre-results** snapshot analysis for one state/day.
- Keep predictions gradeable via `candidate_universe.json` (do not mix in winners artifacts).

Scope
- Results date (D): `2026-01-07`
- History workbook date (H): `2026-01-06` (usually D-1)
- Predictive sharepack root: `sharepacks/_predictive`
- Sharepack state dir: `sharepacks/_predictive/2026-01-07/NewYork4`

---

## Candidate Universe (gradeable predictions)

- Candidate Universe: `sharepacks/_predictive/2026-01-07/NewYork4/candidate_universe.json`
- Packs: `18`; union combos: `83`
- contains_winners_artifacts: `False`
- Pack list (id → mode → cost):
  - `aux_positional_shortlist` → `STRAIGHT` → `10`
  - `combo_pack:PackA_vt8:seed=016` → `STRAIGHT` → `8`
  - `combo_pack:PackB_mirror3rd:seed=016` → `STRAIGHT` → `8`
  - `combo_pack:R-perm-4:envelope` → `STRAIGHT` → `16`
  - `digit_reduction_top:Combined` → `STRAIGHT` → `2`
  - `digit_reduction_top:Evening` → `STRAIGHT` → `3`
  - `digit_reduction_top:Midday` → `STRAIGHT` → `2`
  - `due_doubles:Combined` → `BOX` → `12`
  - `due_doubles:Evening` → `BOX` → `12`
  - `due_doubles:Midday` → `BOX` → `12`
  - `hot_zones_top_triads` → `STRAIGHT` → `8`
  - `profit_alerts:Combined:A05` → `STRAIGHT` → `3`
  - `profit_alerts:Evening:A12` → `STRAIGHT` → `4`
  - `profit_alerts:Midday:A04` → `BOX` → `6`
  - `stable_top:Combined` → `BOX` → `9`
  - `stable_top:Evening` → `BOX` → `9`
  - `stable_top:Midday` → `BOX` → `9`
  - `vtrac_top_straights` → `STRAIGHT` → `8`

## Evidence pointers (sharepack-local)

- Sharepack state README: `sharepacks/_predictive/2026-01-07/NewYork4/README.md`
- Candidate Universe: `sharepacks/_predictive/2026-01-07/NewYork4/candidate_universe.json`
- Control Center portal dir: `sharepacks/_predictive/2026-01-07/control_center`
- Profit Alerts: `sharepacks/_predictive/2026-01-07/control_center/profit_alerts.csv`
- Due Doubles: `sharepacks/_predictive/2026-01-07/control_center/due_doubles.csv`
- VTRAC Repeat Watch: `sharepacks/_predictive/2026-01-07/control_center/vtrac_repeat_watch.csv`
- Stable scores: `sharepacks/_predictive/2026-01-07/NewYork4/stable/NewYork4/NewYork4_stable_patterns_scores.csv`
- Stable report: `sharepacks/_predictive/2026-01-07/NewYork4/stable/NewYork4/NewYork4_stable_patterns_report.html`
- Digit Reduction report: `sharepacks/_predictive/2026-01-07/NewYork4/digit_reduction/NewYork4/NewYork4_digit_reduction_report.html`
- DR Analyzer V2 top: `sharepacks/_predictive/2026-01-07/NewYork4/digit_reduction/NewYork4/analyzer_v2/NewYork4_analyzer_v2_top_candidates.csv`
- Hot Zones top lanes: `sharepacks/_predictive/2026-01-07/NewYork4/hot_zones/NewYork4/NewYork4_hot_zones_top_lanes.csv`
- Aux summary: `sharepacks/_predictive/2026-01-07/NewYork4/aux/NewYork4/summary.md`

## Analyst notes (fill in)

- What is the strongest evidence cluster (Stable/DR/VTRAC/HZ/Aux/Profit Alerts)?
- Which pack(s) do you actually want to play (budgeted, boxed-first)?
- Any cross-variant notes (Midday vs Evening), without treating Combined as an outcome?
- Any anomalies (missing artifacts, suspicious drift, etc.)?
