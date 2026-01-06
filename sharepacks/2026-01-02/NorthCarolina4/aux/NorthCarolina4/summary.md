# Aux Summary — NorthCarolina4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=053, 416, 057, 867, 879
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=416, 867, 455, 766, 885
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2026-01-02/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=053, 057, 879, 168, 911

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=4 streak=1 max=3 last_repeat_gap=27 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=28), P2:4 (gap=33), P3:2 (gap=30)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=48.02946357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 242: score=47.59672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 540: score=43.66945714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 240: score=42.94617142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 040: score=40.613395714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 202: score=39.13209285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=36.43055714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=36.29982857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=35.617785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 292: score=35.40932142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 338: ds=888 sev=B
- 155: ds=876 sev=B
- 446: ds=872 sev=B
- 445: ds=812 sev=B
- 122: ds=795 sev=B
- 036: ds=791 sev=B
- 555: ds=768 sev=B
- 299: ds=765 sev=B
- 277: ds=757 sev=B
- 112: ds=746 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=152 sev=red
  - 77: ds=125 sev=red
  - 33: ds=49 sev=purple
  - 99: ds=48 sev=purple
  - 44: ds=46 sev=purple
  - 22: ds=12 sev=-
  - 88: ds=9 sev=-
  - 11: ds=8 sev=-
  - 66: ds=7 sev=-
  - 55: ds=5 sev=-
- non_repeating:
  - 56: ds=54 sev=blue
  - 27: ds=50 sev=blue
  - 02: ds=44 sev=blue
  - 23: ds=40 sev=blue
  - 09: ds=39 sev=blue
  - 28: ds=36 sev=purple
  - 04: ds=33 sev=purple
  - 06: ds=33 sev=purple
  - 34: ds=31 sev=purple
  - 29: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:480, 32:333, 1:107, 27:103, 31:94, 15:78, 16:76, 10:66, 23:55, 35:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=480 fs=3 fl=0 hz=0.009389671361502348, 32:ds=333 fs=1 fl=1 hz=0.005405405405405406, 1:ds=107 fs=0 fl=3 hz=0.00625, 27:ds=103 fs=15 fl=2 hz=0.02011173184357542, 31:ds=94 fs=19 fl=3 hz=0.02502844141069397, 15:ds=78 fs=16 fl=2 hz=0.019758507135016465, 16:ds=76 fs=4 fl=1 hz=0.008836524300441826, 10:ds=66 fs=21 fl=2 hz=0.027315914489311165, 23:ds=55 fs=17 fl=3 hz=0.024330900243309, 35:ds=46 fs=1 fl=1 hz=0.0053533190578158455

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=88 flags=purple
- S23: ds=72 flags=blue+purple
- S4: ds=47 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 123: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 234: score=2 tags=FLT,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=19 streak=1 max=2 last_repeat_gap=96 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=35), P2:9 (gap=25), P3:2 (gap=38)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=48.02946357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 242: score=47.59672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 540: score=43.66945714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 240: score=42.94617142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 040: score=40.613395714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 202: score=39.13209285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=36.43055714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=36.29982857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=35.617785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 292: score=35.40932142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=973 sev=B
- 123: ds=948 sev=B
- 446: ds=925 sev=B
- 777: ds=885 sev=B
- 119: ds=850 sev=B
- 222: ds=820 sev=B
- 155: ds=782 sev=B
- 488: ds=776 sev=B
- 177: ds=752 sev=B
- 007: ds=731 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=155 sev=red
  - 00: ds=130 sev=red
  - 77: ds=62 sev=purple
  - 99: ds=50 sev=purple
  - 22: ds=38 sev=purple
  - 33: ds=24 sev=-
  - 11: ds=8 sev=-
  - 88: ds=4 sev=-
  - 66: ds=3 sev=-
  - 55: ds=2 sev=-
- non_repeating:
  - 48: ds=146 sev=red
  - 25: ds=59 sev=red
  - 07: ds=54 sev=blue
  - 28: ds=46 sev=blue
  - 23: ds=41 sev=blue
  - 26: ds=41 sev=blue
  - 02: ds=38 sev=blue
  - 29: ds=35 sev=purple
  - 56: ds=29 sev=purple
  - 27: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:378, 25:186, 32:166, 35:140, 4:130, 11:105, 31:98, 2:94, 33:77, 12:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=378 fs=1 fl=0 hz=0.005905511811023622, 25:ds=186 fs=15 fl=1 hz=0.02165087956698241, 32:ds=166 fs=3 fl=1 hz=0.007416563658838071, 35:ds=140 fs=0 fl=2 hz=0.005201560468140442, 4:ds=130 fs=11 fl=3 hz=0.0166073546856465, 11:ds=105 fs=50 fl=0 hz=0.056882821387940846, 31:ds=98 fs=25 fl=0 hz=0.02793296089385475, 2:ds=94 fs=13 fl=3 hz=0.018223234624145785, 33:ds=77 fs=21 fl=2 hz=0.025136612021857924, 12:ds=55 fs=48 fl=0 hz=0.05090137857900318

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=89 flags=purple
- S20: ds=77 flags=red+purple
- S2: ds=68 flags=purple
- S5: ds=64 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '3', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=4 streak=1 max=3 last_repeat_gap=20 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=14), P2:4 (gap=35), P3:5 (gap=20)
- consensus_notes: P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 542: score=48.02946357142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 242: score=47.59672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 540: score=43.66945714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 240: score=42.94617142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 040: score=40.613395714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 202: score=39.13209285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 502: score=36.43055714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 232: score=36.29982857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=35.617785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 292: score=35.40932142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=974 sev=B
- 299: ds=931 sev=B
- 223: ds=861 sev=B
- 122: ds=850 sev=B
- 116: ds=827 sev=B
- 039: ds=810 sev=B
- 377: ds=798 sev=B
- 277: ds=784 sev=B
- 188: ds=772 sev=B
- 557: ds=771 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=179 sev=red
  - 55: ds=122 sev=red
  - 33: ds=121 sev=red
  - 77: ds=80 sev=blue
  - 00: ds=76 sev=blue
  - 66: ds=38 sev=purple
  - 99: ds=24 sev=-
  - 44: ds=23 sev=-
  - 22: ds=6 sev=-
  - 11: ds=4 sev=-
- non_repeating:
  - 45: ds=99 sev=red
  - 34: ds=40 sev=blue
  - 59: ds=39 sev=blue
  - 04: ds=35 sev=purple
  - 06: ds=29 sev=purple
  - 08: ds=28 sev=purple
  - 58: ds=28 sev=purple
  - 56: ds=27 sev=purple
  - 17: ds=25 sev=purple
  - 27: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:258, 26:240, 13:205, 32:179, 1:147, 23:116, 5:97, 17:96, 27:53, 31:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=258 fs=18 fl=0 hz=0.024896265560165977, 26:ds=240 fs=1 fl=2 hz=0.006666666666666667, 13:ds=205 fs=20 fl=0 hz=0.025284450063211127, 32:ds=179 fs=2 fl=2 hz=0.007416563658838071, 1:ds=147 fs=2 fl=3 hz=0.007434944237918215, 23:ds=116 fs=14 fl=3 hz=0.019384264538198404, 5:ds=97 fs=15 fl=2 hz=0.020809248554913295, 17:ds=96 fs=29 fl=0 hz=0.03553921568627451, 27:ds=53 fs=22 fl=3 hz=0.027085590465872156, 31:ds=47 fs=22 fl=2 hz=0.025210084033613446

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=90 flags=purple
- S0: ds=76 flags=blue+purple
- S4: ds=65 flags=blue+purple
- S22: ds=45 flags=purple
- S2: ds=44 flags=purple

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
- 036 -> combined:791(B); evening:724(B)
- 122 -> combined:795(B); evening:850(B)
- 155 -> combined:876(B); midday:782(B)
- 277 -> combined:757(B); evening:784(B)
- 299 -> combined:765(B); evening:931(B)
- 338 -> combined:888(B); midday:711(B)
- 446 -> combined:872(B); midday:925(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:152(red); evening:76(blue); midday:130(red)
- 02 -> combined:44(blue); midday:38(blue)
- 04 -> combined:33(purple); evening:35(purple)
- 06 -> combined:33(purple); evening:29(purple)
- 23 -> combined:40(blue); midday:41(blue)
- 25 -> combined:28(purple); midday:59(red)
- 27 -> combined:50(blue); evening:25(purple); midday:26(purple)
- 28 -> combined:36(purple); midday:46(blue)
- 29 -> combined:30(purple); midday:35(purple)
- 33 -> combined:49(purple); evening:121(red)
- 34 -> combined:31(purple); evening:40(blue)
- 44 -> combined:46(purple); midday:155(red)
- 56 -> combined:54(blue); evening:27(purple); midday:29(purple)
- 77 -> combined:125(red); evening:80(blue); midday:62(purple)
- 99 -> combined:48(purple); midday:50(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(3.938)[R1,XVAR-Cons(CE)], 2(3.214714285714286)[R3,XVAR-Cons(CM)], 0(1.2225)[R2,Double-Pressure], 7(0.8998999999999999)[R2,Double-Pressure], 3(0.42245714285714286)[R3,Swap]
- P2: 4(8.755828571428571)[R1,XVAR-Cons(CEM)], 0(3.7912)[R2,XVAR-Cons(CE)], 3(1.9589357142857144)[R3,XVAR-Cons(CE)], 9(1.5684285714285715)[R1,Mirror-Echo], 2(0.2881)[R3,Swap]
- P3: 2(8.201357142857143)[R1,XVAR-Cons(CEM)], 0(5.9756285714285715)[R2,XVAR-Cons(CEM)], 5(1.3404285714285713)[R1,Mirror-Echo], 8(0.5089)[R2,Swap], 4(0.29800000000000004)[R3,Swap]
