# Aux Summary — Florida4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/Florida4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Florida
- combined: live=`data/cleaned/draws/Florida_draws.csv` snap=`sharepacks/2026-01-03/Florida4/aux/draws/Florida_draws.csv` n=1000 head=589, 862, 291, 195, 211
- midday: live=`data/cleaned/draws/Florida_Midday_draws.csv` snap=`sharepacks/2026-01-03/Florida4/aux/draws/Florida_Midday_draws.csv` n=1000 head=862, 195, 407, 377, 522
- evening: live=`data/cleaned/draws/Florida_Evening_draws.csv` snap=`sharepacks/2026-01-03/Florida4/aux/draws/Florida_Evening_draws.csv` n=1000 head=589, 291, 211, 870, 208

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=2 last_repeat_gap=31 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=37), P2:3 (gap=18), P3:4 (gap=18)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 737: score=37.31847142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 734: score=36.99865714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 733: score=36.99235 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 757: score=35.62703571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=35.307221428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 753: score=35.300914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 732: score=33.97387857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 634: score=33.597857142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 633: score=33.59155 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 730: score=33.52702142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 369: ds=871 sev=B
- 447: ds=755 sev=B
- 668: ds=745 sev=B
- 388: ds=736 sev=B
- 199: ds=735 sev=B
- 777: ds=727 sev=B
- 335: ds=700 sev=B
- 155: ds=689 sev=B
- 266: ds=674 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=65 sev=purple
  - 44: ds=48 sev=purple
  - 66: ds=43 sev=purple
  - 33: ds=30 sev=purple
  - 55: ds=24 sev=-
  - 99: ds=11 sev=-
  - 00: ds=10 sev=-
  - 22: ds=9 sev=-
  - 77: ds=7 sev=-
  - 11: ds=4 sev=-
- non_repeating:
  - 27: ds=82 sev=red
  - 57: ds=74 sev=red
  - 39: ds=68 sev=red
  - 79: ds=53 sev=blue
  - 67: ds=52 sev=blue
  - 38: ds=49 sev=blue
  - 05: ds=47 sev=blue
  - 18: ds=36 sev=purple
  - 17: ds=35 sev=purple
  - 35: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:469, 26:282, 16:171, 35:141, 31:129, 29:122, 33:97, 5:92, 7:81, 1:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=469 fs=0 fl=0 hz=0.003745318352059925, 26:ds=282 fs=2 fl=0 hz=0.006198347107438016, 16:ds=171 fs=1 fl=1 hz=0.005235602094240838, 35:ds=141 fs=1 fl=1 hz=0.007281553398058252, 31:ds=129 fs=17 fl=1 hz=0.02278481012658228, 29:ds=122 fs=23 fl=0 hz=0.03083109919571046, 33:ds=97 fs=14 fl=2 hz=0.017837235228539576, 5:ds=92 fs=19 fl=2 hz=0.024734982332155476, 7:ds=81 fs=40 fl=1 hz=0.04581005586592179, 1:ds=57 fs=4 fl=5 hz=0.00986842105263158

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S14: ds=50 flags=red+purple
- S2: ds=46 flags=blue+purple
- S5: ds=41 flags=purple
- S23: ds=34 flags=purple
- S20: ds=28 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3', '4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=3 tags=FLT,RS
  - 023: score=3 tags=FLT,RS
  - 059: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 149: score=3 tags=FLT,RS
  - 167: score=3 tags=FLT,RS
  - 239: score=3 tags=FLT,RS
  - 248: score=3 tags=FLT,RS
  - 257: score=3 tags=FLT,RS
  - 347: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=20 last_repeat_index=20

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=18), P2:8 (gap=24), P3:0 (gap=40)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:0 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 737: score=37.31847142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 734: score=36.99865714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 733: score=36.99235 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 757: score=35.62703571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=35.307221428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 753: score=35.300914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 732: score=33.97387857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 634: score=33.597857142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 633: score=33.59155 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 730: score=33.52702142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=985 sev=B
- 339: ds=872 sev=B
- 228: ds=812 sev=B
- 117: ds=794 sev=B
- 999: ds=784 sev=B
- 455: ds=738 sev=B
- 277: ds=726 sev=B
- 788: ds=699 sev=B
- 167: ds=696 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=83 sev=blue
  - 00: ds=68 sev=purple
  - 11: ds=63 sev=purple
  - 88: ds=32 sev=purple
  - 55: ds=28 sev=purple
  - 66: ds=21 sev=-
  - 33: ds=15 sev=-
  - 99: ds=5 sev=-
  - 22: ds=4 sev=-
  - 77: ds=3 sev=-
- non_repeating:
  - 39: ds=99 sev=red
  - 29: ds=64 sev=red
  - 18: ds=60 sev=red
  - 57: ds=51 sev=blue
  - 27: ds=42 sev=blue
  - 01: ds=40 sev=blue
  - 78: ds=38 sev=blue
  - 02: ds=31 sev=purple
  - 03: ds=31 sev=purple
  - 34: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:333, 32:234, 25:138, 16:85, 29:81, 5:78, 35:70, 3:68, 31:64, 14:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=333 fs=2 fl=0 hz=0.006125574272588055, 32:ds=234 fs=2 fl=0 hz=0.006289308176100629, 25:ds=138 fs=20 fl=1 hz=0.02602230483271375, 16:ds=85 fs=0 fl=2 hz=0.004524886877828055, 29:ds=81 fs=22 fl=2 hz=0.027149321266968323, 5:ds=78 fs=19 fl=3 hz=0.023887079261672092, 35:ds=70 fs=2 fl=1 hz=0.005506607929515419, 3:ds=68 fs=27 fl=0 hz=0.02944383860414395, 31:ds=64 fs=22 fl=1 hz=0.02619589977220957, 14:ds=56 fs=53 fl=0 hz=0.05656350053361793

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=68 flags=purple
- S23: ds=58 flags=purple
- S7: ds=50 flags=purple
- S4: ds=45 flags=blue+purple
- S3: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=2 last_repeat_gap=4 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=47), P2:6 (gap=15), P3:7 (gap=26)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:7 (ds=47)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 737: score=37.31847142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 734: score=36.99865714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 733: score=36.99235 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 757: score=35.62703571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=35.307221428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 753: score=35.300914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 732: score=33.97387857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 634: score=33.597857142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 633: score=33.59155 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 730: score=33.52702142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=963 sev=B
- 889: ds=922 sev=B
- 189: ds=863 sev=B
- 022: ds=851 sev=B
- 077: ds=816 sev=B
- 448: ds=783 sev=B
- 449: ds=778 sev=B
- 009: ds=773 sev=B
- 366: ds=729 sev=B
- 244: ds=713 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=104 sev=blue
  - 88: ds=76 sev=blue
  - 66: ds=26 sev=purple
  - 44: ds=24 sev=-
  - 33: ds=15 sev=-
  - 55: ds=12 sev=-
  - 99: ds=11 sev=-
  - 22: ds=10 sev=-
  - 00: ds=5 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 35: ds=126 sev=red
  - 25: ds=109 sev=red
  - 79: ds=75 sev=red
  - 49: ds=64 sev=red
  - 38: ds=58 sev=red
  - 47: ds=56 sev=red
  - 05: ds=47 sev=blue
  - 17: ds=44 sev=blue
  - 23: ds=41 sev=blue
  - 27: ds=41 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:679, 32:368, 26:141, 31:128, 16:105, 10:104, 20:97, 1:92, 33:87, 29:61

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=679 fs=1 fl=0 hz=0.010101010101010102, 32:ds=368 fs=4 fl=1 hz=0.010273972602739727, 26:ds=141 fs=3 fl=2 hz=0.008130081300813009, 31:ds=128 fs=19 fl=1 hz=0.024154589371980676, 16:ds=105 fs=1 fl=2 hz=0.006042296072507553, 10:ds=104 fs=8 fl=3 hz=0.013793103448275862, 20:ds=97 fs=20 fl=2 hz=0.026537997587454766, 1:ds=92 fs=2 fl=2 hz=0.010498687664041995, 33:ds=87 fs=16 fl=1 hz=0.019362186788154895, 29:ds=61 fs=27 fl=2 hz=0.031115879828326178

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S18: ds=79 flags=red+purple
- S21: ds=51 flags=purple
- S5: ds=42 flags=purple
- S17: ds=33 flags=purple
- S16: ds=32 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '4', '6'], 'pairs': {'remaining_count': 2}}
- top candidates:
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- none

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:47(blue); evening:47(blue)
- 06 -> combined:32(purple); midday:25(purple)
- 17 -> combined:35(purple); evening:44(blue)
- 18 -> combined:36(purple); midday:60(red)
- 23 -> combined:27(purple); evening:41(blue)
- 27 -> combined:82(red); evening:41(blue); midday:42(blue)
- 35 -> combined:33(purple); evening:126(red)
- 38 -> combined:49(blue); evening:58(red)
- 39 -> combined:68(red); evening:34(purple); midday:99(red)
- 44 -> combined:48(purple); midday:83(blue)
- 57 -> combined:74(red); evening:37(blue); midday:51(blue)
- 66 -> combined:43(purple); evening:26(purple)
- 67 -> combined:52(blue); evening:26(purple); midday:26(purple)
- 79 -> combined:53(blue); evening:75(red); midday:26(purple)
- 88 -> combined:65(purple); evening:76(blue); midday:32(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.645928571428572)[R1,XVAR-Cons(CEM)], 6(6.245128571428571)[R2,XVAR-Cons(CEM)], 2(1.2159857142857142)[R2,Mirror-Echo], 4(0.23435714285714285)[R3,Swap], 9(0.15557142857142858)[R3]
- P2: 3(3.166092857142857)[R1,XVAR-Cons(CM)], 5(2.4746571428571427)[R3,XVAR-Cons(CE)], 8(1.4659642857142856)[R1,Mirror-Echo], 6(1.1478571428571427)[R1,Double-Pressure], 1(1.0252999999999999)[R2,Double-Pressure]
- P3: 4(2.686635714285714)[R1,XVAR-Cons(CE)], 3(2.6803285714285714)[R3,XVAR-Cons(CM)], 0(1.7149999999999999)[R1,Double-Pressure], 7(1.4712857142857143)[R1,Mirror-Echo], 2(1.161857142857143)[R2,Mirror-Echo]
