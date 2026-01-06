# Aux Summary — SouthCarolina4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-01/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=044, 653, 976, 754, 463
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-01/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=653, 754, 425, 462, 144
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-01/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=044, 976, 463, 849, 257

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=2 last_repeat_gap=13 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=13), P2:3 (gap=29), P3:1 (gap=15)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=39.28106857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 181: score=38.13224 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 138: score=37.177757142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=36.02892857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 130: score=34.43094285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 180: score=33.282114285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 931: score=33.01389999999999 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 938: score=32.747814285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=32.70227142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=32.24995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 225: ds=999 sev=B
- 233: ds=996 sev=B
- 366: ds=968 sev=B
- 449: ds=897 sev=B
- 156: ds=880 sev=B
- 778: ds=850 sev=B
- 279: ds=849 sev=B
- 033: ds=781 sev=B
- 004: ds=769 sev=B
- 688: ds=736 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=177 sev=red
  - 55: ds=114 sev=red
  - 77: ds=98 sev=blue
  - 33: ds=85 sev=blue
  - 88: ds=80 sev=blue
  - 22: ds=60 sev=purple
  - 66: ds=48 sev=purple
  - 00: ds=21 sev=-
  - 11: ds=17 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 15: ds=56 sev=red
  - 18: ds=54 sev=blue
  - 78: ds=49 sev=blue
  - 05: ds=45 sev=blue
  - 68: ds=37 sev=blue
  - 29: ds=30 sev=purple
  - 09: ds=25 sev=purple
  - 06: ds=23 sev=-
  - 16: ds=23 sev=-
  - 08: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:441, 35:384, 1:165, 26:153, 31:115, 4:106, 23:104, 28:98, 27:81, 19:65

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=441 fs=0 fl=0 hz=0.002197802197802198, 35:ds=384 fs=0 fl=0 hz=0.001949317738791423, 1:ds=165 fs=6 fl=4 hz=0.012195121951219513, 26:ds=153 fs=2 fl=0 hz=0.0062402496099844, 31:ds=115 fs=27 fl=0 hz=0.03085714285714286, 4:ds=106 fs=21 fl=2 hz=0.026589595375722544, 23:ds=104 fs=25 fl=1 hz=0.029850746268656716, 28:ds=98 fs=16 fl=2 hz=0.021479713603818614, 27:ds=81 fs=26 fl=0 hz=0.02911534154535274, 19:ds=65 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=90 flags=red+purple
- S0: ds=63 flags=blue+purple
- S23: ds=52 flags=blue+purple
- S5: ds=51 flags=purple
- S24: ds=49 flags=blue+purple
- S4: ds=41 flags=purple
- S3: ds=40 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '8'], 'pairs': {'remaining_count': 0}}
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
- current_index=8 streak=1 max=3 last_repeat_gap=2 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=29), P2:3 (gap=38), P3:9 (gap=23)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=39.28106857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 181: score=38.13224 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 138: score=37.177757142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=36.02892857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 130: score=34.43094285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 180: score=33.282114285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 931: score=33.01389999999999 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 938: score=32.747814285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=32.70227142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=32.24995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=876 sev=B
- 555: ds=871 sev=B
- 222: ds=848 sev=B
- 337: ds=825 sev=B
- 003: ds=816 sev=B
- 228: ds=807 sev=B
- 556: ds=709 sev=B
- 449: ds=667 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=111 sev=red
  - 55: ds=75 sev=blue
  - 77: ds=44 sev=purple
  - 33: ds=38 sev=purple
  - 88: ds=36 sev=purple
  - 22: ds=34 sev=purple
  - 66: ds=21 sev=-
  - 00: ds=12 sev=-
  - 11: ds=7 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 49: ds=52 sev=blue
  - 67: ds=46 sev=blue
  - 34: ds=45 sev=blue
  - 09: ds=42 sev=blue
  - 27: ds=39 sev=blue
  - 07: ds=30 sev=purple
  - 05: ds=27 sev=purple
  - 15: ds=25 sev=purple
  - 18: ds=24 sev=-
  - 78: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:412, 26:190, 35:176, 27:141, 6:109, 5:78, 1:75, 15:70, 34:56, 31:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=412 fs=1 fl=2 hz=0.006993006993006993, 26:ds=190 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=176 fs=1 fl=1 hz=0.004968944099378882, 27:ds=141 fs=18 fl=3 hz=0.026582278481012658, 6:ds=109 fs=24 fl=2 hz=0.02957906712172924, 5:ds=78 fs=20 fl=1 hz=0.023102310231023104, 1:ds=75 fs=7 fl=3 hz=0.012127894156560088, 15:ds=70 fs=17 fl=3 hz=0.021691973969631236, 34:ds=56 fs=28 fl=1 hz=0.03159041394335512, 31:ds=52 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=79 flags=purple
- S25: ds=76 flags=purple
- S21: ds=56 flags=purple
- S20: ds=52 flags=purple
- S17: ds=50 flags=purple
- S8: ds=48 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=3 tags=FLT,RS
  - 026: score=3 tags=FLT,RS
  - 035: score=3 tags=FLT,RS
  - 089: score=3 tags=FLT,RS
  - 179: score=3 tags=FLT,RS
  - 269: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 359: score=3 tags=FLT,RS
  - 368: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=3 last_repeat_gap=29 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=15), P2:8 (gap=19), P3:1 (gap=22)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 131: score=39.28106857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 181: score=38.13224 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 138: score=37.177757142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=36.02892857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 130: score=34.43094285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 180: score=33.282114285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 931: score=33.01389999999999 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 938: score=32.747814285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=32.70227142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 136: score=32.24995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=979 sev=B
- 117: ds=890 sev=B
- 005: ds=876 sev=B
- 577: ds=853 sev=B
- 155: ds=833 sev=B
- 777: ds=832 sev=B
- 669: ds=824 sev=B
- 179: ds=806 sev=B
- 366: ds=772 sev=B
- 222: ds=766 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=96 sev=blue
  - 77: ds=83 sev=blue
  - 66: ds=75 sev=blue
  - 33: ds=71 sev=blue
  - 55: ds=62 sev=purple
  - 88: ds=56 sev=purple
  - 22: ds=33 sev=purple
  - 11: ds=22 sev=-
  - 00: ds=12 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 58: ds=97 sev=red
  - 35: ds=64 sev=red
  - 29: ds=59 sev=red
  - 47: ds=49 sev=blue
  - 15: ds=45 sev=blue
  - 18: ds=31 sev=purple
  - 19: ds=31 sev=purple
  - 78: ds=27 sev=purple
  - 05: ds=25 sev=purple
  - 08: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:484, 1:271, 32:238, 31:217, 4:137, 28:110, 19:106, 23:101, 26:83, 16:79

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=484 fs=3 fl=1 hz=0.017391304347826087, 1:ds=271 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=238 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=217 fs=16 fl=1 hz=0.021935483870967745, 4:ds=137 fs=21 fl=3 hz=0.028742514970059883, 28:ds=110 fs=10 fl=4 hz=0.017676767676767676, 19:ds=106 fs=12 fl=2 hz=0.016968325791855206, 23:ds=101 fs=24 fl=0 hz=0.02937576499388005, 26:ds=83 fs=0 fl=0 hz=0.002347417840375587, 16:ds=79 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=62 flags=purple
- S15: ds=53 flags=red+purple
- S9: ds=50 flags=purple
- S17: ds=49 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 126: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 189: score=3 tags=FLT,RS
  - 027: score=2 tags=RS
  - 036: score=2 tags=RS
  - 045: score=2 tags=RS
  - 234: score=2 tags=RS
  - 279: score=2 tags=RS
  - 369: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:766(B); midday:848(B)
- 366 -> combined:968(B); evening:772(B)
- 449 -> combined:897(B); midday:667(B)
- 688 -> combined:736(B); evening:731(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:45(blue); evening:25(purple); midday:27(purple)
- 09 -> combined:25(purple); midday:42(blue)
- 15 -> combined:56(red); evening:45(blue); midday:25(purple)
- 18 -> combined:54(blue); evening:31(purple)
- 22 -> combined:60(purple); evening:33(purple); midday:34(purple)
- 29 -> combined:30(purple); evening:59(red)
- 33 -> combined:85(blue); evening:71(blue); midday:38(purple)
- 55 -> combined:114(red); evening:62(purple); midday:75(blue)
- 66 -> combined:48(purple); evening:75(blue)
- 77 -> combined:98(blue); evening:83(blue); midday:44(purple)
- 78 -> combined:49(blue); evening:27(purple)
- 88 -> combined:80(blue); evening:56(purple); midday:36(purple)
- 99 -> combined:177(red); evening:96(blue); midday:111(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(2.4958)[R3,XVAR-Cons(CE)], 9(1.5658571428571428)[R1,Double-Pressure], 6(1.1618571428571427)[R1,Mirror-Echo], 5(1.0085714285714285)[R1,Double-Pressure], 3(0.942)[R2,Double-Pressure]
- P2: 3(8.819757142857142)[R1,Mirror-Echo], 8(7.670928571428572)[R2,Mirror-Echo], 9(1.8599357142857142)[R3,XVAR-Cons(CE)], 7(0.5598)[R2,Swap]
- P3: 1(3.628285714285714)[R1,XVAR-Cons(CE)], 8(3.3622)[R2,XVAR-Cons(CE)], 0(1.6153857142857144)[R3,XVAR-Cons(CM)], 9(1.3867142857142856)[R1,Double-Pressure], 6(0.9343999999999999)[R2,Double-Pressure]
