# Aux Summary — Indiana4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/Indiana4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Indiana
- combined: live=`data/cleaned/draws/Indiana_draws.csv` snap=`sharepacks/2026-01-01/Indiana4/aux/draws/Indiana_draws.csv` n=1000 head=539, 204, 512, 585, 560
- midday: live=`data/cleaned/draws/Indiana_Midday_draws.csv` snap=`sharepacks/2026-01-01/Indiana4/aux/draws/Indiana_Midday_draws.csv` n=1000 head=204, 585, 144, 494, 351
- evening: live=`data/cleaned/draws/Indiana_Evening_draws.csv` snap=`sharepacks/2026-01-01/Indiana4/aux/draws/Indiana_Evening_draws.csv` n=1000 head=539, 512, 560, 998, 803

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=15 last_repeat_index=27

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=27), P2:2 (gap=15), P3:6 (gap=35)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 026: score=44.23043571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 076: score=43.44428571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 056: score=42.37363571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 626: score=42.251891428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 676: score=41.46574142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 656: score=40.39509142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 066: score=38.61535000000001 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 021: score=37.15882142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 666: score=36.636805714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 036: score=36.569007142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 068: ds=981 sev=B
- 066: ds=936 sev=B
- 669: ds=924 sev=B
- 258: ds=893 sev=B
- 566: ds=838 sev=B
- 688: ds=824 sev=B
- 667: ds=755 sev=B
- 447: ds=738 sev=B
- 244: ds=724 sev=B
- 779: ds=719 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=124 sev=red
  - 77: ds=48 sev=purple
  - 88: ds=31 sev=purple
  - 00: ds=27 sev=purple
  - 22: ds=15 sev=-
  - 11: ds=11 sev=-
  - 33: ds=10 sev=-
  - 99: ds=6 sev=-
  - 44: ds=5 sev=-
  - 55: ds=3 sev=-
- non_repeating:
  - 18: ds=74 sev=red
  - 16: ds=58 sev=red
  - 01: ds=56 sev=red
  - 28: ds=51 sev=blue
  - 68: ds=44 sev=blue
  - 69: ds=41 sev=blue
  - 57: ds=36 sev=purple
  - 36: ds=35 sev=purple
  - 67: ds=35 sev=purple
  - 19: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:275, 28:144, 9:107, 6:104, 18:95, 5:78, 1:72, 10:71, 19:62, 20:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=275 fs=2 fl=1 hz=0.006956521739130435, 28:ds=144 fs=19 fl=1 hz=0.025149700598802397, 9:ds=107 fs=52 fl=0 hz=0.05855855855855856, 6:ds=104 fs=12 fl=2 hz=0.016222479721900347, 18:ds=95 fs=24 fl=1 hz=0.029478458049886625, 5:ds=78 fs=22 fl=2 hz=0.026519337016574582, 1:ds=72 fs=4 fl=3 hz=0.008830022075055188, 10:ds=71 fs=17 fl=3 hz=0.023391812865497075, 19:ds=62 fs=29 fl=1 hz=0.032051282051282055, 20:ds=53 fs=18 fl=2 hz=0.021299254526091587

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=85 flags=purple
- S21: ds=69 flags=purple
- S13: ds=49 flags=red+purple
- S10: ds=46 flags=red+purple
- S5: ds=42 flags=purple
- S19: ds=31 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 037: score=3 tags=FLT,RS
  - 127: score=3 tags=FLT,RS
  - 379: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS
  - 019: score=2 tags=RS
  - 028: score=2 tags=RS
  - 046: score=2 tags=RS
  - 136: score=2 tags=RS
  - 145: score=2 tags=RS
  - 235: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=2 last_repeat_gap=80 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=46), P2:6 (gap=20), P3:0 (gap=36)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=46)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 026: score=44.23043571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 076: score=43.44428571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 056: score=42.37363571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 626: score=42.251891428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 676: score=41.46574142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 656: score=40.39509142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 066: score=38.61535000000001 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 021: score=37.15882142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 666: score=36.636805714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 036: score=36.569007142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 669: ds=998 sev=B
- 288: ds=993 sev=B
- 337: ds=945 sev=B
- 666: ds=917 sev=B
- 677: ds=915 sev=B
- 566: ds=872 sev=B
- 445: ds=808 sev=B
- 266: ds=768 sev=B
- 444: ds=766 sev=B
- 177: ds=729 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=137 sev=red
  - 77: ds=37 sev=purple
  - 33: ds=22 sev=-
  - 88: ds=15 sev=-
  - 00: ds=13 sev=-
  - 99: ds=9 sev=-
  - 22: ds=7 sev=-
  - 11: ds=5 sev=-
  - 44: ds=2 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 45: ds=102 sev=red
  - 16: ds=76 sev=red
  - 18: ds=68 sev=red
  - 56: ds=53 sev=blue
  - 68: ds=51 sev=blue
  - 05: ds=45 sev=blue
  - 19: ds=40 sev=blue
  - 01: ds=32 sev=purple
  - 08: ds=31 sev=purple
  - 12: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:243, 16:137, 6:104, 24:86, 28:79, 13:67, 5:55, 9:53, 7:49, 18:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=243 fs=3 fl=1 hz=0.007668711656441718, 16:ds=137 fs=4 fl=0 hz=0.007342143906020559, 6:ds=104 fs=20 fl=2 hz=0.02458100558659218, 24:ds=86 fs=43 fl=1 hz=0.0484048404840484, 28:ds=79 fs=18 fl=1 hz=0.022650056625141565, 13:ds=67 fs=15 fl=1 hz=0.021505376344086023, 5:ds=55 fs=18 fl=0 hz=0.022113022113022112, 9:ds=53 fs=52 fl=0 hz=0.05526036131774707, 7:ds=49 fs=39 fl=1 hz=0.04314994606256742, 18:ds=47 fs=31 fl=1 hz=0.035595105672969966

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=77 flags=blue+purple
- S20: ds=53 flags=purple
- S24: ds=48 flags=purple
- S5: ds=47 flags=purple
- S23: ds=42 flags=purple
- S21: ds=34 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=13 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=36), P2:5 (gap=13), P3:1 (gap=31)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 026: score=44.23043571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 076: score=43.44428571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 056: score=42.37363571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 626: score=42.251891428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 676: score=41.46574142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 656: score=40.39509142857142 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 066: score=38.61535000000001 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 021: score=37.15882142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 666: score=36.636805714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 036: score=36.569007142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 166: ds=895 sev=B
- 555: ds=880 sev=B
- 117: ds=868 sev=B
- 559: ds=867 sev=B
- 777: ds=839 sev=B
- 666: ds=812 sev=B
- 002: ds=800 sev=B
- 009: ds=789 sev=B
- 189: ds=743 sev=B
- 888: ds=736 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=62 sev=purple
  - 44: ds=57 sev=purple
  - 88: ds=51 sev=purple
  - 22: ds=42 sev=purple
  - 00: ds=36 sev=purple
  - 55: ds=33 sev=purple
  - 77: ds=24 sev=-
  - 11: ds=15 sev=-
  - 33: ds=5 sev=-
  - 99: ds=3 sev=-
- non_repeating:
  - 36: ds=63 sev=red
  - 69: ds=50 sev=blue
  - 18: ds=37 sev=blue
  - 49: ds=34 sev=purple
  - 14: ds=31 sev=purple
  - 28: ds=30 sev=purple
  - 16: ds=29 sev=purple
  - 01: ds=28 sev=purple
  - 13: ds=28 sev=purple
  - 34: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:200, 23:189, 10:113, 20:81, 28:72, 18:62, 9:59, 15:57, 21:53, 6:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=200 fs=2 fl=1 hz=0.006426735218508998, 23:ds=189 fs=20 fl=2 hz=0.030219780219780217, 10:ds=113 fs=18 fl=2 hz=0.02301495972382048, 20:ds=81 fs=17 fl=3 hz=0.022246941045606226, 28:ds=72 fs=23 fl=3 hz=0.028047464940668825, 18:ds=62 fs=22 fl=2 hz=0.026115342763873776, 9:ds=59 fs=49 fl=0 hz=0.05268817204301075, 15:ds=57 fs=32 fl=1 hz=0.03737259343148358, 21:ds=53 fs=51 fl=0 hz=0.0551948051948052, 6:ds=52 fs=18 fl=3 hz=0.025893958076448828

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S23: ds=99 flags=purple
- S6: ds=92 flags=red+purple
- S25: ds=67 flags=purple
- S21: ds=61 flags=red+purple
- S19: ds=50 flags=red+purple

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
- 566 -> combined:838(B); midday:872(B)
- 666 -> evening:812(B); midday:917(B)
- 669 -> combined:924(B); midday:998(B)
- 777 -> combined:687(B); evening:839(B)
- 779 -> combined:719(B); evening:728(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:27(purple); evening:36(purple)
- 01 -> combined:56(red); evening:28(purple); midday:32(purple)
- 09 -> combined:28(purple); midday:27(purple)
- 16 -> combined:58(red); evening:29(purple); midday:76(red)
- 18 -> combined:74(red); evening:37(blue); midday:68(red)
- 19 -> combined:32(purple); midday:40(blue)
- 28 -> combined:51(blue); evening:30(purple); midday:25(purple)
- 36 -> combined:35(purple); evening:63(red)
- 66 -> combined:124(red); evening:62(purple); midday:137(red)
- 68 -> combined:44(blue); midday:51(blue)
- 69 -> combined:41(blue); evening:50(blue)
- 77 -> combined:48(purple); midday:37(purple)
- 88 -> combined:31(purple); evening:51(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(7.378235714285715)[R1,XVAR-Cons(CEM)], 6(4.129)[R2,XVAR-Cons(CM)], 1(0.9834999999999999)[R2,Double-Pressure], 9(0.48799999999999993)[R2,Swap], 7(0.3687142857142857)[R3,Swap]
- P2: 2(3.4122285714285714)[R1,Mirror-Echo], 7(2.6260785714285713)[R2,Mirror-Echo], 5(2.5554285714285716)[R3,XVAR-Cons(CE)], 6(1.2971428571428572)[R1,Double-Pressure], 3(0.25079999999999997)[R2]
- P3: 6(8.439971428571429)[R1,Mirror-Echo], 1(3.8683571428571426)[R3,Mirror-Echo], 0(1.7149999999999999)[R1,Double-Pressure], 7(0.942)[R2,Double-Pressure], 4(0.2418428571428571)[R3]
