# Aux Summary — NorthCarolina4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/NorthCarolina4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: North Carolina
- combined: live=`data/cleaned/draws/North_Carolina_draws.csv` snap=`sharepacks/2025-06-22/NorthCarolina4/aux/draws/North_Carolina_draws.csv` n=1000 head=397, 427, 261, 707, 902
- midday: live=`data/cleaned/draws/North_Carolina_Midday_draws.csv` snap=`sharepacks/2025-06-22/NorthCarolina4/aux/draws/North_Carolina_Midday_draws.csv` n=1000 head=427, 707, 579, 257, 718
- evening: live=`data/cleaned/draws/North_Carolina_Evening_draws.csv` snap=`sharepacks/2025-06-22/NorthCarolina4/aux/draws/North_Carolina_Evening_draws.csv` n=1000 head=397, 261, 902, 799, 800

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=3 last_repeat_gap=5 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=31), P2:4 (gap=15), P3:4 (gap=31)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 144: score=52.50541821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 146: score=50.908791071428574 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 143: score=50.72161214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 134: score=46.494567857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 136: score=44.89794071428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 133: score=44.71076178571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 644: score=42.7754575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.788539285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 646: score=41.48266714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 186: score=40.191912142857134 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 666: ds=829 sev=B
- 228: ds=822 sev=B
- 244: ds=796 sev=B
- 004: ds=770 sev=B
- 001: ds=734 sev=B
- 677: ds=695 sev=B
- 377: ds=693 sev=B
- 044: ds=691 sev=B
- 226: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=101 sev=blue
  - 44: ds=55 sev=purple
  - 66: ds=48 sev=purple
  - 11: ds=38 sev=purple
  - 33: ds=36 sev=purple
  - 22: ds=27 sev=purple
  - 55: ds=26 sev=purple
  - 00: ds=8 sev=-
  - 99: ds=6 sev=-
  - 77: ds=3 sev=-
- non_repeating:
  - 89: ds=130 sev=red
  - 46: ds=98 sev=red
  - 15: ds=75 sev=red
  - 13: ds=41 sev=blue
  - 36: ds=36 sev=purple
  - 49: ds=33 sev=purple
  - 14: ds=31 sev=purple
  - 23: ds=30 sev=purple
  - 67: ds=28 sev=purple
  - 06: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:375, 16:243, 35:199, 29:151, 15:105, 26:92, 2:76, 6:75, 27:59, 25:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=375 fs=0 fl=2 hz=0.0049504950495049506, 16:ds=243 fs=0 fl=1 hz=0.0036900369003690036, 35:ds=199 fs=0 fl=2 hz=0.005154639175257732, 29:ds=151 fs=19 fl=1 hz=0.02442002442002442, 15:ds=105 fs=21 fl=0 hz=0.025059665871121718, 26:ds=92 fs=3 fl=1 hz=0.007109004739336493, 2:ds=76 fs=22 fl=0 hz=0.024017467248908297, 6:ds=75 fs=23 fl=3 hz=0.029213483146067414, 27:ds=59 fs=12 fl=1 hz=0.016587677725118485, 25:ds=55 fs=17 fl=4 hz=0.022364217252396165

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=84 flags=purple
- S2: ds=82 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '8'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 015: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=2 last_repeat_gap=15 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=19), P2:3 (gap=20), P3:3 (gap=63)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:3 (ds=63)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 144: score=52.50541821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 146: score=50.908791071428574 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 143: score=50.72161214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 134: score=46.494567857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 136: score=44.89794071428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 133: score=44.71076178571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 644: score=42.7754575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.788539285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 646: score=41.48266714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 186: score=40.191912142857134 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 344: ds=829 sev=B
- 188: ds=822 sev=B
- 558: ds=779 sev=B
- 115: ds=771 sev=B
- 123: ds=754 sev=B
- 446: ds=731 sev=B
- 335: ds=695 sev=B
- 777: ds=691 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 11: ds=88 sev=blue
  - 33: ds=63 sev=purple
  - 88: ds=50 sev=purple
  - 00: ds=47 sev=purple
  - 55: ds=40 sev=purple
  - 66: ds=35 sev=purple
  - 44: ds=27 sev=purple
  - 22: ds=13 sev=-
  - 99: ds=8 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 89: ds=77 sev=red
  - 46: ds=74 sev=red
  - 28: ds=65 sev=red
  - 26: ds=49 sev=blue
  - 29: ds=41 sev=blue
  - 15: ds=37 sev=blue
  - 36: ds=35 sev=purple
  - 67: ds=32 sev=purple
  - 03: ds=31 sev=purple
  - 23: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:187, 26:184, 1:179, 16:121, 35:99, 33:79, 22:78, 29:75, 20:71, 23:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=187 fs=3 fl=2 hz=0.007741935483870969, 26:ds=184 fs=1 fl=0 hz=0.0049382716049382715, 1:ds=179 fs=3 fl=3 hz=0.00857843137254902, 16:ds=121 fs=2 fl=1 hz=0.009174311926605505, 35:ds=99 fs=0 fl=1 hz=0.00487012987012987, 33:ds=79 fs=21 fl=2 hz=0.026744186046511628, 22:ds=78 fs=44 fl=0 hz=0.04851157662624035, 29:ds=75 fs=17 fl=2 hz=0.02132435465768799, 20:ds=71 fs=22 fl=1 hz=0.02481121898597627, 23:ds=69 fs=17 fl=2 hz=0.021300448430493273

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
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 0}}
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
- current_index=30 streak=1 max=3 last_repeat_gap=22 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=16), P2:4 (gap=31), P3:4 (gap=19)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 8 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 144: score=52.50541821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 146: score=50.908791071428574 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 143: score=50.72161214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 134: score=46.494567857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 136: score=44.89794071428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 133: score=44.71076178571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 644: score=42.7754575 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.788539285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 646: score=41.48266714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 186: score=40.191912142857134 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=985 sev=B
- 668: ds=969 sev=B
- 166: ds=864 sev=B
- 378: ds=863 sev=B
- 666: ds=861 sev=B
- 455: ds=855 sev=B
- 225: ds=825 sev=B
- 279: ds=816 sev=B
- 111: ds=780 sev=B
- 222: ds=779 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=64 sev=purple
  - 88: ds=57 sev=purple
  - 22: ds=25 sev=purple
  - 66: ds=24 sev=-
  - 11: ds=19 sev=-
  - 33: ds=18 sev=-
  - 55: ds=13 sev=-
  - 77: ds=6 sev=-
  - 00: ds=4 sev=-
  - 99: ds=3 sev=-
- non_repeating:
  - 04: ds=102 sev=red
  - 89: ds=65 sev=red
  - 45: ds=49 sev=blue
  - 46: ds=49 sev=blue
  - 15: ds=42 sev=blue
  - 01: ds=41 sev=blue
  - 13: ds=37 sev=blue
  - 69: ds=35 sev=purple
  - 59: ds=34 sev=purple
  - 35: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:633, 35:299, 32:250, 5:125, 14:105, 29:78, 15:67, 34:64, 27:48, 9:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=633 fs=4 fl=1 hz=0.0154320987654321, 35:ds=299 fs=1 fl=3 hz=0.008032128514056224, 32:ds=250 fs=3 fl=2 hz=0.00946372239747634, 5:ds=125 fs=18 fl=1 hz=0.02328288707799767, 14:ds=105 fs=39 fl=0 hz=0.04426787741203178, 29:ds=78 fs=18 fl=2 hz=0.023781212841854936, 15:ds=67 fs=15 fl=2 hz=0.019653179190751446, 34:ds=64 fs=19 fl=0 hz=0.023086269744835963, 27:ds=48 fs=19 fl=4 hz=0.02454642475987193, 9:ds=47 fs=52 fl=0 hz=0.05573419078242229

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=74 flags=purple
- S23: ds=67 flags=purple
- S20: ds=57 flags=purple
- S0: ds=56 flags=blue+purple
- S10: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 666 -> combined:829(B); evening:861(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 11 -> combined:38(purple); midday:88(blue)
- 13 -> combined:41(blue); evening:37(blue)
- 15 -> combined:75(red); evening:42(blue); midday:37(blue)
- 22 -> combined:27(purple); evening:25(purple)
- 23 -> combined:30(purple); midday:29(purple)
- 33 -> combined:36(purple); midday:63(purple)
- 36 -> combined:36(purple); midday:35(purple)
- 44 -> combined:55(purple); evening:64(purple); midday:27(purple)
- 46 -> combined:98(red); evening:49(blue); midday:74(red)
- 49 -> combined:33(purple); evening:31(purple)
- 55 -> combined:26(purple); midday:40(purple)
- 66 -> combined:48(purple); midday:35(purple)
- 67 -> combined:28(purple); midday:32(purple)
- 88 -> combined:101(blue); evening:57(purple); midday:50(purple)
- 89 -> combined:130(red); evening:65(red); midday:77(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.867285714285714)[R1,Mirror-Echo], 6(2.4499285714285715)[R3,Mirror-Echo], 8(1.2672857142857143)[R1,Double-Pressure], 0(0.9079999999999999)[R2,Double-Pressure], 5(0.8716999999999999)[R2,Double-Pressure]
- P2: 4(6.89105)[R1,XVAR-Cons(CEM)], 3(2.9685714285714284)[R3,Mirror-Echo], 1(1.0971)[R2,Double-Pressure], 6(1.0971)[R2,Double-Pressure], 8(1.0502857142857143)[R2,Mirror-Echo]
- P3: 4(7.855071428571429)[R1,XVAR-Cons(CEM)], 6(6.4667)[R2,XVAR-Cons(CEM)], 3(6.303935714285714)[R3,XVAR-Cons(CEM)]
