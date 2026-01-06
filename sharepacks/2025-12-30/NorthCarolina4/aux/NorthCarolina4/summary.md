# Aux Summary — NorthCarolina4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2025-12-30/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=168, 766, 911, 885, 391
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2025-12-30/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=766, 885, 789, 157, 673
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2025-12-30/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=168, 911, 391, 226, 964

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=21 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=38), P2:4 (gap=27), P3:2 (gap=24)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.278864285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.463437142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 043: score=44.362207142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.156057142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 542: score=43.917078571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.23499714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.34063 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.06455 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.04365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.45495 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 338: ds=882 sev=B
- 155: ds=870 sev=B
- 446: ds=866 sev=B
- 445: ds=806 sev=B
- 122: ds=789 sev=B
- 036: ds=785 sev=B
- 555: ds=762 sev=B
- 299: ds=759 sev=B
- 277: ds=751 sev=B
- 112: ds=740 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=146 sev=red
  - 77: ds=119 sev=red
  - 55: ds=101 sev=blue
  - 33: ds=43 sev=purple
  - 99: ds=42 sev=purple
  - 44: ds=40 sev=purple
  - 22: ds=6 sev=-
  - 88: ds=3 sev=-
  - 11: ds=2 sev=-
  - 66: ds=1 sev=-
- non_repeating:
  - 45: ds=109 sev=red
  - 56: ds=48 sev=blue
  - 27: ds=44 sev=blue
  - 02: ds=38 sev=blue
  - 23: ds=34 sev=purple
  - 09: ds=33 sev=purple
  - 03: ds=32 sev=purple
  - 28: ds=30 sev=purple
  - 04: ds=27 sev=purple
  - 06: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:474, 32:327, 1:101, 27:97, 31:88, 15:72, 16:70, 10:60, 4:50, 23:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=474 fs=3 fl=0 hz=0.009389671361502348, 32:ds=327 fs=1 fl=1 hz=0.005405405405405406, 1:ds=101 fs=0 fl=3 hz=0.00625, 27:ds=97 fs=15 fl=2 hz=0.02011173184357542, 31:ds=88 fs=19 fl=3 hz=0.02502844141069397, 15:ds=72 fs=16 fl=2 hz=0.019758507135016465, 16:ds=70 fs=4 fl=1 hz=0.008836524300441826, 10:ds=60 fs=21 fl=2 hz=0.027315914489311165, 4:ds=50 fs=18 fl=2 hz=0.0213903743315508, 23:ds=49 fs=17 fl=3 hz=0.024330900243309

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=82 flags=purple
- S23: ds=66 flags=blue+purple
- S4: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '4'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 059: score=4 tags=FLT,MIR,RS
  - 149: score=4 tags=FLT,MIR,RS
  - 257: score=4 tags=FLT,MIR,RS
  - 014: score=3 tags=FLT,RS
  - 023: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 167: score=3 tags=MIR,RS
  - 239: score=3 tags=FLT,RS
  - 248: score=3 tags=FLT,RS
  - 347: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=2 last_repeat_gap=93 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=32), P2:9 (gap=22), P3:2 (gap=35)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.278864285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.463437142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 043: score=44.362207142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.156057142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 542: score=43.917078571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.23499714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.34063 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.06455 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.04365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.45495 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=970 sev=B
- 123: ds=945 sev=B
- 446: ds=922 sev=B
- 777: ds=882 sev=B
- 119: ds=847 sev=B
- 222: ds=817 sev=B
- 155: ds=779 sev=B
- 488: ds=773 sev=B
- 177: ds=749 sev=B
- 007: ds=728 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=152 sev=red
  - 00: ds=127 sev=red
  - 77: ds=59 sev=purple
  - 55: ds=50 sev=purple
  - 99: ds=47 sev=purple
  - 22: ds=35 sev=purple
  - 33: ds=21 sev=-
  - 11: ds=5 sev=-
  - 88: ds=1 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 48: ds=143 sev=red
  - 68: ds=71 sev=red
  - 25: ds=56 sev=red
  - 45: ds=54 sev=blue
  - 07: ds=51 sev=blue
  - 28: ds=43 sev=blue
  - 23: ds=38 sev=blue
  - 26: ds=38 sev=blue
  - 02: ds=35 sev=purple
  - 29: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:375, 25:183, 32:163, 35:137, 4:127, 11:102, 31:95, 2:91, 33:74, 12:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=375 fs=1 fl=0 hz=0.005905511811023622, 25:ds=183 fs=15 fl=1 hz=0.02165087956698241, 32:ds=163 fs=3 fl=1 hz=0.007416563658838071, 35:ds=137 fs=0 fl=2 hz=0.005201560468140442, 4:ds=127 fs=12 fl=3 hz=0.017241379310344827, 11:ds=102 fs=50 fl=0 hz=0.056882821387940846, 31:ds=95 fs=25 fl=0 hz=0.02793296089385475, 2:ds=91 fs=13 fl=3 hz=0.018223234624145785, 33:ds=74 fs=21 fl=2 hz=0.025136612021857924, 12:ds=52 fs=48 fl=0 hz=0.05090137857900318

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=86 flags=purple
- S20: ds=74 flags=red+purple
- S2: ds=65 flags=purple
- S5: ds=61 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '4'], 'pairs': {'remaining_count': 1}}
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

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=17 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=25), P2:4 (gap=32), P3:3 (gap=24)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.278864285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.463437142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 043: score=44.362207142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.156057142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 542: score=43.917078571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.23499714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.34063 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.06455 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.04365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.45495 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=971 sev=B
- 299: ds=928 sev=B
- 223: ds=858 sev=B
- 122: ds=847 sev=B
- 116: ds=824 sev=B
- 039: ds=807 sev=B
- 377: ds=795 sev=B
- 277: ds=781 sev=B
- 188: ds=769 sev=B
- 557: ds=768 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=176 sev=red
  - 55: ds=119 sev=red
  - 33: ds=118 sev=red
  - 77: ds=77 sev=blue
  - 00: ds=73 sev=blue
  - 66: ds=35 sev=purple
  - 99: ds=21 sev=-
  - 44: ds=20 sev=-
  - 22: ds=3 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 45: ds=96 sev=red
  - 79: ds=44 sev=blue
  - 34: ds=37 sev=blue
  - 59: ds=36 sev=purple
  - 04: ds=32 sev=purple
  - 06: ds=26 sev=purple
  - 08: ds=25 sev=purple
  - 58: ds=25 sev=purple
  - 56: ds=24 sev=-
  - 17: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:255, 26:237, 13:202, 32:176, 1:144, 23:113, 5:94, 17:93, 27:50, 31:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=255 fs=18 fl=0 hz=0.024896265560165977, 26:ds=237 fs=1 fl=2 hz=0.006666666666666667, 13:ds=202 fs=20 fl=0 hz=0.025284450063211127, 32:ds=176 fs=2 fl=2 hz=0.007416563658838071, 1:ds=144 fs=2 fl=3 hz=0.007434944237918215, 23:ds=113 fs=14 fl=3 hz=0.019384264538198404, 5:ds=94 fs=15 fl=2 hz=0.020809248554913295, 17:ds=93 fs=29 fl=0 hz=0.03553921568627451, 27:ds=50 fs=22 fl=3 hz=0.027085590465872156, 31:ds=44 fs=22 fl=2 hz=0.025210084033613446

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=87 flags=purple
- S0: ds=73 flags=blue+purple
- S4: ds=62 flags=blue+purple
- S22: ds=42 flags=purple
- S2: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=4 triggers={'mirror': True, 'root_due': [7], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=4 tags=FLT,MIR,RS
  - 025: score=4 tags=FLT,MIR,RS
  - 034: score=4 tags=FLT,PAT,RS
  - 358: score=4 tags=FLT,MIR,RS
  - 079: score=3 tags=FLT,RS
  - 124: score=3 tags=PAT,RS
  - 169: score=3 tags=MIR,RS
  - 178: score=3 tags=FLT,RS
  - 259: score=3 tags=FLT,RS
  - 349: score=3 tags=MIR,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:785(B); evening:721(B)
- 122 -> combined:789(B); evening:847(B)
- 155 -> combined:870(B); midday:779(B)
- 277 -> combined:751(B); evening:781(B)
- 299 -> combined:759(B); evening:928(B)
- 338 -> combined:882(B); midday:708(B)
- 446 -> combined:866(B); midday:922(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:146(red); evening:73(blue); midday:127(red)
- 02 -> combined:38(blue); midday:35(purple)
- 04 -> combined:27(purple); evening:32(purple)
- 06 -> combined:27(purple); evening:26(purple)
- 23 -> combined:34(purple); midday:38(blue)
- 28 -> combined:30(purple); midday:43(blue)
- 33 -> combined:43(purple); evening:118(red)
- 34 -> combined:25(purple); evening:37(blue)
- 44 -> combined:40(purple); midday:152(red)
- 45 -> combined:109(red); evening:96(red); midday:54(blue)
- 55 -> combined:101(blue); evening:119(red); midday:50(purple)
- 56 -> combined:48(blue); midday:26(purple)
- 77 -> combined:119(red); evening:77(blue); midday:59(purple)
- 99 -> combined:42(purple); midday:47(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(8.24407857142857)[R1,Mirror-Echo], 5(3.382292857142857)[R2,Mirror-Echo], 2(1.5554285714285714)[R1,Double-Pressure], 8(1.4164285714285714)[R1,Double-Pressure], 3(0.38215)[R3,Swap]
- P2: 4(8.274271428571428)[R1,XVAR-Cons(CEM)], 0(3.651464285714286)[R2,XVAR-Cons(CE)], 9(1.4503571428571427)[R1,Mirror-Echo], 5(0.45842142857142854)[R3,Mirror-Echo], 3(0.3262857142857143)[R3,Swap]
- P3: 2(7.260514285714287)[R1,XVAR-Cons(CEM)], 3(2.843857142857143)[R3,XVAR-Cons(CE)], 0(2.6706642857142855)[R2,XVAR-Cons(CM)], 8(1.0461999999999998)[R2,Double-Pressure], 5(1.0252999999999999)[R2,Double-Pressure]
