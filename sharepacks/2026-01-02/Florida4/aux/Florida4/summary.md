# Aux Summary — Florida4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/Florida4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Florida
- combined: live=`data/cleaned/draws/Florida_draws.csv` snap=`sharepacks/2026-01-02/Florida4/aux/draws/Florida_draws.csv` n=1000 head=291, 195, 211, 407, 870
- midday: live=`data/cleaned/draws/Florida_Midday_draws.csv` snap=`sharepacks/2026-01-02/Florida4/aux/draws/Florida_Midday_draws.csv` n=1000 head=195, 407, 377, 522, 909
- evening: live=`data/cleaned/draws/Florida_Evening_draws.csv` snap=`sharepacks/2026-01-02/Florida4/aux/draws/Florida_Evening_draws.csv` n=1000 head=291, 211, 870, 208, 003

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=29 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=35), P2:6 (gap=28), P3:4 (gap=16)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 769: score=44.76215714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 767: score=44.07318642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 764: score=40.888014285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 760: score=40.4423 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 763: score=39.8453 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 766: score=39.6913 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 669: score=35.52292857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 789: score=32.23515714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 739: score=32.00044285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 667: score=31.889464285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 369: ds=869 sev=B
- 447: ds=753 sev=B
- 668: ds=743 sev=B
- 388: ds=734 sev=B
- 199: ds=733 sev=B
- 777: ds=725 sev=B
- 335: ds=698 sev=B
- 155: ds=687 sev=B
- 266: ds=672 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=63 sev=purple
  - 44: ds=46 sev=purple
  - 66: ds=41 sev=purple
  - 33: ds=28 sev=purple
  - 55: ds=22 sev=-
  - 99: ds=9 sev=-
  - 00: ds=8 sev=-
  - 22: ds=7 sev=-
  - 77: ds=5 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 27: ds=80 sev=red
  - 57: ds=72 sev=red
  - 39: ds=66 sev=red
  - 26: ds=57 sev=red
  - 79: ds=51 sev=blue
  - 67: ds=50 sev=blue
  - 38: ds=47 sev=blue
  - 05: ds=45 sev=blue
  - 18: ds=34 sev=purple
  - 17: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:467, 26:280, 16:169, 35:139, 31:127, 29:120, 33:95, 5:90, 7:79, 1:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=467 fs=0 fl=0 hz=0.003745318352059925, 26:ds=280 fs=2 fl=0 hz=0.006198347107438016, 16:ds=169 fs=1 fl=1 hz=0.005235602094240838, 35:ds=139 fs=1 fl=1 hz=0.007281553398058252, 31:ds=127 fs=17 fl=1 hz=0.02278481012658228, 29:ds=120 fs=23 fl=0 hz=0.03083109919571046, 33:ds=95 fs=14 fl=2 hz=0.017837235228539576, 5:ds=90 fs=19 fl=2 hz=0.024734982332155476, 7:ds=79 fs=40 fl=1 hz=0.04581005586592179, 1:ds=55 fs=4 fl=5 hz=0.00986842105263158

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S14: ds=48 flags=red+purple
- S16: ds=47 flags=purple
- S2: ds=44 flags=blue+purple
- S5: ds=39 flags=purple
- S23: ds=32 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 023: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 167: score=3 tags=FLT,RS
  - 239: score=3 tags=FLT,RS
  - 347: score=3 tags=FLT,RS
  - 356: score=3 tags=FLT,RS
  - 689: score=3 tags=FLT,RS
  - 014: score=2 tags=RS
  - 059: score=2 tags=RS
  - 149: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=2 last_repeat_gap=19 last_repeat_index=20

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=32), P2:8 (gap=23), P3:0 (gap=39)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 769: score=44.76215714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 767: score=44.07318642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 764: score=40.888014285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 760: score=40.4423 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 763: score=39.8453 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 766: score=39.6913 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 669: score=35.52292857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 789: score=32.23515714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 739: score=32.00044285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 667: score=31.889464285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=984 sev=B
- 339: ds=871 sev=B
- 228: ds=811 sev=B
- 117: ds=793 sev=B
- 999: ds=783 sev=B
- 455: ds=737 sev=B
- 277: ds=725 sev=B
- 788: ds=698 sev=B
- 167: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=82 sev=blue
  - 00: ds=67 sev=purple
  - 11: ds=62 sev=purple
  - 88: ds=31 sev=purple
  - 55: ds=27 sev=purple
  - 66: ds=20 sev=-
  - 33: ds=14 sev=-
  - 99: ds=4 sev=-
  - 22: ds=3 sev=-
  - 77: ds=2 sev=-
- non_repeating:
  - 39: ds=98 sev=red
  - 29: ds=63 sev=red
  - 18: ds=59 sev=red
  - 57: ds=50 sev=blue
  - 27: ds=41 sev=blue
  - 01: ds=39 sev=blue
  - 78: ds=37 sev=blue
  - 28: ds=32 sev=purple
  - 02: ds=30 sev=purple
  - 03: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:332, 32:233, 25:137, 16:84, 29:80, 5:77, 35:69, 3:67, 31:63, 14:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=332 fs=2 fl=0 hz=0.006125574272588055, 32:ds=233 fs=2 fl=0 hz=0.006289308176100629, 25:ds=137 fs=20 fl=1 hz=0.02602230483271375, 16:ds=84 fs=0 fl=2 hz=0.004524886877828055, 29:ds=80 fs=22 fl=2 hz=0.027149321266968323, 5:ds=77 fs=19 fl=3 hz=0.023887079261672092, 35:ds=69 fs=2 fl=1 hz=0.005506607929515419, 3:ds=67 fs=27 fl=0 hz=0.02944383860414395, 31:ds=63 fs=22 fl=1 hz=0.02619589977220957, 14:ds=55 fs=54 fl=0 hz=0.057203389830508475

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=67 flags=purple
- S23: ds=57 flags=purple
- S7: ds=49 flags=purple
- S4: ds=44 flags=blue+purple
- S3: ds=39 flags=purple

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

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=3 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=46), P2:6 (gap=14), P3:7 (gap=25)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:7 (ds=46)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 769: score=44.76215714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 767: score=44.07318642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 764: score=40.888014285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 760: score=40.4423 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 763: score=39.8453 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 766: score=39.6913 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 669: score=35.52292857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 789: score=32.23515714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 739: score=32.00044285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 667: score=31.889464285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=962 sev=B
- 889: ds=921 sev=B
- 189: ds=862 sev=B
- 022: ds=850 sev=B
- 077: ds=815 sev=B
- 448: ds=782 sev=B
- 449: ds=777 sev=B
- 009: ds=772 sev=B
- 366: ds=728 sev=B
- 244: ds=712 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=103 sev=blue
  - 88: ds=75 sev=blue
  - 66: ds=25 sev=purple
  - 44: ds=23 sev=-
  - 33: ds=14 sev=-
  - 55: ds=11 sev=-
  - 99: ds=10 sev=-
  - 22: ds=9 sev=-
  - 00: ds=4 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 35: ds=125 sev=red
  - 25: ds=108 sev=red
  - 79: ds=74 sev=red
  - 49: ds=63 sev=red
  - 38: ds=57 sev=red
  - 47: ds=55 sev=blue
  - 05: ds=46 sev=blue
  - 17: ds=43 sev=blue
  - 23: ds=40 sev=blue
  - 27: ds=40 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:678, 32:367, 26:140, 31:127, 16:104, 10:103, 20:96, 1:91, 33:86, 29:60

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=678 fs=1 fl=0 hz=0.010101010101010102, 32:ds=367 fs=4 fl=1 hz=0.010273972602739727, 26:ds=140 fs=3 fl=2 hz=0.008130081300813009, 31:ds=127 fs=19 fl=1 hz=0.024154589371980676, 16:ds=104 fs=1 fl=2 hz=0.006042296072507553, 10:ds=103 fs=8 fl=3 hz=0.013793103448275862, 20:ds=96 fs=20 fl=2 hz=0.026537997587454766, 1:ds=91 fs=2 fl=2 hz=0.010498687664041995, 33:ds=86 fs=16 fl=1 hz=0.019362186788154895, 29:ds=60 fs=27 fl=2 hz=0.031115879828326178

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S18: ds=78 flags=red+purple
- S21: ds=50 flags=purple
- S5: ds=41 flags=purple
- S17: ds=32 flags=purple
- S16: ds=31 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5', '6'], 'pairs': {'remaining_count': 2}}
- top candidates:
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 045: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- none

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:45(blue); evening:46(blue)
- 17 -> combined:33(purple); evening:43(blue)
- 18 -> combined:34(purple); midday:59(red)
- 23 -> combined:25(purple); evening:40(blue)
- 26 -> combined:57(red); evening:31(purple); midday:28(purple)
- 27 -> combined:80(red); evening:40(blue); midday:41(blue)
- 35 -> combined:31(purple); evening:125(red)
- 38 -> combined:47(blue); evening:57(red)
- 39 -> combined:66(red); evening:33(purple); midday:98(red)
- 44 -> combined:46(purple); midday:82(blue)
- 57 -> combined:72(red); evening:36(purple); midday:50(blue)
- 66 -> combined:41(purple); evening:25(purple)
- 67 -> combined:50(blue); evening:25(purple); midday:25(purple)
- 79 -> combined:51(blue); evening:74(red); midday:25(purple)
- 88 -> combined:63(purple); evening:75(blue); midday:31(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.413585714285714)[R1,XVAR-Cons(CEM)], 6(2.6743571428571427)[R2,XVAR-Cons(CE)], 8(1.6254285714285714)[R1,Double-Pressure], 5(0.8299)[R2,Double-Pressure], 2(0.4227285714285714)[R3,Mirror-Echo]
- P2: 6(7.813714285714286)[R1,XVAR-Cons(CEM)], 8(1.2867142857142857)[R1,Double-Pressure], 3(1.0519999999999998)[R2,Double-Pressure], 5(0.8998999999999999)[R2,Double-Pressure], 1(0.47497142857142854)[R3,Mirror-Echo]
- P3: 9(2.5348571428571427)[R3,Mirror-Echo], 0(1.7149999999999999)[R1,Double-Pressure], 7(1.401392857142857)[R1,Mirror-Echo], 4(1.1607142857142856)[R1,Mirror-Echo], 3(1.1179999999999999)[R2,Double-Pressure]
