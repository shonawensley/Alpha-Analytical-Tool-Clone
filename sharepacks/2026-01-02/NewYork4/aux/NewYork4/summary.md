# Aux Summary — NewYork4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/NewYork4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: New York
- combined: live=`data/cleaned/draws/New_York_draws.csv` snap=`sharepacks/2026-01-02/NewYork4/aux/draws/New_York_draws.csv` n=1000 head=174, 117, 116, 419, 132
- midday: live=`data/cleaned/draws/New_York_Midday_draws.csv` snap=`sharepacks/2026-01-02/NewYork4/aux/draws/New_York_Midday_draws.csv` n=1000 head=117, 419, 051, 321, 498
- evening: live=`data/cleaned/draws/New_York_Evening_draws.csv` snap=`sharepacks/2026-01-02/NewYork4/aux/draws/New_York_Evening_draws.csv` n=1000 head=174, 116, 132, 195, 353

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=23 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=24), P2:4 (gap=24), P3:0 (gap=10)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 948: score=34.877278571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 908: score=34.32239285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 940: score=33.94213571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 900: score=33.387249999999995 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 248: score=31.691221428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 949: score=31.619674285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 208: score=31.136335714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 909: score=31.06478857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 240: score=30.75607857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 848: score=30.64245785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 244: ds=982 sev=B
- 699: ds=925 sev=B
- 115: ds=843 sev=B
- 222: ds=779 sev=B
- 339: ds=760 sev=B
- 136: ds=751 sev=B
- 000: ds=750 sev=B
- 177: ds=744 sev=B
- 667: ds=712 sev=B
- 777: ds=706 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=53 sev=purple
  - 99: ds=49 sev=purple
  - 77: ds=39 sev=purple
  - 55: ds=38 sev=purple
  - 22: ds=34 sev=purple
  - 66: ds=14 sev=-
  - 44: ds=13 sev=-
  - 00: ds=10 sev=-
  - 33: ds=8 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 67: ds=65 sev=red
  - 06: ds=62 sev=red
  - 69: ds=58 sev=red
  - 36: ds=54 sev=blue
  - 56: ds=40 sev=blue
  - 68: ds=40 sev=blue
  - 07: ds=39 sev=blue
  - 34: ds=35 sev=purple
  - 26: ds=34 sev=purple
  - 27: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:212, 35:200, 26:116, 32:101, 28:70, 5:64, 23:54, 31:49, 10:39, 3:38

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=212 fs=13 fl=3 hz=0.020356234096692113, 35:ds=200 fs=4 fl=3 hz=0.009138381201044387, 26:ds=116 fs=2 fl=1 hz=0.007173601147776184, 32:ds=101 fs=7 fl=3 hz=0.012515644555694618, 28:ds=70 fs=16 fl=3 hz=0.021788990825688075, 5:ds=64 fs=15 fl=3 hz=0.01973684210526316, 23:ds=54 fs=23 fl=2 hz=0.02910360884749709, 31:ds=49 fs=21 fl=1 hz=0.023579849946409433, 10:ds=39 fs=23 fl=1 hz=0.027809965237543453, 3:ds=38 fs=15 fl=2 hz=0.021660649819494587

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=78 flags=purple
- S22: ds=76 flags=purple
- S7: ds=66 flags=purple
- S23: ds=53 flags=purple
- S3: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT
  - 568: score=2 tags=FLT,PAT
  - 569: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=2 last_repeat_gap=16 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=29), P2:4 (gap=25), P3:6 (gap=22)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 948: score=34.877278571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 908: score=34.32239285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 940: score=33.94213571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 900: score=33.387249999999995 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 248: score=31.691221428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 949: score=31.619674285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 208: score=31.136335714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 909: score=31.06478857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 240: score=30.75607857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 848: score=30.64245785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=996 sev=B
- 337: ds=829 sev=B
- 366: ds=822 sev=B
- 044: ds=800 sev=B
- 667: ds=778 sev=B
- 189: ds=764 sev=B
- 449: ds=760 sev=B
- 456: ds=731 sev=B
- 223: ds=724 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=114 sev=red
  - 55: ds=44 sev=purple
  - 33: ds=42 sev=purple
  - 88: ds=26 sev=purple
  - 99: ds=24 sev=-
  - 00: ds=21 sev=-
  - 22: ds=20 sev=-
  - 77: ds=19 sev=-
  - 44: ds=6 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 27: ds=68 sev=red
  - 06: ds=54 sev=blue
  - 25: ds=53 sev=blue
  - 36: ds=38 sev=blue
  - 69: ds=37 sev=blue
  - 09: ds=34 sev=purple
  - 56: ds=32 sev=purple
  - 67: ds=32 sev=purple
  - 16: ds=29 sev=purple
  - 29: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:368, 26:340, 16:263, 18:116, 22:99, 15:88, 23:81, 27:74, 1:70, 28:67

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=368 fs=1 fl=1 hz=0.005145797598627787, 26:ds=340 fs=1 fl=0 hz=0.004081632653061225, 16:ds=263 fs=3 fl=0 hz=0.005471956224350205, 18:ds=116 fs=16 fl=2 hz=0.020524515393386546, 22:ds=99 fs=42 fl=0 hz=0.04713804713804714, 15:ds=88 fs=17 fl=2 hz=0.02134831460674157, 23:ds=81 fs=24 fl=1 hz=0.02860411899313501, 27:ds=74 fs=12 fl=2 hz=0.01728110599078341, 1:ds=70 fs=3 fl=2 hz=0.008075370121130552, 28:ds=67 fs=21 fl=2 hz=0.0257847533632287

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=85 flags=red+purple
- S25: ds=61 flags=blue+purple
- S10: ds=53 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 567: score=2 tags=FLT,PAT
  - 568: score=2 tags=FLT,PAT
  - 569: score=2 tags=FLT,PAT
  - 678: score=2 tags=FLT,PAT
  - 679: score=2 tags=FLT,PAT
  - 689: score=2 tags=FLT,PAT
  - 012: score=1 tags=PAT
  - 013: score=1 tags=PAT
  - 014: score=1 tags=PAT
  - 016: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=31 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=23), P2:8 (gap=37), P3:7 (gap=39)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 948: score=34.877278571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 908: score=34.32239285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 940: score=33.94213571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 900: score=33.387249999999995 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 248: score=31.691221428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 949: score=31.619674285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 208: score=31.136335714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 909: score=31.06478857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 240: score=30.75607857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 848: score=30.64245785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 566: ds=975 sev=B
- 668: ds=855 sev=B
- 248: ds=849 sev=B
- 014: ds=829 sev=B
- 222: ds=813 sev=B
- 001: ds=794 sev=B
- 999: ds=784 sev=B
- 444: ds=783 sev=B
- 156: ds=758 sev=B
- 133: ds=706 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=125 sev=red
  - 44: ds=49 sev=purple
  - 99: ds=39 sev=purple
  - 88: ds=36 sev=purple
  - 55: ds=19 sev=-
  - 22: ds=17 sev=-
  - 66: ds=7 sev=-
  - 00: ds=5 sev=-
  - 33: ds=4 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 48: ds=95 sev=red
  - 07: ds=84 sev=red
  - 03: ds=61 sev=red
  - 39: ds=42 sev=blue
  - 67: ds=38 sev=blue
  - 06: ds=31 sev=purple
  - 46: ds=29 sev=purple
  - 69: ds=29 sev=purple
  - 36: ds=27 sev=purple
  - 38: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:106, 34:105, 35:100, 32:83, 33:76, 10:66, 17:64, 26:58, 4:50, 2:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=106 fs=14 fl=1 hz=0.01884570082449941, 34:ds=105 fs=19 fl=0 hz=0.02242152466367713, 35:ds=100 fs=5 fl=2 hz=0.00963855421686747, 32:ds=83 fs=9 fl=1 hz=0.013095238095238096, 33:ds=76 fs=16 fl=2 hz=0.022113022113022112, 10:ds=66 fs=27 fl=1 hz=0.030335861321776812, 17:ds=64 fs=31 fl=1 hz=0.034408602150537634, 26:ds=58 fs=3 fl=4 hz=0.008879023307436182, 4:ds=50 fs=23 fl=1 hz=0.026200873362445417, 2:ds=45 fs=28 fl=1 hz=0.03456495828367104

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=66 flags=purple
- S3: ds=51 flags=purple
- S16: ds=44 flags=purple
- S25: ds=39 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [7], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=3 tags=FLT,RS
  - 025: score=3 tags=FLT,RS
  - 034: score=3 tags=FLT,RS
  - 079: score=3 tags=FLT,RS
  - 178: score=3 tags=FLT,RS
  - 268: score=3 tags=FLT,RS
  - 358: score=3 tags=FLT,RS
  - 124: score=2 tags=RS
  - 169: score=2 tags=RS
  - 259: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 001 -> evening:794(B); midday:996(B)
- 222 -> combined:779(B); evening:813(B)
- 667 -> combined:712(B); midday:778(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 06 -> combined:62(red); evening:31(purple); midday:54(blue)
- 07 -> combined:39(blue); evening:84(red)
- 27 -> combined:32(purple); midday:68(red)
- 36 -> combined:54(blue); evening:27(purple); midday:38(blue)
- 55 -> combined:38(purple); midday:44(purple)
- 56 -> combined:40(blue); midday:32(purple)
- 67 -> combined:65(red); evening:38(blue); midday:32(purple)
- 69 -> combined:58(red); evening:29(purple); midday:37(blue)
- 77 -> combined:39(purple); evening:125(red)
- 88 -> combined:53(purple); evening:36(purple); midday:26(purple)
- 99 -> combined:49(purple); evening:39(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(3.8749857142857143)[R1,XVAR-Cons(CM)], 2(1.6889285714285713)[R3,XVAR-Cons(CM)], 6(1.4658571428571427)[R1,Double-Pressure], 4(1.3867142857142856)[R1,Double-Pressure], 5(1.0879999999999999)[R2,Double-Pressure]
- P2: 4(7.031942857142858)[R1,XVAR-Cons(CEM)], 0(6.477057142857143)[R2,XVAR-Cons(CEM)], 8(3.357142857142857)[R3,XVAR-Cons(CE)], 3(1.0761999999999998)[R2,Double-Pressure]
- P3: 0(2.5352071428571428)[R1,XVAR-Cons(CM)], 8(2.47035)[R2,Mirror-Echo], 7(1.645)[R1,Double-Pressure], 6(1.2568571428571427)[R1,Double-Pressure], 9(1.1925)[R2,Double-Pressure]
