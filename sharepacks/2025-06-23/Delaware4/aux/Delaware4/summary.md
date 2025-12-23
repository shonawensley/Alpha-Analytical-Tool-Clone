# Aux Summary — Delaware4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/Delaware4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Delaware
- combined: live=`data/cleaned/draws/Delaware_draws.csv` snap=`sharepacks/2025-06-23/Delaware4/aux/draws/Delaware_draws.csv` n=1000 head=127, 979, 989, 756, 527
- midday: live=`data/cleaned/draws/Delaware_Midday_draws.csv` snap=`sharepacks/2025-06-23/Delaware4/aux/draws/Delaware_Midday_draws.csv` n=1000 head=979, 756, 772, 489, 937
- evening: live=`data/cleaned/draws/Delaware_Evening_draws.csv` snap=`sharepacks/2025-06-23/Delaware4/aux/draws/Delaware_Evening_draws.csv` n=1000 head=127, 989, 527, 471, 702

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=20 streak=1 max=3 last_repeat_gap=15 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=37), P2:4 (gap=31), P3:4 (gap=23)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 845: score=46.709601428571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 844: score=43.64353571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 345: score=42.6153 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 344: score=42.380921428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 645: score=40.502471428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 644: score=40.26809285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=39.75801 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 895: score=37.23052142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 848: score=37.19250642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 894: score=36.99614285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 455: ds=907 sev=B
- 228: ds=871 sev=B
- 355: ds=867 sev=B
- 144: ds=831 sev=B
- 599: ds=819 sev=B
- 009: ds=800 sev=B
- 055: ds=789 sev=B
- 668: ds=757 sev=B
- 189: ds=751 sev=B
- 368: ds=714 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=117 sev=red
  - 88: ds=56 sev=purple
  - 66: ds=42 sev=purple
  - 22: ds=27 sev=purple
  - 11: ds=24 sev=-
  - 44: ds=23 sev=-
  - 33: ds=19 sev=-
  - 00: ds=11 sev=-
  - 77: ds=5 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 35: ds=69 sev=red
  - 04: ds=58 sev=red
  - 09: ds=58 sev=red
  - 69: ds=55 sev=blue
  - 36: ds=47 sev=blue
  - 68: ds=46 sev=blue
  - 03: ds=45 sev=blue
  - 28: ds=41 sev=blue
  - 29: ds=38 sev=blue
  - 58: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 13:178, 35:149, 5:100, 4:98, 21:71, 33:68, 14:60, 19:55, 24:51, 1:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 13:ds=178 fs=11 fl=1 hz=0.016883116883116882, 35:ds=149 fs=3 fl=0 hz=0.00909090909090909, 5:ds=100 fs=20 fl=1 hz=0.023411371237458192, 4:ds=98 fs=19 fl=1 hz=0.02600780234070221, 21:ds=71 fs=36 fl=1 hz=0.04111111111111111, 33:ds=68 fs=14 fl=2 hz=0.0188470066518847, 14:ds=60 fs=44 fl=0 hz=0.047311827956989246, 19:ds=55 fs=35 fl=1 hz=0.03956043956043956, 24:ds=51 fs=46 fl=0 hz=0.04935622317596566, 1:ds=48 fs=0 fl=0 hz=0.002103049421661409

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S23: ds=82 flags=purple
- S24: ds=75 flags=blue+purple
- S17: ds=69 flags=red+purple
- S20: ds=68 flags=purple
- S22: ds=56 flags=purple
- S5: ds=48 flags=blue+purple
- S13: ds=31 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 049: score=4 tags=FLT,MIR,RS
  - 058: score=4 tags=FLT,MIR,RS
  - 238: score=4 tags=FLT,MIR,RS
  - 247: score=4 tags=FLT,MIR,RS
  - 013: score=3 tags=FLT,RS
  - 067: score=3 tags=FLT,RS
  - 139: score=3 tags=FLT,RS
  - 148: score=3 tags=FLT,RS
  - 346: score=3 tags=FLT,RS
  - 015: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=1 max=2 last_repeat_gap=73 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=29), P2:0 (gap=39), P3:4 (gap=11)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 845: score=46.709601428571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 844: score=43.64353571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 345: score=42.6153 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 344: score=42.380921428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 645: score=40.502471428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 644: score=40.26809285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=39.75801 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 895: score=37.23052142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 848: score=37.19250642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 894: score=36.99614285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 008: ds=966 sev=B
- 589: ds=899 sev=B
- 244: ds=826 sev=B
- 035: ds=776 sev=B
- 122: ds=760 sev=B
- 778: ds=756 sev=B
- 336: ds=755 sev=B
- 368: ds=745 sev=B
- 588: ds=721 sev=B
- 118: ds=694 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=59 sev=purple
  - 55: ds=58 sev=purple
  - 11: ds=29 sev=purple
  - 66: ds=27 sev=purple
  - 22: ds=13 sev=-
  - 44: ds=11 sev=-
  - 33: ds=9 sev=-
  - 00: ds=5 sev=-
  - 77: ds=2 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 05: ds=88 sev=red
  - 06: ds=66 sev=red
  - 04: ds=47 sev=blue
  - 02: ds=43 sev=blue
  - 09: ds=43 sev=blue
  - 12: ds=42 sev=blue
  - 58: ds=38 sev=blue
  - 17: ds=35 sev=purple
  - 35: ds=34 sev=purple
  - 23: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:394, 16:220, 5:131, 17:108, 27:107, 33:100, 13:90, 3:88, 4:85, 35:74

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=394 fs=1 fl=3 hz=0.008888888888888889, 16:ds=220 fs=2 fl=1 hz=0.00657030223390276, 5:ds=131 fs=23 fl=2 hz=0.031685678073510776, 17:ds=108 fs=16 fl=3 hz=0.021420518602029315, 27:ds=107 fs=21 fl=1 hz=0.025142857142857144, 33:ds=100 fs=15 fl=2 hz=0.01893095768374165, 13:ds=90 fs=18 fl=0 hz=0.022511848341232227, 3:ds=88 fs=26 fl=0 hz=0.03082191780821918, 4:ds=85 fs=17 fl=2 hz=0.021566401816118047, 35:ds=74 fs=2 fl=1 hz=0.013636363636363637

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=86 flags=purple
- S3: ds=85 flags=purple
- S22: ds=83 flags=purple
- S20: ds=64 flags=red+purple
- S4: ds=60 flags=purple
- S9: ds=49 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '1'], 'pairs': {'remaining_count': 0}}
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
- current_index=20 streak=1 max=3 last_repeat_gap=20 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=23), P2:4 (gap=20), P3:3 (gap=25)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 845: score=46.709601428571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 844: score=43.64353571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 345: score=42.6153 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 344: score=42.380921428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 645: score=40.502471428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 644: score=40.26809285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=39.75801 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 895: score=37.23052142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 848: score=37.19250642857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 894: score=36.99614285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=977 sev=B
- 699: ds=967 sev=B
- 019: ds=952 sev=B
- 449: ds=827 sev=B
- 244: ds=782 sev=B
- 116: ds=767 sev=B
- 229: ds=757 sev=B
- 055: ds=725 sev=B
- 399: ds=683 sev=B
- 000: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=92 sev=blue
  - 33: ds=89 sev=blue
  - 44: ds=56 sev=purple
  - 22: ds=43 sev=purple
  - 88: ds=28 sev=purple
  - 66: ds=21 sev=-
  - 11: ds=12 sev=-
  - 00: ds=10 sev=-
  - 77: ds=5 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 36: ds=79 sev=red
  - 35: ds=66 sev=red
  - 24: ds=64 sev=red
  - 03: ds=51 sev=blue
  - 08: ds=49 sev=blue
  - 34: ds=40 sev=blue
  - 28: ds=39 sev=blue
  - 69: ds=37 sev=blue
  - 48: ds=34 sev=purple
  - 04: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:229, 32:126, 13:89, 21:85, 28:80, 31:60, 11:57, 5:50, 4:49, 19:42

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=229 fs=1 fl=2 hz=0.005270092226613966, 32:ds=126 fs=1 fl=2 hz=0.007079646017699115, 13:ds=89 fs=14 fl=1 hz=0.01839080459770115, 21:ds=85 fs=54 fl=0 hz=0.06242774566473988, 28:ds=80 fs=20 fl=2 hz=0.024043715846994534, 31:ds=60 fs=18 fl=3 hz=0.02458100558659218, 11:ds=57 fs=50 fl=0 hz=0.05405405405405406, 5:ds=50 fs=10 fl=3 hz=0.014238773274917854, 4:ds=49 fs=24 fl=0 hz=0.02575107296137339, 19:ds=42 fs=27 fl=2 hz=0.03049421661409043

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=68 flags=red+purple
- S4: ds=51 flags=purple
- S6: ds=47 flags=red+purple
- S23: ds=41 flags=blue+purple
- S20: ds=34 flags=purple

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

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 055 -> combined:789(B); evening:725(B)
- 244 -> evening:782(B); midday:826(B)
- 368 -> combined:714(B); midday:745(B)
- 668 -> combined:757(B); evening:668(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:45(blue); evening:51(blue)
- 04 -> combined:58(red); evening:29(purple); midday:47(blue)
- 09 -> combined:58(red); evening:29(purple); midday:43(blue)
- 13 -> combined:25(purple); evening:25(purple)
- 22 -> combined:27(purple); evening:43(purple)
- 28 -> combined:41(blue); evening:39(blue)
- 35 -> combined:69(red); evening:66(red); midday:34(purple)
- 36 -> combined:47(blue); evening:79(red)
- 55 -> combined:117(red); evening:92(blue); midday:58(purple)
- 58 -> combined:36(purple); midday:38(blue)
- 66 -> combined:42(purple); midday:27(purple)
- 68 -> combined:46(blue); midday:30(purple)
- 69 -> combined:55(blue); evening:37(blue); midday:27(purple)
- 88 -> combined:56(purple); evening:28(purple); midday:59(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 8(4.591678571428572)[R1,Mirror-Echo], 3(3.329064285714286)[R2,Mirror-Echo], 6(2.2162357142857143)[R3,XVAR-Cons(CM)], 5(1.4658571428571427)[R1,Double-Pressure], 1(1.3329642857142856)[R2,Mirror-Echo]
- P2: 4(7.399035714285714)[R1,Mirror-Echo], 6(3.6228999999999996)[R2,XVAR-Cons(CM)], 9(3.251642857142857)[R3,Mirror-Echo], 0(1.7449999999999999)[R1,Double-Pressure], 3(0.2746642857142857)[R3,Swap]
- P3: 5(6.8872)[R2,XVAR-Cons(CEM)], 4(6.652821428571428)[R1,XVAR-Cons(CEM)], 8(1.7879142857142858)[R3,XVAR-Cons(CM)], 3(1.3464285714285715)[R1,Double-Pressure]
