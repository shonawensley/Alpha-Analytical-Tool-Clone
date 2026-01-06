# Aux Summary — NewYork4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/NewYork4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: New York
- combined: live=`data/cleaned/draws/New_York_draws.csv` snap=`sharepacks/2025-12-31/NewYork4/aux/draws/New_York_draws.csv` n=1000 head=132, 051, 195, 321, 353
- midday: live=`data/cleaned/draws/New_York_Midday_draws.csv` snap=`sharepacks/2025-12-31/NewYork4/aux/draws/New_York_Midday_draws.csv` n=1000 head=051, 321, 498, 893, 464
- evening: live=`data/cleaned/draws/New_York_Evening_draws.csv` snap=`sharepacks/2025-12-31/NewYork4/aux/draws/New_York_Evening_draws.csv` n=1000 head=132, 195, 353, 050, 114

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=19 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=20), P2:4 (gap=20), P3:9 (gap=45)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 949: score=40.95151964285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 909: score=38.291255 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 946: score=37.827329285714285 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 906: score=37.337002142857145 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 979: score=35.740005 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 947: score=35.00792250000001 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 646: score=34.540239285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 606: score=34.11386785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 989: score=34.053354999999996 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 919: score=33.884497857142854 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 244: ds=978 sev=B
- 699: ds=921 sev=B
- 115: ds=839 sev=B
- 222: ds=775 sev=B
- 339: ds=756 sev=B
- 136: ds=747 sev=B
- 000: ds=746 sev=B
- 177: ds=740 sev=B
- 667: ds=708 sev=B
- 777: ds=702 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=49 sev=purple
  - 99: ds=45 sev=purple
  - 77: ds=35 sev=purple
  - 55: ds=34 sev=purple
  - 22: ds=30 sev=purple
  - 66: ds=10 sev=-
  - 44: ds=9 sev=-
  - 11: ds=8 sev=-
  - 00: ds=6 sev=-
  - 33: ds=4 sev=-
- non_repeating:
  - 67: ds=61 sev=red
  - 06: ds=58 sev=red
  - 69: ds=54 sev=blue
  - 36: ds=50 sev=blue
  - 17: ds=38 sev=blue
  - 56: ds=36 sev=purple
  - 68: ds=36 sev=purple
  - 07: ds=35 sev=purple
  - 34: ds=31 sev=purple
  - 26: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:208, 35:196, 26:112, 32:97, 17:75, 22:72, 28:66, 5:60, 23:50, 31:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=208 fs=13 fl=3 hz=0.020356234096692113, 35:ds=196 fs=4 fl=3 hz=0.009138381201044387, 26:ds=112 fs=2 fl=1 hz=0.007173601147776184, 32:ds=97 fs=7 fl=3 hz=0.012515644555694618, 17:ds=75 fs=21 fl=1 hz=0.025669642857142856, 22:ds=72 fs=49 fl=0 hz=0.05378704720087815, 28:ds=66 fs=16 fl=3 hz=0.021788990825688075, 5:ds=60 fs=15 fl=3 hz=0.01973684210526316, 23:ds=50 fs=23 fl=2 hz=0.02910360884749709, 31:ds=45 fs=21 fl=1 hz=0.023579849946409433

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=74 flags=purple
- S22: ds=72 flags=purple
- S9: ds=65 flags=red+purple
- S7: ds=62 flags=purple
- S23: ds=49 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '6', '7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 036: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=14 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=27), P2:1 (gap=27), P3:9 (gap=22)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 949: score=40.95151964285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 909: score=38.291255 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 946: score=37.827329285714285 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 906: score=37.337002142857145 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 979: score=35.740005 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 947: score=35.00792250000001 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 646: score=34.540239285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 606: score=34.11386785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 989: score=34.053354999999996 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 919: score=33.884497857142854 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=994 sev=B
- 337: ds=827 sev=B
- 366: ds=820 sev=B
- 044: ds=798 sev=B
- 667: ds=776 sev=B
- 189: ds=762 sev=B
- 449: ds=758 sev=B
- 456: ds=729 sev=B
- 223: ds=722 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=169 sev=red
  - 66: ds=112 sev=red
  - 55: ds=42 sev=purple
  - 33: ds=40 sev=purple
  - 88: ds=24 sev=-
  - 99: ds=22 sev=-
  - 00: ds=19 sev=-
  - 22: ds=18 sev=-
  - 77: ds=17 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 27: ds=66 sev=red
  - 06: ds=52 sev=blue
  - 25: ds=51 sev=blue
  - 17: ds=37 sev=blue
  - 36: ds=36 sev=purple
  - 69: ds=35 sev=purple
  - 09: ds=32 sev=purple
  - 56: ds=30 sev=purple
  - 67: ds=30 sev=purple
  - 14: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:366, 26:338, 16:261, 18:114, 22:97, 15:86, 23:79, 27:72, 1:68, 28:65

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=366 fs=1 fl=1 hz=0.005145797598627787, 26:ds=338 fs=1 fl=0 hz=0.004081632653061225, 16:ds=261 fs=3 fl=0 hz=0.005471956224350205, 18:ds=114 fs=16 fl=2 hz=0.020524515393386546, 22:ds=97 fs=43 fl=0 hz=0.04772475027746948, 15:ds=86 fs=17 fl=2 hz=0.02134831460674157, 23:ds=79 fs=25 fl=1 hz=0.02826086956521739, 27:ds=72 fs=12 fl=2 hz=0.01728110599078341, 1:ds=68 fs=3 fl=2 hz=0.008075370121130552, 28:ds=65 fs=21 fl=2 hz=0.0257847533632287

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=83 flags=red+purple
- S25: ds=59 flags=blue+purple
- S10: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 027: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 247: score=2 tags=FLT,MIR
  - 257: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 279: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=29 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=21), P2:8 (gap=35), P3:7 (gap=37)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 949: score=40.95151964285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 909: score=38.291255 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 946: score=37.827329285714285 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 906: score=37.337002142857145 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 979: score=35.740005 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 947: score=35.00792250000001 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 646: score=34.540239285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 606: score=34.11386785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 989: score=34.053354999999996 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 919: score=33.884497857142854 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 566: ds=973 sev=B
- 668: ds=853 sev=B
- 248: ds=847 sev=B
- 014: ds=827 sev=B
- 222: ds=811 sev=B
- 001: ds=792 sev=B
- 999: ds=782 sev=B
- 444: ds=781 sev=B
- 156: ds=756 sev=B
- 133: ds=704 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=123 sev=red
  - 44: ds=47 sev=purple
  - 99: ds=37 sev=purple
  - 88: ds=34 sev=purple
  - 55: ds=17 sev=-
  - 22: ds=15 sev=-
  - 66: ds=5 sev=-
  - 11: ds=4 sev=-
  - 00: ds=3 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 47: ds=125 sev=red
  - 48: ds=93 sev=red
  - 07: ds=82 sev=red
  - 03: ds=59 sev=red
  - 39: ds=40 sev=blue
  - 67: ds=36 sev=purple
  - 06: ds=29 sev=purple
  - 46: ds=27 sev=purple
  - 69: ds=27 sev=purple
  - 36: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:104, 34:103, 35:98, 32:81, 33:74, 10:64, 17:62, 26:56, 4:48, 2:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=104 fs=14 fl=1 hz=0.01884570082449941, 34:ds=103 fs=19 fl=0 hz=0.02242152466367713, 35:ds=98 fs=5 fl=2 hz=0.00963855421686747, 32:ds=81 fs=9 fl=1 hz=0.013095238095238096, 33:ds=74 fs=16 fl=2 hz=0.022113022113022112, 10:ds=64 fs=27 fl=1 hz=0.030335861321776812, 17:ds=62 fs=31 fl=1 hz=0.034408602150537634, 26:ds=56 fs=3 fl=4 hz=0.008879023307436182, 4:ds=48 fs=23 fl=1 hz=0.026200873362445417, 2:ds=43 fs=28 fl=1 hz=0.03456495828367104

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=64 flags=purple
- S3: ds=49 flags=purple
- S16: ds=42 flags=purple
- S25: ds=37 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [7], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 016: score=3 tags=FLT,RS
  - 079: score=3 tags=FLT,RS
  - 169: score=3 tags=FLT,RS
  - 178: score=3 tags=FLT,RS
  - 268: score=3 tags=FLT,RS
  - 358: score=3 tags=FLT,RS
  - 367: score=3 tags=FLT,RS
  - 457: score=3 tags=FLT,RS
  - 025: score=2 tags=RS
  - 034: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 001 -> evening:792(B); midday:994(B)
- 222 -> combined:775(B); evening:811(B)
- 667 -> combined:708(B); midday:776(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 06 -> combined:58(red); evening:29(purple); midday:52(blue)
- 07 -> combined:35(purple); evening:82(red)
- 17 -> combined:38(blue); midday:37(blue)
- 27 -> combined:28(purple); midday:66(red)
- 36 -> combined:50(blue); evening:25(purple); midday:36(purple)
- 55 -> combined:34(purple); midday:42(purple)
- 56 -> combined:36(purple); midday:30(purple)
- 67 -> combined:61(red); evening:36(purple); midday:30(purple)
- 69 -> combined:54(blue); evening:27(purple); midday:35(purple)
- 77 -> combined:35(purple); evening:123(red)
- 88 -> combined:49(purple); evening:34(purple)
- 99 -> combined:45(purple); evening:37(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(3.7074714285714285)[R1,XVAR-Cons(CM)], 6(1.4733214285714284)[R1,Mirror-Echo], 4(1.327)[R1,Double-Pressure], 8(1.0044)[R2,Double-Pressure], 5(1.0)[R2,Double-Pressure]
- P2: 4(3.809271428571429)[R1,XVAR-Cons(CM)], 0(3.3829)[R2,XVAR-Cons(CE)], 7(1.8316500000000002)[R3,XVAR-Cons(CE)], 8(1.645)[R1,Double-Pressure], 1(1.4761428571428572)[R1,Double-Pressure]
- P3: 6(7.5504999999999995)[R2,XVAR-Cons(CEM)], 9(7.375878571428571)[R1,XVAR-Cons(CEM)], 7(5.968407142857142)[R3,XVAR-Cons(CEM)]
