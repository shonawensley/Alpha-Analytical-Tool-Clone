# Aux Summary — Connecticut4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2025-06-22/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=155, 950, 763, 913, 201
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2025-06-22/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=950, 913, 620, 221, 894
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2025-06-22/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=155, 763, 201, 070, 059

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=5 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=14), P2:4 (gap=19), P3:7 (gap=24)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 347: score=43.869635357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 547: score=39.40745714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=37.74296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 337: score=37.73652857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 387: score=37.736171428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 537: score=35.73560714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 587: score=35.73525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 737: score=34.07111428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 787: score=34.07075714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 346: score=33.982150000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=938 sev=B
- 111: ds=922 sev=B
- 145: ds=897 sev=B
- 448: ds=839 sev=B
- 004: ds=830 sev=B
- 223: ds=811 sev=B
- 099: ds=802 sev=B
- 001: ds=785 sev=B
- 127: ds=784 sev=B
- 466: ds=737 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=165 sev=red
  - 88: ds=31 sev=purple
  - 44: ds=30 sev=purple
  - 99: ds=23 sev=-
  - 11: ds=16 sev=-
  - 66: ds=13 sev=-
  - 77: ds=10 sev=-
  - 22: ds=7 sev=-
  - 00: ds=6 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 14: ds=87 sev=red
  - 03: ds=45 sev=blue
  - 56: ds=41 sev=blue
  - 04: ds=40 sev=blue
  - 47: ds=37 sev=blue
  - 68: ds=29 sev=purple
  - 27: ds=28 sev=purple
  - 57: ds=27 sev=purple
  - 17: ds=24 sev=-
  - 79: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 13:170, 4:83, 23:74, 8:68, 14:63, 10:47, 15:43, 6:41, 9:40, 30:37

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 13:ds=170 fs=16 fl=2 hz=0.022140221402214024, 4:ds=83 fs=25 fl=2 hz=0.029900332225913623, 23:ds=74 fs=17 fl=2 hz=0.021372328458942633, 8:ds=68 fs=43 fl=0 hz=0.04658721560130011, 14:ds=63 fs=31 fl=0 hz=0.033879781420765025, 10:ds=47 fs=17 fl=1 hz=0.022641509433962266, 15:ds=43 fs=17 fl=3 hz=0.02107481559536354, 6:ds=41 fs=31 fl=0 hz=0.03311965811965812, 9:ds=40 fs=35 fl=1 hz=0.03761755485893417, 30:ds=37 fs=55 fl=0 hz=0.05789473684210526

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=88 flags=red+purple
- S4: ds=68 flags=purple
- S12: ds=59 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 189: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 378: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 468: score=3 tags=FLT,RS
  - 027: score=2 tags=RS
  - 036: score=2 tags=RS
  - 126: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=3 last_repeat_gap=32 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=26), P2:0 (gap=26), P3:7 (gap=13)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 347: score=43.869635357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 547: score=39.40745714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=37.74296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 337: score=37.73652857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 387: score=37.736171428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 537: score=35.73560714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 587: score=35.73525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 737: score=34.07111428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 787: score=34.07075714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 346: score=33.982150000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=892 sev=B
- 337: ds=855 sev=B
- 889: ds=825 sev=B
- 234: ds=776 sev=B
- 225: ds=752 sev=B
- 077: ds=733 sev=B
- 009: ds=726 sev=B
- 279: ds=699 sev=B
- 117: ds=685 sev=B
- 128: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=82 sev=blue
  - 11: ds=73 sev=blue
  - 00: ds=41 sev=purple
  - 44: ds=38 sev=purple
  - 77: ds=24 sev=-
  - 88: ds=15 sev=-
  - 55: ds=12 sev=-
  - 99: ds=11 sev=-
  - 66: ds=6 sev=-
  - 22: ds=3 sev=-
- non_repeating:
  - 18: ds=91 sev=red
  - 69: ds=68 sev=red
  - 14: ds=43 sev=blue
  - 04: ds=35 sev=purple
  - 45: ds=31 sev=purple
  - 58: ds=31 sev=purple
  - 67: ds=27 sev=purple
  - 01: ds=26 sev=purple
  - 28: ds=25 sev=purple
  - 29: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:143, 13:124, 19:105, 23:91, 17:73, 2:66, 8:58, 27:50, 31:47, 12:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=143 fs=2 fl=0 hz=0.006006006006006006, 13:ds=124 fs=16 fl=1 hz=0.021013597033374538, 19:ds=105 fs=21 fl=1 hz=0.026284348864994027, 23:ds=91 fs=22 fl=1 hz=0.02561247216035635, 17:ds=73 fs=32 fl=2 hz=0.037158469945355196, 2:ds=66 fs=22 fl=1 hz=0.026713124274099886, 8:ds=58 fs=53 fl=0 hz=0.05644302449414271, 27:ds=50 fs=16 fl=3 hz=0.020452099031216364, 31:ds=47 fs=20 fl=3 hz=0.024390243902439025, 12:ds=42 fs=50 fl=0 hz=0.052576235541535225

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=93 flags=purple
- S6: ds=66 flags=red+purple
- S9: ds=58 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [7], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=3 tags=MIR,RS
  - 025: score=3 tags=MIR,RS
  - 079: score=3 tags=FLT,RS
  - 169: score=3 tags=MIR,RS
  - 178: score=3 tags=FLT,RS
  - 349: score=3 tags=MIR,RS
  - 358: score=3 tags=MIR,RS
  - 367: score=3 tags=FLT,RS
  - 457: score=3 tags=FLT,RS
  - 027: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=3 last_repeat_gap=24 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=18), P2:3 (gap=37), P3:6 (gap=13)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 347: score=43.869635357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 547: score=39.40745714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 747: score=37.74296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 337: score=37.73652857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 387: score=37.736171428571424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 537: score=35.73560714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 587: score=35.73525 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 737: score=34.07111428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 787: score=34.07075714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 346: score=33.982150000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 255: ds=934 sev=B
- 034: ds=911 sev=B
- 228: ds=889 sev=B
- 088: ds=887 sev=B
- 223: ds=848 sev=B
- 666: ds=836 sev=B
- 225: ds=811 sev=B
- 678: ds=712 sev=B
- 668: ds=709 sev=B
- 399: ds=708 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=85 sev=blue
  - 88: ds=50 sev=purple
  - 99: ds=16 sev=-
  - 44: ds=15 sev=-
  - 66: ds=13 sev=-
  - 11: ds=8 sev=-
  - 22: ds=6 sev=-
  - 77: ds=5 sev=-
  - 00: ds=3 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 35: ds=89 sev=red
  - 14: ds=78 sev=red
  - 56: ds=73 sev=red
  - 16: ds=44 sev=blue
  - 08: ds=36 sev=purple
  - 03: ds=34 sev=purple
  - 57: ds=32 sev=purple
  - 39: ds=31 sev=purple
  - 34: ds=30 sev=purple
  - 47: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 20:224, 15:145, 32:131, 16:118, 34:94, 13:85, 4:56, 6:54, 33:50, 10:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 20:ds=224 fs=18 fl=2 hz=0.0258732212160414, 15:ds=145 fs=14 fl=1 hz=0.01873536299765808, 32:ds=131 fs=2 fl=0 hz=0.004120879120879121, 16:ds=118 fs=2 fl=1 hz=0.005961251862891207, 34:ds=94 fs=20 fl=2 hz=0.025, 13:ds=85 fs=23 fl=3 hz=0.028540065861690448, 4:ds=56 fs=22 fl=1 hz=0.024918743228602384, 6:ds=54 fs=16 fl=1 hz=0.0196078431372549, 33:ds=50 fs=29 fl=0 hz=0.03176341730558598, 10:ds=42 fs=20 fl=3 hz=0.02561247216035635

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=94 flags=red+purple
- S8: ds=92 flags=red+purple
- S24: ds=71 flags=purple
- S20: ds=70 flags=purple
- S6: ds=58 flags=purple
- S2: ds=54 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '8'], 'pairs': {'remaining_count': 0}}
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
- 044 -> combined:697(B); evening:704(B)
- 145 -> combined:897(B); evening:673(B)
- 223 -> combined:811(B); evening:848(B)
- 225 -> evening:811(B); midday:752(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:45(blue); evening:34(purple)
- 04 -> combined:40(blue); midday:35(purple)
- 14 -> combined:87(red); evening:78(red); midday:43(blue)
- 33 -> combined:165(red); evening:85(blue); midday:82(blue)
- 44 -> combined:30(purple); midday:38(purple)
- 47 -> combined:37(blue); evening:30(purple)
- 56 -> combined:41(blue); evening:73(red)
- 57 -> combined:27(purple); evening:32(purple)
- 88 -> combined:31(purple); evening:50(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 3(3.585585714285714)[R2,XVAR-Cons(CE)], 5(2.5846642857142856)[R1,XVAR-Cons(CM)], 4(1.8571071428571428)[R3,XVAR-Cons(CE)], 1(1.4762857142857142)[R1,Double-Pressure], 8(1.3989285714285713)[R1,Mirror-Echo]
- P2: 4(5.6524214285714285)[R1,XVAR-Cons(CEM)], 3(3.4805714285714284)[R3,Mirror-Echo], 8(3.4802142857142857)[R2,Mirror-Echo], 0(1.4462857142857144)[R1,Double-Pressure], 1(1.2643)[R2,Double-Pressure]
- P3: 7(7.170371428571428)[R1,Mirror-Echo], 6(3.244142857142857)[R2,XVAR-Cons(CE)], 9(0.8998999999999999)[R2,Double-Pressure], 2(0.5125714285714286)[R3,Mirror-Echo], 4(0.24779285714285712)[R3,Swap]
