# Aux Summary — Connecticut4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=356, 970, 109, 228, 361
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=970, 228, 932, 095, 211
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-03/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=356, 109, 361, 467, 055

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=2 last_repeat_gap=35 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=38), P2:8 (gap=12), P3:4 (gap=24)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=37.92402857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 784: score=37.46292857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 714: score=36.65757142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.23789285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 794: score=33.94 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 749: score=32.31308571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.264135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 789: score=31.851985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 740: score=31.21781428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 719: score=31.046628571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=887 sev=B
- 129: ds=869 sev=B
- 288: ds=857 sev=B
- 149: ds=839 sev=B
- 445: ds=771 sev=B
- 114: ds=741 sev=B
- 069: ds=705 sev=B
- 888: ds=703 sev=B
- 688: ds=699 sev=B
- 133: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=89 sev=blue
  - 99: ds=70 sev=purple
  - 00: ds=40 sev=purple
  - 33: ds=27 sev=purple
  - 88: ds=26 sev=purple
  - 66: ds=25 sev=purple
  - 77: ds=15 sev=-
  - 11: ds=9 sev=-
  - 55: ds=8 sev=-
  - 22: ds=3 sev=-
- non_repeating:
  - 69: ds=87 sev=red
  - 48: ds=76 sev=red
  - 78: ds=72 sev=red
  - 57: ds=71 sev=red
  - 49: ds=70 sev=red
  - 25: ds=39 sev=blue
  - 06: ds=37 sev=blue
  - 37: ds=32 sev=purple
  - 18: ds=29 sev=purple
  - 58: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:405, 32:172, 25:158, 29:131, 4:129, 15:117, 31:106, 34:101, 3:86, 35:70

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=405 fs=1 fl=2 hz=0.01098901098901099, 32:ds=172 fs=5 fl=2 hz=0.011267605633802818, 25:ds=158 fs=22 fl=2 hz=0.029055690072639227, 29:ds=131 fs=25 fl=1 hz=0.029988465974625143, 4:ds=129 fs=21 fl=2 hz=0.027677496991576414, 15:ds=117 fs=9 fl=4 hz=0.015531660692951015, 31:ds=106 fs=32 fl=0 hz=0.03665521191294387, 34:ds=101 fs=15 fl=2 hz=0.01951779563719862, 3:ds=86 fs=27 fl=0 hz=0.030337078651685393, 35:ds=70 fs=13 fl=4 hz=0.018743109151047408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=80 flags=purple
- S24: ds=72 flags=blue+purple
- S22: ds=70 flags=purple

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
- current_index=12 streak=1 max=3 last_repeat_gap=74 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=27), P2:0 (gap=27), P3:4 (gap=31)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=37.92402857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 784: score=37.46292857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 714: score=36.65757142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.23789285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 794: score=33.94 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 749: score=32.31308571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.264135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 789: score=31.851985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 740: score=31.21781428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 719: score=31.046628571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=880 sev=B
- 478: ds=861 sev=B
- 459: ds=856 sev=B
- 159: ds=812 sev=B
- 099: ds=793 sev=B
- 127: ds=784 sev=B
- 559: ds=726 sev=B
- 004: ds=685 sev=B
- 155: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=92 sev=blue
  - 88: ds=52 sev=purple
  - 44: ds=44 sev=purple
  - 55: ds=29 sev=purple
  - 00: ds=25 sev=purple
  - 33: ds=13 sev=-
  - 66: ds=12 sev=-
  - 77: ds=7 sev=-
  - 11: ds=4 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 78: ds=70 sev=red
  - 13: ds=57 sev=red
  - 49: ds=44 sev=blue
  - 19: ds=43 sev=blue
  - 69: ds=43 sev=blue
  - 48: ds=40 sev=blue
  - 57: ds=35 sev=purple
  - 37: ds=24 sev=-
  - 01: ds=22 sev=-
  - 08: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:202, 25:103, 31:92, 32:90, 18:87, 3:75, 29:65, 4:64, 15:58, 34:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=202 fs=3 fl=0 hz=0.008565310492505354, 25:ds=103 fs=21 fl=1 hz=0.025974025974025976, 31:ds=92 fs=20 fl=2 hz=0.024608501118568233, 32:ds=90 fs=3 fl=4 hz=0.009510869565217392, 18:ds=87 fs=23 fl=1 hz=0.026519337016574582, 3:ds=75 fs=22 fl=2 hz=0.02631578947368421, 29:ds=65 fs=18 fl=2 hz=0.023446658851113716, 4:ds=64 fs=26 fl=0 hz=0.02931228861330327, 15:ds=58 fs=24 fl=1 hz=0.02662406815761448, 34:ds=50 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=86 flags=blue+purple
- S24: ds=83 flags=blue+purple
- S8: ds=53 flags=purple

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
- current_index=8 streak=1 max=3 last_repeat_gap=11 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=19), P2:9 (gap=16), P3:0 (gap=20)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 744: score=37.92402857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 784: score=37.46292857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 714: score=36.65757142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.23789285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 794: score=33.94 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 749: score=32.31308571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.264135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 789: score=31.851985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 740: score=31.21781428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 719: score=31.046628571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=907 sev=B
- 668: ds=904 sev=B
- 399: ds=903 sev=B
- 044: ds=899 sev=B
- 133: ds=896 sev=B
- 145: ds=868 sev=B
- 677: ds=775 sev=B
- 333: ds=770 sev=B
- 112: ds=722 sev=B
- 344: ds=702 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=114 sev=red
  - 22: ds=71 sev=blue
  - 99: ds=35 sev=purple
  - 77: ds=29 sev=purple
  - 66: ds=24 sev=-
  - 11: ds=23 sev=-
  - 33: ds=21 sev=-
  - 00: ds=20 sev=-
  - 88: ds=13 sev=-
  - 55: ds=4 sev=-
- non_repeating:
  - 57: ds=50 sev=blue
  - 69: ds=48 sev=blue
  - 23: ds=45 sev=blue
  - 25: ds=43 sev=blue
  - 06: ds=42 sev=blue
  - 07: ds=42 sev=blue
  - 48: ds=38 sev=blue
  - 78: ds=36 sev=purple
  - 49: ds=35 sev=purple
  - 15: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:313, 26:141, 4:124, 34:93, 32:86, 25:79, 29:67, 15:66, 2:56, 31:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=313 fs=2 fl=1 hz=0.005961251862891207, 26:ds=141 fs=3 fl=1 hz=0.008680555555555556, 4:ds=124 fs=18 fl=1 hz=0.02243211334120425, 34:ds=93 fs=14 fl=3 hz=0.019144144144144143, 32:ds=86 fs=2 fl=0 hz=0.008450704225352114, 25:ds=79 fs=21 fl=0 hz=0.023836549375709424, 29:ds=67 fs=27 fl=0 hz=0.030100334448160536, 15:ds=66 fs=15 fl=1 hz=0.019698725376593278, 2:ds=56 fs=23 fl=2 hz=0.028344671201814057, 31:ds=53 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=93 flags=blue+purple
- S8: ds=70 flags=red+purple
- S20: ds=53 flags=purple
- S3: ds=40 flags=blue+purple
- S24: ds=36 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 038: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:695(B); evening:896(B)
- 445 -> combined:771(B); evening:691(B)
- 459 -> combined:680(B); midday:856(B)
- 888 -> combined:703(B); evening:699(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:40(purple); midday:25(purple)
- 06 -> combined:37(blue); evening:42(blue)
- 25 -> combined:39(blue); evening:43(blue)
- 44 -> combined:89(blue); evening:114(red); midday:44(purple)
- 48 -> combined:76(red); evening:38(blue); midday:40(blue)
- 49 -> combined:70(red); evening:35(purple); midday:44(blue)
- 57 -> combined:71(red); evening:50(blue); midday:35(purple)
- 69 -> combined:87(red); evening:48(blue); midday:43(blue)
- 78 -> combined:72(red); evening:36(purple); midday:70(red)
- 88 -> combined:26(purple); midday:52(purple)
- 99 -> combined:70(purple); evening:35(purple); midday:92(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.173428571428571)[R1,XVAR-Cons(CEM)], 5(2.679957142857143)[R3,XVAR-Cons(CM)], 6(2.6632285714285713)[R2,XVAR-Cons(CE)], 9(1.0252999999999999)[R2,Double-Pressure], 3(0.24466428571428572)[R3,Swap]
- P2: 8(3.286142857142857)[R1,XVAR-Cons(CM)], 4(2.747242857142857)[R2,XVAR-Cons(CE)], 1(2.480785714285714)[R3,XVAR-Cons(CE)], 0(1.5611071428571428)[R1,Mirror-Echo], 9(1.2632142857142856)[R1,Mirror-Echo]
- P3: 4(4.503357142857142)[R1,XVAR-Cons(CM)], 9(1.3924142857142856)[R2,Mirror-Echo], 0(1.2971428571428572)[R1,Double-Pressure], 3(0.9339999999999999)[R2,Double-Pressure], 2(0.8926)[R2,Double-Pressure]
