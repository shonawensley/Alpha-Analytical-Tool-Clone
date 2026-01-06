# Aux Summary — Ohio4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/Ohio4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Ohio
- combined: live=`data/cleaned/draws/Ohio_draws.csv` snap=`sharepacks/2026-01-04/Ohio4/aux/draws/Ohio_draws.csv` n=1000 head=411, 563, 133, 747, 416
- midday: live=`data/cleaned/draws/Ohio_Midday_draws.csv` snap=`sharepacks/2026-01-04/Ohio4/aux/draws/Ohio_Midday_draws.csv` n=1000 head=563, 747, 746, 306, 338
- evening: live=`data/cleaned/draws/Ohio_Evening_draws.csv` snap=`sharepacks/2026-01-04/Ohio4/aux/draws/Ohio_Evening_draws.csv` n=1000 head=411, 133, 416, 197, 327

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=19 streak=1 max=2 last_repeat_gap=6 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=26), P2:7 (gap=45), P3:0 (gap=28)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=54.736014999999995 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=53.091286428571436 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 870: score=41.97949285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 060: score=40.79878642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 090: score=40.63919357142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 080: score=40.56635785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 850: score=40.334764285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 075: score=39.995464285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=39.07946428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.71075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 555: ds=967 sev=B
- 333: ds=964 sev=B
- 699: ds=900 sev=B
- 125: ds=765 sev=B
- 002: ds=719 sev=B
- 599: ds=717 sev=B
- 000: ds=697 sev=B
- 667: ds=690 sev=B
- 188: ds=687 sev=B
- 666: ds=677 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=120 sev=red
  - 00: ds=26 sev=purple
  - 22: ds=23 sev=-
  - 55: ds=20 sev=-
  - 88: ds=15 sev=-
  - 44: ds=14 sev=-
  - 99: ds=13 sev=-
  - 77: ds=3 sev=-
  - 33: ds=2 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 29: ds=84 sev=red
  - 25: ds=77 sev=red
  - 07: ds=59 sev=red
  - 02: ds=42 sev=blue
  - 89: ds=41 sev=blue
  - 39: ds=32 sev=purple
  - 59: ds=30 sev=purple
  - 08: ds=29 sev=purple
  - 04: ds=28 sev=purple
  - 45: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:303, 10:168, 35:131, 34:109, 5:82, 12:77, 17:57, 14:56, 18:52, 4:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=303 fs=1 fl=2 hz=0.01020408163265306, 10:ds=168 fs=21 fl=3 hz=0.02937576499388005, 35:ds=131 fs=0 fl=1 hz=0.003795066413662239, 34:ds=109 fs=25 fl=2 hz=0.030439684329199548, 5:ds=82 fs=14 fl=3 hz=0.01954022988505747, 12:ds=77 fs=40 fl=0 hz=0.04362050163576881, 17:ds=57 fs=23 fl=0 hz=0.025871766029246346, 14:ds=56 fs=43 fl=0 hz=0.04658721560130011, 18:ds=52 fs=20 fl=1 hz=0.024793388429752063, 4:ds=51 fs=21 fl=2 hz=0.02677532013969732

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S21: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S20: ds=58 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '8', '9'], 'pairs': {'remaining_count': 0}}
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

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=15 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=46), P2:5 (gap=27), P3:4 (gap=19)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:0 (ds=46)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=54.736014999999995 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=53.091286428571436 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 870: score=41.97949285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 060: score=40.79878642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 090: score=40.63919357142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 080: score=40.56635785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 850: score=40.334764285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 075: score=39.995464285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=39.07946428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.71075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=997 sev=B
- 688: ds=974 sev=B
- 788: ds=956 sev=B
- 222: ds=939 sev=B
- 699: ds=936 sev=B
- 224: ds=893 sev=B
- 022: ds=857 sev=B
- 258: ds=767 sev=B
- 119: ds=750 sev=B
- 557: ds=696 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=144 sev=red
  - 66: ds=82 sev=blue
  - 44: ds=31 sev=purple
  - 11: ds=28 sev=purple
  - 00: ds=25 sev=purple
  - 22: ds=11 sev=-
  - 88: ds=7 sev=-
  - 99: ds=6 sev=-
  - 33: ds=4 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 39: ds=70 sev=red
  - 02: ds=51 sev=blue
  - 29: ds=51 sev=blue
  - 79: ds=45 sev=blue
  - 05: ds=43 sev=blue
  - 25: ds=38 sev=blue
  - 04: ds=33 sev=purple
  - 48: ds=33 sev=purple
  - 07: ds=29 sev=purple
  - 16: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:151, 10:104, 1:87, 19:86, 18:82, 2:69, 35:65, 3:59, 34:54, 33:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=151 fs=2 fl=0 hz=0.004956629491945477, 10:ds=104 fs=22 fl=0 hz=0.028436018957345974, 1:ds=87 fs=3 fl=0 hz=0.005787037037037037, 19:ds=86 fs=12 fl=0 hz=0.01862464183381089, 18:ds=82 fs=15 fl=2 hz=0.020884520884520884, 2:ds=69 fs=17 fl=2 hz=0.020474137931034482, 35:ds=65 fs=0 fl=3 hz=0.004733727810650888, 3:ds=59 fs=17 fl=4 hz=0.022556390977443608, 34:ds=54 fs=28 fl=1 hz=0.032474804031354984, 33:ds=50 fs=20 fl=1 hz=0.022411953041622197

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=90 flags=purple
- S20: ds=76 flags=purple
- S5: ds=71 flags=purple
- S25: ds=66 flags=purple
- S24: ds=60 flags=purple
- S26: ds=54 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=3 tags=FLT,RS
  - 039: score=3 tags=FLT,RS
  - 129: score=3 tags=FLT,RS
  - 138: score=3 tags=FLT,RS
  - 147: score=3 tags=FLT,RS
  - 156: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 489: score=3 tags=FLT,RS
  - 579: score=3 tags=FLT,RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=19 streak=1 max=3 last_repeat_gap=12 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=20), P2:7 (gap=32), P3:9 (gap=28)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=54.736014999999995 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=53.091286428571436 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 870: score=41.97949285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 060: score=40.79878642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 090: score=40.63919357142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 080: score=40.56635785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 850: score=40.334764285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 075: score=39.995464285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=39.07946428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.71075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=996 sev=B
- 166: ds=945 sev=B
- 224: ds=941 sev=B
- 335: ds=895 sev=B
- 449: ds=874 sev=B
- 347: ds=867 sev=B
- 558: ds=825 sev=B
- 188: ds=799 sev=B
- 455: ds=798 sev=B
- 007: ds=711 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=100 sev=blue
  - 66: ds=60 sev=purple
  - 99: ds=55 sev=purple
  - 88: ds=37 sev=purple
  - 77: ds=17 sev=-
  - 00: ds=13 sev=-
  - 55: ds=10 sev=-
  - 44: ds=7 sev=-
  - 33: ds=1 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 03: ds=74 sev=red
  - 45: ds=71 sev=red
  - 25: ds=56 sev=red
  - 29: ds=42 sev=blue
  - 89: ds=42 sev=blue
  - 67: ds=39 sev=blue
  - 07: ds=32 sev=purple
  - 35: ds=28 sev=purple
  - 36: ds=26 sev=purple
  - 78: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:329, 16:290, 32:265, 26:172, 13:119, 17:89, 10:84, 4:74, 12:71, 34:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=329 fs=0 fl=0 hz=0.001834862385321101, 16:ds=290 fs=1 fl=0 hz=0.0030534351145038168, 32:ds=265 fs=0 fl=0 hz=0.0, 26:ds=172 fs=4 fl=0 hz=0.007874015748031496, 13:ds=119 fs=20 fl=2 hz=0.02546296296296296, 17:ds=89 fs=21 fl=1 hz=0.02463605823068309, 10:ds=84 fs=27 fl=2 hz=0.03172866520787746, 4:ds=74 fs=18 fl=2 hz=0.023529411764705882, 12:ds=71 fs=45 fl=0 hz=0.0487012987012987, 34:ds=55 fs=26 fl=2 hz=0.029723991507430995

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S4: ds=93 flags=purple
- S3: ds=74 flags=purple
- S22: ds=68 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '5', '8'], 'pairs': {'remaining_count': 0}}
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
- 188 -> combined:687(B); evening:799(B)
- 224 -> evening:941(B); midday:893(B)
- 699 -> combined:900(B); midday:936(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:26(purple); midday:25(purple)
- 02 -> combined:42(blue); midday:51(blue)
- 04 -> combined:28(purple); midday:33(purple)
- 07 -> combined:59(red); evening:32(purple); midday:29(purple)
- 25 -> combined:77(red); evening:56(red); midday:38(blue)
- 29 -> combined:84(red); evening:42(blue); midday:51(blue)
- 39 -> combined:32(purple); midday:70(red)
- 45 -> combined:25(purple); evening:71(red)
- 66 -> combined:120(red); evening:60(purple); midday:82(blue)
- 89 -> combined:41(blue); evening:42(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.618235714285715)[R1,XVAR-Cons(CEM)], 8(2.7026642857142855)[R2,XVAR-Cons(CM)], 9(2.576457142857143)[R3,XVAR-Cons(CE)], 5(1.3765357142857142)[R1,Mirror-Echo], 2(1.1298)[R2,Double-Pressure]
- P2: 7(8.42522857142857)[R1,XVAR-Cons(CEM)], 5(6.7805)[R2,XVAR-Cons(CEM)], 6(0.48799999999999993)[R2,Swap], 9(0.32840714285714284)[R3,Swap], 8(0.25557142857142856)[R3,Swap]
- P3: 0(6.8515999999999995)[R1,Mirror-Echo], 9(1.536)[R1,Double-Pressure], 5(1.452)[R2,Mirror-Echo], 4(1.1672857142857143)[R1,Double-Pressure], 8(1.1389)[R2,Double-Pressure]
