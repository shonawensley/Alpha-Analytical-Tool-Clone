# Aux Summary — Indiana4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/Indiana4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Indiana
- combined: live=`data/cleaned/draws/Indiana_draws.csv` snap=`sharepacks/2026-01-02/Indiana4/aux/draws/Indiana_draws.csv` n=1000 head=909, 474, 539, 204, 512
- midday: live=`data/cleaned/draws/Indiana_Midday_draws.csv` snap=`sharepacks/2026-01-02/Indiana4/aux/draws/Indiana_Midday_draws.csv` n=1000 head=474, 204, 585, 144, 494
- evening: live=`data/cleaned/draws/Indiana_Evening_draws.csv` snap=`sharepacks/2026-01-02/Indiana4/aux/draws/Indiana_Evening_draws.csv` n=1000 head=909, 539, 512, 560, 998

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=3 last_repeat_gap=17 last_repeat_index=27

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=29), P2:2 (gap=17), P3:6 (gap=37)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 026: score=48.6162 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 626: score=46.639031428571435 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 056: score=43.262728571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 021: score=41.544 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 656: score=41.285560000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 066: score=38.789728571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 020: score=38.57385857142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 666: score=36.812560000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 036: score=36.73442857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 046: score=36.68052142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 068: ds=983 sev=B
- 066: ds=938 sev=B
- 669: ds=926 sev=B
- 258: ds=895 sev=B
- 566: ds=840 sev=B
- 688: ds=826 sev=B
- 667: ds=757 sev=B
- 244: ds=726 sev=B
- 779: ds=721 sev=B
- 335: ds=709 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=126 sev=red
  - 77: ds=50 sev=purple
  - 88: ds=33 sev=purple
  - 00: ds=29 sev=purple
  - 22: ds=17 sev=-
  - 11: ds=13 sev=-
  - 33: ds=12 sev=-
  - 55: ds=5 sev=-
  - 44: ds=1 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 18: ds=76 sev=red
  - 16: ds=60 sev=red
  - 01: ds=58 sev=red
  - 28: ds=53 sev=blue
  - 68: ds=46 sev=blue
  - 69: ds=43 sev=blue
  - 57: ds=38 sev=blue
  - 36: ds=37 sev=blue
  - 67: ds=37 sev=blue
  - 19: ds=34 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:277, 28:146, 9:109, 6:106, 18:97, 5:80, 1:74, 10:73, 19:64, 20:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=277 fs=2 fl=1 hz=0.006956521739130435, 28:ds=146 fs=19 fl=1 hz=0.025149700598802397, 9:ds=109 fs=52 fl=0 hz=0.05855855855855856, 6:ds=106 fs=12 fl=2 hz=0.016222479721900347, 18:ds=97 fs=24 fl=1 hz=0.029478458049886625, 5:ds=80 fs=22 fl=2 hz=0.026519337016574582, 1:ds=74 fs=4 fl=3 hz=0.008830022075055188, 10:ds=73 fs=17 fl=3 hz=0.023391812865497075, 19:ds=64 fs=28 fl=1 hz=0.031115879828326178, 20:ds=55 fs=18 fl=2 hz=0.021299254526091587

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=87 flags=purple
- S21: ds=71 flags=purple
- S13: ds=51 flags=red+purple
- S10: ds=48 flags=red+purple
- S5: ds=44 flags=purple
- S19: ds=33 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 028: score=3 tags=FLT,RS
  - 046: score=3 tags=FLT,RS
  - 136: score=3 tags=FLT,RS
  - 289: score=3 tags=FLT,RS
  - 469: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS
  - 568: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 037: score=2 tags=RS
  - 127: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=1 max=2 last_repeat_gap=81 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=47), P2:6 (gap=21), P3:0 (gap=37)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=47)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 026: score=48.6162 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 626: score=46.639031428571435 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 056: score=43.262728571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 021: score=41.544 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 656: score=41.285560000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 066: score=38.789728571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 020: score=38.57385857142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 666: score=36.812560000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 036: score=36.73442857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 046: score=36.68052142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 669: ds=999 sev=B
- 288: ds=994 sev=B
- 337: ds=946 sev=B
- 666: ds=918 sev=B
- 677: ds=916 sev=B
- 566: ds=873 sev=B
- 445: ds=809 sev=B
- 266: ds=769 sev=B
- 444: ds=767 sev=B
- 177: ds=730 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=138 sev=red
  - 77: ds=38 sev=purple
  - 33: ds=23 sev=-
  - 88: ds=16 sev=-
  - 00: ds=14 sev=-
  - 99: ds=10 sev=-
  - 22: ds=8 sev=-
  - 11: ds=6 sev=-
  - 55: ds=2 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 45: ds=103 sev=red
  - 16: ds=77 sev=red
  - 18: ds=69 sev=red
  - 56: ds=54 sev=blue
  - 68: ds=52 sev=blue
  - 05: ds=46 sev=blue
  - 19: ds=41 sev=blue
  - 01: ds=33 sev=purple
  - 08: ds=32 sev=purple
  - 12: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:244, 16:138, 6:105, 24:87, 28:80, 13:68, 5:56, 9:54, 7:50, 18:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=244 fs=3 fl=1 hz=0.007668711656441718, 16:ds=138 fs=4 fl=0 hz=0.007342143906020559, 6:ds=105 fs=19 fl=2 hz=0.024110218140068886, 24:ds=87 fs=43 fl=1 hz=0.0484048404840484, 28:ds=80 fs=18 fl=1 hz=0.022650056625141565, 13:ds=68 fs=15 fl=1 hz=0.021505376344086023, 5:ds=56 fs=18 fl=0 hz=0.022113022113022112, 9:ds=54 fs=52 fl=0 hz=0.05526036131774707, 7:ds=50 fs=39 fl=1 hz=0.04314994606256742, 18:ds=48 fs=31 fl=1 hz=0.035595105672969966

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=78 flags=blue+purple
- S20: ds=54 flags=purple
- S24: ds=49 flags=purple
- S5: ds=48 flags=purple
- S23: ds=43 flags=purple
- S21: ds=35 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 013: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=3 last_repeat_gap=14 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=37), P2:5 (gap=14), P3:1 (gap=32)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 026: score=48.6162 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 626: score=46.639031428571435 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 056: score=43.262728571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 021: score=41.544 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 656: score=41.285560000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 066: score=38.789728571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 020: score=38.57385857142857 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 666: score=36.812560000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 036: score=36.73442857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 046: score=36.68052142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 166: ds=896 sev=B
- 555: ds=881 sev=B
- 117: ds=869 sev=B
- 559: ds=868 sev=B
- 777: ds=840 sev=B
- 666: ds=813 sev=B
- 002: ds=801 sev=B
- 009: ds=790 sev=B
- 189: ds=744 sev=B
- 888: ds=737 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=63 sev=purple
  - 44: ds=58 sev=purple
  - 88: ds=52 sev=purple
  - 22: ds=43 sev=purple
  - 00: ds=37 sev=purple
  - 55: ds=34 sev=purple
  - 77: ds=25 sev=purple
  - 11: ds=16 sev=-
  - 33: ds=6 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 36: ds=64 sev=red
  - 69: ds=51 sev=blue
  - 18: ds=38 sev=blue
  - 49: ds=35 sev=purple
  - 14: ds=32 sev=purple
  - 28: ds=31 sev=purple
  - 16: ds=30 sev=purple
  - 01: ds=29 sev=purple
  - 13: ds=29 sev=purple
  - 34: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:201, 23:190, 10:114, 20:82, 28:73, 18:63, 9:60, 21:54, 6:53, 25:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=201 fs=2 fl=1 hz=0.006426735218508998, 23:ds=190 fs=20 fl=2 hz=0.030219780219780217, 10:ds=114 fs=18 fl=2 hz=0.02301495972382048, 20:ds=82 fs=17 fl=3 hz=0.022246941045606226, 28:ds=73 fs=22 fl=3 hz=0.02774694783573807, 18:ds=63 fs=22 fl=2 hz=0.026115342763873776, 9:ds=60 fs=49 fl=0 hz=0.05268817204301075, 21:ds=54 fs=51 fl=0 hz=0.0551948051948052, 6:ds=53 fs=18 fl=3 hz=0.025893958076448828, 25:ds=51 fs=17 fl=1 hz=0.01958650707290533

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=93 flags=red+purple
- S25: ds=68 flags=purple
- S21: ds=62 flags=red+purple
- S19: ds=51 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 566 -> combined:840(B); midday:873(B)
- 666 -> evening:813(B); midday:918(B)
- 669 -> combined:926(B); midday:999(B)
- 777 -> combined:689(B); evening:840(B)
- 779 -> combined:721(B); evening:729(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:29(purple); evening:37(purple)
- 01 -> combined:58(red); evening:29(purple); midday:33(purple)
- 16 -> combined:60(red); evening:30(purple); midday:77(red)
- 18 -> combined:76(red); evening:38(blue); midday:69(red)
- 19 -> combined:34(purple); midday:41(blue)
- 28 -> combined:53(blue); evening:31(purple); midday:26(purple)
- 36 -> combined:37(blue); evening:64(red)
- 45 -> combined:26(purple); midday:103(red)
- 66 -> combined:126(red); evening:63(purple); midday:138(red)
- 68 -> combined:46(blue); midday:52(blue)
- 69 -> combined:43(blue); evening:51(blue)
- 77 -> combined:50(purple); evening:25(purple); midday:38(purple)
- 88 -> combined:33(purple); evening:52(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.454528571428572)[R1,XVAR-Cons(CEM)], 6(4.173)[R2,XVAR-Cons(CM)], 1(1.0044)[R2,Double-Pressure], 9(0.5388999999999999)[R2,Swap], 7(0.36700000000000005)[R3,Swap]
- P2: 2(6.153471428571429)[R1,XVAR-Cons(CEM)], 5(3.3)[R2,XVAR-Cons(CE)], 6(1.327)[R1,Double-Pressure], 3(0.27169999999999994)[R2], 4(0.21779285714285712)[R3,Swap]
- P3: 6(8.5082)[R1,Mirror-Echo], 1(3.936)[R3,Mirror-Echo], 0(1.7149999999999999)[R1,Double-Pressure], 7(0.956)[R2,Double-Pressure], 4(0.3252785714285714)[R3,Swap]
