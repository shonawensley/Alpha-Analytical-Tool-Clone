# Worklog — Spinecap6 Display Canon Ranked Spine Chooser (B36 • stable10 • tool_only) — 2026-02-15

Goal: test a **single** within-lane lever on top of promoted `...spinecap6` while proving invariants (cap, display share, breadth) and measuring whether it changes anything (no-op rate + scoreboard deltas).

Lock:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: **B36 only**
- No analyzer edits (selection-layer only)

## Strategy under test (experimental; not promoted)

- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_canon_ranked`
  - Spine cap: 6 lines per spine index
  - Spine chooser: `display_canon_ranked` (rank display members by canonical/permutation evidence)

Baseline:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`

Comparator (already known to be effectively a no-op in the scoreboard):
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_ranked`

## Notes

- `sharepacks/_predictive/2026-01-19` is missing (Sunday); window tooling is robust to missing grade days and will exclude it automatically.

## Commands executed (repro)

Rebuild Play Cards (adds the new strategy key into per-state `play_card__tool_only__stable10.json`):
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
python3 scripts/tools/create_conversion_scoreboard.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategies <S1,S2,S3> --budgets B36 --out <OUT.md>
```

Winner lane rank sweep:
```bash
python3 scripts/tools/create_winner_lane_rank_report.py --date-from <D0> --date-to <D1> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag stable10 --strategies <S1,S2,S3> --budget B36 --out-csv <OUT.csv> --out-md <OUT.md>
```

Lane allocation (breadth/depth sanity; **label must be unique per strategy**):
```bash
python3 scripts/tools/create_lane_allocation_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategy <STRAT> --budget B36 --label <LABEL>
```

Geometry invariants (cap proof + no-op detection + display share):
```bash
python3 scripts/tools/create_play_card_geometry_invariants_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --roster-strategy <ROSTER_STRAT> --baseline-strategy <BASELINE_STRAT> --strategies <S1,S2,S3> --budget B36 --label <LABEL>
```

## Outputs written (key)

Morning brief (promotion decision):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__SPINECAP6_CANON_RANK_SPINECHOOSER__2026-02-15.md:1`

Scoreboards (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`

Geometry invariants (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__PLAY_CARD_GEOMETRY__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`

Winner lane rank sweeps (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__WINNER_LANE_RANK__tool_only__stable10__B36__SPINECAP6_CANON_RANK_SWEEP.md:1`

Lane allocation (one file per strategy label):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_BASE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_DISPRANK.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_CANONRANK.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_BASE.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_DISPRANK.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__LANE_ALLOCATION__tool_only__stable10__B36__SPINECAP6_CANONRANK.md:1`

Casebooks + ladders (per strategy/window; B36 casebooks):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_canon_ranked__stable10__B36.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_CASEBOOK__tool_only__v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_canon_ranked__stable10__B36.md:1`

## Outcome

- Not promoted; baseline remains `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6`.

