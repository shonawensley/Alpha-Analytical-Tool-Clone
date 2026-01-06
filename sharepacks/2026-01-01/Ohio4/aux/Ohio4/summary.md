# Aux Summary — Ohio4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/Ohio4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Ohio
- combined: live=`data/cleaned/draws/Ohio_draws.csv` snap=`sharepacks/2026-01-01/Ohio4/aux/draws/Ohio_draws.csv` n=1000 head=197, 306, 327, 338, 694
- midday: live=`data/cleaned/draws/Ohio_Midday_draws.csv` snap=`sharepacks/2026-01-01/Ohio4/aux/draws/Ohio_Midday_draws.csv` n=1000 head=306, 338, 187, 909, 388
- evening: live=`data/cleaned/draws/Ohio_Evening_draws.csv` snap=`sharepacks/2026-01-01/Ohio4/aux/draws/Ohio_Evening_draws.csv` n=1000 head=197, 327, 694, 241, 442

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=60 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=20), P2:7 (gap=39), P3:0 (gap=22)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=53.966792142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=46.92840642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 570: score=43.699621428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 060: score=40.129135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 090: score=39.991935 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 010: score=39.98769214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 030: score=39.978499285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=38.74802857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.37931428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 078: score=38.2778 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 555: ds=961 sev=B
- 333: ds=958 sev=B
- 699: ds=894 sev=B
- 125: ds=759 sev=B
- 002: ds=713 sev=B
- 599: ds=711 sev=B
- 000: ds=691 sev=B
- 667: ds=684 sev=B
- 188: ds=681 sev=B
- 666: ds=671 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=114 sev=red
  - 11: ds=51 sev=purple
  - 77: ds=28 sev=purple
  - 00: ds=20 sev=-
  - 22: ds=17 sev=-
  - 55: ds=14 sev=-
  - 88: ds=9 sev=-
  - 44: ds=8 sev=-
  - 99: ds=7 sev=-
  - 33: ds=3 sev=-
- non_repeating:
  - 29: ds=78 sev=red
  - 25: ds=71 sev=red
  - 07: ds=53 sev=blue
  - 67: ds=47 sev=blue
  - 35: ds=43 sev=blue
  - 02: ds=36 sev=purple
  - 89: ds=35 sev=purple
  - 16: ds=32 sev=purple
  - 56: ds=32 sev=purple
  - 47: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:297, 10:162, 35:125, 34:103, 19:98, 5:76, 12:71, 23:63, 17:51, 14:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=297 fs=1 fl=2 hz=0.01020408163265306, 10:ds=162 fs=21 fl=3 hz=0.02937576499388005, 35:ds=125 fs=0 fl=1 hz=0.003795066413662239, 34:ds=103 fs=26 fl=2 hz=0.03131991051454139, 19:ds=98 fs=15 fl=1 hz=0.019340159271899887, 5:ds=76 fs=14 fl=3 hz=0.01954022988505747, 12:ds=71 fs=40 fl=0 hz=0.04362050163576881, 23:ds=63 fs=31 fl=1 hz=0.034782608695652174, 17:ds=51 fs=24 fl=0 hz=0.02542372881355932, 14:ds=50 fs=43 fl=0 hz=0.04658721560130011

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=99 flags=red+purple
- S20: ds=52 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT
  - 125: score=1 tags=FLT
  - 135: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=12 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=43), P2:5 (gap=24), P3:4 (gap=16)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:0 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=53.966792142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=46.92840642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 570: score=43.699621428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 060: score=40.129135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 090: score=39.991935 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 010: score=39.98769214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 030: score=39.978499285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=38.74802857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.37931428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 078: score=38.2778 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=994 sev=B
- 688: ds=971 sev=B
- 788: ds=953 sev=B
- 222: ds=936 sev=B
- 699: ds=933 sev=B
- 224: ds=890 sev=B
- 022: ds=854 sev=B
- 258: ds=764 sev=B
- 119: ds=747 sev=B
- 557: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=141 sev=red
  - 66: ds=79 sev=blue
  - 77: ds=41 sev=purple
  - 44: ds=28 sev=purple
  - 11: ds=25 sev=purple
  - 00: ds=22 sev=-
  - 22: ds=8 sev=-
  - 88: ds=4 sev=-
  - 99: ds=3 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 39: ds=67 sev=red
  - 47: ds=50 sev=blue
  - 02: ds=48 sev=blue
  - 29: ds=48 sev=blue
  - 79: ds=42 sev=blue
  - 05: ds=40 sev=blue
  - 25: ds=35 sev=purple
  - 04: ds=30 sev=purple
  - 48: ds=30 sev=purple
  - 07: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 28:166, 16:148, 10:101, 1:84, 19:83, 18:79, 2:66, 35:62, 3:56, 34:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 28:ds=166 fs=22 fl=2 hz=0.03076923076923077, 16:ds=148 fs=2 fl=0 hz=0.004956629491945477, 10:ds=101 fs=22 fl=0 hz=0.028436018957345974, 1:ds=84 fs=3 fl=0 hz=0.005787037037037037, 19:ds=83 fs=12 fl=0 hz=0.01530054644808743, 18:ds=79 fs=15 fl=2 hz=0.020884520884520884, 2:ds=66 fs=17 fl=2 hz=0.020474137931034482, 35:ds=62 fs=0 fl=3 hz=0.004733727810650888, 3:ds=56 fs=17 fl=4 hz=0.022556390977443608, 34:ds=51 fs=28 fl=1 hz=0.032474804031354984

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=87 flags=purple
- S20: ds=73 flags=purple
- S5: ds=68 flags=purple
- S25: ds=63 flags=purple
- S24: ds=57 flags=purple
- S26: ds=51 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 026: score=3 tags=FLT,RS
  - 035: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 134: score=3 tags=FLT,RS
  - 269: score=3 tags=FLT,RS
  - 278: score=3 tags=FLT,RS
  - 359: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 467: score=3 tags=FLT,RS
  - 017: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=9 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=17), P2:7 (gap=29), P3:9 (gap=25)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=53.966792142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=46.92840642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 570: score=43.699621428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 060: score=40.129135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 090: score=39.991935 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 010: score=39.98769214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 030: score=39.978499285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=38.74802857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.37931428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 078: score=38.2778 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=993 sev=B
- 166: ds=942 sev=B
- 224: ds=938 sev=B
- 335: ds=892 sev=B
- 449: ds=871 sev=B
- 347: ds=864 sev=B
- 558: ds=822 sev=B
- 188: ds=796 sev=B
- 455: ds=795 sev=B
- 007: ds=708 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=97 sev=blue
  - 66: ds=57 sev=purple
  - 99: ds=52 sev=purple
  - 11: ds=49 sev=purple
  - 33: ds=35 sev=purple
  - 88: ds=34 sev=purple
  - 77: ds=14 sev=-
  - 00: ds=10 sev=-
  - 55: ds=7 sev=-
  - 44: ds=4 sev=-
- non_repeating:
  - 03: ds=71 sev=red
  - 45: ds=68 sev=red
  - 25: ds=53 sev=blue
  - 29: ds=39 sev=blue
  - 89: ds=39 sev=blue
  - 67: ds=36 sev=purple
  - 07: ds=29 sev=purple
  - 35: ds=25 sev=purple
  - 36: ds=23 sev=-
  - 78: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:326, 16:287, 32:262, 26:169, 13:116, 17:86, 10:81, 4:71, 12:68, 34:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=326 fs=0 fl=0 hz=0.001834862385321101, 16:ds=287 fs=1 fl=0 hz=0.0030534351145038168, 32:ds=262 fs=0 fl=0 hz=0.0, 26:ds=169 fs=4 fl=0 hz=0.007874015748031496, 13:ds=116 fs=20 fl=2 hz=0.02546296296296296, 17:ds=86 fs=21 fl=1 hz=0.02463605823068309, 10:ds=81 fs=27 fl=2 hz=0.03172866520787746, 4:ds=71 fs=18 fl=2 hz=0.023529411764705882, 12:ds=68 fs=45 fl=0 hz=0.0487012987012987, 34:ds=52 fs=26 fl=2 hz=0.029723991507430995

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S4: ds=90 flags=purple
- S3: ds=71 flags=purple
- S22: ds=65 flags=purple

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
- 188 -> combined:681(B); evening:796(B)
- 224 -> evening:938(B); midday:890(B)
- 699 -> combined:894(B); midday:933(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 02 -> combined:36(purple); midday:48(blue)
- 07 -> combined:53(blue); evening:29(purple); midday:26(purple)
- 11 -> combined:51(purple); evening:49(purple); midday:25(purple)
- 25 -> combined:71(red); evening:53(blue); midday:35(purple)
- 29 -> combined:78(red); evening:39(blue); midday:48(blue)
- 35 -> combined:43(blue); evening:25(purple)
- 39 -> combined:26(purple); midday:67(red)
- 47 -> combined:28(purple); midday:50(blue)
- 66 -> combined:114(red); evening:57(purple); midday:79(blue)
- 67 -> combined:47(blue); evening:36(purple)
- 77 -> combined:28(purple); midday:41(purple)
- 89 -> combined:35(purple); evening:39(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.538642857142857)[R1,Mirror-Echo], 5(3.9723571428571427)[R2,Mirror-Echo], 7(1.359435714285714)[R2,Mirror-Echo], 9(0.9299)[R2,Double-Pressure], 2(0.5722785714285714)[R3,Mirror-Echo]
- P2: 7(8.262957142857143)[R1,XVAR-Cons(CEM)], 5(3.7245714285714286)[R2,XVAR-Cons(CM)], 6(0.42529999999999996)[R2,Swap], 9(0.2881)[R3,Swap], 1(0.28385714285714286)[R3,Swap]
- P3: 0(6.464307142857143)[R1,Mirror-Echo], 9(1.4464285714285714)[R1,Double-Pressure], 4(1.0777142857142856)[R1,Double-Pressure], 8(0.9761999999999998)[R2,Double-Pressure], 3(0.942)[R2,Double-Pressure]
