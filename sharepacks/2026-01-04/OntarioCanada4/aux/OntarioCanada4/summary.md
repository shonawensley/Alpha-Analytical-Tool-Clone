# Aux Summary — OntarioCanada4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2026-01-04/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=032, 968, 816, 053, 546
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2026-01-04/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=968, 053, 528, 918, 409
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2026-01-04/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=032, 816, 546, 932, 372

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=3 last_repeat_gap=54 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=28), P2:8 (gap=26), P3:4 (gap=27)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=50.08537142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.99365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=46.08120714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.80462142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.56755 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.509978571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 180: score=38.9263 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=38.78072857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=38.75312857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 789: score=38.47582857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=925 sev=B
- 555: ds=890 sev=B
- 039: ds=781 sev=B
- 333: ds=752 sev=B
- 188: ds=725 sev=B
- 266: ds=711 sev=B
- 477: ds=709 sev=B
- 126: ds=701 sev=B
- 669: ds=696 sev=B
- 007: ds=686 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=127 sev=red
  - 55: ds=83 sev=blue
  - 11: ds=42 sev=purple
  - 88: ds=36 sev=purple
  - 44: ds=27 sev=purple
  - 77: ds=18 sev=-
  - 99: ds=15 sev=-
  - 66: ds=14 sev=-
  - 33: ds=13 sev=-
  - 00: ds=11 sev=-
- non_repeating:
  - 01: ds=62 sev=red
  - 15: ds=59 sev=red
  - 17: ds=53 sev=blue
  - 12: ds=39 sev=blue
  - 24: ds=37 sev=blue
  - 26: ds=37 sev=blue
  - 67: ds=34 sev=purple
  - 36: ds=31 sev=purple
  - 48: ds=30 sev=purple
  - 08: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:337, 16:291, 17:163, 20:141, 33:87, 12:86, 26:81, 34:68, 8:64, 7:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=337 fs=1 fl=0 hz=0.005698005698005698, 16:ds=291 fs=2 fl=0 hz=0.006329113924050633, 17:ds=163 fs=19 fl=1 hz=0.024242424242424242, 20:ds=141 fs=13 fl=2 hz=0.01847290640394089, 33:ds=87 fs=24 fl=1 hz=0.027472527472527472, 12:ds=86 fs=45 fl=0 hz=0.04928806133625411, 26:ds=81 fs=2 fl=1 hz=0.006075334143377886, 34:ds=68 fs=14 fl=2 hz=0.019698725376593278, 8:ds=64 fs=39 fl=2 hz=0.044956140350877194, 7:ds=48 fs=44 fl=1 hz=0.04756871035940803

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S9: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=79 flags=purple
- S4: ds=73 flags=purple
- S3: ds=62 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 037: score=3 tags=FLT,RS
  - 127: score=3 tags=FLT,RS
  - 379: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 028: score=2 tags=RS
  - 046: score=2 tags=RS
  - 136: score=2 tags=RS
  - 145: score=2 tags=RS
  - 235: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=19 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=28), P2:7 (gap=25), P3:0 (gap=17)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=50.08537142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.99365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=46.08120714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.80462142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.56755 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.509978571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 180: score=38.9263 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=38.78072857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=38.75312857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 789: score=38.47582857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=997 sev=B
- 333: ds=980 sev=B
- 255: ds=947 sev=B
- 355: ds=912 sev=B
- 466: ds=833 sev=B
- 446: ds=741 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=63 sev=purple
  - 55: ds=41 sev=purple
  - 11: ds=31 sev=purple
  - 77: ds=24 sev=-
  - 88: ds=20 sev=-
  - 66: ds=15 sev=-
  - 44: ds=13 sev=-
  - 99: ds=7 sev=-
  - 33: ds=6 sev=-
  - 00: ds=5 sev=-
- non_repeating:
  - 34: ds=72 sev=red
  - 07: ds=69 sev=red
  - 16: ds=55 sev=blue
  - 39: ds=43 sev=blue
  - 37: ds=38 sev=blue
  - 67: ds=38 sev=blue
  - 48: ds=35 sev=purple
  - 01: ds=31 sev=purple
  - 15: ds=29 sev=purple
  - 45: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:168, 34:163, 16:145, 27:100, 12:97, 14:82, 17:81, 20:70, 19:55, 33:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=168 fs=4 fl=3 hz=0.010432190760059612, 34:ds=163 fs=8 fl=4 hz=0.014423076923076924, 16:ds=145 fs=3 fl=0 hz=0.007462686567164179, 27:ds=100 fs=15 fl=2 hz=0.0189520624303233, 12:ds=97 fs=45 fl=0 hz=0.05079006772009029, 14:ds=82 fs=39 fl=0 hz=0.04276315789473684, 17:ds=81 fs=29 fl=2 hz=0.033879781420765025, 20:ds=70 fs=24 fl=3 hz=0.029315960912052113, 19:ds=55 fs=20 fl=2 hz=0.023732470334412083, 33:ds=43 fs=18 fl=2 hz=0.021119324181626188

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=79 flags=purple
- S25: ds=75 flags=purple
- S1: ds=64 flags=blue+purple
- S5: ds=62 flags=purple
- S9: ds=52 flags=purple

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
- current_index=11 streak=1 max=3 last_repeat_gap=56 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=15), P2:6 (gap=17), P3:9 (gap=41)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:9 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 184: score=50.08537142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 784: score=47.99365 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 181: score=46.08120714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 781: score=40.80462142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 189: score=40.56755 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 484: score=39.509978571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 180: score=38.9263 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 185: score=38.78072857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=38.75312857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 789: score=38.47582857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=904 sev=B
- 113: ds=855 sev=B
- 378: ds=848 sev=B
- 566: ds=837 sev=B
- 199: ds=829 sev=B
- 899: ds=807 sev=B
- 126: ds=803 sev=B
- 559: ds=798 sev=B
- 477: ds=787 sev=B
- 558: ds=753 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=233 sev=red
  - 22: ds=64 sev=purple
  - 00: ds=51 sev=purple
  - 44: ds=34 sev=purple
  - 11: ds=21 sev=-
  - 99: ds=19 sev=-
  - 88: ds=18 sev=-
  - 33: ds=16 sev=-
  - 77: ds=9 sev=-
  - 66: ds=7 sev=-
- non_repeating:
  - 36: ds=76 sev=red
  - 24: ds=60 sev=red
  - 89: ds=54 sev=blue
  - 15: ds=53 sev=blue
  - 78: ds=52 sev=blue
  - 49: ds=46 sev=blue
  - 57: ds=43 sev=blue
  - 09: ds=33 sev=purple
  - 01: ds=31 sev=purple
  - 12: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:429, 1:344, 16:195, 26:127, 17:105, 20:96, 3:75, 23:68, 33:66, 31:62

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=429 fs=0 fl=2 hz=0.005366726296958855, 1:ds=344 fs=0 fl=0 hz=0.0, 16:ds=195 fs=3 fl=1 hz=0.007853403141361256, 26:ds=127 fs=3 fl=3 hz=0.0076045627376425855, 17:ds=105 fs=13 fl=3 hz=0.018626309662398137, 20:ds=96 fs=15 fl=2 hz=0.01925254813137033, 3:ds=75 fs=15 fl=4 hz=0.02092511013215859, 23:ds=68 fs=25 fl=2 hz=0.03085714285714286, 33:ds=66 fs=27 fl=1 hz=0.030803080308030802, 31:ds=62 fs=23 fl=0 hz=0.02666666666666667

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=85 flags=purple
- S2: ds=75 flags=blue+purple
- S4: ds=73 flags=purple
- S25: ds=62 flags=purple
- S20: ds=55 flags=purple
- S9: ds=53 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:701(B); evening:803(B)
- 128 -> combined:925(B); evening:904(B)
- 333 -> combined:752(B); midday:980(B)
- 477 -> combined:709(B); evening:787(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:62(red); evening:31(purple); midday:31(purple)
- 11 -> combined:42(purple); midday:31(purple)
- 12 -> combined:39(blue); evening:31(purple)
- 15 -> combined:59(red); evening:53(blue); midday:29(purple)
- 17 -> combined:53(blue); evening:27(purple); midday:26(purple)
- 22 -> combined:127(red); evening:64(purple); midday:63(purple)
- 24 -> combined:37(blue); evening:60(red)
- 36 -> combined:31(purple); evening:76(red)
- 44 -> combined:27(purple); evening:34(purple)
- 48 -> combined:30(purple); midday:35(purple)
- 55 -> combined:83(blue); evening:233(red); midday:41(purple)
- 67 -> combined:34(purple); midday:38(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.938600000000001)[R1,Mirror-Echo], 7(5.846878571428571)[R2,XVAR-Cons(CEM)], 2(1.3690714285714285)[R2,Mirror-Echo], 4(1.1178571428571429)[R1,Double-Pressure], 6(0.6980000000000001)[R3,Mirror-Echo]
- P2: 8(7.2801285714285715)[R1,XVAR-Cons(CEM)], 7(1.4464285714285714)[R1,Double-Pressure], 6(1.2075714285714285)[R1,Double-Pressure], 9(0.964)[R2,Double-Pressure], 3(0.3512285714285714)[R3,Mirror-Echo]
- P3: 4(6.366642857142857)[R1,XVAR-Cons(CEM)], 1(2.6776142857142857)[R3,XVAR-Cons(CE)], 9(1.8488214285714286)[R1,Mirror-Echo], 0(1.2075714285714285)[R1,Double-Pressure], 5(1.062)[R2,Double-Pressure]
