# Aux Summary — OntarioCanada4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=043, 006, 297, 313, 606
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=006, 313, 909, 497, 941
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2025-12-30/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=043, 297, 606, 056, 770

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=44 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=18), P2:8 (gap=16), P3:2 (gap=23)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 882: score=41.460971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=40.88250714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 888: score=37.43801357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 282: score=35.987096428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 862: score=35.4185 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=34.903971428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 162: score=34.84003571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 889: score=31.433721428571427 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.395542142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 112: score=31.277664285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 222: ds=995 sev=B
- 128: ds=915 sev=B
- 555: ds=880 sev=B
- 039: ds=771 sev=B
- 333: ds=742 sev=B
- 188: ds=715 sev=B
- 266: ds=701 sev=B
- 477: ds=699 sev=B
- 126: ds=691 sev=B
- 669: ds=686 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=117 sev=red
  - 55: ds=73 sev=blue
  - 11: ds=32 sev=purple
  - 88: ds=26 sev=purple
  - 44: ds=17 sev=-
  - 77: ds=8 sev=-
  - 99: ds=5 sev=-
  - 66: ds=4 sev=-
  - 33: ds=3 sev=-
  - 00: ds=1 sev=-
- non_repeating:
  - 89: ds=77 sev=red
  - 01: ds=52 sev=blue
  - 68: ds=50 sev=blue
  - 15: ds=49 sev=blue
  - 17: ds=43 sev=blue
  - 18: ds=43 sev=blue
  - 12: ds=29 sev=purple
  - 69: ds=28 sev=purple
  - 24: ds=27 sev=purple
  - 26: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:327, 16:281, 17:153, 27:144, 20:131, 33:77, 12:76, 26:71, 30:61, 34:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=327 fs=1 fl=0 hz=0.005698005698005698, 16:ds=281 fs=2 fl=0 hz=0.006329113924050633, 17:ds=153 fs=19 fl=1 hz=0.024242424242424242, 27:ds=144 fs=11 fl=4 hz=0.0178359096313912, 20:ds=131 fs=14 fl=2 hz=0.01853997682502897, 33:ds=77 fs=24 fl=1 hz=0.027472527472527472, 12:ds=76 fs=45 fl=0 hz=0.04928806133625411, 26:ds=71 fs=2 fl=1 hz=0.006075334143377886, 30:ds=61 fs=39 fl=1 hz=0.04405286343612335, 34:ds=58 fs=14 fl=2 hz=0.019698725376593278

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=95 flags=red+purple
- S23: ds=72 flags=blue+purple
- S21: ds=69 flags=purple
- S4: ds=63 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 028: score=3 tags=FLT,RS
  - 145: score=3 tags=FLT,RS
  - 235: score=3 tags=FLT,RS
  - 289: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS
  - 568: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 037: score=2 tags=RS
  - 046: score=2 tags=RS
  - 127: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=14 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=24), P2:7 (gap=20), P3:8 (gap=30)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 882: score=41.460971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=40.88250714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 888: score=37.43801357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 282: score=35.987096428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 862: score=35.4185 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=34.903971428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 162: score=34.84003571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 889: score=31.433721428571427 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.395542142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 112: score=31.277664285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 228: ds=992 sev=B
- 333: ds=975 sev=B
- 255: ds=942 sev=B
- 355: ds=907 sev=B
- 466: ds=828 sev=B
- 446: ds=736 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=58 sev=purple
  - 55: ds=36 sev=purple
  - 11: ds=26 sev=purple
  - 77: ds=19 sev=-
  - 88: ds=15 sev=-
  - 66: ds=10 sev=-
  - 44: ds=8 sev=-
  - 99: ds=2 sev=-
  - 33: ds=1 sev=-
  - 00: ds=0 sev=-
- non_repeating:
  - 34: ds=67 sev=red
  - 07: ds=64 sev=red
  - 04: ds=57 sev=red
  - 16: ds=50 sev=blue
  - 39: ds=38 sev=blue
  - 89: ds=38 sev=blue
  - 68: ds=34 sev=purple
  - 37: ds=33 sev=purple
  - 67: ds=33 sev=purple
  - 03: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:163, 34:158, 16:140, 27:95, 12:92, 14:77, 17:76, 20:65, 19:50, 24:40

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=163 fs=4 fl=3 hz=0.010432190760059612, 34:ds=158 fs=8 fl=4 hz=0.014423076923076924, 16:ds=140 fs=3 fl=0 hz=0.007462686567164179, 27:ds=95 fs=15 fl=2 hz=0.0189520624303233, 12:ds=92 fs=45 fl=0 hz=0.05079006772009029, 14:ds=77 fs=39 fl=0 hz=0.04276315789473684, 17:ds=76 fs=29 fl=2 hz=0.033879781420765025, 20:ds=65 fs=24 fl=3 hz=0.029315960912052113, 19:ds=50 fs=20 fl=2 hz=0.023732470334412083, 24:ds=40 fs=48 fl=0 hz=0.052805280528052806

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=74 flags=purple
- S25: ds=70 flags=purple
- S1: ds=59 flags=blue+purple
- S5: ds=57 flags=purple
- S8: ds=55 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 058: score=3 tags=FLT,RS
  - 148: score=3 tags=FLT,RS
  - 157: score=3 tags=FLT,RS
  - 238: score=3 tags=FLT,RS
  - 247: score=3 tags=FLT,RS
  - 256: score=3 tags=FLT,RS
  - 589: score=3 tags=FLT,RS
  - 013: score=2 tags=RS
  - 049: score=2 tags=RS
  - 067: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=51 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=14), P2:1 (gap=49), P3:9 (gap=36)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:1 (ds=49)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 882: score=41.460971428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=40.88250714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 888: score=37.43801357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 282: score=35.987096428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 862: score=35.4185 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 188: score=34.903971428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 162: score=34.84003571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 889: score=31.433721428571427 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 868: score=31.395542142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 112: score=31.277664285714287 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 128: ds=899 sev=B
- 113: ds=850 sev=B
- 378: ds=843 sev=B
- 566: ds=832 sev=B
- 199: ds=824 sev=B
- 899: ds=802 sev=B
- 126: ds=798 sev=B
- 559: ds=793 sev=B
- 477: ds=782 sev=B
- 558: ds=748 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=228 sev=red
  - 22: ds=59 sev=purple
  - 00: ds=46 sev=purple
  - 44: ds=29 sev=purple
  - 11: ds=16 sev=-
  - 99: ds=14 sev=-
  - 88: ds=13 sev=-
  - 33: ds=11 sev=-
  - 77: ds=4 sev=-
  - 66: ds=2 sev=-
- non_repeating:
  - 36: ds=71 sev=red
  - 24: ds=55 sev=blue
  - 18: ds=49 sev=blue
  - 89: ds=49 sev=blue
  - 15: ds=48 sev=blue
  - 78: ds=47 sev=blue
  - 49: ds=41 sev=blue
  - 57: ds=38 sev=blue
  - 09: ds=28 sev=purple
  - 01: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:424, 1:339, 16:190, 26:122, 18:107, 17:100, 20:91, 27:72, 3:70, 23:63

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=424 fs=0 fl=2 hz=0.005366726296958855, 1:ds=339 fs=0 fl=0 hz=0.0, 16:ds=190 fs=3 fl=1 hz=0.007853403141361256, 26:ds=122 fs=3 fl=3 hz=0.0076045627376425855, 18:ds=107 fs=16 fl=1 hz=0.019384264538198404, 17:ds=100 fs=13 fl=3 hz=0.018626309662398137, 20:ds=91 fs=15 fl=2 hz=0.01925254813137033, 27:ds=72 fs=12 fl=1 hz=0.015486725663716814, 3:ds=70 fs=16 fl=4 hz=0.02152852529601722, 23:ds=63 fs=25 fl=2 hz=0.03085714285714286

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=80 flags=purple
- S2: ds=70 flags=blue+purple
- S4: ds=68 flags=purple
- S25: ds=57 flags=purple
- S20: ds=50 flags=purple
- S9: ds=48 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 038: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 126 -> combined:691(B); evening:798(B)
- 128 -> combined:915(B); evening:899(B)
- 333 -> combined:742(B); midday:975(B)
- 477 -> combined:699(B); evening:782(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:52(blue); evening:26(purple); midday:26(purple)
- 11 -> combined:32(purple); midday:26(purple)
- 12 -> combined:29(purple); evening:26(purple)
- 15 -> combined:49(blue); evening:48(blue)
- 18 -> combined:43(blue); evening:49(blue)
- 22 -> combined:117(red); evening:59(purple); midday:58(purple)
- 24 -> combined:27(purple); evening:55(blue)
- 55 -> combined:73(blue); evening:228(red); midday:36(purple)
- 68 -> combined:50(blue); evening:25(purple); midday:34(purple)
- 69 -> combined:28(purple); midday:25(purple)
- 89 -> combined:77(red); evening:49(blue); midday:38(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(3.7464142857142857)[R1,XVAR-Cons(CM)], 8(3.3248785714285716)[R2,XVAR-Cons(CE)], 5(2.786285714285714)[R3,XVAR-Cons(CM)], 9(1.018)[R1,Double-Pressure], 3(0.3712928571428571)[R3,Mirror-Echo]
- P2: 8(6.463842857142857)[R1,Mirror-Echo], 6(2.9213714285714283)[R3,XVAR-Cons(CE)], 1(1.859)[R1,Mirror-Echo], 7(1.3404285714285713)[R1,Mirror-Echo], 3(1.2365714285714284)[R2,Mirror-Echo]
- P3: 2(6.67225)[R1,XVAR-Cons(CEM)], 8(3.1937142857142855)[R3,XVAR-Cons(CM)], 9(1.645)[R1,Double-Pressure], 4(0.974)[R2,Double-Pressure], 0(0.8508)[R2,Double-Pressure]
