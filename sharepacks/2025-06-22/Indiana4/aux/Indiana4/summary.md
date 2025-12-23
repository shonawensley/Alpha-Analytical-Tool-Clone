# Aux Summary — Indiana4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/Indiana4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Indiana
- combined: live=`data/cleaned/draws/Indiana_draws.csv` snap=`sharepacks/2025-06-22/Indiana4/aux/draws/Indiana_draws.csv` n=1000 head=135, 565, 059, 923, 378
- midday: live=`data/cleaned/draws/Indiana_Midday_draws.csv` snap=`sharepacks/2025-06-22/Indiana4/aux/draws/Indiana_Midday_draws.csv` n=1000 head=565, 923, 377, 689, 940
- evening: live=`data/cleaned/draws/Indiana_Evening_draws.csv` snap=`sharepacks/2025-06-22/Indiana4/aux/draws/Indiana_Evening_draws.csv` n=1000 head=135, 059, 378, 641, 188

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=19 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=44), P2:9 (gap=16), P3:4 (gap=32)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 414: score=47.15702 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 494: score=46.63856285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 404: score=44.60017714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 464: score=43.17322 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 424: score=42.48352 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 454: score=40.87607714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 814: score=35.32502857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 416: score=35.04291428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 894: score=34.80657142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 496: score=34.524457142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 337: ds=990 sev=B
- 277: ds=951 sev=B
- 224: ds=917 sev=B
- 177: ds=900 sev=B
- 899: ds=860 sev=B
- 122: ds=820 sev=B
- 002: ds=781 sev=B
- 699: ds=743 sev=B
- 448: ds=740 sev=B
- 000: ds=717 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=72 sev=blue
  - 22: ds=42 sev=purple
  - 66: ds=34 sev=purple
  - 44: ds=32 sev=purple
  - 99: ds=29 sev=purple
  - 00: ds=21 sev=-
  - 11: ds=14 sev=-
  - 88: ds=8 sev=-
  - 77: ds=5 sev=-
  - 55: ds=1 sev=-
- non_repeating:
  - 28: ds=60 sev=red
  - 79: ds=54 sev=blue
  - 12: ds=48 sev=blue
  - 47: ds=39 sev=blue
  - 48: ds=39 sev=blue
  - 06: ds=37 sev=blue
  - 26: ds=34 sev=purple
  - 45: ds=32 sev=purple
  - 03: ds=28 sev=purple
  - 57: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:363, 26:216, 18:201, 6:129, 32:95, 31:94, 25:50, 34:47, 20:46, 22:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=363 fs=1 fl=1 hz=0.010869565217391304, 26:ds=216 fs=1 fl=0 hz=0.004081632653061225, 18:ds=201 fs=27 fl=1 hz=0.03598971722365039, 6:ds=129 fs=23 fl=0 hz=0.027777777777777776, 32:ds=95 fs=1 fl=2 hz=0.009009009009009009, 31:ds=94 fs=22 fl=1 hz=0.027315914489311165, 25:ds=50 fs=22 fl=0 hz=0.023429179978700747, 34:ds=47 fs=18 fl=2 hz=0.02188183807439825, 20:ds=46 fs=23 fl=1 hz=0.0255863539445629, 22:ds=43 fs=49 fl=0 hz=0.05147058823529412

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=71 flags=purple
- S21: ds=53 flags=purple
- S3: ds=48 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 124: score=1 tags=FLT
  - 134: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=74 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=30), P2:5 (gap=15), P3:8 (gap=26)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 414: score=47.15702 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 494: score=46.63856285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 404: score=44.60017714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 464: score=43.17322 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 424: score=42.48352 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 454: score=40.87607714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 814: score=35.32502857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 416: score=35.04291428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 894: score=34.80657142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 496: score=34.524457142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 222: ds=986 sev=B
- 088: ds=936 sev=B
- 038: ds=870 sev=B
- 111: ds=828 sev=B
- 559: ds=827 sev=B
- 466: ds=810 sev=B
- 669: ds=805 sev=B
- 035: ds=803 sev=B
- 288: ds=800 sev=B
- 334: ds=760 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=49 sev=purple
  - 33: ds=40 sev=purple
  - 44: ds=36 sev=purple
  - 88: ds=26 sev=purple
  - 66: ds=17 sev=-
  - 99: ds=14 sev=-
  - 11: ds=12 sev=-
  - 00: ds=10 sev=-
  - 77: ds=2 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 79: ds=161 sev=red
  - 18: ds=67 sev=red
  - 28: ds=48 sev=blue
  - 38: ds=38 sev=blue
  - 12: ds=33 sev=purple
  - 15: ds=33 sev=purple
  - 03: ds=28 sev=purple
  - 58: ds=26 sev=purple
  - 59: ds=22 sev=-
  - 24: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:475, 31:185, 35:181, 28:166, 25:113, 18:100, 5:66, 6:64, 21:54, 19:52

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=475 fs=0 fl=0 hz=0.0020920502092050207, 31:ds=185 fs=19 fl=1 hz=0.02628120893561104, 35:ds=181 fs=3 fl=0 hz=0.00823045267489712, 28:ds=166 fs=17 fl=2 hz=0.02464332036316472, 25:ds=113 fs=28 fl=0 hz=0.03248259860788863, 18:ds=100 fs=31 fl=0 hz=0.03629976580796253, 5:ds=66 fs=16 fl=1 hz=0.018867924528301886, 6:ds=64 fs=20 fl=3 hz=0.025302530253025302, 21:ds=54 fs=45 fl=1 hz=0.052873563218390804, 19:ds=52 fs=25 fl=1 hz=0.028540065861690448

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S20: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=50 flags=purple
- S25: ds=42 flags=purple
- S6: ds=39 flags=purple

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
  - 123: score=1 tags=FLT
  - 124: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=10 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=43), P2:6 (gap=55), P3:7 (gap=23)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:9 (ds=43), P2:6 (ds=55)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 414: score=47.15702 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 494: score=46.63856285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 404: score=44.60017714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 464: score=43.17322 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 424: score=42.48352 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 454: score=40.87607714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 814: score=35.32502857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 416: score=35.04291428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 894: score=34.80657142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 496: score=34.524457142857145 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 356: ds=970 sev=B
- 068: ds=953 sev=B
- 111: ds=893 sev=B
- 022: ds=873 sev=B
- 444: ds=839 sev=B
- 118: ds=765 sev=B
- 556: ds=758 sev=B
- 088: ds=705 sev=B
- 166: ds=702 sev=B
- 555: ds=687 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=65 sev=purple
  - 00: ds=56 sev=purple
  - 33: ds=36 sev=purple
  - 77: ds=23 sev=-
  - 22: ds=21 sev=-
  - 66: ds=17 sev=-
  - 44: ds=16 sev=-
  - 11: ds=7 sev=-
  - 55: ds=5 sev=-
  - 88: ds=4 sev=-
- non_repeating:
  - 06: ds=60 sev=red
  - 68: ds=53 sev=blue
  - 47: ds=47 sev=blue
  - 27: ds=46 sev=blue
  - 07: ds=45 sev=blue
  - 17: ds=43 sev=blue
  - 23: ds=36 sev=purple
  - 49: ds=34 sev=purple
  - 34: ds=33 sev=purple
  - 48: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:250, 18:135, 11:128, 6:120, 32:119, 26:108, 34:85, 4:57, 24:52, 31:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=250 fs=2 fl=0 hz=0.006633499170812604, 18:ds=135 fs=21 fl=1 hz=0.025912838633686687, 11:ds=128 fs=34 fl=0 hz=0.040229885057471264, 6:ds=120 fs=26 fl=2 hz=0.0319634703196347, 32:ds=119 fs=2 fl=1 hz=0.006097560975609756, 26:ds=108 fs=1 fl=1 hz=0.0036855036855036856, 34:ds=85 fs=14 fl=4 hz=0.02127659574468085, 4:ds=57 fs=23 fl=3 hz=0.029246344206974126, 24:ds=52 fs=44 fl=0 hz=0.046858359957401494, 31:ds=47 fs=28 fl=1 hz=0.0306553911205074

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S5: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S4: ds=56 flags=blue+purple
- S19: ds=32 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 123: score=1 tags=FLT
  - 124: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 088 -> evening:705(B); midday:936(B)
- 111 -> evening:893(B); midday:828(B)
- 337 -> combined:990(B); midday:752(B)
- 339 -> evening:679(B); midday:721(B)
- 559 -> evening:674(B); midday:827(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:28(purple); midday:28(purple)
- 06 -> combined:37(blue); evening:60(red)
- 12 -> combined:48(blue); midday:33(purple)
- 22 -> combined:42(purple); midday:49(purple)
- 28 -> combined:60(red); evening:30(purple); midday:48(blue)
- 33 -> combined:72(blue); evening:36(purple); midday:40(purple)
- 44 -> combined:32(purple); midday:36(purple)
- 47 -> combined:39(blue); evening:47(blue)
- 48 -> combined:39(blue); evening:33(purple)
- 57 -> combined:27(purple); evening:27(purple)
- 79 -> combined:54(blue); evening:27(purple); midday:161(red)
- 99 -> combined:29(purple); evening:65(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(7.744885714285715)[R1,XVAR-Cons(CEM)], 8(4.011714285714286)[R2,XVAR-Cons(CM)], 7(2.7181571428571427)[R3,XVAR-Cons(CE)], 9(1.8793571428571427)[R1,Mirror-Echo], 1(0.2612285714285714)[R3,Swap]
- P2: 1(3.2287999999999997)[R2,XVAR-Cons(CM)], 9(2.710342857142857)[R1,XVAR-Cons(CM)], 6(1.7449999999999999)[R1,Double-Pressure], 0(1.671957142857143)[R3,XVAR-Cons(CE)], 2(1.0553)[R2,Double-Pressure]
- P3: 4(7.584514285714285)[R1,XVAR-Cons(CEM)], 6(2.5692285714285714)[R2,XVAR-Cons(CM)], 8(1.3762857142857143)[R1,Double-Pressure], 7(1.2867142857142857)[R1,Double-Pressure], 2(0.28385714285714286)[R3,Swap]
