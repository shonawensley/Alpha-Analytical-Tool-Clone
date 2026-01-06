# Aux Summary — NorthCarolina4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2025-12-31/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=879, 455, 168, 766, 911
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2025-12-31/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=455, 766, 885, 789, 157
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2025-12-31/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=879, 168, 911, 391, 226

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=23 last_repeat_index=19

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=40), P2:4 (gap=29), P3:2 (gap=26)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.57010714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.83938285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=44.758492857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 043: score=44.6353 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.59112142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.30017785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.86039714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.300399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.2795 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.78836428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 338: ds=884 sev=B
- 155: ds=872 sev=B
- 446: ds=868 sev=B
- 445: ds=808 sev=B
- 122: ds=791 sev=B
- 036: ds=787 sev=B
- 555: ds=764 sev=B
- 299: ds=761 sev=B
- 277: ds=753 sev=B
- 112: ds=742 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=148 sev=red
  - 77: ds=121 sev=red
  - 33: ds=45 sev=purple
  - 99: ds=44 sev=purple
  - 44: ds=42 sev=purple
  - 22: ds=8 sev=-
  - 88: ds=5 sev=-
  - 11: ds=4 sev=-
  - 66: ds=3 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 56: ds=50 sev=blue
  - 27: ds=46 sev=blue
  - 02: ds=40 sev=blue
  - 23: ds=36 sev=purple
  - 09: ds=35 sev=purple
  - 03: ds=34 sev=purple
  - 28: ds=32 sev=purple
  - 04: ds=29 sev=purple
  - 06: ds=29 sev=purple
  - 34: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:476, 32:329, 1:103, 27:99, 31:90, 15:74, 16:72, 10:62, 4:52, 23:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=476 fs=3 fl=0 hz=0.009389671361502348, 32:ds=329 fs=1 fl=1 hz=0.005405405405405406, 1:ds=103 fs=0 fl=3 hz=0.00625, 27:ds=99 fs=15 fl=2 hz=0.02011173184357542, 31:ds=90 fs=19 fl=3 hz=0.02502844141069397, 15:ds=74 fs=16 fl=2 hz=0.019758507135016465, 16:ds=72 fs=4 fl=1 hz=0.008836524300441826, 10:ds=62 fs=21 fl=2 hz=0.027315914489311165, 4:ds=52 fs=18 fl=2 hz=0.0213903743315508, 23:ds=51 fs=17 fl=3 hz=0.024330900243309

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=84 flags=purple
- S23: ds=68 flags=blue+purple
- S4: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '2', '3'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 123: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 134: score=2 tags=FLT,PAT
  - 234: score=2 tags=FLT,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=2 last_repeat_gap=94 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=33), P2:9 (gap=23), P3:2 (gap=36)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.57010714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.83938285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=44.758492857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 043: score=44.6353 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.59112142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.30017785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.86039714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.300399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.2795 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.78836428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=971 sev=B
- 123: ds=946 sev=B
- 446: ds=923 sev=B
- 777: ds=883 sev=B
- 119: ds=848 sev=B
- 222: ds=818 sev=B
- 155: ds=780 sev=B
- 488: ds=774 sev=B
- 177: ds=750 sev=B
- 007: ds=729 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=153 sev=red
  - 00: ds=128 sev=red
  - 77: ds=60 sev=purple
  - 99: ds=48 sev=purple
  - 22: ds=36 sev=purple
  - 33: ds=22 sev=-
  - 11: ds=6 sev=-
  - 88: ds=2 sev=-
  - 66: ds=1 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 48: ds=144 sev=red
  - 68: ds=72 sev=red
  - 25: ds=57 sev=red
  - 07: ds=52 sev=blue
  - 28: ds=44 sev=blue
  - 23: ds=39 sev=blue
  - 26: ds=39 sev=blue
  - 02: ds=36 sev=purple
  - 29: ds=33 sev=purple
  - 56: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:376, 25:184, 32:164, 35:138, 4:128, 11:103, 31:96, 2:92, 33:75, 12:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=376 fs=1 fl=0 hz=0.005905511811023622, 25:ds=184 fs=15 fl=1 hz=0.02165087956698241, 32:ds=164 fs=3 fl=1 hz=0.007416563658838071, 35:ds=138 fs=0 fl=2 hz=0.005201560468140442, 4:ds=128 fs=12 fl=3 hz=0.017241379310344827, 11:ds=103 fs=50 fl=0 hz=0.056882821387940846, 31:ds=96 fs=25 fl=0 hz=0.02793296089385475, 2:ds=92 fs=13 fl=3 hz=0.018223234624145785, 33:ds=75 fs=21 fl=2 hz=0.025136612021857924, 12:ds=53 fs=48 fl=0 hz=0.05090137857900318

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=87 flags=purple
- S20: ds=75 flags=red+purple
- S2: ds=66 flags=purple
- S5: ds=62 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '3'], 'pairs': {'remaining_count': 1}}
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
- current_index=30 streak=1 max=3 last_repeat_gap=18 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=20), P2:4 (gap=33), P3:3 (gap=25)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 042: score=51.57010714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 040: score=47.83938285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 542: score=44.758492857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 043: score=44.6353 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 002: score=44.59112142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 242: score=41.30017785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=40.86039714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 048: score=40.300399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 045: score=40.2795 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 092: score=39.78836428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=972 sev=B
- 299: ds=929 sev=B
- 223: ds=859 sev=B
- 122: ds=848 sev=B
- 116: ds=825 sev=B
- 039: ds=808 sev=B
- 377: ds=796 sev=B
- 277: ds=782 sev=B
- 188: ds=770 sev=B
- 557: ds=769 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=177 sev=red
  - 55: ds=120 sev=red
  - 33: ds=119 sev=red
  - 77: ds=78 sev=blue
  - 00: ds=74 sev=blue
  - 66: ds=36 sev=purple
  - 99: ds=22 sev=-
  - 44: ds=21 sev=-
  - 22: ds=4 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 45: ds=97 sev=red
  - 34: ds=38 sev=blue
  - 59: ds=37 sev=blue
  - 04: ds=33 sev=purple
  - 06: ds=27 sev=purple
  - 08: ds=26 sev=purple
  - 58: ds=26 sev=purple
  - 56: ds=25 sev=purple
  - 17: ds=23 sev=-
  - 27: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 34:256, 26:238, 13:203, 32:177, 1:145, 23:114, 5:95, 17:94, 27:51, 31:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 34:ds=256 fs=18 fl=0 hz=0.024896265560165977, 26:ds=238 fs=1 fl=2 hz=0.006666666666666667, 13:ds=203 fs=20 fl=0 hz=0.025284450063211127, 32:ds=177 fs=2 fl=2 hz=0.007416563658838071, 1:ds=145 fs=2 fl=3 hz=0.007434944237918215, 23:ds=114 fs=14 fl=3 hz=0.019384264538198404, 5:ds=95 fs=15 fl=2 hz=0.020809248554913295, 17:ds=94 fs=29 fl=0 hz=0.03553921568627451, 27:ds=51 fs=22 fl=3 hz=0.027085590465872156, 31:ds=45 fs=22 fl=2 hz=0.025210084033613446

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=88 flags=purple
- S0: ds=74 flags=blue+purple
- S4: ds=63 flags=blue+purple
- S22: ds=43 flags=purple
- S2: ds=42 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': False, 'root_due': [7], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 034: score=4 tags=FLT,PAT,RS
  - 124: score=4 tags=FLT,PAT,RS
  - 016: score=3 tags=FLT,RS
  - 025: score=3 tags=FLT,RS
  - 079: score=3 tags=FLT,RS
  - 259: score=3 tags=FLT,RS
  - 349: score=3 tags=FLT,RS
  - 358: score=3 tags=FLT,RS
  - 457: score=3 tags=FLT,RS
  - 012: score=2 tags=FLT,PAT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 036 -> combined:787(B); evening:722(B)
- 122 -> combined:791(B); evening:848(B)
- 155 -> combined:872(B); midday:780(B)
- 277 -> combined:753(B); evening:782(B)
- 299 -> combined:761(B); evening:929(B)
- 338 -> combined:884(B); midday:709(B)
- 446 -> combined:868(B); midday:923(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:148(red); evening:74(blue); midday:128(red)
- 02 -> combined:40(blue); midday:36(purple)
- 04 -> combined:29(purple); evening:33(purple)
- 06 -> combined:29(purple); evening:27(purple)
- 23 -> combined:36(purple); midday:39(blue)
- 28 -> combined:32(purple); midday:44(blue)
- 29 -> combined:26(purple); midday:33(purple)
- 33 -> combined:45(purple); evening:119(red)
- 34 -> combined:27(purple); evening:38(blue)
- 44 -> combined:42(purple); midday:153(red)
- 56 -> combined:50(blue); evening:25(purple); midday:27(purple)
- 77 -> combined:121(red); evening:78(blue); midday:60(purple)
- 99 -> combined:44(purple); midday:48(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(8.531842857142857)[R1,Mirror-Echo], 5(4.220228571428572)[R2,Mirror-Echo], 2(1.5852857142857142)[R1,Double-Pressure], 3(0.39558571428571426)[R3,Swap], 7(0.19092142857142858)[R3,Swap]
- P2: 4(8.201457142857143)[R1,XVAR-Cons(CEM)], 0(3.7224714285714287)[R2,XVAR-Cons(CE)], 9(1.4197142857142857)[R1,Mirror-Echo], 5(0.4813571428571428)[R3,Mirror-Echo], 3(0.35457142857142854)[R3,Swap]
- P3: 2(7.336807142857143)[R1,XVAR-Cons(CEM)], 3(2.902)[R3,XVAR-Cons(CE)], 0(2.7281)[R2,XVAR-Cons(CM)], 8(1.0671)[R2,Double-Pressure], 5(1.0461999999999998)[R2,Double-Pressure]
