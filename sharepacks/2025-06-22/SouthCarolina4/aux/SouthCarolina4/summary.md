# Aux Summary — SouthCarolina4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2025-06-22/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=847, 069, 402, 442, 351
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2025-06-22/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=069, 442, 968, 237, 029
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2025-06-22/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=847, 402, 351, 002, 116

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=2 last_repeat_gap=60 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=21), P2:9 (gap=32), P3:4 (gap=29)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=45.28892214285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 694: score=41.41724285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 574: score=38.562951428571424 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 593: score=37.63058071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 595: score=36.20816678571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 584: score=35.810271428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 674: score=35.24248571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 684: score=34.845842857142856 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 693: score=34.43172857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 695: score=31.52705 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=935 sev=B
- 288: ds=903 sev=B
- 466: ds=822 sev=B
- 238: ds=814 sev=B
- 788: ds=725 sev=B
- 388: ds=716 sev=B
- 228: ds=707 sev=B
- 557: ds=706 sev=B
- 137: ds=687 sev=B
- 668: ds=675 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=87 sev=blue
  - 33: ds=50 sev=purple
  - 99: ds=27 sev=purple
  - 55: ds=24 sev=-
  - 22: ds=22 sev=-
  - 77: ds=20 sev=-
  - 88: ds=17 sev=-
  - 11: ds=8 sev=-
  - 00: ds=6 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 28: ds=141 sev=red
  - 56: ds=81 sev=red
  - 18: ds=72 sev=red
  - 01: ds=38 sev=blue
  - 17: ds=38 sev=blue
  - 14: ds=37 sev=blue
  - 19: ds=37 sev=blue
  - 08: ds=36 sev=purple
  - 45: ds=34 sev=purple
  - 39: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 2:187, 1:145, 5:104, 19:94, 34:93, 32:84, 6:83, 4:80, 15:61, 26:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 2:ds=187 fs=9 fl=4 hz=0.016414141414141416, 1:ds=145 fs=5 fl=3 hz=0.011299435028248588, 5:ds=104 fs=21 fl=1 hz=0.028061224489795922, 19:ds=94 fs=13 fl=1 hz=0.016968325791855206, 34:ds=93 fs=26 fl=2 hz=0.031180400890868598, 32:ds=84 fs=2 fl=2 hz=0.005675368898978434, 6:ds=83 fs=21 fl=1 hz=0.02480270574971815, 4:ds=80 fs=26 fl=2 hz=0.03153153153153153, 15:ds=61 fs=13 fl=3 hz=0.01845444059976932, 26:ds=57 fs=2 fl=0 hz=0.007894736842105263

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S27: ds=100 flags=purple
- S26: ds=93 flags=blue+purple
- S25: ds=82 flags=purple
- S3: ds=59 flags=purple
- S13: ds=47 flags=purple
- S20: ds=45 flags=purple
- S17: ds=42 flags=purple
- S4: ds=39 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 013: score=2 tags=RS
  - 049: score=2 tags=RS
  - 058: score=2 tags=RS
  - 067: score=2 tags=RS
  - 139: score=2 tags=RS
  - 148: score=2 tags=RS
  - 157: score=2 tags=RS
  - 238: score=2 tags=RS
  - 247: score=2 tags=RS
  - 256: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=36 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=47), P2:8 (gap=25), P3:1 (gap=27)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=47)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=45.28892214285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 694: score=41.41724285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 574: score=38.562951428571424 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 593: score=37.63058071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 595: score=36.20816678571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 584: score=35.810271428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 674: score=35.24248571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 684: score=34.845842857142856 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 693: score=34.43172857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 695: score=31.52705 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 144: ds=976 sev=B
- 777: ds=975 sev=B
- 224: ds=946 sev=B
- 011: ds=766 sev=B
- 277: ds=712 sev=B
- 555: ds=707 sev=B
- 222: ds=684 sev=B
- 048: ds=667 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=61 sev=purple
  - 00: ds=54 sev=purple
  - 88: ds=41 sev=purple
  - 66: ds=40 sev=purple
  - 33: ds=23 sev=-
  - 99: ds=12 sev=-
  - 55: ds=11 sev=-
  - 22: ds=10 sev=-
  - 77: ds=9 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 78: ds=126 sev=red
  - 04: ds=85 sev=red
  - 28: ds=65 sev=red
  - 08: ds=41 sev=blue
  - 56: ds=37 sev=blue
  - 15: ds=35 sev=purple
  - 35: ds=34 sev=purple
  - 18: ds=33 sev=purple
  - 16: ds=29 sev=purple
  - 67: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:294, 32:248, 1:168, 2:86, 5:85, 16:61, 8:60, 4:54, 34:44, 19:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=294 fs=23 fl=0 hz=0.03412462908011869, 32:ds=248 fs=1 fl=2 hz=0.006993006993006993, 1:ds=168 fs=4 fl=3 hz=0.00963855421686747, 2:ds=86 fs=11 fl=1 hz=0.015435501653803748, 5:ds=85 fs=20 fl=0 hz=0.02531645569620253, 16:ds=61 fs=3 fl=1 hz=0.009191176470588236, 8:ds=60 fs=42 fl=1 hz=0.04767184035476718, 4:ds=54 fs=26 fl=2 hz=0.030871003307607496, 34:ds=44 fs=27 fl=1 hz=0.03083700440528634, 19:ds=43 fs=15 fl=3 hz=0.0192102454642476

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S0: ds=97 flags=blue+purple
- S4: ds=92 flags=purple
- S21: ds=43 flags=purple
- S16: ds=41 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=72 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=83), P2:9 (gap=17), P3:4 (gap=33)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=83)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=45.28892214285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 694: score=41.41724285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 574: score=38.562951428571424 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 593: score=37.63058071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 595: score=36.20816678571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 584: score=35.810271428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 674: score=35.24248571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 684: score=34.845842857142856 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 693: score=34.43172857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 695: score=31.52705 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 114: ds=974 sev=B
- 238: ds=891 sev=B
- 558: ds=869 sev=B
- 477: ds=856 sev=B
- 000: ds=853 sev=B
- 556: ds=819 sev=B
- 115: ds=814 sev=B
- 111: ds=801 sev=B
- 999: ds=786 sev=B
- 078: ds=773 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=113 sev=red
  - 66: ds=83 sev=blue
  - 44: ds=59 sev=purple
  - 22: ds=57 sev=purple
  - 55: ds=31 sev=purple
  - 33: ds=30 sev=purple
  - 99: ds=24 sev=-
  - 88: ds=9 sev=-
  - 11: ds=4 sev=-
  - 00: ds=3 sev=-
- non_repeating:
  - 28: ds=90 sev=red
  - 56: ds=49 sev=blue
  - 09: ds=47 sev=blue
  - 18: ds=42 sev=blue
  - 06: ds=39 sev=blue
  - 34: ds=36 sev=purple
  - 46: ds=33 sev=purple
  - 49: ds=33 sev=purple
  - 68: ds=28 sev=purple
  - 23: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:291, 19:211, 26:204, 6:146, 10:109, 2:106, 1:78, 15:75, 5:56, 14:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=291 fs=3 fl=1 hz=0.017391304347826087, 19:ds=211 fs=16 fl=2 hz=0.02319587628865979, 26:ds=204 fs=0 fl=0 hz=0.002628120893561104, 6:ds=146 fs=23 fl=2 hz=0.030637254901960783, 10:ds=109 fs=20 fl=0 hz=0.024110218140068886, 2:ds=106 fs=13 fl=3 hz=0.01875732708089097, 1:ds=78 fs=2 fl=0 hz=0.005440696409140369, 15:ds=75 fs=24 fl=1 hz=0.027056277056277056, 5:ds=56 fs=16 fl=3 hz=0.0202991452991453, 14:ds=52 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S3: ds=72 flags=purple
- S22: ds=67 flags=purple
- S26: ds=50 flags=blue+purple
- S7: ds=48 flags=purple
- S14: ds=45 flags=purple
- S25: ds=44 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 019: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 059: score=1 tags=FLT
  - 069: score=1 tags=FLT
  - 079: score=1 tags=FLT
  - 089: score=1 tags=FLT
  - 129: score=1 tags=FLT
  - 139: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 115 -> combined:673(B); evening:814(B)
- 238 -> combined:814(B); evening:891(B)
- 788 -> combined:725(B); evening:758(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:38(blue); midday:27(purple)
- 08 -> combined:36(purple); midday:41(blue)
- 18 -> combined:72(red); evening:42(blue); midday:33(purple)
- 19 -> combined:37(blue); evening:25(purple)
- 28 -> combined:141(red); evening:90(red); midday:65(red)
- 33 -> combined:50(purple); evening:30(purple)
- 34 -> combined:29(purple); evening:36(purple)
- 56 -> combined:81(red); evening:49(blue); midday:37(blue)
- 66 -> combined:87(blue); evening:83(blue); midday:40(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(4.205)[R1,XVAR-Cons(CM)], 6(3.240571428571428)[R3,XVAR-Cons(CE)], 2(1.4015)[R2,Double-Pressure], 3(1.0344)[R2,Double-Pressure], 7(0.986)[R2,Double-Pressure]
- P2: 9(7.098257142857143)[R1,XVAR-Cons(CEM)], 7(3.4234999999999998)[R2,XVAR-Cons(CE)], 8(3.0268571428571427)[R3,XVAR-Cons(CM)], 1(1.0252999999999999)[R2,Double-Pressure], 3(0.2881)[R3,Swap]
- P3: 4(8.078414285714285)[R1,XVAR-Cons(CEM)], 3(3.5928999999999998)[R2,XVAR-Cons(CE)], 5(1.6882214285714285)[R3,XVAR-Cons(CM)], 1(1.4061428571428571)[R1,Double-Pressure], 0(0.2552785714285714)[R3]
