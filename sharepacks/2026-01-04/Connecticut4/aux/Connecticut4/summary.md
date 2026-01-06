# Aux Summary — Connecticut4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2026-01-04/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=181, 533, 356, 970, 109
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2026-01-04/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=533, 970, 228, 932, 095
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2026-01-04/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=181, 356, 109, 361, 467

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=2 last_repeat_gap=37 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=40), P2:4 (gap=13), P3:4 (gap=26)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 794: score=38.35089285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 744: score=38.33739285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 714: score=37.55511428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 694: score=35.65620714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 614: score=34.86042857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.435785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 784: score=32.768614285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 799: score=32.67220714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 749: score=32.65870714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.45307142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=889 sev=B
- 129: ds=871 sev=B
- 288: ds=859 sev=B
- 149: ds=841 sev=B
- 445: ds=773 sev=B
- 114: ds=743 sev=B
- 069: ds=707 sev=B
- 888: ds=705 sev=B
- 688: ds=701 sev=B
- 133: ds=697 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=91 sev=blue
  - 99: ds=72 sev=blue
  - 00: ds=42 sev=purple
  - 88: ds=28 sev=purple
  - 66: ds=27 sev=purple
  - 77: ds=17 sev=-
  - 55: ds=10 sev=-
  - 22: ds=5 sev=-
  - 33: ds=1 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 69: ds=89 sev=red
  - 48: ds=78 sev=red
  - 78: ds=74 sev=red
  - 57: ds=73 sev=red
  - 49: ds=72 sev=red
  - 25: ds=41 sev=blue
  - 06: ds=39 sev=blue
  - 37: ds=34 sev=purple
  - 58: ds=23 sev=-
  - 68: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:407, 32:174, 25:160, 29:133, 4:131, 15:119, 31:108, 34:103, 3:88, 35:72

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=407 fs=1 fl=2 hz=0.01098901098901099, 32:ds=174 fs=5 fl=2 hz=0.011267605633802818, 25:ds=160 fs=22 fl=2 hz=0.029055690072639227, 29:ds=133 fs=24 fl=1 hz=0.03071253071253071, 4:ds=131 fs=21 fl=2 hz=0.027677496991576414, 15:ds=119 fs=9 fl=4 hz=0.015531660692951015, 31:ds=108 fs=32 fl=0 hz=0.03665521191294387, 34:ds=103 fs=15 fl=2 hz=0.01951779563719862, 3:ds=88 fs=27 fl=0 hz=0.030337078651685393, 35:ds=72 fs=13 fl=4 hz=0.018743109151047408

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S8: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=82 flags=purple
- S24: ds=74 flags=blue+purple
- S22: ds=72 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=13 streak=1 max=3 last_repeat_gap=75 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=28), P2:0 (gap=28), P3:4 (gap=32)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 794: score=38.35089285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 744: score=38.33739285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 714: score=37.55511428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 694: score=35.65620714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 614: score=34.86042857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.435785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 784: score=32.768614285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 799: score=32.67220714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 749: score=32.65870714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.45307142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 117: ds=881 sev=B
- 478: ds=862 sev=B
- 459: ds=857 sev=B
- 159: ds=813 sev=B
- 099: ds=794 sev=B
- 127: ds=785 sev=B
- 559: ds=727 sev=B
- 004: ds=686 sev=B
- 155: ds=682 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=93 sev=blue
  - 88: ds=53 sev=purple
  - 44: ds=45 sev=purple
  - 55: ds=30 sev=purple
  - 00: ds=26 sev=purple
  - 66: ds=13 sev=-
  - 77: ds=8 sev=-
  - 11: ds=5 sev=-
  - 22: ds=2 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 78: ds=71 sev=red
  - 13: ds=58 sev=red
  - 49: ds=45 sev=blue
  - 19: ds=44 sev=blue
  - 69: ds=44 sev=blue
  - 48: ds=41 sev=blue
  - 57: ds=36 sev=purple
  - 37: ds=25 sev=purple
  - 01: ds=23 sev=-
  - 08: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:203, 25:104, 31:93, 32:91, 18:88, 3:76, 29:66, 4:65, 15:59, 34:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=203 fs=3 fl=0 hz=0.008565310492505354, 25:ds=104 fs=21 fl=1 hz=0.025974025974025976, 31:ds=93 fs=20 fl=2 hz=0.024608501118568233, 32:ds=91 fs=3 fl=4 hz=0.009510869565217392, 18:ds=88 fs=23 fl=1 hz=0.026519337016574582, 3:ds=76 fs=22 fl=2 hz=0.02631578947368421, 29:ds=66 fs=18 fl=2 hz=0.023446658851113716, 4:ds=65 fs=26 fl=0 hz=0.02931228861330327, 15:ds=59 fs=24 fl=1 hz=0.02662406815761448, 34:ds=51 fs=23 fl=1 hz=0.026845637583892617

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=87 flags=blue+purple
- S24: ds=84 flags=blue+purple
- S8: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=12 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=20), P2:9 (gap=17), P3:0 (gap=21)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 794: score=38.35089285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 744: score=38.33739285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 714: score=37.55511428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 694: score=35.65620714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 614: score=34.86042857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 704: score=34.435785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 784: score=32.768614285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 799: score=32.67220714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 749: score=32.65870714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 754: score=32.45307142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 678: ds=908 sev=B
- 668: ds=905 sev=B
- 399: ds=904 sev=B
- 044: ds=900 sev=B
- 133: ds=897 sev=B
- 145: ds=869 sev=B
- 677: ds=776 sev=B
- 333: ds=771 sev=B
- 112: ds=723 sev=B
- 344: ds=703 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=115 sev=red
  - 22: ds=72 sev=blue
  - 99: ds=36 sev=purple
  - 77: ds=30 sev=purple
  - 66: ds=25 sev=purple
  - 33: ds=22 sev=-
  - 00: ds=21 sev=-
  - 88: ds=14 sev=-
  - 55: ds=5 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 57: ds=51 sev=blue
  - 69: ds=49 sev=blue
  - 23: ds=46 sev=blue
  - 25: ds=44 sev=blue
  - 06: ds=43 sev=blue
  - 07: ds=43 sev=blue
  - 48: ds=39 sev=blue
  - 78: ds=37 sev=blue
  - 49: ds=36 sev=purple
  - 15: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:314, 26:142, 4:125, 34:94, 32:87, 25:80, 29:68, 15:67, 2:57, 31:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=314 fs=2 fl=1 hz=0.005961251862891207, 26:ds=142 fs=3 fl=1 hz=0.008680555555555556, 4:ds=125 fs=18 fl=1 hz=0.02243211334120425, 34:ds=94 fs=14 fl=3 hz=0.019144144144144143, 32:ds=87 fs=2 fl=0 hz=0.008450704225352114, 25:ds=80 fs=21 fl=0 hz=0.023836549375709424, 29:ds=68 fs=27 fl=0 hz=0.030100334448160536, 15:ds=67 fs=15 fl=1 hz=0.019698725376593278, 2:ds=57 fs=23 fl=2 hz=0.028344671201814057, 31:ds=54 fs=23 fl=1 hz=0.03296703296703297

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=94 flags=blue+purple
- S8: ds=71 flags=red+purple
- S20: ds=54 flags=purple
- S3: ds=41 flags=blue+purple
- S24: ds=37 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 123: score=1 tags=FLT
  - 124: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 133 -> combined:697(B); evening:897(B)
- 445 -> combined:773(B); evening:692(B)
- 459 -> combined:682(B); midday:857(B)
- 888 -> combined:705(B); evening:700(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:42(purple); midday:26(purple)
- 06 -> combined:39(blue); evening:43(blue)
- 25 -> combined:41(blue); evening:44(blue)
- 37 -> combined:34(purple); midday:25(purple)
- 44 -> combined:91(blue); evening:115(red); midday:45(purple)
- 48 -> combined:78(red); evening:39(blue); midday:41(blue)
- 49 -> combined:72(red); evening:36(purple); midday:45(blue)
- 57 -> combined:73(red); evening:51(blue); midday:36(purple)
- 66 -> combined:27(purple); evening:25(purple)
- 69 -> combined:89(red); evening:49(blue); midday:44(blue)
- 78 -> combined:74(red); evening:37(blue); midday:71(red)
- 88 -> combined:28(purple); midday:53(purple)
- 99 -> combined:72(blue); evening:36(purple); midday:93(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.233142857142859)[R1,XVAR-Cons(CEM)], 6(5.538457142857143)[R2,XVAR-Cons(CEM)], 9(1.0761999999999998)[R2,Double-Pressure], 3(0.8926)[R2,Double-Pressure], 8(0.35457142857142854)[R3,Swap]
- P2: 1(3.2164)[R2,XVAR-Cons(CE)], 9(3.0121785714285716)[R3,Mirror-Echo], 4(2.9986785714285715)[R1,Mirror-Echo], 0(1.5970714285714285)[R1,Mirror-Echo], 8(0.9299)[R2,Double-Pressure]
- P3: 4(4.605571428571428)[R1,XVAR-Cons(CM)], 9(1.4268857142857143)[R2,Mirror-Echo], 0(1.327)[R1,Double-Pressure], 2(0.9135)[R2,Double-Pressure], 5(0.8979999999999999)[R2,Double-Pressure]
