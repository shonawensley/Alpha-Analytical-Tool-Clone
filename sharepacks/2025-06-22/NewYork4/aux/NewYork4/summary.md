# Aux Summary — NewYork4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/NewYork4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: New York
- combined: live=`data/cleaned/draws/New_York_draws.csv` snap=`sharepacks/2025-06-22/NewYork4/aux/draws/New_York_draws.csv` n=1000 head=602, 802, 308, 573, 520
- midday: live=`data/cleaned/draws/New_York_Midday_draws.csv` snap=`sharepacks/2025-06-22/NewYork4/aux/draws/New_York_Midday_draws.csv` n=1000 head=802, 573, 255, 878, 211
- evening: live=`data/cleaned/draws/New_York_Evening_draws.csv` snap=`sharepacks/2025-06-22/NewYork4/aux/draws/New_York_Evening_draws.csv` n=1000 head=602, 308, 520, 610, 680

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=5 last_repeat_index=3

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=36), P2:4 (gap=20), P3:7 (gap=31)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 447: score=48.25461428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 497: score=42.79048571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 047: score=40.61815714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 446: score=40.224964285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=39.349871428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 449: score=38.558 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 457: score=37.675399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 437: score=37.48597142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 477: score=37.37398571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 467: score=37.326685714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 189: ds=722 sev=B
- 014: ds=717 sev=B
- 228: ds=702 sev=B
- 477: ds=692 sev=B
- 113: ds=685 sev=B
- 888: ds=675 sev=B
- 999: ds=667 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=70 sev=purple
  - 44: ds=53 sev=purple
  - 77: ds=40 sev=purple
  - 33: ds=32 sev=purple
  - 99: ds=28 sev=purple
  - 66: ds=19 sev=-
  - 00: ds=17 sev=-
  - 11: ds=9 sev=-
  - 88: ds=7 sev=-
  - 55: ds=5 sev=-
- non_repeating:
  - 56: ds=95 sev=red
  - 18: ds=67 sev=red
  - 15: ds=41 sev=blue
  - 45: ds=41 sev=blue
  - 39: ds=39 sev=blue
  - 24: ds=37 sev=blue
  - 59: ds=35 sev=purple
  - 17: ds=34 sev=purple
  - 04: ds=33 sev=purple
  - 07: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:162, 32:114, 16:82, 23:67, 5:61, 10:60, 4:58, 20:57, 19:56, 33:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=162 fs=4 fl=1 hz=0.008086253369272238, 32:ds=114 fs=3 fl=3 hz=0.007972665148063782, 16:ds=82 fs=3 fl=1 hz=0.005868544600938967, 23:ds=67 fs=19 fl=2 hz=0.02354260089686099, 5:ds=61 fs=22 fl=1 hz=0.02505446623093682, 10:ds=60 fs=28 fl=1 hz=0.03269447576099211, 4:ds=58 fs=24 fl=0 hz=0.030808729139922976, 20:ds=57 fs=19 fl=1 hz=0.02450980392156863, 19:ds=56 fs=19 fl=0 hz=0.024906600249066005, 33:ds=55 fs=23 fl=2 hz=0.02682403433476395

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=90 flags=purple
- S22: ds=80 flags=purple
- S24: ds=77 flags=purple
- S6: ds=46 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 126: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 189: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 279: score=3 tags=FLT,RS
  - 369: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 468: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=2 max=2 last_repeat_gap=1 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=33), P2:3 (gap=19), P3:7 (gap=15)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 447: score=48.25461428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 497: score=42.79048571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 047: score=40.61815714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 446: score=40.224964285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=39.349871428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 449: score=38.558 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 457: score=37.675399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 437: score=37.48597142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 477: score=37.37398571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 467: score=37.326685714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 477: ds=981 sev=B
- 666: ds=959 sev=B
- 066: ds=957 sev=B
- 444: ds=923 sev=B
- 166: ds=876 sev=B
- 344: ds=826 sev=B
- 001: ds=802 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=100 sev=blue
  - 22: ds=96 sev=blue
  - 99: ds=83 sev=blue
  - 44: ds=26 sev=purple
  - 33: ds=24 sev=-
  - 66: ds=9 sev=-
  - 00: ds=8 sev=-
  - 11: ds=4 sev=-
  - 88: ds=3 sev=-
  - 55: ds=2 sev=-
- non_repeating:
  - 16: ds=59 sev=red
  - 06: ds=52 sev=blue
  - 56: ds=47 sev=blue
  - 13: ds=42 sev=blue
  - 03: ds=39 sev=blue
  - 18: ds=33 sev=purple
  - 17: ds=31 sev=purple
  - 07: ds=29 sev=purple
  - 27: ds=28 sev=purple
  - 38: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:414, 35:174, 26:146, 27:127, 10:100, 6:97, 28:94, 4:90, 19:72, 16:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=414 fs=0 fl=0 hz=0.0, 35:ds=174 fs=3 fl=2 hz=0.008075370121130552, 26:ds=146 fs=1 fl=0 hz=0.0038809831824062092, 27:ds=127 fs=19 fl=2 hz=0.02573529411764706, 10:ds=100 fs=24 fl=1 hz=0.029137529137529136, 6:ds=97 fs=18 fl=2 hz=0.022779043280182234, 28:ds=94 fs=17 fl=2 hz=0.021420518602029315, 4:ds=90 fs=30 fl=0 hz=0.037267080745341616, 19:ds=72 fs=25 fl=1 hz=0.030373831775700938, 16:ds=69 fs=4 fl=0 hz=0.006195786864931846

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=57 flags=blue+purple
- S22: ds=51 flags=purple
- S14: ds=48 flags=red+purple
- S6: ds=46 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '6', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 045: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=13 last_repeat_index=8

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=27), P2:5 (gap=23), P3:7 (gap=25)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 447: score=48.25461428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 497: score=42.79048571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 047: score=40.61815714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 446: score=40.224964285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=39.349871428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 449: score=38.558 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 457: score=37.675399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 437: score=37.48597142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 477: score=37.37398571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 467: score=37.326685714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 169: ds=975 sev=B
- 355: ds=930 sev=B
- 358: ds=925 sev=B
- 666: ds=893 sev=B
- 011: ds=857 sev=B
- 566: ds=781 sev=B
- 446: ds=780 sev=B
- 113: ds=760 sev=B
- 039: ds=671 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=81 sev=blue
  - 00: ds=60 sev=purple
  - 11: ds=41 sev=purple
  - 22: ds=35 sev=purple
  - 66: ds=28 sev=purple
  - 55: ds=26 sev=purple
  - 88: ds=22 sev=-
  - 77: ds=20 sev=-
  - 33: ds=16 sev=-
  - 99: ds=14 sev=-
- non_repeating:
  - 18: ds=63 sev=red
  - 45: ds=51 sev=blue
  - 56: ds=49 sev=blue
  - 89: ds=48 sev=blue
  - 59: ds=42 sev=blue
  - 39: ds=33 sev=purple
  - 04: ds=32 sev=purple
  - 58: ds=29 sev=purple
  - 69: ds=28 sev=purple
  - 48: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 15:163, 20:125, 14:123, 29:91, 35:81, 18:61, 32:57, 33:53, 34:48, 5:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 15:ds=163 fs=29 fl=0 hz=0.037613488975356685, 20:ds=125 fs=18 fl=1 hz=0.0247074122236671, 14:ds=123 fs=40 fl=0 hz=0.04581901489117984, 29:ds=91 fs=22 fl=0 hz=0.02756892230576441, 35:ds=81 fs=5 fl=3 hz=0.010238907849829351, 18:ds=61 fs=16 fl=1 hz=0.019522776572668113, 32:ds=57 fs=6 fl=1 hz=0.009944751381215469, 33:ds=53 fs=15 fl=4 hz=0.020364415862808145, 34:ds=48 fs=19 fl=0 hz=0.022988505747126436, 5:ds=42 fs=29 fl=0 hz=0.03068783068783069

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=71 flags=purple
- S5: ds=65 flags=purple
- S3: ds=45 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['4', '7', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 124: score=2 tags=FLT,PAT
  - 134: score=2 tags=FLT,PAT
  - 234: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT
  - 569: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT
  - 579: score=2 tags=FLT,PAT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 113 -> combined:685(B); evening:760(B)
- 477 -> combined:692(B); midday:981(B)
- 666 -> evening:893(B); midday:959(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 04 -> combined:33(purple); evening:32(purple)
- 07 -> combined:30(purple); midday:29(purple)
- 17 -> combined:34(purple); midday:31(purple)
- 18 -> combined:67(red); evening:63(red); midday:33(purple)
- 22 -> combined:70(purple); evening:35(purple); midday:96(blue)
- 39 -> combined:39(blue); evening:33(purple)
- 44 -> combined:53(purple); evening:81(blue); midday:26(purple)
- 45 -> combined:41(blue); evening:51(blue)
- 56 -> combined:95(red); evening:49(blue); midday:47(blue)
- 59 -> combined:35(purple); evening:42(blue)
- 77 -> combined:40(purple); midday:100(blue)
- 99 -> combined:28(purple); midday:83(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(6.750114285714286)[R1,XVAR-Cons(CEM)], 0(2.613657142857143)[R3,XVAR-Cons(CE)], 1(1.6552857142857142)[R1,Double-Pressure], 9(1.6160714285714286)[R1,Mirror-Echo], 3(1.1016)[R2,Double-Pressure]
- P2: 4(5.935928571428572)[R1,Mirror-Echo], 9(2.9718)[R3,Mirror-Echo], 5(1.3567142857142855)[R1,Double-Pressure], 3(1.1672857142857143)[R1,Double-Pressure], 7(1.0553)[R2,Double-Pressure]
- P3: 7(8.068571428571428)[R1,XVAR-Cons(CEM)], 6(2.5389214285714283)[R2,XVAR-Cons(CM)], 9(1.871957142857143)[R3,XVAR-Cons(CE)], 0(0.9208)[R2,Double-Pressure], 5(0.9135)[R2,Double-Pressure]
