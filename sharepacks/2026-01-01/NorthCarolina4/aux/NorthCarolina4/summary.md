# Aux Summary — NorthCarolina4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-01/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=057, 867, 879, 455, 168
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-01/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=867, 455, 766, 885, 789
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-01/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=057, 879, 168, 911, 391

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=3 last_repeat_gap=25 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=26), P2:4 (gap=31), P3:2 (gap=28)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 242: score=46.269215714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=43.78702857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 202: score=37.96687285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 543: score=36.93407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 540: score=36.659464285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 243: score=36.245357142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 240: score=35.97075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=35.48468571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=35.15778714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=34.269644285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 338: ds=886 sev=B
- 155: ds=874 sev=B
- 446: ds=870 sev=B
- 445: ds=810 sev=B
- 122: ds=793 sev=B
- 036: ds=789 sev=B
- 555: ds=766 sev=B
- 299: ds=763 sev=B
- 277: ds=755 sev=B
- 112: ds=744 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=150 sev=red
  - 77: ds=123 sev=red
  - 33: ds=47 sev=purple
  - 99: ds=46 sev=purple
  - 44: ds=44 sev=purple
  - 22: ds=10 sev=-
  - 88: ds=7 sev=-
  - 11: ds=6 sev=-
  - 66: ds=5 sev=-
  - 55: ds=3 sev=-
- non_repeating:
  - 56: ds=52 sev=blue
  - 27: ds=48 sev=blue
  - 02: ds=42 sev=blue
  - 23: ds=38 sev=blue
  - 09: ds=37 sev=blue
  - 03: ds=36 sev=purple
  - 28: ds=34 sev=purple
  - 04: ds=31 sev=purple
  - 06: ds=31 sev=purple
  - 34: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:478, 32:331, 1:105, 27:101, 31:92, 15:76, 16:74, 10:64, 4:54, 23:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=478 fs=3 fl=0 hz=0.009389671361502348, 32:ds=331 fs=1 fl=1 hz=0.005405405405405406, 1:ds=105 fs=0 fl=3 hz=0.00625, 27:ds=101 fs=15 fl=2 hz=0.02011173184357542, 31:ds=92 fs=19 fl=3 hz=0.02502844141069397, 15:ds=76 fs=16 fl=2 hz=0.019758507135016465, 16:ds=74 fs=4 fl=1 hz=0.008836524300441826, 10:ds=64 fs=21 fl=2 hz=0.027315914489311165, 4:ds=54 fs=18 fl=2 hz=0.0213903743315508, 23:ds=53 fs=17 fl=3 hz=0.024330900243309

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=86 flags=purple
- S23: ds=70 flags=blue+purple
- S4: ds=45 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '3'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 034: score=2 tags=FLT,PAT
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 123: score=2 tags=FLT,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=95 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=34), P2:9 (gap=24), P3:2 (gap=37)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 242: score=46.269215714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=43.78702857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 202: score=37.96687285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 543: score=36.93407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 540: score=36.659464285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 243: score=36.245357142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 240: score=35.97075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=35.48468571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=35.15778714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=34.269644285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=972 sev=B
- 123: ds=947 sev=B
- 446: ds=924 sev=B
- 777: ds=884 sev=B
- 119: ds=849 sev=B
- 222: ds=819 sev=B
- 155: ds=781 sev=B
- 488: ds=775 sev=B
- 177: ds=751 sev=B
- 007: ds=730 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=154 sev=red
  - 00: ds=129 sev=red
  - 77: ds=61 sev=purple
  - 99: ds=49 sev=purple
  - 22: ds=37 sev=purple
  - 33: ds=23 sev=-
  - 11: ds=7 sev=-
  - 88: ds=3 sev=-
  - 66: ds=2 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 48: ds=145 sev=red
  - 25: ds=58 sev=red
  - 07: ds=53 sev=blue
  - 28: ds=45 sev=blue
  - 23: ds=40 sev=blue
  - 26: ds=40 sev=blue
  - 02: ds=37 sev=blue
  - 29: ds=34 sev=purple
  - 56: ds=28 sev=purple
  - 27: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:377, 25:185, 32:165, 35:139, 4:129, 11:104, 31:97, 2:93, 33:76, 12:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=377 fs=1 fl=0 hz=0.005905511811023622, 25:ds=185 fs=15 fl=1 hz=0.02165087956698241, 32:ds=165 fs=3 fl=1 hz=0.007416563658838071, 35:ds=139 fs=0 fl=2 hz=0.005201560468140442, 4:ds=129 fs=12 fl=3 hz=0.017241379310344827, 11:ds=104 fs=50 fl=0 hz=0.056882821387940846, 31:ds=97 fs=25 fl=0 hz=0.02793296089385475, 2:ds=93 fs=13 fl=3 hz=0.018223234624145785, 33:ds=76 fs=21 fl=2 hz=0.025136612021857924, 12:ds=54 fs=48 fl=0 hz=0.05090137857900318

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=88 flags=purple
- S20: ds=76 flags=red+purple
- S2: ds=67 flags=purple
- S5: ds=63 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1', '2', '3'], 'pairs': {'remaining_count': 1}}
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
- current_index=3 streak=1 max=3 last_repeat_gap=19 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=13), P2:4 (gap=34), P3:3 (gap=26)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 242: score=46.269215714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=43.78702857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 202: score=37.96687285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 543: score=36.93407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 540: score=36.659464285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 243: score=36.245357142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 240: score=35.97075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=35.48468571428572 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=35.15778714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 292: score=34.269644285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=973 sev=B
- 299: ds=930 sev=B
- 223: ds=860 sev=B
- 122: ds=849 sev=B
- 116: ds=826 sev=B
- 039: ds=809 sev=B
- 377: ds=797 sev=B
- 277: ds=783 sev=B
- 188: ds=771 sev=B
- 557: ds=770 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=178 sev=red
  - 55: ds=121 sev=red
  - 33: ds=120 sev=red
  - 77: ds=79 sev=blue
  - 00: ds=75 sev=blue
  - 66: ds=37 sev=purple
  - 99: ds=23 sev=-
  - 44: ds=22 sev=-
  - 22: ds=5 sev=-
  - 11: ds=3 sev=-
- non_repeating:
  - 45: ds=98 sev=red
  - 34: ds=39 sev=blue
  - 59: ds=38 sev=blue
  - 04: ds=34 sev=purple
  - 06: ds=28 sev=purple
  - 08: ds=27 sev=purple
  - 58: ds=27 sev=purple
  - 56: ds=26 sev=purple
  - 17: ds=24 sev=-
  - 27: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:257, 26:239, 13:204, 32:178, 1:146, 23:115, 5:96, 17:95, 27:52, 31:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=257 fs=18 fl=0 hz=0.024896265560165977, 26:ds=239 fs=1 fl=2 hz=0.006666666666666667, 13:ds=204 fs=20 fl=0 hz=0.025284450063211127, 32:ds=178 fs=2 fl=2 hz=0.007416563658838071, 1:ds=146 fs=2 fl=3 hz=0.007434944237918215, 23:ds=115 fs=14 fl=3 hz=0.019384264538198404, 5:ds=96 fs=15 fl=2 hz=0.020809248554913295, 17:ds=95 fs=29 fl=0 hz=0.03553921568627451, 27:ds=52 fs=22 fl=3 hz=0.027085590465872156, 31:ds=46 fs=22 fl=2 hz=0.025210084033613446

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=89 flags=purple
- S0: ds=75 flags=blue+purple
- S4: ds=64 flags=blue+purple
- S22: ds=44 flags=purple
- S2: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=4 triggers={'mirror': True, 'root_due': [7], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}
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
- 036 -> combined:789(B); evening:723(B)
- 122 -> combined:793(B); evening:849(B)
- 155 -> combined:874(B); midday:781(B)
- 277 -> combined:755(B); evening:783(B)
- 299 -> combined:763(B); evening:930(B)
- 338 -> combined:886(B); midday:710(B)
- 446 -> combined:870(B); midday:924(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:150(red); evening:75(blue); midday:129(red)
- 02 -> combined:42(blue); midday:37(blue)
- 04 -> combined:31(purple); evening:34(purple)
- 06 -> combined:31(purple); evening:28(purple)
- 23 -> combined:38(blue); midday:40(blue)
- 25 -> combined:26(purple); midday:58(red)
- 27 -> combined:48(blue); midday:25(purple)
- 28 -> combined:34(purple); midday:45(blue)
- 29 -> combined:28(purple); midday:34(purple)
- 33 -> combined:47(purple); evening:120(red)
- 34 -> combined:29(purple); evening:39(blue)
- 44 -> combined:44(purple); midday:154(red)
- 56 -> combined:52(blue); evening:26(purple); midday:28(purple)
- 77 -> combined:123(red); evening:79(blue); midday:61(purple)
- 99 -> combined:46(purple); midday:49(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(3.845285714285714)[R1,XVAR-Cons(CE)], 2(3.1565714285714286)[R3,XVAR-Cons(CM)], 0(1.2016)[R2,Double-Pressure], 7(0.879)[R2,Double-Pressure], 3(0.40902142857142854)[R3,Swap]
- P2: 4(8.528642857142858)[R1,XVAR-Cons(CEM)], 0(3.7263)[R2,XVAR-Cons(CE)], 3(1.9172142857142858)[R3,XVAR-Cons(CE)], 9(1.5290714285714284)[R1,Mirror-Echo], 2(0.2746642857142857)[R3,Swap]
- P3: 2(7.413099999999999)[R1,XVAR-Cons(CEM)], 3(3.060142857142857)[R3,XVAR-Cons(CE)], 0(2.785535714285714)[R2,XVAR-Cons(CM)], 8(1.0879999999999999)[R2,Double-Pressure], 5(1.0671)[R2,Double-Pressure]
