# Aux Summary — NewJersey4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/NewJersey4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: New Jersey
- combined: live=`data/cleaned/draws/New_Jersey_draws.csv` snap=`sharepacks/2025-06-22/NewJersey4/aux/draws/New_Jersey_draws.csv` n=1000 head=554, 182, 445, 399, 740
- midday: live=`data/cleaned/draws/New_Jersey_Midday_draws.csv` snap=`sharepacks/2025-06-22/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv` n=1000 head=182, 399, 034, 234, 758
- evening: live=`data/cleaned/draws/New_Jersey_Evening_draws.csv` snap=`sharepacks/2025-06-22/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv` n=1000 head=554, 445, 740, 351, 926

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=2 last_repeat_gap=94 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=24), P2:6 (gap=20), P3:7 (gap=29)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 867: score=42.81189285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 807: score=40.40613571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=39.66782428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 667: score=37.34795 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 808: score=37.26206714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 887: score=36.79589285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 827: score=36.36893571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 877: score=36.24353571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 817: score=35.797892857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 607: score=34.94219285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 223: ds=990 sev=B
- 444: ds=915 sev=B
- 499: ds=851 sev=B
- 336: ds=826 sev=B
- 339: ds=809 sev=B
- 556: ds=789 sev=B
- 666: ds=784 sev=B
- 255: ds=756 sev=B
- 777: ds=752 sev=B
- 377: ds=727 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=146 sev=red
  - 22: ds=115 sev=red
  - 33: ds=77 sev=blue
  - 66: ds=70 sev=purple
  - 88: ds=67 sev=purple
  - 77: ds=52 sev=purple
  - 11: ds=16 sev=-
  - 99: ds=3 sev=-
  - 44: ds=2 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 56: ds=109 sev=red
  - 89: ds=65 sev=red
  - 05: ds=58 sev=red
  - 38: ds=47 sev=blue
  - 16: ds=45 sev=blue
  - 48: ds=44 sev=blue
  - 67: ds=36 sev=purple
  - 79: ds=30 sev=purple
  - 08: ds=28 sev=purple
  - 68: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:416, 35:235, 27:145, 29:127, 13:125, 1:114, 2:80, 32:77, 19:71, 16:70

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=416 fs=2 fl=1 hz=0.013452914798206279, 35:ds=235 fs=3 fl=1 hz=0.007936507936507936, 27:ds=145 fs=11 fl=2 hz=0.016568047337278107, 29:ds=127 fs=19 fl=3 hz=0.02564102564102564, 13:ds=125 fs=9 fl=3 hz=0.01568627450980392, 1:ds=114 fs=1 fl=3 hz=0.007398273736128237, 2:ds=80 fs=18 fl=2 hz=0.022753128555176336, 32:ds=77 fs=3 fl=2 hz=0.007202881152460984, 19:ds=71 fs=28 fl=1 hz=0.03341013824884793, 16:ds=70 fs=1 fl=3 hz=0.0064516129032258064

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S22: ds=85 flags=purple
- S6: ds=80 flags=red+purple
- S24: ds=79 flags=blue+purple
- S12: ds=47 flags=purple
- S18: ds=42 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
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

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=17 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=32), P2:6 (gap=22), P3:5 (gap=27)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 867: score=42.81189285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 807: score=40.40613571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=39.66782428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 667: score=37.34795 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 808: score=37.26206714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 887: score=36.79589285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 827: score=36.36893571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 877: score=36.24353571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 817: score=35.797892857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 607: score=34.94219285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=985 sev=B
- 555: ds=953 sev=B
- 588: ds=942 sev=B
- 889: ds=910 sev=B
- 336: ds=866 sev=B
- 577: ds=858 sev=B
- 168: ds=798 sev=B
- 668: ds=782 sev=B
- 778: ds=778 sev=B
- 069: ds=754 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=204 sev=red
  - 66: ds=111 sev=red
  - 44: ds=85 sev=blue
  - 00: ds=81 sev=blue
  - 22: ds=57 sev=purple
  - 33: ds=38 sev=purple
  - 88: ds=33 sev=purple
  - 11: ds=18 sev=-
  - 55: ds=14 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 26: ds=60 sev=red
  - 56: ds=54 sev=blue
  - 15: ds=44 sev=blue
  - 68: ds=42 sev=blue
  - 08: ds=37 sev=blue
  - 09: ds=37 sev=blue
  - 48: ds=33 sev=purple
  - 89: ds=32 sev=purple
  - 05: ds=30 sev=purple
  - 67: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:251, 1:173, 16:172, 31:134, 18:125, 4:119, 35:117, 15:94, 2:81, 27:72

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=251 fs=1 fl=0 hz=0.007246376811594203, 1:ds=173 fs=4 fl=0 hz=0.009554140127388535, 16:ds=172 fs=6 fl=2 hz=0.013138686131386862, 31:ds=134 fs=23 fl=0 hz=0.029449423815620997, 18:ds=125 fs=17 fl=3 hz=0.023781212841854936, 4:ds=119 fs=28 fl=1 hz=0.03341013824884793, 35:ds=117 fs=3 fl=0 hz=0.006720430107526881, 15:ds=94 fs=21 fl=1 hz=0.02502844141069397, 2:ds=81 fs=26 fl=0 hz=0.030338389731621937, 27:ds=72 fs=13 fl=4 hz=0.018805309734513272

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S3: ds=93 flags=purple
- S6: ds=81 flags=red+purple
- S23: ds=63 flags=purple
- S22: ds=42 flags=purple
- S24: ds=39 flags=purple
- S18: ds=32 flags=red+purple

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
- current_index=5 streak=1 max=3 last_repeat_gap=17 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=62), P2:8 (gap=29), P3:2 (gap=32)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=62)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 867: score=42.81189285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 807: score=40.40613571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=39.66782428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 667: score=37.34795 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 808: score=37.26206714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 887: score=36.79589285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 827: score=36.36893571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 877: score=36.24353571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 817: score=35.797892857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 607: score=34.94219285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=987 sev=B
- 668: ds=942 sev=B
- 225: ds=931 sev=B
- 024: ds=895 sev=B
- 035: ds=759 sev=B
- 499: ds=750 sev=B
- 339: ds=736 sev=B
- 002: ds=704 sev=B
- 556: ds=668 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=222 sev=red
  - 00: ds=73 sev=blue
  - 88: ds=66 sev=purple
  - 99: ds=61 sev=purple
  - 33: ds=43 sev=purple
  - 66: ds=35 sev=purple
  - 77: ds=26 sev=purple
  - 11: ds=8 sev=-
  - 44: ds=1 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 56: ds=125 sev=red
  - 28: ds=96 sev=red
  - 36: ds=52 sev=blue
  - 37: ds=47 sev=blue
  - 89: ds=45 sev=blue
  - 38: ds=43 sev=blue
  - 16: ds=35 sev=purple
  - 27: ds=32 sev=purple
  - 78: ds=31 sev=purple
  - 24: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:230, 26:208, 3:166, 13:154, 29:109, 27:88, 17:67, 23:66, 33:60, 1:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=230 fs=5 fl=1 hz=0.009510869565217392, 26:ds=208 fs=3 fl=0 hz=0.00753012048192771, 3:ds=166 fs=23 fl=1 hz=0.028915662650602407, 13:ds=154 fs=13 fl=2 hz=0.01968503937007874, 29:ds=109 fs=20 fl=0 hz=0.02652519893899204, 27:ds=88 fs=10 fl=2 hz=0.014412416851441241, 17:ds=67 fs=12 fl=3 hz=0.016233766233766232, 23:ds=66 fs=22 fl=2 hz=0.02631578947368421, 33:ds=60 fs=19 fl=2 hz=0.02661596958174905, 1:ds=57 fs=1 fl=1 hz=0.008450704225352114

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=88 flags=purple
- S5: ds=87 flags=purple
- S2: ds=58 flags=purple
- S24: ds=45 flags=blue+purple

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
- 223 -> combined:990(B); midday:676(B)
- 336 -> combined:826(B); midday:866(B)
- 339 -> combined:809(B); evening:736(B)
- 499 -> combined:851(B); evening:750(B)
- 556 -> combined:789(B); evening:668(B)
- 668 -> evening:942(B); midday:782(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:146(red); evening:73(blue); midday:81(blue)
- 05 -> combined:58(red); evening:29(purple); midday:30(purple)
- 08 -> combined:28(purple); midday:37(blue)
- 16 -> combined:45(blue); evening:35(purple)
- 19 -> combined:26(purple); midday:25(purple)
- 22 -> combined:115(red); evening:222(red); midday:57(purple)
- 27 -> combined:27(purple); evening:32(purple)
- 33 -> combined:77(blue); evening:43(purple); midday:38(purple)
- 38 -> combined:47(blue); evening:43(blue)
- 48 -> combined:44(blue); midday:33(purple)
- 56 -> combined:109(red); evening:125(red); midday:54(blue)
- 66 -> combined:70(purple); evening:35(purple); midday:111(red)
- 67 -> combined:36(purple); midday:28(purple)
- 68 -> combined:28(purple); midday:42(blue)
- 77 -> combined:52(purple); evening:26(purple); midday:204(red)
- 88 -> combined:67(purple); evening:66(purple); midday:33(purple)
- 89 -> combined:65(red); evening:45(blue); midday:32(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 8(7.170942857142857)[R1,XVAR-Cons(CEM)], 6(4.207)[R2,XVAR-Cons(CE)], 0(1.0553)[R2,Double-Pressure], 4(0.5433999999999999)[R2], 5(0.21779285714285712)[R3,Swap]
- P2: 6(4.081857142857142)[R1,Mirror-Echo], 0(2.6761)[R2,XVAR-Cons(CE)], 8(1.5658571428571428)[R1,Double-Pressure], 2(1.1389)[R2,Double-Pressure], 7(1.0135)[R2,Double-Pressure]
- P3: 7(6.559092857142858)[R1,XVAR-Cons(CEM)], 8(2.8951857142857143)[R3,Mirror-Echo], 2(1.7714642857142857)[R1,Mirror-Echo], 5(1.4761428571428572)[R1,Double-Pressure], 6(1.0971)[R2,Double-Pressure]
