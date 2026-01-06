# Aux Summary — OntarioCanada4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-03/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=816, 053, 546, 528, 932
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-03/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=053, 528, 918, 409, 006
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-03/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=816, 546, 932, 372, 043

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=52 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=26), P2:8 (gap=24), P3:4 (gap=25)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=49.828407142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.712785714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=45.92408857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=42.72475714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.6343 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 764: score=40.60913571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.39420714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.24375285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 161: score=38.820438571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=38.62920714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=923 sev=B
- 555: ds=888 sev=B
- 039: ds=779 sev=B
- 333: ds=750 sev=B
- 188: ds=723 sev=B
- 266: ds=709 sev=B
- 477: ds=707 sev=B
- 126: ds=699 sev=B
- 669: ds=694 sev=B
- 007: ds=684 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=125 sev=red
  - 55: ds=81 sev=blue
  - 11: ds=40 sev=purple
  - 88: ds=34 sev=purple
  - 44: ds=25 sev=purple
  - 77: ds=16 sev=-
  - 99: ds=13 sev=-
  - 66: ds=12 sev=-
  - 33: ds=11 sev=-
  - 00: ds=9 sev=-
- non_repeating:
  - 01: ds=60 sev=red
  - 15: ds=57 sev=red
  - 17: ds=51 sev=blue
  - 12: ds=37 sev=blue
  - 69: ds=36 sev=purple
  - 24: ds=35 sev=purple
  - 26: ds=35 sev=purple
  - 67: ds=32 sev=purple
  - 36: ds=29 sev=purple
  - 48: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:335, 16:289, 17:161, 20:139, 33:85, 12:84, 26:79, 34:66, 8:62, 7:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=335 fs=1 fl=0 hz=0.005698005698005698, 16:ds=289 fs=2 fl=0 hz=0.006329113924050633, 17:ds=161 fs=19 fl=1 hz=0.024242424242424242, 20:ds=139 fs=13 fl=2 hz=0.01847290640394089, 33:ds=85 fs=24 fl=1 hz=0.027472527472527472, 12:ds=84 fs=45 fl=0 hz=0.04928806133625411, 26:ds=79 fs=2 fl=1 hz=0.006075334143377886, 34:ds=66 fs=14 fl=2 hz=0.019698725376593278, 8:ds=62 fs=39 fl=2 hz=0.044956140350877194, 7:ds=46 fs=44 fl=1 hz=0.04756871035940803

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=80 flags=blue+purple
- S21: ds=77 flags=purple
- S4: ds=71 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 127: score=4 tags=FLT,MIR,RS
  - 037: score=3 tags=FLT,RS
  - 136: score=3 tags=MIR,RS
  - 379: score=3 tags=FLT,RS
  - 469: score=3 tags=MIR,RS
  - 478: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 027: score=2 tags=FLT,MIR
  - 028: score=2 tags=RS
  - 046: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=4 streak=1 max=2 last_repeat_gap=18 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=27), P2:7 (gap=24), P3:0 (gap=16)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=49.828407142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.712785714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=45.92408857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=42.72475714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.6343 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 764: score=40.60913571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.39420714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.24375285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 161: score=38.820438571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=38.62920714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=996 sev=B
- 333: ds=979 sev=B
- 255: ds=946 sev=B
- 355: ds=911 sev=B
- 466: ds=832 sev=B
- 446: ds=740 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=62 sev=purple
  - 55: ds=40 sev=purple
  - 11: ds=30 sev=purple
  - 77: ds=23 sev=-
  - 88: ds=19 sev=-
  - 66: ds=14 sev=-
  - 44: ds=12 sev=-
  - 99: ds=6 sev=-
  - 33: ds=5 sev=-
  - 00: ds=4 sev=-
- non_repeating:
  - 34: ds=71 sev=red
  - 07: ds=68 sev=red
  - 16: ds=54 sev=blue
  - 39: ds=42 sev=blue
  - 68: ds=38 sev=blue
  - 37: ds=37 sev=blue
  - 67: ds=37 sev=blue
  - 48: ds=34 sev=purple
  - 01: ds=30 sev=purple
  - 69: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:167, 34:162, 16:144, 27:99, 12:96, 14:81, 17:80, 20:69, 19:54, 33:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=167 fs=4 fl=3 hz=0.010432190760059612, 34:ds=162 fs=8 fl=4 hz=0.014423076923076924, 16:ds=144 fs=3 fl=0 hz=0.007462686567164179, 27:ds=99 fs=15 fl=2 hz=0.0189520624303233, 12:ds=96 fs=45 fl=0 hz=0.05079006772009029, 14:ds=81 fs=39 fl=0 hz=0.04276315789473684, 17:ds=80 fs=29 fl=2 hz=0.033879781420765025, 20:ds=69 fs=24 fl=3 hz=0.029315960912052113, 19:ds=54 fs=20 fl=2 hz=0.023732470334412083, 33:ds=42 fs=18 fl=2 hz=0.021119324181626188

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=78 flags=purple
- S25: ds=74 flags=purple
- S1: ds=63 flags=blue+purple
- S5: ds=61 flags=purple
- S9: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 027: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 247: score=2 tags=FLT,MIR
  - 257: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 279: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=55 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=14), P2:6 (gap=16), P3:9 (gap=40)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:9 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=49.828407142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.712785714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=45.92408857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=42.72475714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.6343 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 764: score=40.60913571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.39420714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.24375285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 161: score=38.820438571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=38.62920714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=903 sev=B
- 113: ds=854 sev=B
- 378: ds=847 sev=B
- 566: ds=836 sev=B
- 199: ds=828 sev=B
- 899: ds=806 sev=B
- 126: ds=802 sev=B
- 559: ds=797 sev=B
- 477: ds=786 sev=B
- 558: ds=752 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=232 sev=red
  - 22: ds=63 sev=purple
  - 00: ds=50 sev=purple
  - 44: ds=33 sev=purple
  - 11: ds=20 sev=-
  - 99: ds=18 sev=-
  - 88: ds=17 sev=-
  - 33: ds=15 sev=-
  - 77: ds=8 sev=-
  - 66: ds=6 sev=-
- non_repeating:
  - 36: ds=75 sev=red
  - 24: ds=59 sev=red
  - 89: ds=53 sev=blue
  - 15: ds=52 sev=blue
  - 78: ds=51 sev=blue
  - 49: ds=45 sev=blue
  - 57: ds=42 sev=blue
  - 09: ds=32 sev=purple
  - 01: ds=30 sev=purple
  - 12: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:428, 1:343, 16:194, 26:126, 17:104, 20:95, 3:74, 23:67, 33:65, 31:61

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=428 fs=0 fl=2 hz=0.005366726296958855, 1:ds=343 fs=0 fl=0 hz=0.0, 16:ds=194 fs=3 fl=1 hz=0.007853403141361256, 26:ds=126 fs=3 fl=3 hz=0.0076045627376425855, 17:ds=104 fs=13 fl=3 hz=0.018626309662398137, 20:ds=95 fs=15 fl=2 hz=0.01925254813137033, 3:ds=74 fs=15 fl=4 hz=0.02092511013215859, 23:ds=67 fs=25 fl=2 hz=0.03085714285714286, 33:ds=65 fs=27 fl=1 hz=0.030803080308030802, 31:ds=61 fs=23 fl=0 hz=0.02666666666666667

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=84 flags=purple
- S2: ds=74 flags=blue+purple
- S4: ds=72 flags=purple
- S25: ds=61 flags=purple
- S20: ds=54 flags=purple
- S9: ds=52 flags=red+purple

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
- 126 -> combined:699(B); evening:802(B)
- 128 -> combined:923(B); evening:903(B)
- 333 -> combined:750(B); midday:979(B)
- 477 -> combined:707(B); evening:786(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:60(red); evening:30(purple); midday:30(purple)
- 11 -> combined:40(purple); midday:30(purple)
- 12 -> combined:37(blue); evening:30(purple)
- 15 -> combined:57(red); evening:52(blue); midday:28(purple)
- 17 -> combined:51(blue); evening:26(purple); midday:25(purple)
- 22 -> combined:125(red); evening:63(purple); midday:62(purple)
- 24 -> combined:35(purple); evening:59(red)
- 36 -> combined:29(purple); evening:75(red)
- 44 -> combined:25(purple); evening:33(purple)
- 48 -> combined:28(purple); midday:34(purple)
- 55 -> combined:81(blue); evening:232(red); midday:40(purple)
- 67 -> combined:32(purple); midday:37(blue)
- 69 -> combined:36(purple); midday:29(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.882128571428572)[R1,Mirror-Echo], 7(5.766507142857143)[R2,XVAR-Cons(CEM)], 2(1.3420642857142857)[R2,Mirror-Echo], 4(1.088)[R1,Double-Pressure], 6(0.6411428571428572)[R3,Mirror-Echo]
- P2: 8(7.169364285714286)[R1,XVAR-Cons(CEM)], 6(3.565714285714286)[R2,XVAR-Cons(CE)], 7(1.4165714285714284)[R1,Double-Pressure], 3(0.3282928571428571)[R3,Mirror-Echo], 9(0.2414285714285714)[R3,Swap]
- P3: 4(6.276914285714286)[R1,XVAR-Cons(CEM)], 1(2.6984285714285714)[R3,XVAR-Cons(CE)], 9(1.8427142857142857)[R1,Mirror-Echo], 0(1.0777142857142856)[R1,Double-Pressure], 5(1.018)[R2,Double-Pressure]
