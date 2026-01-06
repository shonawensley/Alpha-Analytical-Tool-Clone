# Aux Summary — NorthCarolina4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-03/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=383, 033, 053, 416, 057
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-03/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=033, 416, 867, 455, 766
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-03/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=383, 053, 057, 879, 168

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=32 streak=1 max=3 last_repeat_gap=29 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=30), P2:4 (gap=35), P3:2 (gap=32)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=54.32340392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=49.36922142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 242: score=48.09970571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 240: score=43.25622857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=42.197207142857145 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 545: score=42.18525857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 500: score=40.87216428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 202: score=39.602648571428574 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 522: score=39.24064285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 592: score=38.44889285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=878 sev=B
- 446: ds=874 sev=B
- 445: ds=814 sev=B
- 122: ds=797 sev=B
- 036: ds=793 sev=B
- 555: ds=770 sev=B
- 299: ds=767 sev=B
- 277: ds=759 sev=B
- 112: ds=748 sev=B
- 034: ds=682 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=154 sev=red
  - 77: ds=127 sev=red
  - 99: ds=50 sev=purple
  - 44: ds=48 sev=purple
  - 22: ds=14 sev=-
  - 88: ds=11 sev=-
  - 11: ds=10 sev=-
  - 66: ds=9 sev=-
  - 55: ds=7 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 56: ds=56 sev=red
  - 27: ds=52 sev=blue
  - 02: ds=46 sev=blue
  - 23: ds=42 sev=blue
  - 09: ds=41 sev=blue
  - 28: ds=38 sev=blue
  - 04: ds=35 sev=purple
  - 06: ds=35 sev=purple
  - 34: ds=33 sev=purple
  - 29: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:482, 1:109, 27:105, 31:96, 15:80, 16:78, 10:68, 23:57, 35:48, 12:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=482 fs=3 fl=0 hz=0.009389671361502348, 1:ds=109 fs=0 fl=3 hz=0.00625, 27:ds=105 fs=15 fl=2 hz=0.02463768115942029, 31:ds=96 fs=19 fl=3 hz=0.02502844141069397, 15:ds=80 fs=16 fl=2 hz=0.019758507135016465, 16:ds=78 fs=4 fl=1 hz=0.008836524300441826, 10:ds=68 fs=21 fl=2 hz=0.027315914489311165, 23:ds=57 fs=17 fl=3 hz=0.024330900243309, 35:ds=48 fs=1 fl=1 hz=0.0053533190578158455, 12:ds=46 fs=47 fl=1 hz=0.050367261280167885

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=90 flags=purple
- S23: ds=74 flags=blue+purple
- S4: ds=49 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR
  - 169: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 238: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=13 streak=1 max=2 last_repeat_gap=97 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=36), P2:9 (gap=26), P3:2 (gap=39)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=54.32340392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=49.36922142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 242: score=48.09970571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 240: score=43.25622857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=42.197207142857145 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 545: score=42.18525857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 500: score=40.87216428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 202: score=39.602648571428574 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 522: score=39.24064285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 592: score=38.44889285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=974 sev=B
- 123: ds=949 sev=B
- 446: ds=926 sev=B
- 777: ds=886 sev=B
- 119: ds=851 sev=B
- 222: ds=821 sev=B
- 155: ds=783 sev=B
- 488: ds=777 sev=B
- 177: ds=753 sev=B
- 007: ds=732 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=156 sev=red
  - 00: ds=131 sev=red
  - 77: ds=63 sev=purple
  - 99: ds=51 sev=purple
  - 22: ds=39 sev=purple
  - 11: ds=9 sev=-
  - 88: ds=5 sev=-
  - 66: ds=4 sev=-
  - 55: ds=3 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 48: ds=147 sev=red
  - 25: ds=60 sev=red
  - 07: ds=55 sev=blue
  - 28: ds=47 sev=blue
  - 23: ds=42 sev=blue
  - 26: ds=42 sev=blue
  - 02: ds=39 sev=blue
  - 29: ds=36 sev=purple
  - 56: ds=30 sev=purple
  - 27: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:379, 25:187, 32:167, 35:141, 4:131, 11:106, 31:99, 2:95, 33:78, 12:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=379 fs=1 fl=0 hz=0.005905511811023622, 25:ds=187 fs=15 fl=1 hz=0.02165087956698241, 32:ds=167 fs=3 fl=1 hz=0.007416563658838071, 35:ds=141 fs=0 fl=2 hz=0.005201560468140442, 4:ds=131 fs=11 fl=3 hz=0.0166073546856465, 11:ds=106 fs=50 fl=0 hz=0.056882821387940846, 31:ds=99 fs=25 fl=0 hz=0.02793296089385475, 2:ds=95 fs=13 fl=3 hz=0.018223234624145785, 33:ds=78 fs=21 fl=2 hz=0.025136612021857924, 12:ds=56 fs=48 fl=0 hz=0.05090137857900318

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=90 flags=purple
- S20: ds=78 flags=red+purple
- S2: ds=69 flags=purple
- S5: ds=65 flags=purple
- S8: ds=60 flags=purple

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
- current_index=32 streak=1 max=3 last_repeat_gap=21 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=15), P2:4 (gap=36), P3:5 (gap=21)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=54.32340392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 540: score=49.36922142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 242: score=48.09970571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 240: score=43.25622857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=42.197207142857145 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 545: score=42.18525857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 500: score=40.87216428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 202: score=39.602648571428574 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 522: score=39.24064285714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 592: score=38.44889285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=975 sev=B
- 299: ds=932 sev=B
- 223: ds=862 sev=B
- 122: ds=851 sev=B
- 116: ds=828 sev=B
- 039: ds=811 sev=B
- 377: ds=799 sev=B
- 277: ds=785 sev=B
- 188: ds=773 sev=B
- 557: ds=772 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=180 sev=red
  - 55: ds=123 sev=red
  - 77: ds=81 sev=blue
  - 00: ds=77 sev=blue
  - 66: ds=39 sev=purple
  - 99: ds=25 sev=purple
  - 44: ds=24 sev=-
  - 22: ds=7 sev=-
  - 11: ds=5 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 45: ds=100 sev=red
  - 34: ds=41 sev=blue
  - 59: ds=40 sev=blue
  - 04: ds=36 sev=purple
  - 06: ds=30 sev=purple
  - 08: ds=29 sev=purple
  - 58: ds=29 sev=purple
  - 56: ds=28 sev=purple
  - 17: ds=26 sev=purple
  - 27: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:259, 26:241, 13:206, 1:148, 23:117, 5:98, 17:97, 27:54, 31:48, 14:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=259 fs=18 fl=0 hz=0.024896265560165977, 26:ds=241 fs=1 fl=2 hz=0.006666666666666667, 13:ds=206 fs=20 fl=0 hz=0.025284450063211127, 1:ds=148 fs=2 fl=3 hz=0.007434944237918215, 23:ds=117 fs=14 fl=3 hz=0.019384264538198404, 5:ds=98 fs=15 fl=2 hz=0.020809248554913295, 17:ds=97 fs=29 fl=0 hz=0.03553921568627451, 27:ds=54 fs=22 fl=3 hz=0.027085590465872156, 31:ds=48 fs=21 fl=2 hz=0.024338624338624337, 14:ds=46 fs=41 fl=1 hz=0.0445859872611465

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=91 flags=purple
- S0: ds=77 flags=blue+purple
- S4: ds=66 flags=blue+purple
- S22: ds=46 flags=purple
- S2: ds=45 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=4 triggers={'mirror': True, 'root_due': [7], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 025: score=4 tags=FLT,MIR,RS
  - 034: score=4 tags=FLT,PAT,RS
  - 124: score=4 tags=FLT,PAT,RS
  - 349: score=4 tags=FLT,MIR,RS
  - 016: score=3 tags=MIR,RS
  - 169: score=3 tags=MIR,RS
  - 259: score=3 tags=FLT,RS
  - 268: score=3 tags=FLT,RS
  - 358: score=3 tags=MIR,RS
  - 457: score=3 tags=FLT,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:793(B); evening:725(B)
- 122 -> combined:797(B); evening:851(B)
- 155 -> combined:878(B); midday:783(B)
- 277 -> combined:759(B); evening:785(B)
- 299 -> combined:767(B); evening:932(B)
- 446 -> combined:874(B); midday:926(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:154(red); evening:77(blue); midday:131(red)
- 02 -> combined:46(blue); midday:39(blue)
- 04 -> combined:35(purple); evening:36(purple)
- 06 -> combined:35(purple); evening:30(purple)
- 08 -> combined:25(purple); evening:29(purple)
- 23 -> combined:42(blue); midday:42(blue)
- 25 -> combined:30(purple); midday:60(red)
- 27 -> combined:52(blue); evening:26(purple); midday:27(purple)
- 28 -> combined:38(blue); midday:47(blue)
- 29 -> combined:32(purple); midday:36(purple)
- 34 -> combined:33(purple); evening:41(blue)
- 44 -> combined:48(purple); midday:156(red)
- 56 -> combined:56(red); evening:28(purple); midday:30(purple)
- 77 -> combined:127(red); evening:81(blue); midday:63(purple)
- 99 -> combined:50(purple); evening:25(purple); midday:51(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(6.955992857142856)[R1,XVAR-Cons(CEM)], 2(3.343)[R3,XVAR-Cons(CM)], 3(1.2225)[R2,Double-Pressure], 7(0.9208)[R2,Double-Pressure], 6(0.37399999999999994)[R2]
- P2: 4(8.853157142857143)[R1,XVAR-Cons(CEM)], 0(3.8560999999999996)[R2,XVAR-Cons(CE)], 2(1.8995357142857143)[R3,XVAR-Cons(CM)], 9(1.6077857142857144)[R1,Mirror-Echo], 3(0.2612285714285714)[R3,Swap]
- P3: 2(8.385114285714286)[R1,XVAR-Cons(CEM)], 0(6.060071428571429)[R2,XVAR-Cons(CEM)], 5(1.376392857142857)[R1,Mirror-Echo], 8(1.1298)[R2,Double-Pressure], 4(0.3262857142857143)[R3,Swap]
