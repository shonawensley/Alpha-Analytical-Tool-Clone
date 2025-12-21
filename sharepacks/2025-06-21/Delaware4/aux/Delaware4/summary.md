# Aux Summary — Delaware4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/Delaware4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Delaware
- combined: live=`data/cleaned/draws/Delaware_draws.csv` snap=`sharepacks/2025-06-21/Delaware4/aux/draws/Delaware_draws.csv` n=1000 head=527, 772, 471, 489, 702
- midday: live=`data/cleaned/draws/Delaware_Midday_draws.csv` snap=`sharepacks/2025-06-21/Delaware4/aux/draws/Delaware_Midday_draws.csv` n=1000 head=772, 489, 937, 010, 993
- evening: live=`data/cleaned/draws/Delaware_Evening_draws.csv` snap=`sharepacks/2025-06-21/Delaware4/aux/draws/Delaware_Evening_draws.csv` n=1000 head=527, 471, 702, 277, 612

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=3 last_repeat_gap=11 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=33), P2:4 (gap=27), P3:4 (gap=19)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 845: score=41.672557142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 145: score=41.15146428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=37.604437142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 844: score=37.19134285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 144: score=36.67025 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 865: score=34.5956 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 165: score=34.07450714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 849: score=32.921099999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=32.40000714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 846: score=32.3241 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 455: ds=903 sev=B
- 228: ds=867 sev=B
- 355: ds=863 sev=B
- 144: ds=827 sev=B
- 599: ds=815 sev=B
- 009: ds=796 sev=B
- 055: ds=785 sev=B
- 668: ds=753 sev=B
- 189: ds=747 sev=B
- 368: ds=710 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=113 sev=red
  - 88: ds=52 sev=purple
  - 66: ds=38 sev=purple
  - 22: ds=23 sev=-
  - 11: ds=20 sev=-
  - 44: ds=19 sev=-
  - 33: ds=15 sev=-
  - 99: ds=9 sev=-
  - 00: ds=7 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 35: ds=65 sev=red
  - 04: ds=54 sev=blue
  - 09: ds=54 sev=blue
  - 69: ds=51 sev=blue
  - 36: ds=43 sev=blue
  - 68: ds=42 sev=blue
  - 03: ds=41 sev=blue
  - 28: ds=37 sev=blue
  - 29: ds=34 sev=purple
  - 58: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 13:174, 35:145, 31:116, 5:96, 4:94, 21:67, 33:64, 7:60, 14:56, 19:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 13:ds=174 fs=11 fl=1 hz=0.016883116883116882, 35:ds=145 fs=3 fl=0 hz=0.00909090909090909, 31:ds=116 fs=15 fl=3 hz=0.023622047244094488, 5:ds=96 fs=20 fl=1 hz=0.023411371237458192, 4:ds=94 fs=19 fl=1 hz=0.02600780234070221, 21:ds=67 fs=36 fl=1 hz=0.04111111111111111, 33:ds=64 fs=14 fl=2 hz=0.0188470066518847, 7:ds=60 fs=53 fl=0 hz=0.05656350053361793, 14:ds=56 fs=44 fl=0 hz=0.047311827956989246, 19:ds=51 fs=35 fl=1 hz=0.03956043956043956

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S4: ds=98 flags=purple
- S23: ds=78 flags=purple
- S24: ds=71 flags=blue+purple
- S17: ds=65 flags=red+purple
- S20: ds=64 flags=purple
- S22: ds=52 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=4 triggers={'mirror': True, 'root_due': [4], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=4 tags=FLT,PAT,RS
  - 238: score=4 tags=FLT,MIR,RS
  - 679: score=4 tags=FLT,PAT,RS
  - 049: score=3 tags=MIR,RS
  - 058: score=3 tags=MIR,RS
  - 067: score=3 tags=FLT,RS
  - 139: score=3 tags=FLT,RS
  - 247: score=3 tags=MIR,RS
  - 256: score=3 tags=FLT,RS
  - 346: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=26 streak=1 max=2 last_repeat_gap=71 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=27), P2:0 (gap=37), P3:6 (gap=14)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 845: score=41.672557142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 145: score=41.15146428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=37.604437142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 844: score=37.19134285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 144: score=36.67025 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 865: score=34.5956 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 165: score=34.07450714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 849: score=32.921099999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=32.40000714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 846: score=32.3241 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 008: ds=964 sev=B
- 589: ds=897 sev=B
- 244: ds=824 sev=B
- 035: ds=774 sev=B
- 122: ds=758 sev=B
- 778: ds=754 sev=B
- 336: ds=753 sev=B
- 368: ds=743 sev=B
- 588: ds=719 sev=B
- 118: ds=692 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=57 sev=purple
  - 55: ds=56 sev=purple
  - 11: ds=27 sev=purple
  - 66: ds=25 sev=purple
  - 22: ds=11 sev=-
  - 44: ds=9 sev=-
  - 33: ds=7 sev=-
  - 99: ds=4 sev=-
  - 00: ds=3 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 05: ds=86 sev=red
  - 06: ds=64 sev=red
  - 57: ds=52 sev=blue
  - 04: ds=45 sev=blue
  - 02: ds=41 sev=blue
  - 09: ds=41 sev=blue
  - 12: ds=40 sev=blue
  - 58: ds=36 sev=purple
  - 17: ds=33 sev=purple
  - 35: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:392, 16:218, 5:129, 17:106, 27:105, 33:98, 13:88, 3:86, 4:83, 35:72

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=392 fs=1 fl=3 hz=0.008888888888888889, 16:ds=218 fs=2 fl=1 hz=0.00657030223390276, 5:ds=129 fs=23 fl=2 hz=0.031685678073510776, 17:ds=106 fs=16 fl=3 hz=0.021420518602029315, 27:ds=105 fs=21 fl=1 hz=0.025142857142857144, 33:ds=98 fs=15 fl=2 hz=0.01893095768374165, 13:ds=88 fs=18 fl=0 hz=0.022511848341232227, 3:ds=86 fs=26 fl=0 hz=0.03082191780821918, 4:ds=83 fs=17 fl=2 hz=0.021566401816118047, 35:ds=72 fs=2 fl=1 hz=0.013636363636363637

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=84 flags=purple
- S3: ds=83 flags=purple
- S22: ds=81 flags=purple
- S20: ds=62 flags=purple
- S4: ds=58 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['5', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=3 last_repeat_gap=18 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=35), P2:4 (gap=18), P3:9 (gap=38)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 845: score=41.672557142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 145: score=41.15146428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=37.604437142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 844: score=37.19134285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 144: score=36.67025 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 865: score=34.5956 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 165: score=34.07450714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 849: score=32.921099999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=32.40000714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 846: score=32.3241 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=975 sev=B
- 699: ds=965 sev=B
- 019: ds=950 sev=B
- 449: ds=825 sev=B
- 244: ds=780 sev=B
- 116: ds=765 sev=B
- 229: ds=755 sev=B
- 055: ds=723 sev=B
- 399: ds=681 sev=B
- 000: ds=679 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=101 sev=blue
  - 55: ds=90 sev=blue
  - 33: ds=87 sev=blue
  - 44: ds=54 sev=purple
  - 22: ds=41 sev=purple
  - 88: ds=26 sev=purple
  - 66: ds=19 sev=-
  - 11: ds=10 sev=-
  - 00: ds=8 sev=-
  - 77: ds=3 sev=-
- non_repeating:
  - 36: ds=77 sev=red
  - 35: ds=64 sev=red
  - 24: ds=62 sev=red
  - 03: ds=49 sev=blue
  - 08: ds=47 sev=blue
  - 34: ds=38 sev=blue
  - 28: ds=37 sev=blue
  - 69: ds=35 sev=purple
  - 48: ds=32 sev=purple
  - 89: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:227, 32:124, 13:87, 21:83, 28:78, 31:58, 11:55, 5:48, 4:47, 19:40

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=227 fs=1 fl=2 hz=0.005270092226613966, 32:ds=124 fs=1 fl=2 hz=0.007079646017699115, 13:ds=87 fs=14 fl=1 hz=0.01839080459770115, 21:ds=83 fs=54 fl=0 hz=0.06242774566473988, 28:ds=78 fs=20 fl=2 hz=0.024043715846994534, 31:ds=58 fs=18 fl=3 hz=0.02458100558659218, 11:ds=55 fs=50 fl=0 hz=0.05405405405405406, 5:ds=48 fs=10 fl=3 hz=0.014238773274917854, 4:ds=47 fs=24 fl=0 hz=0.02575107296137339, 19:ds=40 fs=27 fl=2 hz=0.03049421661409043

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=66 flags=purple
- S4: ds=49 flags=purple
- S6: ds=45 flags=red+purple
- S10: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 035: score=4 tags=FLT,MIR,RS
  - 278: score=4 tags=FLT,MIR,RS
  - 368: score=4 tags=FLT,MIR,RS
  - 089: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 179: score=3 tags=FLT,RS
  - 269: score=3 tags=FLT,RS
  - 359: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 017: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 055 -> combined:785(B); evening:723(B)
- 244 -> evening:780(B); midday:824(B)
- 368 -> combined:710(B); midday:743(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:41(blue); evening:49(blue)
- 04 -> combined:54(blue); evening:27(purple); midday:45(blue)
- 09 -> combined:54(blue); evening:27(purple); midday:41(blue)
- 28 -> combined:37(blue); evening:37(blue)
- 35 -> combined:65(red); evening:64(red); midday:32(purple)
- 36 -> combined:43(blue); evening:77(red)
- 55 -> combined:113(red); evening:90(blue); midday:56(purple)
- 58 -> combined:32(purple); midday:36(purple)
- 66 -> combined:38(purple); midday:25(purple)
- 68 -> combined:42(blue); midday:28(purple)
- 69 -> combined:51(blue); evening:35(purple); midday:25(purple)
- 88 -> combined:52(purple); evening:26(purple); midday:57(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 8(4.166042857142857)[R1,Mirror-Echo], 1(3.6449499999999997)[R2,XVAR-Cons(CM)], 9(1.7149999999999999)[R1,Double-Pressure], 5(1.5061428571428572)[R1,Double-Pressure], 3(0.7394285714285714)[R3,Mirror-Echo]
- P2: 4(7.040057142857144)[R1,XVAR-Cons(CEM)], 6(3.4631)[R2,XVAR-Cons(CM)], 0(1.7449999999999999)[R1,Double-Pressure], 8(1.0344)[R2,Double-Pressure], 9(0.48894999999999994)[R3,Mirror-Echo]
- P3: 5(5.466457142857143)[R2,XVAR-Cons(CEM)], 4(3.485242857142857)[R1,XVAR-Cons(CM)], 9(1.7149999999999999)[R1,Double-Pressure], 6(1.1179999999999999)[R1,Double-Pressure], 3(1.0807)[R2,Double-Pressure]
