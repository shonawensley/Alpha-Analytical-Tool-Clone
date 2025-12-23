# Aux Summary — Ohio4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/Ohio4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Ohio
- combined: live=`data/cleaned/draws/Ohio_draws.csv` snap=`sharepacks/2025-06-23/Ohio4/aux/draws/Ohio_draws.csv` n=1000 head=199, 976, 868, 069, 899
- midday: live=`data/cleaned/draws/Ohio_Midday_draws.csv` snap=`sharepacks/2025-06-23/Ohio4/aux/draws/Ohio_Midday_draws.csv` n=1000 head=976, 069, 270, 112, 456
- evening: live=`data/cleaned/draws/Ohio_Evening_draws.csv` snap=`sharepacks/2025-06-23/Ohio4/aux/draws/Ohio_Evening_draws.csv` n=1000 head=199, 868, 899, 412, 754

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=25 streak=1 max=2 last_repeat_gap=44 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=14), P2:0 (gap=21), P3:5 (gap=27)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=38.91687857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 505: score=38.2804 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 525: score=36.16152857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 345: score=35.77533571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 305: score=35.13885714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 535: score=33.96387857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 575: score=33.910135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 595: score=33.82653571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 325: score=33.01998571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 335: score=30.822335714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 066: ds=938 sev=B
- 166: ds=893 sev=B
- 559: ds=887 sev=B
- 668: ds=881 sev=B
- 449: ds=871 sev=B
- 377: ds=861 sev=B
- 146: ds=779 sev=B
- 339: ds=775 sev=B
- 019: ds=758 sev=B
- 888: ds=741 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=124 sev=red
  - 66: ds=86 sev=blue
  - 77: ds=35 sev=purple
  - 44: ds=33 sev=purple
  - 22: ds=24 sev=-
  - 55: ds=11 sev=-
  - 33: ds=10 sev=-
  - 11: ds=7 sev=-
  - 88: ds=2 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 04: ds=52 sev=blue
  - 58: ds=47 sev=blue
  - 29: ds=46 sev=blue
  - 16: ds=38 sev=blue
  - 18: ds=38 sev=blue
  - 08: ds=32 sev=purple
  - 78: ds=32 sev=purple
  - 15: ds=31 sev=purple
  - 17: ds=31 sev=purple
  - 05: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 27:177, 32:140, 35:133, 1:124, 4:108, 28:90, 15:77, 2:70, 16:69, 31:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 27:ds=177 fs=22 fl=2 hz=0.030690537084398974, 32:ds=140 fs=2 fl=0 hz=0.006051437216338881, 35:ds=133 fs=0 fl=1 hz=0.0027100271002710027, 1:ds=124 fs=3 fl=1 hz=0.006702412868632708, 4:ds=108 fs=21 fl=2 hz=0.026047565118912798, 28:ds=90 fs=26 fl=1 hz=0.03085714285714286, 15:ds=77 fs=26 fl=2 hz=0.03181818181818182, 2:ds=70 fs=22 fl=2 hz=0.027809965237543453, 16:ds=69 fs=1 fl=1 hz=0.003640776699029126, 31:ds=53 fs=22 fl=3 hz=0.027964205816554812

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=97 flags=purple
- S2: ds=94 flags=blue+purple
- S5: ds=91 flags=purple
- S20: ds=53 flags=purple
- S3: ds=37 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '3', '4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=9 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=23), P2:3 (gap=13), P3:3 (gap=19)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=38.91687857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 505: score=38.2804 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 525: score=36.16152857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 345: score=35.77533571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 305: score=35.13885714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 535: score=33.96387857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 575: score=33.910135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 595: score=33.82653571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 325: score=33.01998571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 335: score=30.822335714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 669: ds=923 sev=B
- 466: ds=897 sev=B
- 117: ds=896 sev=B
- 029: ds=889 sev=B
- 066: ds=867 sev=B
- 388: ds=847 sev=B
- 556: ds=802 sev=B
- 688: ds=779 sev=B
- 788: ds=761 sev=B
- 222: ds=744 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=83 sev=blue
  - 66: ds=55 sev=purple
  - 33: ds=52 sev=purple
  - 88: ds=48 sev=purple
  - 22: ds=45 sev=purple
  - 99: ds=26 sev=purple
  - 77: ds=17 sev=-
  - 44: ds=16 sev=-
  - 55: ds=5 sev=-
  - 11: ds=3 sev=-
- non_repeating:
  - 78: ds=50 sev=blue
  - 08: ds=44 sev=blue
  - 26: ds=39 sev=blue
  - 04: ds=35 sev=purple
  - 36: ds=30 sev=purple
  - 29: ds=26 sev=purple
  - 16: ds=25 sev=purple
  - 58: ds=23 sev=-
  - 18: ds=22 sev=-
  - 01: ds=19 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:286, 19:234, 32:219, 2:102, 28:94, 27:88, 34:87, 23:69, 35:66, 18:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=286 fs=2 fl=0 hz=0.006382978723404256, 19:ds=234 fs=16 fl=0 hz=0.02309782608695652, 32:ds=219 fs=4 fl=2 hz=0.009510869565217392, 2:ds=102 fs=19 fl=1 hz=0.02242152466367713, 28:ds=94 fs=24 fl=2 hz=0.029478458049886625, 27:ds=88 fs=24 fl=2 hz=0.030842230130486363, 34:ds=87 fs=26 fl=2 hz=0.030701754385964914, 23:ds=69 fs=25 fl=0 hz=0.032552083333333336, 35:ds=66 fs=0 fl=3 hz=0.005333333333333333, 18:ds=55 fs=15 fl=3 hz=0.0192102454642476

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=78 flags=purple
- S24: ds=62 flags=purple
- S25: ds=48 flags=purple
- S2: ds=47 flags=blue+purple
- S5: ds=45 flags=purple
- S8: ds=34 flags=purple

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
- current_index=25 streak=1 max=3 last_repeat_gap=13 last_repeat_index=10

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=18), P2:4 (gap=20), P3:5 (gap=35)
- consensus_notes: P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 7 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 545: score=38.91687857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 505: score=38.2804 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 525: score=36.16152857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 345: score=35.77533571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 305: score=35.13885714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 535: score=33.96387857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 575: score=33.910135714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 595: score=33.82653571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 325: score=33.01998571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 335: score=30.822335714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 446: ds=957 sev=B
- 678: ds=827 sev=B
- 003: ds=826 sev=B
- 357: ds=806 sev=B
- 559: ds=801 sev=B
- 777: ds=778 sev=B
- 166: ds=750 sev=B
- 224: ds=746 sev=B
- 038: ds=727 sev=B
- 335: ds=700 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=90 sev=blue
  - 00: ds=62 sev=purple
  - 77: ds=48 sev=purple
  - 66: ds=43 sev=purple
  - 44: ds=20 sev=-
  - 22: ds=12 sev=-
  - 11: ds=10 sev=-
  - 33: ds=5 sev=-
  - 88: ds=1 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 37: ds=77 sev=red
  - 35: ds=54 sev=blue
  - 39: ds=51 sev=blue
  - 58: ds=50 sev=blue
  - 38: ds=46 sev=blue
  - 56: ds=43 sev=blue
  - 48: ds=41 sev=blue
  - 05: ds=35 sev=purple
  - 69: ds=30 sev=purple
  - 09: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:254, 15:140, 35:134, 3:119, 27:111, 16:95, 5:86, 30:77, 32:70, 1:62

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=254 fs=4 fl=1 hz=0.009646302250803858, 15:ds=140 fs=27 fl=0 hz=0.03214285714285715, 35:ds=134 fs=1 fl=1 hz=0.00423728813559322, 3:ds=119 fs=24 fl=1 hz=0.02937720329024677, 27:ds=111 fs=21 fl=3 hz=0.027777777777777776, 16:ds=95 fs=1 fl=1 hz=0.003886010362694301, 5:ds=86 fs=14 fl=3 hz=0.020383693045563547, 30:ds=77 fs=37 fl=0 hz=0.04138702460850112, 32:ds=70 fs=0 fl=0 hz=0.0011534025374855825, 1:ds=62 fs=3 fl=0 hz=0.006024096385542169

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=74 flags=purple
- S5: ds=57 flags=blue+purple
- S21: ds=52 flags=red+purple
- S2: ds=47 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=3 tags=FLT,RS
  - 023: score=3 tags=FLT,RS
  - 059: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 239: score=3 tags=FLT,RS
  - 347: score=3 tags=FLT,RS
  - 356: score=3 tags=FLT,RS
  - 149: score=2 tags=RS
  - 158: score=2 tags=RS
  - 167: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 029 -> combined:716(B); midday:889(B)
- 066 -> combined:938(B); midday:867(B)
- 166 -> combined:893(B); evening:750(B)
- 224 -> evening:746(B); midday:698(B)
- 449 -> combined:871(B); evening:679(B)
- 559 -> combined:887(B); evening:801(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:124(red); evening:62(purple); midday:83(blue)
- 04 -> combined:52(blue); evening:26(purple); midday:35(purple)
- 05 -> combined:29(purple); evening:35(purple)
- 08 -> combined:32(purple); midday:44(blue)
- 16 -> combined:38(blue); midday:25(purple)
- 29 -> combined:46(blue); midday:26(purple)
- 35 -> combined:27(purple); evening:54(blue)
- 39 -> combined:27(purple); evening:51(blue)
- 49 -> combined:25(purple); evening:25(purple)
- 58 -> combined:47(blue); evening:50(blue)
- 66 -> combined:86(blue); evening:43(purple); midday:55(purple)
- 77 -> combined:35(purple); evening:48(purple)
- 78 -> combined:32(purple); midday:50(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(2.5069214285714287)[R2,XVAR-Cons(CE)], 5(2.4463714285714286)[R3,XVAR-Cons(CE)], 6(1.8474857142857144)[R1,XVAR-Cons(CM)], 8(1.2867142857142857)[R1,Double-Pressure], 9(1.2374285714285713)[R1,Double-Pressure]
- P2: 4(3.541142857142857)[R2,XVAR-Cons(CE)], 0(2.9046642857142855)[R1,XVAR-Cons(CE)], 2(1.7857928571428572)[R3,XVAR-Cons(CM)], 3(1.088142857142857)[R1,Double-Pressure], 7(1.0344)[R2,Double-Pressure]
- P3: 5(8.227271428571427)[R1,XVAR-Cons(CEM)], 1(1.6309428571428572)[R3,XVAR-Cons(CM)], 0(1.5093999999999999)[R2,Mirror-Echo], 3(1.1672857142857143)[R1,Double-Pressure], 7(1.008)[R2,Double-Pressure]
