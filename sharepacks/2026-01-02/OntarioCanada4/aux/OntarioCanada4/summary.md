# Aux Summary — OntarioCanada4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-02/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=546, 528, 932, 918, 372
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-02/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=528, 918, 409, 006, 313
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-02/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=546, 932, 372, 043, 297

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=50 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=24), P2:8 (gap=22), P3:4 (gap=23)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=47.28547857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=43.339848571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=41.91148571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=41.31939285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 484: score=38.17104428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 189: score=37.974900000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=37.96585571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.49648571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 180: score=36.35615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=36.212292857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=921 sev=B
- 555: ds=886 sev=B
- 039: ds=777 sev=B
- 333: ds=748 sev=B
- 188: ds=721 sev=B
- 266: ds=707 sev=B
- 477: ds=705 sev=B
- 126: ds=697 sev=B
- 669: ds=692 sev=B
- 007: ds=682 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=123 sev=red
  - 55: ds=79 sev=blue
  - 11: ds=38 sev=purple
  - 88: ds=32 sev=purple
  - 44: ds=23 sev=-
  - 77: ds=14 sev=-
  - 99: ds=11 sev=-
  - 66: ds=10 sev=-
  - 33: ds=9 sev=-
  - 00: ds=7 sev=-
- non_repeating:
  - 01: ds=58 sev=red
  - 68: ds=56 sev=red
  - 15: ds=55 sev=blue
  - 17: ds=49 sev=blue
  - 12: ds=35 sev=purple
  - 69: ds=34 sev=purple
  - 24: ds=33 sev=purple
  - 26: ds=33 sev=purple
  - 67: ds=30 sev=purple
  - 36: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:333, 16:287, 17:159, 20:137, 33:83, 12:82, 26:77, 34:64, 8:60, 7:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=333 fs=1 fl=0 hz=0.005698005698005698, 16:ds=287 fs=2 fl=0 hz=0.006329113924050633, 17:ds=159 fs=19 fl=1 hz=0.024242424242424242, 20:ds=137 fs=13 fl=2 hz=0.01847290640394089, 33:ds=83 fs=24 fl=1 hz=0.027472527472527472, 12:ds=82 fs=45 fl=0 hz=0.04928806133625411, 26:ds=77 fs=2 fl=1 hz=0.006075334143377886, 34:ds=64 fs=14 fl=2 hz=0.019698725376593278, 8:ds=60 fs=39 fl=2 hz=0.044956140350877194, 7:ds=44 fs=44 fl=1 hz=0.04756871035940803

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=78 flags=blue+purple
- S21: ds=75 flags=purple
- S4: ds=69 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 019: score=3 tags=FLT,RS
  - 028: score=3 tags=FLT,RS
  - 037: score=3 tags=FLT,RS
  - 046: score=3 tags=FLT,RS
  - 127: score=2 tags=RS
  - 136: score=2 tags=RS
  - 145: score=2 tags=RS
  - 235: score=2 tags=RS
  - 289: score=2 tags=RS
  - 379: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=2 last_repeat_gap=17 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=26), P2:7 (gap=23), P3:0 (gap=15)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=47.28547857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=43.339848571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=41.91148571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=41.31939285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 484: score=38.17104428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 189: score=37.974900000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=37.96585571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.49648571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 180: score=36.35615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=36.212292857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=995 sev=B
- 333: ds=978 sev=B
- 255: ds=945 sev=B
- 355: ds=910 sev=B
- 466: ds=831 sev=B
- 446: ds=739 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=61 sev=purple
  - 55: ds=39 sev=purple
  - 11: ds=29 sev=purple
  - 77: ds=22 sev=-
  - 88: ds=18 sev=-
  - 66: ds=13 sev=-
  - 44: ds=11 sev=-
  - 99: ds=5 sev=-
  - 33: ds=4 sev=-
  - 00: ds=3 sev=-
- non_repeating:
  - 34: ds=70 sev=red
  - 07: ds=67 sev=red
  - 16: ds=53 sev=blue
  - 39: ds=41 sev=blue
  - 68: ds=37 sev=blue
  - 37: ds=36 sev=purple
  - 67: ds=36 sev=purple
  - 03: ds=34 sev=purple
  - 48: ds=33 sev=purple
  - 01: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:166, 34:161, 16:143, 27:98, 12:95, 14:80, 17:79, 20:68, 19:53, 33:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=166 fs=4 fl=3 hz=0.010432190760059612, 34:ds=161 fs=8 fl=4 hz=0.014423076923076924, 16:ds=143 fs=3 fl=0 hz=0.007462686567164179, 27:ds=98 fs=15 fl=2 hz=0.0189520624303233, 12:ds=95 fs=45 fl=0 hz=0.05079006772009029, 14:ds=80 fs=39 fl=0 hz=0.04276315789473684, 17:ds=79 fs=29 fl=2 hz=0.033879781420765025, 20:ds=68 fs=24 fl=3 hz=0.029315960912052113, 19:ds=53 fs=20 fl=2 hz=0.023732470334412083, 33:ds=41 fs=18 fl=2 hz=0.021119324181626188

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=77 flags=purple
- S25: ds=73 flags=purple
- S1: ds=62 flags=blue+purple
- S5: ds=60 flags=purple
- S8: ds=58 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 067: score=1 tags=FLT
  - 078: score=1 tags=FLT
  - 079: score=1 tags=FLT
  - 127: score=1 tags=FLT
  - 137: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=54 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=16), P2:1 (gap=52), P3:9 (gap=39)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=52)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=47.28547857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=43.339848571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 164: score=41.91148571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 884: score=41.31939285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 484: score=38.17104428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 189: score=37.974900000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 161: score=37.96585571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 114: score=37.49648571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 180: score=36.35615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=36.212292857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=902 sev=B
- 113: ds=853 sev=B
- 378: ds=846 sev=B
- 566: ds=835 sev=B
- 199: ds=827 sev=B
- 899: ds=805 sev=B
- 126: ds=801 sev=B
- 559: ds=796 sev=B
- 477: ds=785 sev=B
- 558: ds=751 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=231 sev=red
  - 22: ds=62 sev=purple
  - 00: ds=49 sev=purple
  - 44: ds=32 sev=purple
  - 11: ds=19 sev=-
  - 99: ds=17 sev=-
  - 88: ds=16 sev=-
  - 33: ds=14 sev=-
  - 77: ds=7 sev=-
  - 66: ds=5 sev=-
- non_repeating:
  - 36: ds=74 sev=red
  - 24: ds=58 sev=red
  - 18: ds=52 sev=blue
  - 89: ds=52 sev=blue
  - 15: ds=51 sev=blue
  - 78: ds=50 sev=blue
  - 49: ds=44 sev=blue
  - 57: ds=41 sev=blue
  - 09: ds=31 sev=purple
  - 01: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:427, 1:342, 16:193, 26:125, 18:110, 17:103, 20:94, 3:73, 23:66, 33:64

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=427 fs=0 fl=2 hz=0.005366726296958855, 1:ds=342 fs=0 fl=0 hz=0.0, 16:ds=193 fs=3 fl=1 hz=0.007853403141361256, 26:ds=125 fs=3 fl=3 hz=0.0076045627376425855, 18:ds=110 fs=16 fl=1 hz=0.019384264538198404, 17:ds=103 fs=13 fl=3 hz=0.018626309662398137, 20:ds=94 fs=15 fl=2 hz=0.01925254813137033, 3:ds=73 fs=15 fl=4 hz=0.02092511013215859, 23:ds=66 fs=25 fl=2 hz=0.03085714285714286, 33:ds=64 fs=27 fl=1 hz=0.030803080308030802

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=83 flags=purple
- S2: ds=73 flags=blue+purple
- S4: ds=71 flags=purple
- S25: ds=60 flags=purple
- S20: ds=53 flags=purple
- S9: ds=51 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 038: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:697(B); evening:801(B)
- 128 -> combined:921(B); evening:902(B)
- 333 -> combined:748(B); midday:978(B)
- 477 -> combined:705(B); evening:785(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:58(red); evening:29(purple); midday:29(purple)
- 11 -> combined:38(purple); midday:29(purple)
- 12 -> combined:35(purple); evening:29(purple)
- 15 -> combined:55(blue); evening:51(blue); midday:27(purple)
- 17 -> combined:49(blue); evening:25(purple)
- 22 -> combined:123(red); evening:62(purple); midday:61(purple)
- 24 -> combined:33(purple); evening:58(red)
- 36 -> combined:27(purple); evening:74(red)
- 48 -> combined:26(purple); midday:33(purple)
- 55 -> combined:79(blue); evening:231(red); midday:39(purple)
- 67 -> combined:30(purple); midday:36(purple)
- 68 -> combined:56(red); evening:28(purple); midday:37(blue)
- 69 -> combined:34(purple); midday:28(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.061800000000001)[R1,XVAR-Cons(CEM)], 8(3.5957142857142856)[R2,XVAR-Cons(CE)], 7(2.112085714285714)[R3,XVAR-Cons(CM)], 2(1.2150571428571428)[R2,Mirror-Echo], 4(0.8716999999999999)[R2,Double-Pressure]
- P2: 8(6.676492857142858)[R1,XVAR-Cons(CEM)], 6(3.8024999999999998)[R2,XVAR-Cons(CE)], 1(1.8875)[R1,Mirror-Echo], 7(1.3867142857142856)[R1,Double-Pressure], 3(0.37535714285714283)[R3,Mirror-Echo]
- P3: 4(6.047185714285714)[R1,XVAR-Cons(CEM)], 1(2.679242857142857)[R3,XVAR-Cons(CE)], 9(1.7366071428571428)[R1,Mirror-Echo], 0(1.1178571428571429)[R1,Double-Pressure], 5(0.974)[R2,Double-Pressure]
