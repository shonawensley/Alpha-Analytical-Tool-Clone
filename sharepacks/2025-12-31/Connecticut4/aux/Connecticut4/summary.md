# Aux Summary — Connecticut4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2025-12-31/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=467, 095, 055, 211, 279
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2025-12-31/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=095, 211, 042, 261, 177
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2025-12-31/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=467, 055, 279, 083, 435

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=29 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=32), P2:0 (gap=38), P3:0 (gap=29)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.10377142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.88445 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=46.258454285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=46.03913285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=45.03245571428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=44.813134285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=43.58472071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 920: score=43.36539928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 730: score=40.971960714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 930: score=40.75263928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 355: ds=999 sev=B
- 777: ds=881 sev=B
- 129: ds=863 sev=B
- 288: ds=851 sev=B
- 136: ds=838 sev=B
- 149: ds=833 sev=B
- 445: ds=765 sev=B
- 114: ds=735 sev=B
- 069: ds=699 sev=B
- 888: ds=697 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=83 sev=blue
  - 22: ds=71 sev=blue
  - 99: ds=64 sev=purple
  - 00: ds=34 sev=purple
  - 33: ds=21 sev=-
  - 88: ds=20 sev=-
  - 66: ds=19 sev=-
  - 77: ds=9 sev=-
  - 11: ds=3 sev=-
  - 55: ds=2 sev=-
- non_repeating:
  - 23: ds=84 sev=red
  - 69: ds=81 sev=red
  - 48: ds=70 sev=red
  - 78: ds=66 sev=red
  - 57: ds=65 sev=red
  - 49: ds=64 sev=red
  - 19: ds=58 sev=red
  - 13: ds=50 sev=blue
  - 01: ds=39 sev=blue
  - 25: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:399, 32:166, 25:152, 29:125, 4:123, 15:111, 31:100, 34:95, 3:80, 27:79

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=399 fs=1 fl=2 hz=0.01098901098901099, 32:ds=166 fs=5 fl=3 hz=0.010830324909747294, 25:ds=152 fs=22 fl=2 hz=0.029055690072639227, 29:ds=125 fs=25 fl=1 hz=0.029988465974625143, 4:ds=123 fs=22 fl=2 hz=0.0273972602739726, 15:ds=111 fs=11 fl=4 hz=0.016910935738444193, 31:ds=100 fs=32 fl=0 hz=0.03665521191294387, 34:ds=95 fs=15 fl=2 hz=0.01951779563719862, 3:ds=80 fs=27 fl=0 hz=0.030337078651685393, 27:ds=79 fs=19 fl=2 hz=0.025149700598802397

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=97 flags=purple
- S3: ds=74 flags=purple
- S24: ds=66 flags=blue+purple
- S22: ds=64 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=3 last_repeat_gap=71 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=30), P2:0 (gap=24), P3:8 (gap=29)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.10377142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.88445 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=46.258454285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=46.03913285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=45.03245571428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=44.813134285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=43.58472071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 920: score=43.36539928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 730: score=40.971960714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 930: score=40.75263928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=877 sev=B
- 478: ds=858 sev=B
- 459: ds=853 sev=B
- 159: ds=809 sev=B
- 099: ds=790 sev=B
- 127: ds=781 sev=B
- 559: ds=723 sev=B
- 004: ds=682 sev=B
- 155: ds=678 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=89 sev=blue
  - 88: ds=49 sev=purple
  - 44: ds=41 sev=purple
  - 22: ds=35 sev=purple
  - 55: ds=26 sev=purple
  - 00: ds=22 sev=-
  - 33: ds=10 sev=-
  - 66: ds=9 sev=-
  - 77: ds=4 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 23: ds=74 sev=red
  - 78: ds=67 sev=red
  - 13: ds=54 sev=blue
  - 49: ds=41 sev=blue
  - 19: ds=40 sev=blue
  - 69: ds=40 sev=blue
  - 48: ds=37 sev=blue
  - 57: ds=32 sev=purple
  - 79: ds=32 sev=purple
  - 37: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:199, 25:100, 31:89, 32:87, 18:84, 30:74, 3:72, 29:62, 4:61, 15:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=199 fs=3 fl=0 hz=0.008565310492505354, 25:ds=100 fs=21 fl=1 hz=0.025974025974025976, 31:ds=89 fs=20 fl=2 hz=0.024608501118568233, 32:ds=87 fs=3 fl=4 hz=0.009510869565217392, 18:ds=84 fs=23 fl=1 hz=0.026519337016574582, 30:ds=74 fs=35 fl=0 hz=0.03914988814317673, 3:ds=72 fs=22 fl=2 hz=0.02631578947368421, 29:ds=62 fs=18 fl=2 hz=0.023446658851113716, 4:ds=61 fs=26 fl=0 hz=0.02931228861330327, 15:ds=55 fs=24 fl=1 hz=0.02662406815761448

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=83 flags=blue+purple
- S24: ds=80 flags=blue+purple
- S8: ds=50 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 138: score=4 tags=FLT,MIR,RS
  - 237: score=4 tags=FLT,MIR,RS
  - 489: score=4 tags=FLT,MIR,RS
  - 039: score=3 tags=FLT,RS
  - 048: score=3 tags=FLT,RS
  - 057: score=3 tags=MIR,RS
  - 156: score=3 tags=MIR,RS
  - 345: score=3 tags=FLT,RS
  - 678: score=3 tags=FLT,RS
  - 012: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=8 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=16), P2:0 (gap=19), P3:1 (gap=20)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=52.10377142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.88445 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=46.258454285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=46.03913285714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=45.03245571428572 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=44.813134285714284 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 720: score=43.58472071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 920: score=43.36539928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 730: score=40.971960714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 930: score=40.75263928571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=904 sev=B
- 668: ds=901 sev=B
- 399: ds=900 sev=B
- 044: ds=896 sev=B
- 133: ds=893 sev=B
- 145: ds=865 sev=B
- 677: ds=772 sev=B
- 333: ds=767 sev=B
- 112: ds=719 sev=B
- 344: ds=699 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=111 sev=red
  - 22: ds=68 sev=purple
  - 99: ds=32 sev=purple
  - 77: ds=26 sev=purple
  - 66: ds=21 sev=-
  - 11: ds=20 sev=-
  - 33: ds=18 sev=-
  - 00: ds=17 sev=-
  - 88: ds=10 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 09: ds=63 sev=red
  - 57: ds=47 sev=blue
  - 69: ds=45 sev=blue
  - 23: ds=42 sev=blue
  - 25: ds=40 sev=blue
  - 06: ds=39 sev=blue
  - 07: ds=39 sev=blue
  - 01: ds=37 sev=blue
  - 48: ds=35 sev=purple
  - 78: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:310, 26:138, 4:121, 34:90, 32:83, 25:76, 29:64, 15:63, 2:53, 31:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=310 fs=2 fl=1 hz=0.005961251862891207, 26:ds=138 fs=3 fl=1 hz=0.008680555555555556, 4:ds=121 fs=18 fl=1 hz=0.02243211334120425, 34:ds=90 fs=14 fl=3 hz=0.019144144144144143, 32:ds=83 fs=2 fl=0 hz=0.008450704225352114, 25:ds=76 fs=21 fl=0 hz=0.023836549375709424, 29:ds=64 fs=27 fl=0 hz=0.030100334448160536, 15:ds=63 fs=15 fl=1 hz=0.019698725376593278, 2:ds=53 fs=23 fl=2 hz=0.028344671201814057, 31:ds=50 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=90 flags=blue+purple
- S8: ds=67 flags=red+purple
- S20: ds=50 flags=purple
- S3: ds=37 flags=blue+purple
- S24: ds=33 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 123: score=1 tags=FLT
  - 124: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:689(B); evening:893(B)
- 355 -> combined:999(B); evening:685(B)
- 445 -> combined:765(B); evening:688(B)
- 459 -> combined:674(B); midday:853(B)
- 888 -> combined:697(B); evening:696(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:39(blue); evening:37(blue)
- 06 -> combined:31(purple); evening:39(blue)
- 07 -> combined:31(purple); evening:39(blue)
- 13 -> combined:50(blue); evening:25(purple); midday:54(blue)
- 19 -> combined:58(red); evening:29(purple); midday:40(blue)
- 22 -> combined:71(blue); evening:68(purple); midday:35(purple)
- 23 -> combined:84(red); evening:42(blue); midday:74(red)
- 25 -> combined:33(purple); evening:40(blue)
- 44 -> combined:83(blue); evening:111(red); midday:41(purple)
- 48 -> combined:70(red); evening:35(purple); midday:37(blue)
- 49 -> combined:64(red); evening:32(purple); midday:41(blue)
- 57 -> combined:65(red); evening:47(blue); midday:32(purple)
- 69 -> combined:81(red); evening:45(blue); midday:40(blue)
- 78 -> combined:66(red); evening:33(purple); midday:67(red)
- 99 -> combined:64(purple); evening:32(purple); midday:89(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(7.895028571428571)[R1,XVAR-Cons(CEM)], 9(7.704314285714286)[R2,XVAR-Cons(CEM)], 3(1.9716642857142859)[R3,XVAR-Cons(CE)], 5(0.2849714285714286)[R3,Swap]
- P2: 0(8.383857142857142)[R1,XVAR-Cons(CEM)], 2(3.1498999999999997)[R2,XVAR-Cons(CM)], 3(1.7475)[R3,XVAR-Cons(CM)], 9(0.9717)[R2,Double-Pressure], 1(0.16122857142857144)[R3]
- P3: 0(6.8548285714285715)[R1,XVAR-Cons(CEM)], 8(3.945857142857143)[R2,XVAR-Cons(CM)], 4(2.8797714285714284)[R3,XVAR-Cons(CM)], 1(0.5971428571428571)[R1], 2(0.24779285714285712)[R3,Swap]
