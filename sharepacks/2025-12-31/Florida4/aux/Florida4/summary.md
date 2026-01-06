# Aux Summary — Florida4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/Florida4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Florida
- combined: live=`data/cleaned/draws/Florida_draws.csv` snap=`sharepacks/2025-12-31/Florida4/aux/draws/Florida_draws.csv` n=1000 head=870, 377, 208, 522, 003
- midday: live=`data/cleaned/draws/Florida_Midday_draws.csv` snap=`sharepacks/2025-12-31/Florida4/aux/draws/Florida_Midday_draws.csv` n=1000 head=377, 522, 909, 452, 945
- evening: live=`data/cleaned/draws/Florida_Evening_draws.csv` snap=`sharepacks/2025-12-31/Florida4/aux/draws/Florida_Evening_draws.csv` n=1000 head=870, 208, 003, 985, 346

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=2 last_repeat_gap=25 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=31), P2:6 (gap=24), P3:1 (gap=21)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 761: score=51.96712071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 791: score=48.53754285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 661: score=40.81852857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 691: score=40.58031428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 767: score=40.44915714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 797: score=40.210942857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 760: score=38.063271428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 781: score=38.06024285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 751: score=37.879442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=37.82505714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 244: ds=997 sev=B
- 369: ds=865 sev=B
- 447: ds=749 sev=B
- 668: ds=739 sev=B
- 388: ds=730 sev=B
- 199: ds=729 sev=B
- 777: ds=721 sev=B
- 335: ds=694 sev=B
- 155: ds=683 sev=B
- 266: ds=668 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=59 sev=purple
  - 44: ds=42 sev=purple
  - 66: ds=37 sev=purple
  - 33: ds=24 sev=-
  - 11: ds=20 sev=-
  - 55: ds=18 sev=-
  - 99: ds=5 sev=-
  - 00: ds=4 sev=-
  - 22: ds=3 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 27: ds=76 sev=red
  - 57: ds=68 sev=red
  - 39: ds=62 sev=red
  - 26: ds=53 sev=blue
  - 79: ds=47 sev=blue
  - 67: ds=46 sev=blue
  - 38: ds=43 sev=blue
  - 05: ds=41 sev=blue
  - 19: ds=36 sev=purple
  - 29: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:463, 26:276, 16:165, 35:135, 31:123, 29:116, 33:91, 5:86, 7:75, 1:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=463 fs=0 fl=0 hz=0.003745318352059925, 26:ds=276 fs=2 fl=0 hz=0.006198347107438016, 16:ds=165 fs=1 fl=1 hz=0.005235602094240838, 35:ds=135 fs=1 fl=1 hz=0.007281553398058252, 31:ds=123 fs=18 fl=1 hz=0.021739130434782608, 29:ds=116 fs=23 fl=0 hz=0.03083109919571046, 33:ds=91 fs=14 fl=2 hz=0.017837235228539576, 5:ds=86 fs=19 fl=2 hz=0.024734982332155476, 7:ds=75 fs=40 fl=1 hz=0.04581005586592179, 1:ds=51 fs=4 fl=5 hz=0.00986842105263158

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S14: ds=44 flags=red+purple
- S16: ds=43 flags=purple
- S2: ds=40 flags=blue+purple
- S5: ds=35 flags=purple
- S23: ds=28 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '6', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=3 tags=FLT,RS
  - 059: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 149: score=3 tags=FLT,RS
  - 158: score=3 tags=FLT,RS
  - 167: score=3 tags=FLT,RS
  - 239: score=3 tags=FLT,RS
  - 248: score=3 tags=FLT,RS
  - 347: score=3 tags=FLT,RS
  - 356: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=2 last_repeat_gap=17 last_repeat_index=20

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=30), P2:9 (gap=23), P3:0 (gap=37)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 761: score=51.96712071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 791: score=48.53754285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 661: score=40.81852857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 691: score=40.58031428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 767: score=40.44915714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 797: score=40.210942857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 760: score=38.063271428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 781: score=38.06024285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 751: score=37.879442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=37.82505714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=982 sev=B
- 339: ds=869 sev=B
- 228: ds=809 sev=B
- 117: ds=791 sev=B
- 999: ds=781 sev=B
- 455: ds=735 sev=B
- 277: ds=723 sev=B
- 788: ds=696 sev=B
- 167: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=80 sev=blue
  - 00: ds=65 sev=purple
  - 11: ds=60 sev=purple
  - 88: ds=29 sev=purple
  - 55: ds=25 sev=purple
  - 66: ds=18 sev=-
  - 33: ds=12 sev=-
  - 99: ds=2 sev=-
  - 22: ds=1 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 15: ds=111 sev=red
  - 39: ds=96 sev=red
  - 19: ds=74 sev=red
  - 29: ds=61 sev=red
  - 18: ds=57 sev=red
  - 57: ds=48 sev=blue
  - 27: ds=39 sev=blue
  - 01: ds=37 sev=blue
  - 78: ds=35 sev=purple
  - 28: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:330, 32:231, 25:135, 16:82, 29:78, 5:75, 35:67, 3:65, 31:61, 14:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=330 fs=2 fl=0 hz=0.006125574272588055, 32:ds=231 fs=2 fl=0 hz=0.006289308176100629, 25:ds=135 fs=20 fl=1 hz=0.02602230483271375, 16:ds=82 fs=0 fl=2 hz=0.004524886877828055, 29:ds=78 fs=22 fl=2 hz=0.027149321266968323, 5:ds=75 fs=20 fl=3 hz=0.024918743228602384, 35:ds=67 fs=2 fl=1 hz=0.005506607929515419, 3:ds=65 fs=27 fl=0 hz=0.02944383860414395, 31:ds=61 fs=22 fl=1 hz=0.02619589977220957, 14:ds=53 fs=54 fl=0 hz=0.057203389830508475

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=65 flags=purple
- S23: ds=55 flags=purple
- S7: ds=47 flags=purple
- S4: ds=42 flags=blue+purple
- S3: ds=37 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '6', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=2 max=2 last_repeat_gap=1 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=44), P2:6 (gap=12), P3:7 (gap=23)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:7 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 761: score=51.96712071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 791: score=48.53754285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 661: score=40.81852857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 691: score=40.58031428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 767: score=40.44915714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 797: score=40.210942857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 760: score=38.063271428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 781: score=38.06024285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 751: score=37.879442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=37.82505714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=998 sev=B
- 133: ds=960 sev=B
- 889: ds=919 sev=B
- 189: ds=860 sev=B
- 022: ds=848 sev=B
- 077: ds=813 sev=B
- 448: ds=780 sev=B
- 449: ds=775 sev=B
- 009: ds=770 sev=B
- 366: ds=726 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=101 sev=blue
  - 88: ds=73 sev=blue
  - 66: ds=23 sev=-
  - 44: ds=21 sev=-
  - 33: ds=12 sev=-
  - 11: ds=10 sev=-
  - 55: ds=9 sev=-
  - 99: ds=8 sev=-
  - 22: ds=7 sev=-
  - 00: ds=2 sev=-
- non_repeating:
  - 35: ds=123 sev=red
  - 25: ds=106 sev=red
  - 79: ds=72 sev=red
  - 49: ds=61 sev=red
  - 38: ds=55 sev=blue
  - 47: ds=53 sev=blue
  - 05: ds=44 sev=blue
  - 17: ds=41 sev=blue
  - 23: ds=38 sev=blue
  - 27: ds=38 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:676, 32:365, 26:138, 31:125, 16:102, 10:101, 20:94, 1:89, 33:84, 29:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=676 fs=1 fl=0 hz=0.010101010101010102, 32:ds=365 fs=4 fl=1 hz=0.010273972602739727, 26:ds=138 fs=3 fl=2 hz=0.008130081300813009, 31:ds=125 fs=19 fl=1 hz=0.024154589371980676, 16:ds=102 fs=1 fl=2 hz=0.006042296072507553, 10:ds=101 fs=8 fl=3 hz=0.013793103448275862, 20:ds=94 fs=20 fl=2 hz=0.026537997587454766, 1:ds=89 fs=2 fl=2 hz=0.010498687664041995, 33:ds=84 fs=16 fl=1 hz=0.019362186788154895, 29:ds=58 fs=27 fl=2 hz=0.031115879828326178

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S18: ds=76 flags=red+purple
- S21: ds=48 flags=purple
- S5: ds=39 flags=purple
- S17: ds=30 flags=purple
- S16: ds=29 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 2}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 123: score=1 tags=FLT
  - 124: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 244 -> combined:997(B); evening:710(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:41(blue); evening:44(blue)
- 17 -> combined:29(purple); evening:41(blue)
- 18 -> combined:30(purple); midday:57(red)
- 19 -> combined:36(purple); midday:74(red)
- 26 -> combined:53(blue); evening:29(purple); midday:26(purple)
- 27 -> combined:76(red); evening:38(blue); midday:39(blue)
- 29 -> combined:36(purple); midday:61(red)
- 35 -> combined:27(purple); evening:123(red)
- 38 -> combined:43(blue); evening:55(blue)
- 39 -> combined:62(red); evening:31(purple); midday:96(red)
- 44 -> combined:42(purple); midday:80(blue)
- 57 -> combined:68(red); evening:34(purple); midday:48(blue)
- 79 -> combined:47(blue); evening:72(red)
- 88 -> combined:59(purple); evening:73(blue); midday:29(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.093857142857143)[R1,XVAR-Cons(CEM)], 6(2.6366285714285715)[R2,Mirror-Echo], 8(1.5657142857142856)[R1,Double-Pressure], 5(0.7880999999999999)[R2,Double-Pressure], 1(0.3997142857142857)[R3,Mirror-Echo]
- P2: 6(6.754414285714285)[R1,XVAR-Cons(CEM)], 9(6.5161999999999995)[R2,XVAR-Cons(CEM)], 8(1.0389)[R2,Double-Pressure], 5(0.8581)[R2,Double-Pressure], 3(0.26971428571428574)[R3,Swap]
- P3: 1(6.427485714285714)[R1,Mirror-Echo], 0(1.7149999999999999)[R1,Double-Pressure], 7(1.2867142857142857)[R1,Double-Pressure], 3(1.0761999999999998)[R2,Double-Pressure], 4(0.9339999999999999)[R2,Double-Pressure]
