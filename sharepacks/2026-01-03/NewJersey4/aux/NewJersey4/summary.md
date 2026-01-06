# Aux Summary — NewJersey4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/NewJersey4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: New Jersey
- combined: live=`data/cleaned/draws/New_Jersey_draws.csv` snap=`sharepacks/2026-01-03/NewJersey4/aux/draws/New_Jersey_draws.csv` n=1000 head=331, 633, 504, 770, 418
- midday: live=`data/cleaned/draws/New_Jersey_Midday_draws.csv` snap=`sharepacks/2026-01-03/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv` n=1000 head=633, 770, 366, 421, 065
- evening: live=`data/cleaned/draws/New_Jersey_Evening_draws.csv` snap=`sharepacks/2026-01-03/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv` n=1000 head=331, 504, 418, 356, 633

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=2 max=3 last_repeat_gap=1 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=24), P2:8 (gap=40), P3:2 (gap=25)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 282: score=55.10890571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 289: score=50.461307142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 989: score=45.724780714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 292: score=44.15119142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 222: score=43.71933428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=43.19587142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 189: score=43.04235 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 212: score=43.00873428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 242: score=42.470620000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 262: score=41.29961285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 388: ds=990 sev=B
- 005: ds=988 sev=B
- 024: ds=925 sev=B
- 227: ds=891 sev=B
- 266: ds=879 sev=B
- 335: ds=875 sev=B
- 155: ds=861 sev=B
- 277: ds=804 sev=B
- 359: ds=680 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=153 sev=red
  - 22: ds=63 sev=purple
  - 88: ds=49 sev=purple
  - 00: ds=20 sev=-
  - 44: ds=19 sev=-
  - 99: ds=17 sev=-
  - 11: ds=10 sev=-
  - 66: ds=5 sev=-
  - 77: ds=3 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 08: ds=49 sev=blue
  - 19: ds=45 sev=blue
  - 39: ds=42 sev=blue
  - 26: ds=38 sev=blue
  - 25: ds=37 sev=blue
  - 02: ds=36 sev=purple
  - 27: ds=36 sev=purple
  - 69: ds=35 sev=purple
  - 89: ds=31 sev=purple
  - 17: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:804, 35:623, 1:238, 32:154, 28:101, 14:94, 17:93, 12:82, 16:77, 19:61

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=804 fs=2 fl=0 hz=0.016666666666666666, 35:ds=623 fs=1 fl=0 hz=0.008368200836820083, 1:ds=238 fs=0 fl=2 hz=0.005333333333333333, 32:ds=154 fs=2 fl=2 hz=0.005980861244019139, 28:ds=101 fs=20 fl=1 hz=0.024277456647398846, 14:ds=94 fs=35 fl=1 hz=0.041474654377880185, 17:ds=93 fs=20 fl=2 hz=0.02564102564102564, 12:ds=82 fs=38 fl=1 hz=0.044167610419026046, 16:ds=77 fs=1 fl=4 hz=0.007926023778071334, 19:ds=61 fs=26 fl=1 hz=0.030439684329199548

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=62 flags=purple
- S22: ds=56 flags=purple
- S16: ds=48 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=3 last_repeat_gap=19 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=34), P2:8 (gap=24), P3:2 (gap=12)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 282: score=55.10890571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 289: score=50.461307142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 989: score=45.724780714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 292: score=44.15119142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 222: score=43.71933428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=43.19587142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 189: score=43.04235 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 212: score=43.00873428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 242: score=42.470620000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 262: score=41.29961285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 668: ds=976 sev=B
- 778: ds=972 sev=B
- 069: ds=948 sev=B
- 899: ds=921 sev=B
- 455: ds=912 sev=B
- 009: ds=892 sev=B
- 005: ds=890 sev=B
- 099: ds=845 sev=B
- 359: ds=829 sev=B
- 477: ds=820 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=76 sev=blue
  - 11: ds=46 sev=purple
  - 00: ds=33 sev=purple
  - 22: ds=31 sev=purple
  - 88: ds=24 sev=-
  - 44: ds=9 sev=-
  - 99: ds=8 sev=-
  - 66: ds=2 sev=-
  - 77: ds=1 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 26: ds=78 sev=red
  - 17: ds=46 sev=blue
  - 39: ds=41 sev=blue
  - 02: ds=28 sev=purple
  - 27: ds=27 sev=purple
  - 01: ds=26 sev=purple
  - 45: ds=25 sev=purple
  - 08: ds=24 sev=-
  - 19: ds=22 sev=-
  - 48: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:445, 1:367, 35:311, 32:232, 5:76, 14:59, 12:52, 28:50, 17:46, 24:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=445 fs=1 fl=0 hz=0.007246376811594203, 1:ds=367 fs=4 fl=0 hz=0.009554140127388535, 35:ds=311 fs=3 fl=0 hz=0.008032128514056224, 32:ds=232 fs=0 fl=0 hz=0.003552397868561279, 5:ds=76 fs=12 fl=4 hz=0.017429193899782137, 14:ds=59 fs=37 fl=0 hz=0.039784946236559135, 12:ds=52 fs=41 fl=1 hz=0.04530744336569579, 28:ds=50 fs=20 fl=2 hz=0.023231256599788808, 17:ds=46 fs=26 fl=1 hz=0.029411764705882353, 24:ds=45 fs=59 fl=0 hz=0.06184486373165618

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=99 flags=purple
- S25: ds=89 flags=blue+purple
- S3: ds=81 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=3 last_repeat_gap=9 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=28), P2:2 (gap=35), P3:9 (gap=23)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 282: score=55.10890571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 289: score=50.461307142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 989: score=45.724780714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 292: score=44.15119142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 222: score=43.71933428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 182: score=43.19587142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 189: score=43.04235 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 212: score=43.00873428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 242: score=42.470620000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 262: score=41.29961285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 035: ds=953 sev=B
- 499: ds=944 sev=B
- 339: ds=930 sev=B
- 556: ds=862 sev=B
- 000: ds=848 sev=B
- 335: ds=828 sev=B
- 569: ds=818 sev=B
- 558: ds=808 sev=B
- 088: ds=805 sev=B
- 022: ds=747 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=111 sev=red
  - 55: ds=104 sev=blue
  - 77: ds=86 sev=blue
  - 44: ds=43 sev=purple
  - 22: ds=35 sev=purple
  - 99: ds=23 sev=-
  - 66: ds=20 sev=-
  - 00: ds=10 sev=-
  - 11: ds=5 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 59: ds=65 sev=red
  - 03: ds=54 sev=blue
  - 08: ds=49 sev=blue
  - 47: ds=41 sev=blue
  - 25: ds=35 sev=purple
  - 89: ds=31 sev=purple
  - 34: ds=30 sev=purple
  - 12: ds=26 sev=purple
  - 09: ds=25 sev=purple
  - 19: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:424, 26:402, 13:126, 1:119, 27:107, 4:104, 16:101, 17:98, 19:87, 28:79

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=424 fs=2 fl=1 hz=0.007692307692307693, 26:ds=402 fs=1 fl=0 hz=0.0056179775280898875, 13:ds=126 fs=16 fl=2 hz=0.021686746987951807, 1:ds=119 fs=1 fl=2 hz=0.008213552361396304, 27:ds=107 fs=7 fl=2 hz=0.011325028312570783, 4:ds=104 fs=14 fl=1 hz=0.01839080459770115, 16:ds=101 fs=2 fl=2 hz=0.012658227848101266, 17:ds=98 fs=10 fl=2 hz=0.014051522248243558, 19:ds=87 fs=18 fl=2 hz=0.022172949002217293, 28:ds=79 fs=26 fl=0 hz=0.028291621327529923

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=59 flags=blue+purple
- S23: ds=51 flags=purple
- S17: ds=47 flags=purple
- S21: ds=33 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '7', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 005 -> combined:988(B); midday:890(B)
- 335 -> combined:875(B); evening:828(B)
- 359 -> combined:680(B); midday:829(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 02 -> combined:36(purple); midday:28(purple)
- 08 -> combined:49(blue); evening:49(blue)
- 17 -> combined:30(purple); midday:46(blue)
- 19 -> combined:45(blue); evening:25(purple)
- 22 -> combined:63(purple); evening:35(purple); midday:31(purple)
- 25 -> combined:37(blue); evening:35(purple)
- 26 -> combined:38(blue); midday:78(red)
- 27 -> combined:36(purple); midday:27(purple)
- 39 -> combined:42(blue); midday:41(blue)
- 55 -> combined:153(red); evening:104(blue); midday:76(blue)
- 88 -> combined:49(purple); evening:111(red)
- 89 -> combined:31(purple); evening:31(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(7.449157142857143)[R1,XVAR-Cons(CEM)], 1(3.5302)[R2,XVAR-Cons(CM)], 9(3.0764285714285715)[R3,XVAR-Cons(CE)], 7(1.1539857142857142)[R2,Mirror-Echo], 8(0.30153571428571424)[R3,Swap]
- P2: 8(8.13457142857143)[R1,XVAR-Cons(CEM)], 2(1.7449999999999999)[R1,Double-Pressure], 9(1.1768571428571428)[R2,Mirror-Echo], 1(1.0344)[R2,Double-Pressure], 4(0.4962857142857143)[R3,Mirror-Echo]
- P3: 2(7.5311)[R1,Mirror-Echo], 9(7.377578571428572)[R2,XVAR-Cons(CEM)], 7(0.6251428571428572)[R3,Mirror-Echo], 5(0.32840714285714284)[R3,Swap], 4(0.32542142857142853)[R3,Mirror-Echo]
