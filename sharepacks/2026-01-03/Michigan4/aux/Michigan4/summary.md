# Aux Summary — Michigan4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/Michigan4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Michigan
- combined: live=`data/cleaned/draws/Michigan_draws.csv` snap=`sharepacks/2026-01-03/Michigan4/aux/draws/Michigan_draws.csv` n=1000 head=523, 975, 204, 032, 477
- midday: live=`data/cleaned/draws/Michigan_Midday_draws.csv` snap=`sharepacks/2026-01-03/Michigan4/aux/draws/Michigan_Midday_draws.csv` n=1000 head=975, 032, 583, 250, 731
- evening: live=`data/cleaned/draws/Michigan_Evening_draws.csv` snap=`sharepacks/2026-01-03/Michigan4/aux/draws/Michigan_Evening_draws.csv` n=1000 head=523, 204, 477, 214, 896

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=3 last_repeat_gap=2 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=31), P2:6 (gap=26), P3:8 (gap=33)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 368: score=47.91472857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 168: score=47.535778571428565 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=40.68116 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=39.449823571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 348: score=38.78415 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 361: score=38.40322857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 358: score=38.24243571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 308: score=38.02282142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 158: score=37.863485714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 338: score=37.76022142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=971 sev=B
- 111: ds=925 sev=B
- 077: ds=924 sev=B
- 556: ds=919 sev=B
- 144: ds=907 sev=B
- 599: ds=868 sev=B
- 099: ds=828 sev=B
- 247: ds=751 sev=B
- 135: ds=735 sev=B
- 399: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=74 sev=blue
  - 55: ds=60 sev=purple
  - 88: ds=56 sev=purple
  - 33: ds=31 sev=purple
  - 11: ds=27 sev=purple
  - 66: ds=26 sev=purple
  - 99: ds=15 sev=-
  - 00: ds=14 sev=-
  - 44: ds=13 sev=-
  - 77: ds=4 sev=-
- non_repeating:
  - 01: ds=80 sev=red
  - 45: ds=67 sev=red
  - 19: ds=62 sev=red
  - 28: ds=42 sev=blue
  - 39: ds=41 sev=blue
  - 26: ds=38 sev=blue
  - 67: ds=36 sev=purple
  - 15: ds=33 sev=purple
  - 18: ds=33 sev=purple
  - 34: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:464, 32:323, 1:110, 6:108, 23:94, 10:86, 5:82, 30:78, 15:76, 20:70

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=464 fs=2 fl=3 hz=0.010660980810234541, 32:ds=323 fs=1 fl=0 hz=0.003125, 1:ds=110 fs=5 fl=1 hz=0.009060022650056626, 6:ds=108 fs=14 fl=2 hz=0.019079685746352413, 23:ds=94 fs=12 fl=3 hz=0.018203883495145633, 10:ds=86 fs=15 fl=3 hz=0.02011173184357542, 5:ds=82 fs=22 fl=1 hz=0.026345933562428404, 30:ds=78 fs=58 fl=0 hz=0.06775700934579439, 15:ds=76 fs=21 fl=2 hz=0.02547065337763012, 20:ds=70 fs=22 fl=1 hz=0.025081788440567066

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S8: ds=64 flags=red+purple
- S2: ds=59 flags=purple
- S25: ds=56 flags=blue+purple
- S26: ds=53 flags=blue+purple
- S12: ds=38 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '6', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=3 last_repeat_gap=7 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=17), P2:2 (gap=32), P3:8 (gap=16)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 368: score=47.91472857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 168: score=47.535778571428565 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=40.68116 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=39.449823571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 348: score=38.78415 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 361: score=38.40322857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 358: score=38.24243571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 308: score=38.02282142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 158: score=37.863485714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 338: score=37.76022142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 339: ds=998 sev=B
- 266: ds=970 sev=B
- 667: ds=867 sev=B
- 188: ds=827 sev=B
- 345: ds=820 sev=B
- 499: ds=815 sev=B
- 114: ds=806 sev=B
- 777: ds=786 sev=B
- 099: ds=775 sev=B
- 566: ds=753 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=127 sev=red
  - 88: ds=77 sev=blue
  - 55: ds=36 sev=purple
  - 66: ds=28 sev=purple
  - 33: ds=15 sev=-
  - 11: ds=13 sev=-
  - 00: ds=11 sev=-
  - 77: ds=8 sev=-
  - 99: ds=7 sev=-
  - 44: ds=6 sev=-
- non_repeating:
  - 69: ds=64 sev=red
  - 67: ds=60 sev=red
  - 07: ds=52 sev=blue
  - 19: ds=51 sev=blue
  - 04: ds=50 sev=blue
  - 01: ds=48 sev=blue
  - 12: ds=48 sev=blue
  - 26: ds=34 sev=purple
  - 45: ds=33 sev=purple
  - 24: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:466, 26:322, 16:181, 27:179, 32:161, 23:145, 6:122, 5:121, 24:88, 1:86

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=466 fs=2 fl=2 hz=0.01078167115902965, 26:ds=322 fs=0 fl=1 hz=0.005249343832020997, 16:ds=181 fs=1 fl=0 hz=0.008032128514056224, 27:ds=179 fs=23 fl=0 hz=0.03054448871181939, 32:ds=161 fs=4 fl=2 hz=0.008739076154806492, 23:ds=145 fs=12 fl=2 hz=0.017412935323383085, 6:ds=122 fs=19 fl=1 hz=0.02551020408163265, 5:ds=121 fs=10 fl=2 hz=0.01892744479495268, 24:ds=88 fs=60 fl=0 hz=0.06734006734006734, 1:ds=86 fs=2 fl=1 hz=0.0067226890756302525

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S1: ds=93 flags=blue+purple
- S19: ds=78 flags=purple
- S25: ds=77 flags=purple
- S27: ds=73 flags=blue+purple
- S24: ds=72 flags=blue+purple
- S6: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=3 last_repeat_gap=20 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=25), P2:5 (gap=30), P3:5 (gap=26)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 368: score=47.91472857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 168: score=47.535778571428565 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=40.68116 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=39.449823571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 348: score=38.78415 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 361: score=38.40322857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 358: score=38.24243571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 308: score=38.02282142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 158: score=37.863485714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 338: score=37.76022142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 017: ds=977 sev=B
- 146: ds=903 sev=B
- 135: ds=824 sev=B
- 557: ds=803 sev=B
- 258: ds=791 sev=B
- 144: ds=767 sev=B
- 228: ds=758 sev=B
- 009: ds=750 sev=B
- 399: ds=729 sev=B
- 288: ds=712 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=113 sev=red
  - 22: ds=37 sev=purple
  - 33: ds=32 sev=purple
  - 55: ds=30 sev=purple
  - 99: ds=29 sev=purple
  - 88: ds=28 sev=purple
  - 11: ds=16 sev=-
  - 66: ds=13 sev=-
  - 00: ds=7 sev=-
  - 77: ds=2 sev=-
- non_repeating:
  - 34: ds=70 sev=red
  - 56: ds=68 sev=red
  - 48: ds=67 sev=red
  - 03: ds=52 sev=blue
  - 38: ds=51 sev=blue
  - 01: ds=40 sev=blue
  - 05: ds=40 sev=blue
  - 15: ds=40 sev=blue
  - 39: ds=39 sev=blue
  - 45: ds=38 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:232, 32:168, 17:102, 7:81, 9:64, 34:62, 1:55, 6:54, 23:47, 10:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=232 fs=4 fl=0 hz=0.0091324200913242, 32:ds=168 fs=2 fl=0 hz=0.005859375, 17:ds=102 fs=16 fl=3 hz=0.021252796420581654, 7:ds=81 fs=36 fl=0 hz=0.040178571428571425, 9:ds=64 fs=35 fl=1 hz=0.03854389721627409, 34:ds=62 fs=9 fl=2 hz=0.01649175412293853, 1:ds=55 fs=2 fl=5 hz=0.008130081300813009, 6:ds=54 fs=18 fl=3 hz=0.022850924918389557, 23:ds=47 fs=22 fl=3 hz=0.026399155227032733, 10:ds=43 fs=19 fl=3 hz=0.02301255230125523

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=62 flags=blue+purple
- S2: ds=54 flags=purple
- S9: ds=53 flags=red+purple
- S3: ds=52 flags=purple
- S20: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 099 -> combined:828(B); midday:775(B)
- 135 -> combined:735(B); evening:824(B)
- 144 -> combined:907(B); evening:767(B)
- 399 -> combined:681(B); evening:729(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:80(red); evening:40(blue); midday:48(blue)
- 06 -> combined:28(purple); midday:31(purple)
- 15 -> combined:33(purple); evening:40(blue)
- 19 -> combined:62(red); evening:31(purple); midday:51(blue)
- 22 -> combined:74(blue); evening:37(purple); midday:127(red)
- 26 -> combined:38(blue); midday:34(purple)
- 33 -> combined:31(purple); evening:32(purple)
- 34 -> combined:29(purple); evening:70(red)
- 39 -> combined:41(blue); evening:39(blue)
- 45 -> combined:67(red); evening:38(blue); midday:33(purple)
- 55 -> combined:60(purple); evening:30(purple); midday:36(purple)
- 56 -> combined:25(purple); evening:68(red)
- 66 -> combined:26(purple); midday:28(purple)
- 67 -> combined:36(purple); midday:60(red)
- 88 -> combined:56(purple); evening:28(purple); midday:77(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(7.452964285714286)[R1,XVAR-Cons(CEM)], 1(7.074014285714286)[R2,Mirror-Echo], 8(1.2691785714285715)[R1,Mirror-Echo], 6(0.5745714285714285)[R3,Mirror-Echo], 9(0.23435714285714285)[R3,Swap]
- P2: 6(6.168007142857142)[R1,XVAR-Cons(CEM)], 5(1.4957142857142856)[R1,Double-Pressure], 0(1.2761)[R2,Double-Pressure], 4(1.0374285714285714)[R2,Mirror-Echo], 3(1.0135)[R2,Double-Pressure]
- P3: 8(7.793757142857142)[R1,XVAR-Cons(CEM)], 1(1.782257142857143)[R3,XVAR-Cons(CE)], 5(1.4462857142857144)[R1,Double-Pressure], 6(0.9508)[R2,Double-Pressure], 9(0.82)[R2,Double-Pressure]
