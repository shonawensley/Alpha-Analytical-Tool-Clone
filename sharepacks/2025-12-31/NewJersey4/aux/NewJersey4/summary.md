# Aux Summary — NewJersey4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/NewJersey4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: New Jersey
- combined: live=`data/cleaned/draws/New_Jersey_draws.csv` snap=`sharepacks/2025-12-31/NewJersey4/aux/draws/New_Jersey_draws.csv` n=1000 head=356, 421, 633, 065, 311
- midday: live=`data/cleaned/draws/New_Jersey_Midday_draws.csv` snap=`sharepacks/2025-12-31/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv` n=1000 head=421, 065, 530, 768, 737
- evening: live=`data/cleaned/draws/New_Jersey_Evening_draws.csv` snap=`sharepacks/2025-12-31/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv` n=1000 head=356, 633, 311, 051, 857

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=18 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=18), P2:8 (gap=34), P3:2 (gap=19)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 282: score=44.74874642857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 182: score=40.70883571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 289: score=37.190442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 989: score=36.71364642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 189: score=36.33465714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 222: score=33.45330357142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 202: score=32.797875 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 212: score=32.769575 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 286: score=31.648300000000003 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 262: score=31.11284642857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 388: ds=984 sev=B
- 005: ds=982 sev=B
- 024: ds=919 sev=B
- 227: ds=885 sev=B
- 266: ds=873 sev=B
- 335: ds=869 sev=B
- 155: ds=855 sev=B
- 277: ds=798 sev=B
- 077: ds=766 sev=B
- 359: ds=674 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=147 sev=red
  - 22: ds=57 sev=purple
  - 88: ds=43 sev=purple
  - 66: ds=34 sev=purple
  - 00: ds=14 sev=-
  - 44: ds=13 sev=-
  - 99: ds=11 sev=-
  - 77: ds=9 sev=-
  - 11: ds=4 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 08: ds=43 sev=blue
  - 19: ds=39 sev=blue
  - 48: ds=37 sev=blue
  - 39: ds=36 sev=purple
  - 26: ds=32 sev=purple
  - 25: ds=31 sev=purple
  - 02: ds=30 sev=purple
  - 27: ds=30 sev=purple
  - 69: ds=29 sev=purple
  - 18: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:798, 35:617, 1:232, 32:148, 28:95, 5:94, 14:88, 17:87, 12:76, 16:71

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=798 fs=2 fl=0 hz=0.016666666666666666, 35:ds=617 fs=1 fl=0 hz=0.008368200836820083, 1:ds=232 fs=1 fl=2 hz=0.006544502617801046, 32:ds=148 fs=2 fl=2 hz=0.005980861244019139, 28:ds=95 fs=20 fl=1 hz=0.024277456647398846, 5:ds=94 fs=12 fl=3 hz=0.016703786191536747, 14:ds=88 fs=35 fl=1 hz=0.041474654377880185, 17:ds=87 fs=22 fl=2 hz=0.02631578947368421, 12:ds=76 fs=38 fl=1 hz=0.044167610419026046, 16:ds=71 fs=1 fl=4 hz=0.007926023778071334

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=56 flags=purple
- S22: ds=50 flags=purple
- S16: ds=42 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['7', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 047: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=16 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=31), P2:8 (gap=21), P3:6 (gap=27)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 282: score=44.74874642857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 182: score=40.70883571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 289: score=37.190442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 989: score=36.71364642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 189: score=36.33465714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 222: score=33.45330357142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 202: score=32.797875 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 212: score=32.769575 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 286: score=31.648300000000003 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 262: score=31.11284642857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 668: ds=973 sev=B
- 778: ds=969 sev=B
- 069: ds=945 sev=B
- 899: ds=918 sev=B
- 455: ds=909 sev=B
- 009: ds=889 sev=B
- 005: ds=887 sev=B
- 099: ds=842 sev=B
- 359: ds=826 sev=B
- 477: ds=817 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=73 sev=blue
  - 11: ds=43 sev=purple
  - 33: ds=31 sev=purple
  - 00: ds=30 sev=purple
  - 22: ds=28 sev=purple
  - 66: ds=27 sev=purple
  - 88: ds=21 sev=-
  - 44: ds=6 sev=-
  - 99: ds=5 sev=-
  - 77: ds=4 sev=-
- non_repeating:
  - 26: ds=75 sev=red
  - 36: ds=53 sev=blue
  - 17: ds=43 sev=blue
  - 39: ds=38 sev=blue
  - 02: ds=25 sev=purple
  - 07: ds=25 sev=purple
  - 27: ds=24 sev=-
  - 01: ds=23 sev=-
  - 45: ds=22 sev=-
  - 08: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:442, 1:364, 35:308, 32:229, 18:93, 5:73, 14:56, 12:49, 28:47, 17:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=442 fs=1 fl=0 hz=0.007246376811594203, 1:ds=364 fs=4 fl=0 hz=0.009554140127388535, 35:ds=308 fs=3 fl=0 hz=0.008032128514056224, 32:ds=229 fs=0 fl=0 hz=0.003552397868561279, 18:ds=93 fs=15 fl=4 hz=0.021205357142857144, 5:ds=73 fs=12 fl=4 hz=0.017429193899782137, 14:ds=56 fs=37 fl=0 hz=0.039784946236559135, 12:ds=49 fs=41 fl=1 hz=0.04530744336569579, 28:ds=47 fs=20 fl=2 hz=0.023231256599788808, 17:ds=43 fs=26 fl=1 hz=0.029411764705882353

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=96 flags=purple
- S25: ds=86 flags=blue+purple
- S3: ds=78 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 019: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 059: score=1 tags=FLT
  - 069: score=1 tags=FLT
  - 079: score=1 tags=FLT
  - 089: score=1 tags=FLT
  - 129: score=1 tags=FLT
  - 139: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=6 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=32), P2:2 (gap=32), P3:9 (gap=20)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 4 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 282: score=44.74874642857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 182: score=40.70883571428571 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 289: score=37.190442857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 989: score=36.71364642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 189: score=36.33465714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 222: score=33.45330357142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 202: score=32.797875 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 212: score=32.769575 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 286: score=31.648300000000003 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 262: score=31.11284642857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 035: ds=950 sev=B
- 499: ds=941 sev=B
- 339: ds=927 sev=B
- 556: ds=859 sev=B
- 000: ds=845 sev=B
- 335: ds=825 sev=B
- 569: ds=815 sev=B
- 558: ds=805 sev=B
- 088: ds=802 sev=B
- 022: ds=744 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=108 sev=red
  - 55: ds=101 sev=blue
  - 77: ds=83 sev=blue
  - 44: ds=40 sev=purple
  - 22: ds=32 sev=purple
  - 99: ds=20 sev=-
  - 66: ds=17 sev=-
  - 00: ds=7 sev=-
  - 11: ds=2 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 59: ds=62 sev=red
  - 03: ds=51 sev=blue
  - 08: ds=46 sev=blue
  - 47: ds=38 sev=blue
  - 18: ds=37 sev=blue
  - 25: ds=32 sev=purple
  - 48: ds=29 sev=purple
  - 89: ds=28 sev=purple
  - 34: ds=27 sev=purple
  - 14: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:421, 26:399, 13:123, 1:116, 27:104, 4:101, 16:98, 17:95, 19:84, 28:76

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=421 fs=2 fl=1 hz=0.007692307692307693, 26:ds=399 fs=1 fl=0 hz=0.0056179775280898875, 13:ds=123 fs=16 fl=2 hz=0.021686746987951807, 1:ds=116 fs=1 fl=2 hz=0.008213552361396304, 27:ds=104 fs=7 fl=2 hz=0.011325028312570783, 4:ds=101 fs=14 fl=1 hz=0.01839080459770115, 16:ds=98 fs=2 fl=2 hz=0.012658227848101266, 17:ds=95 fs=10 fl=2 hz=0.014051522248243558, 19:ds=84 fs=18 fl=2 hz=0.022172949002217293, 28:ds=76 fs=26 fl=0 hz=0.028291621327529923

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=56 flags=blue+purple
- S23: ds=48 flags=purple
- S17: ds=44 flags=purple
- S21: ds=30 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
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
- 005 -> combined:982(B); midday:887(B)
- 335 -> combined:869(B); evening:825(B)
- 359 -> combined:674(B); midday:826(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 02 -> combined:30(purple); midday:25(purple)
- 08 -> combined:43(blue); evening:46(blue)
- 18 -> combined:27(purple); evening:37(blue)
- 22 -> combined:57(purple); evening:32(purple); midday:28(purple)
- 25 -> combined:31(purple); evening:32(purple)
- 26 -> combined:32(purple); midday:75(red)
- 39 -> combined:36(purple); midday:38(blue)
- 48 -> combined:37(blue); evening:29(purple)
- 55 -> combined:147(red); evening:101(blue); midday:73(blue)
- 66 -> combined:34(purple); midday:27(purple)
- 88 -> combined:43(purple); evening:108(red)
- 89 -> combined:25(purple); evening:28(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(4.191285714285714)[R1,XVAR-Cons(CM)], 1(3.3354999999999997)[R2,XVAR-Cons(CM)], 9(2.038464285714286)[R3,XVAR-Cons(CE)], 5(1.6554285714285715)[R1,Double-Pressure], 4(1.2960785714285714)[R2,Mirror-Echo]
- P2: 8(7.950871428571428)[R1,XVAR-Cons(CEM)], 2(1.6554285714285715)[R1,Double-Pressure], 0(1.0)[R2,Double-Pressure], 1(0.9717)[R2,Double-Pressure], 6(0.31497142857142857)[R3,Swap]
- P3: 2(6.422464285714286)[R1,XVAR-Cons(CEM)], 9(3.548285714285714)[R2,Mirror-Echo], 6(1.5061428571428572)[R1,Double-Pressure], 3(0.9417)[R2,Double-Pressure], 4(0.33971428571428575)[R3,Mirror-Echo]
