# Aux Summary — NewJersey4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/NewJersey4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: New Jersey
- combined: live=`data/cleaned/draws/New_Jersey_draws.csv` snap=`sharepacks/2025-12-30/NewJersey4/aux/draws/New_Jersey_draws.csv` n=1000 head=633, 065, 311, 530, 051
- midday: live=`data/cleaned/draws/New_Jersey_Midday_draws.csv` snap=`sharepacks/2025-12-30/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv` n=1000 head=065, 530, 768, 737, 995
- evening: live=`data/cleaned/draws/New_Jersey_Evening_draws.csv` snap=`sharepacks/2025-12-30/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv` n=1000 head=633, 311, 051, 857, 640

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=3 last_repeat_gap=16 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=16), P2:8 (gap=32), P3:6 (gap=32)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 226: score=47.11754642857142 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 286: score=44.0833 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 126: score=43.27424285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 186: score=43.25532857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 222: score=37.162510714285716 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 282: score=37.14359642857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 229: score=35.13417142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 289: score=35.115257142857146 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 129: score=34.306200000000004 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 122: score=34.302307142857146 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 388: ds=982 sev=B
- 005: ds=980 sev=B
- 024: ds=917 sev=B
- 227: ds=883 sev=B
- 266: ds=871 sev=B
- 335: ds=867 sev=B
- 155: ds=853 sev=B
- 277: ds=796 sev=B
- 356: ds=770 sev=B
- 077: ds=764 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=145 sev=red
  - 22: ds=55 sev=purple
  - 88: ds=41 sev=purple
  - 66: ds=32 sev=purple
  - 00: ds=12 sev=-
  - 44: ds=11 sev=-
  - 99: ds=9 sev=-
  - 77: ds=7 sev=-
  - 11: ds=2 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 14: ds=43 sev=blue
  - 08: ds=41 sev=blue
  - 19: ds=37 sev=blue
  - 48: ds=35 sev=purple
  - 39: ds=34 sev=purple
  - 26: ds=30 sev=purple
  - 12: ds=29 sev=purple
  - 25: ds=29 sev=purple
  - 02: ds=28 sev=purple
  - 27: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:796, 35:615, 1:230, 32:146, 28:93, 5:92, 14:86, 17:85, 12:74, 16:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=796 fs=2 fl=0 hz=0.016666666666666666, 35:ds=615 fs=1 fl=0 hz=0.008368200836820083, 1:ds=230 fs=1 fl=2 hz=0.006544502617801046, 32:ds=146 fs=2 fl=2 hz=0.005980861244019139, 28:ds=93 fs=20 fl=1 hz=0.024277456647398846, 5:ds=92 fs=12 fl=3 hz=0.016703786191536747, 14:ds=86 fs=35 fl=1 hz=0.041474654377880185, 17:ds=85 fs=22 fl=2 hz=0.02631578947368421, 12:ds=74 fs=38 fl=1 hz=0.044167610419026046, 16:ds=69 fs=1 fl=4 hz=0.007926023778071334

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=54 flags=purple
- S22: ds=48 flags=purple
- S16: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4', '7', '8', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=3 last_repeat_gap=15 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=30), P2:8 (gap=20), P3:6 (gap=26)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 226: score=47.11754642857142 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 286: score=44.0833 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 126: score=43.27424285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 186: score=43.25532857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 222: score=37.162510714285716 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 282: score=37.14359642857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 229: score=35.13417142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 289: score=35.115257142857146 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 129: score=34.306200000000004 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 122: score=34.302307142857146 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 668: ds=972 sev=B
- 778: ds=968 sev=B
- 069: ds=944 sev=B
- 899: ds=917 sev=B
- 455: ds=908 sev=B
- 009: ds=888 sev=B
- 005: ds=886 sev=B
- 099: ds=841 sev=B
- 359: ds=825 sev=B
- 477: ds=816 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=72 sev=blue
  - 11: ds=42 sev=purple
  - 33: ds=30 sev=purple
  - 00: ds=29 sev=purple
  - 22: ds=27 sev=purple
  - 66: ds=26 sev=purple
  - 88: ds=20 sev=-
  - 44: ds=5 sev=-
  - 99: ds=4 sev=-
  - 77: ds=3 sev=-
- non_repeating:
  - 26: ds=74 sev=red
  - 36: ds=52 sev=blue
  - 17: ds=42 sev=blue
  - 39: ds=37 sev=blue
  - 02: ds=24 sev=-
  - 07: ds=24 sev=-
  - 27: ds=23 sev=-
  - 01: ds=22 sev=-
  - 14: ds=21 sev=-
  - 45: ds=21 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:441, 1:363, 35:307, 32:228, 18:92, 5:72, 22:62, 14:55, 12:48, 28:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=441 fs=1 fl=0 hz=0.007246376811594203, 1:ds=363 fs=4 fl=0 hz=0.009554140127388535, 35:ds=307 fs=3 fl=0 hz=0.008032128514056224, 32:ds=228 fs=0 fl=0 hz=0.003552397868561279, 18:ds=92 fs=15 fl=4 hz=0.021205357142857144, 5:ds=72 fs=12 fl=4 hz=0.017429193899782137, 22:ds=62 fs=44 fl=0 hz=0.049217002237136466, 14:ds=55 fs=37 fl=0 hz=0.039784946236559135, 12:ds=48 fs=41 fl=1 hz=0.04530744336569579, 28:ds=46 fs=20 fl=2 hz=0.023231256599788808

### Sums (source: aux_validation.sums_stats_by_variant)
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=95 flags=purple
- S25: ds=85 flags=blue+purple
- S3: ds=77 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 136: score=2 tags=FLT,MIR
  - 138: score=2 tags=FLT,MIR

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=23 streak=1 max=3 last_repeat_gap=5 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=31), P2:2 (gap=31), P3:9 (gap=19)
- consensus_notes: P1 digit 2 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 226: score=47.11754642857142 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 286: score=44.0833 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 126: score=43.27424285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 186: score=43.25532857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 222: score=37.162510714285716 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 282: score=37.14359642857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 229: score=35.13417142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 289: score=35.115257142857146 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 129: score=34.306200000000004 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 122: score=34.302307142857146 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 035: ds=949 sev=B
- 499: ds=940 sev=B
- 339: ds=926 sev=B
- 556: ds=858 sev=B
- 000: ds=844 sev=B
- 335: ds=824 sev=B
- 569: ds=814 sev=B
- 558: ds=804 sev=B
- 088: ds=801 sev=B
- 022: ds=743 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=107 sev=red
  - 55: ds=100 sev=blue
  - 77: ds=82 sev=blue
  - 44: ds=39 sev=purple
  - 22: ds=31 sev=purple
  - 99: ds=19 sev=-
  - 66: ds=16 sev=-
  - 00: ds=6 sev=-
  - 11: ds=1 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 35: ds=80 sev=red
  - 59: ds=61 sev=red
  - 03: ds=50 sev=blue
  - 08: ds=45 sev=blue
  - 47: ds=37 sev=blue
  - 18: ds=36 sev=purple
  - 25: ds=31 sev=purple
  - 48: ds=28 sev=purple
  - 89: ds=27 sev=purple
  - 34: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:420, 26:398, 13:122, 1:115, 27:103, 4:100, 16:97, 17:94, 19:83, 28:75

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=420 fs=2 fl=1 hz=0.007692307692307693, 26:ds=398 fs=1 fl=0 hz=0.0056179775280898875, 13:ds=122 fs=16 fl=2 hz=0.021686746987951807, 1:ds=115 fs=1 fl=2 hz=0.008213552361396304, 27:ds=103 fs=7 fl=2 hz=0.011325028312570783, 4:ds=100 fs=14 fl=1 hz=0.01839080459770115, 16:ds=97 fs=2 fl=2 hz=0.012658227848101266, 17:ds=94 fs=10 fl=2 hz=0.014051522248243558, 19:ds=83 fs=18 fl=2 hz=0.022172949002217293, 28:ds=75 fs=26 fl=0 hz=0.028291621327529923

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=55 flags=blue+purple
- S23: ds=47 flags=purple
- S17: ds=43 flags=purple
- S14: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 005 -> combined:980(B); midday:886(B)
- 335 -> combined:867(B); evening:824(B)
- 359 -> combined:672(B); midday:825(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 08 -> combined:41(blue); evening:45(blue)
- 14 -> combined:43(blue); evening:25(purple)
- 18 -> combined:25(purple); evening:36(purple)
- 22 -> combined:55(purple); evening:31(purple); midday:27(purple)
- 25 -> combined:29(purple); evening:31(purple)
- 26 -> combined:30(purple); midday:74(red)
- 39 -> combined:34(purple); midday:37(blue)
- 48 -> combined:35(purple); evening:28(purple)
- 55 -> combined:145(red); evening:100(blue); midday:72(blue)
- 66 -> combined:32(purple); midday:26(purple)
- 88 -> combined:41(purple); evening:107(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(4.098571428571429)[R1,XVAR-Cons(CM)], 1(3.2706)[R2,XVAR-Cons(CM)], 4(2.7246428571428574)[R3,XVAR-Cons(CE)], 5(0.9955714285714284)[R1,Swap], 9(0.5599571428571428)[R3,Mirror-Echo]
- P2: 2(7.856171428571429)[R2,XVAR-Cons(CEM)], 8(7.837257142857144)[R1,XVAR-Cons(CEM)], 6(0.30153571428571424)[R3,Swap], 1(0.2612285714285714)[R3,Swap], 0(0.2538571428571429)[R3,Swap]
- P3: 6(8.147471428571428)[R1,XVAR-Cons(CEM)], 9(2.6794285714285713)[R3,XVAR-Cons(CE)], 2(2.675535714285714)[R2,XVAR-Cons(CE)], 3(0.9208)[R2,Double-Pressure], 1(0.5572142857142858)[R3,Mirror-Echo]
