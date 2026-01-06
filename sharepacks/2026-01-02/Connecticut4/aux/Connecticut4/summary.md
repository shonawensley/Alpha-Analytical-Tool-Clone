# Aux Summary — Connecticut4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-02/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=109, 228, 361, 932, 467
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-02/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=228, 932, 095, 211, 042
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-02/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=109, 361, 467, 055, 279

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=2 last_repeat_gap=33 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=36), P2:8 (gap=10), P3:0 (gap=33)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 740: score=45.65309535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 780: score=45.25816785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 784: score=39.519465 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 700: score=39.177685714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=38.87979285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 744: score=37.64295 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 710: score=37.61514285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 750: score=37.21288571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 540: score=34.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 580: score=34.17198571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=885 sev=B
- 129: ds=867 sev=B
- 288: ds=855 sev=B
- 149: ds=837 sev=B
- 445: ds=769 sev=B
- 114: ds=739 sev=B
- 069: ds=703 sev=B
- 888: ds=701 sev=B
- 688: ds=697 sev=B
- 133: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=87 sev=blue
  - 99: ds=68 sev=purple
  - 00: ds=38 sev=purple
  - 33: ds=25 sev=purple
  - 88: ds=24 sev=-
  - 66: ds=23 sev=-
  - 77: ds=13 sev=-
  - 11: ds=7 sev=-
  - 55: ds=6 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 69: ds=85 sev=red
  - 48: ds=74 sev=red
  - 78: ds=70 sev=red
  - 57: ds=69 sev=red
  - 49: ds=68 sev=red
  - 25: ds=37 sev=blue
  - 06: ds=35 sev=purple
  - 07: ds=35 sev=purple
  - 37: ds=30 sev=purple
  - 18: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:403, 32:170, 25:156, 29:129, 4:127, 15:115, 31:104, 34:99, 3:84, 35:68

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=403 fs=1 fl=2 hz=0.01098901098901099, 32:ds=170 fs=5 fl=2 hz=0.011267605633802818, 25:ds=156 fs=22 fl=2 hz=0.029055690072639227, 29:ds=129 fs=25 fl=1 hz=0.029988465974625143, 4:ds=127 fs=21 fl=2 hz=0.027677496991576414, 15:ds=115 fs=10 fl=4 hz=0.01583710407239819, 31:ds=104 fs=32 fl=0 hz=0.03665521191294387, 34:ds=99 fs=15 fl=2 hz=0.01951779563719862, 3:ds=84 fs=27 fl=0 hz=0.030337078651685393, 35:ds=68 fs=13 fl=4 hz=0.018743109151047408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=78 flags=purple
- S24: ds=70 flags=blue+purple
- S22: ds=68 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT
  - 125: score=1 tags=FLT
  - 135: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=3 last_repeat_gap=73 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=26), P2:0 (gap=26), P3:4 (gap=30)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 740: score=45.65309535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 780: score=45.25816785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 784: score=39.519465 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 700: score=39.177685714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=38.87979285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 744: score=37.64295 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 710: score=37.61514285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 750: score=37.21288571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 540: score=34.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 580: score=34.17198571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=879 sev=B
- 478: ds=860 sev=B
- 459: ds=855 sev=B
- 159: ds=811 sev=B
- 099: ds=792 sev=B
- 127: ds=783 sev=B
- 559: ds=725 sev=B
- 004: ds=684 sev=B
- 155: ds=680 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=91 sev=blue
  - 88: ds=51 sev=purple
  - 44: ds=43 sev=purple
  - 55: ds=28 sev=purple
  - 00: ds=24 sev=-
  - 33: ds=12 sev=-
  - 66: ds=11 sev=-
  - 77: ds=6 sev=-
  - 11: ds=3 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 78: ds=69 sev=red
  - 13: ds=56 sev=red
  - 49: ds=43 sev=blue
  - 19: ds=42 sev=blue
  - 69: ds=42 sev=blue
  - 48: ds=39 sev=blue
  - 57: ds=34 sev=purple
  - 79: ds=34 sev=purple
  - 37: ds=23 sev=-
  - 01: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:201, 25:102, 31:91, 32:89, 18:86, 3:74, 29:64, 4:63, 15:57, 34:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=201 fs=3 fl=0 hz=0.008565310492505354, 25:ds=102 fs=21 fl=1 hz=0.025974025974025976, 31:ds=91 fs=20 fl=2 hz=0.024608501118568233, 32:ds=89 fs=3 fl=4 hz=0.009510869565217392, 18:ds=86 fs=23 fl=1 hz=0.026519337016574582, 3:ds=74 fs=22 fl=2 hz=0.02631578947368421, 29:ds=64 fs=18 fl=2 hz=0.023446658851113716, 4:ds=63 fs=26 fl=0 hz=0.02931228861330327, 15:ds=57 fs=24 fl=1 hz=0.02662406815761448, 34:ds=49 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=85 flags=blue+purple
- S24: ds=82 flags=blue+purple
- S8: ds=52 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=10 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=18), P2:9 (gap=15), P3:0 (gap=19)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 740: score=45.65309535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 780: score=45.25816785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 784: score=39.519465 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 700: score=39.177685714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=38.87979285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 744: score=37.64295 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 710: score=37.61514285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 750: score=37.21288571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 540: score=34.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 580: score=34.17198571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=906 sev=B
- 668: ds=903 sev=B
- 399: ds=902 sev=B
- 044: ds=898 sev=B
- 133: ds=895 sev=B
- 145: ds=867 sev=B
- 677: ds=774 sev=B
- 333: ds=769 sev=B
- 112: ds=721 sev=B
- 344: ds=701 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=113 sev=red
  - 22: ds=70 sev=purple
  - 99: ds=34 sev=purple
  - 77: ds=28 sev=purple
  - 66: ds=23 sev=-
  - 11: ds=22 sev=-
  - 33: ds=20 sev=-
  - 00: ds=19 sev=-
  - 88: ds=12 sev=-
  - 55: ds=3 sev=-
- non_repeating:
  - 57: ds=49 sev=blue
  - 69: ds=47 sev=blue
  - 23: ds=44 sev=blue
  - 25: ds=42 sev=blue
  - 06: ds=41 sev=blue
  - 07: ds=41 sev=blue
  - 48: ds=37 sev=blue
  - 78: ds=35 sev=purple
  - 49: ds=34 sev=purple
  - 15: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:312, 26:140, 4:123, 34:92, 32:85, 25:78, 29:66, 15:65, 2:55, 31:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=312 fs=2 fl=1 hz=0.005961251862891207, 26:ds=140 fs=3 fl=1 hz=0.008680555555555556, 4:ds=123 fs=18 fl=1 hz=0.02243211334120425, 34:ds=92 fs=14 fl=3 hz=0.019144144144144143, 32:ds=85 fs=2 fl=0 hz=0.008450704225352114, 25:ds=78 fs=21 fl=0 hz=0.023836549375709424, 29:ds=66 fs=27 fl=0 hz=0.030100334448160536, 15:ds=65 fs=15 fl=1 hz=0.019698725376593278, 2:ds=55 fs=23 fl=2 hz=0.028344671201814057, 31:ds=52 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=92 flags=blue+purple
- S8: ds=69 flags=red+purple
- S20: ds=52 flags=purple
- S3: ds=39 flags=blue+purple
- S24: ds=35 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 068: score=1 tags=FLT
  - 078: score=1 tags=FLT
  - 089: score=1 tags=FLT
  - 128: score=1 tags=FLT
  - 138: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:693(B); evening:895(B)
- 445 -> combined:769(B); evening:690(B)
- 459 -> combined:678(B); midday:855(B)
- 888 -> combined:701(B); evening:698(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 06 -> combined:35(purple); evening:41(blue)
- 07 -> combined:35(purple); evening:41(blue)
- 25 -> combined:37(blue); evening:42(blue)
- 44 -> combined:87(blue); evening:113(red); midday:43(purple)
- 48 -> combined:74(red); evening:37(blue); midday:39(blue)
- 49 -> combined:68(red); evening:34(purple); midday:43(blue)
- 57 -> combined:69(red); evening:49(blue); midday:34(purple)
- 69 -> combined:85(red); evening:47(blue); midday:42(blue)
- 78 -> combined:70(red); evening:35(purple); midday:69(red)
- 99 -> combined:68(purple); evening:34(purple); midday:91(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.313714285714287)[R1,XVAR-Cons(CEM)], 5(2.6307714285714283)[R3,XVAR-Cons(CM)], 6(2.535792857142857)[R2,XVAR-Cons(CE)], 9(1.0044)[R2,Double-Pressure], 3(0.23122857142857145)[R3,Swap]
- P2: 8(3.2023857142857146)[R1,XVAR-Cons(CM)], 4(2.6762357142857143)[R2,XVAR-Cons(CE)], 0(1.5251428571428571)[R1,Mirror-Echo], 9(1.22725)[R1,Mirror-Echo], 1(0.9625999999999999)[R2,Double-Pressure]
- P3: 0(7.8388285714285715)[R1,XVAR-Cons(CEM)], 4(4.153)[R2,XVAR-Cons(CM)], 2(0.9417)[R2,Double-Pressure], 9(0.6683714285714285)[R3,Mirror-Echo], 6(0.29628571428571426)[R3,Swap]
