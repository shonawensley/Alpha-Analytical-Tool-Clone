# Aux Summary — NorthCarolina4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2025-06-21/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=261, 707, 902, 579, 799
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2025-06-21/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=707, 579, 257, 718, 691
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2025-06-21/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=261, 902, 799, 800, 438

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=3 last_repeat_gap=3 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=29), P2:2 (gap=28), P3:4 (gap=29)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 124: score=51.28055214285715 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 126: score=48.92290428571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 144: score=45.131815714285715 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 123: score=43.78541214285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 324: score=40.34415714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 146: score=40.19492857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 326: score=38.294028571428576 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 134: score=36.96044285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 424: score=36.94055357142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 114: score=36.939542857142854 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 666: ds=827 sev=B
- 228: ds=820 sev=B
- 244: ds=794 sev=B
- 004: ds=768 sev=B
- 001: ds=732 sev=B
- 677: ds=693 sev=B
- 377: ds=691 sev=B
- 044: ds=689 sev=B
- 226: ds=679 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=99 sev=blue
  - 44: ds=53 sev=purple
  - 66: ds=46 sev=purple
  - 11: ds=36 sev=purple
  - 33: ds=34 sev=purple
  - 22: ds=25 sev=purple
  - 55: ds=24 sev=-
  - 00: ds=6 sev=-
  - 99: ds=4 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 89: ds=128 sev=red
  - 46: ds=96 sev=red
  - 15: ds=73 sev=red
  - 37: ds=42 sev=blue
  - 13: ds=39 sev=blue
  - 36: ds=34 sev=purple
  - 24: ds=32 sev=purple
  - 47: ds=32 sev=purple
  - 49: ds=31 sev=purple
  - 14: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:373, 16:241, 35:197, 29:149, 15:103, 26:90, 2:74, 6:73, 27:57, 25:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=373 fs=0 fl=2 hz=0.0049504950495049506, 16:ds=241 fs=0 fl=1 hz=0.0036900369003690036, 35:ds=197 fs=0 fl=2 hz=0.005154639175257732, 29:ds=149 fs=19 fl=1 hz=0.02442002442002442, 15:ds=103 fs=21 fl=0 hz=0.025059665871121718, 26:ds=90 fs=3 fl=1 hz=0.007109004739336493, 2:ds=74 fs=22 fl=0 hz=0.024017467248908297, 6:ds=73 fs=23 fl=3 hz=0.029213483146067414, 27:ds=57 fs=14 fl=1 hz=0.016985138004246284, 25:ds=53 fs=17 fl=4 hz=0.022364217252396165

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=82 flags=purple
- S2: ds=80 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '4', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 136: score=4 tags=FLT,MIR,RS
  - 469: score=4 tags=FLT,MIR,RS
  - 028: score=3 tags=FLT,RS
  - 037: score=3 tags=FLT,RS
  - 046: score=3 tags=FLT,RS
  - 127: score=3 tags=MIR,RS
  - 145: score=3 tags=FLT,RS
  - 235: score=3 tags=FLT,RS
  - 289: score=3 tags=FLT,RS
  - 379: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=2 last_repeat_gap=14 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=18), P2:2 (gap=25), P3:3 (gap=62)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:3 (ds=62)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 124: score=51.28055214285715 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 126: score=48.92290428571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 144: score=45.131815714285715 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 123: score=43.78541214285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 324: score=40.34415714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 146: score=40.19492857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 326: score=38.294028571428576 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 134: score=36.96044285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 424: score=36.94055357142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 114: score=36.939542857142854 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 344: ds=828 sev=B
- 188: ds=821 sev=B
- 558: ds=778 sev=B
- 115: ds=770 sev=B
- 123: ds=753 sev=B
- 446: ds=730 sev=B
- 335: ds=694 sev=B
- 777: ds=690 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=87 sev=blue
  - 33: ds=62 sev=purple
  - 88: ds=49 sev=purple
  - 00: ds=46 sev=purple
  - 55: ds=39 sev=purple
  - 66: ds=34 sev=purple
  - 44: ds=26 sev=purple
  - 22: ds=12 sev=-
  - 99: ds=7 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 89: ds=76 sev=red
  - 46: ds=73 sev=red
  - 47: ds=65 sev=red
  - 28: ds=64 sev=red
  - 26: ds=48 sev=blue
  - 29: ds=40 sev=blue
  - 15: ds=36 sev=purple
  - 36: ds=34 sev=purple
  - 67: ds=31 sev=purple
  - 03: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:186, 26:183, 1:178, 16:120, 35:98, 33:78, 22:77, 29:74, 20:70, 23:68

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=186 fs=3 fl=2 hz=0.007741935483870969, 26:ds=183 fs=1 fl=0 hz=0.0049382716049382715, 1:ds=178 fs=3 fl=3 hz=0.00857843137254902, 16:ds=120 fs=2 fl=1 hz=0.009174311926605505, 35:ds=98 fs=0 fl=1 hz=0.00487012987012987, 33:ds=78 fs=21 fl=2 hz=0.026744186046511628, 22:ds=77 fs=44 fl=0 hz=0.04851157662624035, 29:ds=74 fs=17 fl=2 hz=0.02132435465768799, 20:ds=70 fs=22 fl=1 hz=0.02481121898597627, 23:ds=68 fs=17 fl=2 hz=0.021300448430493273

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S7: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=3 tags=FLT,RS
  - 049: score=3 tags=FLT,RS
  - 139: score=3 tags=FLT,RS
  - 148: score=3 tags=FLT,RS
  - 238: score=3 tags=FLT,RS
  - 247: score=3 tags=FLT,RS
  - 346: score=3 tags=FLT,RS
  - 058: score=2 tags=RS
  - 067: score=2 tags=RS
  - 157: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=3 last_repeat_gap=21 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=15), P2:4 (gap=30), P3:4 (gap=18)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 124: score=51.28055214285715 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 126: score=48.92290428571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 144: score=45.131815714285715 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 123: score=43.78541214285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 324: score=40.34415714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 146: score=40.19492857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 326: score=38.294028571428576 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 134: score=36.96044285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 424: score=36.94055357142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 114: score=36.939542857142854 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=984 sev=B
- 668: ds=968 sev=B
- 166: ds=863 sev=B
- 378: ds=862 sev=B
- 666: ds=860 sev=B
- 455: ds=854 sev=B
- 225: ds=824 sev=B
- 279: ds=815 sev=B
- 111: ds=779 sev=B
- 222: ds=778 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=63 sev=purple
  - 88: ds=56 sev=purple
  - 22: ds=24 sev=-
  - 66: ds=23 sev=-
  - 11: ds=18 sev=-
  - 33: ds=17 sev=-
  - 55: ds=12 sev=-
  - 77: ds=5 sev=-
  - 00: ds=3 sev=-
  - 99: ds=2 sev=-
- non_repeating:
  - 04: ds=101 sev=red
  - 89: ds=64 sev=red
  - 45: ds=48 sev=blue
  - 46: ds=48 sev=blue
  - 15: ds=41 sev=blue
  - 01: ds=40 sev=blue
  - 13: ds=36 sev=purple
  - 69: ds=34 sev=purple
  - 59: ds=33 sev=purple
  - 35: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:632, 35:298, 32:249, 5:124, 14:104, 29:77, 15:66, 34:63, 27:47, 9:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=632 fs=4 fl=1 hz=0.0154320987654321, 35:ds=298 fs=1 fl=3 hz=0.008032128514056224, 32:ds=249 fs=3 fl=2 hz=0.00946372239747634, 5:ds=124 fs=18 fl=1 hz=0.02328288707799767, 14:ds=104 fs=39 fl=0 hz=0.04426787741203178, 29:ds=77 fs=18 fl=2 hz=0.023781212841854936, 15:ds=66 fs=15 fl=2 hz=0.019653179190751446, 34:ds=63 fs=19 fl=0 hz=0.023086269744835963, 27:ds=47 fs=19 fl=4 hz=0.02454642475987193, 9:ds=46 fs=52 fl=0 hz=0.05573419078242229

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=73 flags=purple
- S23: ds=66 flags=purple
- S20: ds=56 flags=purple
- S0: ds=55 flags=blue+purple
- S10: ds=53 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 127: score=3 tags=MIR,RS
  - 136: score=3 tags=MIR,RS
  - 145: score=3 tags=FLT,RS
  - 235: score=3 tags=FLT,RS
  - 469: score=3 tags=MIR,RS
  - 568: score=3 tags=FLT,RS
  - 015: score=2 tags=FLT,MIR
  - 019: score=2 tags=RS
  - 025: score=2 tags=FLT,MIR
  - 028: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 666 -> combined:827(B); evening:860(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 11 -> combined:36(purple); midday:87(blue)
- 13 -> combined:39(blue); evening:36(purple)
- 15 -> combined:73(red); evening:41(blue); midday:36(purple)
- 23 -> combined:28(purple); midday:28(purple)
- 33 -> combined:34(purple); midday:62(purple)
- 36 -> combined:34(purple); midday:34(purple)
- 37 -> combined:42(blue); midday:28(purple)
- 44 -> combined:53(purple); evening:63(purple); midday:26(purple)
- 46 -> combined:96(red); evening:48(blue); midday:73(red)
- 47 -> combined:32(purple); midday:65(red)
- 49 -> combined:31(purple); evening:30(purple)
- 66 -> combined:46(purple); midday:34(purple)
- 67 -> combined:26(purple); midday:31(purple)
- 88 -> combined:99(blue); evening:56(purple); midday:49(purple)
- 89 -> combined:128(red); evening:64(red); midday:76(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.621885714285714)[R1,XVAR-Cons(CEM)], 3(2.5481714285714285)[R3,XVAR-Cons(CE)], 8(1.2374285714285713)[R1,Double-Pressure], 0(0.264)[R2], 4(0.24779285714285712)[R3,Swap]
- P2: 2(7.054528571428572)[R1,XVAR-Cons(CEM)], 4(3.8817142857142857)[R2,XVAR-Cons(CE)], 3(1.0971)[R2,Double-Pressure], 1(1.0761999999999998)[R2,Double-Pressure], 6(0.3418428571428571)[R3,Swap]
- P3: 4(7.741457142857143)[R1,XVAR-Cons(CEM)], 6(5.691328571428572)[R2,XVAR-Cons(CEM)], 3(3.3978571428571427)[R3,XVAR-Cons(CM)], 7(0.9834999999999999)[R2,Double-Pressure]
