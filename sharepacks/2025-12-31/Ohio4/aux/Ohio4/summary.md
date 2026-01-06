# Aux Summary — Ohio4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/Ohio4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Ohio
- combined: live=`data/cleaned/draws/Ohio_draws.csv` snap=`sharepacks/2025-12-31/Ohio4/aux/draws/Ohio_draws.csv` n=1000 head=327, 338, 694, 187, 241
- midday: live=`data/cleaned/draws/Ohio_Midday_draws.csv` snap=`sharepacks/2025-12-31/Ohio4/aux/draws/Ohio_Midday_draws.csv` n=1000 head=338, 187, 909, 388, 463
- evening: live=`data/cleaned/draws/Ohio_Evening_draws.csv` snap=`sharepacks/2025-12-31/Ohio4/aux/draws/Ohio_Evening_draws.csv` n=1000 head=327, 694, 241, 442, 105

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=2 last_repeat_gap=58 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=18), P2:7 (gap=37), P3:0 (gap=20)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=51.676550000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=44.61506428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 076: score=43.34983571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 570: score=41.69674285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 060: score=39.49875 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=38.557550000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.054478571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 090: score=37.73901428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 030: score=37.72557857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 010: score=37.68992142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 555: ds=959 sev=B
- 333: ds=956 sev=B
- 699: ds=892 sev=B
- 125: ds=757 sev=B
- 002: ds=711 sev=B
- 599: ds=709 sev=B
- 000: ds=689 sev=B
- 667: ds=682 sev=B
- 188: ds=679 sev=B
- 666: ds=669 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=112 sev=red
  - 11: ds=49 sev=purple
  - 77: ds=26 sev=purple
  - 00: ds=18 sev=-
  - 22: ds=15 sev=-
  - 55: ds=12 sev=-
  - 88: ds=7 sev=-
  - 44: ds=6 sev=-
  - 99: ds=5 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 29: ds=76 sev=red
  - 25: ds=69 sev=red
  - 07: ds=51 sev=blue
  - 67: ds=45 sev=blue
  - 35: ds=41 sev=blue
  - 02: ds=34 sev=purple
  - 89: ds=33 sev=purple
  - 16: ds=30 sev=purple
  - 56: ds=30 sev=purple
  - 06: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:295, 10:160, 35:123, 34:101, 19:96, 5:74, 12:69, 23:61, 17:49, 14:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=295 fs=1 fl=2 hz=0.01020408163265306, 10:ds=160 fs=21 fl=3 hz=0.02937576499388005, 35:ds=123 fs=0 fl=1 hz=0.003795066413662239, 34:ds=101 fs=26 fl=2 hz=0.03131991051454139, 19:ds=96 fs=15 fl=1 hz=0.019340159271899887, 5:ds=74 fs=14 fl=3 hz=0.01954022988505747, 12:ds=69 fs=40 fl=0 hz=0.04362050163576881, 23:ds=61 fs=31 fl=1 hz=0.034782608695652174, 17:ds=49 fs=24 fl=0 hz=0.02542372881355932, 14:ds=48 fs=43 fl=0 hz=0.04658721560130011

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=97 flags=red+purple
- S20: ds=50 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '5'], 'pairs': {'remaining_count': 0}}
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
- current_index=32 streak=1 max=3 last_repeat_gap=11 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=42), P2:5 (gap=23), P3:6 (gap=22)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:0 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=51.676550000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=44.61506428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 076: score=43.34983571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 570: score=41.69674285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 060: score=39.49875 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=38.557550000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.054478571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 090: score=37.73901428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 030: score=37.72557857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 010: score=37.68992142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=993 sev=B
- 688: ds=970 sev=B
- 788: ds=952 sev=B
- 222: ds=935 sev=B
- 699: ds=932 sev=B
- 224: ds=889 sev=B
- 022: ds=853 sev=B
- 258: ds=763 sev=B
- 119: ds=746 sev=B
- 557: ds=692 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=140 sev=red
  - 66: ds=78 sev=blue
  - 77: ds=40 sev=purple
  - 44: ds=27 sev=purple
  - 11: ds=24 sev=-
  - 00: ds=21 sev=-
  - 22: ds=7 sev=-
  - 88: ds=3 sev=-
  - 99: ds=2 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 39: ds=66 sev=red
  - 47: ds=49 sev=blue
  - 02: ds=47 sev=blue
  - 29: ds=47 sev=blue
  - 79: ds=41 sev=blue
  - 05: ds=39 sev=blue
  - 25: ds=34 sev=purple
  - 04: ds=29 sev=purple
  - 48: ds=29 sev=purple
  - 07: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 28:165, 16:147, 10:100, 1:83, 19:82, 18:78, 2:65, 35:61, 3:55, 34:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 28:ds=165 fs=22 fl=2 hz=0.03076923076923077, 16:ds=147 fs=2 fl=0 hz=0.004956629491945477, 10:ds=100 fs=22 fl=0 hz=0.028436018957345974, 1:ds=83 fs=3 fl=0 hz=0.005787037037037037, 19:ds=82 fs=12 fl=0 hz=0.01530054644808743, 18:ds=78 fs=15 fl=2 hz=0.020884520884520884, 2:ds=65 fs=17 fl=2 hz=0.020474137931034482, 35:ds=61 fs=0 fl=3 hz=0.004733727810650888, 3:ds=55 fs=17 fl=4 hz=0.022556390977443608, 34:ds=50 fs=28 fl=1 hz=0.032474804031354984

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=86 flags=purple
- S20: ds=72 flags=purple
- S5: ds=67 flags=purple
- S25: ds=62 flags=purple
- S24: ds=56 flags=purple
- S26: ds=50 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 035: score=4 tags=FLT,MIR,RS
  - 278: score=4 tags=FLT,MIR,RS
  - 026: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 269: score=3 tags=FLT,RS
  - 359: score=3 tags=FLT,RS
  - 368: score=3 tags=MIR,RS
  - 458: score=3 tags=FLT,RS
  - 015: score=2 tags=FLT,MIR
  - 017: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=27 streak=1 max=3 last_repeat_gap=8 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=16), P2:7 (gap=28), P3:9 (gap=24)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=51.676550000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 050: score=44.61506428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 076: score=43.34983571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 570: score=41.69674285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 060: score=39.49875 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 079: score=38.557550000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.054478571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 090: score=37.73901428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 030: score=37.72557857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 010: score=37.68992142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=992 sev=B
- 166: ds=941 sev=B
- 224: ds=937 sev=B
- 335: ds=891 sev=B
- 449: ds=870 sev=B
- 347: ds=863 sev=B
- 558: ds=821 sev=B
- 188: ds=795 sev=B
- 455: ds=794 sev=B
- 007: ds=707 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=96 sev=blue
  - 66: ds=56 sev=purple
  - 99: ds=51 sev=purple
  - 11: ds=48 sev=purple
  - 33: ds=34 sev=purple
  - 88: ds=33 sev=purple
  - 77: ds=13 sev=-
  - 00: ds=9 sev=-
  - 55: ds=6 sev=-
  - 44: ds=3 sev=-
- non_repeating:
  - 03: ds=70 sev=red
  - 45: ds=67 sev=red
  - 25: ds=52 sev=blue
  - 29: ds=38 sev=blue
  - 89: ds=38 sev=blue
  - 67: ds=35 sev=purple
  - 07: ds=28 sev=purple
  - 35: ds=24 sev=-
  - 36: ds=22 sev=-
  - 78: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:325, 16:286, 32:261, 26:168, 13:115, 17:85, 10:80, 4:70, 12:67, 34:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=325 fs=0 fl=0 hz=0.001834862385321101, 16:ds=286 fs=1 fl=0 hz=0.0030534351145038168, 32:ds=261 fs=0 fl=0 hz=0.0, 26:ds=168 fs=4 fl=0 hz=0.007874015748031496, 13:ds=115 fs=20 fl=2 hz=0.02546296296296296, 17:ds=85 fs=21 fl=1 hz=0.02463605823068309, 10:ds=80 fs=27 fl=2 hz=0.03172866520787746, 4:ds=70 fs=18 fl=2 hz=0.023529411764705882, 12:ds=67 fs=45 fl=0 hz=0.0487012987012987, 34:ds=51 fs=26 fl=2 hz=0.029723991507430995

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S4: ds=89 flags=purple
- S3: ds=70 flags=purple
- S22: ds=64 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 168: score=2 tags=FLT,MIR
  - 238: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 348: score=2 tags=FLT,MIR
  - 358: score=2 tags=FLT,MIR
  - 368: score=2 tags=FLT,MIR
  - 378: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 188 -> combined:679(B); evening:795(B)
- 224 -> evening:937(B); midday:889(B)
- 699 -> combined:892(B); midday:932(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 02 -> combined:34(purple); midday:47(blue)
- 07 -> combined:51(blue); evening:28(purple); midday:25(purple)
- 11 -> combined:49(purple); evening:48(purple)
- 25 -> combined:69(red); evening:52(blue); midday:34(purple)
- 29 -> combined:76(red); evening:38(blue); midday:47(blue)
- 47 -> combined:26(purple); midday:49(blue)
- 66 -> combined:112(red); evening:56(purple); midday:78(blue)
- 67 -> combined:45(blue); evening:35(purple)
- 77 -> combined:26(purple); midday:40(purple)
- 89 -> combined:33(purple); evening:38(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.4287785714285715)[R1,Mirror-Echo], 5(3.8638214285714287)[R2,Mirror-Echo], 7(1.3324285714285713)[R2,Mirror-Echo], 9(0.9089999999999999)[R2,Double-Pressure], 2(0.5493428571428571)[R3,Mirror-Echo]
- P2: 7(8.2122)[R1,XVAR-Cons(CEM)], 5(3.650714285714286)[R2,XVAR-Cons(CM)], 6(1.0344)[R2,Double-Pressure], 9(0.2746642857142857)[R3,Swap], 3(0.2612285714285714)[R3,Swap]
- P3: 0(5.620721428571429)[R1,XVAR-Cons(CEM)], 6(3.7088571428571426)[R2,XVAR-Cons(CM)], 9(1.4165714285714284)[R1,Double-Pressure], 4(0.9135)[R2,Double-Pressure], 8(0.35529999999999995)[R2]
