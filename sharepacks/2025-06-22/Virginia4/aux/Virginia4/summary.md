# Aux Summary — Virginia4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/Virginia4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Virginia
- combined: live=`data/cleaned/draws/Virginia_draws.csv` snap=`sharepacks/2025-06-22/Virginia4/aux/draws/Virginia_draws.csv` n=1000 head=016, 473, 771, 398, 208
- midday: live=`data/cleaned/draws/Virginia_Midday_draws.csv` snap=`sharepacks/2025-06-22/Virginia4/aux/draws/Virginia_Midday_draws.csv` n=1000 head=473, 398, 681, 266, 281
- evening: live=`data/cleaned/draws/Virginia_Evening_draws.csv` snap=`sharepacks/2025-06-22/Virginia4/aux/draws/Virginia_Evening_draws.csv` n=1000 head=016, 771, 208, 906, 960

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=6 streak=1 max=2 last_repeat_gap=84 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=24), P2:4 (gap=26), P3:9 (gap=50)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=55.20443785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 549: score=53.88987964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 547: score=50.040369642857144 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 559: score=46.37006392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 555: score=45.24666357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 849: score=43.38840714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=41.33966428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 595: score=41.086620714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 845: score=41.0588 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 505: score=41.006135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 799: ds=996 sev=B
- 222: ds=979 sev=B
- 778: ds=971 sev=B
- 666: ds=950 sev=B
- 336: ds=916 sev=B
- 111: ds=863 sev=B
- 447: ds=847 sev=B
- 228: ds=808 sev=B
- 445: ds=803 sev=B
- 117: ds=783 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=144 sev=red
  - 33: ds=66 sev=purple
  - 11: ds=52 sev=purple
  - 88: ds=36 sev=purple
  - 44: ds=34 sev=purple
  - 55: ds=26 sev=purple
  - 00: ds=14 sev=-
  - 22: ds=12 sev=-
  - 66: ds=7 sev=-
  - 77: ds=2 sev=-
- non_repeating:
  - 25: ds=97 sev=red
  - 48: ds=76 sev=red
  - 35: ds=61 sev=red
  - 04: ds=60 sev=red
  - 14: ds=52 sev=blue
  - 29: ds=49 sev=blue
  - 15: ds=42 sev=blue
  - 79: ds=39 sev=blue
  - 59: ds=35 sev=purple
  - 49: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:285, 26:261, 35:224, 1:130, 23:111, 15:79, 34:78, 32:70, 12:58, 14:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=285 fs=5 fl=1 hz=0.01206896551724138, 26:ds=261 fs=3 fl=1 hz=0.007352941176470588, 35:ds=224 fs=4 fl=1 hz=0.01092896174863388, 1:ds=130 fs=0 fl=0 hz=0.0032626427406199023, 23:ds=111 fs=16 fl=1 hz=0.021634615384615384, 15:ds=79 fs=21 fl=1 hz=0.024175824175824173, 34:ds=78 fs=21 fl=2 hz=0.026106696935300797, 32:ds=70 fs=3 fl=2 hz=0.007777777777777777, 12:ds=58 fs=61 fl=0 hz=0.06869369369369369, 14:ds=48 fs=45 fl=0 hz=0.04766949152542373

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=85 flags=purple
- S3: ds=73 flags=purple
- S17: ds=67 flags=red+purple
- S6: ds=52 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 057: score=4 tags=FLT,MIR,RS
  - 156: score=4 tags=FLT,MIR,RS
  - 138: score=3 tags=MIR,RS
  - 237: score=3 tags=MIR,RS
  - 345: score=3 tags=FLT,RS
  - 489: score=3 tags=MIR,RS
  - 579: score=3 tags=FLT,RS
  - 012: score=2 tags=RS
  - 015: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=68 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=34), P2:4 (gap=26), P3:9 (gap=33)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=55.20443785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 549: score=53.88987964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 547: score=50.040369642857144 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 559: score=46.37006392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 555: score=45.24666357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 849: score=43.38840714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=41.33966428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 595: score=41.086620714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 845: score=41.0588 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 505: score=41.006135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=944 sev=B
- 555: ds=924 sev=B
- 004: ds=904 sev=B
- 115: ds=874 sev=B
- 177: ds=871 sev=B
- 558: ds=862 sev=B
- 566: ds=861 sev=B
- 667: ds=827 sev=B
- 666: ds=818 sev=B
- 005: ds=815 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=106 sev=blue
  - 99: ds=75 sev=blue
  - 33: ds=43 sev=purple
  - 44: ds=39 sev=purple
  - 77: ds=35 sev=purple
  - 11: ds=27 sev=purple
  - 88: ds=23 sev=-
  - 00: ds=16 sev=-
  - 22: ds=8 sev=-
  - 66: ds=3 sev=-
- non_repeating:
  - 48: ds=77 sev=red
  - 09: ds=70 sev=red
  - 25: ds=48 sev=blue
  - 45: ds=47 sev=blue
  - 58: ds=46 sev=blue
  - 04: ds=32 sev=purple
  - 15: ds=30 sev=purple
  - 35: ds=30 sev=purple
  - 14: ds=26 sev=purple
  - 24: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:320, 1:264, 35:186, 16:142, 26:130, 34:101, 5:70, 29:56, 23:55, 15:39

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=320 fs=2 fl=1 hz=0.007017543859649123, 1:ds=264 fs=1 fl=1 hz=0.005154639175257732, 35:ds=186 fs=2 fl=1 hz=0.00782472613458529, 16:ds=142 fs=5 fl=3 hz=0.010575793184488836, 26:ds=130 fs=5 fl=1 hz=0.01038961038961039, 34:ds=101 fs=20 fl=2 hz=0.024858757062146894, 5:ds=70 fs=22 fl=2 hz=0.02877697841726619, 29:ds=56 fs=25 fl=2 hz=0.029379760609357996, 23:ds=55 fs=20 fl=2 hz=0.024498886414253896, 15:ds=39 fs=17 fl=4 hz=0.0219435736677116

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=62 flags=purple
- S2: ds=42 flags=purple
- S3: ds=36 flags=purple
- S17: ds=33 flags=purple
- S6: ds=32 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=6 streak=1 max=2 last_repeat_gap=4 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=26), P2:3 (gap=31), P3:9 (gap=25)
- consensus_notes: P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=55.20443785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 549: score=53.88987964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 547: score=50.040369642857144 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 559: score=46.37006392857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 555: score=45.24666357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 849: score=43.38840714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=41.33966428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 595: score=41.086620714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 845: score=41.0588 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 505: score=41.006135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 777: ds=880 sev=B
- 277: ds=857 sev=B
- 133: ds=849 sev=B
- 002: ds=785 sev=B
- 111: ds=770 sev=B
- 006: ds=701 sev=B
- 199: ds=672 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=72 sev=blue
  - 33: ds=33 sev=purple
  - 11: ds=26 sev=purple
  - 66: ds=20 sev=-
  - 88: ds=18 sev=-
  - 44: ds=17 sev=-
  - 55: ds=13 sev=-
  - 00: ds=7 sev=-
  - 22: ds=6 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 25: ds=75 sev=red
  - 29: ds=56 sev=red
  - 19: ds=50 sev=blue
  - 18: ds=41 sev=blue
  - 49: ds=39 sev=blue
  - 48: ds=38 sev=blue
  - 12: ds=32 sev=purple
  - 35: ds=31 sev=purple
  - 04: ds=30 sev=purple
  - 59: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:857, 23:335, 16:157, 3:153, 35:112, 25:102, 15:68, 1:65, 31:47, 17:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=857 fs=0 fl=0 hz=0.0, 23:ds=335 fs=17 fl=1 hz=0.02889245585874799, 16:ds=157 fs=4 fl=0 hz=0.010121457489878543, 3:ds=153 fs=17 fl=2 hz=0.02676056338028169, 35:ds=112 fs=1 fl=0 hz=0.004629629629629629, 25:ds=102 fs=13 fl=3 hz=0.017957351290684626, 15:ds=68 fs=23 fl=1 hz=0.0273972602739726, 1:ds=65 fs=5 fl=0 hz=0.007692307692307693, 31:ds=47 fs=25 fl=2 hz=0.028391167192429023, 17:ds=44 fs=19 fl=2 hz=0.02224576271186441

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
- score=3 triggers={'mirror': True, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=4 tags=FLT,MIR,RS
  - 056: score=4 tags=FLT,MIR,RS
  - 146: score=4 tags=FLT,MIR,RS
  - 389: score=4 tags=FLT,MIR,RS
  - 479: score=4 tags=FLT,MIR,RS
  - 047: score=3 tags=FLT,RS
  - 137: score=3 tags=FLT,RS
  - 236: score=3 tags=FLT,RS
  - 245: score=3 tags=FLT,RS
  - 569: score=3 tags=FLT,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 006 -> combined:721(B); evening:701(B)
- 111 -> combined:863(B); evening:770(B)
- 115 -> combined:698(B); midday:874(B)
- 133 -> evening:849(B); midday:944(B)
- 666 -> combined:950(B); midday:818(B)
- 799 -> combined:996(B); midday:682(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 04 -> combined:60(red); evening:30(purple); midday:32(purple)
- 11 -> combined:52(purple); evening:26(purple); midday:27(purple)
- 14 -> combined:52(blue); evening:26(purple); midday:26(purple)
- 15 -> combined:42(blue); midday:30(purple)
- 25 -> combined:97(red); evening:75(red); midday:48(blue)
- 29 -> combined:49(blue); evening:56(red)
- 33 -> combined:66(purple); evening:33(purple); midday:43(purple)
- 35 -> combined:61(red); evening:31(purple); midday:30(purple)
- 44 -> combined:34(purple); midday:39(purple)
- 45 -> combined:26(purple); midday:47(blue)
- 48 -> combined:76(red); evening:38(blue); midday:77(red)
- 49 -> combined:27(purple); evening:39(blue)
- 55 -> combined:26(purple); midday:106(blue)
- 59 -> combined:35(purple); evening:29(purple)
- 79 -> combined:39(blue); evening:29(purple)
- 99 -> combined:144(red); evening:72(blue); midday:75(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(6.839914285714286)[R1,XVAR-Cons(CEM)], 8(3.2805999999999997)[R2,XVAR-Cons(CE)], 1(2.2318571428571428)[R3,XVAR-Cons(CE)], 7(1.685142857142857)[R1,Double-Pressure], 0(0.4576)[R3,Mirror-Echo]
- P2: 4(7.306092857142858)[R1,XVAR-Cons(CEM)], 5(2.9410357142857144)[R2,XVAR-Cons(CM)], 3(1.5955714285714284)[R1,Double-Pressure], 9(1.280992857142857)[R2,Mirror-Echo], 0(1.2005071428571428)[R2,Mirror-Echo]
- P3: 9(8.801714285714286)[R1,XVAR-Cons(CEM)], 5(6.472107142857143)[R2,XVAR-Cons(CEM)], 7(5.454314285714285)[R3,XVAR-Cons(CEM)]
