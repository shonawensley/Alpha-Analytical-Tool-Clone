# Aux Summary — Michigan4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/Michigan4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Michigan
- combined: live=`data/cleaned/draws/Michigan_draws.csv` snap=`sharepacks/2026-01-01/Michigan4/aux/draws/Michigan_draws.csv` n=1000 head=477, 583, 214, 250, 896
- midday: live=`data/cleaned/draws/Michigan_Midday_draws.csv` snap=`sharepacks/2026-01-01/Michigan4/aux/draws/Michigan_Midday_draws.csv` n=1000 head=583, 250, 731, 587, 447
- evening: live=`data/cleaned/draws/Michigan_Evening_draws.csv` snap=`sharepacks/2026-01-01/Michigan4/aux/draws/Michigan_Evening_draws.csv` n=1000 head=477, 214, 896, 089, 772

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=3 last_repeat_gap=40 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=27), P2:6 (gap=22), P3:5 (gap=48)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 165: score=48.282354285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 168: score=43.87423571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 365: score=41.32499285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 125: score=40.85990714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 368: score=39.888485714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 565: score=39.674372857142856 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 105: score=39.65792142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 128: score=39.4234 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 965: score=38.45943571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 108: score=38.22141428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=967 sev=B
- 111: ds=921 sev=B
- 077: ds=920 sev=B
- 556: ds=915 sev=B
- 144: ds=903 sev=B
- 599: ds=864 sev=B
- 099: ds=824 sev=B
- 247: ds=747 sev=B
- 135: ds=731 sev=B
- 399: ds=677 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=70 sev=purple
  - 55: ds=56 sev=purple
  - 88: ds=52 sev=purple
  - 33: ds=27 sev=purple
  - 11: ds=23 sev=-
  - 66: ds=22 sev=-
  - 99: ds=11 sev=-
  - 00: ds=10 sev=-
  - 44: ds=9 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 04: ds=97 sev=red
  - 01: ds=76 sev=red
  - 45: ds=63 sev=red
  - 19: ds=58 sev=red
  - 59: ds=48 sev=blue
  - 23: ds=47 sev=blue
  - 28: ds=38 sev=blue
  - 39: ds=37 sev=blue
  - 26: ds=34 sev=purple
  - 67: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:460, 32:319, 1:106, 6:104, 23:90, 10:82, 5:78, 30:74, 15:72, 20:66

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=460 fs=2 fl=3 hz=0.010660980810234541, 32:ds=319 fs=1 fl=0 hz=0.003125, 1:ds=106 fs=5 fl=1 hz=0.009060022650056626, 6:ds=104 fs=14 fl=2 hz=0.019079685746352413, 23:ds=90 fs=12 fl=3 hz=0.018203883495145633, 10:ds=82 fs=15 fl=3 hz=0.02011173184357542, 5:ds=78 fs=22 fl=1 hz=0.026345933562428404, 30:ds=74 fs=58 fl=0 hz=0.06775700934579439, 15:ds=72 fs=21 fl=2 hz=0.02547065337763012, 20:ds=66 fs=23 fl=1 hz=0.02575107296137339

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S8: ds=60 flags=red+purple
- S2: ds=55 flags=purple
- S25: ds=52 flags=blue+purple
- S26: ds=49 flags=blue+purple
- S21: ds=48 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=13 streak=1 max=3 last_repeat_gap=5 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=18), P2:2 (gap=30), P3:5 (gap=31)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 165: score=48.282354285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 168: score=43.87423571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 365: score=41.32499285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 125: score=40.85990714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 368: score=39.888485714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 565: score=39.674372857142856 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 105: score=39.65792142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 128: score=39.4234 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 965: score=38.45943571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 108: score=38.22141428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 339: ds=996 sev=B
- 266: ds=968 sev=B
- 667: ds=865 sev=B
- 188: ds=825 sev=B
- 345: ds=818 sev=B
- 499: ds=813 sev=B
- 114: ds=804 sev=B
- 777: ds=784 sev=B
- 099: ds=773 sev=B
- 566: ds=751 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=125 sev=red
  - 88: ds=75 sev=blue
  - 55: ds=34 sev=purple
  - 66: ds=26 sev=purple
  - 33: ds=13 sev=-
  - 11: ds=11 sev=-
  - 00: ds=9 sev=-
  - 77: ds=6 sev=-
  - 99: ds=5 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 69: ds=62 sev=red
  - 67: ds=58 sev=red
  - 07: ds=50 sev=blue
  - 19: ds=49 sev=blue
  - 04: ds=48 sev=blue
  - 01: ds=46 sev=blue
  - 12: ds=46 sev=blue
  - 59: ds=42 sev=blue
  - 26: ds=32 sev=purple
  - 45: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:464, 26:320, 16:179, 27:177, 32:159, 23:143, 6:120, 5:119, 24:86, 1:84

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=464 fs=2 fl=2 hz=0.01078167115902965, 26:ds=320 fs=0 fl=1 hz=0.005249343832020997, 16:ds=179 fs=1 fl=0 hz=0.008032128514056224, 27:ds=177 fs=23 fl=0 hz=0.03054448871181939, 32:ds=159 fs=4 fl=2 hz=0.008739076154806492, 23:ds=143 fs=12 fl=2 hz=0.017412935323383085, 6:ds=120 fs=19 fl=1 hz=0.02551020408163265, 5:ds=119 fs=10 fl=2 hz=0.01892744479495268, 24:ds=86 fs=60 fl=0 hz=0.06734006734006734, 1:ds=84 fs=2 fl=1 hz=0.0067226890756302525

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S1: ds=91 flags=blue+purple
- S5: ds=84 flags=purple
- S19: ds=76 flags=purple
- S25: ds=75 flags=purple
- S27: ds=71 flags=blue+purple
- S24: ds=70 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=3 last_repeat_gap=18 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=41), P2:5 (gap=28), P3:3 (gap=25)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 165: score=48.282354285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 168: score=43.87423571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 365: score=41.32499285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 125: score=40.85990714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 368: score=39.888485714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 565: score=39.674372857142856 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 105: score=39.65792142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 128: score=39.4234 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 965: score=38.45943571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 108: score=38.22141428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 017: ds=975 sev=B
- 146: ds=901 sev=B
- 135: ds=822 sev=B
- 557: ds=801 sev=B
- 258: ds=789 sev=B
- 144: ds=765 sev=B
- 228: ds=756 sev=B
- 009: ds=748 sev=B
- 399: ds=727 sev=B
- 288: ds=710 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=111 sev=red
  - 22: ds=35 sev=purple
  - 33: ds=30 sev=purple
  - 55: ds=28 sev=purple
  - 99: ds=27 sev=purple
  - 88: ds=26 sev=purple
  - 11: ds=14 sev=-
  - 66: ds=11 sev=-
  - 00: ds=5 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 04: ds=73 sev=red
  - 34: ds=68 sev=red
  - 56: ds=66 sev=red
  - 48: ds=65 sev=red
  - 25: ds=61 sev=red
  - 03: ds=50 sev=blue
  - 38: ds=49 sev=blue
  - 01: ds=38 sev=blue
  - 05: ds=38 sev=blue
  - 15: ds=38 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:230, 32:166, 17:100, 7:79, 9:62, 34:60, 1:53, 6:52, 23:45, 10:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=230 fs=4 fl=0 hz=0.0091324200913242, 32:ds=166 fs=2 fl=0 hz=0.005859375, 17:ds=100 fs=16 fl=3 hz=0.021252796420581654, 7:ds=79 fs=36 fl=0 hz=0.040178571428571425, 9:ds=62 fs=35 fl=1 hz=0.03854389721627409, 34:ds=60 fs=9 fl=2 hz=0.01649175412293853, 1:ds=53 fs=2 fl=5 hz=0.008130081300813009, 6:ds=52 fs=18 fl=3 hz=0.022850924918389557, 23:ds=45 fs=22 fl=3 hz=0.026399155227032733, 10:ds=41 fs=19 fl=3 hz=0.02301255230125523

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=60 flags=blue+purple
- S2: ds=52 flags=purple
- S9: ds=51 flags=red+purple
- S3: ds=50 flags=purple
- S20: ds=49 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 099 -> combined:824(B); midday:773(B)
- 135 -> combined:731(B); evening:822(B)
- 144 -> combined:903(B); evening:765(B)
- 399 -> combined:677(B); evening:727(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:76(red); evening:38(blue); midday:46(blue)
- 04 -> combined:97(red); evening:73(red); midday:48(blue)
- 15 -> combined:29(purple); evening:38(blue)
- 19 -> combined:58(red); evening:29(purple); midday:49(blue)
- 22 -> combined:70(purple); evening:35(purple); midday:125(red)
- 23 -> combined:47(blue); evening:30(purple)
- 26 -> combined:34(purple); midday:32(purple)
- 33 -> combined:27(purple); evening:30(purple)
- 34 -> combined:25(purple); evening:68(red)
- 39 -> combined:37(blue); evening:37(blue)
- 45 -> combined:63(red); evening:36(purple); midday:31(purple)
- 55 -> combined:56(purple); evening:28(purple); midday:34(purple)
- 59 -> combined:48(blue); midday:42(blue)
- 67 -> combined:32(purple); midday:58(red)
- 88 -> combined:52(purple); evening:26(purple); midday:75(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(5.415021428571428)[R2,XVAR-Cons(CEM)], 3(3.929271428571428)[R1,XVAR-Cons(CE)], 9(2.0637142857142856)[R3,XVAR-Cons(CM)], 5(1.7149999999999999)[R1,Double-Pressure], 8(0.9834999999999999)[R2,Double-Pressure]
- P2: 6(5.89855)[R1,XVAR-Cons(CEM)], 2(3.9477142857142855)[R2,XVAR-Cons(CM)], 0(2.7457285714285717)[R3,XVAR-Cons(CM)], 5(1.536)[R1,Double-Pressure], 3(0.9717)[R2,Double-Pressure]
- P3: 5(8.497171428571429)[R1,XVAR-Cons(CEM)], 8(6.060664285714286)[R2,XVAR-Cons(CEM)], 2(2.610242857142857)[R3,XVAR-Cons(CM)], 3(1.4624642857142858)[R1,Mirror-Echo]
