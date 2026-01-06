# Aux Summary — Ohio4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/Ohio4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Ohio
- combined: live=`data/cleaned/draws/Ohio_draws.csv` snap=`sharepacks/2025-12-30/Ohio4/aux/draws/Ohio_draws.csv` n=1000 head=694, 187, 241, 909, 442
- midday: live=`data/cleaned/draws/Ohio_Midday_draws.csv` snap=`sharepacks/2025-12-30/Ohio4/aux/draws/Ohio_Midday_draws.csv` n=1000 head=187, 909, 388, 463, 412
- evening: live=`data/cleaned/draws/Ohio_Evening_draws.csv` snap=`sharepacks/2025-12-30/Ohio4/aux/draws/Ohio_Evening_draws.csv` n=1000 head=694, 241, 442, 105, 384

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=25 streak=1 max=2 last_repeat_gap=56 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=16), P2:7 (gap=35), P3:0 (gap=18)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=46.23969571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 076: score=44.22892857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 079: score=39.480642857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 078: score=39.09832857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.98652857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 576: score=38.2353 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 077: score=37.341721428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 570: score=37.27037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 030: score=37.07447428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 036: score=35.06370714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 555: ds=957 sev=B
- 333: ds=954 sev=B
- 699: ds=890 sev=B
- 125: ds=755 sev=B
- 002: ds=709 sev=B
- 599: ds=707 sev=B
- 000: ds=687 sev=B
- 667: ds=680 sev=B
- 188: ds=677 sev=B
- 666: ds=667 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=110 sev=red
  - 11: ds=47 sev=purple
  - 77: ds=24 sev=-
  - 33: ds=21 sev=-
  - 00: ds=16 sev=-
  - 22: ds=13 sev=-
  - 55: ds=10 sev=-
  - 88: ds=5 sev=-
  - 44: ds=4 sev=-
  - 99: ds=3 sev=-
- non_repeating:
  - 29: ds=74 sev=red
  - 25: ds=67 sev=red
  - 07: ds=49 sev=blue
  - 67: ds=43 sev=blue
  - 35: ds=39 sev=blue
  - 27: ds=35 sev=purple
  - 02: ds=32 sev=purple
  - 89: ds=31 sev=purple
  - 16: ds=28 sev=purple
  - 56: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:293, 10:158, 35:121, 34:99, 19:94, 5:72, 12:67, 23:59, 17:47, 14:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=293 fs=1 fl=2 hz=0.01020408163265306, 10:ds=158 fs=21 fl=3 hz=0.02937576499388005, 35:ds=121 fs=0 fl=1 hz=0.003795066413662239, 34:ds=99 fs=26 fl=2 hz=0.03131991051454139, 19:ds=94 fs=15 fl=1 hz=0.019340159271899887, 5:ds=72 fs=14 fl=3 hz=0.01954022988505747, 12:ds=67 fs=40 fl=0 hz=0.04362050163576881, 23:ds=59 fs=31 fl=1 hz=0.034782608695652174, 17:ds=47 fs=24 fl=0 hz=0.02542372881355932, 14:ds=46 fs=43 fl=0 hz=0.04658721560130011

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S26: ds=99 flags=blue+purple
- S21: ds=95 flags=red+purple
- S20: ds=48 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 057: score=4 tags=FLT,MIR,RS
  - 138: score=4 tags=FLT,MIR,RS
  - 156: score=4 tags=FLT,MIR,RS
  - 237: score=4 tags=FLT,MIR,RS
  - 039: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 489: score=3 tags=MIR,RS
  - 579: score=3 tags=FLT,RS
  - 012: score=2 tags=RS
  - 015: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=10 last_repeat_index=13

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=41), P2:5 (gap=22), P3:6 (gap=21)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:0 (ds=41)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=46.23969571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 076: score=44.22892857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 079: score=39.480642857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 078: score=39.09832857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.98652857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 576: score=38.2353 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 077: score=37.341721428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 570: score=37.27037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 030: score=37.07447428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 036: score=35.06370714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 556: ds=992 sev=B
- 688: ds=969 sev=B
- 788: ds=951 sev=B
- 222: ds=934 sev=B
- 699: ds=931 sev=B
- 224: ds=888 sev=B
- 022: ds=852 sev=B
- 258: ds=762 sev=B
- 119: ds=745 sev=B
- 557: ds=691 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=139 sev=red
  - 66: ds=77 sev=blue
  - 77: ds=39 sev=purple
  - 44: ds=26 sev=purple
  - 11: ds=23 sev=-
  - 00: ds=20 sev=-
  - 33: ds=10 sev=-
  - 22: ds=6 sev=-
  - 88: ds=2 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 39: ds=65 sev=red
  - 47: ds=48 sev=blue
  - 02: ds=46 sev=blue
  - 29: ds=46 sev=blue
  - 79: ds=40 sev=blue
  - 05: ds=38 sev=blue
  - 25: ds=33 sev=purple
  - 04: ds=28 sev=purple
  - 48: ds=28 sev=purple
  - 07: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 28:164, 16:146, 10:99, 1:82, 19:81, 18:77, 2:64, 35:60, 3:54, 34:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 28:ds=164 fs=22 fl=2 hz=0.03076923076923077, 16:ds=146 fs=2 fl=0 hz=0.004956629491945477, 10:ds=99 fs=22 fl=0 hz=0.028436018957345974, 1:ds=82 fs=3 fl=0 hz=0.005787037037037037, 19:ds=81 fs=12 fl=0 hz=0.01530054644808743, 18:ds=77 fs=15 fl=2 hz=0.020884520884520884, 2:ds=64 fs=17 fl=2 hz=0.020474137931034482, 35:ds=60 fs=0 fl=3 hz=0.004733727810650888, 3:ds=54 fs=17 fl=4 hz=0.022556390977443608, 34:ds=49 fs=28 fl=1 hz=0.032474804031354984

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=85 flags=purple
- S20: ds=71 flags=purple
- S5: ds=66 flags=purple
- S25: ds=61 flags=purple
- S24: ds=55 flags=purple
- S26: ds=49 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [8], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 035: score=3 tags=FLT,RS
  - 125: score=3 tags=FLT,RS
  - 359: score=3 tags=FLT,RS
  - 458: score=3 tags=FLT,RS
  - 017: score=2 tags=RS
  - 026: score=2 tags=RS
  - 089: score=2 tags=RS
  - 134: score=2 tags=RS
  - 179: score=2 tags=RS
  - 269: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=25 streak=1 max=3 last_repeat_gap=7 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=15), P2:7 (gap=27), P3:9 (gap=23)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 070: score=46.23969571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 076: score=44.22892857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 079: score=39.480642857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 078: score=39.09832857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 074: score=38.98652857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 576: score=38.2353 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 077: score=37.341721428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 570: score=37.27037142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 030: score=37.07447428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 036: score=35.06370714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=991 sev=B
- 166: ds=940 sev=B
- 224: ds=936 sev=B
- 335: ds=890 sev=B
- 449: ds=869 sev=B
- 347: ds=862 sev=B
- 558: ds=820 sev=B
- 188: ds=794 sev=B
- 455: ds=793 sev=B
- 007: ds=706 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=95 sev=blue
  - 66: ds=55 sev=purple
  - 99: ds=50 sev=purple
  - 11: ds=47 sev=purple
  - 33: ds=33 sev=purple
  - 88: ds=32 sev=purple
  - 77: ds=12 sev=-
  - 00: ds=8 sev=-
  - 55: ds=5 sev=-
  - 44: ds=2 sev=-
- non_repeating:
  - 03: ds=69 sev=red
  - 45: ds=66 sev=red
  - 23: ds=51 sev=blue
  - 25: ds=51 sev=blue
  - 29: ds=37 sev=blue
  - 89: ds=37 sev=blue
  - 67: ds=34 sev=purple
  - 07: ds=27 sev=purple
  - 35: ds=23 sev=-
  - 36: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:324, 16:285, 32:260, 26:167, 13:114, 17:84, 10:79, 4:69, 12:66, 34:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=324 fs=0 fl=0 hz=0.001834862385321101, 16:ds=285 fs=1 fl=0 hz=0.0030534351145038168, 32:ds=260 fs=0 fl=0 hz=0.0, 26:ds=167 fs=4 fl=0 hz=0.007874015748031496, 13:ds=114 fs=20 fl=2 hz=0.02546296296296296, 17:ds=84 fs=21 fl=1 hz=0.02463605823068309, 10:ds=79 fs=27 fl=2 hz=0.03172866520787746, 4:ds=69 fs=18 fl=2 hz=0.023529411764705882, 12:ds=66 fs=45 fl=0 hz=0.0487012987012987, 34:ds=50 fs=26 fl=2 hz=0.029723991507430995

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S4: ds=88 flags=purple
- S3: ds=69 flags=purple
- S22: ds=63 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 027: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 247: score=2 tags=FLT,MIR
  - 257: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 279: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 188 -> combined:677(B); evening:794(B)
- 224 -> evening:936(B); midday:888(B)
- 699 -> combined:890(B); midday:931(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 02 -> combined:32(purple); midday:46(blue)
- 07 -> combined:49(blue); evening:27(purple)
- 11 -> combined:47(purple); evening:47(purple)
- 25 -> combined:67(red); evening:51(blue); midday:33(purple)
- 29 -> combined:74(red); evening:37(blue); midday:46(blue)
- 66 -> combined:110(red); evening:55(purple); midday:77(blue)
- 67 -> combined:43(blue); evening:34(purple)
- 89 -> combined:31(purple); evening:37(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.248914285714286)[R1,Mirror-Echo], 5(3.7552857142857143)[R2,Mirror-Echo], 7(1.3054214285714285)[R2,Mirror-Echo], 9(0.8880999999999999)[R2,Double-Pressure], 2(0.5564071428571429)[R3,Mirror-Echo]
- P2: 7(8.345014285714287)[R1,Mirror-Echo], 3(2.679792857142857)[R2,XVAR-Cons(CE)], 5(1.3568571428571428)[R1,Double-Pressure], 6(1.0135)[R2,Double-Pressure], 2(0.7838571428571429)[R3,Mirror-Echo]
- P3: 6(3.635)[R2,XVAR-Cons(CM)], 0(2.6700714285714287)[R1,XVAR-Cons(CM)], 9(1.3867142857142856)[R1,Double-Pressure], 8(1.0044)[R2,Double-Pressure], 4(0.8926)[R2,Double-Pressure]
