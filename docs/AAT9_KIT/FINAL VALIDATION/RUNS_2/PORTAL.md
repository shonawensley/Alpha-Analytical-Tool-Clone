# RUNS_2 Portal (Analysis Arena Fresh-Runs Home)

Purpose: give the rebuilt Analysis Arena branch a clean, current home for
fresh runs, window studies, board receipts, validation shells, and end-of-window
analysis without mixing them into the older `RUNS/` history pile.

Key idea:

- `sharepacks/` = frozen state/day evidence
- `RUNS_2/` = current arena-era review, validation, and learning layer
- `RUNS/` = historical / legacy / control-arm comparison layer

---

## Start Here

Open these in order when running the new branch:

1. `docs/AAT9_KIT/FINAL VALIDATION/final docs/README.md`
2. `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md`
3. `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md`
4. `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md`
5. `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`
6. `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`

---

## Folder Posture

Recommended arena-era layout:

- `RUNS_2/ANALYSIS_ARENA/`
  - machine-generated daily/runtime receipts from the arena-era cadence
  - board bundle
  - board scoreboard
  - board overlay
  - shadow DPL
  - translation sandbox day manifest
  - arena-cycle receipts

- `RUNS_2/`
  - filled human review reports and daily syntheses
  - per-state Master Validation reports
  - Brain 2 Master Validation reports
  - window-level summaries
  - end-of-window deep analysis

This keeps:

- machine/runtime receipts together
- human validation shells together
- new arena-era work separate from older historical `RUNS/`

---

## Daily Arena-Era Output Set

For a fresh pre-results day, expect:

- predictive sharepack under `sharepacks/_predictive/<D>/...`
- runtime receipts under `RUNS_2/ANALYSIS_ARENA/`
- per-state translation sandbox seeds under
  `sharepacks/_predictive/<D>/<STATE>/analysis/`
- control-arm outputs inside each predictive state folder

The normal reading order is:

1. board review bundle
2. board scoreboard
3. shadow DPL
4. per-state aggregated analysis arena
5. per-state translation sandbox seed
6. Candidate Universe / Play Card as the control arm

---

## Window Posture

Recommended first arena-era study pattern:

- first run one or two older gold windows for comparison
- use at least `5+` day windows so decay and carryover can actually be studied
- then move into fresh `7-10+` day windows for stronger decay and aggregate learning

Suggested window closeout artifacts:

- window synthesis
- decay/carryover notes
- control-arm comparison rollups
- strongest board-level lessons
- `WINDOW_<...>__ANALYSIS_ARENA__PERFORMANCE_GAP.*`
- `WINDOW_<...>__ANALYSIS_ARENA__DEEP_ANALYSIS__CODEX.*`

Recommended commands:

```bash
python3 scripts/tools/create_window_performance_gap_report.py --window-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2/WINDOW_<...> --force
python3 scripts/tools/create_window_deep_analysis_report.py --window-root docs/AAT9_KIT/FINAL\ VALIDATION/RUNS_2/WINDOW_<...> --force
```

---

## Control-Arm Reminder

The current control arm still matters here, but only as comparison:

- Candidate Universe
- Play Card
- B12/B24/B36 infrastructure

Those remain useful baseline and legacy comparison surfaces.

They are not the conceptual center of the Analysis Arena branch.

---

## Legacy Note

Keep using `docs/AAT9_KIT/FINAL VALIDATION/RUNS/` for:

- old v0.2 / v0.3 historical runs
- control-arm scoreboards
- older deep-analysis material
- comparison windows against the old system

Use `RUNS_2/` for the new arena-era fresh-run phase.
