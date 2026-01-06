# Aux Summary — Pennsylvania4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2025-12-30/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=460, 239, 422, 502, 065
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2025-12-30/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=239, 502, 264, 014, 267
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2025-12-30/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=460, 422, 065, 994, 598

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=17 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=29), P2:4 (gap=22), P3:1 (gap=47)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 371: score=46.516961071428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 376: score=45.36776607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 341: score=45.358540357142864 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 351: score=42.42821428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=41.70377857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 356: score=41.428914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 373: score=41.226488571428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 321: score=39.58580714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 871: score=39.102450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 311: score=38.97897857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=990 sev=B
- 666: ds=988 sev=B
- 159: ds=876 sev=B
- 007: ds=873 sev=B
- 088: ds=837 sev=B
- 008: ds=815 sev=B
- 444: ds=791 sev=B
- 039: ds=766 sev=B
- 355: ds=756 sev=B
- 344: ds=685 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=133 sev=red
  - 77: ds=72 sev=blue
  - 88: ds=71 sev=blue
  - 44: ds=65 sev=purple
  - 66: ds=59 sev=purple
  - 55: ds=36 sev=purple
  - 11: ds=21 sev=-
  - 00: ds=19 sev=-
  - 99: ds=6 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 78: ds=66 sev=red
  - 13: ds=45 sev=blue
  - 12: ds=44 sev=blue
  - 16: ds=44 sev=blue
  - 03: ds=41 sev=blue
  - 07: ds=39 sev=blue
  - 35: ds=32 sev=purple
  - 69: ds=30 sev=purple
  - 37: ds=29 sev=purple
  - 36: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:275, 26:232, 18:201, 16:90, 27:66, 7:58, 21:57, 24:55, 6:53, 13:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=275 fs=2 fl=1 hz=0.007380073800738007, 26:ds=232 fs=0 fl=1 hz=0.003898635477582846, 18:ds=201 fs=26 fl=1 hz=0.03426395939086294, 16:ds=90 fs=3 fl=2 hz=0.007371007371007371, 27:ds=66 fs=11 fl=4 hz=0.01722158438576349, 7:ds=58 fs=36 fl=1 hz=0.03965702036441586, 21:ds=57 fs=58 fl=0 hz=0.061899679829242264, 24:ds=55 fs=44 fl=0 hz=0.048245614035087724, 6:ds=53 fs=23 fl=1 hz=0.025396825396825397, 13:ds=51 fs=21 fl=1 hz=0.024553571428571428

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=84 flags=purple
- S20: ds=71 flags=purple
- S6: ds=50 flags=purple
- S25: ds=48 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=30 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=24), P2:7 (gap=19), P3:6 (gap=29)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 371: score=46.516961071428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 376: score=45.36776607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 341: score=45.358540357142864 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 351: score=42.42821428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=41.70377857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 356: score=41.428914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 373: score=41.226488571428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 321: score=39.58580714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 871: score=39.102450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 311: score=38.97897857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=974 sev=B
- 288: ds=961 sev=B
- 255: ds=932 sev=B
- 668: ds=914 sev=B
- 199: ds=862 sev=B
- 499: ds=788 sev=B
- 399: ds=771 sev=B
- 039: ds=759 sev=B
- 448: ds=748 sev=B
- 005: ds=740 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=183 sev=red
  - 99: ds=130 sev=red
  - 77: ds=73 sev=blue
  - 33: ds=66 sev=purple
  - 22: ds=59 sev=purple
  - 88: ds=35 sev=purple
  - 44: ds=32 sev=purple
  - 66: ds=29 sev=purple
  - 11: ds=10 sev=-
  - 00: ds=9 sev=-
- non_repeating:
  - 59: ds=76 sev=red
  - 79: ds=70 sev=red
  - 12: ds=45 sev=blue
  - 78: ds=43 sev=blue
  - 06: ds=40 sev=blue
  - 35: ds=37 sev=blue
  - 56: ds=29 sev=purple
  - 69: ds=27 sev=purple
  - 16: ds=23 sev=-
  - 13: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:372, 1:357, 34:211, 16:169, 15:160, 32:137, 35:114, 18:100, 27:81, 28:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=372 fs=0 fl=0 hz=0.0, 1:ds=357 fs=2 fl=2 hz=0.009124087591240877, 34:ds=211 fs=19 fl=1 hz=0.02631578947368421, 16:ds=169 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=160 fs=23 fl=0 hz=0.029411764705882353, 32:ds=137 fs=3 fl=1 hz=0.006720430107526881, 35:ds=114 fs=1 fl=1 hz=0.0035587188612099642, 18:ds=100 fs=28 fl=0 hz=0.0343980343980344, 27:ds=81 fs=22 fl=2 hz=0.028605482717520857, 28:ds=59 fs=26 fl=2 hz=0.02997858672376874

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=91 flags=red+purple
- S22: ds=76 flags=purple
- S23: ds=64 flags=purple
- S3: ds=58 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 568: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT
  - 589: score=2 tags=FLT,PAT
  - 678: score=2 tags=FLT,PAT
  - 689: score=2 tags=FLT,PAT
  - 789: score=2 tags=FLT,PAT
  - 012: score=1 tags=PAT
  - 013: score=1 tags=PAT
  - 014: score=1 tags=PAT
  - 018: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=60 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=26), P2:1 (gap=32), P3:1 (gap=25)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 371: score=46.516961071428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 376: score=45.36776607142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 341: score=45.358540357142864 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 351: score=42.42821428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 346: score=41.70377857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 356: score=41.428914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 373: score=41.226488571428575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 321: score=39.58580714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 871: score=39.102450000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 311: score=38.97897857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=970 sev=B
- 009: ds=928 sev=B
- 255: ds=886 sev=B
- 138: ds=826 sev=B
- 117: ds=809 sev=B
- 158: ds=771 sev=B
- 344: ds=764 sev=B
- 199: ds=755 sev=B
- 112: ds=715 sev=B
- 277: ds=700 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=125 sev=red
  - 33: ds=67 sev=purple
  - 44: ds=38 sev=purple
  - 77: ds=36 sev=purple
  - 66: ds=34 sev=purple
  - 11: ds=25 sev=purple
  - 55: ds=18 sev=-
  - 00: ds=12 sev=-
  - 99: ds=3 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 68: ds=83 sev=red
  - 13: ds=61 sev=red
  - 07: ds=60 sev=red
  - 37: ds=55 sev=blue
  - 17: ds=50 sev=blue
  - 15: ds=48 sev=blue
  - 38: ds=47 sev=blue
  - 23: ds=44 sev=blue
  - 03: ds=42 sev=blue
  - 78: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:614, 23:153, 26:116, 18:113, 21:83, 13:62, 29:55, 33:47, 16:45, 30:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=614 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=153 fs=17 fl=2 hz=0.025165562913907286, 26:ds=116 fs=2 fl=1 hz=0.0056657223796034, 18:ds=113 fs=23 fl=2 hz=0.02910360884749709, 21:ds=83 fs=54 fl=0 hz=0.059275521405049394, 13:ds=62 fs=20 fl=1 hz=0.024881516587677725, 29:ds=55 fs=16 fl=3 hz=0.020540540540540542, 33:ds=47 fs=19 fl=3 hz=0.023255813953488372, 16:ds=45 fs=5 fl=3 hz=0.009523809523809525, 30:ds=44 fs=36 fl=1 hz=0.0387434554973822

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=86 flags=blue+purple
- S1: ds=71 flags=blue+purple
- S5: ds=68 flags=purple
- S24: ds=54 flags=blue+purple
- S3: ds=42 flags=purple
- S20: ds=36 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3', '7'], 'pairs': {'remaining_count': 0}}
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
  - 027: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:766(B); midday:759(B)
- 066 -> combined:990(B); midday:737(B)
- 199 -> evening:755(B); midday:862(B)
- 255 -> evening:886(B); midday:932(B)
- 344 -> combined:685(B); evening:764(B)
- 444 -> combined:791(B); evening:970(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:41(blue); evening:42(blue)
- 07 -> combined:39(blue); evening:60(red)
- 12 -> combined:44(blue); midday:45(blue)
- 13 -> combined:45(blue); evening:61(red)
- 33 -> combined:133(red); evening:67(purple); midday:66(purple)
- 35 -> combined:32(purple); midday:37(blue)
- 37 -> combined:29(purple); evening:55(blue)
- 38 -> combined:25(purple); evening:47(blue)
- 44 -> combined:65(purple); evening:38(purple); midday:32(purple)
- 55 -> combined:36(purple); midday:183(red)
- 66 -> combined:59(purple); evening:34(purple); midday:29(purple)
- 68 -> combined:27(purple); evening:83(red)
- 69 -> combined:30(purple); midday:27(purple)
- 77 -> combined:72(blue); evening:36(purple); midday:73(blue)
- 78 -> combined:66(red); evening:33(purple); midday:43(blue)
- 88 -> combined:71(blue); evening:125(red); midday:35(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(6.671100000000001)[R1,Mirror-Echo], 8(4.432714285714286)[R2,Mirror-Echo], 7(3.0994285714285716)[R3,XVAR-Cons(CM)], 4(1.0971)[R2,Double-Pressure], 1(1.0597999999999999)[R2,Double-Pressure]
- P2: 7(3.0172857142857143)[R3,XVAR-Cons(CM)], 4(2.8795285714285717)[R1,XVAR-Cons(CM)], 5(2.6046642857142857)[R2,XVAR-Cons(CE)], 1(1.6554285714285715)[R1,Double-Pressure], 2(1.2622571428571427)[R2,Mirror-Echo]
- P3: 1(8.15245)[R1,Mirror-Echo], 6(7.153149999999999)[R3,Mirror-Echo], 3(3.8507)[R2,XVAR-Cons(CE)], 5(1.2016)[R2,Double-Pressure]
