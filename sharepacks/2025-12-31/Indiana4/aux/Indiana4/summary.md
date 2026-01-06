# Aux Summary — Indiana4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/Indiana4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Indiana
- combined: live=`data/cleaned/draws/Indiana_draws.csv` snap=`sharepacks/2025-12-31/Indiana4/aux/draws/Indiana_draws.csv` n=1000 head=512, 585, 560, 144, 998
- midday: live=`data/cleaned/draws/Indiana_Midday_draws.csv` snap=`sharepacks/2025-12-31/Indiana4/aux/draws/Indiana_Midday_draws.csv` n=1000 head=585, 144, 494, 351, 117
- evening: live=`data/cleaned/draws/Indiana_Evening_draws.csv` snap=`sharepacks/2025-12-31/Indiana4/aux/draws/Indiana_Evening_draws.csv` n=1000 head=512, 560, 998, 803, 383

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=13 last_repeat_index=27

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=25), P2:3 (gap=23), P3:6 (gap=33)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 036: score=49.38572857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 636: score=47.44345142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 026: score=41.363907142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 076: score=41.30161428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 030: score=39.52092571428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 626: score=39.42163 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 676: score=39.35933714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 066: score=38.26311428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 031: score=37.95355714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 056: score=37.916628571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 068: ds=979 sev=B
- 066: ds=934 sev=B
- 669: ds=922 sev=B
- 258: ds=891 sev=B
- 566: ds=836 sev=B
- 688: ds=822 sev=B
- 667: ds=753 sev=B
- 447: ds=736 sev=B
- 244: ds=722 sev=B
- 779: ds=717 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=122 sev=red
  - 77: ds=46 sev=purple
  - 88: ds=29 sev=purple
  - 00: ds=25 sev=purple
  - 22: ds=13 sev=-
  - 11: ds=9 sev=-
  - 33: ds=8 sev=-
  - 99: ds=4 sev=-
  - 44: ds=3 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 18: ds=72 sev=red
  - 16: ds=56 sev=red
  - 01: ds=54 sev=blue
  - 28: ds=49 sev=blue
  - 68: ds=42 sev=blue
  - 02: ds=40 sev=blue
  - 69: ds=39 sev=blue
  - 57: ds=34 sev=purple
  - 36: ds=33 sev=purple
  - 67: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:273, 28:142, 9:105, 6:102, 18:93, 5:76, 1:70, 10:69, 19:60, 20:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=273 fs=2 fl=1 hz=0.006956521739130435, 28:ds=142 fs=19 fl=1 hz=0.025149700598802397, 9:ds=105 fs=52 fl=0 hz=0.05855855855855856, 6:ds=102 fs=12 fl=2 hz=0.016222479721900347, 18:ds=93 fs=24 fl=1 hz=0.029478458049886625, 5:ds=76 fs=22 fl=2 hz=0.026519337016574582, 1:ds=70 fs=4 fl=3 hz=0.008830022075055188, 10:ds=69 fs=17 fl=3 hz=0.023391812865497075, 19:ds=60 fs=29 fl=1 hz=0.032051282051282055, 20:ds=51 fs=18 fl=2 hz=0.021299254526091587

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=83 flags=purple
- S21: ds=67 flags=purple
- S13: ds=47 flags=red+purple
- S10: ds=44 flags=red+purple
- S5: ds=40 flags=purple
- S6: ds=37 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 037: score=3 tags=FLT,RS
  - 127: score=3 tags=FLT,RS
  - 136: score=3 tags=FLT,RS
  - 235: score=3 tags=FLT,RS
  - 379: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 028: score=2 tags=RS
  - 046: score=2 tags=RS
  - 145: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=4 streak=1 max=2 last_repeat_gap=79 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=45), P2:6 (gap=19), P3:0 (gap=35)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=45)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 036: score=49.38572857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 636: score=47.44345142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 026: score=41.363907142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 076: score=41.30161428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 030: score=39.52092571428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 626: score=39.42163 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 676: score=39.35933714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 066: score=38.26311428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 031: score=37.95355714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 056: score=37.916628571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 669: ds=997 sev=B
- 288: ds=992 sev=B
- 337: ds=944 sev=B
- 666: ds=916 sev=B
- 677: ds=914 sev=B
- 566: ds=871 sev=B
- 445: ds=807 sev=B
- 266: ds=767 sev=B
- 444: ds=765 sev=B
- 177: ds=728 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=136 sev=red
  - 77: ds=36 sev=purple
  - 33: ds=21 sev=-
  - 88: ds=14 sev=-
  - 00: ds=12 sev=-
  - 99: ds=8 sev=-
  - 22: ds=6 sev=-
  - 11: ds=4 sev=-
  - 44: ds=1 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 45: ds=101 sev=red
  - 16: ds=75 sev=red
  - 18: ds=67 sev=red
  - 02: ds=55 sev=blue
  - 56: ds=52 sev=blue
  - 68: ds=50 sev=blue
  - 05: ds=44 sev=blue
  - 19: ds=39 sev=blue
  - 01: ds=31 sev=purple
  - 08: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:242, 16:136, 6:103, 24:85, 28:78, 13:66, 5:54, 9:52, 7:48, 18:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=242 fs=3 fl=1 hz=0.007668711656441718, 16:ds=136 fs=4 fl=0 hz=0.007342143906020559, 6:ds=103 fs=20 fl=2 hz=0.02458100558659218, 24:ds=85 fs=43 fl=1 hz=0.0484048404840484, 28:ds=78 fs=18 fl=1 hz=0.022650056625141565, 13:ds=66 fs=15 fl=1 hz=0.021505376344086023, 5:ds=54 fs=18 fl=0 hz=0.022113022113022112, 9:ds=52 fs=52 fl=0 hz=0.05526036131774707, 7:ds=48 fs=39 fl=1 hz=0.04314994606256742, 18:ds=46 fs=31 fl=1 hz=0.035595105672969966

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=76 flags=blue+purple
- S20: ds=52 flags=purple
- S24: ds=47 flags=purple
- S5: ds=46 flags=purple
- S23: ds=41 flags=purple
- S21: ds=33 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '6'], 'pairs': {'remaining_count': 1}}
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

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=12 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=35), P2:3 (gap=20), P3:1 (gap=30)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 036: score=49.38572857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 636: score=47.44345142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 026: score=41.363907142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 076: score=41.30161428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 030: score=39.52092571428571 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 626: score=39.42163 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 676: score=39.35933714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 066: score=38.26311428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 031: score=37.95355714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 056: score=37.916628571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 166: ds=894 sev=B
- 555: ds=879 sev=B
- 117: ds=867 sev=B
- 559: ds=866 sev=B
- 777: ds=838 sev=B
- 666: ds=811 sev=B
- 002: ds=799 sev=B
- 009: ds=788 sev=B
- 189: ds=742 sev=B
- 888: ds=735 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=61 sev=purple
  - 44: ds=56 sev=purple
  - 88: ds=50 sev=purple
  - 22: ds=41 sev=purple
  - 00: ds=35 sev=purple
  - 55: ds=32 sev=purple
  - 77: ds=23 sev=-
  - 11: ds=14 sev=-
  - 33: ds=4 sev=-
  - 99: ds=2 sev=-
- non_repeating:
  - 36: ds=62 sev=red
  - 69: ds=49 sev=blue
  - 35: ds=40 sev=blue
  - 39: ds=40 sev=blue
  - 18: ds=36 sev=purple
  - 49: ds=33 sev=purple
  - 14: ds=30 sev=purple
  - 28: ds=29 sev=purple
  - 16: ds=28 sev=purple
  - 01: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:199, 23:188, 10:112, 20:80, 28:71, 18:61, 9:58, 15:56, 21:52, 6:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=199 fs=2 fl=1 hz=0.006426735218508998, 23:ds=188 fs=20 fl=2 hz=0.030219780219780217, 10:ds=112 fs=19 fl=2 hz=0.02367531003382187, 20:ds=80 fs=17 fl=3 hz=0.022246941045606226, 28:ds=71 fs=23 fl=3 hz=0.028047464940668825, 18:ds=61 fs=22 fl=2 hz=0.026115342763873776, 9:ds=58 fs=49 fl=0 hz=0.05268817204301075, 15:ds=56 fs=32 fl=1 hz=0.03737259343148358, 21:ds=52 fs=51 fl=0 hz=0.0551948051948052, 6:ds=51 fs=18 fl=3 hz=0.025893958076448828

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S23: ds=98 flags=purple
- S6: ds=91 flags=red+purple
- S25: ds=66 flags=purple
- S21: ds=60 flags=red+purple
- S19: ds=49 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 566 -> combined:836(B); midday:871(B)
- 666 -> evening:811(B); midday:916(B)
- 669 -> combined:922(B); midday:997(B)
- 777 -> combined:685(B); evening:838(B)
- 779 -> combined:717(B); evening:727(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:25(purple); evening:35(purple)
- 01 -> combined:54(blue); evening:27(purple); midday:31(purple)
- 02 -> combined:40(blue); midday:55(blue)
- 09 -> combined:26(purple); midday:26(purple)
- 16 -> combined:56(red); evening:28(purple); midday:75(red)
- 18 -> combined:72(red); evening:36(purple); midday:67(red)
- 19 -> combined:30(purple); midday:39(blue)
- 28 -> combined:49(blue); evening:29(purple)
- 36 -> combined:33(purple); evening:62(red)
- 66 -> combined:122(red); evening:61(purple); midday:136(red)
- 68 -> combined:42(blue); midday:50(blue)
- 69 -> combined:39(blue); evening:49(blue)
- 77 -> combined:46(purple); midday:36(purple)
- 88 -> combined:29(purple); evening:50(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.231942857142856)[R1,XVAR-Cons(CEM)], 6(4.085)[R2,XVAR-Cons(CM)], 9(0.9970999999999999)[R2,Double-Pressure], 1(0.9625999999999999)[R2,Double-Pressure], 7(0.34042857142857147)[R3,Swap]
- P2: 3(7.389900000000001)[R1,XVAR-Cons(CEM)], 2(1.8680785714285713)[R2,Mirror-Echo], 7(1.8057857142857143)[R3,Mirror-Echo], 6(1.2672857142857143)[R1,Double-Pressure], 5(0.9208)[R2,Double-Pressure]
- P3: 6(8.263885714285713)[R1,XVAR-Cons(CEM)], 1(1.8317142857142856)[R1,Mirror-Echo], 0(1.7149999999999999)[R1,Double-Pressure], 9(0.82)[R2,Double-Pressure], 4(0.22840714285714284)[R3]
