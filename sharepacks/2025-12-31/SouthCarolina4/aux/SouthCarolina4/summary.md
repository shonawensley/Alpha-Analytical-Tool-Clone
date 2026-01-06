# Aux Summary — SouthCarolina4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/SouthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: South Carolina
- combined: live=`data/cleaned/draws/South_Carolina_draws.csv` snap=`sharepacks/2025-12-31/SouthCarolina4/aux/draws/South_Carolina_draws.csv` n=1000 head=976, 754, 463, 425, 849
- midday: live=`data/cleaned/draws/South_Carolina_Midday_draws.csv` snap=`sharepacks/2025-12-31/SouthCarolina4/aux/draws/South_Carolina_Midday_draws.csv` n=1000 head=754, 425, 462, 144, 528
- evening: live=`data/cleaned/draws/South_Carolina_Evening_draws.csv` snap=`sharepacks/2025-12-31/SouthCarolina4/aux/draws/South_Carolina_Evening_draws.csv` n=1000 head=976, 463, 849, 257, 240

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=11 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=26), P2:3 (gap=27), P3:1 (gap=13)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 631: score=44.17877142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 031: score=43.994257142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 638: score=43.9405 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 038: score=43.755985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 030: score=43.55115857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 681: score=43.08801428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 081: score=42.9035 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 688: score=42.84974285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 088: score=42.66522857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 080: score=42.46040142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 225: ds=997 sev=B
- 233: ds=994 sev=B
- 366: ds=966 sev=B
- 449: ds=895 sev=B
- 156: ds=878 sev=B
- 778: ds=848 sev=B
- 279: ds=847 sev=B
- 033: ds=779 sev=B
- 004: ds=767 sev=B
- 688: ds=734 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=175 sev=red
  - 55: ds=112 sev=red
  - 77: ds=96 sev=blue
  - 33: ds=83 sev=blue
  - 88: ds=78 sev=blue
  - 22: ds=58 sev=purple
  - 66: ds=46 sev=purple
  - 00: ds=19 sev=-
  - 11: ds=15 sev=-
  - 44: ds=8 sev=-
- non_repeating:
  - 35: ds=104 sev=red
  - 15: ds=54 sev=blue
  - 18: ds=52 sev=blue
  - 78: ds=47 sev=blue
  - 05: ds=43 sev=blue
  - 68: ds=35 sev=purple
  - 29: ds=28 sev=purple
  - 09: ds=23 sev=-
  - 06: ds=21 sev=-
  - 16: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:439, 35:382, 1:163, 26:151, 31:113, 4:104, 23:102, 28:96, 15:86, 27:79

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=439 fs=0 fl=0 hz=0.002197802197802198, 35:ds=382 fs=0 fl=0 hz=0.001949317738791423, 1:ds=163 fs=6 fl=4 hz=0.012195121951219513, 26:ds=151 fs=2 fl=0 hz=0.0062402496099844, 31:ds=113 fs=28 fl=0 hz=0.03160270880361174, 4:ds=104 fs=21 fl=2 hz=0.026589595375722544, 23:ds=102 fs=25 fl=1 hz=0.029850746268656716, 28:ds=96 fs=16 fl=2 hz=0.021479713603818614, 15:ds=86 fs=14 fl=3 hz=0.020506634499396863, 27:ds=79 fs=26 fl=0 hz=0.02911534154535274

### Sums (source: aux_validation.sums_stats_by_variant)
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=88 flags=red+purple
- S8: ds=62 flags=red+purple
- S0: ds=61 flags=blue+purple
- S23: ds=50 flags=blue+purple
- S5: ds=49 flags=purple
- S24: ds=47 flags=blue+purple
- S4: ds=39 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 017: score=3 tags=FLT,RS
  - 026: score=3 tags=FLT,RS
  - 035: score=3 tags=FLT,RS
  - 089: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 179: score=3 tags=FLT,RS
  - 269: score=2 tags=RS
  - 278: score=2 tags=RS
  - 359: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=2 max=3 last_repeat_gap=1 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=28), P2:3 (gap=37), P3:9 (gap=22)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 631: score=44.17877142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 031: score=43.994257142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 638: score=43.9405 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 038: score=43.755985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 030: score=43.55115857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 681: score=43.08801428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 081: score=42.9035 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 688: score=42.84974285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 088: score=42.66522857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 080: score=42.46040142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 277: ds=875 sev=B
- 555: ds=870 sev=B
- 222: ds=847 sev=B
- 337: ds=824 sev=B
- 003: ds=815 sev=B
- 228: ds=806 sev=B
- 556: ds=708 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=110 sev=red
  - 55: ds=74 sev=blue
  - 77: ds=43 sev=purple
  - 33: ds=37 sev=purple
  - 88: ds=35 sev=purple
  - 22: ds=33 sev=purple
  - 66: ds=20 sev=-
  - 00: ds=11 sev=-
  - 11: ds=6 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 49: ds=51 sev=blue
  - 35: ds=47 sev=blue
  - 67: ds=45 sev=blue
  - 34: ds=44 sev=blue
  - 09: ds=41 sev=blue
  - 27: ds=38 sev=blue
  - 07: ds=29 sev=purple
  - 05: ds=26 sev=purple
  - 36: ds=25 sev=purple
  - 15: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:411, 26:189, 35:175, 27:140, 6:108, 5:77, 1:74, 15:69, 34:55, 31:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=411 fs=1 fl=2 hz=0.006993006993006993, 26:ds=189 fs=1 fl=1 hz=0.0058309037900874635, 35:ds=175 fs=1 fl=1 hz=0.004968944099378882, 27:ds=140 fs=18 fl=3 hz=0.026582278481012658, 6:ds=108 fs=24 fl=2 hz=0.02957906712172924, 5:ds=77 fs=20 fl=1 hz=0.023102310231023104, 1:ds=74 fs=7 fl=3 hz=0.012127894156560088, 15:ds=69 fs=17 fl=3 hz=0.021691973969631236, 34:ds=55 fs=28 fl=1 hz=0.03159041394335512, 31:ds=51 fs=33 fl=0 hz=0.035752979414951244

### Sums (source: aux_validation.sums_stats_by_variant)
- S3: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=78 flags=purple
- S25: ds=75 flags=purple
- S21: ds=55 flags=purple
- S20: ds=51 flags=purple
- S17: ds=49 flags=purple
- S8: ds=47 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=3 tags=FLT,RS
  - 026: score=3 tags=FLT,RS
  - 035: score=3 tags=FLT,RS
  - 089: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 179: score=3 tags=FLT,RS
  - 269: score=3 tags=FLT,RS
  - 359: score=3 tags=FLT,RS
  - 368: score=3 tags=FLT,RS
  - 125: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=28 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=23), P2:8 (gap=18), P3:1 (gap=21)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 631: score=44.17877142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 031: score=43.994257142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 638: score=43.9405 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 038: score=43.755985714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 030: score=43.55115857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 681: score=43.08801428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 081: score=42.9035 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 688: score=42.84974285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 088: score=42.66522857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 080: score=42.46040142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=978 sev=B
- 117: ds=889 sev=B
- 005: ds=875 sev=B
- 577: ds=852 sev=B
- 155: ds=832 sev=B
- 777: ds=831 sev=B
- 669: ds=823 sev=B
- 179: ds=805 sev=B
- 366: ds=771 sev=B
- 222: ds=765 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=95 sev=blue
  - 77: ds=82 sev=blue
  - 66: ds=74 sev=blue
  - 33: ds=70 sev=purple
  - 55: ds=61 sev=purple
  - 88: ds=55 sev=purple
  - 22: ds=32 sev=purple
  - 11: ds=21 sev=-
  - 44: ds=20 sev=-
  - 00: ds=11 sev=-
- non_repeating:
  - 58: ds=96 sev=red
  - 35: ds=63 sev=red
  - 29: ds=58 sev=red
  - 47: ds=48 sev=blue
  - 15: ds=44 sev=blue
  - 18: ds=30 sev=purple
  - 19: ds=30 sev=purple
  - 78: ds=26 sev=purple
  - 05: ds=24 sev=-
  - 08: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:483, 1:270, 32:237, 31:216, 4:136, 28:109, 19:105, 23:100, 26:82, 16:78

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=483 fs=3 fl=1 hz=0.017391304347826087, 1:ds=270 fs=1 fl=0 hz=0.0049586776859504135, 32:ds=237 fs=1 fl=1 hz=0.0058997050147492625, 31:ds=216 fs=16 fl=1 hz=0.021935483870967745, 4:ds=136 fs=21 fl=3 hz=0.028742514970059883, 28:ds=109 fs=10 fl=4 hz=0.017676767676767676, 19:ds=105 fs=12 fl=2 hz=0.016968325791855206, 23:ds=100 fs=24 fl=0 hz=0.02937576499388005, 26:ds=82 fs=0 fl=0 hz=0.002347417840375587, 16:ds=78 fs=6 fl=4 hz=0.011820330969267141

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S19: ds=61 flags=purple
- S15: ds=52 flags=red+purple
- S9: ds=49 flags=purple
- S17: ds=48 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 179: score=3 tags=FLT,RS
  - 026: score=2 tags=RS
  - 035: score=2 tags=RS
  - 089: score=2 tags=RS
  - 269: score=2 tags=RS
  - 278: score=2 tags=RS
  - 359: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 222 -> evening:765(B); midday:847(B)
- 366 -> combined:966(B); evening:771(B)
- 688 -> combined:734(B); evening:730(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:43(blue); midday:26(purple)
- 15 -> combined:54(blue); evening:44(blue)
- 18 -> combined:52(blue); evening:30(purple)
- 22 -> combined:58(purple); evening:32(purple); midday:33(purple)
- 29 -> combined:28(purple); evening:58(red)
- 33 -> combined:83(blue); evening:70(purple); midday:37(purple)
- 35 -> combined:104(red); evening:63(red); midday:47(blue)
- 55 -> combined:112(red); evening:61(purple); midday:74(blue)
- 66 -> combined:46(purple); evening:74(blue)
- 77 -> combined:96(blue); evening:82(blue); midday:43(purple)
- 78 -> combined:47(blue); evening:26(purple)
- 88 -> combined:78(blue); evening:55(purple); midday:35(purple)
- 99 -> combined:175(red); evening:95(blue); midday:110(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(7.006878571428571)[R2,XVAR-Cons(CEM)], 0(6.822364285714285)[R1,Mirror-Echo], 9(1.536)[R1,Double-Pressure], 5(0.527)[R3,Mirror-Echo], 1(0.2807928571428571)[R3,Mirror-Echo]
- P2: 3(8.63632142857143)[R1,Mirror-Echo], 8(7.545564285714286)[R2,Mirror-Echo], 9(1.8182142857142858)[R3,XVAR-Cons(CE)], 7(0.43889999999999996)[R2]
- P3: 1(3.5355714285714286)[R1,XVAR-Cons(CE)], 8(3.2973)[R2,XVAR-Cons(CE)], 0(1.5736642857142857)[R3,XVAR-Cons(CM)], 9(1.3568571428571428)[R1,Double-Pressure], 6(0.9135)[R2,Double-Pressure]
