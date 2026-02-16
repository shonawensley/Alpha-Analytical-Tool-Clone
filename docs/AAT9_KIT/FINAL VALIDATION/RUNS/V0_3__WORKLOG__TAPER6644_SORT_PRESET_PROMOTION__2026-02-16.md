# Worklog — Taper6644 Sort Preset Promotion (B36 • stable10 • tool_only) — 2026-02-16

Goal: keep the promoted taper6644 allocation geometry fixed and test one **index chooser** lever. Promote only if Crossroads gates pass.

Lock:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: **B36 only**
- No analyzer edits (selection-layer only)

## Strategies compared

Baseline:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644` (sort preset: `methods_first`)

Candidates:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first`
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_packs_first`

## Notes

- `sharepacks/_predictive/2026-01-19` is missing (Sunday); window tooling excludes missing grade days automatically.
- Geometry invariants confirm indices_touched and max_lines/index stay consistent with taper6644; only index ordering/membership changes.

## Commands executed (repro)

Rebuild Play Cards (adds new strategy keys into per-state `play_card__tool_only__stable10.json`):
```bash
python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag stable10 --write-md --force
```

Re-grade Play Cards:
```bash
python3 scripts/tools/grade_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag stable10 --force
```

Generate ladders + casebooks (B36-only):
```bash
python3 scripts/tools/create_conversion_ladder_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategy <STRAT> --budgets B36 --write-casebook --casebook-budget B36 --casebook-n 5
```

Generate sweep scoreboards:
```bash
python3 scripts/tools/create_conversion_scoreboard.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategies <BASE,C1,C2> --budgets B36 --out <OUT.md>
```

Winner lane rank sweep:
```bash
python3 scripts/tools/create_winner_lane_rank_report.py --date-from <D0> --date-to <D1> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag stable10 --strategies <BASE,C1,C2> --budget B36 --out-csv <OUT.csv> --out-md <OUT.md>
```

Lane allocation:
```bash
python3 scripts/tools/create_lane_allocation_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategy <STRAT> --budget B36 --label TAPER6644_SORT_PRESET_SWEEP
```

Geometry invariants:
```bash
python3 scripts/tools/create_play_card_geometry_invariants_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --roster-strategy <BASELINE_STRAT> --baseline-strategy <BASELINE_STRAT> --strategies <BASE,C1,C2> --budget B36 --label TAPER6644_SORT_PRESET_SWEEP
```

## Outputs written (key)

Morning brief (promotion decision):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SORT_PRESET_PROMOTION__2026-02-16.md:1`

Scoreboards (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`

Geometry invariants (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`

Winner lane rank sweeps (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__TAPER6644_SORT_PRESET_SWEEP.md:1`

Casebooks (B36-only; per strategy/window):
- Jan candidate: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first__stable10__B36.md:1`
- OOS candidate: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first__stable10__B36.md:1`

## Outcome

- Promoted: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first`
- Default no longer uses `methods_first` under taper6644; it uses `score_total_first`.

