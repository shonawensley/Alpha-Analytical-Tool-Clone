# Aux Summary — OntarioCanada4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-01/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=932, 918, 372, 409, 043
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-01/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=918, 409, 006, 313, 909
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-01/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=932, 372, 043, 297, 606

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=48 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=22), P2:8 (gap=20), P3:4 (gap=21)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=45.70740714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=41.688540714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 164: score=41.42677857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=39.99754285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 124: score=38.77385 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 161: score=37.40791214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.06717857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=36.86896285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 174: score=36.53153571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=36.480450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 222: ds=999 sev=B
- 128: ds=919 sev=B
- 555: ds=884 sev=B
- 039: ds=775 sev=B
- 333: ds=746 sev=B
- 188: ds=719 sev=B
- 266: ds=705 sev=B
- 477: ds=703 sev=B
- 126: ds=695 sev=B
- 669: ds=690 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=121 sev=red
  - 55: ds=77 sev=blue
  - 11: ds=36 sev=purple
  - 88: ds=30 sev=purple
  - 44: ds=21 sev=-
  - 77: ds=12 sev=-
  - 99: ds=9 sev=-
  - 66: ds=8 sev=-
  - 33: ds=7 sev=-
  - 00: ds=5 sev=-
- non_repeating:
  - 01: ds=56 sev=red
  - 68: ds=54 sev=blue
  - 15: ds=53 sev=blue
  - 17: ds=47 sev=blue
  - 12: ds=33 sev=purple
  - 69: ds=32 sev=purple
  - 24: ds=31 sev=purple
  - 26: ds=31 sev=purple
  - 67: ds=28 sev=purple
  - 36: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:331, 16:285, 17:157, 20:135, 33:81, 12:80, 26:75, 34:62, 8:58, 9:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=331 fs=1 fl=0 hz=0.005698005698005698, 16:ds=285 fs=2 fl=0 hz=0.006329113924050633, 17:ds=157 fs=19 fl=1 hz=0.024242424242424242, 20:ds=135 fs=14 fl=2 hz=0.01853997682502897, 33:ds=81 fs=24 fl=1 hz=0.027472527472527472, 12:ds=80 fs=45 fl=0 hz=0.04928806133625411, 26:ds=75 fs=2 fl=1 hz=0.006075334143377886, 34:ds=62 fs=14 fl=2 hz=0.019698725376593278, 8:ds=58 fs=39 fl=2 hz=0.044956140350877194, 9:ds=53 fs=44 fl=0 hz=0.04751619870410367

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=99 flags=red+purple
- S23: ds=76 flags=blue+purple
- S21: ds=73 flags=purple
- S4: ds=67 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 046: score=3 tags=FLT,RS
  - 136: score=3 tags=FLT,RS
  - 145: score=3 tags=FLT,RS
  - 235: score=3 tags=FLT,RS
  - 469: score=3 tags=FLT,RS
  - 568: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 028: score=2 tags=RS
  - 037: score=2 tags=RS
  - 127: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=16 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=26), P2:7 (gap=22), P3:0 (gap=14)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=45.70740714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=41.688540714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 164: score=41.42677857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=39.99754285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 124: score=38.77385 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 161: score=37.40791214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.06717857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=36.86896285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 174: score=36.53153571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=36.480450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=994 sev=B
- 333: ds=977 sev=B
- 255: ds=944 sev=B
- 355: ds=909 sev=B
- 466: ds=830 sev=B
- 446: ds=738 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=60 sev=purple
  - 55: ds=38 sev=purple
  - 11: ds=28 sev=purple
  - 77: ds=21 sev=-
  - 88: ds=17 sev=-
  - 66: ds=12 sev=-
  - 44: ds=10 sev=-
  - 99: ds=4 sev=-
  - 33: ds=3 sev=-
  - 00: ds=2 sev=-
- non_repeating:
  - 34: ds=69 sev=red
  - 07: ds=66 sev=red
  - 16: ds=52 sev=blue
  - 39: ds=40 sev=blue
  - 68: ds=36 sev=purple
  - 37: ds=35 sev=purple
  - 67: ds=35 sev=purple
  - 03: ds=33 sev=purple
  - 48: ds=32 sev=purple
  - 01: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:165, 34:160, 16:142, 27:97, 12:94, 14:79, 17:78, 20:67, 19:52, 33:40

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=165 fs=4 fl=3 hz=0.010432190760059612, 34:ds=160 fs=8 fl=4 hz=0.014423076923076924, 16:ds=142 fs=3 fl=0 hz=0.007462686567164179, 27:ds=97 fs=15 fl=2 hz=0.0189520624303233, 12:ds=94 fs=45 fl=0 hz=0.05079006772009029, 14:ds=79 fs=39 fl=0 hz=0.04276315789473684, 17:ds=78 fs=29 fl=2 hz=0.033879781420765025, 20:ds=67 fs=24 fl=3 hz=0.029315960912052113, 19:ds=52 fs=20 fl=2 hz=0.023732470334412083, 33:ds=40 fs=18 fl=2 hz=0.021119324181626188

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=76 flags=purple
- S25: ds=72 flags=purple
- S1: ds=61 flags=blue+purple
- S5: ds=59 flags=purple
- S8: ds=57 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=53 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=15), P2:1 (gap=51), P3:9 (gap=38)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=51)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=45.70740714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=41.688540714285715 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 164: score=41.42677857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=39.99754285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 124: score=38.77385 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 161: score=37.40791214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.06717857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=36.86896285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 174: score=36.53153571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=36.480450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=901 sev=B
- 113: ds=852 sev=B
- 378: ds=845 sev=B
- 566: ds=834 sev=B
- 199: ds=826 sev=B
- 899: ds=804 sev=B
- 126: ds=800 sev=B
- 559: ds=795 sev=B
- 477: ds=784 sev=B
- 558: ds=750 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=230 sev=red
  - 22: ds=61 sev=purple
  - 00: ds=48 sev=purple
  - 44: ds=31 sev=purple
  - 11: ds=18 sev=-
  - 99: ds=16 sev=-
  - 88: ds=15 sev=-
  - 33: ds=13 sev=-
  - 77: ds=6 sev=-
  - 66: ds=4 sev=-
- non_repeating:
  - 36: ds=73 sev=red
  - 24: ds=57 sev=red
  - 18: ds=51 sev=blue
  - 89: ds=51 sev=blue
  - 15: ds=50 sev=blue
  - 78: ds=49 sev=blue
  - 49: ds=43 sev=blue
  - 57: ds=40 sev=blue
  - 09: ds=30 sev=purple
  - 01: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:426, 1:341, 16:192, 26:124, 18:109, 17:102, 20:93, 3:72, 23:65, 33:63

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=426 fs=0 fl=2 hz=0.005366726296958855, 1:ds=341 fs=0 fl=0 hz=0.0, 16:ds=192 fs=3 fl=1 hz=0.007853403141361256, 26:ds=124 fs=3 fl=3 hz=0.0076045627376425855, 18:ds=109 fs=16 fl=1 hz=0.019384264538198404, 17:ds=102 fs=13 fl=3 hz=0.018626309662398137, 20:ds=93 fs=15 fl=2 hz=0.01925254813137033, 3:ds=72 fs=15 fl=4 hz=0.02092511013215859, 23:ds=65 fs=25 fl=2 hz=0.03085714285714286, 33:ds=63 fs=27 fl=1 hz=0.030803080308030802

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=82 flags=purple
- S2: ds=72 flags=blue+purple
- S4: ds=70 flags=purple
- S25: ds=59 flags=purple
- S20: ds=52 flags=purple
- S9: ds=50 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:695(B); evening:800(B)
- 128 -> combined:919(B); evening:901(B)
- 333 -> combined:746(B); midday:977(B)
- 477 -> combined:703(B); evening:784(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:56(red); evening:28(purple); midday:28(purple)
- 11 -> combined:36(purple); midday:28(purple)
- 12 -> combined:33(purple); evening:28(purple)
- 15 -> combined:53(blue); evening:50(blue); midday:26(purple)
- 22 -> combined:121(red); evening:61(purple); midday:60(purple)
- 24 -> combined:31(purple); evening:57(red)
- 36 -> combined:25(purple); evening:73(red)
- 55 -> combined:77(blue); evening:230(red); midday:38(purple)
- 67 -> combined:28(purple); midday:35(purple)
- 68 -> combined:54(blue); evening:27(purple); midday:36(purple)
- 69 -> combined:32(purple); midday:27(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(6.731721428571428)[R1,XVAR-Cons(CEM)], 8(3.521857142857143)[R2,XVAR-Cons(CE)], 5(2.9025714285714286)[R3,XVAR-Cons(CM)], 4(0.8508)[R2,Double-Pressure], 2(0.39558571428571426)[R3,Swap]
- P2: 8(6.518228571428572)[R1,XVAR-Cons(CEM)], 6(3.7376)[R2,XVAR-Cons(CE)], 2(2.0846714285714287)[R3,XVAR-Cons(CM)], 1(1.878)[R1,Mirror-Echo], 7(1.3423571428571428)[R1,Mirror-Echo]
- P3: 4(5.957457142857143)[R1,XVAR-Cons(CEM)], 1(2.630057142857143)[R3,XVAR-Cons(CE)], 9(1.7305)[R1,Mirror-Echo], 0(1.018)[R1,Double-Pressure], 2(0.9717)[R2,Double-Pressure]
