# Aux Summary — SouthCarolina4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2026-01-04/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=051, 189, 084, 308, 821
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-04/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=189, 308, 910, 653, 754
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-04/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=051, 084, 821, 044, 976

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=19 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=19), P2:3 (gap=35), P3:2 (gap=14)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 232: score=37.81806285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.58678571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=35.31129857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 235: score=34.59815714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 297: score=34.08002142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 637: score=33.31811428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 632: score=32.77344285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 236: score=32.093135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 295: score=32.09139285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 635: score=31.329485714285717 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 366: ds=974 sev=B
- 449: ds=903 sev=B
- 156: ds=886 sev=B
- 778: ds=856 sev=B
- 279: ds=855 sev=B
- 033: ds=787 sev=B
- 004: ds=775 sev=B
- 688: ds=742 sev=B
- 278: ds=709 sev=B
- 377: ds=689 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=183 sev=red
  - 55: ds=120 sev=red
  - 77: ds=104 sev=blue
  - 33: ds=91 sev=blue
  - 88: ds=86 sev=blue
  - 22: ds=66 sev=purple
  - 66: ds=54 sev=purple
  - 00: ds=27 sev=purple
  - 11: ds=23 sev=-
  - 44: ds=6 sev=-
- non_repeating:
  - 78: ds=55 sev=blue
  - 68: ds=43 sev=blue
  - 29: ds=36 sev=purple
  - 06: ds=29 sev=purple
  - 16: ds=29 sev=purple
  - 59: ds=25 sev=purple
  - 17: ds=23 sev=-
  - 13: ds=21 sev=-
  - 39: ds=21 sev=-
  - 58: ds=19 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:447, 35:390, 1:171, 26:159, 31:121, 4:112, 23:110, 28:104, 27:87, 19:71

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=447 fs=0 fl=0 hz=0.002197802197802198, 35:ds=390 fs=0 fl=0 hz=0.001949317738791423, 1:ds=171 fs=6 fl=4 hz=0.012195121951219513, 26:ds=159 fs=2 fl=0 hz=0.0062402496099844, 31:ds=121 fs=27 fl=0 hz=0.03085714285714286, 4:ds=112 fs=21 fl=2 hz=0.026589595375722544, 23:ds=110 fs=25 fl=1 hz=0.029850746268656716, 28:ds=104 fs=16 fl=2 hz=0.021479713603818614, 27:ds=87 fs=26 fl=0 hz=0.02911534154535274, 19:ds=71 fs=15 fl=1 hz=0.0189520624303233

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=96 flags=red+purple
- S0: ds=69 flags=blue+purple
- S23: ds=58 flags=purple
- S5: ds=57 flags=purple
- S24: ds=55 flags=blue+purple
- S4: ds=47 flags=purple
- S3: ds=46 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=5 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=15), P2:3 (gap=41), P3:6 (gap=19)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:3 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 232: score=37.81806285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.58678571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=35.31129857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 235: score=34.59815714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 297: score=34.08002142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 637: score=33.31811428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 632: score=32.77344285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 236: score=32.093135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 295: score=32.09139285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 635: score=31.329485714285717 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=879 sev=B
- 555: ds=874 sev=B
- 222: ds=851 sev=B
- 337: ds=828 sev=B
- 003: ds=819 sev=B
- 228: ds=810 sev=B
- 556: ds=712 sev=B
- 449: ds=670 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=114 sev=red
  - 55: ds=78 sev=blue
  - 77: ds=47 sev=purple
  - 33: ds=41 sev=purple
  - 88: ds=39 sev=purple
  - 22: ds=37 sev=purple
  - 66: ds=24 sev=-
  - 00: ds=15 sev=-
  - 11: ds=10 sev=-
  - 44: ds=7 sev=-
- non_repeating:
  - 49: ds=55 sev=blue
  - 67: ds=49 sev=blue
  - 34: ds=48 sev=blue
  - 27: ds=42 sev=blue
  - 07: ds=33 sev=purple
  - 05: ds=30 sev=purple
  - 15: ds=28 sev=purple
  - 78: ds=27 sev=purple
  - 69: ds=26 sev=purple
  - 16: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:415, 26:193, 35:179, 27:144, 6:112, 5:81, 1:78, 15:73, 34:59, 31:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=415 fs=1 fl=2 hz=0.006993006993006993, 26:ds=193 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=179 fs=1 fl=1 hz=0.004968944099378882, 27:ds=144 fs=18 fl=3 hz=0.026582278481012658, 6:ds=112 fs=24 fl=2 hz=0.02957906712172924, 5:ds=81 fs=20 fl=1 hz=0.023102310231023104, 1:ds=78 fs=7 fl=3 hz=0.012127894156560088, 15:ds=73 fs=17 fl=3 hz=0.021691973969631236, 34:ds=59 fs=28 fl=1 hz=0.03159041394335512, 31:ds=55 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=82 flags=purple
- S25: ds=79 flags=purple
- S21: ds=59 flags=purple
- S20: ds=55 flags=purple
- S17: ds=53 flags=purple
- S8: ds=51 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 026: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 134: score=3 tags=PAT,RS
  - 269: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 012: score=2 tags=FLT,PAT
  - 017: score=2 tags=RS
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 035: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=3 last_repeat_gap=32 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=18), P2:3 (gap=19), P3:8 (gap=21)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 232: score=37.81806285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 237: score=36.58678571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=35.31129857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 235: score=34.59815714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 297: score=34.08002142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 637: score=33.31811428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 632: score=32.77344285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 236: score=32.093135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 295: score=32.09139285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 635: score=31.329485714285717 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=982 sev=B
- 117: ds=893 sev=B
- 005: ds=879 sev=B
- 577: ds=856 sev=B
- 155: ds=836 sev=B
- 777: ds=835 sev=B
- 669: ds=827 sev=B
- 179: ds=809 sev=B
- 366: ds=775 sev=B
- 222: ds=769 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=99 sev=blue
  - 77: ds=86 sev=blue
  - 66: ds=78 sev=blue
  - 33: ds=74 sev=blue
  - 55: ds=65 sev=purple
  - 88: ds=59 sev=purple
  - 22: ds=36 sev=purple
  - 11: ds=25 sev=purple
  - 00: ds=15 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 58: ds=100 sev=red
  - 35: ds=67 sev=red
  - 29: ds=62 sev=red
  - 47: ds=52 sev=blue
  - 19: ds=34 sev=purple
  - 78: ds=30 sev=purple
  - 68: ds=27 sev=purple
  - 38: ds=21 sev=-
  - 13: ds=19 sev=-
  - 17: ds=19 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:487, 1:274, 32:241, 31:220, 4:140, 28:113, 19:109, 23:104, 26:86, 16:82

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=487 fs=3 fl=1 hz=0.017391304347826087, 1:ds=274 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=241 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=220 fs=16 fl=1 hz=0.021935483870967745, 4:ds=140 fs=21 fl=3 hz=0.028742514970059883, 28:ds=113 fs=10 fl=4 hz=0.017676767676767676, 19:ds=109 fs=12 fl=2 hz=0.016968325791855206, 23:ds=104 fs=24 fl=0 hz=0.02937576499388005, 26:ds=86 fs=0 fl=0 hz=0.002347417840375587, 16:ds=82 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=65 flags=purple
- S15: ds=56 flags=red+purple
- S9: ds=53 flags=purple
- S17: ds=52 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 378: score=4 tags=FLT,MIR,RS
  - 027: score=3 tags=MIR,RS
  - 036: score=3 tags=FLT,RS
  - 045: score=3 tags=MIR,RS
  - 126: score=3 tags=MIR,RS
  - 135: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 279: score=3 tags=MIR,RS
  - 369: score=3 tags=FLT,RS
  - 459: score=3 tags=MIR,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:769(B); midday:851(B)
- 366 -> combined:974(B); evening:775(B)
- 449 -> combined:903(B); midday:670(B)
- 688 -> combined:742(B); evening:734(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 22 -> combined:66(purple); evening:36(purple); midday:37(purple)
- 29 -> combined:36(purple); evening:62(red)
- 33 -> combined:91(blue); evening:74(blue); midday:41(purple)
- 55 -> combined:120(red); evening:65(purple); midday:78(blue)
- 66 -> combined:54(purple); evening:78(blue)
- 68 -> combined:43(blue); evening:27(purple)
- 77 -> combined:104(blue); evening:86(blue); midday:47(purple)
- 78 -> combined:55(blue); evening:30(purple); midday:27(purple)
- 88 -> combined:86(blue); evening:59(purple); midday:39(purple)
- 99 -> combined:183(red); evening:99(blue); midday:114(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(3.1486)[R2,XVAR-Cons(CM)], 6(1.3799285714285714)[R1,Mirror-Echo], 1(1.2277857142857143)[R2,Mirror-Echo], 5(1.197142857142857)[R1,Double-Pressure], 0(1.0478571428571428)[R1,Double-Pressure]
- P2: 3(8.622285714285715)[R1,XVAR-Cons(CEM)], 9(6.115521428571428)[R2,XVAR-Cons(CEM)], 7(1.2225)[R2,Double-Pressure], 1(0.24779285714285712)[R3,Swap], 6(0.2414285714285714)[R3,Swap]
- P3: 7(3.3159)[R2,Mirror-Echo], 2(2.771228571428572)[R1,Mirror-Echo], 5(2.3272714285714287)[R3,XVAR-Cons(CE)], 6(1.32225)[R1,Mirror-Echo], 8(1.297)[R1,Double-Pressure]
