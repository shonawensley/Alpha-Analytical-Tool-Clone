# Aux Summary — NewYork4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/NewYork4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: New York
- combined: live=`data/cleaned/draws/New_York_draws.csv` snap=`sharepacks/2026-01-04/NewYork4/aux/draws/New_York_draws.csv` n=1000 head=679, 243, 256, 998, 174
- midday: live=`data/cleaned/draws/New_York_Midday_draws.csv` snap=`sharepacks/2026-01-04/NewYork4/aux/draws/New_York_Midday_draws.csv` n=1000 head=243, 998, 117, 419, 051
- evening: live=`data/cleaned/draws/New_York_Evening_draws.csv` snap=`sharepacks/2026-01-04/NewYork4/aux/draws/New_York_Evening_draws.csv` n=1000 head=679, 256, 174, 116, 132

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=27 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=23), P2:0 (gap=25), P3:0 (gap=14)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=39.827571428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 707: score=37.45250785714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 701: score=36.657985714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 705: score=35.629778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 500: score=35.43956428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 706: score=34.95635 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 708: score=34.469678571428574 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 780: score=33.931557142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 505: score=32.64659857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 501: score=32.269978571428574 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 244: ds=986 sev=B
- 699: ds=929 sev=B
- 115: ds=847 sev=B
- 222: ds=783 sev=B
- 339: ds=764 sev=B
- 136: ds=755 sev=B
- 000: ds=754 sev=B
- 177: ds=748 sev=B
- 667: ds=716 sev=B
- 777: ds=710 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=57 sev=purple
  - 77: ds=43 sev=purple
  - 55: ds=42 sev=purple
  - 22: ds=38 sev=purple
  - 66: ds=18 sev=-
  - 44: ds=17 sev=-
  - 00: ds=14 sev=-
  - 33: ds=12 sev=-
  - 11: ds=5 sev=-
  - 99: ds=3 sev=-
- non_repeating:
  - 06: ds=66 sev=red
  - 36: ds=58 sev=red
  - 68: ds=44 sev=blue
  - 07: ds=43 sev=blue
  - 27: ds=36 sev=purple
  - 18: ds=33 sev=purple
  - 09: ds=28 sev=purple
  - 04: ds=27 sev=purple
  - 02: ds=25 sev=purple
  - 03: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:216, 35:204, 26:120, 32:105, 28:74, 5:68, 23:58, 31:53, 10:43, 3:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=216 fs=12 fl=3 hz=0.0199203187250996, 35:ds=204 fs=4 fl=3 hz=0.009138381201044387, 26:ds=120 fs=2 fl=1 hz=0.007173601147776184, 32:ds=105 fs=7 fl=3 hz=0.012515644555694618, 28:ds=74 fs=16 fl=3 hz=0.021788990825688075, 5:ds=68 fs=15 fl=3 hz=0.01973684210526316, 23:ds=58 fs=23 fl=2 hz=0.02910360884749709, 31:ds=53 fs=21 fl=1 hz=0.023579849946409433, 10:ds=43 fs=23 fl=1 hz=0.027809965237543453, 3:ds=42 fs=15 fl=2 hz=0.021660649819494587

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=82 flags=purple
- S7: ds=70 flags=red+purple
- S23: ds=57 flags=purple
- S3: ds=47 flags=purple
- S10: ds=38 flags=purple
- S17: ds=35 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
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
- current_index=30 streak=1 max=2 last_repeat_gap=18 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=31), P2:3 (gap=20), P3:6 (gap=24)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=39.827571428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 707: score=37.45250785714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 701: score=36.657985714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 705: score=35.629778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 500: score=35.43956428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 706: score=34.95635 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 708: score=34.469678571428574 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 780: score=33.931557142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 505: score=32.64659857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 501: score=32.269978571428574 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=998 sev=B
- 337: ds=831 sev=B
- 366: ds=824 sev=B
- 044: ds=802 sev=B
- 667: ds=780 sev=B
- 189: ds=766 sev=B
- 449: ds=762 sev=B
- 456: ds=733 sev=B
- 223: ds=726 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=116 sev=red
  - 55: ds=46 sev=purple
  - 33: ds=44 sev=purple
  - 88: ds=28 sev=purple
  - 00: ds=23 sev=-
  - 22: ds=22 sev=-
  - 77: ds=21 sev=-
  - 44: ds=8 sev=-
  - 11: ds=2 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 27: ds=70 sev=red
  - 06: ds=56 sev=red
  - 25: ds=55 sev=blue
  - 36: ds=40 sev=blue
  - 69: ds=39 sev=blue
  - 09: ds=36 sev=purple
  - 56: ds=34 sev=purple
  - 67: ds=34 sev=purple
  - 16: ds=31 sev=purple
  - 29: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:370, 26:342, 16:265, 18:118, 22:101, 15:90, 23:83, 27:76, 1:72, 28:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=370 fs=1 fl=1 hz=0.005145797598627787, 26:ds=342 fs=1 fl=0 hz=0.004081632653061225, 16:ds=265 fs=3 fl=0 hz=0.005471956224350205, 18:ds=118 fs=16 fl=2 hz=0.020524515393386546, 22:ds=101 fs=42 fl=0 hz=0.04713804713804714, 15:ds=90 fs=17 fl=2 hz=0.02134831460674157, 23:ds=83 fs=24 fl=1 hz=0.02860411899313501, 27:ds=76 fs=12 fl=2 hz=0.01728110599078341, 1:ds=72 fs=3 fl=2 hz=0.008075370121130552, 28:ds=69 fs=21 fl=2 hz=0.0257847533632287

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S8: ds=87 flags=red+purple
- S25: ds=63 flags=purple
- S10: ds=55 flags=purple
- S7: ds=50 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 046: score=3 tags=FLT,RS
  - 136: score=3 tags=FLT,RS
  - 469: score=3 tags=FLT,RS
  - 568: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 028: score=2 tags=RS
  - 037: score=2 tags=RS
  - 127: score=2 tags=RS
  - 145: score=2 tags=RS
  - 235: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=33 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=25), P2:8 (gap=39), P3:7 (gap=41)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:7 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=39.827571428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 707: score=37.45250785714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 701: score=36.657985714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 705: score=35.629778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 500: score=35.43956428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 706: score=34.95635 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 708: score=34.469678571428574 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 780: score=33.931557142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 505: score=32.64659857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 501: score=32.269978571428574 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 566: ds=977 sev=B
- 668: ds=857 sev=B
- 248: ds=851 sev=B
- 014: ds=831 sev=B
- 222: ds=815 sev=B
- 001: ds=796 sev=B
- 999: ds=786 sev=B
- 444: ds=785 sev=B
- 156: ds=760 sev=B
- 133: ds=708 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=127 sev=red
  - 44: ds=51 sev=purple
  - 99: ds=41 sev=purple
  - 88: ds=38 sev=purple
  - 55: ds=21 sev=-
  - 22: ds=19 sev=-
  - 66: ds=9 sev=-
  - 00: ds=7 sev=-
  - 33: ds=6 sev=-
  - 11: ds=3 sev=-
- non_repeating:
  - 48: ds=97 sev=red
  - 07: ds=86 sev=red
  - 03: ds=63 sev=red
  - 39: ds=44 sev=blue
  - 06: ds=33 sev=purple
  - 46: ds=31 sev=purple
  - 36: ds=29 sev=purple
  - 38: ds=29 sev=purple
  - 08: ds=28 sev=purple
  - 34: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:108, 34:107, 35:102, 32:85, 33:78, 10:68, 17:66, 26:60, 4:52, 2:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=108 fs=14 fl=1 hz=0.01884570082449941, 34:ds=107 fs=19 fl=0 hz=0.02242152466367713, 35:ds=102 fs=5 fl=2 hz=0.00963855421686747, 32:ds=85 fs=9 fl=1 hz=0.013095238095238096, 33:ds=78 fs=16 fl=2 hz=0.022113022113022112, 10:ds=68 fs=27 fl=1 hz=0.030335861321776812, 17:ds=66 fs=31 fl=1 hz=0.034408602150537634, 26:ds=60 fs=3 fl=4 hz=0.008879023307436182, 4:ds=52 fs=23 fl=1 hz=0.026200873362445417, 2:ds=47 fs=28 fl=1 hz=0.03456495828367104

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=68 flags=purple
- S3: ds=53 flags=purple
- S16: ds=46 flags=purple
- S25: ds=41 flags=blue+purple

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
- 001 -> evening:796(B); midday:998(B)
- 222 -> combined:783(B); evening:815(B)
- 667 -> combined:716(B); midday:780(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 02 -> combined:25(purple); evening:25(purple)
- 03 -> combined:25(purple); evening:63(red)
- 06 -> combined:66(red); evening:33(purple); midday:56(red)
- 07 -> combined:43(blue); evening:86(red)
- 09 -> combined:28(purple); midday:36(purple)
- 27 -> combined:36(purple); midday:70(red)
- 36 -> combined:58(red); evening:29(purple); midday:40(blue)
- 55 -> combined:42(purple); midday:46(purple)
- 77 -> combined:43(purple); evening:127(red)
- 88 -> combined:57(purple); evening:38(purple); midday:28(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(5.480764285714287)[R2,XVAR-Cons(CEM)], 5(3.5927571428571428)[R1,XVAR-Cons(CM)], 8(2.730142857142857)[R3,XVAR-Cons(CE)], 6(1.6255714285714284)[R1,Double-Pressure], 4(0.7464285714285714)[R1]
- P2: 0(7.5590142857142855)[R1,XVAR-Cons(CEM)], 8(4.163)[R2,XVAR-Cons(CE)], 3(1.2671428571428571)[R1,Double-Pressure], 6(0.34042857142857147)[R3,Swap], 7(0.23435714285714285)[R3,Swap]
- P3: 0(2.787792857142857)[R1,Mirror-Echo], 7(1.7449999999999999)[R1,Double-Pressure], 1(1.618207142857143)[R3,XVAR-Cons(CE)], 6(1.4165714285714284)[R1,Double-Pressure], 5(1.09)[R2,Mirror-Echo]
