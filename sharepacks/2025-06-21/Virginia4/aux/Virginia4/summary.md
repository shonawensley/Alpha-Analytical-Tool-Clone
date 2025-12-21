# Aux Summary — Virginia4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/Virginia4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Virginia
- combined: live=`data/cleaned/draws/Virginia_draws.csv` snap=`sharepacks/2025-06-21/Virginia4/aux/draws/Virginia_draws.csv` n=1000 head=771, 398, 208, 681, 906
- midday: live=`data/cleaned/draws/Virginia_Midday_draws.csv` snap=`sharepacks/2025-06-21/Virginia4/aux/draws/Virginia_Midday_draws.csv` n=1000 head=398, 681, 266, 281, 130
- evening: live=`data/cleaned/draws/Virginia_Evening_draws.csv` snap=`sharepacks/2025-06-21/Virginia4/aux/draws/Virginia_Evening_draws.csv` n=1000 head=771, 208, 906, 960, 378

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=2 last_repeat_gap=82 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=22), P2:4 (gap=24), P3:9 (gap=48)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=54.91992571428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 549: score=53.65812999999999 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 547: score=49.64427678571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 559: score=46.19433571428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 555: score=45.04388714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 849: score=43.14814285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 049: score=42.251107142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 595: score=40.92377285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 505: score=40.87328714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 845: score=40.79991428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 799: ds=994 sev=B
- 222: ds=977 sev=B
- 778: ds=969 sev=B
- 666: ds=948 sev=B
- 336: ds=914 sev=B
- 111: ds=861 sev=B
- 447: ds=845 sev=B
- 228: ds=806 sev=B
- 445: ds=801 sev=B
- 117: ds=781 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=142 sev=red
  - 33: ds=64 sev=purple
  - 11: ds=50 sev=purple
  - 88: ds=34 sev=purple
  - 44: ds=32 sev=purple
  - 55: ds=24 sev=-
  - 00: ds=12 sev=-
  - 22: ds=10 sev=-
  - 66: ds=5 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 25: ds=95 sev=red
  - 48: ds=74 sev=red
  - 35: ds=59 sev=red
  - 04: ds=58 sev=red
  - 14: ds=50 sev=blue
  - 29: ds=47 sev=blue
  - 15: ds=40 sev=blue
  - 79: ds=37 sev=blue
  - 59: ds=33 sev=purple
  - 49: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:283, 26:259, 35:222, 1:128, 23:109, 15:77, 34:76, 32:68, 12:56, 14:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=283 fs=5 fl=1 hz=0.01206896551724138, 26:ds=259 fs=3 fl=1 hz=0.007352941176470588, 35:ds=222 fs=4 fl=1 hz=0.01092896174863388, 1:ds=128 fs=0 fl=0 hz=0.0032626427406199023, 23:ds=109 fs=16 fl=1 hz=0.021634615384615384, 15:ds=77 fs=21 fl=1 hz=0.024175824175824173, 34:ds=76 fs=21 fl=2 hz=0.026106696935300797, 32:ds=68 fs=3 fl=2 hz=0.007777777777777777, 12:ds=56 fs=61 fl=0 hz=0.06869369369369369, 14:ds=46 fs=45 fl=0 hz=0.04766949152542373

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=83 flags=purple
- S3: ds=71 flags=purple
- S17: ds=65 flags=red+purple
- S6: ds=50 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 048: score=3 tags=FLT,RS
  - 057: score=3 tags=FLT,RS
  - 147: score=3 tags=FLT,RS
  - 156: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 489: score=3 tags=FLT,RS
  - 579: score=3 tags=FLT,RS
  - 012: score=2 tags=RS
  - 039: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=33 streak=1 max=3 last_repeat_gap=67 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=33), P2:4 (gap=25), P3:9 (gap=32)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=54.91992571428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 549: score=53.65812999999999 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 547: score=49.64427678571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 559: score=46.19433571428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 555: score=45.04388714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 849: score=43.14814285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 049: score=42.251107142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 595: score=40.92377285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 505: score=40.87328714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 845: score=40.79991428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=943 sev=B
- 555: ds=923 sev=B
- 004: ds=903 sev=B
- 115: ds=873 sev=B
- 177: ds=870 sev=B
- 558: ds=861 sev=B
- 566: ds=860 sev=B
- 667: ds=826 sev=B
- 666: ds=817 sev=B
- 005: ds=814 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=105 sev=blue
  - 99: ds=74 sev=blue
  - 33: ds=42 sev=purple
  - 44: ds=38 sev=purple
  - 77: ds=34 sev=purple
  - 11: ds=26 sev=purple
  - 88: ds=22 sev=-
  - 00: ds=15 sev=-
  - 22: ds=7 sev=-
  - 66: ds=2 sev=-
- non_repeating:
  - 48: ds=76 sev=red
  - 09: ds=69 sev=red
  - 25: ds=47 sev=blue
  - 45: ds=46 sev=blue
  - 58: ds=45 sev=blue
  - 34: ds=37 sev=blue
  - 37: ds=36 sev=purple
  - 04: ds=31 sev=purple
  - 15: ds=29 sev=purple
  - 35: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:319, 1:263, 35:185, 16:141, 26:129, 34:100, 5:69, 29:55, 23:54, 15:38

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=319 fs=2 fl=2 hz=0.007352941176470588, 1:ds=263 fs=1 fl=1 hz=0.005154639175257732, 35:ds=185 fs=2 fl=1 hz=0.00782472613458529, 16:ds=141 fs=5 fl=3 hz=0.010575793184488836, 26:ds=129 fs=5 fl=1 hz=0.01038961038961039, 34:ds=100 fs=20 fl=2 hz=0.024858757062146894, 5:ds=69 fs=22 fl=2 hz=0.02877697841726619, 29:ds=55 fs=25 fl=2 hz=0.029379760609357996, 23:ds=54 fs=20 fl=2 hz=0.024498886414253896, 15:ds=38 fs=17 fl=4 hz=0.0219435736677116

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=61 flags=purple
- S2: ds=41 flags=purple
- S3: ds=35 flags=purple
- S17: ds=32 flags=purple
- S6: ds=31 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=2 last_repeat_gap=3 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=25), P2:3 (gap=30), P3:9 (gap=24)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=54.91992571428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 549: score=53.65812999999999 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 547: score=49.64427678571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 559: score=46.19433571428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 555: score=45.04388714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 849: score=43.14814285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 049: score=42.251107142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 595: score=40.92377285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 505: score=40.87328714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 845: score=40.79991428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=879 sev=B
- 277: ds=856 sev=B
- 133: ds=848 sev=B
- 002: ds=784 sev=B
- 111: ds=769 sev=B
- 006: ds=700 sev=B
- 199: ds=671 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=71 sev=blue
  - 33: ds=32 sev=purple
  - 11: ds=25 sev=purple
  - 66: ds=19 sev=-
  - 88: ds=17 sev=-
  - 44: ds=16 sev=-
  - 55: ds=12 sev=-
  - 00: ds=6 sev=-
  - 22: ds=5 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 25: ds=74 sev=red
  - 29: ds=55 sev=blue
  - 19: ds=49 sev=blue
  - 01: ds=40 sev=blue
  - 18: ds=40 sev=blue
  - 49: ds=38 sev=blue
  - 48: ds=37 sev=blue
  - 12: ds=31 sev=purple
  - 35: ds=30 sev=purple
  - 04: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:856, 23:334, 16:156, 3:152, 35:111, 25:101, 15:67, 1:64, 31:46, 17:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=856 fs=0 fl=0 hz=0.0, 23:ds=334 fs=17 fl=1 hz=0.02889245585874799, 16:ds=156 fs=4 fl=0 hz=0.010121457489878543, 3:ds=152 fs=17 fl=2 hz=0.02676056338028169, 35:ds=111 fs=1 fl=0 hz=0.004629629629629629, 25:ds=101 fs=13 fl=3 hz=0.017957351290684626, 15:ds=67 fs=23 fl=1 hz=0.0273972602739726, 1:ds=64 fs=5 fl=0 hz=0.007692307692307693, 31:ds=46 fs=25 fl=2 hz=0.028391167192429023, 17:ds=43 fs=19 fl=2 hz=0.02224576271186441

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 047: score=3 tags=FLT,RS
  - 056: score=3 tags=FLT,RS
  - 146: score=3 tags=FLT,RS
  - 245: score=3 tags=FLT,RS
  - 479: score=3 tags=FLT,RS
  - 569: score=3 tags=FLT,RS
  - 578: score=3 tags=FLT,RS
  - 029: score=2 tags=RS
  - 038: score=2 tags=RS
  - 128: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 006 -> combined:719(B); evening:700(B)
- 111 -> combined:861(B); evening:769(B)
- 115 -> combined:696(B); midday:873(B)
- 133 -> evening:848(B); midday:943(B)
- 666 -> combined:948(B); midday:817(B)
- 799 -> combined:994(B); midday:681(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 04 -> combined:58(red); evening:29(purple); midday:31(purple)
- 11 -> combined:50(purple); evening:25(purple); midday:26(purple)
- 14 -> combined:50(blue); evening:25(purple); midday:25(purple)
- 15 -> combined:40(blue); midday:29(purple)
- 25 -> combined:95(red); evening:74(red); midday:47(blue)
- 29 -> combined:47(blue); evening:55(blue)
- 33 -> combined:64(purple); evening:32(purple); midday:42(purple)
- 35 -> combined:59(red); evening:30(purple); midday:29(purple)
- 44 -> combined:32(purple); midday:38(purple)
- 48 -> combined:74(red); evening:37(blue); midday:76(red)
- 49 -> combined:25(purple); evening:38(blue)
- 59 -> combined:33(purple); evening:28(purple)
- 79 -> combined:37(blue); evening:28(purple)
- 99 -> combined:142(red); evening:71(blue); midday:74(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(6.813757142857144)[R1,Mirror-Echo], 8(3.2157)[R2,XVAR-Cons(CE)], 0(2.3186642857142856)[R3,Mirror-Echo], 7(1.5852857142857142)[R1,Double-Pressure], 1(0.8464285714285715)[R1,Swap]
- P2: 4(7.190442857142857)[R1,XVAR-Cons(CEM)], 5(2.8741000000000003)[R2,XVAR-Cons(CM)], 3(1.5657142857142856)[R1,Double-Pressure], 9(1.2539857142857143)[R2,Mirror-Echo], 0(1.2035)[R2,Mirror-Echo]
- P3: 9(8.741999999999999)[R1,XVAR-Cons(CEM)], 5(6.393771428571428)[R2,XVAR-Cons(CEM)], 7(5.251692857142857)[R3,XVAR-Cons(CEM)]
