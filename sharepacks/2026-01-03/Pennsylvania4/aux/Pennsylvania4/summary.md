# Aux Summary — Pennsylvania4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=360, 871, 328, 322, 221
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=871, 322, 684, 186, 239
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-03/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=360, 328, 221, 173, 460

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=25 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=28), P2:4 (gap=30), P3:7 (gap=17)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 757: score=42.707256428571434 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 755: score=40.872907142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=39.65549285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=39.05430642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 745: score=37.21995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.07009214285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 753: score=36.793778571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 749: score=36.002542857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 756: score=35.84005 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 715: score=35.23574285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=998 sev=B
- 666: ds=996 sev=B
- 159: ds=884 sev=B
- 007: ds=881 sev=B
- 088: ds=845 sev=B
- 008: ds=823 sev=B
- 444: ds=799 sev=B
- 039: ds=774 sev=B
- 355: ds=764 sev=B
- 344: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=141 sev=red
  - 77: ds=80 sev=blue
  - 88: ds=79 sev=blue
  - 44: ds=73 sev=blue
  - 66: ds=67 sev=purple
  - 55: ds=44 sev=purple
  - 11: ds=29 sev=purple
  - 00: ds=27 sev=purple
  - 99: ds=14 sev=-
  - 22: ds=3 sev=-
- non_repeating:
  - 07: ds=47 sev=blue
  - 35: ds=40 sev=blue
  - 69: ds=38 sev=blue
  - 09: ds=34 sev=purple
  - 34: ds=33 sev=purple
  - 19: ds=31 sev=purple
  - 47: ds=26 sev=purple
  - 15: ds=23 sev=-
  - 45: ds=20 sev=-
  - 08: ds=19 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:283, 26:240, 16:98, 7:66, 6:61, 13:59, 19:55, 10:50, 31:46, 1:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=283 fs=2 fl=1 hz=0.007380073800738007, 26:ds=240 fs=0 fl=1 hz=0.003898635477582846, 16:ds=98 fs=3 fl=2 hz=0.007371007371007371, 7:ds=66 fs=36 fl=1 hz=0.03965702036441586, 6:ds=61 fs=22 fl=1 hz=0.02454642475987193, 13:ds=59 fs=21 fl=1 hz=0.024553571428571428, 19:ds=55 fs=21 fl=3 hz=0.025695931477516063, 10:ds=50 fs=23 fl=2 hz=0.02676659528907923, 31:ds=46 fs=22 fl=2 hz=0.02531645569620253, 1:ds=44 fs=1 fl=2 hz=0.0044742729306487695

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=92 flags=purple
- S20: ds=79 flags=purple
- S6: ds=58 flags=purple
- S25: ds=56 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 045: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=34 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=28), P2:4 (gap=18), P3:5 (gap=28)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 757: score=42.707256428571434 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 755: score=40.872907142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=39.65549285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=39.05430642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 745: score=37.21995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.07009214285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 753: score=36.793778571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 749: score=36.002542857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 756: score=35.84005 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 715: score=35.23574285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=978 sev=B
- 288: ds=965 sev=B
- 255: ds=936 sev=B
- 668: ds=918 sev=B
- 199: ds=866 sev=B
- 499: ds=792 sev=B
- 399: ds=775 sev=B
- 039: ds=763 sev=B
- 448: ds=752 sev=B
- 005: ds=744 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=187 sev=red
  - 99: ds=134 sev=red
  - 77: ds=77 sev=blue
  - 33: ds=70 sev=purple
  - 88: ds=39 sev=purple
  - 44: ds=36 sev=purple
  - 66: ds=33 sev=purple
  - 11: ds=14 sev=-
  - 00: ds=13 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 59: ds=80 sev=red
  - 79: ds=74 sev=red
  - 12: ds=49 sev=blue
  - 06: ds=44 sev=blue
  - 35: ds=41 sev=blue
  - 56: ds=33 sev=purple
  - 69: ds=31 sev=purple
  - 13: ds=26 sev=purple
  - 57: ds=25 sev=purple
  - 03: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:376, 1:361, 34:215, 16:173, 15:164, 32:141, 35:118, 28:63, 5:48, 2:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=376 fs=0 fl=0 hz=0.0, 1:ds=361 fs=2 fl=2 hz=0.009124087591240877, 34:ds=215 fs=19 fl=1 hz=0.02631578947368421, 16:ds=173 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=164 fs=23 fl=0 hz=0.029411764705882353, 32:ds=141 fs=3 fl=1 hz=0.006720430107526881, 35:ds=118 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=63 fs=26 fl=2 hz=0.02997858672376874, 5:ds=48 fs=18 fl=2 hz=0.022175290390707498, 2:ds=44 fs=18 fl=3 hz=0.022316684378320933

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=95 flags=red+purple
- S22: ds=80 flags=purple
- S23: ds=68 flags=purple
- S3: ds=62 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT
  - 568: score=2 tags=FLT,PAT
  - 569: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=64 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=30), P2:1 (gap=36), P3:6 (gap=20)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 757: score=42.707256428571434 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 755: score=40.872907142857144 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=39.65549285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=39.05430642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 745: score=37.21995714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.07009214285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 753: score=36.793778571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 749: score=36.002542857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 756: score=35.84005 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 715: score=35.23574285714285 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=974 sev=B
- 009: ds=932 sev=B
- 255: ds=890 sev=B
- 138: ds=830 sev=B
- 117: ds=813 sev=B
- 158: ds=775 sev=B
- 344: ds=768 sev=B
- 199: ds=759 sev=B
- 112: ds=719 sev=B
- 277: ds=704 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=129 sev=red
  - 33: ds=71 sev=blue
  - 44: ds=42 sev=purple
  - 77: ds=40 sev=purple
  - 66: ds=38 sev=purple
  - 11: ds=29 sev=purple
  - 55: ds=22 sev=-
  - 00: ds=16 sev=-
  - 99: ds=7 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 68: ds=87 sev=red
  - 07: ds=64 sev=red
  - 15: ds=52 sev=blue
  - 78: ds=37 sev=blue
  - 19: ds=36 sev=purple
  - 01: ds=30 sev=purple
  - 18: ds=30 sev=purple
  - 14: ds=29 sev=purple
  - 39: ds=27 sev=purple
  - 16: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:618, 23:157, 26:120, 18:117, 13:66, 33:51, 16:49, 30:48, 24:45, 27:37

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=618 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=157 fs=17 fl=2 hz=0.025165562913907286, 26:ds=120 fs=2 fl=1 hz=0.0056657223796034, 18:ds=117 fs=23 fl=2 hz=0.02910360884749709, 13:ds=66 fs=20 fl=1 hz=0.024881516587677725, 33:ds=51 fs=19 fl=3 hz=0.023255813953488372, 16:ds=49 fs=5 fl=3 hz=0.009523809523809525, 30:ds=48 fs=35 fl=1 hz=0.03829787234042553, 24:ds=45 fs=37 fl=0 hz=0.04048140043763676, 27:ds=37 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=90 flags=blue+purple
- S1: ds=75 flags=blue+purple
- S24: ds=58 flags=blue+purple
- S3: ds=46 flags=purple
- S20: ds=40 flags=purple
- S6: ds=29 flags=purple

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

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:774(B); midday:763(B)
- 066 -> combined:998(B); midday:741(B)
- 199 -> evening:759(B); midday:866(B)
- 255 -> evening:890(B); midday:936(B)
- 344 -> combined:693(B); evening:768(B)
- 444 -> combined:799(B); evening:974(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:47(blue); evening:64(red)
- 11 -> combined:29(purple); evening:29(purple)
- 19 -> combined:31(purple); evening:36(purple)
- 33 -> combined:141(red); evening:71(blue); midday:70(purple)
- 35 -> combined:40(blue); midday:41(blue)
- 44 -> combined:73(blue); evening:42(purple); midday:36(purple)
- 55 -> combined:44(purple); midday:187(red)
- 66 -> combined:67(purple); evening:38(purple); midday:33(purple)
- 69 -> combined:38(blue); midday:31(purple)
- 77 -> combined:80(blue); evening:40(purple); midday:77(blue)
- 88 -> combined:79(blue); evening:129(red); midday:39(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(7.708600000000001)[R1,XVAR-Cons(CEM)], 9(2.798035714285714)[R2,XVAR-Cons(CM)], 8(1.4957142857142856)[R1,Double-Pressure], 4(1.2723071428571429)[R2,Mirror-Echo], 0(0.23971428571428574)[R3,Swap]
- P2: 5(6.364307142857142)[R2,XVAR-Cons(CEM)], 4(4.211357142857143)[R1,XVAR-Cons(CM)], 1(3.227142857142857)[R3,XVAR-Cons(CE)], 3(1.1179999999999999)[R2,Double-Pressure], 9(0.4786428571428571)[R3,Mirror-Echo]
- P3: 5(3.8)[R2,XVAR-Cons(CM)], 9(2.5825857142857145)[R3,XVAR-Cons(CE)], 7(2.555207142857143)[R1,XVAR-Cons(CE)], 6(1.2671428571428571)[R1,Double-Pressure], 3(1.2208714285714284)[R2,Mirror-Echo]
