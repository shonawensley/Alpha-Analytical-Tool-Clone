# Aux Summary — NorthCarolina4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2025-06-23/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=153, 765, 397, 427, 261
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2025-06-23/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=765, 427, 707, 579, 257
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2025-06-23/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=153, 397, 261, 902, 799

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=7 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=16), P2:4 (gap=17), P3:4 (gap=33)
- consensus_notes: P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 644: score=44.518225 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 646: score=43.00813071428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 844: score=41.464171428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 846: score=39.91052142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 636: score=36.91068071428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 686: score=36.73740928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 634: score=35.614050000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 684: score=35.440778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 834: score=35.36672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.19345 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 666: ds=831 sev=B
- 228: ds=824 sev=B
- 244: ds=798 sev=B
- 004: ds=772 sev=B
- 001: ds=736 sev=B
- 677: ds=697 sev=B
- 377: ds=695 sev=B
- 044: ds=693 sev=B
- 226: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=103 sev=blue
  - 44: ds=57 sev=purple
  - 66: ds=50 sev=purple
  - 11: ds=40 sev=purple
  - 33: ds=38 sev=purple
  - 22: ds=29 sev=purple
  - 55: ds=28 sev=purple
  - 00: ds=10 sev=-
  - 99: ds=8 sev=-
  - 77: ds=5 sev=-
- non_repeating:
  - 89: ds=132 sev=red
  - 46: ds=100 sev=red
  - 36: ds=38 sev=blue
  - 49: ds=35 sev=purple
  - 14: ds=33 sev=purple
  - 23: ds=32 sev=purple
  - 06: ds=26 sev=purple
  - 01: ds=23 sev=-
  - 28: ds=18 sev=-
  - 68: ds=18 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:377, 16:245, 35:201, 29:153, 15:107, 26:94, 2:78, 6:77, 27:61, 25:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=377 fs=0 fl=2 hz=0.0049504950495049506, 16:ds=245 fs=0 fl=1 hz=0.0036900369003690036, 35:ds=201 fs=0 fl=2 hz=0.005154639175257732, 29:ds=153 fs=19 fl=1 hz=0.02442002442002442, 15:ds=107 fs=21 fl=0 hz=0.025059665871121718, 26:ds=94 fs=3 fl=1 hz=0.007109004739336493, 2:ds=78 fs=22 fl=0 hz=0.024017467248908297, 6:ds=77 fs=23 fl=3 hz=0.029213483146067414, 27:ds=61 fs=12 fl=1 hz=0.016587677725118485, 25:ds=57 fs=17 fl=4 hz=0.022364217252396165

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=86 flags=purple
- S2: ds=84 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '8'], 'pairs': {'remaining_count': 2}}
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

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=16 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=20), P2:3 (gap=21), P3:3 (gap=64)
- consensus_notes: P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:3 (ds=64)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 644: score=44.518225 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 646: score=43.00813071428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 844: score=41.464171428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 846: score=39.91052142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 636: score=36.91068071428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 686: score=36.73740928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 634: score=35.614050000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 684: score=35.440778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 834: score=35.36672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.19345 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 344: ds=830 sev=B
- 188: ds=823 sev=B
- 558: ds=780 sev=B
- 115: ds=772 sev=B
- 123: ds=755 sev=B
- 446: ds=732 sev=B
- 335: ds=696 sev=B
- 777: ds=692 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=89 sev=blue
  - 33: ds=64 sev=purple
  - 88: ds=51 sev=purple
  - 00: ds=48 sev=purple
  - 55: ds=41 sev=purple
  - 66: ds=36 sev=purple
  - 44: ds=28 sev=purple
  - 22: ds=14 sev=-
  - 99: ds=9 sev=-
  - 77: ds=2 sev=-
- non_repeating:
  - 89: ds=78 sev=red
  - 46: ds=75 sev=red
  - 28: ds=66 sev=red
  - 26: ds=50 sev=blue
  - 29: ds=42 sev=blue
  - 15: ds=38 sev=blue
  - 36: ds=36 sev=purple
  - 03: ds=32 sev=purple
  - 23: ds=30 sev=purple
  - 37: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:188, 26:185, 1:180, 16:122, 35:100, 33:80, 22:79, 29:76, 20:72, 23:70

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=188 fs=3 fl=2 hz=0.007741935483870969, 26:ds=185 fs=1 fl=0 hz=0.0049382716049382715, 1:ds=180 fs=3 fl=3 hz=0.00857843137254902, 16:ds=122 fs=2 fl=1 hz=0.009174311926605505, 35:ds=100 fs=0 fl=1 hz=0.00487012987012987, 33:ds=80 fs=21 fl=2 hz=0.026744186046511628, 22:ds=79 fs=44 fl=0 hz=0.04851157662624035, 29:ds=76 fs=17 fl=2 hz=0.02132435465768799, 20:ds=72 fs=22 fl=1 hz=0.02481121898597627, 23:ds=70 fs=17 fl=2 hz=0.021300448430493273

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S7: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '3', '8'], 'pairs': {'remaining_count': 0}}
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
  - 028: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=23 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=14), P2:4 (gap=32), P3:4 (gap=20)
- consensus_notes: P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 644: score=44.518225 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 646: score=43.00813071428571 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 844: score=41.464171428571426 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 846: score=39.91052142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 636: score=36.91068071428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 686: score=36.73740928571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 634: score=35.614050000000006 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 684: score=35.440778571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 834: score=35.36672142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 884: score=35.19345 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=986 sev=B
- 668: ds=970 sev=B
- 166: ds=865 sev=B
- 378: ds=864 sev=B
- 666: ds=862 sev=B
- 455: ds=856 sev=B
- 225: ds=826 sev=B
- 279: ds=817 sev=B
- 111: ds=781 sev=B
- 222: ds=780 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=65 sev=purple
  - 88: ds=58 sev=purple
  - 22: ds=26 sev=purple
  - 66: ds=25 sev=purple
  - 11: ds=20 sev=-
  - 33: ds=19 sev=-
  - 55: ds=14 sev=-
  - 77: ds=7 sev=-
  - 00: ds=5 sev=-
  - 99: ds=4 sev=-
- non_repeating:
  - 04: ds=103 sev=red
  - 89: ds=66 sev=red
  - 45: ds=50 sev=blue
  - 46: ds=50 sev=blue
  - 01: ds=42 sev=blue
  - 69: ds=36 sev=purple
  - 59: ds=35 sev=purple
  - 49: ds=32 sev=purple
  - 57: ds=24 sev=-
  - 18: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:634, 35:300, 32:251, 5:126, 14:106, 29:79, 15:68, 34:65, 27:49, 9:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=634 fs=4 fl=1 hz=0.0154320987654321, 35:ds=300 fs=1 fl=3 hz=0.008032128514056224, 32:ds=251 fs=3 fl=2 hz=0.00946372239747634, 5:ds=126 fs=18 fl=1 hz=0.02328288707799767, 14:ds=106 fs=39 fl=0 hz=0.04426787741203178, 29:ds=79 fs=18 fl=2 hz=0.023781212841854936, 15:ds=68 fs=15 fl=2 hz=0.019653179190751446, 34:ds=65 fs=19 fl=0 hz=0.023086269744835963, 27:ds=49 fs=19 fl=4 hz=0.02454642475987193, 9:ds=48 fs=52 fl=0 hz=0.05573419078242229

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=75 flags=purple
- S23: ds=68 flags=purple
- S20: ds=58 flags=purple
- S0: ds=57 flags=blue+purple
- S10: ds=55 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 014: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 666 -> combined:831(B); evening:862(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 06 -> combined:26(purple); midday:25(purple)
- 11 -> combined:40(purple); midday:89(blue)
- 22 -> combined:29(purple); evening:26(purple)
- 23 -> combined:32(purple); midday:30(purple)
- 33 -> combined:38(purple); midday:64(purple)
- 36 -> combined:38(blue); midday:36(purple)
- 44 -> combined:57(purple); evening:65(purple); midday:28(purple)
- 46 -> combined:100(red); evening:50(blue); midday:75(red)
- 49 -> combined:35(purple); evening:32(purple)
- 55 -> combined:28(purple); midday:41(purple)
- 66 -> combined:50(purple); evening:25(purple); midday:36(purple)
- 88 -> combined:103(blue); evening:58(purple); midday:51(purple)
- 89 -> combined:132(red); evening:66(red); midday:78(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(3.0859)[R2,XVAR-Cons(CE)], 8(2.8385714285714285)[R3,XVAR-Cons(CM)], 0(2.700342857142857)[R1,XVAR-Cons(CE)], 5(1.066857142857143)[R1,Mirror-Echo], 1(1.0344)[R2,Double-Pressure]
- P2: 4(7.656914285714286)[R1,XVAR-Cons(CEM)], 3(3.0594642857142857)[R3,Mirror-Echo], 8(2.8861928571428574)[R2,Mirror-Echo], 1(1.1179999999999999)[R2,Double-Pressure], 2(0.21497142857142856)[R3]
- P3: 4(7.968685714285715)[R1,XVAR-Cons(CEM)], 6(6.415035714285714)[R2,XVAR-Cons(CEM)], 3(1.7449999999999999)[R1,Double-Pressure], 8(0.25557142857142856)[R3,Swap], 5(0.13435714285714284)[R3]
