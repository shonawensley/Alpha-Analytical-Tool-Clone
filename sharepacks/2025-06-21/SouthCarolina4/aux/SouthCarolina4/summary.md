# Aux Summary — SouthCarolina4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2025-06-21/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=402, 442, 351, 968, 002
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2025-06-21/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=442, 968, 237, 029, 609
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2025-06-21/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=402, 351, 002, 116, 311

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=2 last_repeat_gap=58 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=19), P2:9 (gap=30), P3:4 (gap=27)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=46.41434607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 593: score=38.708526071428565 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 694: score=38.56359285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 584: score=37.94050571428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 595: score=37.31589392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 574: score=35.32104285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 544: score=33.063942857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 393: score=32.149742857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 591: score=31.842221428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 693: score=31.53679285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=933 sev=B
- 288: ds=901 sev=B
- 466: ds=820 sev=B
- 238: ds=812 sev=B
- 788: ds=723 sev=B
- 388: ds=714 sev=B
- 228: ds=705 sev=B
- 557: ds=704 sev=B
- 137: ds=685 sev=B
- 668: ds=673 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=85 sev=blue
  - 33: ds=48 sev=purple
  - 99: ds=25 sev=purple
  - 55: ds=22 sev=-
  - 22: ds=20 sev=-
  - 77: ds=18 sev=-
  - 88: ds=15 sev=-
  - 11: ds=6 sev=-
  - 00: ds=4 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 28: ds=139 sev=red
  - 56: ds=79 sev=red
  - 18: ds=70 sev=red
  - 47: ds=38 sev=blue
  - 01: ds=36 sev=purple
  - 17: ds=36 sev=purple
  - 14: ds=35 sev=purple
  - 19: ds=35 sev=purple
  - 08: ds=34 sev=purple
  - 45: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 2:185, 1:143, 5:102, 19:92, 34:91, 32:82, 6:81, 4:78, 15:59, 26:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 2:ds=185 fs=9 fl=4 hz=0.016414141414141416, 1:ds=143 fs=5 fl=3 hz=0.011299435028248588, 5:ds=102 fs=21 fl=1 hz=0.028061224489795922, 19:ds=92 fs=13 fl=1 hz=0.016968325791855206, 34:ds=91 fs=26 fl=2 hz=0.031180400890868598, 32:ds=82 fs=2 fl=2 hz=0.005675368898978434, 6:ds=81 fs=21 fl=1 hz=0.02480270574971815, 4:ds=78 fs=27 fl=2 hz=0.03152173913043478, 15:ds=59 fs=13 fl=3 hz=0.01845444059976932, 26:ds=55 fs=2 fl=0 hz=0.007894736842105263

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S27: ds=100 flags=purple
- S26: ds=91 flags=blue+purple
- S25: ds=80 flags=purple
- S3: ds=57 flags=purple
- S13: ds=45 flags=purple
- S20: ds=43 flags=purple
- S17: ds=40 flags=purple
- S4: ds=37 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 067: score=3 tags=FLT,RS
  - 157: score=3 tags=FLT,RS
  - 247: score=3 tags=FLT,RS
  - 679: score=3 tags=FLT,RS
  - 013: score=2 tags=RS
  - 049: score=2 tags=RS
  - 058: score=2 tags=RS
  - 139: score=2 tags=RS
  - 148: score=2 tags=RS
  - 238: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=1 max=3 last_repeat_gap=35 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=46), P2:8 (gap=24), P3:1 (gap=26)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=46)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=46.41434607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 593: score=38.708526071428565 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 694: score=38.56359285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 584: score=37.94050571428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 595: score=37.31589392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 574: score=35.32104285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 544: score=33.063942857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 393: score=32.149742857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 591: score=31.842221428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 693: score=31.53679285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 144: ds=975 sev=B
- 777: ds=974 sev=B
- 224: ds=945 sev=B
- 011: ds=765 sev=B
- 277: ds=711 sev=B
- 555: ds=706 sev=B
- 222: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=60 sev=purple
  - 00: ds=53 sev=purple
  - 88: ds=40 sev=purple
  - 66: ds=39 sev=purple
  - 33: ds=22 sev=-
  - 99: ds=11 sev=-
  - 55: ds=10 sev=-
  - 22: ds=9 sev=-
  - 77: ds=8 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 78: ds=125 sev=red
  - 04: ds=84 sev=red
  - 28: ds=64 sev=red
  - 08: ds=40 sev=blue
  - 56: ds=36 sev=purple
  - 15: ds=34 sev=purple
  - 35: ds=33 sev=purple
  - 18: ds=32 sev=purple
  - 16: ds=28 sev=purple
  - 67: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:293, 32:247, 1:167, 2:85, 5:84, 16:60, 8:59, 4:53, 34:43, 19:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=293 fs=23 fl=0 hz=0.03412462908011869, 32:ds=247 fs=1 fl=2 hz=0.006993006993006993, 1:ds=167 fs=4 fl=3 hz=0.00963855421686747, 2:ds=85 fs=11 fl=1 hz=0.015435501653803748, 5:ds=84 fs=20 fl=0 hz=0.02531645569620253, 16:ds=60 fs=3 fl=1 hz=0.009191176470588236, 8:ds=59 fs=42 fl=1 hz=0.04767184035476718, 4:ds=53 fs=26 fl=2 hz=0.030871003307607496, 34:ds=43 fs=27 fl=1 hz=0.03083700440528634, 19:ds=42 fs=15 fl=3 hz=0.0192102454642476

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S0: ds=96 flags=blue+purple
- S4: ds=91 flags=purple
- S21: ds=42 flags=purple
- S16: ds=40 flags=red+purple

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
- current_index=12 streak=1 max=3 last_repeat_gap=71 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=82), P2:4 (gap=36), P3:4 (gap=32)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=82)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 594: score=46.41434607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 593: score=38.708526071428565 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 694: score=38.56359285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 584: score=37.94050571428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 595: score=37.31589392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 574: score=35.32104285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 544: score=33.063942857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 393: score=32.149742857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 591: score=31.842221428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 693: score=31.53679285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 114: ds=973 sev=B
- 238: ds=890 sev=B
- 558: ds=868 sev=B
- 477: ds=855 sev=B
- 000: ds=852 sev=B
- 556: ds=818 sev=B
- 115: ds=813 sev=B
- 111: ds=800 sev=B
- 999: ds=785 sev=B
- 078: ds=772 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=112 sev=red
  - 66: ds=82 sev=blue
  - 44: ds=58 sev=purple
  - 22: ds=56 sev=purple
  - 55: ds=30 sev=purple
  - 33: ds=29 sev=purple
  - 99: ds=23 sev=-
  - 88: ds=8 sev=-
  - 11: ds=3 sev=-
  - 00: ds=2 sev=-
- non_repeating:
  - 28: ds=89 sev=red
  - 48: ds=68 sev=red
  - 56: ds=48 sev=blue
  - 09: ds=46 sev=blue
  - 18: ds=41 sev=blue
  - 06: ds=38 sev=blue
  - 34: ds=35 sev=purple
  - 46: ds=32 sev=purple
  - 49: ds=32 sev=purple
  - 68: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:290, 19:210, 26:203, 6:145, 10:108, 2:105, 1:77, 15:74, 5:55, 14:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=290 fs=3 fl=1 hz=0.017391304347826087, 19:ds=210 fs=16 fl=2 hz=0.02319587628865979, 26:ds=203 fs=0 fl=0 hz=0.002628120893561104, 6:ds=145 fs=23 fl=2 hz=0.030637254901960783, 10:ds=108 fs=20 fl=0 hz=0.024110218140068886, 2:ds=105 fs=13 fl=3 hz=0.01875732708089097, 1:ds=77 fs=2 fl=0 hz=0.005440696409140369, 15:ds=74 fs=24 fl=1 hz=0.027056277056277056, 5:ds=55 fs=16 fl=3 hz=0.0202991452991453, 14:ds=51 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S3: ds=71 flags=purple
- S22: ds=66 flags=purple
- S26: ds=49 flags=blue+purple
- S7: ds=47 flags=purple
- S14: ds=44 flags=purple
- S25: ds=43 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['7', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 047: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 115 -> combined:671(B); evening:813(B)
- 238 -> combined:812(B); evening:890(B)
- 788 -> combined:723(B); evening:757(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:36(purple); midday:26(purple)
- 08 -> combined:34(purple); midday:40(blue)
- 18 -> combined:70(red); evening:41(blue); midday:32(purple)
- 28 -> combined:139(red); evening:89(red); midday:64(red)
- 33 -> combined:48(purple); evening:29(purple)
- 34 -> combined:27(purple); evening:35(purple)
- 48 -> combined:27(purple); evening:68(red)
- 56 -> combined:79(red); evening:48(blue); midday:36(purple)
- 66 -> combined:85(blue); evening:82(blue); midday:39(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(4.142142857142857)[R1,XVAR-Cons(CM)], 6(1.7149999999999999)[R1,Double-Pressure], 2(1.4015)[R2,Double-Pressure], 8(1.03)[R2,Double-Pressure], 3(0.9834999999999999)[R2,Double-Pressure]
- P2: 9(7.323792857142857)[R1,XVAR-Cons(CEM)], 8(2.9987142857142857)[R3,XVAR-Cons(CM)], 7(2.6541)[R2,XVAR-Cons(CE)], 4(1.8969999999999998)[R1,Mirror-Echo], 1(1.0044)[R2,Double-Pressure]
- P3: 4(8.024799999999999)[R1,XVAR-Cons(CEM)], 3(3.498)[R2,XVAR-Cons(CE)], 5(1.6465)[R3,XVAR-Cons(CM)], 1(1.3762857142857143)[R1,Double-Pressure], 0(0.2418428571428571)[R3]
