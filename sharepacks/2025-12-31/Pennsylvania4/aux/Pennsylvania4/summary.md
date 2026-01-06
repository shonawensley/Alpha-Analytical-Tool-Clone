# Aux Summary — Pennsylvania4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2025-12-31/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=173, 186, 460, 239, 422
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2025-12-31/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=186, 239, 502, 264, 014
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2025-12-31/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=173, 460, 422, 065, 994

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=19 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=31), P2:4 (gap=24), P3:1 (gap=49)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=44.303107142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 341: score=44.11635714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 351: score=43.75263571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 371: score=41.04917857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 321: score=40.91726428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 331: score=39.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 811: score=38.86445714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 841: score=38.677707142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 316: score=32.14187857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=31.955128571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=992 sev=B
- 666: ds=990 sev=B
- 159: ds=878 sev=B
- 007: ds=875 sev=B
- 088: ds=839 sev=B
- 008: ds=817 sev=B
- 444: ds=793 sev=B
- 039: ds=768 sev=B
- 355: ds=758 sev=B
- 344: ds=687 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=135 sev=red
  - 77: ds=74 sev=blue
  - 88: ds=73 sev=blue
  - 44: ds=67 sev=purple
  - 66: ds=61 sev=purple
  - 55: ds=38 sev=purple
  - 11: ds=23 sev=-
  - 00: ds=21 sev=-
  - 99: ds=8 sev=-
  - 22: ds=4 sev=-
- non_repeating:
  - 78: ds=68 sev=red
  - 12: ds=46 sev=blue
  - 03: ds=43 sev=blue
  - 07: ds=41 sev=blue
  - 35: ds=34 sev=purple
  - 69: ds=32 sev=purple
  - 36: ds=29 sev=purple
  - 09: ds=28 sev=purple
  - 34: ds=27 sev=purple
  - 38: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:277, 26:234, 16:92, 27:68, 7:60, 24:57, 6:55, 13:53, 19:49, 10:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=277 fs=2 fl=1 hz=0.007380073800738007, 26:ds=234 fs=0 fl=1 hz=0.003898635477582846, 16:ds=92 fs=3 fl=2 hz=0.007371007371007371, 27:ds=68 fs=11 fl=4 hz=0.01722158438576349, 7:ds=60 fs=36 fl=1 hz=0.03965702036441586, 24:ds=57 fs=44 fl=0 hz=0.048245614035087724, 6:ds=55 fs=22 fl=1 hz=0.02454642475987193, 13:ds=53 fs=21 fl=1 hz=0.024553571428571428, 19:ds=49 fs=21 fl=3 hz=0.025695931477516063, 10:ds=44 fs=24 fl=2 hz=0.027253668763102725

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=86 flags=purple
- S20: ds=73 flags=purple
- S6: ds=52 flags=purple
- S25: ds=50 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT
  - 125: score=1 tags=FLT
  - 135: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=18 streak=1 max=3 last_repeat_gap=31 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=25), P2:7 (gap=20), P3:5 (gap=25)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=44.303107142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 341: score=44.11635714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 351: score=43.75263571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 371: score=41.04917857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 321: score=40.91726428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 331: score=39.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 811: score=38.86445714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 841: score=38.677707142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 316: score=32.14187857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=31.955128571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=975 sev=B
- 288: ds=962 sev=B
- 255: ds=933 sev=B
- 668: ds=915 sev=B
- 199: ds=863 sev=B
- 499: ds=789 sev=B
- 399: ds=772 sev=B
- 039: ds=760 sev=B
- 448: ds=749 sev=B
- 005: ds=741 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=184 sev=red
  - 99: ds=131 sev=red
  - 77: ds=74 sev=blue
  - 33: ds=67 sev=purple
  - 22: ds=60 sev=purple
  - 88: ds=36 sev=purple
  - 44: ds=33 sev=purple
  - 66: ds=30 sev=purple
  - 11: ds=11 sev=-
  - 00: ds=10 sev=-
- non_repeating:
  - 59: ds=77 sev=red
  - 79: ds=71 sev=red
  - 12: ds=46 sev=blue
  - 78: ds=44 sev=blue
  - 06: ds=41 sev=blue
  - 35: ds=38 sev=blue
  - 56: ds=30 sev=purple
  - 69: ds=28 sev=purple
  - 13: ds=23 sev=-
  - 57: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:373, 1:358, 34:212, 16:170, 15:161, 32:138, 35:115, 27:82, 28:60, 5:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=373 fs=0 fl=0 hz=0.0, 1:ds=358 fs=2 fl=2 hz=0.009124087591240877, 34:ds=212 fs=19 fl=1 hz=0.02631578947368421, 16:ds=170 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=161 fs=23 fl=0 hz=0.029411764705882353, 32:ds=138 fs=3 fl=1 hz=0.006720430107526881, 35:ds=115 fs=1 fl=1 hz=0.0035587188612099642, 27:ds=82 fs=22 fl=2 hz=0.028605482717520857, 28:ds=60 fs=26 fl=2 hz=0.02997858672376874, 5:ds=45 fs=18 fl=2 hz=0.022175290390707498

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=92 flags=red+purple
- S22: ds=77 flags=purple
- S23: ds=65 flags=purple
- S3: ds=59 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 027: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 247: score=2 tags=FLT,MIR
  - 257: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 279: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=61 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=27), P2:1 (gap=33), P3:1 (gap=26)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 311: score=44.303107142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 341: score=44.11635714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 351: score=43.75263571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 371: score=41.04917857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 321: score=40.91726428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 331: score=39.64583571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 811: score=38.86445714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 841: score=38.677707142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 316: score=32.14187857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=31.955128571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=971 sev=B
- 009: ds=929 sev=B
- 255: ds=887 sev=B
- 138: ds=827 sev=B
- 117: ds=810 sev=B
- 158: ds=772 sev=B
- 344: ds=765 sev=B
- 199: ds=756 sev=B
- 112: ds=716 sev=B
- 277: ds=701 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=126 sev=red
  - 33: ds=68 sev=purple
  - 44: ds=39 sev=purple
  - 77: ds=37 sev=purple
  - 66: ds=35 sev=purple
  - 11: ds=26 sev=purple
  - 55: ds=19 sev=-
  - 00: ds=13 sev=-
  - 99: ds=4 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 68: ds=84 sev=red
  - 07: ds=61 sev=red
  - 15: ds=49 sev=blue
  - 38: ds=48 sev=blue
  - 23: ds=45 sev=blue
  - 03: ds=43 sev=blue
  - 78: ds=34 sev=purple
  - 19: ds=33 sev=purple
  - 28: ds=32 sev=purple
  - 01: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:615, 23:154, 26:117, 18:114, 13:63, 29:56, 33:48, 16:46, 30:45, 24:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=615 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=154 fs=17 fl=2 hz=0.025165562913907286, 26:ds=117 fs=2 fl=1 hz=0.0056657223796034, 18:ds=114 fs=23 fl=2 hz=0.02910360884749709, 13:ds=63 fs=20 fl=1 hz=0.024881516587677725, 29:ds=56 fs=16 fl=3 hz=0.020540540540540542, 33:ds=48 fs=19 fl=3 hz=0.023255813953488372, 16:ds=46 fs=5 fl=3 hz=0.009523809523809525, 30:ds=45 fs=35 fl=1 hz=0.03829787234042553, 24:ds=42 fs=37 fl=0 hz=0.04048140043763676

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=87 flags=blue+purple
- S1: ds=72 flags=blue+purple
- S5: ds=69 flags=purple
- S24: ds=55 flags=blue+purple
- S3: ds=43 flags=purple
- S20: ds=37 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
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
- 039 -> combined:768(B); midday:760(B)
- 066 -> combined:992(B); midday:738(B)
- 199 -> evening:756(B); midday:863(B)
- 255 -> evening:887(B); midday:933(B)
- 344 -> combined:687(B); evening:765(B)
- 444 -> combined:793(B); evening:971(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:43(blue); evening:43(blue)
- 07 -> combined:41(blue); evening:61(red)
- 12 -> combined:46(blue); midday:46(blue)
- 19 -> combined:25(purple); evening:33(purple)
- 33 -> combined:135(red); evening:68(purple); midday:67(purple)
- 35 -> combined:34(purple); midday:38(blue)
- 38 -> combined:27(purple); evening:48(blue)
- 44 -> combined:67(purple); evening:39(purple); midday:33(purple)
- 55 -> combined:38(purple); midday:184(red)
- 66 -> combined:61(purple); evening:35(purple); midday:30(purple)
- 69 -> combined:32(purple); midday:28(purple)
- 77 -> combined:74(blue); evening:37(purple); midday:74(blue)
- 78 -> combined:68(red); evening:34(purple); midday:44(blue)
- 88 -> combined:73(blue); evening:126(red); midday:36(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(7.55115)[R1,Mirror-Echo], 8(4.6125)[R2,Mirror-Echo], 7(3.0575714285714284)[R3,XVAR-Cons(CM)], 4(1.1179999999999999)[R2,Double-Pressure], 2(0.2746642857142857)[R3,Swap]
- P2: 1(3.2125714285714286)[R3,XVAR-Cons(CE)], 4(3.025821428571428)[R1,XVAR-Cons(CM)], 5(2.6621)[R2,XVAR-Cons(CE)], 7(1.4586428571428571)[R1,Mirror-Echo], 2(1.3267285714285713)[R2,Mirror-Echo]
- P3: 1(8.539385714285714)[R1,XVAR-Cons(CEM)], 5(1.4464285714285714)[R1,Double-Pressure], 6(1.3781571428571429)[R2,Mirror-Echo], 7(0.942)[R2,Double-Pressure], 3(0.3552785714285714)[R3,Swap]
