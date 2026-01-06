# Aux Summary — Pennsylvania4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=221, 684, 173, 186, 460
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=684, 186, 239, 502, 264
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-01/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=221, 173, 460, 422, 065

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=3 last_repeat_gap=21 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=33), P2:4 (gap=26), P3:7 (gap=13)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 315: score=35.44205714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 345: score=35.27345714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 317: score=35.05525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 717: score=34.92414785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 355: score=34.89087857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 347: score=34.88665 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 747: score=34.75554785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 357: score=34.50407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 757: score=34.372969285714284 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 715: score=32.73708571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=994 sev=B
- 666: ds=992 sev=B
- 159: ds=880 sev=B
- 007: ds=877 sev=B
- 088: ds=841 sev=B
- 008: ds=819 sev=B
- 444: ds=795 sev=B
- 039: ds=770 sev=B
- 355: ds=760 sev=B
- 344: ds=689 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=137 sev=red
  - 77: ds=76 sev=blue
  - 88: ds=75 sev=blue
  - 44: ds=69 sev=purple
  - 66: ds=63 sev=purple
  - 55: ds=40 sev=purple
  - 11: ds=25 sev=purple
  - 00: ds=23 sev=-
  - 99: ds=10 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 78: ds=70 sev=red
  - 03: ds=45 sev=blue
  - 07: ds=43 sev=blue
  - 35: ds=36 sev=purple
  - 69: ds=34 sev=purple
  - 36: ds=31 sev=purple
  - 09: ds=30 sev=purple
  - 34: ds=29 sev=purple
  - 38: ds=29 sev=purple
  - 19: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:279, 26:236, 16:94, 27:70, 7:62, 6:57, 13:55, 19:51, 10:46, 31:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=279 fs=2 fl=1 hz=0.007380073800738007, 26:ds=236 fs=0 fl=1 hz=0.003898635477582846, 16:ds=94 fs=3 fl=2 hz=0.007371007371007371, 27:ds=70 fs=11 fl=4 hz=0.01722158438576349, 7:ds=62 fs=36 fl=1 hz=0.03965702036441586, 6:ds=57 fs=22 fl=1 hz=0.02454642475987193, 13:ds=55 fs=21 fl=1 hz=0.024553571428571428, 19:ds=51 fs=21 fl=3 hz=0.025695931477516063, 10:ds=46 fs=23 fl=2 hz=0.02676659528907923, 31:ds=42 fs=22 fl=2 hz=0.02531645569620253

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=88 flags=purple
- S20: ds=75 flags=purple
- S6: ds=54 flags=purple
- S25: ds=52 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=32 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=26), P2:7 (gap=21), P3:5 (gap=26)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 315: score=35.44205714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 345: score=35.27345714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 317: score=35.05525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 717: score=34.92414785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 355: score=34.89087857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 347: score=34.88665 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 747: score=34.75554785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 357: score=34.50407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 757: score=34.372969285714284 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 715: score=32.73708571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=976 sev=B
- 288: ds=963 sev=B
- 255: ds=934 sev=B
- 668: ds=916 sev=B
- 199: ds=864 sev=B
- 499: ds=790 sev=B
- 399: ds=773 sev=B
- 039: ds=761 sev=B
- 448: ds=750 sev=B
- 005: ds=742 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=185 sev=red
  - 99: ds=132 sev=red
  - 77: ds=75 sev=blue
  - 33: ds=68 sev=purple
  - 22: ds=61 sev=purple
  - 88: ds=37 sev=purple
  - 44: ds=34 sev=purple
  - 66: ds=31 sev=purple
  - 11: ds=12 sev=-
  - 00: ds=11 sev=-
- non_repeating:
  - 59: ds=78 sev=red
  - 79: ds=72 sev=red
  - 12: ds=47 sev=blue
  - 78: ds=45 sev=blue
  - 06: ds=42 sev=blue
  - 35: ds=39 sev=blue
  - 56: ds=31 sev=purple
  - 69: ds=29 sev=purple
  - 13: ds=24 sev=-
  - 57: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:374, 1:359, 34:213, 16:171, 15:162, 32:139, 35:116, 27:83, 28:61, 5:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=374 fs=0 fl=0 hz=0.0, 1:ds=359 fs=2 fl=2 hz=0.009124087591240877, 34:ds=213 fs=19 fl=1 hz=0.02631578947368421, 16:ds=171 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=162 fs=23 fl=0 hz=0.029411764705882353, 32:ds=139 fs=3 fl=1 hz=0.006720430107526881, 35:ds=116 fs=1 fl=1 hz=0.0035587188612099642, 27:ds=83 fs=22 fl=2 hz=0.028605482717520857, 28:ds=61 fs=26 fl=2 hz=0.02997858672376874, 5:ds=46 fs=18 fl=2 hz=0.022175290390707498

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=93 flags=red+purple
- S22: ds=78 flags=purple
- S23: ds=66 flags=purple
- S3: ds=60 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 567: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT
  - 579: score=2 tags=FLT,PAT
  - 678: score=2 tags=FLT,PAT
  - 679: score=2 tags=FLT,PAT
  - 789: score=2 tags=FLT,PAT
  - 012: score=1 tags=PAT
  - 013: score=1 tags=PAT
  - 014: score=1 tags=PAT
  - 017: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=3 last_repeat_gap=62 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=28), P2:1 (gap=34), P3:6 (gap=18)
- consensus_notes: P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 315: score=35.44205714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 345: score=35.27345714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 317: score=35.05525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 717: score=34.92414785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R3 src=cartesian
- 355: score=34.89087857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 347: score=34.88665 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 747: score=34.75554785714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 357: score=34.50407142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 757: score=34.372969285714284 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 715: score=32.73708571428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=972 sev=B
- 009: ds=930 sev=B
- 255: ds=888 sev=B
- 138: ds=828 sev=B
- 117: ds=811 sev=B
- 158: ds=773 sev=B
- 344: ds=766 sev=B
- 199: ds=757 sev=B
- 112: ds=717 sev=B
- 277: ds=702 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=127 sev=red
  - 33: ds=69 sev=purple
  - 44: ds=40 sev=purple
  - 77: ds=38 sev=purple
  - 66: ds=36 sev=purple
  - 11: ds=27 sev=purple
  - 55: ds=20 sev=-
  - 00: ds=14 sev=-
  - 99: ds=5 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 68: ds=85 sev=red
  - 07: ds=62 sev=red
  - 15: ds=50 sev=blue
  - 38: ds=49 sev=blue
  - 23: ds=46 sev=blue
  - 03: ds=44 sev=blue
  - 78: ds=35 sev=purple
  - 19: ds=34 sev=purple
  - 28: ds=33 sev=purple
  - 01: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:616, 23:155, 26:118, 18:115, 13:64, 29:57, 33:49, 16:47, 30:46, 24:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=616 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=155 fs=17 fl=2 hz=0.025165562913907286, 26:ds=118 fs=2 fl=1 hz=0.0056657223796034, 18:ds=115 fs=23 fl=2 hz=0.02910360884749709, 13:ds=64 fs=20 fl=1 hz=0.024881516587677725, 29:ds=57 fs=16 fl=3 hz=0.020540540540540542, 33:ds=49 fs=19 fl=3 hz=0.023255813953488372, 16:ds=47 fs=5 fl=3 hz=0.009523809523809525, 30:ds=46 fs=35 fl=1 hz=0.03829787234042553, 24:ds=43 fs=37 fl=0 hz=0.04048140043763676

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=88 flags=blue+purple
- S1: ds=73 flags=blue+purple
- S24: ds=56 flags=blue+purple
- S3: ds=44 flags=purple
- S20: ds=38 flags=purple
- S6: ds=27 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:770(B); midday:761(B)
- 066 -> combined:994(B); midday:739(B)
- 199 -> evening:757(B); midday:864(B)
- 255 -> evening:888(B); midday:934(B)
- 344 -> combined:689(B); evening:766(B)
- 444 -> combined:795(B); evening:972(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:45(blue); evening:44(blue)
- 07 -> combined:43(blue); evening:62(red)
- 11 -> combined:25(purple); evening:27(purple)
- 19 -> combined:27(purple); evening:34(purple)
- 33 -> combined:137(red); evening:69(purple); midday:68(purple)
- 35 -> combined:36(purple); midday:39(blue)
- 38 -> combined:29(purple); evening:49(blue)
- 44 -> combined:69(purple); evening:40(purple); midday:34(purple)
- 55 -> combined:40(purple); midday:185(red)
- 66 -> combined:63(purple); evening:36(purple); midday:31(purple)
- 69 -> combined:34(purple); midday:29(purple)
- 77 -> combined:76(blue); evening:38(purple); midday:75(blue)
- 78 -> combined:70(red); evening:35(purple); midday:45(blue)
- 88 -> combined:75(blue); evening:127(red); midday:37(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(7.681914285714286)[R1,Mirror-Echo], 7(5.976942857142857)[R3,XVAR-Cons(CEM)], 8(4.724428571428572)[R2,Mirror-Echo], 4(1.1389)[R2,Double-Pressure]
- P2: 1(3.270714285714286)[R3,XVAR-Cons(CE)], 4(3.102114285714286)[R1,XVAR-Cons(CM)], 5(2.719535714285714)[R2,XVAR-Cons(CE)], 7(1.4979999999999998)[R1,Mirror-Echo], 2(1.3312)[R2,Mirror-Echo]
- P3: 5(2.9894285714285713)[R3,XVAR-Cons(CM)], 7(2.6026214285714286)[R1,XVAR-Cons(CE)], 1(1.2225)[R2,Double-Pressure], 6(1.2074285714285713)[R1,Double-Pressure], 9(0.9834999999999999)[R2,Double-Pressure]
