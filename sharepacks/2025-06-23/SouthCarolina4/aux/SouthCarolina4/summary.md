# Aux Summary — SouthCarolina4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2025-06-23/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=675, 847, 069, 402, 442
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2025-06-23/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=069, 442, 968, 237, 029
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2025-06-23/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=675, 847, 402, 351, 002

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=61 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=22), P2:9 (gap=33), P3:4 (gap=30)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=51.141435 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 584: score=48.36664285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 583: score=41.36274285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 593: score=40.793000000000006 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 580: score=38.53608571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=38.11398571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 590: score=37.96634285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 534: score=37.71192857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 294: score=37.544242857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 514: score=36.69265714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=936 sev=B
- 288: ds=904 sev=B
- 466: ds=823 sev=B
- 238: ds=815 sev=B
- 788: ds=726 sev=B
- 388: ds=717 sev=B
- 228: ds=708 sev=B
- 557: ds=707 sev=B
- 137: ds=688 sev=B
- 668: ds=676 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=88 sev=blue
  - 33: ds=51 sev=purple
  - 99: ds=28 sev=purple
  - 55: ds=25 sev=purple
  - 22: ds=23 sev=-
  - 77: ds=21 sev=-
  - 88: ds=18 sev=-
  - 11: ds=9 sev=-
  - 00: ds=7 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 28: ds=142 sev=red
  - 18: ds=73 sev=red
  - 01: ds=39 sev=blue
  - 17: ds=39 sev=blue
  - 14: ds=38 sev=blue
  - 19: ds=38 sev=blue
  - 08: ds=37 sev=blue
  - 45: ds=35 sev=purple
  - 39: ds=33 sev=purple
  - 34: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 2:188, 1:146, 5:105, 19:95, 34:94, 32:85, 6:84, 4:81, 15:62, 26:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 2:ds=188 fs=9 fl=4 hz=0.016414141414141416, 1:ds=146 fs=5 fl=3 hz=0.011299435028248588, 5:ds=105 fs=21 fl=1 hz=0.028061224489795922, 19:ds=95 fs=13 fl=1 hz=0.016968325791855206, 34:ds=94 fs=26 fl=2 hz=0.031180400890868598, 32:ds=85 fs=2 fl=2 hz=0.005675368898978434, 6:ds=84 fs=21 fl=1 hz=0.02480270574971815, 4:ds=81 fs=26 fl=2 hz=0.03153153153153153, 15:ds=62 fs=13 fl=3 hz=0.01845444059976932, 26:ds=58 fs=2 fl=0 hz=0.007894736842105263

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S27: ds=100 flags=purple
- S26: ds=94 flags=blue+purple
- S25: ds=83 flags=purple
- S3: ds=60 flags=purple
- S13: ds=48 flags=purple
- S20: ds=46 flags=purple
- S17: ds=43 flags=purple
- S4: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 013: score=3 tags=FLT,RS
  - 139: score=3 tags=FLT,RS
  - 148: score=3 tags=FLT,RS
  - 157: score=3 tags=FLT,RS
  - 238: score=3 tags=FLT,RS
  - 346: score=3 tags=FLT,RS
  - 049: score=2 tags=RS
  - 058: score=2 tags=RS
  - 067: score=2 tags=RS
  - 247: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=36 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=47), P2:8 (gap=25), P3:1 (gap=27)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=47)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=51.141435 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 584: score=48.36664285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 583: score=41.36274285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 593: score=40.793000000000006 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 580: score=38.53608571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=38.11398571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 590: score=37.96634285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 534: score=37.71192857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 294: score=37.544242857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 514: score=36.69265714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

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
- current_index=7 streak=1 max=3 last_repeat_gap=73 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=38), P2:9 (gap=18), P3:4 (gap=34)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=51.141435 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 584: score=48.36664285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 583: score=41.36274285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 593: score=40.793000000000006 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 580: score=38.53608571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 284: score=38.11398571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 590: score=37.96634285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 534: score=37.71192857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 294: score=37.544242857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 514: score=36.69265714285714 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 114: ds=975 sev=B
- 238: ds=892 sev=B
- 558: ds=870 sev=B
- 477: ds=857 sev=B
- 000: ds=854 sev=B
- 556: ds=820 sev=B
- 115: ds=815 sev=B
- 111: ds=802 sev=B
- 999: ds=787 sev=B
- 078: ds=774 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=114 sev=red
  - 66: ds=84 sev=blue
  - 44: ds=60 sev=purple
  - 22: ds=58 sev=purple
  - 55: ds=32 sev=purple
  - 33: ds=31 sev=purple
  - 99: ds=25 sev=purple
  - 88: ds=10 sev=-
  - 11: ds=5 sev=-
  - 00: ds=4 sev=-
- non_repeating:
  - 28: ds=91 sev=red
  - 09: ds=48 sev=blue
  - 18: ds=43 sev=blue
  - 06: ds=40 sev=blue
  - 34: ds=37 sev=blue
  - 46: ds=34 sev=purple
  - 49: ds=34 sev=purple
  - 68: ds=29 sev=purple
  - 23: ds=28 sev=purple
  - 27: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:292, 19:212, 26:205, 6:147, 10:110, 2:107, 1:79, 15:76, 5:57, 14:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=292 fs=3 fl=1 hz=0.017391304347826087, 19:ds=212 fs=16 fl=2 hz=0.02319587628865979, 26:ds=205 fs=0 fl=0 hz=0.002628120893561104, 6:ds=147 fs=23 fl=2 hz=0.030637254901960783, 10:ds=110 fs=20 fl=0 hz=0.024110218140068886, 2:ds=107 fs=13 fl=3 hz=0.01875732708089097, 1:ds=79 fs=2 fl=0 hz=0.005440696409140369, 15:ds=76 fs=23 fl=1 hz=0.028103044496487116, 5:ds=57 fs=16 fl=3 hz=0.0202991452991453, 14:ds=53 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S3: ds=73 flags=purple
- S22: ds=68 flags=purple
- S26: ds=51 flags=blue+purple
- S7: ds=49 flags=purple
- S14: ds=46 flags=purple
- S25: ds=45 flags=blue+purple

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
- 115 -> combined:674(B); evening:815(B)
- 238 -> combined:815(B); evening:892(B)
- 788 -> combined:726(B); evening:759(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:39(blue); midday:27(purple)
- 08 -> combined:37(blue); midday:41(blue)
- 18 -> combined:73(red); evening:43(blue); midday:33(purple)
- 19 -> combined:38(blue); evening:26(purple)
- 28 -> combined:142(red); evening:91(red); midday:65(red)
- 33 -> combined:51(purple); evening:31(purple)
- 34 -> combined:30(purple); evening:37(blue)
- 55 -> combined:25(purple); evening:32(purple)
- 66 -> combined:88(blue); evening:84(blue); midday:40(purple)
- 99 -> combined:28(purple); evening:25(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(6.997657142857142)[R1,XVAR-Cons(CEM)], 2(1.7449999999999999)[R1,Double-Pressure], 1(1.7153857142857145)[R3,XVAR-Cons(CM)], 9(1.1806999999999999)[R2,Double-Pressure], 3(1.0344)[R2,Double-Pressure]
- P2: 9(7.159542857142858)[R1,XVAR-Cons(CEM)], 8(6.729285714285715)[R2,XVAR-Cons(CEM)], 3(1.0745714285714285)[R2,Mirror-Echo], 1(1.0553)[R2,Double-Pressure], 2(0.2414285714285714)[R3,Swap]
- P3: 4(8.1397)[R1,XVAR-Cons(CEM)], 3(3.6357999999999997)[R2,XVAR-Cons(CE)], 0(1.8091428571428572)[R3,XVAR-Cons(CE)], 1(1.4061428571428571)[R1,Double-Pressure], 5(0.14779285714285711)[R3]
