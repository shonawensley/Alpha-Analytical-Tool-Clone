# Aux Summary — Michigan4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/Michigan4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Michigan
- combined: live=`data/cleaned/draws/Michigan_draws.csv` snap=`sharepacks/2025-12-30/Michigan4/aux/draws/Michigan_draws.csv` n=1000 head=896, 731, 089, 587, 772
- midday: live=`data/cleaned/draws/Michigan_Midday_draws.csv` snap=`sharepacks/2025-12-30/Michigan4/aux/draws/Michigan_Midday_draws.csv` n=1000 head=731, 587, 447, 299, 774
- evening: live=`data/cleaned/draws/Michigan_Evening_draws.csv` snap=`sharepacks/2025-12-30/Michigan4/aux/draws/Michigan_Evening_draws.csv` n=1000 head=896, 089, 772, 700, 079

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=36 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=23), P2:5 (gap=25), P3:5 (gap=44)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 355: score=36.19266428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 315: score=35.83342142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 365: score=35.77269285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 155: score=35.756885714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 555: score=35.48385428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 115: score=35.397642857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 165: score=35.336914285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 515: score=35.12461142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 565: score=35.06388285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 358: score=34.806642857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=963 sev=B
- 111: ds=917 sev=B
- 077: ds=916 sev=B
- 556: ds=911 sev=B
- 144: ds=899 sev=B
- 599: ds=860 sev=B
- 099: ds=820 sev=B
- 247: ds=743 sev=B
- 135: ds=727 sev=B
- 399: ds=673 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=66 sev=purple
  - 55: ds=52 sev=purple
  - 88: ds=48 sev=purple
  - 33: ds=23 sev=-
  - 11: ds=19 sev=-
  - 66: ds=18 sev=-
  - 99: ds=7 sev=-
  - 00: ds=6 sev=-
  - 44: ds=5 sev=-
  - 77: ds=4 sev=-
- non_repeating:
  - 04: ds=93 sev=red
  - 01: ds=72 sev=red
  - 45: ds=59 sev=red
  - 05: ds=55 sev=blue
  - 19: ds=54 sev=blue
  - 59: ds=44 sev=blue
  - 23: ds=43 sev=blue
  - 25: ds=43 sev=blue
  - 28: ds=34 sev=purple
  - 39: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:456, 32:315, 1:102, 6:100, 23:86, 10:78, 5:74, 30:70, 15:68, 13:64

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=456 fs=2 fl=3 hz=0.010660980810234541, 32:ds=315 fs=1 fl=0 hz=0.003125, 1:ds=102 fs=5 fl=1 hz=0.009060022650056626, 6:ds=100 fs=14 fl=2 hz=0.019079685746352413, 23:ds=86 fs=12 fl=3 hz=0.018203883495145633, 10:ds=78 fs=15 fl=3 hz=0.02011173184357542, 5:ds=74 fs=22 fl=1 hz=0.026345933562428404, 30:ds=70 fs=59 fl=0 hz=0.06357758620689655, 15:ds=68 fs=21 fl=2 hz=0.02547065337763012, 13:ds=64 fs=20 fl=1 hz=0.02267818574514039

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S8: ds=56 flags=red+purple
- S2: ds=51 flags=purple
- S25: ds=48 flags=blue+purple
- S26: ds=45 flags=blue+purple
- S21: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 124: score=1 tags=FLT
  - 134: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=3 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=16), P2:2 (gap=28), P3:5 (gap=29)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 355: score=36.19266428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 315: score=35.83342142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 365: score=35.77269285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 155: score=35.756885714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 555: score=35.48385428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 115: score=35.397642857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 165: score=35.336914285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 515: score=35.12461142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 565: score=35.06388285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 358: score=34.806642857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 339: ds=994 sev=B
- 266: ds=966 sev=B
- 667: ds=863 sev=B
- 188: ds=823 sev=B
- 345: ds=816 sev=B
- 499: ds=811 sev=B
- 114: ds=802 sev=B
- 777: ds=782 sev=B
- 099: ds=771 sev=B
- 566: ds=749 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=123 sev=red
  - 88: ds=73 sev=blue
  - 55: ds=32 sev=purple
  - 66: ds=24 sev=-
  - 33: ds=11 sev=-
  - 11: ds=9 sev=-
  - 00: ds=7 sev=-
  - 77: ds=4 sev=-
  - 99: ds=3 sev=-
  - 44: ds=2 sev=-
- non_repeating:
  - 69: ds=60 sev=red
  - 67: ds=56 sev=red
  - 07: ds=48 sev=blue
  - 19: ds=47 sev=blue
  - 04: ds=46 sev=blue
  - 01: ds=44 sev=blue
  - 12: ds=44 sev=blue
  - 59: ds=40 sev=blue
  - 26: ds=30 sev=purple
  - 45: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:462, 26:318, 16:177, 27:175, 32:157, 23:141, 6:118, 5:117, 24:84, 1:82

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=462 fs=2 fl=2 hz=0.01078167115902965, 26:ds=318 fs=0 fl=1 hz=0.005249343832020997, 16:ds=177 fs=1 fl=0 hz=0.008032128514056224, 27:ds=175 fs=23 fl=0 hz=0.03054448871181939, 32:ds=157 fs=4 fl=2 hz=0.008739076154806492, 23:ds=141 fs=12 fl=2 hz=0.017412935323383085, 6:ds=118 fs=19 fl=1 hz=0.02551020408163265, 5:ds=117 fs=10 fl=2 hz=0.01892744479495268, 24:ds=84 fs=60 fl=0 hz=0.06734006734006734, 1:ds=82 fs=2 fl=1 hz=0.0067226890756302525

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S1: ds=89 flags=blue+purple
- S5: ds=82 flags=purple
- S19: ds=74 flags=purple
- S25: ds=73 flags=purple
- S27: ds=69 flags=blue+purple
- S24: ds=68 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '6'], 'pairs': {'remaining_count': 0}}
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
- current_index=24 streak=1 max=3 last_repeat_gap=16 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=39), P2:5 (gap=26), P3:3 (gap=23)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 355: score=36.19266428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 315: score=35.83342142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 365: score=35.77269285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 155: score=35.756885714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 555: score=35.48385428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 115: score=35.397642857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 165: score=35.336914285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 515: score=35.12461142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 565: score=35.06388285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 358: score=34.806642857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 017: ds=973 sev=B
- 146: ds=899 sev=B
- 135: ds=820 sev=B
- 557: ds=799 sev=B
- 258: ds=787 sev=B
- 144: ds=763 sev=B
- 228: ds=754 sev=B
- 009: ds=746 sev=B
- 399: ds=725 sev=B
- 288: ds=708 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=109 sev=red
  - 22: ds=33 sev=purple
  - 33: ds=28 sev=purple
  - 55: ds=26 sev=purple
  - 99: ds=25 sev=purple
  - 88: ds=24 sev=-
  - 11: ds=12 sev=-
  - 66: ds=9 sev=-
  - 00: ds=3 sev=-
  - 77: ds=2 sev=-
- non_repeating:
  - 04: ds=71 sev=red
  - 34: ds=66 sev=red
  - 56: ds=64 sev=red
  - 47: ds=63 sev=red
  - 48: ds=63 sev=red
  - 25: ds=59 sev=red
  - 03: ds=48 sev=blue
  - 38: ds=47 sev=blue
  - 01: ds=36 sev=purple
  - 05: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:228, 32:164, 17:98, 7:77, 9:60, 34:58, 1:51, 6:50, 28:44, 23:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=228 fs=4 fl=0 hz=0.0091324200913242, 32:ds=164 fs=2 fl=0 hz=0.005859375, 17:ds=98 fs=16 fl=3 hz=0.021252796420581654, 7:ds=77 fs=37 fl=0 hz=0.04013015184381779, 9:ds=60 fs=35 fl=1 hz=0.03854389721627409, 34:ds=58 fs=9 fl=2 hz=0.01649175412293853, 1:ds=51 fs=2 fl=5 hz=0.008130081300813009, 6:ds=50 fs=18 fl=3 hz=0.022850924918389557, 28:ds=44 fs=21 fl=2 hz=0.024390243902439025, 23:ds=43 fs=22 fl=3 hz=0.026399155227032733

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=58 flags=blue+purple
- S2: ds=50 flags=purple
- S9: ds=49 flags=red+purple
- S3: ds=48 flags=purple
- S20: ds=47 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3', '4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 036: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 126: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 189: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 369: score=3 tags=FLT,RS
  - 378: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 099 -> combined:820(B); midday:771(B)
- 135 -> combined:727(B); evening:820(B)
- 144 -> combined:899(B); evening:763(B)
- 399 -> combined:673(B); evening:725(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:72(red); evening:36(purple); midday:44(blue)
- 04 -> combined:93(red); evening:71(red); midday:46(blue)
- 05 -> combined:55(blue); evening:36(purple); midday:27(purple)
- 15 -> combined:25(purple); evening:36(purple)
- 19 -> combined:54(blue); evening:27(purple); midday:47(blue)
- 22 -> combined:66(purple); evening:33(purple); midday:123(red)
- 23 -> combined:43(blue); evening:28(purple)
- 25 -> combined:43(blue); evening:59(red)
- 26 -> combined:30(purple); midday:30(purple)
- 38 -> combined:29(purple); evening:47(blue)
- 39 -> combined:33(purple); evening:35(purple)
- 45 -> combined:59(red); evening:34(purple); midday:29(purple)
- 55 -> combined:52(purple); evening:26(purple); midday:32(purple)
- 59 -> combined:44(blue); midday:40(blue)
- 67 -> combined:28(purple); midday:56(red)
- 88 -> combined:48(purple); midday:73(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(3.005007142857143)[R1,XVAR-Cons(CE)], 1(2.5692285714285714)[R2,XVAR-Cons(CM)], 9(2.5474285714285716)[R3,XVAR-Cons(CM)], 5(1.7449999999999999)[R1,Double-Pressure], 4(1.2269999999999999)[R2,Double-Pressure]
- P2: 5(4.2620000000000005)[R1,XVAR-Cons(CE)], 1(2.902757142857143)[R3,Mirror-Echo], 6(2.8420285714285716)[R2,Mirror-Echo], 2(1.436)[R1,Double-Pressure], 0(1.1925)[R2,Double-Pressure]
- P3: 5(8.425657142857142)[R1,XVAR-Cons(CEM)], 8(6.039635714285714)[R2,Mirror-Echo], 3(3.3658214285714285)[R3,Mirror-Echo], 2(0.9552999999999999)[R2,Double-Pressure]
