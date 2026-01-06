# Aux Summary — Virginia4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/Virginia4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Virginia
- combined: live=`data/cleaned/draws/Virginia_draws.csv` snap=`sharepacks/2025-12-30/Virginia4/aux/draws/Virginia_draws.csv` n=1000 head=933, 908, 658, 055, 604
- midday: live=`data/cleaned/draws/Virginia_Midday_draws.csv` snap=`sharepacks/2025-12-30/Virginia4/aux/draws/Virginia_Midday_draws.csv` n=1000 head=908, 055, 428, 829, 002
- evening: live=`data/cleaned/draws/Virginia_Evening_draws.csv` snap=`sharepacks/2025-12-30/Virginia4/aux/draws/Virginia_Evening_draws.csv` n=1000 head=933, 658, 604, 060, 232

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=33 streak=1 max=2 last_repeat_gap=26 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=20), P2:8 (gap=27), P3:1 (gap=20)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 381: score=46.569649999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 181: score=43.527389285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 311: score=40.30180714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 387: score=39.7195 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 383: score=38.204907142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 111: score=37.259546428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 386: score=37.03377142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 331: score=36.67647142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 389: score=36.117914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 361: score=35.982235714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=939 sev=B
- 556: ds=895 sev=B
- 125: ds=890 sev=B
- 677: ds=878 sev=B
- 688: ds=839 sev=B
- 119: ds=798 sev=B
- 344: ds=677 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=101 sev=blue
  - 11: ds=45 sev=purple
  - 77: ds=40 sev=purple
  - 44: ds=39 sev=purple
  - 66: ds=18 sev=-
  - 88: ds=14 sev=-
  - 22: ds=8 sev=-
  - 00: ds=6 sev=-
  - 55: ds=3 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 16: ds=53 sev=blue
  - 37: ds=46 sev=blue
  - 26: ds=44 sev=blue
  - 36: ds=44 sev=blue
  - 59: ds=37 sev=blue
  - 69: ds=37 sev=blue
  - 14: ds=32 sev=purple
  - 19: ds=32 sev=purple
  - 01: ds=31 sev=purple
  - 03: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:267, 26:184, 34:132, 23:130, 18:111, 6:106, 15:102, 24:92, 16:85, 11:68

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=267 fs=1 fl=1 hz=0.006147540983606558, 26:ds=184 fs=4 fl=0 hz=0.009174311926605505, 34:ds=132 fs=18 fl=2 hz=0.023640661938534282, 23:ds=130 fs=15 fl=3 hz=0.024965325936199722, 18:ds=111 fs=19 fl=2 hz=0.023836549375709424, 6:ds=106 fs=16 fl=3 hz=0.02186421173762946, 15:ds=102 fs=16 fl=2 hz=0.022058823529411763, 24:ds=92 fs=45 fl=1 hz=0.05082872928176795, 16:ds=85 fs=8 fl=0 hz=0.011335012594458438, 11:ds=68 fs=51 fl=0 hz=0.0552546045503792

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S8: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=79 flags=purple
- S23: ds=34 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '7'], 'pairs': {'remaining_count': 0}}
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
- current_index=14 streak=1 max=3 last_repeat_gap=3 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=29), P2:6 (gap=29), P3:3 (gap=15)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 381: score=46.569649999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 181: score=43.527389285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 311: score=40.30180714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 387: score=39.7195 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 383: score=38.204907142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 111: score=37.259546428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 386: score=37.03377142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 331: score=36.67647142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 389: score=36.117914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 361: score=35.982235714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=985 sev=B
- 338: ds=925 sev=B
- 223: ds=924 sev=B
- 377: ds=909 sev=B
- 677: ds=894 sev=B
- 125: ds=875 sev=B
- 699: ds=839 sev=B
- 356: ds=836 sev=B
- 278: ds=803 sev=B
- 179: ds=739 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=89 sev=blue
  - 99: ds=50 sev=purple
  - 66: ds=41 sev=purple
  - 77: ds=40 sev=purple
  - 88: ds=30 sev=purple
  - 11: ds=22 sev=-
  - 44: ds=19 sev=-
  - 22: ds=10 sev=-
  - 00: ds=4 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 26: ds=69 sev=red
  - 39: ds=53 sev=blue
  - 68: ds=48 sev=blue
  - 23: ds=47 sev=blue
  - 46: ds=37 sev=blue
  - 35: ds=35 sev=purple
  - 34: ds=32 sev=purple
  - 38: ds=30 sev=purple
  - 37: ds=29 sev=purple
  - 16: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:143, 35:133, 26:120, 29:115, 25:90, 23:89, 6:80, 11:64, 33:63, 18:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=143 fs=18 fl=2 hz=0.023752969121140142, 35:ds=133 fs=2 fl=1 hz=0.007396449704142012, 26:ds=120 fs=4 fl=1 hz=0.01046337817638266, 29:ds=115 fs=24 fl=1 hz=0.02965599051008304, 25:ds=90 fs=12 fl=3 hz=0.018270401948842874, 23:ds=89 fs=20 fl=1 hz=0.02648171500630517, 6:ds=80 fs=14 fl=1 hz=0.018411967779056387, 11:ds=64 fs=45 fl=0 hz=0.048283261802575105, 33:ds=63 fs=15 fl=2 hz=0.018743109151047408, 18:ds=55 fs=17 fl=1 hz=0.020618556701030927

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=87 flags=red+purple
- S25: ds=77 flags=purple
- S21: ds=41 flags=red+purple
- S23: ds=40 flags=purple

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
- current_index=33 streak=1 max=4 last_repeat_gap=21 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=40), P2:1 (gap=42), P3:9 (gap=29)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=40), P2:1 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 381: score=46.569649999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 181: score=43.527389285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 311: score=40.30180714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 387: score=39.7195 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 383: score=38.204907142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 111: score=37.259546428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 386: score=37.03377142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 331: score=36.67647142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 389: score=36.117914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 361: score=35.982235714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=846 sev=B
- 118: ds=821 sev=B
- 122: ds=805 sev=B
- 244: ds=802 sev=B
- 005: ds=780 sev=B
- 888: ds=767 sev=B
- 999: ds=763 sev=B
- 445: ds=742 sev=B
- 344: ds=735 sev=B
- 003: ds=719 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=125 sev=red
  - 99: ds=72 sev=blue
  - 11: ds=70 sev=purple
  - 44: ds=27 sev=purple
  - 77: ds=20 sev=-
  - 66: ds=9 sev=-
  - 88: ds=7 sev=-
  - 22: ds=4 sev=-
  - 00: ds=3 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 89: ds=57 sev=red
  - 01: ds=55 sev=blue
  - 16: ds=52 sev=blue
  - 59: ds=51 sev=blue
  - 69: ds=49 sev=blue
  - 79: ds=43 sev=blue
  - 17: ds=42 sev=blue
  - 57: ds=34 sev=purple
  - 03: ds=33 sev=purple
  - 25: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:256, 35:159, 5:141, 32:137, 20:110, 18:100, 22:99, 31:93, 26:92, 16:84

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=256 fs=4 fl=0 hz=0.007987220447284345, 35:ds=159 fs=1 fl=1 hz=0.005050505050505051, 5:ds=141 fs=19 fl=1 hz=0.024242424242424242, 32:ds=137 fs=5 fl=2 hz=0.012987012987012988, 20:ds=110 fs=15 fl=2 hz=0.0215311004784689, 18:ds=100 fs=26 fl=0 hz=0.029378531073446325, 22:ds=99 fs=45 fl=0 hz=0.05022321428571429, 31:ds=93 fs=24 fl=2 hz=0.02888888888888889, 26:ds=92 fs=0 fl=0 hz=0.0, 16:ds=84 fs=5 fl=1 hz=0.009234828496042216

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=75 flags=purple
- S3: ds=70 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 037: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 001 -> combined:939(B); evening:846(B)
- 125 -> combined:890(B); midday:875(B)
- 344 -> combined:677(B); evening:735(B)
- 677 -> combined:878(B); midday:894(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:31(purple); evening:55(blue)
- 03 -> combined:31(purple); evening:33(purple)
- 11 -> combined:45(purple); evening:70(purple)
- 16 -> combined:53(blue); evening:52(blue); midday:26(purple)
- 19 -> combined:32(purple); midday:26(purple)
- 26 -> combined:44(blue); midday:69(red)
- 37 -> combined:46(blue); midday:29(purple)
- 44 -> combined:39(purple); evening:27(purple)
- 45 -> combined:29(purple); evening:32(purple)
- 59 -> combined:37(blue); evening:51(blue)
- 69 -> combined:37(blue); evening:49(blue)
- 77 -> combined:40(purple); midday:40(purple)
- 99 -> combined:101(blue); evening:72(blue); midday:50(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(6.998785714285715)[R1,XVAR-Cons(CEM)], 1(2.831728571428571)[R2,XVAR-Cons(CM)], 5(2.557142857142857)[R3,XVAR-Cons(CE)], 6(1.2239857142857142)[R2,Mirror-Echo], 7(1.0135)[R2,Double-Pressure]
- P2: 8(6.153271428571428)[R1,XVAR-Cons(CEM)], 1(3.3854285714285712)[R3,XVAR-Cons(CE)], 6(1.5658571428571428)[R1,Double-Pressure], 3(1.2600928571428571)[R2,Mirror-Echo], 7(1.1179999999999999)[R2,Double-Pressure]
- P3: 1(5.917592857142857)[R1,Mirror-Echo], 7(2.567442857142857)[R3,XVAR-Cons(CE)], 9(1.4658571428571427)[R1,Double-Pressure], 6(1.3817142857142857)[R2,Mirror-Echo], 3(1.1178571428571429)[R1,Double-Pressure]
