# Aux Summary — NorthCarolina4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-04/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=178, 374, 383, 033, 053
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-04/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=374, 033, 416, 867, 455
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-04/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=178, 383, 053, 057, 879

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=31 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=32), P2:4 (gap=37), P3:2 (gap=34)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=55.40861785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=53.73560714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 242: score=48.249832857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=46.231495 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 500: score=44.558484285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 240: score=43.373428571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=43.348549999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 522: score=40.221557142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 541: score=39.86458714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 202: score=39.813204285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=880 sev=B
- 446: ds=876 sev=B
- 445: ds=816 sev=B
- 122: ds=799 sev=B
- 036: ds=795 sev=B
- 555: ds=772 sev=B
- 299: ds=769 sev=B
- 277: ds=761 sev=B
- 112: ds=750 sev=B
- 034: ds=684 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=156 sev=red
  - 77: ds=129 sev=red
  - 99: ds=52 sev=purple
  - 44: ds=50 sev=purple
  - 22: ds=16 sev=-
  - 88: ds=13 sev=-
  - 11: ds=12 sev=-
  - 66: ds=11 sev=-
  - 55: ds=9 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 56: ds=58 sev=red
  - 27: ds=54 sev=blue
  - 02: ds=48 sev=blue
  - 23: ds=44 sev=blue
  - 09: ds=43 sev=blue
  - 28: ds=40 sev=blue
  - 04: ds=37 sev=blue
  - 06: ds=37 sev=blue
  - 29: ds=34 sev=purple
  - 24: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:484, 1:111, 27:107, 31:98, 15:82, 16:80, 10:70, 23:59, 35:50, 12:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=484 fs=3 fl=0 hz=0.009389671361502348, 1:ds=111 fs=0 fl=3 hz=0.00625, 27:ds=107 fs=15 fl=2 hz=0.02463768115942029, 31:ds=98 fs=19 fl=3 hz=0.02502844141069397, 15:ds=82 fs=16 fl=2 hz=0.019758507135016465, 16:ds=80 fs=4 fl=1 hz=0.008836524300441826, 10:ds=70 fs=21 fl=2 hz=0.027315914489311165, 23:ds=59 fs=17 fl=3 hz=0.024330900243309, 35:ds=50 fs=1 fl=1 hz=0.0053533190578158455, 12:ds=48 fs=46 fl=1 hz=0.049893842887473464

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=92 flags=purple
- S23: ds=76 flags=blue+purple
- S4: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '6', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=2 last_repeat_gap=98 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=37), P2:9 (gap=27), P3:2 (gap=40)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:2 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=55.40861785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=53.73560714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 242: score=48.249832857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=46.231495 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 500: score=44.558484285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 240: score=43.373428571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=43.348549999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 522: score=40.221557142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 541: score=39.86458714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 202: score=39.813204285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=975 sev=B
- 123: ds=950 sev=B
- 446: ds=927 sev=B
- 777: ds=887 sev=B
- 119: ds=852 sev=B
- 222: ds=822 sev=B
- 155: ds=784 sev=B
- 488: ds=778 sev=B
- 177: ds=754 sev=B
- 007: ds=733 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=157 sev=red
  - 00: ds=132 sev=red
  - 77: ds=64 sev=purple
  - 99: ds=52 sev=purple
  - 22: ds=40 sev=purple
  - 11: ds=10 sev=-
  - 88: ds=6 sev=-
  - 66: ds=5 sev=-
  - 55: ds=4 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 48: ds=148 sev=red
  - 25: ds=61 sev=red
  - 07: ds=56 sev=red
  - 28: ds=48 sev=blue
  - 23: ds=43 sev=blue
  - 26: ds=43 sev=blue
  - 02: ds=40 sev=blue
  - 29: ds=37 sev=blue
  - 56: ds=31 sev=purple
  - 27: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:380, 25:188, 32:168, 35:142, 4:132, 11:107, 31:100, 2:96, 33:79, 12:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=380 fs=1 fl=0 hz=0.005905511811023622, 25:ds=188 fs=15 fl=1 hz=0.02165087956698241, 32:ds=168 fs=3 fl=1 hz=0.007416563658838071, 35:ds=142 fs=0 fl=2 hz=0.005201560468140442, 4:ds=132 fs=11 fl=3 hz=0.0166073546856465, 11:ds=107 fs=50 fl=0 hz=0.056882821387940846, 31:ds=100 fs=25 fl=0 hz=0.02793296089385475, 2:ds=96 fs=13 fl=3 hz=0.018223234624145785, 33:ds=79 fs=21 fl=2 hz=0.025136612021857924, 12:ds=57 fs=47 fl=0 hz=0.05181918412348401

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=91 flags=purple
- S20: ds=79 flags=red+purple
- S2: ds=70 flags=purple
- S5: ds=66 flags=purple
- S8: ds=61 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=22 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=16), P2:4 (gap=37), P3:5 (gap=22)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=55.40861785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=53.73560714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 242: score=48.249832857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=46.231495 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 500: score=44.558484285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 240: score=43.373428571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=43.348549999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 522: score=40.221557142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 541: score=39.86458714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 202: score=39.813204285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=976 sev=B
- 299: ds=933 sev=B
- 223: ds=863 sev=B
- 122: ds=852 sev=B
- 116: ds=829 sev=B
- 039: ds=812 sev=B
- 377: ds=800 sev=B
- 277: ds=786 sev=B
- 188: ds=774 sev=B
- 557: ds=773 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=181 sev=red
  - 55: ds=124 sev=red
  - 77: ds=82 sev=blue
  - 00: ds=78 sev=blue
  - 66: ds=40 sev=purple
  - 99: ds=26 sev=purple
  - 44: ds=25 sev=purple
  - 22: ds=8 sev=-
  - 11: ds=6 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 45: ds=101 sev=red
  - 34: ds=42 sev=blue
  - 59: ds=41 sev=blue
  - 04: ds=37 sev=blue
  - 06: ds=31 sev=purple
  - 08: ds=30 sev=purple
  - 58: ds=30 sev=purple
  - 56: ds=29 sev=purple
  - 27: ds=27 sev=purple
  - 02: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:260, 26:242, 13:207, 1:149, 23:118, 5:99, 17:98, 27:55, 31:49, 14:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=260 fs=18 fl=0 hz=0.024896265560165977, 26:ds=242 fs=1 fl=2 hz=0.006666666666666667, 13:ds=207 fs=20 fl=0 hz=0.025284450063211127, 1:ds=149 fs=2 fl=3 hz=0.007434944237918215, 23:ds=118 fs=14 fl=3 hz=0.019384264538198404, 5:ds=99 fs=15 fl=2 hz=0.020809248554913295, 17:ds=98 fs=29 fl=0 hz=0.03553921568627451, 27:ds=55 fs=22 fl=3 hz=0.027085590465872156, 31:ds=49 fs=21 fl=2 hz=0.024338624338624337, 14:ds=47 fs=41 fl=1 hz=0.0445859872611465

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=92 flags=purple
- S0: ds=78 flags=blue+purple
- S4: ds=67 flags=blue+purple
- S22: ds=47 flags=purple
- S2: ds=46 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '4', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 123: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 134: score=2 tags=FLT,PAT
  - 234: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:795(B); evening:726(B)
- 122 -> combined:799(B); evening:852(B)
- 155 -> combined:880(B); midday:784(B)
- 277 -> combined:761(B); evening:786(B)
- 299 -> combined:769(B); evening:933(B)
- 446 -> combined:876(B); midday:927(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:156(red); evening:78(blue); midday:132(red)
- 02 -> combined:48(blue); midday:40(blue)
- 04 -> combined:37(blue); evening:37(blue)
- 06 -> combined:37(blue); evening:31(purple)
- 08 -> combined:27(purple); evening:30(purple)
- 23 -> combined:44(blue); midday:43(blue)
- 25 -> combined:32(purple); midday:61(red)
- 27 -> combined:54(blue); evening:27(purple); midday:28(purple)
- 28 -> combined:40(blue); midday:48(blue)
- 29 -> combined:34(purple); midday:37(blue)
- 44 -> combined:50(purple); evening:25(purple); midday:157(red)
- 56 -> combined:58(red); evening:29(purple); midday:31(purple)
- 59 -> combined:25(purple); evening:41(blue)
- 77 -> combined:129(red); evening:82(blue); midday:64(purple)
- 99 -> combined:52(purple); evening:26(purple); midday:52(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(7.811428571428571)[R1,XVAR-Cons(CEM)], 2(3.3712857142857144)[R3,XVAR-Cons(CM)], 7(0.9417)[R2,Double-Pressure], 6(0.4179999999999999)[R2], 4(0.2612285714285714)[R3,Swap]
- P2: 4(8.857628571428572)[R1,XVAR-Cons(CEM)], 0(3.921)[R2,XVAR-Cons(CE)], 2(1.9412571428571428)[R3,XVAR-Cons(CM)], 9(1.647142857142857)[R1,Mirror-Echo], 3(0.24466428571428572)[R3,Swap]
- P3: 2(8.468871428571429)[R1,XVAR-Cons(CEM)], 0(6.144514285714286)[R2,XVAR-Cons(CEM)], 5(1.4123571428571429)[R1,Mirror-Echo], 8(0.5507)[R2,Swap], 1(0.16971428571428573)[R3]
