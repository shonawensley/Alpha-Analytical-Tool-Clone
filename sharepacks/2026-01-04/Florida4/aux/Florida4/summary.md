# Aux Summary — Florida4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/Florida4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Florida
- combined: live=`data/cleaned/draws/Florida_draws.csv` snap=`sharepacks/2026-01-04/Florida4/aux/draws/Florida_draws.csv` n=1000 head=611, 708, 589, 862, 291
- midday: live=`data/cleaned/draws/Florida_Midday_draws.csv` snap=`sharepacks/2026-01-04/Florida4/aux/draws/Florida_Midday_draws.csv` n=1000 head=708, 862, 195, 407, 377
- evening: live=`data/cleaned/draws/Florida_Evening_draws.csv` snap=`sharepacks/2026-01-04/Florida4/aux/draws/Florida_Evening_draws.csv` n=1000 head=611, 589, 291, 211, 870

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=16 streak=1 max=2 last_repeat_gap=33 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=13), P2:3 (gap=20), P3:4 (gap=20)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 034: score=27.47067857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 033: score=27.437264285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 054: score=25.738564285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CM),R1,R2 src=cartesian
- 053: score=25.70515 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CM),R2,R3 src=cartesian
- 030: score=25.172787857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 037: score=24.71839285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 434: score=24.55663428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=repeat_endcap
- 032: score=24.40407857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 734: score=24.163885714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 733: score=24.13047142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 369: ds=873 sev=B
- 447: ds=757 sev=B
- 668: ds=747 sev=B
- 388: ds=738 sev=B
- 199: ds=737 sev=B
- 777: ds=729 sev=B
- 335: ds=702 sev=B
- 155: ds=691 sev=B
- 266: ds=676 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=67 sev=purple
  - 44: ds=50 sev=purple
  - 66: ds=45 sev=purple
  - 33: ds=32 sev=purple
  - 55: ds=26 sev=purple
  - 99: ds=13 sev=-
  - 00: ds=12 sev=-
  - 22: ds=11 sev=-
  - 77: ds=9 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 27: ds=84 sev=red
  - 57: ds=76 sev=red
  - 39: ds=70 sev=red
  - 79: ds=55 sev=blue
  - 67: ds=54 sev=blue
  - 38: ds=51 sev=blue
  - 05: ds=49 sev=blue
  - 18: ds=38 sev=blue
  - 17: ds=37 sev=blue
  - 35: ds=35 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:471, 26:284, 35:143, 31:131, 29:124, 33:99, 5:94, 7:83, 1:59, 2:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=471 fs=0 fl=0 hz=0.003745318352059925, 26:ds=284 fs=2 fl=0 hz=0.006198347107438016, 35:ds=143 fs=1 fl=1 hz=0.007281553398058252, 31:ds=131 fs=17 fl=1 hz=0.02278481012658228, 29:ds=124 fs=23 fl=0 hz=0.03083109919571046, 33:ds=99 fs=14 fl=2 hz=0.017837235228539576, 5:ds=94 fs=19 fl=2 hz=0.024734982332155476, 7:ds=83 fs=40 fl=1 hz=0.04581005586592179, 1:ds=59 fs=4 fl=5 hz=0.00986842105263158, 2:ds=53 fs=26 fl=2 hz=0.03278688524590164

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S14: ds=52 flags=red+purple
- S2: ds=48 flags=blue+purple
- S5: ds=43 flags=purple
- S23: ds=36 flags=purple
- S20: ds=30 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 149: score=4 tags=FLT,MIR,RS
  - 014: score=3 tags=FLT,RS
  - 023: score=3 tags=FLT,RS
  - 059: score=3 tags=MIR,RS
  - 167: score=3 tags=MIR,RS
  - 239: score=3 tags=FLT,RS
  - 248: score=3 tags=FLT,RS
  - 257: score=3 tags=MIR,RS
  - 347: score=3 tags=FLT,RS
  - 356: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=2 last_repeat_gap=21 last_repeat_index=20

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=14), P2:8 (gap=25), P3:0 (gap=41)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:0 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 034: score=27.47067857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 033: score=27.437264285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 054: score=25.738564285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CM),R1,R2 src=cartesian
- 053: score=25.70515 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CM),R2,R3 src=cartesian
- 030: score=25.172787857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 037: score=24.71839285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 434: score=24.55663428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=repeat_endcap
- 032: score=24.40407857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 734: score=24.163885714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 733: score=24.13047142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=986 sev=B
- 339: ds=873 sev=B
- 228: ds=813 sev=B
- 117: ds=795 sev=B
- 999: ds=785 sev=B
- 455: ds=739 sev=B
- 277: ds=727 sev=B
- 788: ds=700 sev=B
- 167: ds=697 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=84 sev=blue
  - 00: ds=69 sev=purple
  - 11: ds=64 sev=purple
  - 88: ds=33 sev=purple
  - 55: ds=29 sev=purple
  - 66: ds=22 sev=-
  - 33: ds=16 sev=-
  - 99: ds=6 sev=-
  - 22: ds=5 sev=-
  - 77: ds=4 sev=-
- non_repeating:
  - 39: ds=100 sev=red
  - 29: ds=65 sev=red
  - 18: ds=61 sev=red
  - 57: ds=52 sev=blue
  - 27: ds=43 sev=blue
  - 01: ds=41 sev=blue
  - 02: ds=32 sev=purple
  - 03: ds=32 sev=purple
  - 34: ds=28 sev=purple
  - 67: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:334, 32:235, 25:139, 16:86, 29:82, 5:79, 35:71, 3:69, 31:65, 14:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=334 fs=2 fl=0 hz=0.006125574272588055, 32:ds=235 fs=2 fl=0 hz=0.006289308176100629, 25:ds=139 fs=20 fl=1 hz=0.02602230483271375, 16:ds=86 fs=0 fl=2 hz=0.004524886877828055, 29:ds=82 fs=22 fl=2 hz=0.027149321266968323, 5:ds=79 fs=18 fl=3 hz=0.02323008849557522, 35:ds=71 fs=2 fl=1 hz=0.005506607929515419, 3:ds=69 fs=27 fl=0 hz=0.02944383860414395, 31:ds=65 fs=22 fl=1 hz=0.02619589977220957, 14:ds=57 fs=53 fl=0 hz=0.05656350053361793

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=69 flags=purple
- S23: ds=59 flags=purple
- S7: ds=51 flags=purple
- S4: ds=46 flags=blue+purple
- S3: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- _no candidates_

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=16 streak=1 max=2 last_repeat_gap=5 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=48), P2:6 (gap=16), P3:7 (gap=27)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:7 (ds=48)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 034: score=27.47067857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 033: score=27.437264285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 054: score=25.738564285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CM),R1,R2 src=cartesian
- 053: score=25.70515 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CM),R2,R3 src=cartesian
- 030: score=25.172787857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 037: score=24.71839285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 434: score=24.55663428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=repeat_endcap
- 032: score=24.40407857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian
- 734: score=24.163885714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 733: score=24.13047142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=964 sev=B
- 889: ds=923 sev=B
- 189: ds=864 sev=B
- 022: ds=852 sev=B
- 077: ds=817 sev=B
- 448: ds=784 sev=B
- 449: ds=779 sev=B
- 009: ds=774 sev=B
- 366: ds=730 sev=B
- 244: ds=714 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=105 sev=blue
  - 88: ds=77 sev=blue
  - 66: ds=27 sev=purple
  - 44: ds=25 sev=purple
  - 33: ds=16 sev=-
  - 55: ds=13 sev=-
  - 99: ds=12 sev=-
  - 22: ds=11 sev=-
  - 00: ds=6 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 35: ds=127 sev=red
  - 25: ds=110 sev=red
  - 79: ds=76 sev=red
  - 49: ds=65 sev=red
  - 38: ds=59 sev=red
  - 47: ds=57 sev=red
  - 05: ds=48 sev=blue
  - 17: ds=45 sev=blue
  - 23: ds=42 sev=blue
  - 27: ds=42 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:680, 32:369, 26:142, 31:129, 10:105, 20:98, 1:93, 33:88, 29:62, 13:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=680 fs=1 fl=0 hz=0.010101010101010102, 32:ds=369 fs=4 fl=1 hz=0.010273972602739727, 26:ds=142 fs=3 fl=2 hz=0.008130081300813009, 31:ds=129 fs=19 fl=1 hz=0.024154589371980676, 10:ds=105 fs=8 fl=3 hz=0.013793103448275862, 20:ds=98 fs=20 fl=2 hz=0.026537997587454766, 1:ds=93 fs=2 fl=2 hz=0.010498687664041995, 33:ds=88 fs=16 fl=1 hz=0.019362186788154895, 29:ds=62 fs=27 fl=2 hz=0.031115879828326178, 13:ds=59 fs=24 fl=1 hz=0.026595744680851064

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S18: ds=80 flags=red+purple
- S21: ds=52 flags=purple
- S5: ds=43 flags=purple
- S17: ds=34 flags=purple
- S16: ds=33 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '4'], 'pairs': {'remaining_count': 2}}
- top candidates:
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 238: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- none

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:49(blue); evening:48(blue)
- 06 -> combined:34(purple); midday:26(purple)
- 17 -> combined:37(blue); evening:45(blue)
- 18 -> combined:38(blue); midday:61(red)
- 23 -> combined:29(purple); evening:42(blue)
- 27 -> combined:84(red); evening:42(blue); midday:43(blue)
- 35 -> combined:35(purple); evening:127(red)
- 38 -> combined:51(blue); evening:59(red); midday:25(purple)
- 39 -> combined:70(red); evening:35(purple); midday:100(red)
- 44 -> combined:50(purple); evening:25(purple); midday:84(blue)
- 48 -> combined:25(purple); evening:26(purple)
- 55 -> combined:26(purple); midday:29(purple)
- 57 -> combined:76(red); evening:38(blue); midday:52(blue)
- 66 -> combined:45(purple); evening:27(purple)
- 67 -> combined:54(blue); evening:27(purple); midday:27(purple)
- 79 -> combined:55(blue); evening:76(red); midday:27(purple)
- 88 -> combined:67(purple); evening:77(blue); midday:33(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(2.4517928571428573)[R2,XVAR-Cons(CM)], 7(1.645)[R1,Double-Pressure], 2(1.1179999999999999)[R1,Double-Pressure], 9(1.0085714285714285)[R1,Double-Pressure], 6(0.9717)[R2,Double-Pressure]
- P2: 3(3.255957142857143)[R1,XVAR-Cons(CM)], 5(2.5238428571428573)[R3,XVAR-Cons(CE)], 8(1.5019285714285715)[R1,Mirror-Echo], 6(1.1777142857142857)[R1,Double-Pressure], 1(1.0761999999999998)[R2,Double-Pressure]
- P3: 4(2.7629285714285716)[R1,XVAR-Cons(CE)], 3(2.7295142857142856)[R3,XVAR-Cons(CM)], 0(1.7149999999999999)[R1,Double-Pressure], 7(1.5106428571428572)[R1,Mirror-Echo], 2(1.1963285714285714)[R2,Mirror-Echo]
