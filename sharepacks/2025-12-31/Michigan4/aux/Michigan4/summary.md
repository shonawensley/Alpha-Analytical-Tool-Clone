# Aux Summary — Michigan4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/Michigan4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Michigan
- combined: live=`data/cleaned/draws/Michigan_draws.csv` snap=`sharepacks/2025-12-31/Michigan4/aux/draws/Michigan_draws.csv` n=1000 head=214, 250, 896, 731, 089
- midday: live=`data/cleaned/draws/Michigan_Midday_draws.csv` snap=`sharepacks/2025-12-31/Michigan4/aux/draws/Michigan_Midday_draws.csv` n=1000 head=250, 731, 587, 447, 299
- evening: live=`data/cleaned/draws/Michigan_Evening_draws.csv` snap=`sharepacks/2025-12-31/Michigan4/aux/draws/Michigan_Evening_draws.csv` n=1000 head=214, 896, 089, 772, 700

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=38 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=25), P2:6 (gap=20), P3:5 (gap=46)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 365: score=42.937016071428566 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 965: score=39.86080714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 165: score=39.8219 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 565: score=39.51866 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 368: score=39.02705714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 968: score=38.55132857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 168: score=38.51242142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 868: score=36.538217857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 325: score=35.80157142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 363: score=35.79960428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=965 sev=B
- 111: ds=919 sev=B
- 077: ds=918 sev=B
- 556: ds=913 sev=B
- 144: ds=901 sev=B
- 599: ds=862 sev=B
- 099: ds=822 sev=B
- 247: ds=745 sev=B
- 135: ds=729 sev=B
- 399: ds=675 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=68 sev=purple
  - 55: ds=54 sev=purple
  - 88: ds=50 sev=purple
  - 33: ds=25 sev=purple
  - 11: ds=21 sev=-
  - 66: ds=20 sev=-
  - 99: ds=9 sev=-
  - 00: ds=8 sev=-
  - 44: ds=7 sev=-
  - 77: ds=6 sev=-
- non_repeating:
  - 04: ds=95 sev=red
  - 01: ds=74 sev=red
  - 45: ds=61 sev=red
  - 19: ds=56 sev=red
  - 59: ds=46 sev=blue
  - 23: ds=45 sev=blue
  - 28: ds=36 sev=purple
  - 39: ds=35 sev=purple
  - 26: ds=32 sev=purple
  - 38: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:458, 32:317, 1:104, 6:102, 23:88, 10:80, 5:76, 30:72, 15:70, 13:66

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=458 fs=2 fl=3 hz=0.010660980810234541, 32:ds=317 fs=1 fl=0 hz=0.003125, 1:ds=104 fs=5 fl=1 hz=0.009060022650056626, 6:ds=102 fs=14 fl=2 hz=0.019079685746352413, 23:ds=88 fs=12 fl=3 hz=0.018203883495145633, 10:ds=80 fs=15 fl=3 hz=0.02011173184357542, 5:ds=76 fs=22 fl=1 hz=0.026345933562428404, 30:ds=72 fs=58 fl=0 hz=0.06775700934579439, 15:ds=70 fs=21 fl=2 hz=0.02547065337763012, 13:ds=66 fs=20 fl=1 hz=0.02267818574514039

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S8: ds=58 flags=red+purple
- S2: ds=53 flags=purple
- S25: ds=50 flags=blue+purple
- S26: ds=47 flags=blue+purple
- S21: ds=46 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=3 last_repeat_gap=4 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=17), P2:2 (gap=29), P3:5 (gap=30)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 365: score=42.937016071428566 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 965: score=39.86080714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 165: score=39.8219 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 565: score=39.51866 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 368: score=39.02705714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 968: score=38.55132857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 168: score=38.51242142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 868: score=36.538217857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 325: score=35.80157142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 363: score=35.79960428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 339: ds=995 sev=B
- 266: ds=967 sev=B
- 667: ds=864 sev=B
- 188: ds=824 sev=B
- 345: ds=817 sev=B
- 499: ds=812 sev=B
- 114: ds=803 sev=B
- 777: ds=783 sev=B
- 099: ds=772 sev=B
- 566: ds=750 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=124 sev=red
  - 88: ds=74 sev=blue
  - 55: ds=33 sev=purple
  - 66: ds=25 sev=purple
  - 33: ds=12 sev=-
  - 11: ds=10 sev=-
  - 00: ds=8 sev=-
  - 77: ds=5 sev=-
  - 99: ds=4 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 69: ds=61 sev=red
  - 67: ds=57 sev=red
  - 07: ds=49 sev=blue
  - 19: ds=48 sev=blue
  - 04: ds=47 sev=blue
  - 01: ds=45 sev=blue
  - 12: ds=45 sev=blue
  - 59: ds=41 sev=blue
  - 26: ds=31 sev=purple
  - 45: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:463, 26:319, 16:178, 27:176, 32:158, 23:142, 6:119, 5:118, 24:85, 1:83

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=463 fs=2 fl=2 hz=0.01078167115902965, 26:ds=319 fs=0 fl=1 hz=0.005249343832020997, 16:ds=178 fs=1 fl=0 hz=0.008032128514056224, 27:ds=176 fs=23 fl=0 hz=0.03054448871181939, 32:ds=158 fs=4 fl=2 hz=0.008739076154806492, 23:ds=142 fs=12 fl=2 hz=0.017412935323383085, 6:ds=119 fs=19 fl=1 hz=0.02551020408163265, 5:ds=118 fs=10 fl=2 hz=0.01892744479495268, 24:ds=85 fs=60 fl=0 hz=0.06734006734006734, 1:ds=83 fs=2 fl=1 hz=0.0067226890756302525

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S1: ds=90 flags=blue+purple
- S5: ds=83 flags=purple
- S19: ds=75 flags=purple
- S25: ds=74 flags=purple
- S27: ds=70 flags=blue+purple
- S24: ds=69 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 168: score=2 tags=FLT,MIR
  - 169: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=17 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=40), P2:5 (gap=27), P3:3 (gap=24)
- consensus_notes: P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:5 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 365: score=42.937016071428566 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 965: score=39.86080714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 165: score=39.8219 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 565: score=39.51866 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=repeat_endcap
- 368: score=39.02705714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 968: score=38.55132857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 168: score=38.51242142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 868: score=36.538217857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 325: score=35.80157142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 363: score=35.79960428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 017: ds=974 sev=B
- 146: ds=900 sev=B
- 135: ds=821 sev=B
- 557: ds=800 sev=B
- 258: ds=788 sev=B
- 144: ds=764 sev=B
- 228: ds=755 sev=B
- 009: ds=747 sev=B
- 399: ds=726 sev=B
- 288: ds=709 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=110 sev=red
  - 22: ds=34 sev=purple
  - 33: ds=29 sev=purple
  - 55: ds=27 sev=purple
  - 99: ds=26 sev=purple
  - 88: ds=25 sev=purple
  - 11: ds=13 sev=-
  - 66: ds=10 sev=-
  - 00: ds=4 sev=-
  - 77: ds=3 sev=-
- non_repeating:
  - 04: ds=72 sev=red
  - 34: ds=67 sev=red
  - 56: ds=65 sev=red
  - 47: ds=64 sev=red
  - 48: ds=64 sev=red
  - 25: ds=60 sev=red
  - 03: ds=49 sev=blue
  - 38: ds=48 sev=blue
  - 01: ds=37 sev=blue
  - 05: ds=37 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:229, 32:165, 17:99, 7:78, 9:61, 34:59, 1:52, 6:51, 28:45, 23:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=229 fs=4 fl=0 hz=0.0091324200913242, 32:ds=165 fs=2 fl=0 hz=0.005859375, 17:ds=99 fs=16 fl=3 hz=0.021252796420581654, 7:ds=78 fs=36 fl=0 hz=0.040178571428571425, 9:ds=61 fs=35 fl=1 hz=0.03854389721627409, 34:ds=59 fs=9 fl=2 hz=0.01649175412293853, 1:ds=52 fs=2 fl=5 hz=0.008130081300813009, 6:ds=51 fs=18 fl=3 hz=0.022850924918389557, 28:ds=45 fs=21 fl=2 hz=0.024390243902439025, 23:ds=44 fs=22 fl=3 hz=0.026399155227032733

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=59 flags=blue+purple
- S2: ds=51 flags=purple
- S9: ds=50 flags=red+purple
- S3: ds=49 flags=purple
- S20: ds=48 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 036: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 369: score=3 tags=FLT,RS
  - 378: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 567: score=3 tags=FLT,RS
  - 018: score=2 tags=RS
  - 027: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 099 -> combined:822(B); midday:772(B)
- 135 -> combined:729(B); evening:821(B)
- 144 -> combined:901(B); evening:764(B)
- 399 -> combined:675(B); evening:726(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:74(red); evening:37(blue); midday:45(blue)
- 04 -> combined:95(red); evening:72(red); midday:47(blue)
- 15 -> combined:27(purple); evening:37(blue)
- 19 -> combined:56(red); evening:28(purple); midday:48(blue)
- 22 -> combined:68(purple); evening:34(purple); midday:124(red)
- 23 -> combined:45(blue); evening:29(purple)
- 26 -> combined:32(purple); midday:31(purple)
- 33 -> combined:25(purple); evening:29(purple)
- 38 -> combined:31(purple); evening:48(blue)
- 39 -> combined:35(purple); evening:36(purple)
- 45 -> combined:61(red); evening:35(purple); midday:30(purple)
- 55 -> combined:54(purple); evening:27(purple); midday:33(purple)
- 59 -> combined:46(blue); midday:41(blue)
- 67 -> combined:30(purple); midday:57(red)
- 88 -> combined:50(purple); evening:25(purple); midday:74(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(3.0812999999999997)[R1,XVAR-Cons(CE)], 9(2.6055714285714284)[R3,XVAR-Cons(CM)], 1(2.5666642857142854)[R2,XVAR-Cons(CM)], 5(1.7149999999999999)[R1,Double-Pressure], 4(1.2478999999999998)[R2,Double-Pressure]
- P2: 6(5.808821428571429)[R1,XVAR-Cons(CEM)], 2(3.7738571428571426)[R2,XVAR-Cons(CM)], 0(2.696542857142857)[R3,XVAR-Cons(CM)], 5(1.5061428571428572)[R1,Double-Pressure], 3(0.9508)[R2,Double-Pressure]
- P3: 5(8.446414285714285)[R1,XVAR-Cons(CEM)], 8(6.136935714285714)[R2,Mirror-Echo], 3(3.4500714285714285)[R3,Mirror-Echo], 2(1.0761999999999998)[R2,Double-Pressure]
