# Aux Summary — Michigan4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/Michigan4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Michigan
- combined: live=`data/cleaned/draws/Michigan_draws.csv` snap=`sharepacks/2025-06-22/Michigan4/aux/draws/Michigan_draws.csv` n=1000 head=280, 432, 117, 139, 156
- midday: live=`data/cleaned/draws/Michigan_Midday_draws.csv` snap=`sharepacks/2025-06-22/Michigan4/aux/draws/Michigan_Midday_draws.csv` n=1000 head=432, 139, 516, 408, 618
- evening: live=`data/cleaned/draws/Michigan_Evening_draws.csv` snap=`sharepacks/2025-06-22/Michigan4/aux/draws/Michigan_Evening_draws.csv` n=1000 head=280, 117, 156, 216, 339

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=3 last_repeat_gap=5 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=25), P2:2 (gap=62), P3:5 (gap=17)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:2 (ds=62)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 021: score=45.14575714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 025: score=44.083414285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 024: score=42.00369285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 023: score=40.95925714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 028: score=40.86317142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 027: score=39.885 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 721: score=38.551857142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 725: score=37.489514285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 071: score=37.11412857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 075: score=36.051785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=978 sev=B
- 299: ds=944 sev=B
- 000: ds=911 sev=B
- 357: ds=853 sev=B
- 037: ds=838 sev=B
- 033: ds=806 sev=B
- 677: ds=753 sev=B
- 228: ds=721 sev=B
- 225: ds=720 sev=B
- 388: ds=711 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=119 sev=red
  - 99: ds=74 sev=blue
  - 22: ds=72 sev=blue
  - 66: ds=56 sev=purple
  - 55: ds=54 sev=purple
  - 77: ds=41 sev=purple
  - 44: ds=21 sev=-
  - 00: ds=11 sev=-
  - 33: ds=8 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 79: ds=51 sev=blue
  - 06: ds=50 sev=blue
  - 05: ds=47 sev=blue
  - 37: ds=43 sev=blue
  - 57: ds=37 sev=blue
  - 89: ds=36 sev=purple
  - 07: ds=35 sev=purple
  - 59: ds=34 sev=purple
  - 35: ds=30 sev=purple
  - 69: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:573, 26:255, 2:195, 4:161, 3:101, 16:96, 28:82, 9:80, 1:78, 35:74

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=573 fs=3 fl=2 hz=0.012594458438287152, 26:ds=255 fs=1 fl=1 hz=0.006, 2:ds=195 fs=14 fl=1 hz=0.0201765447667087, 4:ds=161 fs=26 fl=3 hz=0.03580246913580247, 3:ds=101 fs=23 fl=1 hz=0.027491408934707903, 16:ds=96 fs=2 fl=1 hz=0.005567928730512249, 28:ds=82 fs=25 fl=1 hz=0.03155339805825243, 9:ds=80 fs=46 fl=0 hz=0.05094130675526024, 1:ds=78 fs=4 fl=2 hz=0.008938547486033519, 35:ds=74 fs=3 fl=3 hz=0.007990867579908675

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=74 flags=purple
- S18: ds=65 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=2 tags=RS
  - 026: score=2 tags=RS
  - 035: score=2 tags=RS
  - 089: score=2 tags=RS
  - 125: score=2 tags=RS
  - 134: score=2 tags=RS
  - 179: score=2 tags=RS
  - 269: score=2 tags=RS
  - 278: score=2 tags=RS
  - 359: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=23 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=24), P2:2 (gap=71), P3:1 (gap=29)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:2 (ds=71)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 021: score=45.14575714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 025: score=44.083414285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 024: score=42.00369285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 023: score=40.95925714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 028: score=40.86317142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 027: score=39.885 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 721: score=38.551857142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 725: score=37.489514285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 071: score=37.11412857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 075: score=36.051785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=997 sev=B
- 166: ds=940 sev=B
- 007: ds=934 sev=B
- 199: ds=900 sev=B
- 339: ds=803 sev=B
- 266: ds=775 sev=B
- 356: ds=755 sev=B
- 037: ds=752 sev=B
- 336: ds=676 sev=B
- 667: ds=672 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=213 sev=red
  - 99: ds=120 sev=red
  - 88: ds=59 sev=purple
  - 22: ds=58 sev=purple
  - 55: ds=50 sev=purple
  - 66: ds=40 sev=purple
  - 77: ds=20 sev=-
  - 44: ds=10 sev=-
  - 33: ds=6 sev=-
  - 00: ds=5 sev=-
- non_repeating:
  - 12: ds=147 sev=red
  - 06: ds=74 sev=red
  - 25: ds=44 sev=blue
  - 59: ds=44 sev=blue
  - 46: ds=37 sev=blue
  - 35: ds=34 sev=purple
  - 14: ds=29 sev=purple
  - 36: ds=27 sev=purple
  - 79: ds=25 sev=purple
  - 89: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:286, 35:271, 16:213, 1:186, 26:127, 2:97, 4:80, 28:58, 33:56, 3:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=286 fs=5 fl=3 hz=0.011594202898550725, 35:ds=271 fs=2 fl=3 hz=0.00896057347670251, 16:ds=213 fs=3 fl=0 hz=0.005471956224350205, 1:ds=186 fs=2 fl=1 hz=0.01, 26:ds=127 fs=0 fl=1 hz=0.005249343832020997, 2:ds=97 fs=15 fl=3 hz=0.02, 4:ds=80 fs=32 fl=0 hz=0.03636363636363636, 28:ds=58 fs=20 fl=2 hz=0.02363050483351235, 33:ds=56 fs=9 fl=3 hz=0.013086150490730643, 3:ds=50 fs=30 fl=0 hz=0.03161222339304531

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=86 flags=purple
- S25: ds=59 flags=purple

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
- current_index=11 streak=1 max=3 last_repeat_gap=33 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=27), P2:2 (gap=31), P3:3 (gap=15)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 021: score=45.14575714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 025: score=44.083414285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 024: score=42.00369285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 023: score=40.95925714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 028: score=40.86317142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 027: score=39.885 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 721: score=38.551857142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 725: score=37.489514285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 071: score=37.11412857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 075: score=36.051785714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=974 sev=B
- 222: ds=946 sev=B
- 489: ds=915 sev=B
- 899: ds=904 sev=B
- 025: ds=828 sev=B
- 244: ds=821 sev=B
- 447: ds=819 sev=B
- 017: ds=782 sev=B
- 778: ds=722 sev=B
- 046: ds=709 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=103 sev=blue
  - 00: ds=66 sev=purple
  - 99: ds=37 sev=purple
  - 22: ds=36 sev=purple
  - 66: ds=28 sev=purple
  - 55: ds=27 sev=purple
  - 44: ds=24 sev=-
  - 77: ds=22 sev=-
  - 33: ds=4 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 07: ds=97 sev=red
  - 57: ds=75 sev=red
  - 04: ds=51 sev=blue
  - 79: ds=47 sev=blue
  - 13: ds=43 sev=blue
  - 05: ds=39 sev=blue
  - 37: ds=30 sev=purple
  - 47: ds=29 sev=purple
  - 69: ds=28 sev=purple
  - 06: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:372, 2:206, 13:157, 26:156, 4:114, 23:87, 31:82, 10:75, 3:66, 27:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=372 fs=2 fl=0 hz=0.017699115044247787, 2:ds=206 fs=18 fl=1 hz=0.027104136947218263, 13:ds=157 fs=22 fl=0 hz=0.02666666666666667, 26:ds=156 fs=1 fl=2 hz=0.006501950585175552, 4:ds=114 fs=16 fl=2 hz=0.02100350058343057, 23:ds=87 fs=22 fl=1 hz=0.031123139377537214, 31:ds=82 fs=23 fl=0 hz=0.02811735941320293, 10:ds=75 fs=27 fl=2 hz=0.031938325991189426, 3:ds=66 fs=21 fl=1 hz=0.027848101265822787, 27:ds=55 fs=27 fl=2 hz=0.030752916224814426

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=74 flags=purple
- S2: ds=66 flags=purple
- S23: ds=63 flags=purple
- S6: ds=51 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 124: score=1 tags=FLT
  - 134: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 001 -> combined:978(B); midday:997(B)
- 037 -> combined:838(B); midday:752(B)
- 677 -> combined:753(B); evening:693(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:47(blue); evening:39(blue)
- 06 -> combined:50(blue); evening:25(purple); midday:74(red)
- 07 -> combined:35(purple); evening:97(red)
- 22 -> combined:72(blue); evening:36(purple); midday:58(purple)
- 35 -> combined:30(purple); midday:34(purple)
- 37 -> combined:43(blue); evening:30(purple)
- 55 -> combined:54(purple); evening:27(purple); midday:50(purple)
- 57 -> combined:37(blue); evening:75(red)
- 59 -> combined:34(purple); midday:44(blue)
- 66 -> combined:56(purple); evening:28(purple); midday:40(purple)
- 69 -> combined:29(purple); evening:28(purple)
- 79 -> combined:51(blue); evening:47(blue); midday:25(purple)
- 88 -> combined:119(red); evening:103(blue); midday:59(purple)
- 89 -> combined:36(purple); midday:25(purple)
- 99 -> combined:74(blue); evening:37(purple); midday:120(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(6.950471428571429)[R1,XVAR-Cons(CEM)], 7(3.8565714285714288)[R2,XVAR-Cons(CM)], 5(1.686642857142857)[R1,Mirror-Echo], 3(1.0389)[R2,Double-Pressure], 9(0.32840714285714284)[R3,Swap]
- P2: 2(9.337428571428571)[R1,Mirror-Echo], 7(3.8057999999999996)[R3,Mirror-Echo], 6(2.7292285714285716)[R2,XVAR-Cons(CE)], 5(1.1806999999999999)[R2,Double-Pressure], 9(0.31497142857142857)[R3,Swap]
- P3: 1(3.857857142857143)[R2,XVAR-Cons(CM)], 5(2.795514285714286)[R1,XVAR-Cons(CE)], 4(1.7157928571428571)[R3,XVAR-Cons(CM)], 3(1.1713571428571428)[R1,Mirror-Echo], 7(1.0971)[R2,Double-Pressure]
