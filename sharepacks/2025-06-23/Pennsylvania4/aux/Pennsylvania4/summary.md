# Aux Summary — Pennsylvania4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2025-06-23/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=570, 398, 360, 667, 226
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2025-06-23/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=398, 667, 354, 041, 954
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2025-06-23/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=570, 360, 226, 846, 567

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=3 last_repeat_gap=123 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=27), P2:3 (gap=43), P3:2 (gap=29)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=54.38529857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 732: score=44.97468571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.34325714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.31601428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.912792857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=40.151430714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 102: score=39.43022857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 134: score=38.70065714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.42445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.76054285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 488: ds=876 sev=B
- 012: ds=860 sev=B
- 455: ds=804 sev=B
- 467: ds=734 sev=B
- 059: ds=715 sev=B
- 244: ds=704 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=53 sev=purple
  - 77: ds=51 sev=purple
  - 00: ds=46 sev=purple
  - 44: ds=45 sev=purple
  - 11: ds=23 sev=-
  - 88: ds=20 sev=-
  - 33: ds=15 sev=-
  - 99: ds=14 sev=-
  - 22: ds=4 sev=-
  - 66: ds=3 sev=-
- non_repeating:
  - 15: ds=53 sev=blue
  - 23: ds=37 sev=blue
  - 37: ds=34 sev=purple
  - 18: ds=31 sev=purple
  - 47: ds=29 sev=purple
  - 27: ds=26 sev=purple
  - 08: ds=25 sev=purple
  - 02: ds=24 sev=-
  - 09: ds=24 sev=-
  - 29: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:257, 26:188, 1:156, 32:151, 4:140, 35:114, 6:86, 5:67, 27:65, 34:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=257 fs=3 fl=2 hz=0.008241758241758242, 26:ds=188 fs=0 fl=1 hz=0.005649717514124294, 1:ds=156 fs=5 fl=3 hz=0.010126582278481013, 32:ds=151 fs=2 fl=1 hz=0.005738880918220947, 4:ds=140 fs=20 fl=1 hz=0.02530120481927711, 35:ds=114 fs=2 fl=0 hz=0.005917159763313609, 6:ds=86 fs=20 fl=0 hz=0.021953896816684963, 5:ds=67 fs=12 fl=2 hz=0.016181229773462785, 27:ds=65 fs=18 fl=3 hz=0.023127753303964757, 34:ds=43 fs=14 fl=4 hz=0.019251336898395723

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=71 flags=purple
- S7: ds=65 flags=purple
- S22: ds=50 flags=purple
- S0: ds=49 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=33 streak=1 max=3 last_repeat_gap=67 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=13), P2:3 (gap=21), P3:2 (gap=14)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=54.38529857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 732: score=44.97468571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.34325714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.31601428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.912792857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=40.151430714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 102: score=39.43022857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 134: score=38.70065714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.42445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.76054285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=999 sev=B
- 118: ds=835 sev=B
- 559: ds=784 sev=B
- 018: ds=772 sev=B
- 288: ds=771 sev=B
- 255: ds=742 sev=B
- 668: ds=724 sev=B
- 199: ds=672 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=26 sev=purple
  - 77: ds=25 sev=purple
  - 00: ds=24 sev=-
  - 22: ds=23 sev=-
  - 44: ds=22 sev=-
  - 88: ds=15 sev=-
  - 11: ds=11 sev=-
  - 99: ds=10 sev=-
  - 33: ds=7 sev=-
  - 66: ds=1 sev=-
- non_repeating:
  - 48: ds=68 sev=red
  - 25: ds=67 sev=red
  - 68: ds=51 sev=blue
  - 29: ds=50 sev=blue
  - 69: ds=47 sev=blue
  - 28: ds=46 sev=blue
  - 19: ds=45 sev=blue
  - 17: ds=40 sev=blue
  - 03: ds=39 sev=blue
  - 37: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:598, 26:182, 4:175, 1:167, 6:162, 29:134, 16:128, 25:102, 32:75, 12:66

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=598 fs=6 fl=1 hz=0.01881720430107527, 26:ds=182 fs=1 fl=0 hz=0.0028328611898017, 4:ds=175 fs=18 fl=2 hz=0.026075619295958277, 1:ds=167 fs=2 fl=3 hz=0.00904977375565611, 6:ds=162 fs=16 fl=1 hz=0.0228494623655914, 29:ds=134 fs=23 fl=0 hz=0.030666666666666665, 16:ds=128 fs=2 fl=5 hz=0.008728179551122194, 25:ds=102 fs=20 fl=2 hz=0.024608501118568233, 32:ds=75 fs=6 fl=1 hz=0.008781558726673985, 12:ds=66 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=89 flags=red+purple
- S26: ds=81 flags=blue+purple
- S1: ds=80 flags=blue+purple
- S23: ds=76 flags=purple
- S22: ds=63 flags=purple
- S14: ds=37 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 249: score=4 tags=FLT,MIR,RS
  - 267: score=4 tags=FLT,MIR,RS
  - 015: score=3 tags=MIR,RS
  - 024: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 168: score=3 tags=MIR,RS
  - 258: score=3 tags=FLT,RS
  - 348: score=3 tags=MIR,RS
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=3 streak=1 max=3 last_repeat_gap=39 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=30), P2:5 (gap=41), P3:2 (gap=44)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P2 mirror cluster around digit 5 (Mirror-Echo(CM)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 8 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=41), P3:2 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=54.38529857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 732: score=44.97468571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=43.34325714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 139: score=42.31601428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 133: score=40.912792857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 232: score=40.151430714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 102: score=39.43022857142857 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 134: score=38.70065714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=38.42445714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=37.76054285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Swap src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 677: ds=910 sev=B
- 788: ds=872 sev=B
- 557: ds=851 sev=B
- 779: ds=845 sev=B
- 278: ds=791 sev=B
- 444: ds=780 sev=B
- 899: ds=777 sev=B
- 778: ds=760 sev=B
- 009: ds=738 sev=B
- 077: ds=728 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=114 sev=red
  - 55: ds=66 sev=purple
  - 33: ds=44 sev=purple
  - 66: ds=32 sev=purple
  - 44: ds=30 sev=purple
  - 00: ds=23 sev=-
  - 11: ds=16 sev=-
  - 88: ds=10 sev=-
  - 99: ds=7 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 59: ds=66 sev=red
  - 49: ds=57 sev=red
  - 78: ds=50 sev=blue
  - 23: ds=38 sev=blue
  - 39: ds=35 sev=purple
  - 15: ds=34 sev=purple
  - 89: ds=33 sev=purple
  - 47: ds=30 sev=purple
  - 12: ds=29 sev=purple
  - 04: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:424, 16:211, 28:151, 26:94, 15:82, 1:78, 17:73, 4:70, 5:66, 30:64

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=424 fs=0 fl=1 hz=0.004405286343612335, 16:ds=211 fs=4 fl=4 hz=0.011142061281337047, 28:ds=151 fs=14 fl=3 hz=0.020118343195266272, 26:ds=94 fs=2 fl=0 hz=0.005242463958060288, 15:ds=82 fs=35 fl=0 hz=0.042682926829268296, 1:ds=78 fs=8 fl=3 hz=0.013480392156862744, 17:ds=73 fs=24 fl=1 hz=0.02824858757062147, 4:ds=70 fs=28 fl=1 hz=0.03125, 5:ds=66 fs=15 fl=4 hz=0.020496224379719524, 30:ds=64 fs=39 fl=0 hz=0.04314159292035399

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=60 flags=purple
- S7: ds=54 flags=purple
- S8: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 059: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR
  - 146: score=2 tags=FLT,MIR
  - 149: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 059 -> combined:715(B); evening:717(B)
- 255 -> evening:696(B); midday:742(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 15 -> combined:53(blue); evening:34(purple); midday:26(purple)
- 23 -> combined:37(blue); evening:38(blue)
- 37 -> combined:34(purple); midday:31(purple)
- 44 -> combined:45(purple); evening:30(purple)
- 47 -> combined:29(purple); evening:30(purple)
- 55 -> combined:53(purple); evening:66(purple); midday:26(purple)
- 77 -> combined:51(purple); evening:114(red); midday:25(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.271114285714286)[R1,XVAR-Cons(CEM)], 7(3.9977142857142858)[R2,XVAR-Cons(CE)], 8(0.9508)[R2,Double-Pressure], 0(0.2612285714285714)[R3,Swap], 4(0.18385714285714286)[R3]
- P2: 3(8.702542857142857)[R1,Mirror-Echo], 8(3.797714285714286)[R2,Mirror-Echo], 0(1.8846857142857143)[R3,XVAR-Cons(CM)], 5(1.7149999999999999)[R1,Double-Pressure], 2(1.0761999999999998)[R2,Double-Pressure]
- P3: 2(8.274428571428572)[R1,XVAR-Cons(CEM)], 9(2.342357142857143)[R2,XVAR-Cons(CM)], 3(1.9391357142857144)[R3,XVAR-Cons(CE)], 4(1.2269999999999999)[R2,Double-Pressure], 0(0.9508)[R2,Double-Pressure]
