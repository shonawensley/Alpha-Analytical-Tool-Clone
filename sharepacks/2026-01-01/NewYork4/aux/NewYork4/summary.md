# Aux Summary — NewYork4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/NewYork4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: New York
- combined: live=`data/cleaned/draws/New_York_draws.csv` snap=`sharepacks/2026-01-01/NewYork4/aux/draws/New_York_draws.csv` n=1000 head=116, 419, 132, 051, 195
- midday: live=`data/cleaned/draws/New_York_Midday_draws.csv` snap=`sharepacks/2026-01-01/NewYork4/aux/draws/New_York_Midday_draws.csv` n=1000 head=419, 051, 321, 498, 893
- evening: live=`data/cleaned/draws/New_York_Evening_draws.csv` snap=`sharepacks/2026-01-01/NewYork4/aux/draws/New_York_Evening_draws.csv` n=1000 head=116, 132, 195, 353, 050

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=16 streak=1 max=2 last_repeat_gap=21 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=22), P2:4 (gap=22), P3:7 (gap=37)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 907: score=42.67222142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 607: score=38.89027857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 947: score=37.9815 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 977: score=34.746871428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 647: score=34.199557142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 987: score=33.0185 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 937: score=32.3988 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 677: score=30.964928571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 909: score=30.750398571428576 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 906: score=29.316950000000002 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 244: ds=980 sev=B
- 699: ds=923 sev=B
- 115: ds=841 sev=B
- 222: ds=777 sev=B
- 339: ds=758 sev=B
- 136: ds=749 sev=B
- 000: ds=748 sev=B
- 177: ds=742 sev=B
- 667: ds=710 sev=B
- 777: ds=704 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=51 sev=purple
  - 99: ds=47 sev=purple
  - 77: ds=37 sev=purple
  - 55: ds=36 sev=purple
  - 22: ds=32 sev=purple
  - 66: ds=12 sev=-
  - 44: ds=11 sev=-
  - 00: ds=8 sev=-
  - 33: ds=6 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 67: ds=63 sev=red
  - 06: ds=60 sev=red
  - 69: ds=56 sev=red
  - 36: ds=52 sev=blue
  - 17: ds=40 sev=blue
  - 56: ds=38 sev=blue
  - 68: ds=38 sev=blue
  - 07: ds=37 sev=blue
  - 34: ds=33 sev=purple
  - 26: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:210, 35:198, 26:114, 32:99, 17:77, 22:74, 28:68, 5:62, 23:52, 31:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=210 fs=13 fl=3 hz=0.020356234096692113, 35:ds=198 fs=4 fl=3 hz=0.009138381201044387, 26:ds=114 fs=2 fl=1 hz=0.007173601147776184, 32:ds=99 fs=7 fl=3 hz=0.012515644555694618, 17:ds=77 fs=21 fl=1 hz=0.025669642857142856, 22:ds=74 fs=49 fl=0 hz=0.05378704720087815, 28:ds=68 fs=16 fl=3 hz=0.021788990825688075, 5:ds=62 fs=15 fl=3 hz=0.01973684210526316, 23:ds=52 fs=23 fl=2 hz=0.02910360884749709, 31:ds=47 fs=21 fl=1 hz=0.023579849946409433

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S25: ds=76 flags=purple
- S22: ds=74 flags=purple
- S9: ds=67 flags=red+purple
- S7: ds=64 flags=purple
- S23: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 027: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 168: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 238: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=25 streak=1 max=2 last_repeat_gap=15 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=28), P2:4 (gap=24), P3:6 (gap=21)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 907: score=42.67222142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 607: score=38.89027857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 947: score=37.9815 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 977: score=34.746871428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 647: score=34.199557142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 987: score=33.0185 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 937: score=32.3988 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 677: score=30.964928571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 909: score=30.750398571428576 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 906: score=29.316950000000002 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=995 sev=B
- 337: ds=828 sev=B
- 366: ds=821 sev=B
- 044: ds=799 sev=B
- 667: ds=777 sev=B
- 189: ds=763 sev=B
- 449: ds=759 sev=B
- 456: ds=730 sev=B
- 223: ds=723 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=170 sev=red
  - 66: ds=113 sev=red
  - 55: ds=43 sev=purple
  - 33: ds=41 sev=purple
  - 88: ds=25 sev=purple
  - 99: ds=23 sev=-
  - 00: ds=20 sev=-
  - 22: ds=19 sev=-
  - 77: ds=18 sev=-
  - 44: ds=5 sev=-
- non_repeating:
  - 27: ds=67 sev=red
  - 06: ds=53 sev=blue
  - 25: ds=52 sev=blue
  - 17: ds=38 sev=blue
  - 36: ds=37 sev=blue
  - 69: ds=36 sev=purple
  - 09: ds=33 sev=purple
  - 56: ds=31 sev=purple
  - 67: ds=31 sev=purple
  - 16: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:367, 26:339, 16:262, 18:115, 22:98, 15:87, 23:80, 27:73, 1:69, 28:66

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=367 fs=1 fl=1 hz=0.005145797598627787, 26:ds=339 fs=1 fl=0 hz=0.004081632653061225, 16:ds=262 fs=3 fl=0 hz=0.005471956224350205, 18:ds=115 fs=16 fl=2 hz=0.020524515393386546, 22:ds=98 fs=43 fl=0 hz=0.04772475027746948, 15:ds=87 fs=17 fl=2 hz=0.02134831460674157, 23:ds=80 fs=24 fl=1 hz=0.02860411899313501, 27:ds=73 fs=12 fl=2 hz=0.01728110599078341, 1:ds=69 fs=3 fl=2 hz=0.008075370121130552, 28:ds=66 fs=21 fl=2 hz=0.0257847533632287

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S8: ds=84 flags=red+purple
- S25: ds=60 flags=blue+purple
- S10: ds=52 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=16 streak=1 max=2 last_repeat_gap=30 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=22), P2:8 (gap=36), P3:7 (gap=38)
- consensus_notes: P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 907: score=42.67222142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 607: score=38.89027857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 947: score=37.9815 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 977: score=34.746871428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 647: score=34.199557142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 987: score=33.0185 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 937: score=32.3988 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 677: score=30.964928571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 909: score=30.750398571428576 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 906: score=29.316950000000002 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 566: ds=974 sev=B
- 668: ds=854 sev=B
- 248: ds=848 sev=B
- 014: ds=828 sev=B
- 222: ds=812 sev=B
- 001: ds=793 sev=B
- 999: ds=783 sev=B
- 444: ds=782 sev=B
- 156: ds=757 sev=B
- 133: ds=705 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=124 sev=red
  - 44: ds=48 sev=purple
  - 99: ds=38 sev=purple
  - 88: ds=35 sev=purple
  - 55: ds=18 sev=-
  - 22: ds=16 sev=-
  - 66: ds=6 sev=-
  - 00: ds=4 sev=-
  - 33: ds=3 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 47: ds=126 sev=red
  - 48: ds=94 sev=red
  - 07: ds=83 sev=red
  - 03: ds=60 sev=red
  - 39: ds=41 sev=blue
  - 67: ds=37 sev=blue
  - 06: ds=30 sev=purple
  - 46: ds=28 sev=purple
  - 69: ds=28 sev=purple
  - 36: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:105, 34:104, 35:99, 32:82, 33:75, 10:65, 17:63, 26:57, 4:49, 2:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=105 fs=14 fl=1 hz=0.01884570082449941, 34:ds=104 fs=19 fl=0 hz=0.02242152466367713, 35:ds=99 fs=5 fl=2 hz=0.00963855421686747, 32:ds=82 fs=9 fl=1 hz=0.013095238095238096, 33:ds=75 fs=16 fl=2 hz=0.022113022113022112, 10:ds=65 fs=27 fl=1 hz=0.030335861321776812, 17:ds=63 fs=31 fl=1 hz=0.034408602150537634, 26:ds=57 fs=3 fl=4 hz=0.008879023307436182, 4:ds=49 fs=23 fl=1 hz=0.026200873362445417, 2:ds=44 fs=28 fl=1 hz=0.03456495828367104

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=65 flags=purple
- S3: ds=50 flags=purple
- S16: ds=43 flags=purple
- S25: ds=38 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [7], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '7', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 349: score=4 tags=FLT,MIR,RS
  - 358: score=4 tags=FLT,MIR,RS
  - 016: score=3 tags=MIR,RS
  - 025: score=3 tags=MIR,RS
  - 034: score=3 tags=FLT,RS
  - 079: score=3 tags=FLT,RS
  - 124: score=3 tags=FLT,RS
  - 169: score=3 tags=MIR,RS
  - 178: score=3 tags=FLT,RS
  - 268: score=3 tags=FLT,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 001 -> evening:793(B); midday:995(B)
- 222 -> combined:777(B); evening:812(B)
- 667 -> combined:710(B); midday:777(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 06 -> combined:60(red); evening:30(purple); midday:53(blue)
- 07 -> combined:37(blue); evening:83(red)
- 17 -> combined:40(blue); midday:38(blue)
- 27 -> combined:30(purple); midday:67(red)
- 36 -> combined:52(blue); evening:26(purple); midday:37(blue)
- 55 -> combined:36(purple); midday:43(purple)
- 56 -> combined:38(blue); midday:31(purple)
- 67 -> combined:63(red); evening:37(blue); midday:31(purple)
- 69 -> combined:56(red); evening:28(purple); midday:36(purple)
- 77 -> combined:37(purple); evening:124(red)
- 88 -> combined:51(purple); evening:35(purple); midday:25(purple)
- 99 -> combined:47(purple); evening:38(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(3.7912285714285714)[R1,XVAR-Cons(CM)], 6(1.5092857142857143)[R1,Mirror-Echo], 4(1.3568571428571428)[R1,Double-Pressure], 5(1.044)[R2,Double-Pressure], 8(1.0252999999999999)[R2,Double-Pressure]
- P2: 0(6.298721428571429)[R2,XVAR-Cons(CEM)], 4(4.1080000000000005)[R1,XVAR-Cons(CM)], 7(1.8733714285714287)[R3,XVAR-Cons(CE)], 8(1.645)[R1,Double-Pressure], 3(1.0252999999999999)[R2,Double-Pressure]
- P3: 7(8.582271428571428)[R1,XVAR-Cons(CEM)], 6(1.2269999999999999)[R1,Double-Pressure], 9(1.1716)[R2,Double-Pressure], 4(0.9199999999999999)[R2,Double-Pressure], 2(0.37535714285714283)[R3,Mirror-Echo]
