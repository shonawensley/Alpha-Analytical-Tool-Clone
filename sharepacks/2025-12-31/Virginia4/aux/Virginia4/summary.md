# Aux Summary — Virginia4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/Virginia4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Virginia
- combined: live=`data/cleaned/draws/Virginia_draws.csv` snap=`sharepacks/2025-12-31/Virginia4/aux/draws/Virginia_draws.csv` n=1000 head=100, 888, 933, 908, 658
- midday: live=`data/cleaned/draws/Virginia_Midday_draws.csv` snap=`sharepacks/2025-12-31/Virginia4/aux/draws/Virginia_Midday_draws.csv` n=1000 head=888, 908, 055, 428, 829
- evening: live=`data/cleaned/draws/Virginia_Evening_draws.csv` snap=`sharepacks/2025-12-31/Virginia4/aux/draws/Virginia_Evening_draws.csv` n=1000 head=100, 933, 658, 604, 060

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=28 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=22), P2:7 (gap=21), P3:1 (gap=22)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=41.29525714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 371: score=40.02661428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 391: score=39.7697 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 361: score=36.22797142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 331: score=35.83385714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=35.609321428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 317: score=34.484564285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 571: score=34.34067857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 381: score=33.917228571428566 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 377: score=33.21592142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=897 sev=B
- 125: ds=892 sev=B
- 677: ds=880 sev=B
- 688: ds=841 sev=B
- 119: ds=800 sev=B
- 344: ds=679 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=103 sev=blue
  - 11: ds=47 sev=purple
  - 77: ds=42 sev=purple
  - 44: ds=41 sev=purple
  - 66: ds=20 sev=-
  - 22: ds=10 sev=-
  - 55: ds=5 sev=-
  - 33: ds=2 sev=-
  - 88: ds=1 sev=-
  - 00: ds=0 sev=-
- non_repeating:
  - 16: ds=55 sev=blue
  - 37: ds=48 sev=blue
  - 26: ds=46 sev=blue
  - 36: ds=46 sev=blue
  - 59: ds=39 sev=blue
  - 69: ds=39 sev=blue
  - 14: ds=34 sev=purple
  - 19: ds=34 sev=purple
  - 03: ds=33 sev=purple
  - 45: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:269, 26:186, 34:134, 23:132, 18:113, 6:108, 15:104, 24:94, 16:87, 11:70

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=269 fs=1 fl=1 hz=0.006147540983606558, 26:ds=186 fs=4 fl=0 hz=0.009174311926605505, 34:ds=134 fs=18 fl=2 hz=0.023640661938534282, 23:ds=132 fs=15 fl=3 hz=0.024965325936199722, 18:ds=113 fs=19 fl=2 hz=0.023836549375709424, 6:ds=108 fs=16 fl=3 hz=0.02186421173762946, 15:ds=104 fs=16 fl=2 hz=0.022058823529411763, 24:ds=94 fs=45 fl=1 hz=0.05082872928176795, 16:ds=87 fs=8 fl=0 hz=0.011335012594458438, 11:ds=70 fs=51 fl=0 hz=0.0552546045503792

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S8: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=36 flags=blue+purple
- S4: ds=33 flags=purple
- S9: ds=26 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=4 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=30), P2:6 (gap=30), P3:3 (gap=16)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=41.29525714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 371: score=40.02661428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 391: score=39.7697 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 361: score=36.22797142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 331: score=35.83385714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=35.609321428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 317: score=34.484564285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 571: score=34.34067857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 381: score=33.917228571428566 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 377: score=33.21592142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=986 sev=B
- 338: ds=926 sev=B
- 223: ds=925 sev=B
- 377: ds=910 sev=B
- 677: ds=895 sev=B
- 125: ds=876 sev=B
- 699: ds=840 sev=B
- 356: ds=837 sev=B
- 278: ds=804 sev=B
- 179: ds=740 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=90 sev=blue
  - 99: ds=51 sev=purple
  - 66: ds=42 sev=purple
  - 77: ds=41 sev=purple
  - 11: ds=23 sev=-
  - 44: ds=20 sev=-
  - 22: ds=11 sev=-
  - 00: ds=5 sev=-
  - 55: ds=2 sev=-
  - 88: ds=0 sev=-
- non_repeating:
  - 26: ds=70 sev=red
  - 39: ds=54 sev=blue
  - 68: ds=49 sev=blue
  - 23: ds=48 sev=blue
  - 46: ds=38 sev=blue
  - 35: ds=36 sev=purple
  - 34: ds=33 sev=purple
  - 38: ds=31 sev=purple
  - 37: ds=30 sev=purple
  - 16: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:144, 35:134, 26:121, 29:116, 25:91, 23:90, 6:81, 11:65, 33:64, 18:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=144 fs=18 fl=2 hz=0.023752969121140142, 35:ds=134 fs=2 fl=1 hz=0.007396449704142012, 26:ds=121 fs=4 fl=1 hz=0.01046337817638266, 29:ds=116 fs=24 fl=1 hz=0.02965599051008304, 25:ds=91 fs=12 fl=3 hz=0.018270401948842874, 23:ds=90 fs=20 fl=1 hz=0.02648171500630517, 6:ds=81 fs=14 fl=1 hz=0.018411967779056387, 11:ds=65 fs=45 fl=0 hz=0.048283261802575105, 33:ds=64 fs=15 fl=2 hz=0.018743109151047408, 18:ds=56 fs=17 fl=1 hz=0.020618556701030927

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=88 flags=red+purple
- S25: ds=78 flags=purple
- S21: ds=42 flags=red+purple
- S23: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3', '6', '7'], 'pairs': {'remaining_count': 0}}
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
- current_index=2 streak=1 max=4 last_repeat_gap=22 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=41), P2:1 (gap=43), P3:9 (gap=30)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=41), P2:1 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=41.29525714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 371: score=40.02661428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 391: score=39.7697 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 361: score=36.22797142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 331: score=35.83385714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=35.609321428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 317: score=34.484564285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 571: score=34.34067857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 381: score=33.917228571428566 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 377: score=33.21592142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 118: ds=822 sev=B
- 122: ds=806 sev=B
- 244: ds=803 sev=B
- 005: ds=781 sev=B
- 888: ds=768 sev=B
- 999: ds=764 sev=B
- 445: ds=743 sev=B
- 344: ds=736 sev=B
- 003: ds=720 sev=B
- 558: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=126 sev=red
  - 99: ds=73 sev=blue
  - 11: ds=71 sev=blue
  - 44: ds=28 sev=purple
  - 77: ds=21 sev=-
  - 66: ds=10 sev=-
  - 88: ds=8 sev=-
  - 22: ds=5 sev=-
  - 33: ds=1 sev=-
  - 00: ds=0 sev=-
- non_repeating:
  - 89: ds=58 sev=red
  - 16: ds=53 sev=blue
  - 59: ds=52 sev=blue
  - 69: ds=50 sev=blue
  - 79: ds=44 sev=blue
  - 17: ds=43 sev=blue
  - 57: ds=35 sev=purple
  - 03: ds=34 sev=purple
  - 25: ds=33 sev=purple
  - 45: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:257, 35:160, 5:142, 32:138, 20:111, 18:101, 22:100, 31:94, 26:93, 16:85

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=257 fs=4 fl=0 hz=0.007987220447284345, 35:ds=160 fs=1 fl=1 hz=0.005050505050505051, 5:ds=142 fs=19 fl=1 hz=0.024242424242424242, 32:ds=138 fs=5 fl=2 hz=0.012987012987012988, 20:ds=111 fs=15 fl=2 hz=0.0215311004784689, 18:ds=101 fs=26 fl=0 hz=0.029378531073446325, 22:ds=100 fs=45 fl=0 hz=0.05022321428571429, 31:ds=94 fs=24 fl=2 hz=0.02888888888888889, 26:ds=93 fs=0 fl=0 hz=0.0, 16:ds=85 fs=5 fl=1 hz=0.009234828496042216

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=76 flags=purple
- S3: ds=71 flags=blue+purple
- S5: ds=56 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 037: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 125 -> combined:892(B); midday:876(B)
- 344 -> combined:679(B); evening:736(B)
- 677 -> combined:880(B); midday:895(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:33(purple); evening:34(purple)
- 11 -> combined:47(purple); evening:71(blue)
- 16 -> combined:55(blue); evening:53(blue); midday:27(purple)
- 19 -> combined:34(purple); midday:27(purple)
- 26 -> combined:46(blue); midday:70(red)
- 34 -> combined:26(purple); midday:33(purple)
- 37 -> combined:48(blue); midday:30(purple)
- 44 -> combined:41(purple); evening:28(purple)
- 45 -> combined:31(purple); evening:33(purple)
- 59 -> combined:39(blue); evening:52(blue)
- 69 -> combined:39(blue); evening:50(blue)
- 77 -> combined:42(purple); midday:41(purple)
- 99 -> combined:103(blue); evening:73(blue); midday:51(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(7.104935714285714)[R1,XVAR-Cons(CEM)], 5(3.9189999999999996)[R2,XVAR-Cons(CE)], 7(2.618257142857143)[R3,XVAR-Cons(CE)], 6(1.250992857142857)[R2,Mirror-Echo], 1(0.5026642857142857)[R3,Mirror-Echo]
- P2: 1(4.163)[R2,XVAR-Cons(CE)], 7(2.8943571428571424)[R1,XVAR-Cons(CM)], 9(2.637442857142857)[R3,XVAR-Cons(CE)], 6(1.5957142857142856)[R1,Double-Pressure], 3(1.2016)[R2,Double-Pressure]
- P3: 1(6.027321428571429)[R1,Mirror-Echo], 7(2.716628571428571)[R3,XVAR-Cons(CE)], 9(1.5957142857142856)[R1,Double-Pressure], 6(1.4542857142857142)[R2,Mirror-Echo], 3(1.1477142857142857)[R1,Double-Pressure]
