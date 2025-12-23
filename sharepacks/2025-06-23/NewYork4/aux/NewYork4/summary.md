# Aux Summary — NewYork4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/NewYork4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: New York
- combined: live=`data/cleaned/draws/New_York_draws.csv` snap=`sharepacks/2025-06-23/NewYork4/aux/draws/New_York_draws.csv` n=1000 head=968, 202, 602, 802, 308
- midday: live=`data/cleaned/draws/New_York_Midday_draws.csv` snap=`sharepacks/2025-06-23/NewYork4/aux/draws/New_York_Midday_draws.csv` n=1000 head=202, 802, 573, 255, 878
- evening: live=`data/cleaned/draws/New_York_Evening_draws.csv` snap=`sharepacks/2025-06-23/NewYork4/aux/draws/New_York_Evening_draws.csv` n=1000 head=968, 602, 308, 520, 610

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=7 last_repeat_index=3

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=38), P2:4 (gap=22), P3:7 (gap=33)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 447: score=51.15776607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 497: score=45.97556357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 446: score=42.1087625 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 047: score=41.15801428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 437: score=41.11037857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 449: score=40.43868214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 747: score=39.7285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 457: score=37.23009285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 496: score=36.92656 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 477: score=36.91972142857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 189: ds=724 sev=B
- 014: ds=719 sev=B
- 228: ds=704 sev=B
- 477: ds=694 sev=B
- 113: ds=687 sev=B
- 888: ds=677 sev=B
- 999: ds=669 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=55 sev=purple
  - 77: ds=42 sev=purple
  - 33: ds=34 sev=purple
  - 99: ds=30 sev=purple
  - 66: ds=21 sev=-
  - 00: ds=19 sev=-
  - 11: ds=11 sev=-
  - 88: ds=9 sev=-
  - 55: ds=7 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 56: ds=97 sev=red
  - 18: ds=69 sev=red
  - 15: ds=43 sev=blue
  - 45: ds=43 sev=blue
  - 39: ds=41 sev=blue
  - 24: ds=39 sev=blue
  - 59: ds=37 sev=blue
  - 17: ds=36 sev=purple
  - 04: ds=35 sev=purple
  - 07: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:164, 32:116, 16:84, 23:69, 5:63, 4:60, 20:59, 19:58, 33:57, 28:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=164 fs=4 fl=1 hz=0.008086253369272238, 32:ds=116 fs=3 fl=3 hz=0.007972665148063782, 16:ds=84 fs=3 fl=1 hz=0.005868544600938967, 23:ds=69 fs=19 fl=2 hz=0.02354260089686099, 5:ds=63 fs=22 fl=1 hz=0.02505446623093682, 4:ds=60 fs=24 fl=0 hz=0.030808729139922976, 20:ds=59 fs=19 fl=1 hz=0.02450980392156863, 19:ds=58 fs=19 fl=0 hz=0.024906600249066005, 33:ds=57 fs=23 fl=2 hz=0.02682403433476395, 28:ds=52 fs=16 fl=3 hz=0.02062975027144408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=92 flags=purple
- S22: ds=82 flags=purple
- S24: ds=79 flags=purple
- S6: ds=48 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 027: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 126: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 189: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 279: score=3 tags=FLT,RS
  - 378: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=2 last_repeat_gap=2 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=34), P2:3 (gap=20), P3:7 (gap=16)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 447: score=51.15776607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 497: score=45.97556357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 446: score=42.1087625 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 047: score=41.15801428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 437: score=41.11037857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 449: score=40.43868214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 747: score=39.7285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 457: score=37.23009285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 496: score=36.92656 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 477: score=36.91972142857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 477: ds=982 sev=B
- 666: ds=960 sev=B
- 066: ds=958 sev=B
- 444: ds=924 sev=B
- 166: ds=877 sev=B
- 344: ds=827 sev=B
- 001: ds=803 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=101 sev=blue
  - 99: ds=84 sev=blue
  - 44: ds=27 sev=purple
  - 33: ds=25 sev=purple
  - 66: ds=10 sev=-
  - 00: ds=9 sev=-
  - 11: ds=5 sev=-
  - 88: ds=4 sev=-
  - 55: ds=3 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 16: ds=60 sev=red
  - 06: ds=53 sev=blue
  - 56: ds=48 sev=blue
  - 13: ds=43 sev=blue
  - 03: ds=40 sev=blue
  - 18: ds=34 sev=purple
  - 17: ds=32 sev=purple
  - 07: ds=30 sev=purple
  - 27: ds=29 sev=purple
  - 38: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:415, 35:175, 26:147, 27:128, 6:98, 28:95, 4:91, 19:73, 16:70, 2:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=415 fs=0 fl=0 hz=0.0, 35:ds=175 fs=3 fl=2 hz=0.008075370121130552, 26:ds=147 fs=1 fl=0 hz=0.0038809831824062092, 27:ds=128 fs=19 fl=2 hz=0.02573529411764706, 6:ds=98 fs=18 fl=2 hz=0.022779043280182234, 28:ds=95 fs=17 fl=2 hz=0.021420518602029315, 4:ds=91 fs=30 fl=0 hz=0.037267080745341616, 19:ds=73 fs=25 fl=1 hz=0.030373831775700938, 16:ds=70 fs=4 fl=0 hz=0.006195786864931846, 2:ds=47 fs=20 fl=2 hz=0.02328042328042328

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=58 flags=blue+purple
- S22: ds=52 flags=purple
- S14: ds=49 flags=red+purple
- S6: ds=47 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '6', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=14 last_repeat_index=8

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=23), P2:5 (gap=24), P3:7 (gap=26)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 447: score=51.15776607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 497: score=45.97556357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 446: score=42.1087625 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 047: score=41.15801428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 437: score=41.11037857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 449: score=40.43868214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 747: score=39.7285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 457: score=37.23009285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 496: score=36.92656 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 477: score=36.91972142857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 169: ds=976 sev=B
- 355: ds=931 sev=B
- 358: ds=926 sev=B
- 666: ds=894 sev=B
- 011: ds=858 sev=B
- 566: ds=782 sev=B
- 446: ds=781 sev=B
- 113: ds=761 sev=B
- 039: ds=672 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=82 sev=blue
  - 00: ds=61 sev=purple
  - 11: ds=42 sev=purple
  - 22: ds=36 sev=purple
  - 66: ds=29 sev=purple
  - 55: ds=27 sev=purple
  - 88: ds=23 sev=-
  - 77: ds=21 sev=-
  - 33: ds=17 sev=-
  - 99: ds=15 sev=-
- non_repeating:
  - 18: ds=64 sev=red
  - 45: ds=52 sev=blue
  - 56: ds=50 sev=blue
  - 59: ds=43 sev=blue
  - 39: ds=34 sev=purple
  - 04: ds=33 sev=purple
  - 58: ds=30 sev=purple
  - 48: ds=25 sev=purple
  - 15: ds=24 sev=-
  - 78: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 15:164, 20:126, 14:124, 29:92, 35:82, 18:62, 32:58, 33:54, 34:49, 5:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 15:ds=164 fs=29 fl=0 hz=0.037613488975356685, 20:ds=126 fs=18 fl=1 hz=0.0247074122236671, 14:ds=124 fs=40 fl=0 hz=0.04581901489117984, 29:ds=92 fs=22 fl=0 hz=0.02756892230576441, 35:ds=82 fs=5 fl=3 hz=0.010238907849829351, 18:ds=62 fs=16 fl=1 hz=0.019522776572668113, 32:ds=58 fs=6 fl=1 hz=0.009944751381215469, 33:ds=54 fs=15 fl=4 hz=0.020364415862808145, 34:ds=49 fs=19 fl=0 hz=0.022988505747126436, 5:ds=43 fs=29 fl=0 hz=0.03068783068783069

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=72 flags=purple
- S5: ds=66 flags=purple
- S3: ds=46 flags=purple
- S22: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 113 -> combined:687(B); evening:761(B)
- 477 -> combined:694(B); midday:982(B)
- 666 -> evening:894(B); midday:960(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 04 -> combined:35(purple); evening:33(purple)
- 07 -> combined:32(purple); midday:30(purple)
- 17 -> combined:36(purple); midday:32(purple)
- 18 -> combined:69(red); evening:64(red); midday:34(purple)
- 33 -> combined:34(purple); midday:25(purple)
- 39 -> combined:41(blue); evening:34(purple)
- 44 -> combined:55(purple); evening:82(blue); midday:27(purple)
- 45 -> combined:43(blue); evening:52(blue)
- 56 -> combined:97(red); evening:50(blue); midday:48(blue)
- 59 -> combined:37(blue); evening:43(blue)
- 77 -> combined:42(purple); midday:101(blue)
- 99 -> combined:30(purple); midday:84(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(7.152378571428572)[R1,XVAR-Cons(CEM)], 0(2.8688571428571428)[R3,XVAR-Cons(CE)], 1(1.615142857142857)[R1,Double-Pressure], 3(1.2225)[R2,Double-Pressure], 7(1.14)[R2,Double-Pressure]
- P2: 4(6.098014285714286)[R1,Mirror-Echo], 9(3.7656642857142852)[R2,Mirror-Echo], 3(2.766857142857143)[R3,XVAR-Cons(CM)], 5(1.3865714285714286)[R1,Double-Pressure], 7(1.0761999999999998)[R2,Double-Pressure]
- P3: 7(8.191142857142857)[R1,XVAR-Cons(CEM)], 6(2.4963571428571427)[R2,XVAR-Cons(CM)], 9(1.9136785714285716)[R3,XVAR-Cons(CE)], 0(0.9417)[R2,Double-Pressure], 5(0.9343999999999999)[R2,Double-Pressure]
