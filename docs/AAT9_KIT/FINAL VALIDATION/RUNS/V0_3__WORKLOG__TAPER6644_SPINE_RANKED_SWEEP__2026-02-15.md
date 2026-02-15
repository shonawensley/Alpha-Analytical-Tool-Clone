# Worklog — Taper6644 Spine Ranked Sweep (B36 • stable10 • tool_only) — 2026-02-15

Goal: test a within-spine conversion lever **without** changing the promoted taper6644 allocation geometry, and promote only if it improves without regressions.

Lock:
- Profile: `tool_only`
- CU posture: `stable10`
- Budget: **B36 only**
- No analyzer edits (selection-layer only)

## Strategies compared

Baseline:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644`

Candidates:
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_ranked`
- `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_canon_ranked`

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
python3 scripts/tools/create_conversion_scoreboard.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategies <BASE,C1,C2> --budgets B36 --out <OUT.md>
```

Winner lane rank sweep:
```bash
python3 scripts/tools/create_winner_lane_rank_report.py --date-from <D0> --date-to <D1> --sharepacks-root sharepacks/_predictive --profile tool_only --experiment-tag stable10 --strategies <BASE,C1,C2> --budget B36 --out-csv <OUT.csv> --out-md <OUT.md>
```

Lane allocation:
```bash
python3 scripts/tools/create_lane_allocation_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --strategy <STRAT> --budget B36 --label SPINECAP6_TAPER6644_SPINE_RANKED_SWEEP
```

Geometry invariants:
```bash
python3 scripts/tools/create_play_card_geometry_invariants_report.py --date-from <D0> --date-to <D1> --profile tool_only --experiment-tag stable10 --roster-strategy <BASELINE_STRAT> --baseline-strategy <BASELINE_STRAT> --strategies <BASE,C1,C2> --budget B36 --label SPINECAP6_TAPER6644_SPINE_RANKED_SWEEP
```

## Outputs written (key)

Morning brief (decision):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__MORNING_BRIEF__TAPER6644_SPINE_RANKED_SWEEP__2026-02-15.md:1`

Scoreboards (Jan + OOS):
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6644_SPINE_RANKED_SWEEP.md:1`
- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINECAP6_TAPER6644_SPINE_RANKED_SWEEP.md:1`

## Outcome

- Not promoted (no measurable isolation gain; Jan strict regressed).
- Default remains: `v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644`

