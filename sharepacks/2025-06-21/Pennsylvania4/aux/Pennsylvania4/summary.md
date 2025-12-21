# Aux Summary — Pennsylvania4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2025-06-21/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=226, 354, 846, 041, 567
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2025-06-21/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=354, 041, 954, 578, 413
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2025-06-21/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=226, 846, 567, 917, 605

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=3 last_repeat_gap=119 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=23), P2:3 (gap=39), P3:2 (gap=25)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=52.3314 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=48.645942857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=45.53247142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=45.106428571428566 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 730: score=41.84701428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=41.42097142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=40.438457142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=39.657585714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 122: score=38.97698571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 782: score=38.3075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 488: ds=872 sev=B
- 012: ds=856 sev=B
- 455: ds=800 sev=B
- 467: ds=730 sev=B
- 059: ds=711 sev=B
- 244: ds=700 sev=B
- 036: ds=699 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=49 sev=purple
  - 77: ds=47 sev=purple
  - 00: ds=42 sev=purple
  - 44: ds=41 sev=purple
  - 11: ds=19 sev=-
  - 88: ds=16 sev=-
  - 66: ds=15 sev=-
  - 33: ds=11 sev=-
  - 99: ds=10 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 15: ds=49 sev=blue
  - 38: ds=48 sev=blue
  - 39: ds=39 sev=blue
  - 03: ds=34 sev=purple
  - 23: ds=33 sev=purple
  - 37: ds=30 sev=purple
  - 07: ds=29 sev=purple
  - 18: ds=27 sev=purple
  - 47: ds=25 sev=purple
  - 27: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 16:253, 26:184, 1:152, 32:147, 4:136, 35:110, 6:82, 33:66, 5:63, 27:61

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 16:ds=253 fs=3 fl=2 hz=0.008241758241758242, 26:ds=184 fs=0 fl=1 hz=0.005649717514124294, 1:ds=152 fs=5 fl=3 hz=0.010126582278481013, 32:ds=147 fs=2 fl=1 hz=0.005738880918220947, 4:ds=136 fs=20 fl=1 hz=0.02530120481927711, 35:ds=110 fs=2 fl=0 hz=0.005917159763313609, 6:ds=82 fs=20 fl=0 hz=0.021953896816684963, 33:ds=66 fs=20 fl=1 hz=0.02260495156081808, 5:ds=63 fs=13 fl=2 hz=0.01714898177920686, 27:ds=61 fs=18 fl=3 hz=0.023127753303964757

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=67 flags=purple
- S7: ds=61 flags=purple
- S19: ds=47 flags=purple
- S22: ds=46 flags=purple

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

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=65 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=15), P2:3 (gap=19), P3:7 (gap=23)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=52.3314 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=48.645942857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=45.53247142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=45.106428571428566 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 730: score=41.84701428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=41.42097142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=40.438457142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=39.657585714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 122: score=38.97698571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 782: score=38.3075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 133: ds=997 sev=B
- 118: ds=833 sev=B
- 559: ds=782 sev=B
- 018: ds=770 sev=B
- 288: ds=769 sev=B
- 255: ds=740 sev=B
- 668: ds=722 sev=B
- 199: ds=670 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=24 sev=-
  - 77: ds=23 sev=-
  - 00: ds=22 sev=-
  - 22: ds=21 sev=-
  - 44: ds=20 sev=-
  - 88: ds=13 sev=-
  - 11: ds=9 sev=-
  - 99: ds=8 sev=-
  - 66: ds=7 sev=-
  - 33: ds=5 sev=-
- non_repeating:
  - 48: ds=66 sev=red
  - 25: ds=65 sev=red
  - 68: ds=49 sev=blue
  - 29: ds=48 sev=blue
  - 69: ds=45 sev=blue
  - 28: ds=44 sev=blue
  - 19: ds=43 sev=blue
  - 17: ds=38 sev=blue
  - 03: ds=37 sev=blue
  - 37: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:596, 26:180, 4:173, 1:165, 6:160, 29:132, 16:126, 25:100, 32:73, 12:64

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=596 fs=6 fl=1 hz=0.01881720430107527, 26:ds=180 fs=1 fl=0 hz=0.0028328611898017, 4:ds=173 fs=18 fl=2 hz=0.026075619295958277, 1:ds=165 fs=2 fl=3 hz=0.00904977375565611, 6:ds=160 fs=16 fl=1 hz=0.0228494623655914, 29:ds=132 fs=23 fl=0 hz=0.030666666666666665, 16:ds=126 fs=2 fl=5 hz=0.008728179551122194, 25:ds=100 fs=20 fl=2 hz=0.024608501118568233, 32:ds=73 fs=6 fl=1 hz=0.008781558726673985, 12:ds=64 fs=44 fl=0 hz=0.04756756756756757

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=87 flags=purple
- S26: ds=79 flags=blue+purple
- S1: ds=78 flags=blue+purple
- S23: ds=74 flags=purple
- S22: ds=61 flags=purple
- S14: ds=35 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 024: score=3 tags=FLT,RS
  - 069: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 168: score=3 tags=FLT,RS
  - 249: score=3 tags=FLT,RS
  - 258: score=3 tags=FLT,RS
  - 267: score=3 tags=FLT,RS
  - 456: score=3 tags=FLT,RS
  - 015: score=2 tags=RS
  - 078: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=3 last_repeat_gap=37 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=28), P2:5 (gap=39), P3:2 (gap=42)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:2 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 132: score=52.3314 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 130: score=48.645942857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 732: score=45.53247142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 182: score=45.106428571428566 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 730: score=41.84701428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 180: score=41.42097142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 137: score=40.438457142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 152: score=39.657585714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 122: score=38.97698571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 782: score=38.3075 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 677: ds=908 sev=B
- 788: ds=870 sev=B
- 557: ds=849 sev=B
- 779: ds=843 sev=B
- 278: ds=789 sev=B
- 444: ds=778 sev=B
- 899: ds=775 sev=B
- 778: ds=758 sev=B
- 009: ds=736 sev=B
- 077: ds=726 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=112 sev=red
  - 55: ds=64 sev=purple
  - 33: ds=42 sev=purple
  - 66: ds=30 sev=purple
  - 44: ds=28 sev=purple
  - 00: ds=21 sev=-
  - 11: ds=14 sev=-
  - 88: ds=8 sev=-
  - 99: ds=5 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 59: ds=64 sev=red
  - 07: ds=56 sev=red
  - 49: ds=55 sev=blue
  - 78: ds=48 sev=blue
  - 23: ds=36 sev=purple
  - 39: ds=33 sev=purple
  - 15: ds=32 sev=purple
  - 89: ds=31 sev=purple
  - 47: ds=28 sev=purple
  - 12: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:422, 3:261, 16:209, 28:149, 26:92, 15:80, 1:76, 17:71, 4:68, 5:64

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=422 fs=0 fl=1 hz=0.004405286343612335, 3:ds=261 fs=12 fl=2 hz=0.020710059171597635, 16:ds=209 fs=4 fl=4 hz=0.011142061281337047, 28:ds=149 fs=15 fl=3 hz=0.02120141342756184, 26:ds=92 fs=2 fl=0 hz=0.005242463958060288, 15:ds=80 fs=35 fl=0 hz=0.042682926829268296, 1:ds=76 fs=8 fl=3 hz=0.013480392156862744, 17:ds=71 fs=24 fl=1 hz=0.02824858757062147, 4:ds=68 fs=28 fl=1 hz=0.03125, 5:ds=64 fs=15 fl=4 hz=0.020496224379719524

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=58 flags=purple
- S7: ds=52 flags=purple
- S9: ds=45 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT
  - 123: score=1 tags=FLT
  - 134: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 059 -> combined:711(B); evening:715(B)
- 255 -> evening:694(B); midday:740(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:34(purple); midday:37(blue)
- 07 -> combined:29(purple); evening:56(red)
- 15 -> combined:49(blue); evening:32(purple)
- 23 -> combined:33(purple); evening:36(purple)
- 37 -> combined:30(purple); midday:29(purple)
- 38 -> combined:48(blue); midday:28(purple)
- 39 -> combined:39(blue); evening:33(purple)
- 44 -> combined:41(purple); evening:28(purple)
- 47 -> combined:25(purple); evening:28(purple)
- 55 -> combined:49(purple); evening:64(purple)
- 77 -> combined:47(purple); evening:112(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.148928571428572)[R1,XVAR-Cons(CEM)], 7(3.85)[R2,XVAR-Cons(CE)], 6(1.1523571428571429)[R1,Mirror-Echo], 0(0.23435714285714285)[R3,Swap], 8(0.23435714285714285)[R3,Swap]
- P2: 3(8.388814285714286)[R1,Mirror-Echo], 8(3.663842857142857)[R2,Mirror-Echo], 5(1.7149999999999999)[R1,Double-Pressure], 2(1.0344)[R2,Double-Pressure], 0(0.2881)[R3,Swap]
- P3: 2(8.293657142857143)[R1,XVAR-Cons(CEM)], 0(5.6082)[R2,XVAR-Cons(CEM)], 7(1.4007142857142856)[R1,Mirror-Echo], 4(0.6551999999999999)[R2,Swap], 9(0.1414285714285714)[R3]
