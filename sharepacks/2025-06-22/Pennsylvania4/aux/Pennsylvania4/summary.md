# Aux Summary — Pennsylvania4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=360, 667, 226, 354, 846
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=667, 354, 041, 954, 578
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2025-06-22/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=360, 226, 846, 567, 917

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=121 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=25), P2:3 (gap=41), P3:2 (gap=27)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=50.46489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=44.73125 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.06999285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.1681 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.680592857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=39.936571428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 134: score=38.55927857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.183078571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.55421428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 782: score=37.336349999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 488: ds=874 sev=B
- 012: ds=858 sev=B
- 455: ds=802 sev=B
- 467: ds=732 sev=B
- 059: ds=713 sev=B
- 244: ds=702 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=51 sev=purple
  - 77: ds=49 sev=purple
  - 00: ds=44 sev=purple
  - 44: ds=43 sev=purple
  - 11: ds=21 sev=-
  - 88: ds=18 sev=-
  - 33: ds=13 sev=-
  - 99: ds=12 sev=-
  - 22: ds=2 sev=-
  - 66: ds=1 sev=-
- non_repeating:
  - 15: ds=51 sev=blue
  - 38: ds=50 sev=blue
  - 39: ds=41 sev=blue
  - 23: ds=35 sev=purple
  - 37: ds=32 sev=purple
  - 07: ds=31 sev=purple
  - 18: ds=29 sev=purple
  - 47: ds=27 sev=purple
  - 27: ds=24 sev=-
  - 08: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:255, 26:186, 1:154, 32:149, 4:138, 35:112, 6:84, 33:68, 5:65, 27:63

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=255 fs=3 fl=2 hz=0.008241758241758242, 26:ds=186 fs=0 fl=1 hz=0.005649717514124294, 1:ds=154 fs=5 fl=3 hz=0.010126582278481013, 32:ds=149 fs=2 fl=1 hz=0.005738880918220947, 4:ds=138 fs=20 fl=1 hz=0.02530120481927711, 35:ds=112 fs=2 fl=0 hz=0.005917159763313609, 6:ds=84 fs=20 fl=0 hz=0.021953896816684963, 33:ds=68 fs=20 fl=1 hz=0.02260495156081808, 5:ds=65 fs=13 fl=2 hz=0.01714898177920686, 27:ds=63 fs=18 fl=3 hz=0.023127753303964757

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=69 flags=purple
- S7: ds=63 flags=purple
- S22: ds=48 flags=purple
- S0: ds=47 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=17 streak=1 max=3 last_repeat_gap=66 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=12), P2:3 (gap=20), P3:2 (gap=13)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=50.46489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=44.73125 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.06999285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.1681 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.680592857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=39.936571428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 134: score=38.55927857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.183078571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.55421428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 782: score=37.336349999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=998 sev=B
- 118: ds=834 sev=B
- 559: ds=783 sev=B
- 018: ds=771 sev=B
- 288: ds=770 sev=B
- 255: ds=741 sev=B
- 668: ds=723 sev=B
- 199: ds=671 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=25 sev=purple
  - 77: ds=24 sev=-
  - 00: ds=23 sev=-
  - 22: ds=22 sev=-
  - 44: ds=21 sev=-
  - 88: ds=14 sev=-
  - 11: ds=10 sev=-
  - 99: ds=9 sev=-
  - 33: ds=6 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 48: ds=67 sev=red
  - 25: ds=66 sev=red
  - 68: ds=50 sev=blue
  - 29: ds=49 sev=blue
  - 69: ds=46 sev=blue
  - 28: ds=45 sev=blue
  - 19: ds=44 sev=blue
  - 17: ds=39 sev=blue
  - 03: ds=38 sev=blue
  - 37: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:597, 26:181, 4:174, 1:166, 6:161, 29:133, 16:127, 25:101, 32:74, 12:65

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=597 fs=6 fl=1 hz=0.01881720430107527, 26:ds=181 fs=1 fl=0 hz=0.0028328611898017, 4:ds=174 fs=18 fl=2 hz=0.026075619295958277, 1:ds=166 fs=2 fl=3 hz=0.00904977375565611, 6:ds=161 fs=16 fl=1 hz=0.0228494623655914, 29:ds=133 fs=23 fl=0 hz=0.030666666666666665, 16:ds=127 fs=2 fl=5 hz=0.008728179551122194, 25:ds=101 fs=20 fl=2 hz=0.024608501118568233, 32:ds=74 fs=6 fl=1 hz=0.008781558726673985, 12:ds=65 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=88 flags=purple
- S26: ds=80 flags=blue+purple
- S1: ds=79 flags=blue+purple
- S23: ds=75 flags=purple
- S22: ds=62 flags=purple
- S14: ds=36 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 024: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 249: score=3 tags=FLT,RS
  - 258: score=3 tags=FLT,RS
  - 267: score=3 tags=FLT,RS
  - 015: score=2 tags=RS
  - 069: score=2 tags=RS
  - 078: score=2 tags=RS
  - 159: score=2 tags=RS
  - 168: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=8 streak=1 max=3 last_repeat_gap=38 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=29), P2:5 (gap=40), P3:2 (gap=43)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=40), P3:2 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=50.46489285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=44.73125 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.06999285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.1681 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.680592857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=39.936571428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 134: score=38.55927857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.183078571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.55421428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian
- 782: score=37.336349999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 677: ds=909 sev=B
- 788: ds=871 sev=B
- 557: ds=850 sev=B
- 779: ds=844 sev=B
- 278: ds=790 sev=B
- 444: ds=779 sev=B
- 899: ds=776 sev=B
- 778: ds=759 sev=B
- 009: ds=737 sev=B
- 077: ds=727 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=113 sev=red
  - 55: ds=65 sev=purple
  - 33: ds=43 sev=purple
  - 66: ds=31 sev=purple
  - 44: ds=29 sev=purple
  - 00: ds=22 sev=-
  - 11: ds=15 sev=-
  - 88: ds=9 sev=-
  - 99: ds=6 sev=-
  - 22: ds=1 sev=-
- non_repeating:
  - 59: ds=65 sev=red
  - 07: ds=57 sev=red
  - 49: ds=56 sev=red
  - 78: ds=49 sev=blue
  - 23: ds=37 sev=blue
  - 39: ds=34 sev=purple
  - 15: ds=33 sev=purple
  - 89: ds=32 sev=purple
  - 47: ds=29 sev=purple
  - 12: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:423, 3:262, 16:210, 28:150, 26:93, 15:81, 1:77, 17:72, 4:69, 5:65

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=423 fs=0 fl=1 hz=0.004405286343612335, 3:ds=262 fs=12 fl=2 hz=0.020710059171597635, 16:ds=210 fs=4 fl=4 hz=0.011142061281337047, 28:ds=150 fs=15 fl=3 hz=0.02120141342756184, 26:ds=93 fs=2 fl=0 hz=0.005242463958060288, 15:ds=81 fs=35 fl=0 hz=0.042682926829268296, 1:ds=77 fs=8 fl=3 hz=0.013480392156862744, 17:ds=72 fs=24 fl=1 hz=0.02824858757062147, 4:ds=69 fs=28 fl=1 hz=0.03125, 5:ds=65 fs=15 fl=4 hz=0.020496224379719524

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=59 flags=purple
- S7: ds=53 flags=purple
- S8: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 059 -> combined:713(B); evening:716(B)
- 255 -> evening:695(B); midday:741(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:31(purple); evening:57(red)
- 15 -> combined:51(blue); evening:33(purple); midday:25(purple)
- 23 -> combined:35(purple); evening:37(blue)
- 37 -> combined:32(purple); midday:30(purple)
- 38 -> combined:50(blue); evening:25(purple); midday:29(purple)
- 39 -> combined:41(blue); evening:34(purple)
- 44 -> combined:43(purple); evening:29(purple)
- 47 -> combined:27(purple); evening:29(purple)
- 55 -> combined:51(purple); evening:65(purple); midday:25(purple)
- 77 -> combined:49(purple); evening:113(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.157500000000001)[R1,XVAR-Cons(CEM)], 7(3.923857142857143)[R2,XVAR-Cons(CE)], 8(0.9299)[R2,Double-Pressure], 0(0.24779285714285712)[R3,Swap], 4(0.15557142857142858)[R3]
- P2: 3(8.62567857142857)[R1,Mirror-Echo], 8(3.7307785714285715)[R2,Mirror-Echo], 5(1.7149999999999999)[R1,Double-Pressure], 2(1.0553)[R2,Double-Pressure], 0(0.30153571428571424)[R3,Swap]
- P3: 2(8.181714285714285)[R1,XVAR-Cons(CEM)], 9(2.3849214285714284)[R2,XVAR-Cons(CM)], 3(1.8974142857142857)[R3,XVAR-Cons(CE)], 4(1.2761)[R2,Double-Pressure], 0(0.8998999999999999)[R2,Double-Pressure]
