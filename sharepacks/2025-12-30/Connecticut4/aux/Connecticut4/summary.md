# Aux Summary — Connecticut4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2025-12-30/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=055, 211, 279, 042, 083
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2025-12-30/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=211, 042, 261, 177, 893
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2025-12-30/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=055, 279, 083, 435, 829

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=1 streak=1 max=2 last_repeat_gap=27 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=30), P2:0 (gap=36), P3:0 (gap=27)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=51.792671785714276 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.71003607142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=45.89369071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=45.811054999999996 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=44.77656428571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 790: score=42.54802035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 720: score=42.436371785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=41.864285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 990: score=39.92642142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 920: score=39.82933571428572 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 355: ds=997 sev=B
- 777: ds=879 sev=B
- 129: ds=861 sev=B
- 288: ds=849 sev=B
- 136: ds=836 sev=B
- 149: ds=831 sev=B
- 445: ds=763 sev=B
- 114: ds=733 sev=B
- 069: ds=697 sev=B
- 888: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=81 sev=blue
  - 22: ds=69 sev=purple
  - 99: ds=62 sev=purple
  - 00: ds=32 sev=purple
  - 33: ds=19 sev=-
  - 88: ds=18 sev=-
  - 66: ds=17 sev=-
  - 77: ds=7 sev=-
  - 11: ds=1 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 23: ds=82 sev=red
  - 69: ds=79 sev=red
  - 48: ds=68 sev=red
  - 78: ds=64 sev=red
  - 57: ds=63 sev=red
  - 49: ds=62 sev=red
  - 09: ds=59 sev=red
  - 19: ds=56 sev=red
  - 13: ds=48 sev=blue
  - 01: ds=37 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:397, 32:164, 25:150, 29:123, 4:121, 15:109, 31:98, 34:93, 3:78, 27:77

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=397 fs=1 fl=2 hz=0.01098901098901099, 32:ds=164 fs=5 fl=3 hz=0.010830324909747294, 25:ds=150 fs=22 fl=2 hz=0.029055690072639227, 29:ds=123 fs=25 fl=1 hz=0.029988465974625143, 4:ds=121 fs=22 fl=2 hz=0.0273972602739726, 15:ds=109 fs=11 fl=4 hz=0.016910935738444193, 31:ds=98 fs=32 fl=0 hz=0.03665521191294387, 34:ds=93 fs=15 fl=2 hz=0.01951779563719862, 3:ds=78 fs=27 fl=0 hz=0.030337078651685393, 27:ds=77 fs=19 fl=2 hz=0.025149700598802397

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=99 flags=red+purple
- S23: ds=95 flags=purple
- S3: ds=72 flags=purple
- S24: ds=64 flags=blue+purple
- S22: ds=62 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 167: score=4 tags=FLT,MIR,RS
  - 059: score=3 tags=MIR,RS
  - 068: score=3 tags=FLT,RS
  - 149: score=3 tags=MIR,RS
  - 257: score=3 tags=MIR,RS
  - 356: score=3 tags=FLT,RS
  - 689: score=3 tags=FLT,RS
  - 014: score=2 tags=RS
  - 016: score=2 tags=FLT,MIR
  - 023: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=3 last_repeat_gap=70 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=29), P2:0 (gap=23), P3:8 (gap=28)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=51.792671785714276 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.71003607142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=45.89369071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=45.811054999999996 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=44.77656428571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 790: score=42.54802035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 720: score=42.436371785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=41.864285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 990: score=39.92642142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 920: score=39.82933571428572 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=876 sev=B
- 478: ds=857 sev=B
- 459: ds=852 sev=B
- 159: ds=808 sev=B
- 099: ds=789 sev=B
- 127: ds=780 sev=B
- 559: ds=722 sev=B
- 004: ds=681 sev=B
- 155: ds=677 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=88 sev=blue
  - 88: ds=48 sev=purple
  - 44: ds=40 sev=purple
  - 22: ds=34 sev=purple
  - 55: ds=25 sev=purple
  - 00: ds=21 sev=-
  - 33: ds=9 sev=-
  - 66: ds=8 sev=-
  - 77: ds=3 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 23: ds=73 sev=red
  - 78: ds=66 sev=red
  - 13: ds=53 sev=blue
  - 49: ds=40 sev=blue
  - 19: ds=39 sev=blue
  - 69: ds=39 sev=blue
  - 48: ds=36 sev=purple
  - 57: ds=31 sev=purple
  - 79: ds=31 sev=purple
  - 09: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:198, 25:99, 31:88, 32:86, 18:83, 30:73, 3:71, 29:61, 4:60, 15:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=198 fs=3 fl=0 hz=0.008565310492505354, 25:ds=99 fs=21 fl=1 hz=0.025974025974025976, 31:ds=88 fs=21 fl=2 hz=0.025246981339187704, 32:ds=86 fs=3 fl=4 hz=0.009510869565217392, 18:ds=83 fs=23 fl=1 hz=0.026519337016574582, 30:ds=73 fs=35 fl=0 hz=0.03914988814317673, 3:ds=71 fs=22 fl=2 hz=0.02631578947368421, 29:ds=61 fs=18 fl=2 hz=0.023446658851113716, 4:ds=60 fs=26 fl=0 hz=0.02931228861330327, 15:ds=54 fs=24 fl=1 hz=0.02662406815761448

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=82 flags=blue+purple
- S24: ds=79 flags=blue+purple
- S8: ds=49 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 057: score=3 tags=FLT,RS
  - 156: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 579: score=3 tags=FLT,RS
  - 012: score=2 tags=RS
  - 039: score=2 tags=RS
  - 048: score=2 tags=RS
  - 129: score=2 tags=RS
  - 138: score=2 tags=RS
  - 147: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=1 streak=1 max=3 last_repeat_gap=7 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=15), P2:0 (gap=18), P3:1 (gap=19)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 700: score=51.792671785714276 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 900: score=51.71003607142857 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 708: score=45.89369071428571 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 908: score=45.811054999999996 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 704: score=44.77656428571429 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 790: score=42.54802035714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 720: score=42.436371785714286 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 904: score=41.864285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 990: score=39.92642142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 920: score=39.82933571428572 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=903 sev=B
- 668: ds=900 sev=B
- 399: ds=899 sev=B
- 044: ds=895 sev=B
- 133: ds=892 sev=B
- 145: ds=864 sev=B
- 677: ds=771 sev=B
- 333: ds=766 sev=B
- 112: ds=718 sev=B
- 344: ds=698 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=110 sev=red
  - 22: ds=67 sev=purple
  - 99: ds=31 sev=purple
  - 77: ds=25 sev=purple
  - 66: ds=20 sev=-
  - 11: ds=19 sev=-
  - 33: ds=17 sev=-
  - 00: ds=16 sev=-
  - 88: ds=9 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 09: ds=62 sev=red
  - 57: ds=46 sev=blue
  - 69: ds=44 sev=blue
  - 23: ds=41 sev=blue
  - 25: ds=39 sev=blue
  - 06: ds=38 sev=blue
  - 07: ds=38 sev=blue
  - 01: ds=36 sev=purple
  - 48: ds=34 sev=purple
  - 78: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:309, 26:137, 4:120, 34:89, 32:82, 25:75, 29:63, 15:62, 2:52, 31:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=309 fs=2 fl=1 hz=0.005961251862891207, 26:ds=137 fs=3 fl=1 hz=0.008680555555555556, 4:ds=120 fs=19 fl=1 hz=0.022753128555176336, 34:ds=89 fs=14 fl=3 hz=0.019144144144144143, 32:ds=82 fs=2 fl=0 hz=0.008450704225352114, 25:ds=75 fs=21 fl=0 hz=0.023836549375709424, 29:ds=63 fs=27 fl=0 hz=0.030100334448160536, 15:ds=62 fs=15 fl=1 hz=0.019698725376593278, 2:ds=52 fs=23 fl=2 hz=0.028344671201814057, 31:ds=49 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=89 flags=blue+purple
- S8: ds=66 flags=red+purple
- S20: ds=49 flags=purple
- S3: ds=36 flags=blue+purple
- S24: ds=32 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:687(B); evening:892(B)
- 355 -> combined:997(B); evening:684(B)
- 445 -> combined:763(B); evening:687(B)
- 459 -> combined:672(B); midday:852(B)
- 888 -> combined:695(B); evening:695(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:37(blue); evening:36(purple)
- 06 -> combined:29(purple); evening:38(blue)
- 07 -> combined:29(purple); evening:38(blue)
- 09 -> combined:59(red); evening:62(red); midday:29(purple)
- 13 -> combined:48(blue); midday:53(blue)
- 19 -> combined:56(red); evening:28(purple); midday:39(blue)
- 22 -> combined:69(purple); evening:67(purple); midday:34(purple)
- 23 -> combined:82(red); evening:41(blue); midday:73(red)
- 25 -> combined:31(purple); evening:39(blue)
- 44 -> combined:81(blue); evening:110(red); midday:40(purple)
- 47 -> combined:25(purple); evening:25(purple)
- 48 -> combined:68(red); evening:34(purple); midday:36(purple)
- 49 -> combined:62(red); evening:31(purple); midday:40(blue)
- 57 -> combined:63(red); evening:46(blue); midday:31(purple)
- 69 -> combined:79(red); evening:44(blue); midday:39(blue)
- 78 -> combined:64(red); evening:32(purple); midday:66(red)
- 99 -> combined:62(purple); evening:31(purple); midday:88(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(7.781414285714286)[R1,XVAR-Cons(CEM)], 9(7.709557142857143)[R2,XVAR-Cons(CEM)], 3(1.9299428571428572)[R3,XVAR-Cons(CE)], 5(0.27153571428571427)[R3,Swap]
- P2: 0(8.324142857142856)[R1,XVAR-Cons(CEM)], 9(2.4592285714285715)[R2,XVAR-Cons(CE)], 2(2.362142857142857)[R3,XVAR-Cons(CM)], 6(0.9135)[R2,Double-Pressure], 3(0.22092142857142857)[R3,Swap]
- P3: 0(6.7576357142857155)[R1,XVAR-Cons(CEM)], 8(3.8019999999999996)[R2,XVAR-Cons(CM)], 4(2.8305857142857143)[R3,XVAR-Cons(CM)], 1(1.1672857142857143)[R1,Double-Pressure], 7(0.23122857142857145)[R3,Swap]
