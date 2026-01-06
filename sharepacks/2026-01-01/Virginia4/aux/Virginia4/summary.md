# Aux Summary — Virginia4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/Virginia4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Virginia
- combined: live=`data/cleaned/draws/Virginia_draws.csv` snap=`sharepacks/2026-01-01/Virginia4/aux/draws/Virginia_draws.csv` n=1000 head=636, 686, 100, 888, 933
- midday: live=`data/cleaned/draws/Virginia_Midday_draws.csv` snap=`sharepacks/2026-01-01/Virginia4/aux/draws/Virginia_Midday_draws.csv` n=1000 head=686, 888, 908, 055, 428
- evening: live=`data/cleaned/draws/Virginia_Evening_draws.csv` snap=`sharepacks/2026-01-01/Virginia4/aux/draws/Virginia_Evening_draws.csv` n=1000 head=636, 100, 933, 658, 604

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=2 max=2 last_repeat_gap=1 last_repeat_index=18

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=24), P2:7 (gap=23), P3:1 (gap=24)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=40.33513571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=39.80797142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 371: score=39.09878571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 391: score=38.81476428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 571: score=38.57162142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 317: score=36.51032857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 517: score=35.98316428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 377: score=35.27397857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 361: score=35.22370714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R3,Swap src=cartesian
- 397: score=34.98995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=899 sev=B
- 125: ds=894 sev=B
- 677: ds=882 sev=B
- 688: ds=843 sev=B
- 119: ds=802 sev=B
- 344: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=105 sev=blue
  - 11: ds=49 sev=purple
  - 77: ds=44 sev=purple
  - 44: ds=43 sev=purple
  - 22: ds=12 sev=-
  - 55: ds=7 sev=-
  - 33: ds=4 sev=-
  - 88: ds=3 sev=-
  - 00: ds=2 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 16: ds=57 sev=red
  - 37: ds=50 sev=blue
  - 26: ds=48 sev=blue
  - 59: ds=41 sev=blue
  - 69: ds=41 sev=blue
  - 14: ds=36 sev=purple
  - 19: ds=36 sev=purple
  - 03: ds=35 sev=purple
  - 45: ds=33 sev=purple
  - 07: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:271, 26:188, 34:136, 23:134, 6:110, 15:106, 24:96, 16:89, 11:72, 17:67

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=271 fs=1 fl=1 hz=0.006147540983606558, 26:ds=188 fs=4 fl=0 hz=0.009174311926605505, 34:ds=136 fs=18 fl=2 hz=0.023640661938534282, 23:ds=134 fs=15 fl=3 hz=0.024965325936199722, 6:ds=110 fs=16 fl=3 hz=0.02186421173762946, 15:ds=106 fs=16 fl=2 hz=0.022058823529411763, 24:ds=96 fs=44 fl=1 hz=0.0510204081632653, 16:ds=89 fs=8 fl=0 hz=0.011335012594458438, 11:ds=72 fs=51 fl=0 hz=0.0552546045503792, 17:ds=67 fs=24 fl=1 hz=0.027085590465872156

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S8: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=38 flags=purple
- S4: ds=35 flags=purple
- S9: ds=28 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=5 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=31), P2:6 (gap=31), P3:3 (gap=17)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=40.33513571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=39.80797142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 371: score=39.09878571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 391: score=38.81476428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 571: score=38.57162142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 317: score=36.51032857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 517: score=35.98316428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 377: score=35.27397857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 361: score=35.22370714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R3,Swap src=cartesian
- 397: score=34.98995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=987 sev=B
- 338: ds=927 sev=B
- 223: ds=926 sev=B
- 377: ds=911 sev=B
- 677: ds=896 sev=B
- 125: ds=877 sev=B
- 699: ds=841 sev=B
- 356: ds=838 sev=B
- 278: ds=805 sev=B
- 179: ds=741 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=91 sev=blue
  - 99: ds=52 sev=purple
  - 77: ds=42 sev=purple
  - 11: ds=24 sev=-
  - 44: ds=21 sev=-
  - 22: ds=12 sev=-
  - 00: ds=6 sev=-
  - 55: ds=3 sev=-
  - 88: ds=1 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 26: ds=71 sev=red
  - 39: ds=55 sev=blue
  - 23: ds=49 sev=blue
  - 46: ds=39 sev=blue
  - 35: ds=37 sev=blue
  - 34: ds=34 sev=purple
  - 38: ds=32 sev=purple
  - 37: ds=31 sev=purple
  - 16: ds=28 sev=purple
  - 19: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:145, 35:135, 26:122, 29:117, 25:92, 23:91, 6:82, 11:66, 33:65, 13:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=145 fs=18 fl=2 hz=0.023752969121140142, 35:ds=135 fs=2 fl=1 hz=0.007396449704142012, 26:ds=122 fs=4 fl=1 hz=0.01046337817638266, 29:ds=117 fs=24 fl=1 hz=0.02965599051008304, 25:ds=92 fs=12 fl=3 hz=0.018270401948842874, 23:ds=91 fs=20 fl=1 hz=0.02648171500630517, 6:ds=82 fs=14 fl=1 hz=0.018411967779056387, 11:ds=66 fs=45 fl=0 hz=0.048283261802575105, 33:ds=65 fs=15 fl=2 hz=0.018743109151047408, 13:ds=56 fs=22 fl=2 hz=0.02666666666666667

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=89 flags=red+purple
- S25: ds=79 flags=purple
- S21: ds=43 flags=red+purple
- S23: ds=42 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=3 tags=FLT,RS
  - 039: score=3 tags=FLT,RS
  - 057: score=3 tags=FLT,RS
  - 129: score=3 tags=FLT,RS
  - 138: score=3 tags=FLT,RS
  - 147: score=3 tags=FLT,RS
  - 156: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 579: score=3 tags=FLT,RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=4 last_repeat_gap=23 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=42), P2:1 (gap=44), P3:9 (gap=31)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=42), P2:1 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=40.33513571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 511: score=39.80797142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 371: score=39.09878571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 391: score=38.81476428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 571: score=38.57162142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 317: score=36.51032857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 517: score=35.98316428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 377: score=35.27397857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 361: score=35.22370714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R3,Swap src=cartesian
- 397: score=34.98995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 118: ds=823 sev=B
- 122: ds=807 sev=B
- 244: ds=804 sev=B
- 005: ds=782 sev=B
- 888: ds=769 sev=B
- 999: ds=765 sev=B
- 445: ds=744 sev=B
- 344: ds=737 sev=B
- 003: ds=721 sev=B
- 558: ds=696 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=127 sev=red
  - 99: ds=74 sev=blue
  - 11: ds=72 sev=blue
  - 44: ds=29 sev=purple
  - 77: ds=22 sev=-
  - 88: ds=9 sev=-
  - 22: ds=6 sev=-
  - 33: ds=2 sev=-
  - 00: ds=1 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 89: ds=59 sev=red
  - 16: ds=54 sev=blue
  - 59: ds=53 sev=blue
  - 69: ds=51 sev=blue
  - 79: ds=45 sev=blue
  - 17: ds=44 sev=blue
  - 57: ds=36 sev=purple
  - 03: ds=35 sev=purple
  - 25: ds=34 sev=purple
  - 45: ds=34 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:258, 35:161, 5:143, 32:139, 20:112, 22:101, 31:95, 26:94, 16:86, 34:68

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=258 fs=4 fl=0 hz=0.007987220447284345, 35:ds=161 fs=1 fl=1 hz=0.005050505050505051, 5:ds=143 fs=19 fl=1 hz=0.024242424242424242, 32:ds=139 fs=5 fl=2 hz=0.012987012987012988, 20:ds=112 fs=15 fl=2 hz=0.0215311004784689, 22:ds=101 fs=45 fl=0 hz=0.05022321428571429, 31:ds=95 fs=24 fl=2 hz=0.02888888888888889, 26:ds=94 fs=0 fl=0 hz=0.0, 16:ds=86 fs=5 fl=1 hz=0.009234828496042216, 34:ds=68 fs=27 fl=0 hz=0.03082191780821918

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=77 flags=purple
- S3: ds=72 flags=blue+purple
- S5: ds=57 flags=purple

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
- 125 -> combined:894(B); midday:877(B)
- 344 -> combined:681(B); evening:737(B)
- 677 -> combined:882(B); midday:896(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:35(purple); evening:35(purple)
- 11 -> combined:49(purple); evening:72(blue)
- 16 -> combined:57(red); evening:54(blue); midday:28(purple)
- 19 -> combined:36(purple); midday:28(purple)
- 26 -> combined:48(blue); midday:71(red)
- 34 -> combined:28(purple); midday:34(purple)
- 35 -> combined:26(purple); midday:37(blue)
- 37 -> combined:50(blue); evening:25(purple); midday:31(purple)
- 38 -> combined:26(purple); midday:32(purple)
- 44 -> combined:43(purple); evening:29(purple)
- 45 -> combined:33(purple); evening:34(purple)
- 59 -> combined:41(blue); evening:53(blue)
- 69 -> combined:41(blue); evening:51(blue)
- 77 -> combined:44(purple); midday:42(purple)
- 99 -> combined:105(blue); evening:74(blue); midday:52(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(7.211085714285714)[R1,XVAR-Cons(CEM)], 5(6.683921428571429)[R2,XVAR-Cons(CEM)], 7(2.6674428571428574)[R3,XVAR-Cons(CE)], 1(0.9925999999999999)[R2,Double-Pressure]
- P2: 1(4.207)[R2,XVAR-Cons(CE)], 7(2.97065)[R1,XVAR-Cons(CM)], 9(2.6866285714285714)[R3,XVAR-Cons(CE)], 6(1.5955714285714284)[R1,Double-Pressure], 3(1.2225)[R2,Double-Pressure]
- P3: 1(5.91705)[R1,XVAR-Cons(CEM)], 7(3.592242857142857)[R2,Mirror-Echo], 9(1.6255714285714284)[R1,Double-Pressure], 3(1.1775714285714285)[R1,Double-Pressure], 4(1.0044)[R2,Double-Pressure]
