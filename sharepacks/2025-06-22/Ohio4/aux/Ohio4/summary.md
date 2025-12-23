# Aux Summary — Ohio4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/Ohio4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Ohio
- combined: live=`data/cleaned/draws/Ohio_draws.csv` snap=`sharepacks/2025-06-22/Ohio4/aux/draws/Ohio_draws.csv` n=1000 head=868, 069, 899, 270, 412
- midday: live=`data/cleaned/draws/Ohio_Midday_draws.csv` snap=`sharepacks/2025-06-22/Ohio4/aux/draws/Ohio_Midday_draws.csv` n=1000 head=069, 270, 112, 456, 552
- evening: live=`data/cleaned/draws/Ohio_Evening_draws.csv` snap=`sharepacks/2025-06-22/Ohio4/aux/draws/Ohio_Evening_draws.csv` n=1000 head=868, 899, 412, 754, 433

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=2 last_repeat_gap=42 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=17), P2:0 (gap=19), P3:5 (gap=25)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 945: score=42.16078571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 905: score=41.45187142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 925: score=39.367571428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 935: score=37.18178571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 975: score=37.137 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 995: score=37.053399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 545: score=34.242560000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 505: score=33.53364571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 845: score=31.8983 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 525: score=31.449345714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=936 sev=B
- 166: ds=891 sev=B
- 559: ds=885 sev=B
- 668: ds=879 sev=B
- 449: ds=869 sev=B
- 377: ds=859 sev=B
- 146: ds=777 sev=B
- 339: ds=773 sev=B
- 019: ds=756 sev=B
- 888: ds=739 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=122 sev=red
  - 66: ds=84 sev=blue
  - 77: ds=33 sev=purple
  - 44: ds=31 sev=purple
  - 22: ds=22 sev=-
  - 55: ds=9 sev=-
  - 33: ds=8 sev=-
  - 11: ds=5 sev=-
  - 99: ds=2 sev=-
  - 88: ds=0 sev=-
- non_repeating:
  - 04: ds=50 sev=blue
  - 58: ds=45 sev=blue
  - 29: ds=44 sev=blue
  - 16: ds=36 sev=purple
  - 18: ds=36 sev=purple
  - 79: ds=34 sev=purple
  - 08: ds=30 sev=purple
  - 78: ds=30 sev=purple
  - 15: ds=29 sev=purple
  - 17: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 27:175, 32:138, 35:131, 1:122, 4:106, 28:88, 15:75, 2:68, 16:67, 31:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 27:ds=175 fs=22 fl=2 hz=0.030690537084398974, 32:ds=138 fs=2 fl=0 hz=0.006051437216338881, 35:ds=131 fs=0 fl=1 hz=0.0027100271002710027, 1:ds=122 fs=3 fl=1 hz=0.006702412868632708, 4:ds=106 fs=21 fl=2 hz=0.026047565118912798, 28:ds=88 fs=26 fl=1 hz=0.03085714285714286, 15:ds=75 fs=26 fl=2 hz=0.03181818181818182, 2:ds=68 fs=22 fl=2 hz=0.027809965237543453, 16:ds=67 fs=1 fl=1 hz=0.003640776699029126, 31:ds=51 fs=22 fl=3 hz=0.027964205816554812

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=95 flags=purple
- S2: ds=92 flags=blue+purple
- S5: ds=89 flags=purple
- S20: ds=51 flags=purple
- S3: ds=35 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=8 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=22), P2:3 (gap=12), P3:3 (gap=18)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 945: score=42.16078571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 905: score=41.45187142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 925: score=39.367571428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 935: score=37.18178571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 975: score=37.137 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 995: score=37.053399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 545: score=34.242560000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 505: score=33.53364571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 845: score=31.8983 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 525: score=31.449345714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 669: ds=922 sev=B
- 466: ds=896 sev=B
- 117: ds=895 sev=B
- 029: ds=888 sev=B
- 066: ds=866 sev=B
- 388: ds=846 sev=B
- 556: ds=801 sev=B
- 688: ds=778 sev=B
- 788: ds=760 sev=B
- 222: ds=743 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=82 sev=blue
  - 66: ds=54 sev=purple
  - 33: ds=51 sev=purple
  - 88: ds=47 sev=purple
  - 22: ds=44 sev=purple
  - 99: ds=25 sev=purple
  - 77: ds=16 sev=-
  - 44: ds=15 sev=-
  - 55: ds=4 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 78: ds=49 sev=blue
  - 08: ds=43 sev=blue
  - 79: ds=40 sev=blue
  - 26: ds=38 sev=blue
  - 04: ds=34 sev=purple
  - 36: ds=29 sev=purple
  - 29: ds=25 sev=purple
  - 16: ds=24 sev=-
  - 58: ds=22 sev=-
  - 18: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:285, 19:233, 32:218, 2:101, 28:93, 27:87, 34:86, 23:68, 35:65, 18:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=285 fs=2 fl=0 hz=0.006382978723404256, 19:ds=233 fs=16 fl=0 hz=0.02309782608695652, 32:ds=218 fs=4 fl=2 hz=0.009510869565217392, 2:ds=101 fs=19 fl=1 hz=0.02242152466367713, 28:ds=93 fs=24 fl=2 hz=0.029478458049886625, 27:ds=87 fs=24 fl=2 hz=0.030842230130486363, 34:ds=86 fs=26 fl=2 hz=0.030701754385964914, 23:ds=68 fs=25 fl=0 hz=0.032552083333333336, 35:ds=65 fs=0 fl=3 hz=0.005333333333333333, 18:ds=54 fs=15 fl=3 hz=0.0192102454642476

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=77 flags=purple
- S22: ds=65 flags=purple
- S24: ds=61 flags=purple
- S25: ds=47 flags=purple
- S2: ds=46 flags=blue+purple
- S5: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=3 last_repeat_gap=12 last_repeat_index=10

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=17), P2:4 (gap=19), P3:5 (gap=34)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 945: score=42.16078571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 905: score=41.45187142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 925: score=39.367571428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 935: score=37.18178571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 975: score=37.137 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 995: score=37.053399999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 545: score=34.242560000000005 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 505: score=33.53364571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 845: score=31.8983 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 525: score=31.449345714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap

### Doubles (source: aux_validation.collect_variant_stats)
- 446: ds=956 sev=B
- 199: ds=832 sev=B
- 678: ds=826 sev=B
- 003: ds=825 sev=B
- 357: ds=805 sev=B
- 559: ds=800 sev=B
- 777: ds=777 sev=B
- 166: ds=749 sev=B
- 224: ds=745 sev=B
- 038: ds=726 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=89 sev=blue
  - 00: ds=61 sev=purple
  - 77: ds=47 sev=purple
  - 66: ds=42 sev=purple
  - 44: ds=19 sev=-
  - 22: ds=11 sev=-
  - 11: ds=9 sev=-
  - 33: ds=4 sev=-
  - 99: ds=1 sev=-
  - 88: ds=0 sev=-
- non_repeating:
  - 37: ds=76 sev=red
  - 35: ds=53 sev=blue
  - 39: ds=50 sev=blue
  - 58: ds=49 sev=blue
  - 38: ds=45 sev=blue
  - 56: ds=42 sev=blue
  - 48: ds=40 sev=blue
  - 05: ds=34 sev=purple
  - 69: ds=29 sev=purple
  - 09: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:253, 15:139, 35:133, 3:118, 27:110, 16:94, 5:85, 30:76, 32:69, 1:61

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=253 fs=4 fl=1 hz=0.009646302250803858, 15:ds=139 fs=27 fl=0 hz=0.03214285714285715, 35:ds=133 fs=1 fl=1 hz=0.00423728813559322, 3:ds=118 fs=24 fl=1 hz=0.02937720329024677, 27:ds=110 fs=21 fl=3 hz=0.027777777777777776, 16:ds=94 fs=1 fl=1 hz=0.003886010362694301, 5:ds=85 fs=14 fl=3 hz=0.020383693045563547, 30:ds=76 fs=37 fl=0 hz=0.04138702460850112, 32:ds=69 fs=0 fl=0 hz=0.0011534025374855825, 1:ds=61 fs=3 fl=0 hz=0.006024096385542169

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=73 flags=purple
- S5: ds=56 flags=blue+purple
- S21: ds=51 flags=red+purple
- S2: ds=46 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
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
- 029 -> combined:714(B); midday:888(B)
- 066 -> combined:936(B); midday:866(B)
- 166 -> combined:891(B); evening:749(B)
- 224 -> evening:745(B); midday:697(B)
- 449 -> combined:869(B); evening:678(B)
- 559 -> combined:885(B); evening:800(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:122(red); evening:61(purple); midday:82(blue)
- 04 -> combined:50(blue); evening:25(purple); midday:34(purple)
- 05 -> combined:27(purple); evening:34(purple)
- 08 -> combined:30(purple); midday:43(blue)
- 29 -> combined:44(blue); midday:25(purple)
- 35 -> combined:25(purple); evening:53(blue)
- 39 -> combined:25(purple); evening:50(blue)
- 58 -> combined:45(blue); evening:49(blue)
- 66 -> combined:84(blue); evening:42(purple); midday:54(purple)
- 77 -> combined:33(purple); evening:47(purple)
- 78 -> combined:30(purple); midday:49(blue)
- 79 -> combined:34(purple); midday:40(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(6.519342857142857)[R1,XVAR-Cons(CEM)], 8(1.2568571428571427)[R1,Double-Pressure], 7(0.9925999999999999)[R2,Double-Pressure], 5(0.8998999999999999)[R2,Double-Pressure], 6(0.264)[R2]
- P2: 4(3.537285714285714)[R2,XVAR-Cons(CE)], 0(2.8283714285714288)[R1,XVAR-Cons(CE)], 2(1.7440714285714287)[R3,XVAR-Cons(CM)], 3(1.0582857142857143)[R1,Double-Pressure], 7(1.0135)[R2,Double-Pressure]
- P3: 5(8.104157142857144)[R1,XVAR-Cons(CEM)], 1(1.5892214285714288)[R3,XVAR-Cons(CM)], 0(1.4749285714285714)[R2,Mirror-Echo], 3(1.1374285714285712)[R1,Double-Pressure], 7(0.964)[R2,Double-Pressure]
