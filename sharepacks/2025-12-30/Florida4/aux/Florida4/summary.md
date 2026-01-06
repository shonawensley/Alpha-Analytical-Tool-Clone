# Aux Summary — Florida4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/Florida4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Florida
- combined: live=`data/cleaned/draws/Florida_draws.csv` snap=`sharepacks/2025-12-30/Florida4/aux/draws/Florida_draws.csv` n=1000 head=208, 522, 003, 909, 985
- midday: live=`data/cleaned/draws/Florida_Midday_draws.csv` snap=`sharepacks/2025-12-30/Florida4/aux/draws/Florida_Midday_draws.csv` n=1000 head=522, 909, 452, 945, 425
- evening: live=`data/cleaned/draws/Florida_Evening_draws.csv` snap=`sharepacks/2025-12-30/Florida4/aux/draws/Florida_Evening_draws.csv` n=1000 head=208, 003, 985, 346, 310

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=2 last_repeat_gap=23 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=30), P2:6 (gap=22), P3:7 (gap=27)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 767: score=51.59213642857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 867: score=51.44260464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 797: score=46.23725785714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 777: score=45.90125785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 897: score=45.65949428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 861: score=44.60561785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 877: score=42.49834285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 787: score=41.19040071428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 761: score=40.804135714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 757: score=39.24988642857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 244: ds=995 sev=B
- 369: ds=863 sev=B
- 447: ds=747 sev=B
- 668: ds=737 sev=B
- 388: ds=728 sev=B
- 199: ds=727 sev=B
- 777: ds=719 sev=B
- 335: ds=692 sev=B
- 155: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=57 sev=purple
  - 44: ds=40 sev=purple
  - 66: ds=35 sev=purple
  - 77: ds=29 sev=purple
  - 33: ds=22 sev=-
  - 11: ds=18 sev=-
  - 55: ds=16 sev=-
  - 99: ds=3 sev=-
  - 00: ds=2 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 27: ds=74 sev=red
  - 78: ds=69 sev=red
  - 57: ds=66 sev=red
  - 39: ds=60 sev=red
  - 26: ds=51 sev=blue
  - 79: ds=45 sev=blue
  - 67: ds=44 sev=blue
  - 38: ds=41 sev=blue
  - 05: ds=39 sev=blue
  - 19: ds=34 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:461, 26:274, 16:163, 35:133, 31:121, 29:114, 33:89, 5:84, 27:74, 7:73

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=461 fs=0 fl=0 hz=0.003745318352059925, 26:ds=274 fs=2 fl=0 hz=0.006198347107438016, 16:ds=163 fs=1 fl=1 hz=0.005235602094240838, 35:ds=133 fs=1 fl=1 hz=0.007281553398058252, 31:ds=121 fs=19 fl=1 hz=0.022779043280182234, 29:ds=114 fs=23 fl=0 hz=0.03083109919571046, 33:ds=89 fs=14 fl=2 hz=0.017837235228539576, 5:ds=84 fs=19 fl=2 hz=0.024734982332155476, 27:ds=74 fs=21 fl=1 hz=0.024498886414253896, 7:ds=73 fs=40 fl=1 hz=0.04581005586592179

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=58 flags=red+purple
- S14: ds=42 flags=red+purple
- S16: ds=41 flags=purple
- S2: ds=38 flags=blue+purple
- S5: ds=33 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 149: score=3 tags=FLT,RS
  - 158: score=3 tags=FLT,RS
  - 167: score=3 tags=FLT,RS
  - 248: score=3 tags=FLT,RS
  - 257: score=3 tags=FLT,RS
  - 347: score=3 tags=FLT,RS
  - 356: score=3 tags=FLT,RS
  - 689: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=2 last_repeat_gap=16 last_repeat_index=20

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=29), P2:9 (gap=22), P3:0 (gap=36)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 767: score=51.59213642857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 867: score=51.44260464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 797: score=46.23725785714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 777: score=45.90125785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 897: score=45.65949428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 861: score=44.60561785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 877: score=42.49834285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 787: score=41.19040071428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 761: score=40.804135714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 757: score=39.24988642857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=981 sev=B
- 339: ds=868 sev=B
- 228: ds=808 sev=B
- 117: ds=790 sev=B
- 999: ds=780 sev=B
- 455: ds=734 sev=B
- 277: ds=722 sev=B
- 788: ds=695 sev=B
- 167: ds=692 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=79 sev=blue
  - 00: ds=64 sev=purple
  - 11: ds=59 sev=purple
  - 88: ds=28 sev=purple
  - 55: ds=24 sev=-
  - 66: ds=17 sev=-
  - 77: ds=14 sev=-
  - 33: ds=11 sev=-
  - 99: ds=1 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 15: ds=110 sev=red
  - 39: ds=95 sev=red
  - 19: ds=73 sev=red
  - 29: ds=60 sev=red
  - 18: ds=56 sev=red
  - 57: ds=47 sev=blue
  - 27: ds=38 sev=blue
  - 01: ds=36 sev=purple
  - 78: ds=34 sev=purple
  - 28: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:329, 32:230, 25:134, 27:90, 16:81, 29:77, 5:74, 35:66, 3:64, 31:60

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=329 fs=2 fl=0 hz=0.006125574272588055, 32:ds=230 fs=2 fl=0 hz=0.006289308176100629, 25:ds=134 fs=20 fl=1 hz=0.02602230483271375, 27:ds=90 fs=21 fl=1 hz=0.02634730538922156, 16:ds=81 fs=0 fl=2 hz=0.004524886877828055, 29:ds=77 fs=22 fl=2 hz=0.027149321266968323, 5:ds=74 fs=21 fl=3 hz=0.025945945945945948, 35:ds=66 fs=2 fl=1 hz=0.005506607929515419, 3:ds=64 fs=27 fl=0 hz=0.02944383860414395, 31:ds=60 fs=22 fl=1 hz=0.02619589977220957

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=99 flags=purple
- S2: ds=64 flags=purple
- S23: ds=54 flags=purple
- S17: ds=52 flags=purple
- S7: ds=46 flags=purple
- S4: ds=41 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3', '6', '7', '8'], 'pairs': {'remaining_count': 1}}
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
  - 026: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=2 last_repeat_gap=24 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=43), P2:7 (gap=44), P3:7 (gap=22)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:7 (ds=43), P2:7 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 767: score=51.59213642857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 867: score=51.44260464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 797: score=46.23725785714286 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 777: score=45.90125785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 897: score=45.65949428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 861: score=44.60561785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 877: score=42.49834285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 787: score=41.19040071428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 761: score=40.804135714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 757: score=39.24988642857143 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=997 sev=B
- 133: ds=959 sev=B
- 889: ds=918 sev=B
- 189: ds=859 sev=B
- 022: ds=847 sev=B
- 077: ds=812 sev=B
- 448: ds=779 sev=B
- 449: ds=774 sev=B
- 009: ds=769 sev=B
- 366: ds=725 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=100 sev=blue
  - 88: ds=72 sev=blue
  - 66: ds=22 sev=-
  - 44: ds=20 sev=-
  - 33: ds=11 sev=-
  - 11: ds=9 sev=-
  - 55: ds=8 sev=-
  - 99: ds=7 sev=-
  - 22: ds=6 sev=-
  - 00: ds=1 sev=-
- non_repeating:
  - 35: ds=122 sev=red
  - 25: ds=105 sev=red
  - 78: ds=89 sev=red
  - 79: ds=71 sev=red
  - 49: ds=60 sev=red
  - 38: ds=54 sev=blue
  - 47: ds=52 sev=blue
  - 05: ds=43 sev=blue
  - 07: ds=43 sev=blue
  - 17: ds=40 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:675, 32:364, 26:137, 31:124, 16:101, 10:100, 20:93, 1:88, 33:83, 29:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=675 fs=1 fl=0 hz=0.010101010101010102, 32:ds=364 fs=4 fl=1 hz=0.010273972602739727, 26:ds=137 fs=3 fl=2 hz=0.008130081300813009, 31:ds=124 fs=19 fl=1 hz=0.024154589371980676, 16:ds=101 fs=1 fl=2 hz=0.006042296072507553, 10:ds=100 fs=8 fl=3 hz=0.013793103448275862, 20:ds=93 fs=20 fl=2 hz=0.026537997587454766, 1:ds=88 fs=2 fl=2 hz=0.010498687664041995, 33:ds=83 fs=16 fl=1 hz=0.019362186788154895, 29:ds=57 fs=27 fl=2 hz=0.031115879828326178

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S18: ds=75 flags=red+purple
- S21: ds=47 flags=purple
- S5: ds=38 flags=purple
- S17: ds=29 flags=purple
- S16: ds=28 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 2}}
- top candidates:
  - 017: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 067: score=1 tags=FLT
  - 078: score=1 tags=FLT
  - 079: score=1 tags=FLT
  - 127: score=1 tags=FLT
  - 137: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 244 -> combined:995(B); evening:709(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:39(blue); evening:43(blue)
- 17 -> combined:27(purple); evening:40(blue)
- 18 -> combined:28(purple); midday:56(red)
- 19 -> combined:34(purple); midday:73(red)
- 26 -> combined:51(blue); evening:28(purple); midday:25(purple)
- 27 -> combined:74(red); evening:37(blue); midday:38(blue)
- 29 -> combined:34(purple); midday:60(red)
- 35 -> combined:25(purple); evening:122(red)
- 37 -> combined:27(purple); evening:37(blue)
- 38 -> combined:41(blue); evening:54(blue)
- 39 -> combined:60(red); evening:30(purple); midday:95(red)
- 44 -> combined:40(purple); midday:79(blue)
- 57 -> combined:66(red); evening:33(purple); midday:47(blue)
- 77 -> combined:29(purple); evening:100(blue)
- 78 -> combined:69(red); evening:89(red); midday:34(purple)
- 79 -> combined:45(blue); evening:71(red)
- 88 -> combined:57(purple); evening:72(blue); midday:28(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 8(8.089392857142856)[R1,XVAR-Cons(CEM)], 7(7.9756)[R2,XVAR-Cons(CEM)], 3(0.5413642857142857)[R3,Mirror-Echo], 6(0.29800000000000004)[R3,Swap], 5(0.10748571428571428)[R3]
- P2: 6(6.519735714285714)[R1,XVAR-Cons(CEM)], 9(3.6648571428571426)[R2,XVAR-Cons(CM)], 7(3.328857142857143)[R3,XVAR-Cons(CE)], 8(1.1179999999999999)[R2,Double-Pressure], 5(0.1774857142857143)[R3,Swap]
- P3: 7(7.0800928571428585)[R1,XVAR-Cons(CEM)], 1(3.3087999999999997)[R2,XVAR-Cons(CE)], 0(1.115)[R1,Swap], 3(0.9552999999999999)[R2,Double-Pressure], 4(0.2114285714285714)[R3,Swap]
