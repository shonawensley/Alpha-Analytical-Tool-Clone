# Aux Summary — Ohio4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/Ohio4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Ohio
- combined: live=`data/cleaned/draws/Ohio_draws.csv` snap=`sharepacks/2026-01-02/Ohio4/aux/draws/Ohio_draws.csv` n=1000 head=416, 746, 197, 306, 327
- midday: live=`data/cleaned/draws/Ohio_Midday_draws.csv` snap=`sharepacks/2026-01-02/Ohio4/aux/draws/Ohio_Midday_draws.csv` n=1000 head=746, 306, 338, 187, 909
- evening: live=`data/cleaned/draws/Ohio_Evening_draws.csv` snap=`sharepacks/2026-01-02/Ohio4/aux/draws/Ohio_Evening_draws.csv` n=1000 head=416, 197, 327, 694, 241

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=19 streak=1 max=2 last_repeat_gap=2 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=22), P2:7 (gap=41), P3:0 (gap=24)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=54.24343785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=47.28815214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 060: score=44.489780714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 570: score=43.90896428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 090: score=40.29125928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 030: score=40.27782357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=38.87850714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.50979285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 078: score=38.399321428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 073: score=38.38822142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 555: ds=963 sev=B
- 333: ds=960 sev=B
- 699: ds=896 sev=B
- 125: ds=761 sev=B
- 002: ds=715 sev=B
- 599: ds=713 sev=B
- 000: ds=693 sev=B
- 667: ds=686 sev=B
- 188: ds=683 sev=B
- 666: ds=673 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=116 sev=red
  - 11: ds=53 sev=purple
  - 77: ds=30 sev=purple
  - 00: ds=22 sev=-
  - 22: ds=19 sev=-
  - 55: ds=16 sev=-
  - 88: ds=11 sev=-
  - 44: ds=10 sev=-
  - 99: ds=9 sev=-
  - 33: ds=5 sev=-
- non_repeating:
  - 29: ds=80 sev=red
  - 25: ds=73 sev=red
  - 07: ds=55 sev=blue
  - 35: ds=45 sev=blue
  - 02: ds=38 sev=blue
  - 89: ds=37 sev=blue
  - 56: ds=34 sev=purple
  - 39: ds=28 sev=purple
  - 59: ds=26 sev=purple
  - 08: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:299, 10:164, 35:127, 34:105, 5:78, 12:73, 23:65, 17:53, 14:52, 18:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=299 fs=1 fl=2 hz=0.01020408163265306, 10:ds=164 fs=21 fl=3 hz=0.02937576499388005, 35:ds=127 fs=0 fl=1 hz=0.003795066413662239, 34:ds=105 fs=26 fl=2 hz=0.03131991051454139, 5:ds=78 fs=14 fl=3 hz=0.01954022988505747, 12:ds=73 fs=40 fl=0 hz=0.04362050163576881, 23:ds=65 fs=31 fl=1 hz=0.034782608695652174, 17:ds=53 fs=24 fl=0 hz=0.02542372881355932, 14:ds=52 fs=43 fl=0 hz=0.04658721560130011, 18:ds=48 fs=20 fl=1 hz=0.024793388429752063

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
- S20: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=13 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=44), P2:5 (gap=25), P3:4 (gap=17)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:0 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=54.24343785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=47.28815214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 060: score=44.489780714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 570: score=43.90896428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 090: score=40.29125928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 030: score=40.27782357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=38.87850714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.50979285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 078: score=38.399321428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 073: score=38.38822142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=995 sev=B
- 688: ds=972 sev=B
- 788: ds=954 sev=B
- 222: ds=937 sev=B
- 699: ds=934 sev=B
- 224: ds=891 sev=B
- 022: ds=855 sev=B
- 258: ds=765 sev=B
- 119: ds=748 sev=B
- 557: ds=694 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=142 sev=red
  - 66: ds=80 sev=blue
  - 77: ds=42 sev=purple
  - 44: ds=29 sev=purple
  - 11: ds=26 sev=purple
  - 00: ds=23 sev=-
  - 22: ds=9 sev=-
  - 88: ds=5 sev=-
  - 99: ds=4 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 39: ds=68 sev=red
  - 02: ds=49 sev=blue
  - 29: ds=49 sev=blue
  - 79: ds=43 sev=blue
  - 05: ds=41 sev=blue
  - 25: ds=36 sev=purple
  - 04: ds=31 sev=purple
  - 48: ds=31 sev=purple
  - 07: ds=27 sev=purple
  - 16: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 28:167, 16:149, 10:102, 1:85, 19:84, 18:80, 2:67, 35:63, 3:57, 34:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 28:ds=167 fs=22 fl=2 hz=0.03076923076923077, 16:ds=149 fs=2 fl=0 hz=0.004956629491945477, 10:ds=102 fs=22 fl=0 hz=0.028436018957345974, 1:ds=85 fs=3 fl=0 hz=0.005787037037037037, 19:ds=84 fs=12 fl=0 hz=0.01530054644808743, 18:ds=80 fs=15 fl=2 hz=0.020884520884520884, 2:ds=67 fs=17 fl=2 hz=0.020474137931034482, 35:ds=63 fs=0 fl=3 hz=0.004733727810650888, 3:ds=57 fs=17 fl=4 hz=0.022556390977443608, 34:ds=52 fs=28 fl=1 hz=0.032474804031354984

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=88 flags=purple
- S20: ds=74 flags=purple
- S5: ds=69 flags=purple
- S25: ds=64 flags=purple
- S24: ds=58 flags=purple
- S26: ds=52 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 035: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=19 streak=1 max=3 last_repeat_gap=10 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=18), P2:7 (gap=30), P3:9 (gap=26)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=54.24343785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=47.28815214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 060: score=44.489780714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 570: score=43.90896428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 090: score=40.29125928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 030: score=40.27782357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=38.87850714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.50979285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 078: score=38.399321428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 073: score=38.38822142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=994 sev=B
- 166: ds=943 sev=B
- 224: ds=939 sev=B
- 335: ds=893 sev=B
- 449: ds=872 sev=B
- 347: ds=865 sev=B
- 558: ds=823 sev=B
- 188: ds=797 sev=B
- 455: ds=796 sev=B
- 007: ds=709 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=98 sev=blue
  - 66: ds=58 sev=purple
  - 99: ds=53 sev=purple
  - 11: ds=50 sev=purple
  - 33: ds=36 sev=purple
  - 88: ds=35 sev=purple
  - 77: ds=15 sev=-
  - 00: ds=11 sev=-
  - 55: ds=8 sev=-
  - 44: ds=5 sev=-
- non_repeating:
  - 03: ds=72 sev=red
  - 45: ds=69 sev=red
  - 25: ds=54 sev=blue
  - 29: ds=40 sev=blue
  - 89: ds=40 sev=blue
  - 67: ds=37 sev=blue
  - 07: ds=30 sev=purple
  - 35: ds=26 sev=purple
  - 36: ds=24 sev=-
  - 78: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:327, 16:288, 32:263, 26:170, 13:117, 17:87, 10:82, 4:72, 12:69, 34:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=327 fs=0 fl=0 hz=0.001834862385321101, 16:ds=288 fs=1 fl=0 hz=0.0030534351145038168, 32:ds=263 fs=0 fl=0 hz=0.0, 26:ds=170 fs=4 fl=0 hz=0.007874015748031496, 13:ds=117 fs=20 fl=2 hz=0.02546296296296296, 17:ds=87 fs=21 fl=1 hz=0.02463605823068309, 10:ds=82 fs=27 fl=2 hz=0.03172866520787746, 4:ds=72 fs=18 fl=2 hz=0.023529411764705882, 12:ds=69 fs=45 fl=0 hz=0.0487012987012987, 34:ds=53 fs=26 fl=2 hz=0.029723991507430995

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S4: ds=91 flags=purple
- S3: ds=72 flags=purple
- S22: ds=66 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '5', '8'], 'pairs': {'remaining_count': 0}}
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

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 188 -> combined:683(B); evening:797(B)
- 224 -> evening:939(B); midday:891(B)
- 699 -> combined:896(B); midday:934(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 02 -> combined:38(blue); midday:49(blue)
- 07 -> combined:55(blue); evening:30(purple); midday:27(purple)
- 11 -> combined:53(purple); evening:50(purple); midday:26(purple)
- 25 -> combined:73(red); evening:54(blue); midday:36(purple)
- 29 -> combined:80(red); evening:40(blue); midday:49(blue)
- 35 -> combined:45(blue); evening:26(purple)
- 39 -> combined:28(purple); midday:68(red)
- 66 -> combined:116(red); evening:58(purple); midday:80(blue)
- 77 -> combined:30(purple); midday:42(purple)
- 89 -> combined:37(blue); evening:40(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.648507142857143)[R1,Mirror-Echo], 5(4.080892857142857)[R2,Mirror-Echo], 8(1.87065)[R3,XVAR-Cons(CM)], 2(1.0879999999999999)[R2,Double-Pressure], 9(0.9508)[R2,Double-Pressure]
- P2: 7(8.253714285714285)[R1,XVAR-Cons(CEM)], 5(3.7984285714285715)[R2,XVAR-Cons(CM)], 6(2.000057142857143)[R3,XVAR-Cons(CE)], 9(0.30153571428571424)[R3,Swap], 3(0.2881)[R3,Swap]
- P3: 0(6.574357142857143)[R1,Mirror-Echo], 9(1.4762857142857142)[R1,Double-Pressure], 4(1.1075714285714284)[R1,Double-Pressure], 8(0.9970999999999999)[R2,Double-Pressure], 3(0.986)[R2,Double-Pressure]
