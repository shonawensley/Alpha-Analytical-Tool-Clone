# Aux Summary — Connecticut4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-01/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=361, 932, 467, 095, 055
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-01/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=932, 095, 211, 042, 261
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-01/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=361, 467, 055, 279, 083

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=2 last_repeat_gap=31 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=34), P2:0 (gap=40), P3:0 (gap=31)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.85780178571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R3 src=lane
- 708: score=52.644197500000004 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 704: score=45.545865 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=44.34471464285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 728: score=44.13111035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 500: score=43.90516821428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 508: score=43.691563928571426 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 780: score=41.6264175 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 788: score=41.41281321428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 702: score=38.12694285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=883 sev=B
- 129: ds=865 sev=B
- 288: ds=853 sev=B
- 149: ds=835 sev=B
- 445: ds=767 sev=B
- 114: ds=737 sev=B
- 069: ds=701 sev=B
- 888: ds=699 sev=B
- 688: ds=695 sev=B
- 133: ds=691 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=85 sev=blue
  - 22: ds=73 sev=blue
  - 99: ds=66 sev=purple
  - 00: ds=36 sev=purple
  - 33: ds=23 sev=-
  - 88: ds=22 sev=-
  - 66: ds=21 sev=-
  - 77: ds=11 sev=-
  - 11: ds=5 sev=-
  - 55: ds=4 sev=-
- non_repeating:
  - 69: ds=83 sev=red
  - 48: ds=72 sev=red
  - 78: ds=68 sev=red
  - 57: ds=67 sev=red
  - 49: ds=66 sev=red
  - 19: ds=60 sev=red
  - 01: ds=41 sev=blue
  - 25: ds=35 sev=purple
  - 06: ds=33 sev=purple
  - 07: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:401, 32:168, 25:154, 29:127, 4:125, 15:113, 31:102, 34:97, 3:82, 27:81

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=401 fs=1 fl=2 hz=0.01098901098901099, 32:ds=168 fs=5 fl=3 hz=0.010830324909747294, 25:ds=154 fs=22 fl=2 hz=0.029055690072639227, 29:ds=127 fs=25 fl=1 hz=0.029988465974625143, 4:ds=125 fs=21 fl=2 hz=0.027677496991576414, 15:ds=113 fs=10 fl=4 hz=0.01583710407239819, 31:ds=102 fs=32 fl=0 hz=0.03665521191294387, 34:ds=97 fs=15 fl=2 hz=0.01951779563719862, 3:ds=82 fs=27 fl=0 hz=0.030337078651685393, 27:ds=81 fs=19 fl=2 hz=0.025149700598802397

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=99 flags=purple
- S3: ds=76 flags=purple
- S24: ds=68 flags=blue+purple
- S22: ds=66 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 168: score=2 tags=FLT,MIR
  - 238: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 348: score=2 tags=FLT,MIR
  - 358: score=2 tags=FLT,MIR
  - 368: score=2 tags=FLT,MIR
  - 378: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=72 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=25), P2:0 (gap=25), P3:8 (gap=30)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.85780178571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R3 src=lane
- 708: score=52.644197500000004 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 704: score=45.545865 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=44.34471464285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 728: score=44.13111035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 500: score=43.90516821428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 508: score=43.691563928571426 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 780: score=41.6264175 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 788: score=41.41281321428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 702: score=38.12694285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=878 sev=B
- 478: ds=859 sev=B
- 459: ds=854 sev=B
- 159: ds=810 sev=B
- 099: ds=791 sev=B
- 127: ds=782 sev=B
- 559: ds=724 sev=B
- 004: ds=683 sev=B
- 155: ds=679 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=90 sev=blue
  - 88: ds=50 sev=purple
  - 44: ds=42 sev=purple
  - 22: ds=36 sev=purple
  - 55: ds=27 sev=purple
  - 00: ds=23 sev=-
  - 33: ds=11 sev=-
  - 66: ds=10 sev=-
  - 77: ds=5 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 78: ds=68 sev=red
  - 13: ds=55 sev=blue
  - 49: ds=42 sev=blue
  - 19: ds=41 sev=blue
  - 69: ds=41 sev=blue
  - 48: ds=38 sev=blue
  - 57: ds=33 sev=purple
  - 79: ds=33 sev=purple
  - 37: ds=22 sev=-
  - 01: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:200, 25:101, 31:90, 32:88, 18:85, 3:73, 29:63, 4:62, 15:56, 34:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=200 fs=3 fl=0 hz=0.008565310492505354, 25:ds=101 fs=21 fl=1 hz=0.025974025974025976, 31:ds=90 fs=20 fl=2 hz=0.024608501118568233, 32:ds=88 fs=3 fl=4 hz=0.009510869565217392, 18:ds=85 fs=23 fl=1 hz=0.026519337016574582, 3:ds=73 fs=22 fl=2 hz=0.02631578947368421, 29:ds=63 fs=18 fl=2 hz=0.023446658851113716, 4:ds=62 fs=26 fl=0 hz=0.02931228861330327, 15:ds=56 fs=24 fl=1 hz=0.02662406815761448, 34:ds=48 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=84 flags=blue+purple
- S24: ds=81 flags=blue+purple
- S8: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 048: score=3 tags=FLT,RS
  - 057: score=3 tags=FLT,RS
  - 138: score=3 tags=FLT,RS
  - 147: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 489: score=3 tags=FLT,RS
  - 579: score=3 tags=FLT,RS
  - 678: score=3 tags=FLT,RS
  - 012: score=2 tags=RS
  - 039: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=9 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=17), P2:0 (gap=20), P3:0 (gap=18)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.85780178571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R3 src=lane
- 708: score=52.644197500000004 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 704: score=45.545865 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=44.34471464285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 728: score=44.13111035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 500: score=43.90516821428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 508: score=43.691563928571426 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 780: score=41.6264175 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 788: score=41.41281321428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 702: score=38.12694285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=905 sev=B
- 668: ds=902 sev=B
- 399: ds=901 sev=B
- 044: ds=897 sev=B
- 133: ds=894 sev=B
- 145: ds=866 sev=B
- 677: ds=773 sev=B
- 333: ds=768 sev=B
- 112: ds=720 sev=B
- 344: ds=700 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=112 sev=red
  - 22: ds=69 sev=purple
  - 99: ds=33 sev=purple
  - 77: ds=27 sev=purple
  - 66: ds=22 sev=-
  - 11: ds=21 sev=-
  - 33: ds=19 sev=-
  - 00: ds=18 sev=-
  - 88: ds=11 sev=-
  - 55: ds=2 sev=-
- non_repeating:
  - 09: ds=64 sev=red
  - 57: ds=48 sev=blue
  - 69: ds=46 sev=blue
  - 23: ds=43 sev=blue
  - 25: ds=41 sev=blue
  - 06: ds=40 sev=blue
  - 07: ds=40 sev=blue
  - 01: ds=38 sev=blue
  - 48: ds=36 sev=purple
  - 78: ds=34 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:311, 26:139, 4:122, 34:91, 32:84, 25:77, 29:65, 15:64, 2:54, 31:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=311 fs=2 fl=1 hz=0.005961251862891207, 26:ds=139 fs=3 fl=1 hz=0.008680555555555556, 4:ds=122 fs=18 fl=1 hz=0.02243211334120425, 34:ds=91 fs=14 fl=3 hz=0.019144144144144143, 32:ds=84 fs=2 fl=0 hz=0.008450704225352114, 25:ds=77 fs=21 fl=0 hz=0.023836549375709424, 29:ds=65 fs=27 fl=0 hz=0.030100334448160536, 15:ds=64 fs=15 fl=1 hz=0.019698725376593278, 2:ds=54 fs=23 fl=2 hz=0.028344671201814057, 31:ds=51 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=91 flags=blue+purple
- S8: ds=68 flags=red+purple
- S20: ds=51 flags=purple
- S3: ds=38 flags=blue+purple
- S24: ds=34 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=MIR
  - 016: score=1 tags=MIR
  - 025: score=1 tags=MIR
  - 027: score=1 tags=MIR
  - 035: score=1 tags=MIR
  - 038: score=1 tags=MIR
  - 045: score=1 tags=MIR
  - 049: score=1 tags=MIR
  - 056: score=1 tags=MIR
  - 057: score=1 tags=MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:691(B); evening:894(B)
- 445 -> combined:767(B); evening:689(B)
- 459 -> combined:676(B); midday:854(B)
- 888 -> combined:699(B); evening:697(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:41(blue); evening:38(blue)
- 06 -> combined:33(purple); evening:40(blue)
- 07 -> combined:33(purple); evening:40(blue)
- 19 -> combined:60(red); evening:30(purple); midday:41(blue)
- 22 -> combined:73(blue); evening:69(purple); midday:36(purple)
- 25 -> combined:35(purple); evening:41(blue)
- 44 -> combined:85(blue); evening:112(red); midday:42(purple)
- 48 -> combined:72(red); evening:36(purple); midday:38(blue)
- 49 -> combined:66(red); evening:33(purple); midday:42(blue)
- 57 -> combined:67(red); evening:48(blue); midday:33(purple)
- 69 -> combined:83(red); evening:46(blue); midday:41(blue)
- 78 -> combined:68(red); evening:34(purple); midday:68(red)
- 99 -> combined:66(purple); evening:33(purple); midday:90(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.232571428571429)[R1,XVAR-Cons(CEM)], 5(2.621585714285714)[R3,XVAR-Cons(CM)], 9(0.9135)[R2,Double-Pressure], 6(0.44399999999999995)[R2,Swap], 3(0.21779285714285712)[R3,Swap]
- P2: 0(8.443571428571428)[R1,XVAR-Cons(CEM)], 2(3.2148000000000003)[R2,XVAR-Cons(CM)], 8(1.7206285714285716)[R3,XVAR-Cons(CM)], 9(0.9625999999999999)[R2,Double-Pressure], 1(0.24466428571428572)[R3,Swap]
- P3: 0(7.11325)[R1,XVAR-Cons(CEM)], 8(6.927507142857143)[R2,XVAR-Cons(CEM)], 4(2.9289571428571426)[R3,XVAR-Cons(CM)], 2(0.9508)[R2,Double-Pressure]
