# Worklog — Spinecap6 Taper6643 Evaluation (B36 • stable10 • tool_only) — 2026-02-15

Goal: test one micro-taper lever on top of the promoted B36 default (`...spine_taper_6644`) and reject if OOS strict regresses.

Lock:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: **B36 only**
- No analyzer edits (selection-layer only)

## Strategy under test (not promoted)

Candidate:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643`
  - Spine taper: `6,6,4,3` across the 4 spine indices (rank order)

Baseline:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644`

## Notes

- `sharepacks/_predictive/2026-01-19` is missing (Sunday); window tooling excludes missing grade days automatically.

## Commands executed (repro)

Rebuild Play Cards:
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
python3 scripts/tools/create_conversion_scoreboard.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategies <BASE,CANDIDATE> --budgets B36 --out <OUT.md>
```

Winner lane rank sweep:
```bash
python3 scripts/tools/create_winner_lane_rank_report.py --date-from <D0> --date-to <D1> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag stable10 --strategies <BASE,CANDIDATE> --budget B36 --out-csv <OUT.csv> --out-md <OUT.md>
```

Lane allocation:
```bash
python3 scripts/tools/create_lane_allocation_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategy <STRAT> --budget B36 --label SPINECAP6_TAPER6643_SWEEP
```

Geometry invariants:
```bash
python3 scripts/tools/create_play_card_geometry_invariants_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --roster-strategy <BASELINE_STRAT> --baseline-strategy <BASELINE_STRAT> --strategies <BASE,CANDIDATE> --budget B36 --label SPINECAP6_TAPER6643_SWEEP
```

## Outputs written (key)

Morning brief (decision):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_TAPER6643_EVAL__2026-02-15.md:1`

Scoreboards (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`

Geometry invariants (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`

Winner lane rank sweeps (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_TAPER6643_SWEEP.md:1`

Casebooks:
- Jan candidate: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643__stable10__B36.md:1`
- OOS candidate: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643__stable10__B36.md:1`

## Outcome

- Not promoted: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643`
- Default remains: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644`

