# Stage 2 Cross-Window Readiness

Purpose: prevent overfitting March by identifying which older windows can receive the same Stage 2 / Stage 2B treatment.

- `WINDOW_2025-12-30_to_2026-01-04`: scoreboards=`6`, manifests=`6`, stage2_ready=`True`, stage2b_ready=`False`, action=Already current Stage 2B baseline
- `WINDOW_2026-01-05_to_2026-01-09`: scoreboards=`5`, manifests=`5`, stage2_ready=`True`, stage2b_ready=`False`, action=Run Stage 2 then Stage 2B
- `WINDOW_2026-01-15_to_2026-01-18`: scoreboards=`4`, manifests=`4`, stage2_ready=`True`, stage2b_ready=`False`, action=Run Stage 2 then Stage 2B
- `WINDOW_2026-01-15_to_2026-01-22`: scoreboards=`8`, manifests=`8`, stage2_ready=`True`, stage2b_ready=`False`, action=Run Stage 2 then Stage 2B
- `WINDOW_2026-03-09_to_2026-03-23`: scoreboards=`15`, manifests=`15`, stage2_ready=`True`, stage2b_ready=`True`, action=Backfill missing window artifacts
