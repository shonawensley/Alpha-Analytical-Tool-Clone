# Aux Summary — Indiana4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/Indiana4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Indiana
- combined: live=`data/cleaned/draws/Indiana_draws.csv` snap=`sharepacks/2025-12-30/Indiana4/aux/draws/Indiana_draws.csv` n=1000 head=560, 144, 998, 494, 803
- midday: live=`data/cleaned/draws/Indiana_Midday_draws.csv` snap=`sharepacks/2025-12-30/Indiana4/aux/draws/Indiana_Midday_draws.csv` n=1000 head=144, 494, 351, 117, 404
- evening: live=`data/cleaned/draws/Indiana_Evening_draws.csv` snap=`sharepacks/2025-12-30/Indiana4/aux/draws/Indiana_Evening_draws.csv` n=1000 head=560, 998, 803, 383, 879

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=3 last_repeat_gap=11 last_repeat_index=27

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=23), P2:3 (gap=21), P3:6 (gap=31)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 036: score=48.71462857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 636: score=46.684243571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 035: score=43.00206428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 030: score=40.946909285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 086: score=38.06225714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 031: score=38.00329285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 635: score=37.48727142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 066: score=37.36691428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 016: score=37.07118571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 026: score=36.422914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 068: ds=977 sev=B
- 066: ds=932 sev=B
- 669: ds=920 sev=B
- 258: ds=889 sev=B
- 566: ds=834 sev=B
- 688: ds=820 sev=B
- 667: ds=751 sev=B
- 447: ds=734 sev=B
- 244: ds=720 sev=B
- 779: ds=715 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=120 sev=red
  - 77: ds=44 sev=purple
  - 88: ds=27 sev=purple
  - 00: ds=23 sev=-
  - 55: ds=17 sev=-
  - 22: ds=11 sev=-
  - 11: ds=7 sev=-
  - 33: ds=6 sev=-
  - 99: ds=2 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 18: ds=70 sev=red
  - 16: ds=54 sev=blue
  - 01: ds=52 sev=blue
  - 28: ds=47 sev=blue
  - 68: ds=40 sev=blue
  - 02: ds=38 sev=blue
  - 69: ds=37 sev=blue
  - 57: ds=32 sev=purple
  - 36: ds=31 sev=purple
  - 67: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:271, 28:140, 9:103, 6:100, 18:91, 7:90, 5:74, 1:68, 10:67, 19:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=271 fs=2 fl=1 hz=0.006956521739130435, 28:ds=140 fs=19 fl=1 hz=0.025149700598802397, 9:ds=103 fs=52 fl=0 hz=0.05855855855855856, 6:ds=100 fs=12 fl=2 hz=0.016222479721900347, 18:ds=91 fs=24 fl=1 hz=0.029478458049886625, 7:ds=90 fs=43 fl=0 hz=0.04971098265895954, 5:ds=74 fs=22 fl=2 hz=0.026519337016574582, 1:ds=68 fs=4 fl=3 hz=0.008830022075055188, 10:ds=67 fs=17 fl=3 hz=0.023391812865497075, 19:ds=58 fs=29 fl=1 hz=0.032051282051282055

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=81 flags=purple
- S21: ds=65 flags=purple
- S13: ds=45 flags=red+purple
- S10: ds=42 flags=red+purple
- S5: ds=38 flags=purple
- S6: ds=35 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 127: score=4 tags=FLT,MIR,RS
  - 028: score=3 tags=FLT,RS
  - 037: score=3 tags=FLT,RS
  - 136: score=3 tags=MIR,RS
  - 235: score=3 tags=FLT,RS
  - 289: score=3 tags=FLT,RS
  - 379: score=3 tags=FLT,RS
  - 469: score=3 tags=MIR,RS
  - 478: score=3 tags=FLT,RS
  - 019: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=25 streak=1 max=2 last_repeat_gap=78 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=44), P2:6 (gap=18), P3:0 (gap=34)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 036: score=48.71462857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 636: score=46.684243571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 035: score=43.00206428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 030: score=40.946909285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 086: score=38.06225714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 031: score=38.00329285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 635: score=37.48727142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 066: score=37.36691428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 016: score=37.07118571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 026: score=36.422914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 669: ds=996 sev=B
- 288: ds=991 sev=B
- 337: ds=943 sev=B
- 666: ds=915 sev=B
- 677: ds=913 sev=B
- 566: ds=870 sev=B
- 445: ds=806 sev=B
- 266: ds=766 sev=B
- 444: ds=764 sev=B
- 177: ds=727 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=135 sev=red
  - 77: ds=35 sev=purple
  - 33: ds=20 sev=-
  - 88: ds=13 sev=-
  - 00: ds=11 sev=-
  - 55: ds=8 sev=-
  - 99: ds=7 sev=-
  - 22: ds=5 sev=-
  - 11: ds=3 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 45: ds=100 sev=red
  - 16: ds=74 sev=red
  - 18: ds=66 sev=red
  - 02: ds=54 sev=blue
  - 56: ds=51 sev=blue
  - 68: ds=49 sev=blue
  - 05: ds=43 sev=blue
  - 19: ds=38 sev=blue
  - 01: ds=30 sev=purple
  - 08: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:241, 16:135, 6:102, 24:84, 28:77, 13:65, 5:53, 9:51, 7:47, 18:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=241 fs=3 fl=1 hz=0.007668711656441718, 16:ds=135 fs=4 fl=0 hz=0.007342143906020559, 6:ds=102 fs=20 fl=2 hz=0.02458100558659218, 24:ds=84 fs=43 fl=1 hz=0.0484048404840484, 28:ds=77 fs=18 fl=1 hz=0.022650056625141565, 13:ds=65 fs=15 fl=1 hz=0.021505376344086023, 5:ds=53 fs=18 fl=0 hz=0.022113022113022112, 9:ds=51 fs=52 fl=0 hz=0.05526036131774707, 7:ds=47 fs=40 fl=1 hz=0.0430672268907563, 18:ds=45 fs=31 fl=1 hz=0.035595105672969966

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=75 flags=blue+purple
- S20: ds=51 flags=purple
- S24: ds=46 flags=purple
- S5: ds=45 flags=purple
- S23: ds=40 flags=purple
- S21: ds=32 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '6', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=3 last_repeat_gap=11 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=34), P2:3 (gap=19), P3:1 (gap=29)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 036: score=48.71462857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 636: score=46.684243571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 035: score=43.00206428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 030: score=40.946909285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 086: score=38.06225714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 031: score=38.00329285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R3 src=cartesian
- 635: score=37.48727142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 066: score=37.36691428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 016: score=37.07118571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 026: score=36.422914285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 166: ds=893 sev=B
- 555: ds=878 sev=B
- 117: ds=866 sev=B
- 559: ds=865 sev=B
- 777: ds=837 sev=B
- 666: ds=810 sev=B
- 002: ds=798 sev=B
- 009: ds=787 sev=B
- 189: ds=741 sev=B
- 888: ds=734 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=60 sev=purple
  - 44: ds=55 sev=purple
  - 88: ds=49 sev=purple
  - 22: ds=40 sev=purple
  - 00: ds=34 sev=purple
  - 55: ds=31 sev=purple
  - 77: ds=22 sev=-
  - 11: ds=13 sev=-
  - 33: ds=3 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 36: ds=61 sev=red
  - 69: ds=48 sev=blue
  - 15: ds=47 sev=blue
  - 35: ds=39 sev=blue
  - 39: ds=39 sev=blue
  - 18: ds=35 sev=purple
  - 49: ds=32 sev=purple
  - 14: ds=29 sev=purple
  - 28: ds=28 sev=purple
  - 16: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:198, 23:187, 10:111, 20:79, 28:70, 18:60, 9:57, 15:55, 21:51, 6:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=198 fs=2 fl=1 hz=0.006426735218508998, 23:ds=187 fs=20 fl=2 hz=0.030219780219780217, 10:ds=111 fs=19 fl=2 hz=0.02367531003382187, 20:ds=79 fs=17 fl=3 hz=0.022246941045606226, 28:ds=70 fs=23 fl=3 hz=0.028047464940668825, 18:ds=60 fs=22 fl=2 hz=0.026115342763873776, 9:ds=57 fs=49 fl=0 hz=0.05268817204301075, 15:ds=55 fs=32 fl=1 hz=0.03737259343148358, 21:ds=51 fs=51 fl=0 hz=0.0551948051948052, 6:ds=50 fs=18 fl=3 hz=0.025893958076448828

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S23: ds=97 flags=purple
- S6: ds=90 flags=red+purple
- S25: ds=65 flags=purple
- S21: ds=59 flags=red+purple
- S19: ds=48 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 566 -> combined:834(B); midday:870(B)
- 666 -> evening:810(B); midday:915(B)
- 669 -> combined:920(B); midday:996(B)
- 777 -> combined:683(B); evening:837(B)
- 779 -> combined:715(B); evening:726(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 01 -> combined:52(blue); evening:26(purple); midday:30(purple)
- 02 -> combined:38(blue); midday:54(blue)
- 12 -> combined:26(purple); midday:27(purple)
- 16 -> combined:54(blue); evening:27(purple); midday:74(red)
- 18 -> combined:70(red); evening:35(purple); midday:66(red)
- 19 -> combined:28(purple); midday:38(blue)
- 28 -> combined:47(blue); evening:28(purple)
- 36 -> combined:31(purple); evening:61(red)
- 66 -> combined:120(red); evening:60(purple); midday:135(red)
- 68 -> combined:40(blue); midday:49(blue)
- 69 -> combined:37(blue); evening:48(blue)
- 77 -> combined:44(purple); midday:35(purple)
- 88 -> combined:27(purple); evening:49(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.125792857142857)[R1,XVAR-Cons(CEM)], 6(4.111)[R2,XVAR-Cons(CM)], 1(0.9417)[R2,Double-Pressure], 9(0.3761999999999999)[R2], 7(0.21214285714285713)[R3]
- P2: 3(6.585142857142857)[R1,XVAR-Cons(CEM)], 6(1.2374285714285713)[R1,Double-Pressure], 1(0.9417)[R2,Double-Pressure], 8(0.9327714285714285)[R2,Mirror-Echo], 2(0.29342857142857137)[R2,Mirror-Echo]
- P3: 6(7.503692857142857)[R1,XVAR-Cons(CEM)], 5(4.291128571428571)[R2,XVAR-Cons(CM)], 0(1.998642857142857)[R1,Mirror-Echo], 1(1.7923571428571428)[R1,Mirror-Echo], 4(0.21497142857142856)[R3]
