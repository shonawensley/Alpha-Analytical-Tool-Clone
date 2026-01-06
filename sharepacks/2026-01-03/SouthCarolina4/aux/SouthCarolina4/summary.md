# Aux Summary — SouthCarolina4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-03/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=084, 308, 821, 910, 044
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-03/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=308, 910, 653, 754, 425
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-03/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=084, 821, 044, 976, 463

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=2 last_repeat_gap=17 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=17), P2:3 (gap=33), P3:2 (gap=12)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=38.27910714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=38.15195714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 232: score=37.69672642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 139: score=37.59202857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.047914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 239: score=35.48798571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 138: score=33.401314285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=33.18037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 135: score=32.954971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 238: score=31.297271428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 366: ds=972 sev=B
- 449: ds=901 sev=B
- 156: ds=884 sev=B
- 778: ds=854 sev=B
- 279: ds=853 sev=B
- 033: ds=785 sev=B
- 004: ds=773 sev=B
- 688: ds=740 sev=B
- 278: ds=707 sev=B
- 377: ds=687 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=181 sev=red
  - 55: ds=118 sev=red
  - 77: ds=102 sev=blue
  - 33: ds=89 sev=blue
  - 88: ds=84 sev=blue
  - 22: ds=64 sev=purple
  - 66: ds=52 sev=purple
  - 00: ds=25 sev=purple
  - 11: ds=21 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 15: ds=60 sev=red
  - 78: ds=53 sev=blue
  - 05: ds=49 sev=blue
  - 68: ds=41 sev=blue
  - 29: ds=34 sev=purple
  - 06: ds=27 sev=purple
  - 16: ds=27 sev=purple
  - 59: ds=23 sev=-
  - 17: ds=21 sev=-
  - 13: ds=19 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:445, 35:388, 1:169, 26:157, 31:119, 4:110, 23:108, 28:102, 27:85, 19:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=445 fs=0 fl=0 hz=0.002197802197802198, 35:ds=388 fs=0 fl=0 hz=0.001949317738791423, 1:ds=169 fs=6 fl=4 hz=0.012195121951219513, 26:ds=157 fs=2 fl=0 hz=0.0062402496099844, 31:ds=119 fs=27 fl=0 hz=0.03085714285714286, 4:ds=110 fs=21 fl=2 hz=0.026589595375722544, 23:ds=108 fs=25 fl=1 hz=0.029850746268656716, 28:ds=102 fs=16 fl=2 hz=0.021479713603818614, 27:ds=85 fs=26 fl=0 hz=0.02911534154535274, 19:ds=69 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=94 flags=red+purple
- S0: ds=67 flags=blue+purple
- S23: ds=56 flags=purple
- S5: ds=55 flags=purple
- S24: ds=53 flags=blue+purple
- S4: ds=45 flags=purple
- S3: ds=44 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 045: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=13 streak=1 max=3 last_repeat_gap=4 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=14), P2:3 (gap=40), P3:9 (gap=25)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:3 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=38.27910714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=38.15195714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 232: score=37.69672642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 139: score=37.59202857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.047914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 239: score=35.48798571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 138: score=33.401314285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=33.18037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 135: score=32.954971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 238: score=31.297271428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=878 sev=B
- 555: ds=873 sev=B
- 222: ds=850 sev=B
- 337: ds=827 sev=B
- 003: ds=818 sev=B
- 228: ds=809 sev=B
- 556: ds=711 sev=B
- 449: ds=669 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=113 sev=red
  - 55: ds=77 sev=blue
  - 77: ds=46 sev=purple
  - 33: ds=40 sev=purple
  - 88: ds=38 sev=purple
  - 22: ds=36 sev=purple
  - 66: ds=23 sev=-
  - 00: ds=14 sev=-
  - 11: ds=9 sev=-
  - 44: ds=6 sev=-
- non_repeating:
  - 49: ds=54 sev=blue
  - 67: ds=48 sev=blue
  - 34: ds=47 sev=blue
  - 27: ds=41 sev=blue
  - 07: ds=32 sev=purple
  - 05: ds=29 sev=purple
  - 15: ds=27 sev=purple
  - 18: ds=26 sev=purple
  - 78: ds=26 sev=purple
  - 69: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:414, 26:192, 35:178, 27:143, 6:111, 5:80, 1:77, 15:72, 34:58, 31:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=414 fs=1 fl=2 hz=0.006993006993006993, 26:ds=192 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=178 fs=1 fl=1 hz=0.004968944099378882, 27:ds=143 fs=18 fl=3 hz=0.026582278481012658, 6:ds=111 fs=24 fl=2 hz=0.02957906712172924, 5:ds=80 fs=20 fl=1 hz=0.023102310231023104, 1:ds=77 fs=7 fl=3 hz=0.012127894156560088, 15:ds=72 fs=17 fl=3 hz=0.021691973969631236, 34:ds=58 fs=28 fl=1 hz=0.03159041394335512, 31:ds=54 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=81 flags=purple
- S25: ds=78 flags=purple
- S21: ds=58 flags=purple
- S20: ds=54 flags=purple
- S17: ds=52 flags=purple
- S8: ds=50 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [8], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 035: score=3 tags=MIR,RS
  - 134: score=3 tags=PAT,RS
  - 278: score=3 tags=MIR,RS
  - 368: score=3 tags=MIR,RS
  - 017: score=2 tags=RS
  - 026: score=2 tags=RS
  - 089: score=2 tags=RS
  - 125: score=2 tags=RS
  - 179: score=2 tags=RS
  - 269: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=31 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=17), P2:3 (gap=18), P3:8 (gap=20)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=38.27910714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=38.15195714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 232: score=37.69672642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 139: score=37.59202857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.047914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 239: score=35.48798571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 138: score=33.401314285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=33.18037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 135: score=32.954971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 238: score=31.297271428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=981 sev=B
- 117: ds=892 sev=B
- 005: ds=878 sev=B
- 577: ds=855 sev=B
- 155: ds=835 sev=B
- 777: ds=834 sev=B
- 669: ds=826 sev=B
- 179: ds=808 sev=B
- 366: ds=774 sev=B
- 222: ds=768 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=98 sev=blue
  - 77: ds=85 sev=blue
  - 66: ds=77 sev=blue
  - 33: ds=73 sev=blue
  - 55: ds=64 sev=purple
  - 88: ds=58 sev=purple
  - 22: ds=35 sev=purple
  - 11: ds=24 sev=-
  - 00: ds=14 sev=-
  - 44: ds=2 sev=-
- non_repeating:
  - 58: ds=99 sev=red
  - 35: ds=66 sev=red
  - 29: ds=61 sev=red
  - 47: ds=51 sev=blue
  - 15: ds=47 sev=blue
  - 19: ds=33 sev=purple
  - 78: ds=29 sev=purple
  - 05: ds=27 sev=purple
  - 68: ds=26 sev=purple
  - 38: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:486, 1:273, 32:240, 31:219, 4:139, 28:112, 19:108, 23:103, 26:85, 16:81

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=486 fs=3 fl=1 hz=0.017391304347826087, 1:ds=273 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=240 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=219 fs=16 fl=1 hz=0.021935483870967745, 4:ds=139 fs=21 fl=3 hz=0.028742514970059883, 28:ds=112 fs=10 fl=4 hz=0.017676767676767676, 19:ds=108 fs=12 fl=2 hz=0.016968325791855206, 23:ds=103 fs=24 fl=0 hz=0.02937576499388005, 26:ds=85 fs=0 fl=0 hz=0.002347417840375587, 16:ds=81 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=64 flags=purple
- S15: ds=55 flags=red+purple
- S9: ds=52 flags=purple
- S17: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 045: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 567: score=3 tags=FLT,RS
  - 018: score=2 tags=RS
  - 027: score=2 tags=RS
  - 036: score=2 tags=RS
  - 126: score=2 tags=RS
  - 189: score=2 tags=RS
  - 234: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:768(B); midday:850(B)
- 366 -> combined:972(B); evening:774(B)
- 449 -> combined:901(B); midday:669(B)
- 688 -> combined:740(B); evening:733(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:49(blue); evening:27(purple); midday:29(purple)
- 15 -> combined:60(red); evening:47(blue); midday:27(purple)
- 22 -> combined:64(purple); evening:35(purple); midday:36(purple)
- 29 -> combined:34(purple); evening:61(red)
- 33 -> combined:89(blue); evening:73(blue); midday:40(purple)
- 55 -> combined:118(red); evening:64(purple); midday:77(blue)
- 66 -> combined:52(purple); evening:77(blue)
- 68 -> combined:41(blue); evening:26(purple)
- 77 -> combined:102(blue); evening:85(blue); midday:46(purple)
- 78 -> combined:53(blue); evening:29(purple); midday:26(purple)
- 88 -> combined:84(blue); evening:58(purple); midday:38(purple)
- 99 -> combined:181(red); evening:98(blue); midday:113(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(3.501314285714286)[R2,XVAR-Cons(CE)], 2(2.3972714285714285)[R3,XVAR-Cons(CM)], 6(1.3405714285714285)[R1,Mirror-Echo], 5(1.1342857142857143)[R1,Double-Pressure], 0(1.018)[R1,Double-Pressure]
- P2: 3(8.602857142857143)[R1,XVAR-Cons(CEM)], 9(3.3897)[R2,XVAR-Cons(CE)], 7(1.2016)[R2,Double-Pressure], 8(0.7362285714285715)[R3,Mirror-Echo], 1(0.23435714285714285)[R3,Swap]
- P3: 9(2.987857142857143)[R3,XVAR-Cons(CM)], 2(2.674935714285714)[R1,Mirror-Echo], 7(2.5477857142857143)[R2,Mirror-Echo], 8(1.2971428571428572)[R1,Double-Pressure], 6(1.0761999999999998)[R2,Double-Pressure]
