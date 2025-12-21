# Aux Summary — NewJersey4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/NewJersey4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: New Jersey
- combined: live=`data/cleaned/draws/New_Jersey_draws.csv` snap=`sharepacks/2025-06-21/NewJersey4/aux/draws/New_Jersey_draws.csv` n=1000 head=445, 399, 740, 034, 351
- midday: live=`data/cleaned/draws/New_Jersey_Midday_draws.csv` snap=`sharepacks/2025-06-21/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv` n=1000 head=399, 034, 234, 758, 170
- evening: live=`data/cleaned/draws/New_Jersey_Evening_draws.csv` snap=`sharepacks/2025-06-21/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv` n=1000 head=445, 740, 351, 926, 431

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=2 last_repeat_gap=92 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=22), P2:8 (gap=56), P3:2 (gap=31)
- consensus_notes: P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:8 (ds=56)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 582: score=53.35059535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 882: score=45.14932142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 587: score=43.39687142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 562: score=42.03267857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 585: score=39.701565714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 502: score=39.38287142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 887: score=38.56741428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 588: score=37.45445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 586: score=37.20365714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 862: score=37.203221428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 223: ds=988 sev=B
- 444: ds=913 sev=B
- 499: ds=849 sev=B
- 336: ds=824 sev=B
- 339: ds=807 sev=B
- 556: ds=787 sev=B
- 666: ds=782 sev=B
- 255: ds=754 sev=B
- 777: ds=750 sev=B
- 377: ds=725 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=144 sev=red
  - 22: ds=113 sev=red
  - 33: ds=75 sev=blue
  - 66: ds=68 sev=purple
  - 88: ds=65 sev=purple
  - 77: ds=50 sev=purple
  - 55: ds=27 sev=purple
  - 11: ds=14 sev=-
  - 99: ds=1 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 28: ds=137 sev=red
  - 56: ds=107 sev=red
  - 89: ds=63 sev=red
  - 05: ds=56 sev=red
  - 38: ds=45 sev=blue
  - 16: ds=43 sev=blue
  - 48: ds=42 sev=blue
  - 67: ds=34 sev=purple
  - 79: ds=28 sev=purple
  - 08: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:414, 35:233, 27:143, 5:131, 29:125, 13:123, 1:112, 21:102, 2:78, 32:75

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=414 fs=2 fl=1 hz=0.013452914798206279, 35:ds=233 fs=3 fl=1 hz=0.007936507936507936, 27:ds=143 fs=11 fl=2 hz=0.016568047337278107, 5:ds=131 fs=13 fl=2 hz=0.018633540372670808, 29:ds=125 fs=19 fl=3 hz=0.02564102564102564, 13:ds=123 fs=9 fl=3 hz=0.01568627450980392, 1:ds=112 fs=1 fl=3 hz=0.007398273736128237, 21:ds=102 fs=35 fl=0 hz=0.041716328963051254, 2:ds=78 fs=18 fl=2 hz=0.022753128555176336, 32:ds=75 fs=3 fl=2 hz=0.007202881152460984

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S22: ds=83 flags=purple
- S6: ds=78 flags=red+purple
- S24: ds=77 flags=blue+purple
- S12: ds=45 flags=purple
- S18: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '6', '8'], 'pairs': {'remaining_count': 2}}
- top candidates:
  - 012: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=34 streak=1 max=3 last_repeat_gap=16 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=31), P2:8 (gap=40), P3:5 (gap=26)
- consensus_notes: P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:8 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 582: score=53.35059535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 882: score=45.14932142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 587: score=43.39687142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 562: score=42.03267857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 585: score=39.701565714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 502: score=39.38287142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 887: score=38.56741428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 588: score=37.45445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 586: score=37.20365714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 862: score=37.203221428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=984 sev=B
- 555: ds=952 sev=B
- 588: ds=941 sev=B
- 889: ds=909 sev=B
- 336: ds=865 sev=B
- 577: ds=857 sev=B
- 168: ds=797 sev=B
- 668: ds=781 sev=B
- 778: ds=777 sev=B
- 069: ds=753 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=203 sev=red
  - 66: ds=110 sev=red
  - 44: ds=84 sev=blue
  - 00: ds=80 sev=blue
  - 22: ds=56 sev=purple
  - 33: ds=37 sev=purple
  - 88: ds=32 sev=purple
  - 11: ds=17 sev=-
  - 55: ds=13 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 28: ds=68 sev=red
  - 26: ds=59 sev=red
  - 56: ds=53 sev=blue
  - 15: ds=43 sev=blue
  - 68: ds=41 sev=blue
  - 08: ds=36 sev=purple
  - 09: ds=36 sev=purple
  - 48: ds=32 sev=purple
  - 89: ds=31 sev=purple
  - 05: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:250, 1:172, 16:171, 31:133, 18:124, 4:118, 35:116, 21:94, 15:93, 2:80

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=250 fs=1 fl=0 hz=0.007246376811594203, 1:ds=172 fs=4 fl=0 hz=0.009554140127388535, 16:ds=171 fs=6 fl=2 hz=0.013138686131386862, 31:ds=133 fs=23 fl=0 hz=0.029449423815620997, 18:ds=124 fs=17 fl=3 hz=0.023781212841854936, 4:ds=118 fs=28 fl=1 hz=0.03341013824884793, 35:ds=116 fs=3 fl=0 hz=0.006720430107526881, 21:ds=94 fs=38 fl=0 hz=0.04203539823008849, 15:ds=93 fs=21 fl=1 hz=0.02502844141069397, 2:ds=80 fs=26 fl=0 hz=0.030338389731621937

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S3: ds=92 flags=purple
- S6: ds=80 flags=red+purple
- S23: ds=62 flags=purple
- S22: ds=41 flags=purple
- S24: ds=38 flags=purple
- S18: ds=31 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 067: score=1 tags=FLT
  - 068: score=1 tags=FLT
  - 069: score=1 tags=FLT
  - 126: score=1 tags=FLT
  - 136: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=3 last_repeat_gap=16 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=61), P2:8 (gap=28), P3:2 (gap=31)
- consensus_notes: P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=61)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 582: score=53.35059535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 882: score=45.14932142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 587: score=43.39687142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 562: score=42.03267857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 585: score=39.701565714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 502: score=39.38287142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 887: score=38.56741428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 588: score=37.45445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 586: score=37.20365714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 862: score=37.203221428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=986 sev=B
- 668: ds=941 sev=B
- 225: ds=930 sev=B
- 024: ds=894 sev=B
- 035: ds=758 sev=B
- 499: ds=749 sev=B
- 339: ds=735 sev=B
- 002: ds=703 sev=B
- 556: ds=667 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=221 sev=red
  - 00: ds=72 sev=blue
  - 88: ds=65 sev=purple
  - 99: ds=60 sev=purple
  - 55: ds=47 sev=purple
  - 33: ds=42 sev=purple
  - 66: ds=34 sev=purple
  - 77: ds=25 sev=purple
  - 11: ds=7 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 56: ds=124 sev=red
  - 28: ds=95 sev=red
  - 36: ds=51 sev=blue
  - 37: ds=46 sev=blue
  - 89: ds=44 sev=blue
  - 38: ds=42 sev=blue
  - 16: ds=34 sev=purple
  - 27: ds=31 sev=purple
  - 78: ds=30 sev=purple
  - 24: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:229, 26:207, 3:165, 13:153, 5:117, 29:108, 27:87, 17:66, 23:65, 33:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=229 fs=5 fl=1 hz=0.009510869565217392, 26:ds=207 fs=3 fl=0 hz=0.00753012048192771, 3:ds=165 fs=23 fl=1 hz=0.028915662650602407, 13:ds=153 fs=13 fl=2 hz=0.01968503937007874, 5:ds=117 fs=27 fl=1 hz=0.03214695752009185, 29:ds=108 fs=20 fl=0 hz=0.02652519893899204, 27:ds=87 fs=10 fl=2 hz=0.014412416851441241, 17:ds=66 fs=12 fl=3 hz=0.016233766233766232, 23:ds=65 fs=22 fl=2 hz=0.02631578947368421, 33:ds=59 fs=19 fl=2 hz=0.02661596958174905

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=87 flags=purple
- S5: ds=86 flags=purple
- S2: ds=57 flags=purple
- S24: ds=44 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 018: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 068: score=1 tags=FLT
  - 078: score=1 tags=FLT
  - 089: score=1 tags=FLT
  - 128: score=1 tags=FLT
  - 138: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 223 -> combined:988(B); midday:675(B)
- 336 -> combined:824(B); midday:865(B)
- 339 -> combined:807(B); evening:735(B)
- 499 -> combined:849(B); evening:749(B)
- 556 -> combined:787(B); evening:667(B)
- 668 -> evening:941(B); midday:781(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:144(red); evening:72(blue); midday:80(blue)
- 05 -> combined:56(red); evening:28(purple); midday:29(purple)
- 08 -> combined:26(purple); midday:36(purple)
- 16 -> combined:43(blue); evening:34(purple)
- 22 -> combined:113(red); evening:221(red); midday:56(purple)
- 27 -> combined:25(purple); evening:31(purple)
- 28 -> combined:137(red); evening:95(red); midday:68(red)
- 33 -> combined:75(blue); evening:42(purple); midday:37(purple)
- 38 -> combined:45(blue); evening:42(blue)
- 48 -> combined:42(blue); midday:32(purple)
- 55 -> combined:27(purple); evening:47(purple)
- 56 -> combined:107(red); evening:124(red); midday:53(blue)
- 66 -> combined:68(purple); evening:34(purple); midday:110(red)
- 67 -> combined:34(purple); midday:27(purple)
- 68 -> combined:26(purple); midday:41(blue)
- 77 -> combined:50(purple); evening:25(purple); midday:203(red)
- 88 -> combined:65(purple); evening:65(purple); midday:32(purple)
- 89 -> combined:63(red); evening:44(blue); midday:31(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(5.646457142857143)[R2,XVAR-Cons(CEM)], 8(4.317)[R1,XVAR-Cons(CM)], 6(3.4137142857142857)[R3,XVAR-Cons(CE)], 0(1.1199)[R2,Mirror-Echo], 4(0.5225)[R2]
- P2: 8(8.981)[R1,XVAR-Cons(CEM)], 6(3.5349)[R2,XVAR-Cons(CM)], 0(1.8850928571428571)[R3,XVAR-Cons(CE)], 7(0.9925999999999999)[R2,Double-Pressure], 2(0.3687142857142857)[R3,Swap]
- P3: 2(7.851321428571429)[R1,Mirror-Echo], 7(3.769414285714286)[R2,Mirror-Echo], 5(1.4462857142857144)[R1,Double-Pressure], 8(1.327)[R2,Double-Pressure], 6(1.0761999999999998)[R2,Double-Pressure]
