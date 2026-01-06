# Aux Summary — Pennsylvania4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-02/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=328, 322, 221, 684, 173
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-02/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=322, 684, 186, 239, 502
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-02/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=328, 221, 173, 460, 422

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=3 last_repeat_gap=23 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=31), P2:4 (gap=28), P3:7 (gap=15)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 755: score=42.42041142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 757: score=41.90871285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 855: score=39.619150000000005 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=38.63457142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 857: score=38.57192142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 859: score=38.36640714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=37.70268428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.126241428571426 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 745: score=35.681285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 845: score=35.41312142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=996 sev=B
- 666: ds=994 sev=B
- 159: ds=882 sev=B
- 007: ds=879 sev=B
- 088: ds=843 sev=B
- 008: ds=821 sev=B
- 444: ds=797 sev=B
- 039: ds=772 sev=B
- 355: ds=762 sev=B
- 344: ds=691 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=139 sev=red
  - 77: ds=78 sev=blue
  - 88: ds=77 sev=blue
  - 44: ds=71 sev=blue
  - 66: ds=65 sev=purple
  - 55: ds=42 sev=purple
  - 11: ds=27 sev=purple
  - 00: ds=25 sev=purple
  - 99: ds=12 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 78: ds=72 sev=red
  - 03: ds=47 sev=blue
  - 07: ds=45 sev=blue
  - 35: ds=38 sev=blue
  - 69: ds=36 sev=purple
  - 36: ds=33 sev=purple
  - 09: ds=32 sev=purple
  - 34: ds=31 sev=purple
  - 19: ds=29 sev=purple
  - 47: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:281, 26:238, 16:96, 7:64, 6:59, 13:57, 19:53, 10:48, 31:44, 1:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=281 fs=2 fl=1 hz=0.007380073800738007, 26:ds=238 fs=0 fl=1 hz=0.003898635477582846, 16:ds=96 fs=3 fl=2 hz=0.007371007371007371, 7:ds=64 fs=36 fl=1 hz=0.03965702036441586, 6:ds=59 fs=22 fl=1 hz=0.02454642475987193, 13:ds=57 fs=21 fl=1 hz=0.024553571428571428, 19:ds=53 fs=21 fl=3 hz=0.025695931477516063, 10:ds=48 fs=23 fl=2 hz=0.02676659528907923, 31:ds=44 fs=22 fl=2 hz=0.02531645569620253, 1:ds=42 fs=1 fl=2 hz=0.0044742729306487695

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=90 flags=purple
- S20: ds=77 flags=purple
- S6: ds=56 flags=purple
- S25: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=3 last_repeat_gap=33 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=27), P2:7 (gap=22), P3:5 (gap=27)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 755: score=42.42041142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 757: score=41.90871285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 855: score=39.619150000000005 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=38.63457142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 857: score=38.57192142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 859: score=38.36640714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=37.70268428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.126241428571426 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 745: score=35.681285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 845: score=35.41312142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=977 sev=B
- 288: ds=964 sev=B
- 255: ds=935 sev=B
- 668: ds=917 sev=B
- 199: ds=865 sev=B
- 499: ds=791 sev=B
- 399: ds=774 sev=B
- 039: ds=762 sev=B
- 448: ds=751 sev=B
- 005: ds=743 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=186 sev=red
  - 99: ds=133 sev=red
  - 77: ds=76 sev=blue
  - 33: ds=69 sev=purple
  - 88: ds=38 sev=purple
  - 44: ds=35 sev=purple
  - 66: ds=32 sev=purple
  - 11: ds=13 sev=-
  - 00: ds=12 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 59: ds=79 sev=red
  - 79: ds=73 sev=red
  - 12: ds=48 sev=blue
  - 78: ds=46 sev=blue
  - 06: ds=43 sev=blue
  - 35: ds=40 sev=blue
  - 56: ds=32 sev=purple
  - 69: ds=30 sev=purple
  - 13: ds=25 sev=purple
  - 57: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:375, 1:360, 34:214, 16:172, 15:163, 32:140, 35:117, 28:62, 5:47, 2:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=375 fs=0 fl=0 hz=0.0, 1:ds=360 fs=2 fl=2 hz=0.009124087591240877, 34:ds=214 fs=19 fl=1 hz=0.02631578947368421, 16:ds=172 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=163 fs=23 fl=0 hz=0.029411764705882353, 32:ds=140 fs=3 fl=1 hz=0.006720430107526881, 35:ds=117 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=62 fs=26 fl=2 hz=0.02997858672376874, 5:ds=47 fs=18 fl=2 hz=0.022175290390707498, 2:ds=43 fs=18 fl=3 hz=0.022316684378320933

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=94 flags=red+purple
- S22: ds=79 flags=purple
- S23: ds=67 flags=purple
- S3: ds=61 flags=blue+purple

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
- current_index=29 streak=1 max=3 last_repeat_gap=63 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=29), P2:1 (gap=35), P3:6 (gap=19)
- consensus_notes: P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 755: score=42.42041142857143 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 757: score=41.90871285714286 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 855: score=39.619150000000005 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 759: score=38.63457142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 857: score=38.57192142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 859: score=38.36640714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 747: score=37.70268428571429 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 717: score=37.126241428571426 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 745: score=35.681285714285714 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 845: score=35.41312142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=973 sev=B
- 009: ds=931 sev=B
- 255: ds=889 sev=B
- 138: ds=829 sev=B
- 117: ds=812 sev=B
- 158: ds=774 sev=B
- 344: ds=767 sev=B
- 199: ds=758 sev=B
- 112: ds=718 sev=B
- 277: ds=703 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=128 sev=red
  - 33: ds=70 sev=purple
  - 44: ds=41 sev=purple
  - 77: ds=39 sev=purple
  - 66: ds=37 sev=purple
  - 11: ds=28 sev=purple
  - 55: ds=21 sev=-
  - 00: ds=15 sev=-
  - 99: ds=6 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 68: ds=86 sev=red
  - 07: ds=63 sev=red
  - 15: ds=51 sev=blue
  - 03: ds=45 sev=blue
  - 78: ds=36 sev=purple
  - 19: ds=35 sev=purple
  - 01: ds=29 sev=purple
  - 18: ds=29 sev=purple
  - 14: ds=28 sev=purple
  - 39: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:617, 23:156, 26:119, 18:116, 13:65, 33:50, 16:48, 30:47, 24:44, 27:36

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=617 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=156 fs=17 fl=2 hz=0.025165562913907286, 26:ds=119 fs=2 fl=1 hz=0.0056657223796034, 18:ds=116 fs=23 fl=2 hz=0.02910360884749709, 13:ds=65 fs=20 fl=1 hz=0.024881516587677725, 33:ds=50 fs=19 fl=3 hz=0.023255813953488372, 16:ds=48 fs=5 fl=3 hz=0.009523809523809525, 30:ds=47 fs=35 fl=1 hz=0.03829787234042553, 24:ds=44 fs=37 fl=0 hz=0.04048140043763676, 27:ds=36 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=89 flags=blue+purple
- S1: ds=74 flags=blue+purple
- S24: ds=57 flags=blue+purple
- S3: ds=45 flags=purple
- S20: ds=39 flags=purple
- S6: ds=28 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:772(B); midday:762(B)
- 066 -> combined:996(B); midday:740(B)
- 199 -> evening:758(B); midday:865(B)
- 255 -> evening:889(B); midday:935(B)
- 344 -> combined:691(B); evening:767(B)
- 444 -> combined:797(B); evening:973(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:47(blue); evening:45(blue)
- 07 -> combined:45(blue); evening:63(red)
- 11 -> combined:27(purple); evening:28(purple)
- 19 -> combined:29(purple); evening:35(purple)
- 33 -> combined:139(red); evening:70(purple); midday:69(purple)
- 35 -> combined:38(blue); midday:40(blue)
- 44 -> combined:71(blue); evening:41(purple); midday:35(purple)
- 55 -> combined:42(purple); midday:186(red)
- 66 -> combined:65(purple); evening:37(purple); midday:32(purple)
- 69 -> combined:36(purple); midday:30(purple)
- 77 -> combined:78(blue); evening:39(purple); midday:76(blue)
- 78 -> combined:72(red); evening:36(purple); midday:46(blue)
- 88 -> combined:77(blue); evening:128(red); midday:38(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(7.549842857142857)[R2,XVAR-Cons(CEM)], 8(7.2816785714285714)[R1,XVAR-Cons(CEM)], 4(1.1598)[R2,Double-Pressure], 9(0.23971428571428574)[R3,Swap], 6(0.20435714285714285)[R3,Swap]
- P2: 5(5.611328571428572)[R2,XVAR-Cons(CEM)], 4(3.9053)[R1,XVAR-Cons(CM)], 1(3.328857142857143)[R3,XVAR-Cons(CE)], 7(1.3568571428571428)[R1,Double-Pressure], 3(1.0971)[R2,Double-Pressure]
- P3: 5(3.7261428571428574)[R2,XVAR-Cons(CM)], 7(2.678914285714286)[R1,XVAR-Cons(CE)], 9(2.4734)[R3,XVAR-Cons(CE)], 1(1.2433999999999998)[R2,Double-Pressure], 6(1.2372857142857143)[R1,Double-Pressure]
