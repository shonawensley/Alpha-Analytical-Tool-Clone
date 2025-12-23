# Aux Summary — Indiana4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/Indiana4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Indiana
- combined: live=`data/cleaned/draws/Indiana_draws.csv` snap=`sharepacks/2025-06-23/Indiana4/aux/draws/Indiana_draws.csv` n=1000 head=702, 174, 135, 565, 059
- midday: live=`data/cleaned/draws/Indiana_Midday_draws.csv` snap=`sharepacks/2025-06-23/Indiana4/aux/draws/Indiana_Midday_draws.csv` n=1000 head=174, 565, 923, 377, 689
- evening: live=`data/cleaned/draws/Indiana_Evening_draws.csv` snap=`sharepacks/2025-06-23/Indiana4/aux/draws/Indiana_Evening_draws.csv` n=1000 head=702, 135, 059, 378, 641

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=10 streak=1 max=3 last_repeat_gap=21 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=46), P2:9 (gap=18), P3:6 (gap=16)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 496: score=42.7033 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 896: score=40.23950714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 491: score=40.20115714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 494: score=39.52661714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 416: score=37.949442857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 891: score=37.737364285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 898: score=37.248782142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 498: score=37.1346 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 497: score=36.94502857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 490: score=36.54045714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 337: ds=992 sev=B
- 277: ds=953 sev=B
- 224: ds=919 sev=B
- 177: ds=902 sev=B
- 899: ds=862 sev=B
- 122: ds=822 sev=B
- 002: ds=783 sev=B
- 699: ds=745 sev=B
- 448: ds=742 sev=B
- 000: ds=719 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=74 sev=blue
  - 22: ds=44 sev=purple
  - 66: ds=36 sev=purple
  - 44: ds=34 sev=purple
  - 99: ds=31 sev=purple
  - 00: ds=23 sev=-
  - 11: ds=16 sev=-
  - 88: ds=10 sev=-
  - 77: ds=7 sev=-
  - 55: ds=3 sev=-
- non_repeating:
  - 28: ds=62 sev=red
  - 79: ds=56 sev=red
  - 12: ds=50 sev=blue
  - 48: ds=41 sev=blue
  - 06: ds=39 sev=blue
  - 26: ds=36 sev=purple
  - 45: ds=34 sev=purple
  - 03: ds=30 sev=purple
  - 57: ds=29 sev=purple
  - 36: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:365, 26:218, 18:203, 6:131, 32:97, 31:96, 25:52, 34:49, 20:48, 28:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=365 fs=1 fl=1 hz=0.010869565217391304, 26:ds=218 fs=1 fl=0 hz=0.004081632653061225, 18:ds=203 fs=27 fl=1 hz=0.03598971722365039, 6:ds=131 fs=23 fl=0 hz=0.027777777777777776, 32:ds=97 fs=1 fl=2 hz=0.009009009009009009, 31:ds=96 fs=22 fl=1 hz=0.027315914489311165, 25:ds=52 fs=22 fl=0 hz=0.023429179978700747, 34:ds=49 fs=18 fl=2 hz=0.02188183807439825, 20:ds=48 fs=23 fl=1 hz=0.0255863539445629, 28:ds=44 fs=27 fl=2 hz=0.03125

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=73 flags=purple
- S21: ds=55 flags=purple
- S3: ds=50 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=2 tags=FLT,MIR
  - 058: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 168: score=2 tags=FLT,MIR
  - 238: score=2 tags=FLT,MIR
  - 278: score=2 tags=FLT,MIR
  - 348: score=2 tags=FLT,MIR
  - 358: score=2 tags=FLT,MIR
  - 368: score=2 tags=FLT,MIR
  - 378: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=75 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=31), P2:5 (gap=16), P3:8 (gap=27)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 496: score=42.7033 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 896: score=40.23950714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 491: score=40.20115714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 494: score=39.52661714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 416: score=37.949442857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 891: score=37.737364285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 898: score=37.248782142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 498: score=37.1346 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 497: score=36.94502857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 490: score=36.54045714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 222: ds=987 sev=B
- 088: ds=937 sev=B
- 038: ds=871 sev=B
- 111: ds=829 sev=B
- 559: ds=828 sev=B
- 466: ds=811 sev=B
- 669: ds=806 sev=B
- 035: ds=804 sev=B
- 288: ds=801 sev=B
- 334: ds=761 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=50 sev=purple
  - 33: ds=41 sev=purple
  - 44: ds=37 sev=purple
  - 88: ds=27 sev=purple
  - 66: ds=18 sev=-
  - 99: ds=15 sev=-
  - 11: ds=13 sev=-
  - 00: ds=11 sev=-
  - 77: ds=3 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 79: ds=162 sev=red
  - 18: ds=68 sev=red
  - 28: ds=49 sev=blue
  - 38: ds=39 sev=blue
  - 12: ds=34 sev=purple
  - 15: ds=34 sev=purple
  - 03: ds=29 sev=purple
  - 58: ds=27 sev=purple
  - 59: ds=23 sev=-
  - 24: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:476, 31:186, 35:182, 28:167, 25:114, 18:101, 5:67, 6:65, 21:55, 19:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=476 fs=0 fl=0 hz=0.0020920502092050207, 31:ds=186 fs=19 fl=1 hz=0.02628120893561104, 35:ds=182 fs=3 fl=0 hz=0.00823045267489712, 28:ds=167 fs=17 fl=2 hz=0.02464332036316472, 25:ds=114 fs=28 fl=0 hz=0.03248259860788863, 18:ds=101 fs=31 fl=0 hz=0.03629976580796253, 5:ds=67 fs=16 fl=1 hz=0.018867924528301886, 6:ds=65 fs=20 fl=3 hz=0.025302530253025302, 21:ds=55 fs=45 fl=1 hz=0.052873563218390804, 19:ds=53 fs=25 fl=1 hz=0.028540065861690448

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S20: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=51 flags=purple
- S25: ds=43 flags=purple
- S6: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
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
- current_index=10 streak=1 max=3 last_repeat_gap=11 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=44), P2:6 (gap=56), P3:7 (gap=24)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:9 (ds=44), P2:6 (ds=56)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 496: score=42.7033 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 896: score=40.23950714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 491: score=40.20115714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 494: score=39.52661714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 416: score=37.949442857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 891: score=37.737364285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 898: score=37.248782142857145 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 498: score=37.1346 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 497: score=36.94502857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 490: score=36.54045714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 356: ds=971 sev=B
- 068: ds=954 sev=B
- 111: ds=894 sev=B
- 022: ds=874 sev=B
- 444: ds=840 sev=B
- 118: ds=766 sev=B
- 556: ds=759 sev=B
- 088: ds=706 sev=B
- 166: ds=703 sev=B
- 555: ds=688 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=66 sev=purple
  - 00: ds=57 sev=purple
  - 33: ds=37 sev=purple
  - 77: ds=24 sev=-
  - 22: ds=22 sev=-
  - 66: ds=18 sev=-
  - 44: ds=17 sev=-
  - 11: ds=8 sev=-
  - 55: ds=6 sev=-
  - 88: ds=5 sev=-
- non_repeating:
  - 06: ds=61 sev=red
  - 68: ds=54 sev=blue
  - 47: ds=48 sev=blue
  - 17: ds=44 sev=blue
  - 23: ds=37 sev=blue
  - 49: ds=35 sev=purple
  - 34: ds=34 sev=purple
  - 48: ds=34 sev=purple
  - 28: ds=31 sev=purple
  - 57: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:251, 18:136, 11:129, 6:121, 32:120, 26:109, 34:86, 4:58, 24:53, 31:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=251 fs=2 fl=0 hz=0.006633499170812604, 18:ds=136 fs=21 fl=1 hz=0.025912838633686687, 11:ds=129 fs=34 fl=0 hz=0.040229885057471264, 6:ds=121 fs=26 fl=2 hz=0.0319634703196347, 32:ds=120 fs=2 fl=1 hz=0.006097560975609756, 26:ds=109 fs=1 fl=1 hz=0.0036855036855036856, 34:ds=86 fs=14 fl=4 hz=0.02127659574468085, 4:ds=58 fs=23 fl=3 hz=0.029246344206974126, 24:ds=53 fs=44 fl=0 hz=0.046858359957401494, 31:ds=48 fs=28 fl=1 hz=0.0306553911205074

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S5: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S4: ds=57 flags=blue+purple
- S19: ds=33 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=MIR
  - 016: score=1 tags=MIR
  - 025: score=1 tags=MIR
  - 027: score=1 tags=MIR
  - 035: score=1 tags=MIR
  - 038: score=1 tags=MIR
  - 045: score=1 tags=MIR
  - 049: score=1 tags=MIR
  - 056: score=1 tags=MIR
  - 057: score=1 tags=MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 088 -> evening:706(B); midday:937(B)
- 111 -> evening:894(B); midday:829(B)
- 337 -> combined:992(B); midday:753(B)
- 339 -> evening:680(B); midday:722(B)
- 559 -> evening:675(B); midday:828(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:30(purple); midday:29(purple)
- 06 -> combined:39(blue); evening:61(red)
- 12 -> combined:50(blue); evening:25(purple); midday:34(purple)
- 22 -> combined:44(purple); midday:50(purple)
- 28 -> combined:62(red); evening:31(purple); midday:49(blue)
- 33 -> combined:74(blue); evening:37(purple); midday:41(purple)
- 34 -> combined:25(purple); evening:34(purple)
- 44 -> combined:34(purple); midday:37(purple)
- 48 -> combined:41(blue); evening:34(purple)
- 57 -> combined:29(purple); evening:28(purple)
- 79 -> combined:56(red); evening:28(purple); midday:162(red)
- 99 -> combined:31(purple); evening:66(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(8.550899999999999)[R1,XVAR-Cons(CEM)], 8(7.087107142857143)[R2,XVAR-Cons(CEM)], 9(1.9634999999999998)[R1,Mirror-Echo], 2(0.28385714285714286)[R3,Swap], 0(0.12092142857142855)[R3]
- P2: 9(5.577557142857143)[R1,XVAR-Cons(CEM)], 1(3.3236999999999997)[R2,XVAR-Cons(CM)], 6(1.7449999999999999)[R1,Double-Pressure], 5(1.1477142857142857)[R1,Double-Pressure], 2(1.0761999999999998)[R2,Double-Pressure]
- P3: 6(3.5748428571428574)[R1,Mirror-Echo], 1(2.0727)[R3,Mirror-Echo], 8(1.5061428571428572)[R1,Double-Pressure], 7(1.3165714285714285)[R1,Double-Pressure], 4(1.0252999999999999)[R2,Double-Pressure]
