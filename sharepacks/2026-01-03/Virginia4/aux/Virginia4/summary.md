# Aux Summary — Virginia4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/Virginia4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Virginia
- combined: live=`data/cleaned/draws/Virginia_draws.csv` snap=`sharepacks/2026-01-03/Virginia4/aux/draws/Virginia_draws.csv` n=1000 head=765, 184, 354, 019, 636
- midday: live=`data/cleaned/draws/Virginia_Midday_draws.csv` snap=`sharepacks/2026-01-03/Virginia4/aux/draws/Virginia_Midday_draws.csv` n=1000 head=184, 019, 686, 888, 908
- evening: live=`data/cleaned/draws/Virginia_Evening_draws.csv` snap=`sharepacks/2026-01-03/Virginia4/aux/draws/Virginia_Evening_draws.csv` n=1000 head=765, 354, 636, 100, 933

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=5 last_repeat_index=18

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=23), P2:7 (gap=27), P3:1 (gap=28)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 597: score=45.6602675 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 591: score=44.887795 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 571: score=43.25655178571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 577: score=41.41654285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 517: score=37.53830714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 567: score=37.448592857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 537: score=37.02760714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=36.736157142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 561: score=36.64644285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 547: score=36.37202142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=903 sev=B
- 125: ds=898 sev=B
- 677: ds=886 sev=B
- 688: ds=847 sev=B
- 119: ds=806 sev=B
- 344: ds=685 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=109 sev=red
  - 11: ds=53 sev=purple
  - 77: ds=48 sev=purple
  - 44: ds=47 sev=purple
  - 22: ds=16 sev=-
  - 55: ds=11 sev=-
  - 33: ds=8 sev=-
  - 88: ds=7 sev=-
  - 00: ds=6 sev=-
  - 66: ds=4 sev=-
- non_repeating:
  - 16: ds=61 sev=red
  - 37: ds=54 sev=blue
  - 26: ds=52 sev=blue
  - 59: ds=45 sev=blue
  - 69: ds=45 sev=blue
  - 03: ds=39 sev=blue
  - 07: ds=34 sev=purple
  - 38: ds=30 sev=purple
  - 12: ds=28 sev=purple
  - 13: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:275, 26:192, 34:140, 23:138, 6:114, 15:110, 16:93, 11:76, 17:71, 32:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=275 fs=1 fl=1 hz=0.006147540983606558, 26:ds=192 fs=4 fl=0 hz=0.009174311926605505, 34:ds=140 fs=18 fl=2 hz=0.023640661938534282, 23:ds=138 fs=15 fl=3 hz=0.024965325936199722, 6:ds=114 fs=16 fl=3 hz=0.02186421173762946, 15:ds=110 fs=16 fl=2 hz=0.022058823529411763, 16:ds=93 fs=8 fl=0 hz=0.011335012594458438, 11:ds=76 fs=51 fl=0 hz=0.0552546045503792, 17:ds=71 fs=24 fl=1 hz=0.027085590465872156, 32:ds=69 fs=1 fl=3 hz=0.006764374295377677

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S8: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=42 flags=purple
- S4: ds=39 flags=purple
- S9: ds=32 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 123: score=1 tags=FLT
  - 124: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=7 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=33), P2:6 (gap=33), P3:3 (gap=19)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 597: score=45.6602675 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 591: score=44.887795 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 571: score=43.25655178571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 577: score=41.41654285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 517: score=37.53830714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 567: score=37.448592857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 537: score=37.02760714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=36.736157142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 561: score=36.64644285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 547: score=36.37202142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=989 sev=B
- 338: ds=929 sev=B
- 223: ds=928 sev=B
- 377: ds=913 sev=B
- 677: ds=898 sev=B
- 125: ds=879 sev=B
- 699: ds=843 sev=B
- 356: ds=840 sev=B
- 278: ds=807 sev=B
- 179: ds=743 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=93 sev=blue
  - 99: ds=54 sev=purple
  - 77: ds=44 sev=purple
  - 11: ds=26 sev=purple
  - 44: ds=23 sev=-
  - 22: ds=14 sev=-
  - 00: ds=8 sev=-
  - 55: ds=5 sev=-
  - 88: ds=3 sev=-
  - 66: ds=2 sev=-
- non_repeating:
  - 26: ds=73 sev=red
  - 39: ds=57 sev=red
  - 23: ds=51 sev=blue
  - 46: ds=41 sev=blue
  - 35: ds=39 sev=blue
  - 34: ds=36 sev=purple
  - 38: ds=34 sev=purple
  - 37: ds=33 sev=purple
  - 16: ds=30 sev=purple
  - 06: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:147, 35:137, 26:124, 29:119, 25:94, 23:93, 6:84, 11:68, 33:67, 13:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=147 fs=18 fl=2 hz=0.023752969121140142, 35:ds=137 fs=2 fl=1 hz=0.007396449704142012, 26:ds=124 fs=4 fl=1 hz=0.01046337817638266, 29:ds=119 fs=24 fl=1 hz=0.02965599051008304, 25:ds=94 fs=12 fl=3 hz=0.018270401948842874, 23:ds=93 fs=20 fl=1 hz=0.02648171500630517, 6:ds=84 fs=14 fl=1 hz=0.018411967779056387, 11:ds=68 fs=44 fl=0 hz=0.04878048780487805, 33:ds=67 fs=15 fl=2 hz=0.018743109151047408, 13:ds=58 fs=22 fl=2 hz=0.02666666666666667

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=91 flags=red+purple
- S25: ds=81 flags=purple
- S21: ds=45 flags=red+purple
- S23: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '3', '5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=3 tags=FLT,RS
  - 039: score=3 tags=FLT,RS
  - 057: score=3 tags=FLT,RS
  - 129: score=3 tags=FLT,RS
  - 138: score=3 tags=FLT,RS
  - 147: score=3 tags=FLT,RS
  - 156: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=4 last_repeat_gap=25 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=44), P2:1 (gap=46), P3:9 (gap=33)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=44), P2:1 (ds=46)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 597: score=45.6602675 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 591: score=44.887795 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 571: score=43.25655178571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 577: score=41.41654285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 517: score=37.53830714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 567: score=37.448592857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 537: score=37.02760714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=36.736157142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 561: score=36.64644285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 547: score=36.37202142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 118: ds=825 sev=B
- 122: ds=809 sev=B
- 244: ds=806 sev=B
- 005: ds=784 sev=B
- 888: ds=771 sev=B
- 999: ds=767 sev=B
- 445: ds=746 sev=B
- 344: ds=739 sev=B
- 003: ds=723 sev=B
- 558: ds=698 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=129 sev=red
  - 99: ds=76 sev=blue
  - 11: ds=74 sev=blue
  - 44: ds=31 sev=purple
  - 77: ds=24 sev=-
  - 88: ds=11 sev=-
  - 22: ds=8 sev=-
  - 33: ds=4 sev=-
  - 00: ds=3 sev=-
  - 66: ds=2 sev=-
- non_repeating:
  - 89: ds=61 sev=red
  - 16: ds=56 sev=red
  - 59: ds=55 sev=blue
  - 69: ds=53 sev=blue
  - 79: ds=47 sev=blue
  - 17: ds=46 sev=blue
  - 03: ds=37 sev=blue
  - 25: ds=36 sev=purple
  - 09: ds=33 sev=purple
  - 37: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:260, 35:163, 5:145, 32:141, 20:114, 22:103, 31:97, 26:96, 16:88, 34:70

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=260 fs=4 fl=0 hz=0.007987220447284345, 35:ds=163 fs=1 fl=1 hz=0.005050505050505051, 5:ds=145 fs=19 fl=1 hz=0.024242424242424242, 32:ds=141 fs=5 fl=2 hz=0.012987012987012988, 20:ds=114 fs=15 fl=2 hz=0.0215311004784689, 22:ds=103 fs=45 fl=0 hz=0.05022321428571429, 31:ds=97 fs=24 fl=2 hz=0.02888888888888889, 26:ds=96 fs=0 fl=0 hz=0.0, 16:ds=88 fs=5 fl=1 hz=0.009234828496042216, 34:ds=70 fs=27 fl=0 hz=0.03082191780821918

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=79 flags=purple
- S3: ds=74 flags=blue+purple
- S5: ds=59 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 038: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 125 -> combined:898(B); midday:879(B)
- 344 -> combined:685(B); evening:739(B)
- 677 -> combined:886(B); midday:898(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:39(blue); evening:37(blue)
- 07 -> combined:34(purple); midday:25(purple)
- 11 -> combined:53(purple); evening:74(blue); midday:26(purple)
- 16 -> combined:61(red); evening:56(red); midday:30(purple)
- 17 -> combined:25(purple); evening:46(blue)
- 26 -> combined:52(blue); evening:26(purple); midday:73(red)
- 37 -> combined:54(blue); evening:27(purple); midday:33(purple)
- 38 -> combined:30(purple); midday:34(purple)
- 44 -> combined:47(purple); evening:31(purple)
- 59 -> combined:45(blue); evening:55(blue)
- 69 -> combined:45(blue); evening:53(blue)
- 77 -> combined:48(purple); midday:44(purple)
- 99 -> combined:109(red); evening:76(blue); midday:54(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(7.697757142857142)[R1,XVAR-Cons(CEM)], 2(2.526357142857143)[R2,XVAR-Cons(CM)], 4(2.4628571428571426)[R3,XVAR-Cons(CE)], 3(1.6552857142857142)[R1,Double-Pressure], 8(0.19092142857142858)[R3,Swap]
- P2: 9(3.672142857142857)[R2,Mirror-Echo], 7(3.1232357142857143)[R1,XVAR-Cons(CM)], 1(1.7449999999999999)[R1,Double-Pressure], 6(1.6552857142857142)[R1,Double-Pressure], 3(1.2343)[R2,Double-Pressure]
- P3: 1(6.7934)[R1,XVAR-Cons(CEM)], 7(6.595549999999999)[R2,Mirror-Echo], 9(1.6852857142857143)[R1,Double-Pressure], 3(1.2372857142857143)[R1,Double-Pressure], 2(0.5262857142857142)[R3,Mirror-Echo]
