# Aux Summary — Michigan4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/Michigan4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Michigan
- combined: live=`data/cleaned/draws/Michigan_draws.csv` snap=`sharepacks/2025-06-21/Michigan4/aux/draws/Michigan_draws.csv` n=1000 head=117, 139, 156, 516, 216
- midday: live=`data/cleaned/draws/Michigan_Midday_draws.csv` snap=`sharepacks/2025-06-21/Michigan4/aux/draws/Michigan_Midday_draws.csv` n=1000 head=139, 516, 408, 618, 900
- evening: live=`data/cleaned/draws/Michigan_Evening_draws.csv` snap=`sharepacks/2025-06-21/Michigan4/aux/draws/Michigan_Evening_draws.csv` n=1000 head=117, 156, 216, 339, 239

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=3 last_repeat_gap=3 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=23), P2:2 (gap=60), P3:5 (gap=15)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:2 (ds=60)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 021: score=44.908921428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 020: score=42.906333571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 024: score=41.798992857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 023: score=40.59080714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 025: score=39.79635 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 027: score=39.701121428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 721: score=38.35192857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 071: score=36.866749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 724: score=35.242 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 070: score=34.86416214285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=976 sev=B
- 299: ds=942 sev=B
- 000: ds=909 sev=B
- 357: ds=851 sev=B
- 037: ds=836 sev=B
- 033: ds=804 sev=B
- 677: ds=751 sev=B
- 228: ds=719 sev=B
- 225: ds=718 sev=B
- 388: ds=709 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=117 sev=red
  - 99: ds=72 sev=blue
  - 22: ds=70 sev=purple
  - 66: ds=54 sev=purple
  - 55: ds=52 sev=purple
  - 77: ds=39 sev=purple
  - 44: ds=19 sev=-
  - 00: ds=9 sev=-
  - 33: ds=6 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 79: ds=49 sev=blue
  - 06: ds=48 sev=blue
  - 05: ds=45 sev=blue
  - 37: ds=41 sev=blue
  - 57: ds=35 sev=purple
  - 89: ds=34 sev=purple
  - 07: ds=33 sev=purple
  - 59: ds=32 sev=purple
  - 35: ds=28 sev=purple
  - 69: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:571, 26:253, 2:193, 4:159, 3:99, 16:94, 28:80, 9:78, 1:76, 35:72

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=571 fs=3 fl=2 hz=0.012594458438287152, 26:ds=253 fs=1 fl=1 hz=0.005369127516778523, 2:ds=193 fs=14 fl=1 hz=0.0201765447667087, 4:ds=159 fs=26 fl=3 hz=0.03580246913580247, 3:ds=99 fs=24 fl=1 hz=0.027777777777777776, 16:ds=94 fs=2 fl=1 hz=0.005567928730512249, 28:ds=80 fs=25 fl=1 hz=0.03155339805825243, 9:ds=78 fs=46 fl=0 hz=0.05094130675526024, 1:ds=76 fs=4 fl=2 hz=0.008938547486033519, 35:ds=72 fs=3 fl=3 hz=0.007990867579908675

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=72 flags=purple
- S18: ds=63 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '4', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=3 tags=FLT,RS
  - 026: score=3 tags=FLT,RS
  - 035: score=3 tags=FLT,RS
  - 089: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 368: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 467: score=3 tags=FLT,RS
  - 125: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=22 last_repeat_index=5

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=23), P2:2 (gap=70), P3:1 (gap=28)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:2 (ds=70)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 021: score=44.908921428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 020: score=42.906333571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 024: score=41.798992857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 023: score=40.59080714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 025: score=39.79635 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 027: score=39.701121428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 721: score=38.35192857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 071: score=36.866749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 724: score=35.242 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 070: score=34.86416214285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=996 sev=B
- 166: ds=939 sev=B
- 007: ds=933 sev=B
- 199: ds=899 sev=B
- 339: ds=802 sev=B
- 266: ds=774 sev=B
- 356: ds=754 sev=B
- 037: ds=751 sev=B
- 336: ds=675 sev=B
- 667: ds=671 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=212 sev=red
  - 99: ds=119 sev=red
  - 88: ds=58 sev=purple
  - 22: ds=57 sev=purple
  - 55: ds=49 sev=purple
  - 66: ds=39 sev=purple
  - 77: ds=19 sev=-
  - 44: ds=9 sev=-
  - 33: ds=5 sev=-
  - 00: ds=4 sev=-
- non_repeating:
  - 12: ds=146 sev=red
  - 06: ds=73 sev=red
  - 25: ds=43 sev=blue
  - 59: ds=43 sev=blue
  - 46: ds=36 sev=purple
  - 35: ds=33 sev=purple
  - 14: ds=28 sev=purple
  - 34: ds=27 sev=purple
  - 36: ds=26 sev=purple
  - 79: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:285, 35:270, 16:212, 1:185, 26:126, 2:96, 4:79, 28:57, 33:55, 3:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=285 fs=5 fl=3 hz=0.011594202898550725, 35:ds=270 fs=2 fl=3 hz=0.00896057347670251, 16:ds=212 fs=3 fl=0 hz=0.005471956224350205, 1:ds=185 fs=2 fl=1 hz=0.01, 26:ds=126 fs=0 fl=1 hz=0.005249343832020997, 2:ds=96 fs=16 fl=3 hz=0.021040974529346623, 4:ds=79 fs=32 fl=0 hz=0.03636363636363636, 28:ds=57 fs=20 fl=2 hz=0.02363050483351235, 33:ds=55 fs=9 fl=3 hz=0.013086150490730643, 3:ds=49 fs=30 fl=0 hz=0.03161222339304531

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=85 flags=purple
- S25: ds=58 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '7'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 037: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=3 last_repeat_gap=32 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=26), P2:2 (gap=30), P3:0 (gap=65)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:0 (ds=65)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 021: score=44.908921428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 020: score=42.906333571428576 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 024: score=41.798992857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 023: score=40.59080714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 025: score=39.79635 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 027: score=39.701121428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 721: score=38.35192857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 071: score=36.866749999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 724: score=35.242 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 070: score=34.86416214285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=973 sev=B
- 222: ds=945 sev=B
- 489: ds=914 sev=B
- 899: ds=903 sev=B
- 025: ds=827 sev=B
- 244: ds=820 sev=B
- 447: ds=818 sev=B
- 017: ds=781 sev=B
- 778: ds=721 sev=B
- 046: ds=708 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=102 sev=blue
  - 00: ds=65 sev=purple
  - 99: ds=36 sev=purple
  - 22: ds=35 sev=purple
  - 66: ds=27 sev=purple
  - 55: ds=26 sev=purple
  - 44: ds=23 sev=-
  - 77: ds=21 sev=-
  - 33: ds=3 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 07: ds=96 sev=red
  - 57: ds=74 sev=red
  - 04: ds=50 sev=blue
  - 79: ds=46 sev=blue
  - 13: ds=42 sev=blue
  - 05: ds=38 sev=blue
  - 37: ds=29 sev=purple
  - 47: ds=28 sev=purple
  - 69: ds=27 sev=purple
  - 06: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:371, 2:205, 13:156, 26:155, 4:113, 23:86, 31:81, 10:74, 3:65, 27:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=371 fs=2 fl=0 hz=0.017699115044247787, 2:ds=205 fs=18 fl=1 hz=0.027104136947218263, 13:ds=156 fs=22 fl=0 hz=0.02666666666666667, 26:ds=155 fs=1 fl=2 hz=0.006501950585175552, 4:ds=113 fs=16 fl=2 hz=0.02100350058343057, 23:ds=86 fs=22 fl=1 hz=0.031123139377537214, 31:ds=81 fs=23 fl=0 hz=0.02811735941320293, 10:ds=74 fs=27 fl=2 hz=0.031938325991189426, 3:ds=65 fs=21 fl=1 hz=0.027848101265822787, 27:ds=54 fs=27 fl=2 hz=0.030752916224814426

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=73 flags=purple
- S2: ds=65 flags=purple
- S23: ds=62 flags=purple
- S6: ds=50 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '4', '8'], 'pairs': {'remaining_count': 0}}
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
  - 024: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 001 -> combined:976(B); midday:996(B)
- 037 -> combined:836(B); midday:751(B)
- 677 -> combined:751(B); evening:692(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:45(blue); evening:38(blue)
- 06 -> combined:48(blue); midday:73(red)
- 07 -> combined:33(purple); evening:96(red)
- 22 -> combined:70(purple); evening:35(purple); midday:57(purple)
- 35 -> combined:28(purple); midday:33(purple)
- 37 -> combined:41(blue); evening:29(purple)
- 55 -> combined:52(purple); evening:26(purple); midday:49(purple)
- 57 -> combined:35(purple); evening:74(red)
- 59 -> combined:32(purple); midday:43(blue)
- 66 -> combined:54(purple); evening:27(purple); midday:39(purple)
- 69 -> combined:27(purple); evening:27(purple)
- 79 -> combined:49(blue); evening:46(blue)
- 88 -> combined:117(red); evening:102(blue); midday:58(purple)
- 99 -> combined:72(blue); evening:36(purple); midday:119(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(6.839707142857143)[R1,XVAR-Cons(CEM)], 7(3.7827142857142855)[R2,XVAR-Cons(CM)], 5(1.6472857142857142)[R1,Mirror-Echo], 3(1.018)[R2,Double-Pressure], 9(0.31497142857142857)[R3,Swap]
- P2: 2(9.285214285714286)[R1,Mirror-Echo], 7(3.743042857142857)[R3,Mirror-Echo], 6(2.671792857142857)[R2,XVAR-Cons(CE)], 5(1.1598)[R2,Double-Pressure], 9(0.30153571428571424)[R3,Swap]
- P3: 1(3.784)[R2,XVAR-Cons(CM)], 0(1.7149999999999999)[R1,Double-Pressure], 4(1.6740714285714287)[R3,XVAR-Cons(CM)], 5(1.1714285714285715)[R1,Double-Pressure], 7(1.0761999999999998)[R2,Double-Pressure]
