# Aux Summary — Virginia4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/Virginia4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Virginia
- combined: live=`data/cleaned/draws/Virginia_draws.csv` snap=`sharepacks/2026-01-02/Virginia4/aux/draws/Virginia_draws.csv` n=1000 head=354, 019, 636, 686, 100
- midday: live=`data/cleaned/draws/Virginia_Midday_draws.csv` snap=`sharepacks/2026-01-02/Virginia4/aux/draws/Virginia_Midday_draws.csv` n=1000 head=019, 686, 888, 908, 055
- evening: live=`data/cleaned/draws/Virginia_Evening_draws.csv` snap=`sharepacks/2026-01-02/Virginia4/aux/draws/Virginia_Evening_draws.csv` n=1000 head=354, 636, 100, 933, 658

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=2 last_repeat_gap=3 last_repeat_index=18

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=21), P2:7 (gap=25), P3:1 (gap=26)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 591: score=40.51052142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 571: score=38.96307857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 597: score=36.703742857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 791: score=35.61136428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 511: score=35.16113571428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R3,Swap src=cartesian
- 577: score=35.1563 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 561: score=35.04156428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R3,Swap src=cartesian
- 531: score=34.559535714285715 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 771: score=34.06392142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 797: score=33.967645714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),R2,Repeat-Endcap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=901 sev=B
- 125: ds=896 sev=B
- 677: ds=884 sev=B
- 688: ds=845 sev=B
- 119: ds=804 sev=B
- 344: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=107 sev=red
  - 11: ds=51 sev=purple
  - 77: ds=46 sev=purple
  - 44: ds=45 sev=purple
  - 22: ds=14 sev=-
  - 55: ds=9 sev=-
  - 33: ds=6 sev=-
  - 88: ds=5 sev=-
  - 00: ds=4 sev=-
  - 66: ds=2 sev=-
- non_repeating:
  - 16: ds=59 sev=red
  - 37: ds=52 sev=blue
  - 26: ds=50 sev=blue
  - 59: ds=43 sev=blue
  - 69: ds=43 sev=blue
  - 14: ds=38 sev=blue
  - 03: ds=37 sev=blue
  - 07: ds=32 sev=purple
  - 38: ds=28 sev=purple
  - 12: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:273, 26:190, 34:138, 23:136, 6:112, 15:108, 24:98, 16:91, 11:74, 17:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=273 fs=1 fl=1 hz=0.006147540983606558, 26:ds=190 fs=4 fl=0 hz=0.009174311926605505, 34:ds=138 fs=18 fl=2 hz=0.023640661938534282, 23:ds=136 fs=15 fl=3 hz=0.024965325936199722, 6:ds=112 fs=16 fl=3 hz=0.02186421173762946, 15:ds=108 fs=16 fl=2 hz=0.022058823529411763, 24:ds=98 fs=44 fl=1 hz=0.0510204081632653, 16:ds=91 fs=8 fl=0 hz=0.011335012594458438, 11:ds=74 fs=51 fl=0 hz=0.0552546045503792, 17:ds=69 fs=24 fl=1 hz=0.027085590465872156

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S8: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=40 flags=purple
- S4: ds=37 flags=purple
- S9: ds=30 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 027: score=3 tags=FLT,RS
  - 126: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 279: score=3 tags=FLT,RS
  - 378: score=3 tags=FLT,RS
  - 567: score=3 tags=FLT,RS
  - 018: score=2 tags=RS
  - 036: score=2 tags=RS
  - 045: score=2 tags=RS
  - 135: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=6 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=32), P2:6 (gap=32), P3:3 (gap=18)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 591: score=40.51052142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 571: score=38.96307857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 597: score=36.703742857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 791: score=35.61136428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 511: score=35.16113571428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R3,Swap src=cartesian
- 577: score=35.1563 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 561: score=35.04156428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R3,Swap src=cartesian
- 531: score=34.559535714285715 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 771: score=34.06392142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 797: score=33.967645714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),R2,Repeat-Endcap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=988 sev=B
- 338: ds=928 sev=B
- 223: ds=927 sev=B
- 377: ds=912 sev=B
- 677: ds=897 sev=B
- 125: ds=878 sev=B
- 699: ds=842 sev=B
- 356: ds=839 sev=B
- 278: ds=806 sev=B
- 179: ds=742 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=92 sev=blue
  - 99: ds=53 sev=purple
  - 77: ds=43 sev=purple
  - 11: ds=25 sev=purple
  - 44: ds=22 sev=-
  - 22: ds=13 sev=-
  - 00: ds=7 sev=-
  - 55: ds=4 sev=-
  - 88: ds=2 sev=-
  - 66: ds=1 sev=-
- non_repeating:
  - 26: ds=72 sev=red
  - 39: ds=56 sev=red
  - 23: ds=50 sev=blue
  - 46: ds=40 sev=blue
  - 35: ds=38 sev=blue
  - 34: ds=35 sev=purple
  - 38: ds=33 sev=purple
  - 37: ds=32 sev=purple
  - 16: ds=29 sev=purple
  - 06: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:146, 35:136, 26:123, 29:118, 25:93, 23:92, 6:83, 11:67, 33:66, 13:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=146 fs=18 fl=2 hz=0.023752969121140142, 35:ds=136 fs=2 fl=1 hz=0.007396449704142012, 26:ds=123 fs=4 fl=1 hz=0.01046337817638266, 29:ds=118 fs=24 fl=1 hz=0.02965599051008304, 25:ds=93 fs=12 fl=3 hz=0.018270401948842874, 23:ds=92 fs=20 fl=1 hz=0.02648171500630517, 6:ds=83 fs=14 fl=1 hz=0.018411967779056387, 11:ds=67 fs=45 fl=0 hz=0.048283261802575105, 33:ds=66 fs=15 fl=2 hz=0.018743109151047408, 13:ds=57 fs=22 fl=2 hz=0.02666666666666667

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=90 flags=red+purple
- S25: ds=80 flags=purple
- S21: ds=44 flags=red+purple
- S23: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '3', '4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=3 tags=FLT,RS
  - 039: score=3 tags=FLT,RS
  - 048: score=3 tags=FLT,RS
  - 057: score=3 tags=FLT,RS
  - 129: score=3 tags=FLT,RS
  - 138: score=3 tags=FLT,RS
  - 147: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=4 last_repeat_gap=24 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=43), P2:1 (gap=45), P3:9 (gap=32)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=43), P2:1 (ds=45)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 591: score=40.51052142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 571: score=38.96307857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 597: score=36.703742857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 791: score=35.61136428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 511: score=35.16113571428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R3,Swap src=cartesian
- 577: score=35.1563 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 561: score=35.04156428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R3,Swap src=cartesian
- 531: score=34.559535714285715 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 771: score=34.06392142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 797: score=33.967645714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),R2,Repeat-Endcap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 118: ds=824 sev=B
- 122: ds=808 sev=B
- 244: ds=805 sev=B
- 005: ds=783 sev=B
- 888: ds=770 sev=B
- 999: ds=766 sev=B
- 445: ds=745 sev=B
- 344: ds=738 sev=B
- 003: ds=722 sev=B
- 558: ds=697 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=128 sev=red
  - 99: ds=75 sev=blue
  - 11: ds=73 sev=blue
  - 44: ds=30 sev=purple
  - 77: ds=23 sev=-
  - 88: ds=10 sev=-
  - 22: ds=7 sev=-
  - 33: ds=3 sev=-
  - 00: ds=2 sev=-
  - 66: ds=1 sev=-
- non_repeating:
  - 89: ds=60 sev=red
  - 16: ds=55 sev=blue
  - 59: ds=54 sev=blue
  - 69: ds=52 sev=blue
  - 79: ds=46 sev=blue
  - 17: ds=45 sev=blue
  - 57: ds=37 sev=blue
  - 03: ds=36 sev=purple
  - 25: ds=35 sev=purple
  - 09: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:259, 35:162, 5:144, 32:140, 20:113, 22:102, 31:96, 26:95, 16:87, 34:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=259 fs=4 fl=0 hz=0.007987220447284345, 35:ds=162 fs=1 fl=1 hz=0.005050505050505051, 5:ds=144 fs=19 fl=1 hz=0.024242424242424242, 32:ds=140 fs=5 fl=2 hz=0.012987012987012988, 20:ds=113 fs=15 fl=2 hz=0.0215311004784689, 22:ds=102 fs=45 fl=0 hz=0.05022321428571429, 31:ds=96 fs=24 fl=2 hz=0.02888888888888889, 26:ds=95 fs=0 fl=0 hz=0.0, 16:ds=87 fs=5 fl=1 hz=0.009234828496042216, 34:ds=69 fs=27 fl=0 hz=0.03082191780821918

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=78 flags=purple
- S3: ds=73 flags=blue+purple
- S5: ds=58 flags=purple

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
- 125 -> combined:896(B); midday:878(B)
- 344 -> combined:683(B); evening:738(B)
- 677 -> combined:884(B); midday:897(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:37(blue); evening:36(purple)
- 11 -> combined:51(purple); evening:73(blue); midday:25(purple)
- 16 -> combined:59(red); evening:55(blue); midday:29(purple)
- 26 -> combined:50(blue); evening:25(purple); midday:72(red)
- 37 -> combined:52(blue); evening:26(purple); midday:32(purple)
- 38 -> combined:28(purple); midday:33(purple)
- 44 -> combined:45(purple); evening:30(purple)
- 59 -> combined:43(blue); evening:54(blue)
- 69 -> combined:43(blue); evening:52(blue)
- 77 -> combined:46(purple); midday:43(purple)
- 99 -> combined:107(red); evening:75(blue); midday:53(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(6.939357142857142)[R1,XVAR-Cons(CEM)], 7(3.5402)[R2,Mirror-Echo], 3(1.6254285714285714)[R1,Double-Pressure], 1(1.0135)[R2,Double-Pressure], 2(0.438)[R3,Mirror-Echo]
- P2: 9(3.594385714285714)[R2,Mirror-Echo], 7(3.046942857142857)[R1,XVAR-Cons(CM)], 1(1.7449999999999999)[R1,Double-Pressure], 6(1.6254285714285714)[R1,Double-Pressure], 3(1.1434)[R2,Double-Pressure]
- P3: 1(5.976778571428572)[R1,XVAR-Cons(CEM)], 7(3.67)[R2,Mirror-Echo], 9(1.6554285714285715)[R1,Double-Pressure], 3(1.2074285714285713)[R1,Double-Pressure], 4(1.0553)[R2,Double-Pressure]
