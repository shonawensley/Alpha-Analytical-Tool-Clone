# Aux Summary — Ohio4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/Ohio4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Ohio
- combined: live=`data/cleaned/draws/Ohio_draws.csv` snap=`sharepacks/2026-01-03/Ohio4/aux/draws/Ohio_draws.csv` n=1000 head=133, 747, 416, 746, 197
- midday: live=`data/cleaned/draws/Ohio_Midday_draws.csv` snap=`sharepacks/2026-01-03/Ohio4/aux/draws/Ohio_Midday_draws.csv` n=1000 head=747, 746, 306, 338, 187
- evening: live=`data/cleaned/draws/Ohio_Evening_draws.csv` snap=`sharepacks/2026-01-03/Ohio4/aux/draws/Ohio_Evening_draws.csv` n=1000 head=133, 416, 197, 327, 694

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=2 last_repeat_gap=4 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=24), P2:7 (gap=43), P3:0 (gap=26)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=54.71508357142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=53.03381928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 060: score=44.889855000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 570: score=44.29830714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 550: score=42.617042857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 090: score=40.65558357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 075: score=40.01227142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=39.13898571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.770271428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 055: score=38.33100714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 555: ds=965 sev=B
- 333: ds=962 sev=B
- 699: ds=898 sev=B
- 125: ds=763 sev=B
- 002: ds=717 sev=B
- 599: ds=715 sev=B
- 000: ds=695 sev=B
- 667: ds=688 sev=B
- 188: ds=685 sev=B
- 666: ds=675 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=118 sev=red
  - 11: ds=55 sev=purple
  - 00: ds=24 sev=-
  - 22: ds=21 sev=-
  - 55: ds=18 sev=-
  - 88: ds=13 sev=-
  - 44: ds=12 sev=-
  - 99: ds=11 sev=-
  - 77: ds=1 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 29: ds=82 sev=red
  - 25: ds=75 sev=red
  - 07: ds=57 sev=red
  - 35: ds=47 sev=blue
  - 02: ds=40 sev=blue
  - 89: ds=39 sev=blue
  - 56: ds=36 sev=purple
  - 39: ds=30 sev=purple
  - 59: ds=28 sev=purple
  - 08: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:301, 10:166, 35:129, 34:107, 5:80, 12:75, 17:55, 14:54, 18:50, 4:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=301 fs=1 fl=2 hz=0.01020408163265306, 10:ds=166 fs=21 fl=3 hz=0.02937576499388005, 35:ds=129 fs=0 fl=1 hz=0.003795066413662239, 34:ds=107 fs=25 fl=2 hz=0.030439684329199548, 5:ds=80 fs=14 fl=3 hz=0.01954022988505747, 12:ds=75 fs=40 fl=0 hz=0.04362050163576881, 17:ds=55 fs=24 fl=0 hz=0.02542372881355932, 14:ds=54 fs=43 fl=0 hz=0.04658721560130011, 18:ds=50 fs=20 fl=1 hz=0.024793388429752063, 4:ds=49 fs=21 fl=2 hz=0.02677532013969732

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
- S20: ds=56 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '5', '8'], 'pairs': {'remaining_count': 0}}
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
- current_index=28 streak=1 max=3 last_repeat_gap=14 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=45), P2:5 (gap=26), P3:4 (gap=18)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:0 (ds=45)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=54.71508357142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=53.03381928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 060: score=44.889855000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 570: score=44.29830714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 550: score=42.617042857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 090: score=40.65558357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 075: score=40.01227142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=39.13898571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.770271428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 055: score=38.33100714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=996 sev=B
- 688: ds=973 sev=B
- 788: ds=955 sev=B
- 222: ds=938 sev=B
- 699: ds=935 sev=B
- 224: ds=892 sev=B
- 022: ds=856 sev=B
- 258: ds=766 sev=B
- 119: ds=749 sev=B
- 557: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=143 sev=red
  - 66: ds=81 sev=blue
  - 44: ds=30 sev=purple
  - 11: ds=27 sev=purple
  - 00: ds=24 sev=-
  - 22: ds=10 sev=-
  - 88: ds=6 sev=-
  - 99: ds=5 sev=-
  - 33: ds=3 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 39: ds=69 sev=red
  - 02: ds=50 sev=blue
  - 29: ds=50 sev=blue
  - 79: ds=44 sev=blue
  - 05: ds=42 sev=blue
  - 25: ds=37 sev=blue
  - 04: ds=32 sev=purple
  - 48: ds=32 sev=purple
  - 07: ds=28 sev=purple
  - 16: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:150, 10:103, 1:86, 19:85, 18:81, 2:68, 35:64, 3:58, 34:53, 33:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=150 fs=2 fl=0 hz=0.004956629491945477, 10:ds=103 fs=22 fl=0 hz=0.028436018957345974, 1:ds=86 fs=3 fl=0 hz=0.005787037037037037, 19:ds=85 fs=12 fl=0 hz=0.01862464183381089, 18:ds=81 fs=15 fl=2 hz=0.020884520884520884, 2:ds=68 fs=17 fl=2 hz=0.020474137931034482, 35:ds=64 fs=0 fl=3 hz=0.004733727810650888, 3:ds=58 fs=17 fl=4 hz=0.022556390977443608, 34:ds=53 fs=28 fl=1 hz=0.032474804031354984, 33:ds=49 fs=20 fl=1 hz=0.022411953041622197

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=89 flags=purple
- S20: ds=75 flags=purple
- S5: ds=70 flags=purple
- S25: ds=65 flags=purple
- S24: ds=59 flags=purple
- S26: ds=53 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=3 last_repeat_gap=11 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=19), P2:7 (gap=31), P3:9 (gap=27)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=54.71508357142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=53.03381928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 060: score=44.889855000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 570: score=44.29830714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 550: score=42.617042857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 090: score=40.65558357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 075: score=40.01227142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=39.13898571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.770271428571434 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 055: score=38.33100714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=995 sev=B
- 166: ds=944 sev=B
- 224: ds=940 sev=B
- 335: ds=894 sev=B
- 449: ds=873 sev=B
- 347: ds=866 sev=B
- 558: ds=824 sev=B
- 188: ds=798 sev=B
- 455: ds=797 sev=B
- 007: ds=710 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=99 sev=blue
  - 66: ds=59 sev=purple
  - 99: ds=54 sev=purple
  - 11: ds=51 sev=purple
  - 88: ds=36 sev=purple
  - 77: ds=16 sev=-
  - 00: ds=12 sev=-
  - 55: ds=9 sev=-
  - 44: ds=6 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 03: ds=73 sev=red
  - 45: ds=70 sev=red
  - 25: ds=55 sev=blue
  - 29: ds=41 sev=blue
  - 89: ds=41 sev=blue
  - 67: ds=38 sev=blue
  - 07: ds=31 sev=purple
  - 35: ds=27 sev=purple
  - 36: ds=25 sev=purple
  - 78: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:328, 16:289, 32:264, 26:171, 13:118, 17:88, 10:83, 4:73, 12:70, 34:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=328 fs=0 fl=0 hz=0.001834862385321101, 16:ds=289 fs=1 fl=0 hz=0.0030534351145038168, 32:ds=264 fs=0 fl=0 hz=0.0, 26:ds=171 fs=4 fl=0 hz=0.007874015748031496, 13:ds=118 fs=20 fl=2 hz=0.02546296296296296, 17:ds=88 fs=21 fl=1 hz=0.02463605823068309, 10:ds=83 fs=27 fl=2 hz=0.03172866520787746, 4:ds=73 fs=18 fl=2 hz=0.023529411764705882, 12:ds=70 fs=45 fl=0 hz=0.0487012987012987, 34:ds=54 fs=26 fl=2 hz=0.029723991507430995

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S4: ds=92 flags=purple
- S3: ds=73 flags=purple
- S22: ds=67 flags=purple

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
- 188 -> combined:685(B); evening:798(B)
- 224 -> evening:940(B); midday:892(B)
- 699 -> combined:898(B); midday:935(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 02 -> combined:40(blue); midday:50(blue)
- 04 -> combined:26(purple); midday:32(purple)
- 07 -> combined:57(red); evening:31(purple); midday:28(purple)
- 11 -> combined:55(purple); evening:51(purple); midday:27(purple)
- 25 -> combined:75(red); evening:55(blue); midday:37(blue)
- 29 -> combined:82(red); evening:41(blue); midday:50(blue)
- 35 -> combined:47(blue); evening:27(purple)
- 39 -> combined:30(purple); midday:69(red)
- 56 -> combined:36(purple); midday:25(purple)
- 66 -> combined:118(red); evening:59(purple); midday:81(blue)
- 89 -> combined:39(blue); evening:41(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.7583714285714285)[R1,Mirror-Echo], 5(4.1894285714285715)[R2,Mirror-Echo], 8(1.7723714285714287)[R3,XVAR-Cons(CM)], 2(1.1089)[R2,Double-Pressure], 9(0.9717)[R2,Double-Pressure]
- P2: 7(8.374471428571429)[R1,XVAR-Cons(CEM)], 5(6.693207142857142)[R2,XVAR-Cons(CEM)], 6(2.049242857142857)[R3,XVAR-Cons(CE)], 9(0.31497142857142857)[R3,Swap]
- P3: 0(6.734407142857143)[R1,Mirror-Echo], 9(1.5061428571428572)[R1,Double-Pressure], 5(1.3794285714285714)[R2,Mirror-Echo], 4(1.1374285714285712)[R1,Double-Pressure], 8(0.4179999999999999)[R2]
