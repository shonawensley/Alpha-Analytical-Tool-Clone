# Aux Summary — Indiana4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/Indiana4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Indiana
- combined: live=`data/cleaned/draws/Indiana_draws.csv` snap=`sharepacks/2026-01-04/Indiana4/aux/draws/Indiana_draws.csv` n=1000 head=199, 527, 359, 974, 909
- midday: live=`data/cleaned/draws/Indiana_Midday_draws.csv` snap=`sharepacks/2026-01-04/Indiana4/aux/draws/Indiana_Midday_draws.csv` n=1000 head=527, 974, 474, 204, 585
- evening: live=`data/cleaned/draws/Indiana_Evening_draws.csv` snap=`sharepacks/2026-01-04/Indiana4/aux/draws/Indiana_Evening_draws.csv` n=1000 head=199, 359, 909, 539, 512

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=25 streak=1 max=3 last_repeat_gap=21 last_repeat_index=27

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=33), P2:4 (gap=11), P3:6 (gap=41)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 666: score=49.51709857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 646: score=48.078941428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 066: score=45.570342857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 046: score=44.13218571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 626: score=42.93434857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 616: score=42.88115571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 676: score=42.78602 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 636: score=41.77502714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 061: score=39.12125714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 026: score=38.98759285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 068: ds=987 sev=B
- 066: ds=942 sev=B
- 669: ds=930 sev=B
- 258: ds=899 sev=B
- 566: ds=844 sev=B
- 688: ds=830 sev=B
- 667: ds=761 sev=B
- 244: ds=730 sev=B
- 779: ds=725 sev=B
- 335: ds=713 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=130 sev=red
  - 77: ds=54 sev=purple
  - 88: ds=37 sev=purple
  - 00: ds=33 sev=purple
  - 22: ds=21 sev=-
  - 11: ds=17 sev=-
  - 33: ds=16 sev=-
  - 55: ds=9 sev=-
  - 44: ds=5 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 18: ds=80 sev=red
  - 16: ds=64 sev=red
  - 01: ds=62 sev=red
  - 28: ds=57 sev=red
  - 68: ds=50 sev=blue
  - 69: ds=47 sev=blue
  - 36: ds=41 sev=blue
  - 67: ds=41 sev=blue
  - 34: ds=31 sev=purple
  - 48: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:281, 28:150, 9:113, 6:110, 18:101, 5:84, 1:78, 19:68, 20:59, 23:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=281 fs=2 fl=1 hz=0.006956521739130435, 28:ds=150 fs=19 fl=1 hz=0.025149700598802397, 9:ds=113 fs=51 fl=0 hz=0.057692307692307696, 6:ds=110 fs=12 fl=2 hz=0.016222479721900347, 18:ds=101 fs=24 fl=1 hz=0.029478458049886625, 5:ds=84 fs=22 fl=2 hz=0.026519337016574582, 1:ds=78 fs=4 fl=3 hz=0.008830022075055188, 19:ds=68 fs=27 fl=1 hz=0.030735455543358946, 20:ds=59 fs=18 fl=2 hz=0.021299254526091587, 23:ds=51 fs=19 fl=2 hz=0.02346368715083799

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=91 flags=purple
- S21: ds=75 flags=purple
- S13: ds=55 flags=red+purple
- S10: ds=52 flags=red+purple
- S5: ds=48 flags=purple
- S4: ds=36 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 058: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=2 last_repeat_gap=2 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=49), P2:6 (gap=23), P3:0 (gap=39)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=49)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 666: score=49.51709857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 646: score=48.078941428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 066: score=45.570342857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 046: score=44.13218571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 626: score=42.93434857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 616: score=42.88115571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 676: score=42.78602 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 636: score=41.77502714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 061: score=39.12125714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 026: score=38.98759285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 288: ds=996 sev=B
- 337: ds=948 sev=B
- 666: ds=920 sev=B
- 677: ds=918 sev=B
- 566: ds=875 sev=B
- 445: ds=811 sev=B
- 266: ds=771 sev=B
- 444: ds=769 sev=B
- 177: ds=732 sev=B
- 488: ds=705 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=140 sev=red
  - 77: ds=40 sev=purple
  - 33: ds=25 sev=purple
  - 88: ds=18 sev=-
  - 00: ds=16 sev=-
  - 99: ds=12 sev=-
  - 22: ds=10 sev=-
  - 11: ds=8 sev=-
  - 55: ds=4 sev=-
  - 44: ds=2 sev=-
- non_repeating:
  - 45: ds=105 sev=red
  - 16: ds=79 sev=red
  - 18: ds=71 sev=red
  - 56: ds=56 sev=red
  - 68: ds=54 sev=blue
  - 05: ds=48 sev=blue
  - 19: ds=43 sev=blue
  - 01: ds=35 sev=purple
  - 08: ds=34 sev=purple
  - 12: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:246, 16:140, 6:107, 24:89, 28:82, 13:70, 5:58, 9:56, 7:52, 18:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=246 fs=3 fl=1 hz=0.007668711656441718, 16:ds=140 fs=4 fl=0 hz=0.007342143906020559, 6:ds=107 fs=19 fl=2 hz=0.024110218140068886, 24:ds=89 fs=43 fl=1 hz=0.0484048404840484, 28:ds=82 fs=18 fl=1 hz=0.022650056625141565, 13:ds=70 fs=15 fl=1 hz=0.021505376344086023, 5:ds=58 fs=18 fl=0 hz=0.022113022113022112, 9:ds=56 fs=52 fl=0 hz=0.05526036131774707, 7:ds=52 fs=39 fl=1 hz=0.04314994606256742, 18:ds=50 fs=31 fl=1 hz=0.035595105672969966

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=80 flags=blue+purple
- S24: ds=51 flags=purple
- S5: ds=50 flags=purple
- S23: ds=45 flags=purple
- S21: ds=37 flags=purple
- S4: ds=35 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=25 streak=1 max=3 last_repeat_gap=16 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=39), P2:2 (gap=15), P3:1 (gap=34)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 666: score=49.51709857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 646: score=48.078941428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 066: score=45.570342857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 046: score=44.13218571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 626: score=42.93434857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 616: score=42.88115571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 676: score=42.78602 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 636: score=41.77502714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 061: score=39.12125714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 026: score=38.98759285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 166: ds=898 sev=B
- 555: ds=883 sev=B
- 117: ds=871 sev=B
- 559: ds=870 sev=B
- 777: ds=842 sev=B
- 666: ds=815 sev=B
- 002: ds=803 sev=B
- 009: ds=792 sev=B
- 189: ds=746 sev=B
- 888: ds=739 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=65 sev=purple
  - 44: ds=60 sev=purple
  - 88: ds=54 sev=purple
  - 22: ds=45 sev=purple
  - 00: ds=39 sev=purple
  - 55: ds=36 sev=purple
  - 77: ds=27 sev=purple
  - 11: ds=18 sev=-
  - 33: ds=8 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 36: ds=66 sev=red
  - 69: ds=53 sev=blue
  - 18: ds=40 sev=blue
  - 49: ds=37 sev=blue
  - 14: ds=34 sev=purple
  - 28: ds=33 sev=purple
  - 16: ds=32 sev=purple
  - 01: ds=31 sev=purple
  - 13: ds=31 sev=purple
  - 34: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:203, 23:192, 10:116, 20:84, 28:75, 18:65, 9:62, 21:56, 6:55, 26:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=203 fs=2 fl=1 hz=0.006426735218508998, 23:ds=192 fs=20 fl=2 hz=0.030219780219780217, 10:ds=116 fs=18 fl=2 hz=0.02301495972382048, 20:ds=84 fs=17 fl=3 hz=0.022246941045606226, 28:ds=75 fs=22 fl=3 hz=0.02774694783573807, 18:ds=65 fs=22 fl=2 hz=0.026115342763873776, 9:ds=62 fs=49 fl=0 hz=0.05268817204301075, 21:ds=56 fs=51 fl=0 hz=0.0551948051948052, 6:ds=55 fs=18 fl=3 hz=0.025893958076448828, 26:ds=45 fs=1 fl=3 hz=0.008869179600886918

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=95 flags=red+purple
- S25: ds=70 flags=purple
- S21: ds=64 flags=red+purple
- S15: ds=38 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '6', '7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 036: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 566 -> combined:844(B); midday:875(B)
- 666 -> evening:815(B); midday:920(B)
- 777 -> combined:693(B); evening:842(B)
- 779 -> combined:725(B); evening:731(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:33(purple); evening:39(purple)
- 01 -> combined:62(red); evening:31(purple); midday:35(purple)
- 07 -> combined:26(purple); midday:30(purple)
- 16 -> combined:64(red); evening:32(purple); midday:79(red)
- 18 -> combined:80(red); evening:40(blue); midday:71(red)
- 26 -> combined:28(purple); midday:29(purple)
- 28 -> combined:57(red); evening:33(purple); midday:28(purple)
- 34 -> combined:31(purple); evening:26(purple)
- 36 -> combined:41(blue); evening:66(red)
- 45 -> combined:30(purple); midday:105(red)
- 66 -> combined:130(red); evening:65(purple); midday:140(red)
- 68 -> combined:50(blue); evening:25(purple); midday:54(blue)
- 69 -> combined:47(blue); evening:53(blue)
- 77 -> combined:54(purple); evening:27(purple); midday:40(purple)
- 88 -> combined:37(purple); evening:54(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(8.116542857142857)[R1,XVAR-Cons(CEM)], 6(7.249099999999999)[R2,XVAR-Cons(CEM)], 4(1.0135)[R2,Double-Pressure], 7(0.4535714285714286)[R3,Swap], 8(0.30153571428571424)[R3,Swap]
- P2: 6(3.6555714285714282)[R2,XVAR-Cons(CM)], 4(3.217414285714286)[R1,XVAR-Cons(CE)], 2(0.5728214285714285)[R1,Mirror-Echo], 1(0.5196285714285714)[R3,Mirror-Echo], 7(0.4244928571428571)[R3,Mirror-Echo]
- P3: 6(8.798228571428572)[R1,Mirror-Echo], 1(4.849142857142857)[R2,Mirror-Echo], 0(1.645)[R1,Double-Pressure], 4(0.38215)[R3,Swap], 3(0.29800000000000004)[R3,Swap]
