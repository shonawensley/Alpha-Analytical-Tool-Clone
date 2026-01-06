# Aux Summary — Virginia4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/Virginia4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Virginia
- combined: live=`data/cleaned/draws/Virginia_draws.csv` snap=`sharepacks/2026-01-04/Virginia4/aux/draws/Virginia_draws.csv` n=1000 head=976, 432, 765, 184, 354
- midday: live=`data/cleaned/draws/Virginia_Midday_draws.csv` snap=`sharepacks/2026-01-04/Virginia4/aux/draws/Virginia_Midday_draws.csv` n=1000 head=432, 184, 019, 686, 888
- evening: live=`data/cleaned/draws/Virginia_Evening_draws.csv` snap=`sharepacks/2026-01-04/Virginia4/aux/draws/Virginia_Evening_draws.csv` n=1000 head=976, 765, 354, 636, 100

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=7 last_repeat_index=18

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=25), P2:9 (gap=23), P3:1 (gap=30)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 591: score=51.215405714285716 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 597: score=50.813406785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 593: score=43.98658107142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 291: score=42.772526071428565 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 541: score=40.08708035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 297: score=39.97437142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 547: score=39.68508142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 599: score=37.816207142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=36.91710714285715 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 561: score=36.85725 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=905 sev=B
- 125: ds=900 sev=B
- 677: ds=888 sev=B
- 688: ds=849 sev=B
- 119: ds=808 sev=B
- 344: ds=687 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=111 sev=red
  - 11: ds=55 sev=purple
  - 77: ds=50 sev=purple
  - 44: ds=49 sev=purple
  - 22: ds=18 sev=-
  - 55: ds=13 sev=-
  - 33: ds=10 sev=-
  - 88: ds=9 sev=-
  - 00: ds=8 sev=-
  - 66: ds=6 sev=-
- non_repeating:
  - 16: ds=63 sev=red
  - 37: ds=56 sev=red
  - 26: ds=54 sev=blue
  - 59: ds=47 sev=blue
  - 03: ds=41 sev=blue
  - 07: ds=36 sev=purple
  - 38: ds=32 sev=purple
  - 12: ds=30 sev=purple
  - 13: ds=30 sev=purple
  - 17: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:277, 26:194, 34:142, 23:140, 6:116, 15:112, 16:95, 11:78, 17:73, 32:71

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=277 fs=1 fl=1 hz=0.006147540983606558, 26:ds=194 fs=4 fl=0 hz=0.009174311926605505, 34:ds=142 fs=18 fl=2 hz=0.023640661938534282, 23:ds=140 fs=15 fl=3 hz=0.024965325936199722, 6:ds=116 fs=16 fl=3 hz=0.02186421173762946, 15:ds=112 fs=16 fl=2 hz=0.022058823529411763, 16:ds=95 fs=8 fl=0 hz=0.011335012594458438, 11:ds=78 fs=50 fl=0 hz=0.05820721769499418, 17:ds=73 fs=24 fl=1 hz=0.027085590465872156, 32:ds=71 fs=1 fl=3 hz=0.006764374295377677

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S8: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=44 flags=purple
- S4: ds=41 flags=purple
- S5: ds=31 flags=purple
- S16: ds=27 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=8 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=34), P2:6 (gap=34), P3:3 (gap=20)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 591: score=51.215405714285716 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 597: score=50.813406785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 593: score=43.98658107142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 291: score=42.772526071428565 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 541: score=40.08708035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 297: score=39.97437142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 547: score=39.68508142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 599: score=37.816207142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=36.91710714285715 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 561: score=36.85725 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=990 sev=B
- 338: ds=930 sev=B
- 223: ds=929 sev=B
- 377: ds=914 sev=B
- 677: ds=899 sev=B
- 125: ds=880 sev=B
- 699: ds=844 sev=B
- 356: ds=841 sev=B
- 278: ds=808 sev=B
- 179: ds=744 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=94 sev=blue
  - 99: ds=55 sev=purple
  - 77: ds=45 sev=purple
  - 11: ds=27 sev=purple
  - 44: ds=24 sev=-
  - 22: ds=15 sev=-
  - 00: ds=9 sev=-
  - 55: ds=6 sev=-
  - 88: ds=4 sev=-
  - 66: ds=3 sev=-
- non_repeating:
  - 26: ds=74 sev=red
  - 39: ds=58 sev=red
  - 46: ds=42 sev=blue
  - 35: ds=40 sev=blue
  - 38: ds=35 sev=purple
  - 37: ds=34 sev=purple
  - 16: ds=31 sev=purple
  - 06: ds=28 sev=purple
  - 36: ds=28 sev=purple
  - 07: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:148, 35:138, 26:125, 29:120, 25:95, 23:94, 6:85, 11:69, 33:68, 13:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=148 fs=18 fl=2 hz=0.023752969121140142, 35:ds=138 fs=2 fl=1 hz=0.007396449704142012, 26:ds=125 fs=4 fl=1 hz=0.01046337817638266, 29:ds=120 fs=24 fl=1 hz=0.02965599051008304, 25:ds=95 fs=12 fl=3 hz=0.018270401948842874, 23:ds=94 fs=20 fl=1 hz=0.02648171500630517, 6:ds=85 fs=14 fl=1 hz=0.018411967779056387, 11:ds=69 fs=44 fl=0 hz=0.04878048780487805, 33:ds=68 fs=15 fl=2 hz=0.018743109151047408, 13:ds=59 fs=22 fl=2 hz=0.02666666666666667

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=92 flags=red+purple
- S25: ds=82 flags=purple
- S21: ds=46 flags=red+purple
- S23: ds=45 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 057: score=3 tags=FLT,RS
  - 147: score=3 tags=FLT,RS
  - 156: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 579: score=3 tags=FLT,RS
  - 678: score=3 tags=FLT,RS
  - 012: score=2 tags=RS
  - 039: score=2 tags=RS
  - 048: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=4 last_repeat_gap=26 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=45), P2:1 (gap=47), P3:9 (gap=34)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=45), P2:1 (ds=47)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 591: score=51.215405714285716 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 597: score=50.813406785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 593: score=43.98658107142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 291: score=42.772526071428565 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 541: score=40.08708035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 297: score=39.97437142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 547: score=39.68508142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 599: score=37.816207142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=36.91710714285715 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 561: score=36.85725 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 118: ds=826 sev=B
- 122: ds=810 sev=B
- 244: ds=807 sev=B
- 005: ds=785 sev=B
- 888: ds=772 sev=B
- 999: ds=768 sev=B
- 445: ds=747 sev=B
- 344: ds=740 sev=B
- 003: ds=724 sev=B
- 558: ds=699 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=130 sev=red
  - 99: ds=77 sev=blue
  - 11: ds=75 sev=blue
  - 44: ds=32 sev=purple
  - 77: ds=25 sev=purple
  - 88: ds=12 sev=-
  - 22: ds=9 sev=-
  - 33: ds=5 sev=-
  - 00: ds=4 sev=-
  - 66: ds=3 sev=-
- non_repeating:
  - 89: ds=62 sev=red
  - 16: ds=57 sev=red
  - 59: ds=56 sev=red
  - 17: ds=47 sev=blue
  - 03: ds=38 sev=blue
  - 25: ds=37 sev=blue
  - 09: ds=34 sev=purple
  - 37: ds=28 sev=purple
  - 26: ds=27 sev=purple
  - 47: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:261, 35:164, 5:146, 32:142, 20:115, 31:98, 26:97, 16:89, 34:71, 23:70

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=261 fs=4 fl=0 hz=0.007987220447284345, 35:ds=164 fs=1 fl=1 hz=0.005050505050505051, 5:ds=146 fs=19 fl=1 hz=0.024242424242424242, 32:ds=142 fs=5 fl=2 hz=0.012987012987012988, 20:ds=115 fs=15 fl=2 hz=0.0215311004784689, 31:ds=98 fs=24 fl=2 hz=0.02888888888888889, 26:ds=97 fs=0 fl=0 hz=0.0, 16:ds=89 fs=5 fl=1 hz=0.009234828496042216, 34:ds=71 fs=27 fl=0 hz=0.03082191780821918, 23:ds=70 fs=18 fl=1 hz=0.022522522522522525

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=80 flags=purple
- S3: ds=75 flags=blue+purple
- S5: ds=60 flags=purple
- S20: ds=39 flags=purple

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
- 125 -> combined:900(B); midday:880(B)
- 344 -> combined:687(B); evening:740(B)
- 677 -> combined:888(B); midday:899(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:41(blue); evening:38(blue)
- 07 -> combined:36(purple); midday:26(purple)
- 11 -> combined:55(purple); evening:75(blue); midday:27(purple)
- 16 -> combined:63(red); evening:57(red); midday:31(purple)
- 17 -> combined:27(purple); evening:47(blue)
- 25 -> combined:25(purple); evening:37(blue)
- 26 -> combined:54(blue); evening:27(purple); midday:74(red)
- 37 -> combined:56(red); evening:28(purple); midday:34(purple)
- 38 -> combined:32(purple); midday:35(purple)
- 44 -> combined:49(purple); evening:32(purple)
- 59 -> combined:47(blue); evening:56(red)
- 77 -> combined:50(purple); evening:25(purple); midday:45(purple)
- 99 -> combined:111(red); evening:77(blue); midday:55(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(7.781514285714286)[R1,XVAR-Cons(CEM)], 2(2.6137928571428573)[R2,XVAR-Cons(CM)], 3(1.685142857142857)[R1,Double-Pressure], 8(1.6616428571428572)[R3,XVAR-Cons(CE)], 4(0.9299)[R2,Double-Pressure]
- P2: 9(6.81955)[R1,Mirror-Echo], 1(1.7449999999999999)[R1,Double-Pressure], 6(1.685142857142857)[R1,Double-Pressure], 4(1.4905714285714284)[R2,Mirror-Echo], 7(0.9925999999999999)[R2,Double-Pressure]
- P3: 1(6.890592857142857)[R1,XVAR-Cons(CEM)], 7(6.541028571428571)[R2,XVAR-Cons(CEM)], 3(2.7785714285714285)[R3,XVAR-Cons(CM)], 9(1.715142857142857)[R1,Double-Pressure]
