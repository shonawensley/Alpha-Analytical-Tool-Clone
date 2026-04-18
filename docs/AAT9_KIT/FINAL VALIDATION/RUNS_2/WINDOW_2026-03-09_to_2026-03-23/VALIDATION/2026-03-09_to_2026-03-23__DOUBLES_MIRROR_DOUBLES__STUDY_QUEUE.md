# Doubles + Mirror-Doubles — Study Queue (Index Hit → Box Miss)

- Generated: `2026-04-16T23:39:06.692348+00:00`
- Source: `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_2026-03-09_to_2026-03-23/VALIDATION/2026-03-09_to_2026-03-23__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv`

Purpose: review **mirror-double** events where the predictive **Candidate Universe hit the VTRAC/index lane** (`cu_index_hit=True`) but **missed the exact box** (`cu_box_hit=False`).
These are the highest-leverage examples for designing **bounded closure packs** that convert “lane hits” into “box hits” without changing analyzers.

How to use each row:
- Open the deep-dive section (line pointer) for winners-lens Set1 col1/2 samples + evidence paths.
- Open the Master Validation run report for the full post-results analysis context.
- Open the predictive artifacts for the same day/state (`candidate_universe.json`, `play_card.json`) to see what we actually played pre-results.

| Rank | Date | State | Period | Winner | Canon | MirrorPair | VTRAC idx | WL family cells | WL winner cells | WL vt-straight cells | Best CU index method | Play idx hit | Deep dive | Run report | Predictive CU | Predictive Play Card |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
