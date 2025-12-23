# Aux Summary — Michigan4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/Michigan4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Michigan
- combined: live=`data/cleaned/draws/Michigan_draws.csv` snap=`sharepacks/2025-06-23/Michigan4/aux/draws/Michigan_draws.csv` n=1000 head=700, 309, 280, 432, 117
- midday: live=`data/cleaned/draws/Michigan_Midday_draws.csv` snap=`sharepacks/2025-06-23/Michigan4/aux/draws/Michigan_Midday_draws.csv` n=1000 head=309, 432, 139, 516, 408
- evening: live=`data/cleaned/draws/Michigan_Evening_draws.csv` snap=`sharepacks/2025-06-23/Michigan4/aux/draws/Michigan_Evening_draws.csv` n=1000 head=700, 280, 117, 156, 216

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=3 last_repeat_gap=7 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=27), P2:2 (gap=64), P3:5 (gap=19)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:2 (ds=64)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 021: score=49.161072857142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 025: score=44.94972142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 024: score=42.83542857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 023: score=41.788628571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 028: score=41.68765714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 027: score=40.69591428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 071: score=38.058542857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 821: score=37.08027857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 075: score=36.99863571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 825: score=36.02037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=980 sev=B
- 299: ds=946 sev=B
- 000: ds=913 sev=B
- 357: ds=855 sev=B
- 037: ds=840 sev=B
- 033: ds=808 sev=B
- 677: ds=755 sev=B
- 228: ds=723 sev=B
- 225: ds=722 sev=B
- 388: ds=713 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=121 sev=red
  - 99: ds=76 sev=blue
  - 22: ds=74 sev=blue
  - 66: ds=58 sev=purple
  - 55: ds=56 sev=purple
  - 77: ds=43 sev=purple
  - 44: ds=23 sev=-
  - 33: ds=10 sev=-
  - 11: ds=4 sev=-
  - 00: ds=0 sev=-
- non_repeating:
  - 79: ds=53 sev=blue
  - 06: ds=52 sev=blue
  - 05: ds=49 sev=blue
  - 37: ds=45 sev=blue
  - 57: ds=39 sev=blue
  - 89: ds=38 sev=blue
  - 59: ds=36 sev=purple
  - 35: ds=32 sev=purple
  - 69: ds=31 sev=purple
  - 27: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:575, 26:257, 2:197, 4:163, 16:98, 28:84, 9:82, 1:80, 35:76, 34:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=575 fs=3 fl=2 hz=0.012594458438287152, 26:ds=257 fs=1 fl=1 hz=0.006, 2:ds=197 fs=14 fl=1 hz=0.0201765447667087, 4:ds=163 fs=26 fl=3 hz=0.03580246913580247, 16:ds=98 fs=2 fl=1 hz=0.005567928730512249, 28:ds=84 fs=25 fl=1 hz=0.03155339805825243, 9:ds=82 fs=46 fl=0 hz=0.05094130675526024, 1:ds=80 fs=4 fl=2 hz=0.008938547486033519, 35:ds=76 fs=3 fl=3 hz=0.007990867579908675, 34:ds=69 fs=20 fl=2 hz=0.024175824175824173

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=76 flags=purple
- S18: ds=67 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['5', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 026: score=3 tags=FLT,RS
  - 035: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 134: score=3 tags=PAT,RS
  - 269: score=3 tags=FLT,RS
  - 359: score=3 tags=FLT,RS
  - 368: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 467: score=3 tags=FLT,RS
  - 017: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=24 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=25), P2:2 (gap=72), P3:1 (gap=30)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:2 (ds=72)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 021: score=49.161072857142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 025: score=44.94972142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 024: score=42.83542857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 023: score=41.788628571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 028: score=41.68765714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 027: score=40.69591428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 071: score=38.058542857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 821: score=37.08027857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 075: score=36.99863571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 825: score=36.02037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=998 sev=B
- 166: ds=941 sev=B
- 007: ds=935 sev=B
- 199: ds=901 sev=B
- 339: ds=804 sev=B
- 266: ds=776 sev=B
- 356: ds=756 sev=B
- 037: ds=753 sev=B
- 336: ds=677 sev=B
- 667: ds=673 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=214 sev=red
  - 99: ds=121 sev=red
  - 88: ds=60 sev=purple
  - 22: ds=59 sev=purple
  - 55: ds=51 sev=purple
  - 66: ds=41 sev=purple
  - 77: ds=21 sev=-
  - 44: ds=11 sev=-
  - 33: ds=7 sev=-
  - 00: ds=6 sev=-
- non_repeating:
  - 12: ds=148 sev=red
  - 06: ds=75 sev=red
  - 25: ds=45 sev=blue
  - 59: ds=45 sev=blue
  - 46: ds=38 sev=blue
  - 35: ds=35 sev=purple
  - 14: ds=30 sev=purple
  - 36: ds=28 sev=purple
  - 79: ds=26 sev=purple
  - 89: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:287, 35:272, 16:214, 1:187, 26:128, 2:98, 4:81, 28:59, 33:57, 3:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=287 fs=5 fl=3 hz=0.011594202898550725, 35:ds=272 fs=2 fl=3 hz=0.00896057347670251, 16:ds=214 fs=3 fl=0 hz=0.005471956224350205, 1:ds=187 fs=2 fl=1 hz=0.01, 26:ds=128 fs=0 fl=1 hz=0.005249343832020997, 2:ds=98 fs=15 fl=3 hz=0.02, 4:ds=81 fs=32 fl=0 hz=0.03636363636363636, 28:ds=59 fs=20 fl=2 hz=0.02363050483351235, 33:ds=57 fs=9 fl=3 hz=0.013086150490730643, 3:ds=51 fs=29 fl=0 hz=0.031115879828326178

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=87 flags=purple
- S25: ds=60 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 017: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 067: score=1 tags=FLT
  - 078: score=1 tags=FLT
  - 079: score=1 tags=FLT
  - 127: score=1 tags=FLT
  - 137: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=3 last_repeat_gap=34 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=28), P2:2 (gap=32), P3:3 (gap=16)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 021: score=49.161072857142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 025: score=44.94972142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 024: score=42.83542857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 023: score=41.788628571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 028: score=41.68765714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 027: score=40.69591428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 071: score=38.058542857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 821: score=37.08027857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 075: score=36.99863571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 825: score=36.02037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=975 sev=B
- 222: ds=947 sev=B
- 489: ds=916 sev=B
- 899: ds=905 sev=B
- 025: ds=829 sev=B
- 244: ds=822 sev=B
- 447: ds=820 sev=B
- 017: ds=783 sev=B
- 778: ds=723 sev=B
- 046: ds=710 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=104 sev=blue
  - 99: ds=38 sev=purple
  - 22: ds=37 sev=purple
  - 66: ds=29 sev=purple
  - 55: ds=28 sev=purple
  - 44: ds=25 sev=purple
  - 77: ds=23 sev=-
  - 33: ds=5 sev=-
  - 11: ds=2 sev=-
  - 00: ds=0 sev=-
- non_repeating:
  - 57: ds=76 sev=red
  - 04: ds=52 sev=blue
  - 79: ds=48 sev=blue
  - 13: ds=44 sev=blue
  - 05: ds=40 sev=blue
  - 37: ds=31 sev=purple
  - 47: ds=30 sev=purple
  - 69: ds=29 sev=purple
  - 06: ds=26 sev=purple
  - 38: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:373, 2:207, 13:158, 26:157, 4:115, 23:88, 31:83, 10:76, 27:56, 34:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=373 fs=2 fl=0 hz=0.017699115044247787, 2:ds=207 fs=18 fl=1 hz=0.027104136947218263, 13:ds=158 fs=22 fl=0 hz=0.02666666666666667, 26:ds=157 fs=1 fl=2 hz=0.006501950585175552, 4:ds=115 fs=16 fl=2 hz=0.02100350058343057, 23:ds=88 fs=22 fl=1 hz=0.031123139377537214, 31:ds=83 fs=23 fl=0 hz=0.02811735941320293, 10:ds=76 fs=27 fl=2 hz=0.031938325991189426, 27:ds=56 fs=27 fl=2 hz=0.030752916224814426, 34:ds=51 fs=14 fl=2 hz=0.018909899888765295

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=75 flags=purple
- S2: ds=67 flags=purple
- S23: ds=64 flags=purple
- S6: ds=52 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '4', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 001 -> combined:980(B); midday:998(B)
- 037 -> combined:840(B); midday:753(B)
- 677 -> combined:755(B); evening:694(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:49(blue); evening:40(blue)
- 06 -> combined:52(blue); evening:26(purple); midday:75(red)
- 22 -> combined:74(blue); evening:37(purple); midday:59(purple)
- 35 -> combined:32(purple); midday:35(purple)
- 37 -> combined:45(blue); evening:31(purple)
- 47 -> combined:25(purple); evening:30(purple)
- 55 -> combined:56(purple); evening:28(purple); midday:51(purple)
- 57 -> combined:39(blue); evening:76(red)
- 59 -> combined:36(purple); midday:45(blue)
- 66 -> combined:58(purple); evening:29(purple); midday:41(purple)
- 69 -> combined:31(purple); evening:29(purple)
- 79 -> combined:53(blue); evening:48(blue); midday:26(purple)
- 88 -> combined:121(red); evening:104(blue); midday:60(purple)
- 89 -> combined:38(blue); midday:26(purple)
- 99 -> combined:76(blue); evening:38(purple); midday:121(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.758271428571429)[R1,XVAR-Cons(CEM)], 8(2.3289214285714284)[R2,XVAR-Cons(CM)], 9(1.9257)[R3,XVAR-Cons(CE)], 5(1.726)[R1,Mirror-Echo], 7(1.4464285714285714)[R1,Double-Pressure]
- P2: 2(9.319642857142856)[R1,Mirror-Echo], 7(3.868557142857143)[R3,Mirror-Echo], 6(2.786664285714286)[R2,XVAR-Cons(CE)], 5(1.2016)[R2,Double-Pressure], 9(0.32840714285714284)[R3,Swap]
- P3: 1(3.9317142857142855)[R2,XVAR-Cons(CM)], 5(2.8718071428571426)[R1,XVAR-Cons(CE)], 4(1.7575142857142856)[R3,XVAR-Cons(CM)], 3(1.2107142857142856)[R1,Mirror-Echo], 7(1.1179999999999999)[R2,Double-Pressure]
