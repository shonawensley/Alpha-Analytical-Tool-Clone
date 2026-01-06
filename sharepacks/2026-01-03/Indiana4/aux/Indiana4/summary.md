# Aux Summary — Indiana4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/Indiana4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Indiana
- combined: live=`data/cleaned/draws/Indiana_draws.csv` snap=`sharepacks/2026-01-03/Indiana4/aux/draws/Indiana_draws.csv` n=1000 head=359, 974, 909, 474, 539
- midday: live=`data/cleaned/draws/Indiana_Midday_draws.csv` snap=`sharepacks/2026-01-03/Indiana4/aux/draws/Indiana_Midday_draws.csv` n=1000 head=974, 474, 204, 585, 144
- evening: live=`data/cleaned/draws/Indiana_Evening_draws.csv` snap=`sharepacks/2026-01-03/Indiana4/aux/draws/Indiana_Evening_draws.csv` n=1000 head=359, 909, 539, 512, 560

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=19 last_repeat_index=27

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=31), P2:2 (gap=19), P3:6 (gap=39)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 026: score=50.53413571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 626: score=48.056378571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 046: score=44.0873 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 021: score=43.46135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 646: score=41.60954285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 020: score=40.506042857142866 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 096: score=40.05707142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 066: score=39.46607142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 076: score=38.5067 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 696: score=37.57931428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 068: ds=985 sev=B
- 066: ds=940 sev=B
- 669: ds=928 sev=B
- 258: ds=897 sev=B
- 566: ds=842 sev=B
- 688: ds=828 sev=B
- 667: ds=759 sev=B
- 244: ds=728 sev=B
- 779: ds=723 sev=B
- 335: ds=711 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=128 sev=red
  - 77: ds=52 sev=purple
  - 88: ds=35 sev=purple
  - 00: ds=31 sev=purple
  - 22: ds=19 sev=-
  - 11: ds=15 sev=-
  - 33: ds=14 sev=-
  - 55: ds=7 sev=-
  - 44: ds=3 sev=-
  - 99: ds=2 sev=-
- non_repeating:
  - 18: ds=78 sev=red
  - 16: ds=62 sev=red
  - 01: ds=60 sev=red
  - 28: ds=55 sev=blue
  - 68: ds=48 sev=blue
  - 69: ds=45 sev=blue
  - 57: ds=40 sev=blue
  - 36: ds=39 sev=blue
  - 67: ds=39 sev=blue
  - 19: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:279, 28:148, 9:111, 6:108, 18:99, 5:82, 1:76, 10:75, 19:66, 20:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=279 fs=2 fl=1 hz=0.006956521739130435, 28:ds=148 fs=19 fl=1 hz=0.025149700598802397, 9:ds=111 fs=52 fl=0 hz=0.05855855855855856, 6:ds=108 fs=12 fl=2 hz=0.016222479721900347, 18:ds=99 fs=24 fl=1 hz=0.029478458049886625, 5:ds=82 fs=22 fl=2 hz=0.026519337016574582, 1:ds=76 fs=4 fl=3 hz=0.008830022075055188, 10:ds=75 fs=17 fl=3 hz=0.023391812865497075, 19:ds=66 fs=28 fl=1 hz=0.031115879828326178, 20:ds=57 fs=18 fl=2 hz=0.021299254526091587

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=89 flags=purple
- S21: ds=73 flags=purple
- S13: ds=53 flags=red+purple
- S10: ds=50 flags=red+purple
- S5: ds=46 flags=purple
- S19: ds=35 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '6', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 019: score=3 tags=FLT,RS
  - 028: score=3 tags=FLT,RS
  - 046: score=3 tags=FLT,RS
  - 127: score=3 tags=FLT,RS
  - 136: score=3 tags=FLT,RS
  - 145: score=3 tags=FLT,RS
  - 235: score=3 tags=FLT,RS
  - 289: score=3 tags=FLT,RS
  - 469: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=2 max=2 last_repeat_gap=1 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=48), P2:6 (gap=22), P3:0 (gap=38)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=48)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 026: score=50.53413571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 626: score=48.056378571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 046: score=44.0873 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 021: score=43.46135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 646: score=41.60954285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 020: score=40.506042857142866 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 096: score=40.05707142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 066: score=39.46607142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 076: score=38.5067 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 696: score=37.57931428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 288: ds=995 sev=B
- 337: ds=947 sev=B
- 666: ds=919 sev=B
- 677: ds=917 sev=B
- 566: ds=874 sev=B
- 445: ds=810 sev=B
- 266: ds=770 sev=B
- 444: ds=768 sev=B
- 177: ds=731 sev=B
- 488: ds=704 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=139 sev=red
  - 77: ds=39 sev=purple
  - 33: ds=24 sev=-
  - 88: ds=17 sev=-
  - 00: ds=15 sev=-
  - 99: ds=11 sev=-
  - 22: ds=9 sev=-
  - 11: ds=7 sev=-
  - 55: ds=3 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 45: ds=104 sev=red
  - 16: ds=78 sev=red
  - 18: ds=70 sev=red
  - 56: ds=55 sev=blue
  - 68: ds=53 sev=blue
  - 05: ds=47 sev=blue
  - 19: ds=42 sev=blue
  - 01: ds=34 sev=purple
  - 08: ds=33 sev=purple
  - 12: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:245, 16:139, 6:106, 24:88, 28:81, 13:69, 5:57, 9:55, 7:51, 18:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=245 fs=3 fl=1 hz=0.007668711656441718, 16:ds=139 fs=4 fl=0 hz=0.007342143906020559, 6:ds=106 fs=19 fl=2 hz=0.024110218140068886, 24:ds=88 fs=43 fl=1 hz=0.0484048404840484, 28:ds=81 fs=18 fl=1 hz=0.022650056625141565, 13:ds=69 fs=15 fl=1 hz=0.021505376344086023, 5:ds=57 fs=18 fl=0 hz=0.022113022113022112, 9:ds=55 fs=52 fl=0 hz=0.05526036131774707, 7:ds=51 fs=39 fl=1 hz=0.04314994606256742, 18:ds=49 fs=31 fl=1 hz=0.035595105672969966

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=79 flags=blue+purple
- S24: ds=50 flags=purple
- S5: ds=49 flags=purple
- S23: ds=44 flags=purple
- S21: ds=36 flags=purple
- S4: ds=34 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 016: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 156: score=2 tags=FLT,MIR
  - 167: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=15 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=38), P2:2 (gap=14), P3:1 (gap=33)
- consensus_notes: P1 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 026: score=50.53413571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 626: score=48.056378571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 046: score=44.0873 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 021: score=43.46135 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 646: score=41.60954285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 020: score=40.506042857142866 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 096: score=40.05707142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 066: score=39.46607142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 076: score=38.5067 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 696: score=37.57931428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 166: ds=897 sev=B
- 555: ds=882 sev=B
- 117: ds=870 sev=B
- 559: ds=869 sev=B
- 777: ds=841 sev=B
- 666: ds=814 sev=B
- 002: ds=802 sev=B
- 009: ds=791 sev=B
- 189: ds=745 sev=B
- 888: ds=738 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=64 sev=purple
  - 44: ds=59 sev=purple
  - 88: ds=53 sev=purple
  - 22: ds=44 sev=purple
  - 00: ds=38 sev=purple
  - 55: ds=35 sev=purple
  - 77: ds=26 sev=purple
  - 11: ds=17 sev=-
  - 33: ds=7 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 36: ds=65 sev=red
  - 69: ds=52 sev=blue
  - 18: ds=39 sev=blue
  - 49: ds=36 sev=purple
  - 14: ds=33 sev=purple
  - 28: ds=32 sev=purple
  - 16: ds=31 sev=purple
  - 01: ds=30 sev=purple
  - 13: ds=30 sev=purple
  - 34: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:202, 23:191, 10:115, 20:83, 28:74, 18:64, 9:61, 21:55, 6:54, 25:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=202 fs=2 fl=1 hz=0.006426735218508998, 23:ds=191 fs=20 fl=2 hz=0.030219780219780217, 10:ds=115 fs=18 fl=2 hz=0.02301495972382048, 20:ds=83 fs=17 fl=3 hz=0.022246941045606226, 28:ds=74 fs=22 fl=3 hz=0.02774694783573807, 18:ds=64 fs=22 fl=2 hz=0.026115342763873776, 9:ds=61 fs=49 fl=0 hz=0.05268817204301075, 21:ds=55 fs=51 fl=0 hz=0.0551948051948052, 6:ds=54 fs=18 fl=3 hz=0.025893958076448828, 25:ds=52 fs=17 fl=1 hz=0.01958650707290533

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=94 flags=red+purple
- S25: ds=69 flags=purple
- S21: ds=63 flags=red+purple
- S19: ds=52 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [1], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '7', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 028: score=3 tags=FLT,RS
  - 037: score=3 tags=FLT,RS
  - 046: score=3 tags=FLT,RS
  - 127: score=3 tags=FLT,RS
  - 145: score=3 tags=FLT,RS
  - 289: score=3 tags=FLT,RS
  - 379: score=3 tags=FLT,RS
  - 469: score=3 tags=FLT,RS
  - 478: score=3 tags=FLT,RS
  - 568: score=3 tags=FLT,RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 566 -> combined:842(B); midday:874(B)
- 666 -> evening:814(B); midday:919(B)
- 777 -> combined:691(B); evening:841(B)
- 779 -> combined:723(B); evening:730(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:31(purple); evening:38(purple)
- 01 -> combined:60(red); evening:30(purple); midday:34(purple)
- 16 -> combined:62(red); evening:31(purple); midday:78(red)
- 18 -> combined:78(red); evening:39(blue); midday:70(red)
- 19 -> combined:36(purple); midday:42(blue)
- 26 -> combined:26(purple); midday:28(purple)
- 28 -> combined:55(blue); evening:32(purple); midday:27(purple)
- 34 -> combined:29(purple); evening:25(purple)
- 36 -> combined:39(blue); evening:65(red)
- 45 -> combined:28(purple); midday:104(red)
- 57 -> combined:40(blue); midday:25(purple)
- 66 -> combined:128(red); evening:64(purple); midday:139(red)
- 68 -> combined:48(blue); midday:53(blue)
- 69 -> combined:45(blue); evening:52(blue)
- 77 -> combined:52(purple); evening:26(purple); midday:39(purple)
- 88 -> combined:35(purple); evening:53(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 0(8.032785714285714)[R1,XVAR-Cons(CEM)], 6(4.217)[R2,XVAR-Cons(CM)], 1(1.0252999999999999)[R2,Double-Pressure], 7(0.42528571428571427)[R3,Swap], 4(0.2881)[R3,Swap]
- P2: 2(6.4249214285714285)[R1,XVAR-Cons(CEM)], 4(2.4780857142857142)[R3,Mirror-Echo], 6(1.3568571428571428)[R1,Double-Pressure], 9(0.9478571428571428)[R2,Mirror-Echo], 7(0.3974857142857143)[R3,Mirror-Echo]
- P3: 6(8.576428571428572)[R1,Mirror-Echo], 1(4.003642857142857)[R3,Mirror-Echo], 0(1.645)[R1,Double-Pressure], 7(1.03)[R2,Double-Pressure], 4(0.3687142857142857)[R3,Swap]
