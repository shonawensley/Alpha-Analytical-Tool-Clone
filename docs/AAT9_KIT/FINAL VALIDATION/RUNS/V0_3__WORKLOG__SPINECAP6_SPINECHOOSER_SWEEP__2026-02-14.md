# Worklog — Spinecap6 “Spine Chooser” Sweep (B36 • stable10 • tool_only) — 2026-02-14

Goal: test a **single** within-lane conversion lever (how spine lines are chosen) on top of the promoted `spinecap6` geometry, without touching analyzers.

Lock:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: **B36 only**
- No analyzer edits (selection-layer only)

## New strategies (experimental; not promoted)

- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_evidence`
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_ranked`

Baseline for comparison:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`

## Commands executed (repro)

Rebuild Play Cards (adds the new strategies to the per-state `play_card__tool_only__stable10.json` artifacts):
```bash
python3 scripts/tools/create_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag stable10 --write-md --force
```

Re-grade Play Cards (updates `__PLAY_CARD_GRADE__tool_only__stable10.csv` to include the new strategies):
```bash
python3 scripts/tools/grade_play_card.py --date <D> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag stable10 --force
```

Generate ladders + casebooks (B36-only):
```bash
python3 scripts/tools/create_conversion_ladder_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategy <STRAT> --budgets B36 --write-casebook --casebook-budget B36 --casebook-n 5
```

Generate sweep scoreboards:
```bash
python3 scripts/tools/create_conversion_scoreboard.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategies <S1,S2,S3> --budgets B36 --out <OUT.md>
```

Winner lane rank sweep:
```bash
python3 scripts/tools/create_winner_lane_rank_report.py --date-from <D0> --date-to <D1> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag stable10 --strategies <S1,S2,S3> --budget B36
```

Lane allocation reports (from ladder CSVs):
```bash
python3 scripts/tools/create_lane_allocation_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategy <STRAT> --budget B36 --label <LABEL>
```

## Results (promotion gate check)

See the morning brief:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_SPINECHOOSER_SWEEP__2026-02-14.md:1`

## Outputs written (key)

Scoreboard sweeps:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_SPINECHOOSER_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_SPINECHOOSER_SWEEP.md:1`

Winner lane rank sweeps:
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_SPINECHOOSER_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_SPINECHOOSER_SWEEP.md:1`

Lane allocation (sanity):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_EVSPINE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_DISPRANK.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_EVSPINE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_DISPRANK.md:1`

Casebooks + ladders (per strategy/window; B36 casebooks):
- Jan: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_evidence__stable10__B36.md:1`
- Jan: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_ranked__stable10__B36.md:1`
- OOS: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_evidence__stable10__B36.md:1`
- OOS: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_ranked__stable10__B36.md:1`

## Outcome

- No promotion; baseline remains `...spinecap6`.
- Next lever should be designed as a constrained hybrid (preserve bounded display coverage, then use evidence to pick a small number of additional lines) rather than “replace the bounded pack”.

