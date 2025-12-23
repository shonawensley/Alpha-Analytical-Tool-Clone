# Aux Summary — Virginia4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/Virginia4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Virginia
- combined: live=`data/cleaned/draws/Virginia_draws.csv` snap=`sharepacks/2025-06-23/Virginia4/aux/draws/Virginia_draws.csv` n=1000 head=938, 793, 016, 473, 771
- midday: live=`data/cleaned/draws/Virginia_Midday_draws.csv` snap=`sharepacks/2025-06-23/Virginia4/aux/draws/Virginia_Midday_draws.csv` n=1000 head=793, 473, 398, 681, 266
- evening: live=`data/cleaned/draws/Virginia_Evening_draws.csv` snap=`sharepacks/2025-06-23/Virginia4/aux/draws/Virginia_Evening_draws.csv` n=1000 head=938, 016, 771, 208, 906

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=33 streak=1 max=2 last_repeat_gap=86 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=26), P2:4 (gap=28), P3:9 (gap=52)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=56.88756321428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 549: score=55.42271464285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 555: score=54.159459285714284 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 849: score=53.064211428571426 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 559: score=52.694610714285716 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 845: score=50.40657785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 547: score=49.88654785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 859: score=47.227050000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 557: score=47.15844392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 855: score=44.916064285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 799: ds=998 sev=B
- 222: ds=981 sev=B
- 778: ds=973 sev=B
- 666: ds=952 sev=B
- 336: ds=918 sev=B
- 111: ds=865 sev=B
- 447: ds=849 sev=B
- 228: ds=810 sev=B
- 445: ds=805 sev=B
- 117: ds=785 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=146 sev=red
  - 33: ds=68 sev=purple
  - 11: ds=54 sev=purple
  - 88: ds=38 sev=purple
  - 44: ds=36 sev=purple
  - 55: ds=28 sev=purple
  - 00: ds=16 sev=-
  - 22: ds=14 sev=-
  - 66: ds=9 sev=-
  - 77: ds=4 sev=-
- non_repeating:
  - 25: ds=99 sev=red
  - 48: ds=78 sev=red
  - 35: ds=63 sev=red
  - 04: ds=62 sev=red
  - 14: ds=54 sev=blue
  - 29: ds=51 sev=blue
  - 15: ds=44 sev=blue
  - 59: ds=37 sev=blue
  - 49: ds=29 sev=purple
  - 45: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:287, 26:263, 35:226, 1:132, 23:113, 15:81, 34:80, 32:72, 12:60, 14:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=287 fs=5 fl=1 hz=0.01206896551724138, 26:ds=263 fs=3 fl=1 hz=0.007352941176470588, 35:ds=226 fs=4 fl=1 hz=0.01092896174863388, 1:ds=132 fs=0 fl=0 hz=0.0032626427406199023, 23:ds=113 fs=16 fl=1 hz=0.021634615384615384, 15:ds=81 fs=21 fl=1 hz=0.024175824175824173, 34:ds=80 fs=21 fl=2 hz=0.026106696935300797, 32:ds=72 fs=3 fl=2 hz=0.007777777777777777, 12:ds=60 fs=61 fl=0 hz=0.06869369369369369, 14:ds=50 fs=45 fl=0 hz=0.04766949152542373

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=87 flags=purple
- S3: ds=75 flags=purple
- S17: ds=69 flags=red+purple
- S6: ds=54 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 057: score=4 tags=FLT,MIR,RS
  - 156: score=4 tags=FLT,MIR,RS
  - 237: score=4 tags=FLT,MIR,RS
  - 012: score=3 tags=FLT,RS
  - 129: score=3 tags=FLT,RS
  - 138: score=3 tags=MIR,RS
  - 246: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 489: score=3 tags=MIR,RS
  - 579: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=2 max=3 last_repeat_gap=1 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=22), P2:4 (gap=27), P3:9 (gap=34)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=56.88756321428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 549: score=55.42271464285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 555: score=54.159459285714284 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 849: score=53.064211428571426 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 559: score=52.694610714285716 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 845: score=50.40657785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 547: score=49.88654785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 859: score=47.227050000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 557: score=47.15844392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 855: score=44.916064285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=945 sev=B
- 555: ds=925 sev=B
- 004: ds=905 sev=B
- 115: ds=875 sev=B
- 177: ds=872 sev=B
- 558: ds=863 sev=B
- 566: ds=862 sev=B
- 667: ds=828 sev=B
- 666: ds=819 sev=B
- 005: ds=816 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=107 sev=red
  - 99: ds=76 sev=blue
  - 33: ds=44 sev=purple
  - 44: ds=40 sev=purple
  - 77: ds=36 sev=purple
  - 11: ds=28 sev=purple
  - 88: ds=24 sev=-
  - 00: ds=17 sev=-
  - 22: ds=9 sev=-
  - 66: ds=4 sev=-
- non_repeating:
  - 48: ds=78 sev=red
  - 09: ds=71 sev=red
  - 25: ds=49 sev=blue
  - 45: ds=48 sev=blue
  - 58: ds=47 sev=blue
  - 04: ds=33 sev=purple
  - 15: ds=31 sev=purple
  - 35: ds=31 sev=purple
  - 14: ds=27 sev=purple
  - 24: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:321, 1:265, 35:187, 16:143, 26:131, 34:102, 5:71, 29:57, 23:56, 15:40

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=321 fs=2 fl=1 hz=0.007017543859649123, 1:ds=265 fs=1 fl=1 hz=0.005154639175257732, 35:ds=187 fs=2 fl=1 hz=0.00782472613458529, 16:ds=143 fs=5 fl=3 hz=0.010575793184488836, 26:ds=131 fs=5 fl=1 hz=0.01038961038961039, 34:ds=102 fs=20 fl=2 hz=0.024858757062146894, 5:ds=71 fs=22 fl=2 hz=0.02877697841726619, 29:ds=57 fs=25 fl=2 hz=0.029379760609357996, 23:ds=56 fs=20 fl=2 hz=0.024498886414253896, 15:ds=40 fs=17 fl=4 hz=0.0219435736677116

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=63 flags=purple
- S2: ds=43 flags=purple
- S3: ds=37 flags=purple
- S17: ds=34 flags=purple
- S6: ds=33 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 027: score=3 tags=FLT,RS
  - 036: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 567: score=3 tags=FLT,RS
  - 126: score=2 tags=RS
  - 189: score=2 tags=RS
  - 234: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=33 streak=1 max=2 last_repeat_gap=5 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=27), P2:9 (gap=25), P3:9 (gap=26)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=56.88756321428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 549: score=55.42271464285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 555: score=54.159459285714284 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 849: score=53.064211428571426 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 559: score=52.694610714285716 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 845: score=50.40657785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 547: score=49.88654785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 859: score=47.227050000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 557: score=47.15844392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 855: score=44.916064285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=881 sev=B
- 277: ds=858 sev=B
- 133: ds=850 sev=B
- 002: ds=786 sev=B
- 111: ds=771 sev=B
- 006: ds=702 sev=B
- 199: ds=673 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=73 sev=blue
  - 33: ds=34 sev=purple
  - 11: ds=27 sev=purple
  - 66: ds=21 sev=-
  - 88: ds=19 sev=-
  - 44: ds=18 sev=-
  - 55: ds=14 sev=-
  - 00: ds=8 sev=-
  - 22: ds=7 sev=-
  - 77: ds=2 sev=-
- non_repeating:
  - 25: ds=76 sev=red
  - 29: ds=57 sev=red
  - 19: ds=51 sev=blue
  - 18: ds=42 sev=blue
  - 49: ds=40 sev=blue
  - 48: ds=39 sev=blue
  - 12: ds=33 sev=purple
  - 35: ds=32 sev=purple
  - 04: ds=31 sev=purple
  - 59: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:858, 23:336, 16:158, 3:154, 35:113, 25:103, 15:69, 1:66, 31:48, 17:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=858 fs=0 fl=0 hz=0.0, 23:ds=336 fs=17 fl=1 hz=0.02889245585874799, 16:ds=158 fs=4 fl=0 hz=0.010121457489878543, 3:ds=154 fs=17 fl=2 hz=0.02676056338028169, 35:ds=113 fs=1 fl=0 hz=0.004629629629629629, 25:ds=103 fs=13 fl=3 hz=0.017957351290684626, 15:ds=69 fs=23 fl=1 hz=0.0273972602739726, 1:ds=66 fs=5 fl=0 hz=0.007692307692307693, 31:ds=48 fs=25 fl=2 hz=0.028391167192429023, 17:ds=45 fs=19 fl=2 hz=0.02224576271186441

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
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 006 -> combined:723(B); evening:702(B)
- 111 -> combined:865(B); evening:771(B)
- 115 -> combined:700(B); midday:875(B)
- 133 -> evening:850(B); midday:945(B)
- 666 -> combined:952(B); midday:819(B)
- 799 -> combined:998(B); midday:683(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 04 -> combined:62(red); evening:31(purple); midday:33(purple)
- 11 -> combined:54(purple); evening:27(purple); midday:28(purple)
- 14 -> combined:54(blue); evening:27(purple); midday:27(purple)
- 15 -> combined:44(blue); midday:31(purple)
- 25 -> combined:99(red); evening:76(red); midday:49(blue)
- 29 -> combined:51(blue); evening:57(red); midday:25(purple)
- 33 -> combined:68(purple); evening:34(purple); midday:44(purple)
- 35 -> combined:63(red); evening:32(purple); midday:31(purple)
- 44 -> combined:36(purple); midday:40(purple)
- 45 -> combined:28(purple); midday:48(blue)
- 48 -> combined:78(red); evening:39(blue); midday:78(red)
- 49 -> combined:29(purple); evening:40(blue)
- 55 -> combined:28(purple); midday:107(red)
- 58 -> combined:26(purple); midday:47(blue)
- 59 -> combined:37(blue); evening:30(purple)
- 99 -> combined:146(red); evening:73(blue); midday:76(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(7.191164285714287)[R1,XVAR-Cons(CEM)], 8(6.009857142857143)[R2,XVAR-Cons(CEM)], 1(2.29)[R3,XVAR-Cons(CE)], 0(1.2820714285714285)[R2,Mirror-Echo]
- P2: 4(8.228028571428572)[R1,XVAR-Cons(CEM)], 5(5.855764285714286)[R2,XVAR-Cons(CEM)], 9(1.5794285714285714)[R1,Mirror-Echo], 0(1.2275142857142856)[R2,Mirror-Echo], 2(0.268)[R3,Swap]
- P3: 9(8.861428571428572)[R1,XVAR-Cons(CEM)], 5(6.5504428571428575)[R2,XVAR-Cons(CEM)], 7(4.916935714285715)[R3,XVAR-Cons(CEM)]
