# Aux Summary — Florida4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/Florida4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Florida
- combined: live=`data/cleaned/draws/Florida_draws.csv` snap=`sharepacks/2026-01-01/Florida4/aux/draws/Florida_draws.csv` n=1000 head=211, 407, 870, 377, 208
- midday: live=`data/cleaned/draws/Florida_Midday_draws.csv` snap=`sharepacks/2026-01-01/Florida4/aux/draws/Florida_Midday_draws.csv` n=1000 head=407, 377, 522, 909, 452
- evening: live=`data/cleaned/draws/Florida_Evening_draws.csv` snap=`sharepacks/2026-01-01/Florida4/aux/draws/Florida_Evening_draws.csv` n=1000 head=211, 870, 208, 003, 985

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=2 last_repeat_gap=27 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=33), P2:6 (gap=26), P3:4 (gap=14)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 767: score=41.77445928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 797: score=41.51738785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 760: score=38.259285714285724 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=38.00221428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 764: score=37.65428571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 763: score=37.64138571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 766: score=37.46428571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 769: score=37.43238571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 794: score=37.397214285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 793: score=37.38431428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 244: ds=999 sev=B
- 369: ds=867 sev=B
- 447: ds=751 sev=B
- 668: ds=741 sev=B
- 388: ds=732 sev=B
- 199: ds=731 sev=B
- 777: ds=723 sev=B
- 335: ds=696 sev=B
- 155: ds=685 sev=B
- 266: ds=670 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=61 sev=purple
  - 44: ds=44 sev=purple
  - 66: ds=39 sev=purple
  - 33: ds=26 sev=purple
  - 55: ds=20 sev=-
  - 99: ds=7 sev=-
  - 00: ds=6 sev=-
  - 22: ds=5 sev=-
  - 77: ds=3 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 27: ds=78 sev=red
  - 57: ds=70 sev=red
  - 39: ds=64 sev=red
  - 26: ds=55 sev=blue
  - 79: ds=49 sev=blue
  - 67: ds=48 sev=blue
  - 38: ds=45 sev=blue
  - 05: ds=43 sev=blue
  - 19: ds=38 sev=blue
  - 29: ds=38 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:465, 26:278, 16:167, 35:137, 31:125, 29:118, 33:93, 5:88, 7:77, 1:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=465 fs=0 fl=0 hz=0.003745318352059925, 26:ds=278 fs=2 fl=0 hz=0.006198347107438016, 16:ds=167 fs=1 fl=1 hz=0.005235602094240838, 35:ds=137 fs=1 fl=1 hz=0.007281553398058252, 31:ds=125 fs=18 fl=1 hz=0.021739130434782608, 29:ds=118 fs=23 fl=0 hz=0.03083109919571046, 33:ds=93 fs=14 fl=2 hz=0.017837235228539576, 5:ds=88 fs=19 fl=2 hz=0.024734982332155476, 7:ds=77 fs=40 fl=1 hz=0.04581005586592179, 1:ds=53 fs=4 fl=5 hz=0.00986842105263158

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S14: ds=46 flags=red+purple
- S16: ds=45 flags=purple
- S2: ds=42 flags=blue+purple
- S5: ds=37 flags=purple
- S23: ds=30 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [5], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '6', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 059: score=3 tags=FLT,RS
  - 068: score=3 tags=FLT,RS
  - 149: score=3 tags=FLT,RS
  - 158: score=3 tags=FLT,RS
  - 167: score=3 tags=FLT,RS
  - 239: score=3 tags=FLT,RS
  - 257: score=3 tags=FLT,RS
  - 356: score=3 tags=FLT,RS
  - 689: score=3 tags=FLT,RS
  - 014: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=2 last_repeat_gap=18 last_repeat_index=20

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=31), P2:9 (gap=24), P3:0 (gap=38)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 767: score=41.77445928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 797: score=41.51738785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 760: score=38.259285714285724 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=38.00221428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 764: score=37.65428571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 763: score=37.64138571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 766: score=37.46428571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 769: score=37.43238571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 794: score=37.397214285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 793: score=37.38431428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=983 sev=B
- 339: ds=870 sev=B
- 228: ds=810 sev=B
- 117: ds=792 sev=B
- 999: ds=782 sev=B
- 455: ds=736 sev=B
- 277: ds=724 sev=B
- 788: ds=697 sev=B
- 167: ds=694 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=81 sev=blue
  - 00: ds=66 sev=purple
  - 11: ds=61 sev=purple
  - 88: ds=30 sev=purple
  - 55: ds=26 sev=purple
  - 66: ds=19 sev=-
  - 33: ds=13 sev=-
  - 99: ds=3 sev=-
  - 22: ds=2 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 15: ds=112 sev=red
  - 39: ds=97 sev=red
  - 19: ds=75 sev=red
  - 29: ds=62 sev=red
  - 18: ds=58 sev=red
  - 57: ds=49 sev=blue
  - 27: ds=40 sev=blue
  - 01: ds=38 sev=blue
  - 78: ds=36 sev=purple
  - 28: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:331, 32:232, 25:136, 16:83, 29:79, 5:76, 35:68, 3:66, 31:62, 14:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=331 fs=2 fl=0 hz=0.006125574272588055, 32:ds=232 fs=2 fl=0 hz=0.006289308176100629, 25:ds=136 fs=20 fl=1 hz=0.02602230483271375, 16:ds=83 fs=0 fl=2 hz=0.004524886877828055, 29:ds=79 fs=22 fl=2 hz=0.027149321266968323, 5:ds=76 fs=20 fl=3 hz=0.024918743228602384, 35:ds=68 fs=2 fl=1 hz=0.005506607929515419, 3:ds=66 fs=27 fl=0 hz=0.02944383860414395, 31:ds=62 fs=22 fl=1 hz=0.02619589977220957, 14:ds=54 fs=54 fl=0 hz=0.057203389830508475

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=66 flags=purple
- S23: ds=56 flags=purple
- S7: ds=48 flags=purple
- S4: ds=43 flags=blue+purple
- S3: ds=38 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '6', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 028: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=2 last_repeat_gap=2 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=45), P2:6 (gap=13), P3:7 (gap=24)
- consensus_notes: P1 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:7 (ds=45)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 767: score=41.77445928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 797: score=41.51738785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 760: score=38.259285714285724 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 790: score=38.00221428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 764: score=37.65428571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 763: score=37.64138571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 766: score=37.46428571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 769: score=37.43238571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 794: score=37.397214285714284 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 793: score=37.38431428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=999 sev=B
- 133: ds=961 sev=B
- 889: ds=920 sev=B
- 189: ds=861 sev=B
- 022: ds=849 sev=B
- 077: ds=814 sev=B
- 448: ds=781 sev=B
- 449: ds=776 sev=B
- 009: ds=771 sev=B
- 366: ds=727 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=102 sev=blue
  - 88: ds=74 sev=blue
  - 66: ds=24 sev=-
  - 44: ds=22 sev=-
  - 33: ds=13 sev=-
  - 55: ds=10 sev=-
  - 99: ds=9 sev=-
  - 22: ds=8 sev=-
  - 00: ds=3 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 35: ds=124 sev=red
  - 25: ds=107 sev=red
  - 79: ds=73 sev=red
  - 49: ds=62 sev=red
  - 38: ds=56 sev=red
  - 47: ds=54 sev=blue
  - 05: ds=45 sev=blue
  - 17: ds=42 sev=blue
  - 23: ds=39 sev=blue
  - 27: ds=39 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:677, 32:366, 26:139, 31:126, 16:103, 10:102, 20:95, 1:90, 33:85, 29:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=677 fs=1 fl=0 hz=0.010101010101010102, 32:ds=366 fs=4 fl=1 hz=0.010273972602739727, 26:ds=139 fs=3 fl=2 hz=0.008130081300813009, 31:ds=126 fs=19 fl=1 hz=0.024154589371980676, 16:ds=103 fs=1 fl=2 hz=0.006042296072507553, 10:ds=102 fs=8 fl=3 hz=0.013793103448275862, 20:ds=95 fs=20 fl=2 hz=0.026537997587454766, 1:ds=90 fs=2 fl=2 hz=0.010498687664041995, 33:ds=85 fs=16 fl=1 hz=0.019362186788154895, 29:ds=59 fs=27 fl=2 hz=0.031115879828326178

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S18: ds=77 flags=red+purple
- S21: ds=49 flags=purple
- S5: ds=40 flags=purple
- S17: ds=31 flags=purple
- S16: ds=30 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '6'], 'pairs': {'remaining_count': 2}}
- top candidates:
  - 014: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 244 -> combined:999(B); evening:711(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:43(blue); evening:45(blue)
- 17 -> combined:31(purple); evening:42(blue)
- 18 -> combined:32(purple); midday:58(red)
- 19 -> combined:38(blue); midday:75(red)
- 26 -> combined:55(blue); evening:30(purple); midday:27(purple)
- 27 -> combined:78(red); evening:39(blue); midday:40(blue)
- 29 -> combined:38(blue); midday:62(red)
- 35 -> combined:29(purple); evening:124(red)
- 38 -> combined:45(blue); evening:56(red)
- 39 -> combined:64(red); evening:32(purple); midday:97(red)
- 44 -> combined:44(purple); midday:81(blue)
- 57 -> combined:70(red); evening:35(purple); midday:49(blue)
- 79 -> combined:49(blue); evening:73(red)
- 88 -> combined:61(purple); evening:74(blue); midday:30(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 7(8.18372142857143)[R1,XVAR-Cons(CEM)], 6(2.7069214285714285)[R2,Mirror-Echo], 8(1.5955714285714284)[R1,Double-Pressure], 5(0.8089999999999999)[R2,Double-Pressure], 1(0.448)[R3,Mirror-Echo]
- P2: 6(6.860564285714286)[R1,XVAR-Cons(CEM)], 9(6.603492857142856)[R2,XVAR-Cons(CEM)], 8(1.0597999999999999)[R2,Double-Pressure], 5(0.9089999999999999)[R2,Double-Pressure], 3(0.29800000000000004)[R3,Swap]
- P3: 0(1.7149999999999999)[R1,Double-Pressure], 7(1.3654285714285714)[R1,Mirror-Echo], 4(1.11)[R1,Double-Pressure], 3(1.0971)[R2,Double-Pressure], 6(0.9199999999999999)[R2,Double-Pressure]
