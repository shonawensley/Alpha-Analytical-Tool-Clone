# Aux Summary — NewYork4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/NewYork4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: New York
- combined: live=`data/cleaned/draws/New_York_draws.csv` snap=`sharepacks/2025-12-30/NewYork4/aux/draws/New_York_draws.csv` n=1000 head=195, 321, 353, 498, 050
- midday: live=`data/cleaned/draws/New_York_Midday_draws.csv` snap=`sharepacks/2025-12-30/NewYork4/aux/draws/New_York_Midday_draws.csv` n=1000 head=321, 498, 893, 464, 783
- evening: live=`data/cleaned/draws/New_York_Evening_draws.csv` snap=`sharepacks/2025-12-30/NewYork4/aux/draws/New_York_Evening_draws.csv` n=1000 head=195, 353, 050, 114, 661

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=2 last_repeat_gap=17 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=18), P2:3 (gap=24), P3:9 (gap=43)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 939: score=47.037885357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 936: score=43.95352678571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 937: score=40.789210357142856 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 949: score=40.475804999999994 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 636: score=40.34835285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 639: score=37.48842142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 946: score=37.39144642857142 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 909: score=37.343332857142855 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 436: score=36.524321428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 439: score=36.34820714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 244: ds=976 sev=B
- 699: ds=919 sev=B
- 115: ds=837 sev=B
- 222: ds=773 sev=B
- 339: ds=754 sev=B
- 136: ds=745 sev=B
- 000: ds=744 sev=B
- 177: ds=738 sev=B
- 667: ds=706 sev=B
- 777: ds=700 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=47 sev=purple
  - 99: ds=43 sev=purple
  - 77: ds=33 sev=purple
  - 55: ds=32 sev=purple
  - 22: ds=28 sev=purple
  - 66: ds=8 sev=-
  - 44: ds=7 sev=-
  - 11: ds=6 sev=-
  - 00: ds=4 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 67: ds=59 sev=red
  - 06: ds=56 sev=red
  - 69: ds=52 sev=blue
  - 36: ds=48 sev=blue
  - 17: ds=36 sev=purple
  - 56: ds=34 sev=purple
  - 68: ds=34 sev=purple
  - 07: ds=33 sev=purple
  - 34: ds=29 sev=purple
  - 26: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:206, 35:194, 26:110, 32:95, 2:84, 17:73, 22:70, 28:64, 5:58, 23:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=206 fs=13 fl=3 hz=0.020356234096692113, 35:ds=194 fs=4 fl=3 hz=0.009138381201044387, 26:ds=110 fs=2 fl=1 hz=0.007173601147776184, 32:ds=95 fs=7 fl=3 hz=0.012515644555694618, 2:ds=84 fs=20 fl=3 hz=0.025302530253025302, 17:ds=73 fs=21 fl=1 hz=0.025669642857142856, 22:ds=70 fs=49 fl=0 hz=0.05378704720087815, 28:ds=64 fs=16 fl=3 hz=0.021788990825688075, 5:ds=58 fs=15 fl=3 hz=0.01973684210526316, 23:ds=48 fs=24 fl=2 hz=0.027368421052631577

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=72 flags=purple
- S22: ds=70 flags=purple
- S9: ds=63 flags=red+purple
- S7: ds=60 flags=purple
- S23: ds=47 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=13 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=26), P2:1 (gap=26), P3:9 (gap=21)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 939: score=47.037885357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 936: score=43.95352678571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 937: score=40.789210357142856 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 949: score=40.475804999999994 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 636: score=40.34835285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 639: score=37.48842142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 946: score=37.39144642857142 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 909: score=37.343332857142855 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 436: score=36.524321428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 439: score=36.34820714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=993 sev=B
- 337: ds=826 sev=B
- 366: ds=819 sev=B
- 044: ds=797 sev=B
- 667: ds=775 sev=B
- 189: ds=761 sev=B
- 449: ds=757 sev=B
- 456: ds=728 sev=B
- 223: ds=721 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=168 sev=red
  - 66: ds=111 sev=red
  - 55: ds=41 sev=purple
  - 33: ds=39 sev=purple
  - 88: ds=23 sev=-
  - 99: ds=21 sev=-
  - 00: ds=18 sev=-
  - 22: ds=17 sev=-
  - 77: ds=16 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 01: ds=97 sev=red
  - 27: ds=65 sev=red
  - 06: ds=51 sev=blue
  - 25: ds=50 sev=blue
  - 17: ds=36 sev=purple
  - 36: ds=35 sev=purple
  - 69: ds=34 sev=purple
  - 09: ds=31 sev=purple
  - 56: ds=29 sev=purple
  - 67: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:365, 26:337, 16:260, 18:113, 22:96, 15:85, 23:78, 27:71, 2:69, 1:67

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=365 fs=1 fl=1 hz=0.005145797598627787, 26:ds=337 fs=1 fl=0 hz=0.004081632653061225, 16:ds=260 fs=3 fl=0 hz=0.005471956224350205, 18:ds=113 fs=16 fl=2 hz=0.020524515393386546, 22:ds=96 fs=43 fl=0 hz=0.04772475027746948, 15:ds=85 fs=17 fl=2 hz=0.02134831460674157, 23:ds=78 fs=25 fl=1 hz=0.02826086956521739, 27:ds=71 fs=12 fl=2 hz=0.01728110599078341, 2:ds=69 fs=19 fl=2 hz=0.022653721682847894, 1:ds=67 fs=3 fl=2 hz=0.008075370121130552

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=82 flags=red+purple
- S25: ds=58 flags=blue+purple
- S10: ds=50 flags=purple

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
- current_index=9 streak=1 max=2 last_repeat_gap=28 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=20), P2:8 (gap=34), P3:7 (gap=36)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 939: score=47.037885357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 936: score=43.95352678571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 937: score=40.789210357142856 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 949: score=40.475804999999994 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 636: score=40.34835285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 639: score=37.48842142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 946: score=37.39144642857142 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 909: score=37.343332857142855 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 436: score=36.524321428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 439: score=36.34820714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 566: ds=972 sev=B
- 668: ds=852 sev=B
- 248: ds=846 sev=B
- 014: ds=826 sev=B
- 222: ds=810 sev=B
- 001: ds=791 sev=B
- 999: ds=781 sev=B
- 444: ds=780 sev=B
- 156: ds=755 sev=B
- 133: ds=703 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=122 sev=red
  - 44: ds=46 sev=purple
  - 99: ds=36 sev=purple
  - 88: ds=33 sev=purple
  - 55: ds=16 sev=-
  - 22: ds=14 sev=-
  - 66: ds=4 sev=-
  - 11: ds=3 sev=-
  - 00: ds=2 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 47: ds=124 sev=red
  - 48: ds=92 sev=red
  - 07: ds=81 sev=red
  - 03: ds=58 sev=red
  - 39: ds=39 sev=blue
  - 67: ds=35 sev=purple
  - 06: ds=28 sev=purple
  - 46: ds=26 sev=purple
  - 69: ds=26 sev=purple
  - 36: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:103, 34:102, 35:97, 32:80, 33:73, 10:63, 17:61, 26:55, 4:47, 2:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=103 fs=14 fl=1 hz=0.01884570082449941, 34:ds=102 fs=19 fl=0 hz=0.02242152466367713, 35:ds=97 fs=5 fl=2 hz=0.00963855421686747, 32:ds=80 fs=9 fl=1 hz=0.013095238095238096, 33:ds=73 fs=16 fl=2 hz=0.022113022113022112, 10:ds=63 fs=27 fl=1 hz=0.030335861321776812, 17:ds=61 fs=31 fl=1 hz=0.034408602150537634, 26:ds=55 fs=3 fl=4 hz=0.008879023307436182, 4:ds=47 fs=23 fl=1 hz=0.026200873362445417, 2:ds=42 fs=28 fl=1 hz=0.03456495828367104

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=63 flags=purple
- S3: ds=48 flags=purple
- S16: ds=41 flags=purple
- S25: ds=36 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [7], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '7', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 025: score=3 tags=FLT,RS
  - 079: score=3 tags=FLT,RS
  - 124: score=3 tags=FLT,RS
  - 178: score=3 tags=FLT,RS
  - 259: score=3 tags=FLT,RS
  - 268: score=3 tags=FLT,RS
  - 358: score=3 tags=FLT,RS
  - 367: score=3 tags=FLT,RS
  - 457: score=3 tags=FLT,RS
  - 016: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 001 -> evening:791(B); midday:993(B)
- 222 -> combined:773(B); evening:810(B)
- 667 -> combined:706(B); midday:775(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 06 -> combined:56(red); evening:28(purple); midday:51(blue)
- 07 -> combined:33(purple); evening:81(red)
- 17 -> combined:36(purple); midday:36(purple)
- 27 -> combined:26(purple); midday:65(red)
- 36 -> combined:48(blue); midday:35(purple)
- 55 -> combined:32(purple); midday:41(purple)
- 56 -> combined:34(purple); midday:29(purple)
- 67 -> combined:59(red); evening:35(purple); midday:29(purple)
- 69 -> combined:52(blue); evening:26(purple); midday:34(purple)
- 77 -> combined:33(purple); evening:122(red)
- 88 -> combined:47(purple); evening:33(purple)
- 99 -> combined:43(purple); evening:36(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(3.6237142857142857)[R1,XVAR-Cons(CM)], 6(1.4373571428571428)[R1,Mirror-Echo], 4(1.2971428571428572)[R1,Double-Pressure], 8(0.9834999999999999)[R2,Double-Pressure], 5(0.956)[R2,Double-Pressure]
- P2: 3(6.218478571428571)[R1,XVAR-Cons(CEM)], 4(3.5557999999999996)[R2,XVAR-Cons(CM)], 0(2.600142857142857)[R3,XVAR-Cons(CE)], 8(1.6884285714285714)[R1,Mirror-Echo], 1(1.4462857142857144)[R1,Double-Pressure]
- P3: 6(7.508699999999999)[R2,XVAR-Cons(CEM)], 9(7.332585714285714)[R1,XVAR-Cons(CEM)], 7(5.626685714285715)[R3,XVAR-Cons(CEM)]
