# Stage 2 Cross-Window Readiness

Purpose: prevent overfitting March by identifying which older windows can receive the same Stage 2 / Stage 2B treatment.

- `WINDOW_2025-12-30_to_2026-01-09`: scoreboards=`11`, manifests=`11`, stage2_ready=`True`, stage2b_ready=`True`, action=Ready for cross-window rollup
- `WINDOW_2026-01-15_to_2026-01-18`: scoreboards=`4`, manifests=`4`, stage2_ready=`True`, stage2b_ready=`True`, action=Ready for cross-window rollup
- `WINDOW_2026-01-20_to_2026-01-22`: scoreboards=`3`, manifests=`3`, stage2_ready=`True`, stage2b_ready=`False`, action=Already current Stage 2B baseline
