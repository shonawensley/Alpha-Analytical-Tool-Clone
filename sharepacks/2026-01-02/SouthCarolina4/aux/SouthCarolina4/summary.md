# Aux Summary — SouthCarolina4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-02/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=821, 910, 044, 653, 976
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-02/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=910, 653, 754, 425, 462
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-02/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=821, 044, 976, 463, 849

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=15 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=15), P2:3 (gap=31), P3:8 (gap=15)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 138: score=40.02653392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 132: score=39.54705892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 188: score=38.70759892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 137: score=37.737450714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 182: score=36.30706428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 187: score=34.60305714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 638: score=33.88312142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 632: score=33.59662142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=33.23711142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 688: score=32.736221428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 233: ds=998 sev=B
- 366: ds=970 sev=B
- 449: ds=899 sev=B
- 156: ds=882 sev=B
- 778: ds=852 sev=B
- 279: ds=851 sev=B
- 033: ds=783 sev=B
- 004: ds=771 sev=B
- 688: ds=738 sev=B
- 278: ds=705 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=179 sev=red
  - 55: ds=116 sev=red
  - 77: ds=100 sev=blue
  - 33: ds=87 sev=blue
  - 88: ds=82 sev=blue
  - 22: ds=62 sev=purple
  - 66: ds=50 sev=purple
  - 00: ds=23 sev=-
  - 11: ds=19 sev=-
  - 44: ds=2 sev=-
- non_repeating:
  - 15: ds=58 sev=red
  - 78: ds=51 sev=blue
  - 05: ds=47 sev=blue
  - 68: ds=39 sev=blue
  - 29: ds=32 sev=purple
  - 06: ds=25 sev=purple
  - 16: ds=25 sev=purple
  - 08: ds=24 sev=-
  - 38: ds=24 sev=-
  - 59: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:443, 35:386, 1:167, 26:155, 31:117, 4:108, 23:106, 28:100, 27:83, 19:67

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=443 fs=0 fl=0 hz=0.002197802197802198, 35:ds=386 fs=0 fl=0 hz=0.001949317738791423, 1:ds=167 fs=6 fl=4 hz=0.012195121951219513, 26:ds=155 fs=2 fl=0 hz=0.0062402496099844, 31:ds=117 fs=27 fl=0 hz=0.03085714285714286, 4:ds=108 fs=21 fl=2 hz=0.026589595375722544, 23:ds=106 fs=25 fl=1 hz=0.029850746268656716, 28:ds=100 fs=16 fl=2 hz=0.021479713603818614, 27:ds=83 fs=26 fl=0 hz=0.02911534154535274, 19:ds=67 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=92 flags=red+purple
- S0: ds=65 flags=blue+purple
- S23: ds=54 flags=purple
- S5: ds=53 flags=purple
- S24: ds=51 flags=blue+purple
- S4: ds=43 flags=purple
- S3: ds=42 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=3 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=13), P2:3 (gap=39), P3:9 (gap=24)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 138: score=40.02653392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 132: score=39.54705892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 188: score=38.70759892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 137: score=37.737450714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 182: score=36.30706428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 187: score=34.60305714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 638: score=33.88312142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 632: score=33.59662142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=33.23711142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 688: score=32.736221428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=877 sev=B
- 555: ds=872 sev=B
- 222: ds=849 sev=B
- 337: ds=826 sev=B
- 003: ds=817 sev=B
- 228: ds=808 sev=B
- 556: ds=710 sev=B
- 449: ds=668 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=112 sev=red
  - 55: ds=76 sev=blue
  - 77: ds=45 sev=purple
  - 33: ds=39 sev=purple
  - 88: ds=37 sev=purple
  - 22: ds=35 sev=purple
  - 66: ds=22 sev=-
  - 00: ds=13 sev=-
  - 11: ds=8 sev=-
  - 44: ds=5 sev=-
- non_repeating:
  - 49: ds=53 sev=blue
  - 67: ds=47 sev=blue
  - 34: ds=46 sev=blue
  - 27: ds=40 sev=blue
  - 07: ds=31 sev=purple
  - 05: ds=28 sev=purple
  - 15: ds=26 sev=purple
  - 18: ds=25 sev=purple
  - 78: ds=25 sev=purple
  - 69: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:413, 26:191, 35:177, 27:142, 6:110, 5:79, 1:76, 15:71, 34:57, 31:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=413 fs=1 fl=2 hz=0.006993006993006993, 26:ds=191 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=177 fs=1 fl=1 hz=0.004968944099378882, 27:ds=142 fs=18 fl=3 hz=0.026582278481012658, 6:ds=110 fs=24 fl=2 hz=0.02957906712172924, 5:ds=79 fs=20 fl=1 hz=0.023102310231023104, 1:ds=76 fs=7 fl=3 hz=0.012127894156560088, 15:ds=71 fs=17 fl=3 hz=0.021691973969631236, 34:ds=57 fs=28 fl=1 hz=0.03159041394335512, 31:ds=53 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=80 flags=purple
- S25: ds=77 flags=purple
- S21: ds=57 flags=purple
- S20: ds=53 flags=purple
- S17: ds=51 flags=purple
- S8: ds=49 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 089: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 368: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 017: score=2 tags=RS
  - 026: score=2 tags=RS
  - 035: score=2 tags=RS
  - 125: score=2 tags=RS
  - 134: score=2 tags=RS
  - 179: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=30 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=16), P2:8 (gap=20), P3:8 (gap=19)
- consensus_notes: P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 138: score=40.02653392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 132: score=39.54705892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 188: score=38.70759892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 137: score=37.737450714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 182: score=36.30706428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 187: score=34.60305714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 638: score=33.88312142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 632: score=33.59662142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=33.23711142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 688: score=32.736221428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=980 sev=B
- 117: ds=891 sev=B
- 005: ds=877 sev=B
- 577: ds=854 sev=B
- 155: ds=834 sev=B
- 777: ds=833 sev=B
- 669: ds=825 sev=B
- 179: ds=807 sev=B
- 366: ds=773 sev=B
- 222: ds=767 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=97 sev=blue
  - 77: ds=84 sev=blue
  - 66: ds=76 sev=blue
  - 33: ds=72 sev=blue
  - 55: ds=63 sev=purple
  - 88: ds=57 sev=purple
  - 22: ds=34 sev=purple
  - 11: ds=23 sev=-
  - 00: ds=13 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 58: ds=98 sev=red
  - 35: ds=65 sev=red
  - 29: ds=60 sev=red
  - 47: ds=50 sev=blue
  - 15: ds=46 sev=blue
  - 19: ds=32 sev=purple
  - 78: ds=28 sev=purple
  - 05: ds=26 sev=purple
  - 08: ds=25 sev=purple
  - 68: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:485, 1:272, 32:239, 31:218, 4:138, 28:111, 19:107, 23:102, 26:84, 16:80

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=485 fs=3 fl=1 hz=0.017391304347826087, 1:ds=272 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=239 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=218 fs=16 fl=1 hz=0.021935483870967745, 4:ds=138 fs=21 fl=3 hz=0.028742514970059883, 28:ds=111 fs=10 fl=4 hz=0.017676767676767676, 19:ds=107 fs=12 fl=2 hz=0.016968325791855206, 23:ds=102 fs=24 fl=0 hz=0.02937576499388005, 26:ds=84 fs=0 fl=0 hz=0.002347417840375587, 16:ds=80 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=63 flags=purple
- S15: ds=54 flags=red+purple
- S9: ds=51 flags=purple
- S17: ds=50 flags=purple

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
- 222 -> evening:767(B); midday:849(B)
- 366 -> combined:970(B); evening:773(B)
- 449 -> combined:899(B); midday:668(B)
- 688 -> combined:738(B); evening:732(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:47(blue); evening:26(purple); midday:28(purple)
- 15 -> combined:58(red); evening:46(blue); midday:26(purple)
- 22 -> combined:62(purple); evening:34(purple); midday:35(purple)
- 29 -> combined:32(purple); evening:60(red)
- 33 -> combined:87(blue); evening:72(blue); midday:39(purple)
- 55 -> combined:116(red); evening:63(purple); midday:76(blue)
- 66 -> combined:50(purple); evening:76(blue)
- 68 -> combined:39(blue); evening:25(purple)
- 77 -> combined:100(blue); evening:84(blue); midday:45(purple)
- 78 -> combined:51(blue); evening:28(purple); midday:25(purple)
- 88 -> combined:82(blue); evening:57(purple); midday:37(purple)
- 99 -> combined:179(red); evening:97(blue); midday:112(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(2.558557142857143)[R3,XVAR-Cons(CE)], 6(1.2012142857142856)[R1,Mirror-Echo], 5(1.0714285714285714)[R1,Double-Pressure], 0(0.9881428571428571)[R1,Double-Pressure], 3(0.986)[R2,Double-Pressure]
- P2: 3(8.943192857142858)[R1,Mirror-Echo], 8(7.7962928571428565)[R2,Mirror-Echo], 9(1.901657142857143)[R3,XVAR-Cons(CE)], 7(1.1806999999999999)[R2,Double-Pressure]
- P3: 8(3.738714285714286)[R1,XVAR-Cons(CE)], 2(2.4522142857142857)[R2,Mirror-Echo], 7(1.7482071428571428)[R3,Mirror-Echo], 6(0.9552999999999999)[R2,Double-Pressure], 5(0.8299)[R2,Double-Pressure]
