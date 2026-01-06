# Aux Summary — PuertoRico4 — 2026-01-02

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-02/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-01.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2026-01-02/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=913, 451, 643, 098, 785
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2026-01-02/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=451, 098, 875, 793, 962
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2026-01-02/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=913, 643, 785, 490, 902

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=5 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=58), P2:3 (gap=18), P3:9 (gap=33)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=58)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.84557857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 224: score=47.621715714285706 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=46.803801785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 234: score=45.57993892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=45.13639214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 329: score=45.12171428571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 324: score=43.89785142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=43.094615357142864 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 339: score=43.0799375 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 334: score=41.856074642857145 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=991 sev=B
- 447: ds=982 sev=B
- 000: ds=730 sev=B
- 039: ds=718 sev=B
- 466: ds=714 sev=B
- 677: ds=692 sev=B
- 259: ds=683 sev=B
- 577: ds=673 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=62 sev=purple
  - 77: ds=61 sev=purple
  - 99: ds=52 sev=purple
  - 44: ds=47 sev=purple
  - 11: ds=46 sev=purple
  - 55: ds=27 sev=purple
  - 33: ds=22 sev=-
  - 66: ds=21 sev=-
  - 88: ds=14 sev=-
  - 00: ds=12 sev=-
- non_repeating:
  - 47: ds=170 sev=red
  - 24: ds=84 sev=red
  - 25: ds=59 sev=red
  - 48: ds=48 sev=blue
  - 23: ds=45 sev=blue
  - 56: ds=41 sev=blue
  - 59: ds=41 sev=blue
  - 05: ds=39 sev=blue
  - 28: ds=34 sev=purple
  - 35: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:189, 27:130, 5:93, 32:87, 26:82, 31:79, 28:61, 18:53, 34:52, 33:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=189 fs=18 fl=1 hz=0.025477707006369428, 27:ds=130 fs=24 fl=1 hz=0.029868578255675033, 5:ds=93 fs=27 fl=1 hz=0.0343980343980344, 32:ds=87 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=82 fs=4 fl=2 hz=0.01020408163265306, 31:ds=79 fs=14 fl=3 hz=0.018619934282584887, 28:ds=61 fs=26 fl=0 hz=0.0278372591006424, 18:ds=53 fs=20 fl=0 hz=0.022727272727272728, 34:ds=52 fs=26 fl=0 hz=0.02857142857142857, 33:ds=49 fs=10 fl=0 hz=0.016516516516516516

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=79 flags=purple
- S23: ds=61 flags=blue+purple
- S26: ds=52 flags=blue+purple
- S8: ds=46 flags=purple
- S6: ds=42 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 123: score=1 tags=FLT
  - 124: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=59 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=29), P2:1 (gap=25), P3:9 (gap=16)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.84557857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 224: score=47.621715714285706 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=46.803801785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 234: score=45.57993892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=45.13639214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 329: score=45.12171428571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 324: score=43.89785142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=43.094615357142864 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 339: score=43.0799375 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 334: score=41.856074642857145 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=959 sev=B
- 299: ds=950 sev=B
- 003: ds=941 sev=B
- 077: ds=927 sev=B
- 333: ds=876 sev=B
- 555: ds=850 sev=B
- 088: ds=821 sev=B
- 888: ds=815 sev=B
- 666: ds=800 sev=B
- 447: ds=739 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=106 sev=blue
  - 22: ds=79 sev=blue
  - 11: ds=55 sev=purple
  - 99: ds=39 sev=purple
  - 77: ds=30 sev=purple
  - 33: ds=24 sev=-
  - 44: ds=23 sev=-
  - 88: ds=21 sev=-
  - 55: ds=13 sev=-
  - 66: ds=10 sev=-
- non_repeating:
  - 47: ds=112 sev=red
  - 24: ds=58 sev=red
  - 38: ds=43 sev=blue
  - 03: ds=42 sev=blue
  - 04: ds=42 sev=blue
  - 35: ds=40 sev=blue
  - 48: ds=32 sev=purple
  - 19: ds=31 sev=purple
  - 25: ds=29 sev=purple
  - 18: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 25:138, 29:96, 10:94, 27:93, 26:90, 3:83, 16:55, 23:50, 15:48, 5:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 25:ds=138 fs=18 fl=0 hz=0.02211874272409779, 29:ds=96 fs=16 fl=2 hz=0.020809248554913295, 10:ds=94 fs=20 fl=3 hz=0.026376146788990827, 27:ds=93 fs=19 fl=1 hz=0.024721878862793572, 26:ds=90 fs=7 fl=2 hz=0.011682242990654207, 3:ds=83 fs=31 fl=0 hz=0.03506787330316742, 16:ds=55 fs=4 fl=2 hz=0.009695290858725763, 23:ds=50 fs=31 fl=1 hz=0.034782608695652174, 15:ds=48 fs=25 fl=0 hz=0.026939655172413795, 5:ds=46 fs=28 fl=0 hz=0.03181818181818182

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=42 flags=purple
- S25: ds=39 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- _no candidates_

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=2 max=2 last_repeat_gap=1 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=29), P2:5 (gap=45), P3:6 (gap=21)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=45)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.84557857142857 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 224: score=47.621715714285706 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=46.803801785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 234: score=45.57993892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=45.13639214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 329: score=45.12171428571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 324: score=43.89785142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=43.094615357142864 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 339: score=43.0799375 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 334: score=41.856074642857145 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=991 sev=B
- 579: ds=972 sev=B
- 114: ds=916 sev=B
- 555: ds=855 sev=B
- 888: ds=763 sev=B
- 067: ds=752 sev=B
- 446: ds=739 sev=B
- 259: ds=737 sev=B
- 224: ds=723 sev=B
- 449: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=143 sev=red
  - 44: ds=139 sev=red
  - 77: ds=41 sev=purple
  - 66: ds=32 sev=purple
  - 22: ds=31 sev=purple
  - 99: ds=26 sev=purple
  - 11: ds=23 sev=-
  - 33: ds=11 sev=-
  - 88: ds=7 sev=-
  - 00: ds=6 sev=-
- non_repeating:
  - 25: ds=99 sev=red
  - 47: ds=85 sev=red
  - 45: ds=69 sev=red
  - 26: ds=62 sev=red
  - 59: ds=55 sev=blue
  - 79: ds=46 sev=blue
  - 24: ds=42 sev=blue
  - 05: ds=38 sev=blue
  - 56: ds=38 sev=blue
  - 23: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:448, 32:163, 4:117, 22:116, 10:104, 31:92, 5:82, 33:68, 27:65, 1:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=448 fs=5 fl=1 hz=0.01662049861495845, 32:ds=163 fs=6 fl=1 hz=0.009987515605493134, 4:ds=117 fs=23 fl=2 hz=0.03071253071253071, 22:ds=116 fs=34 fl=0 hz=0.04, 10:ds=104 fs=16 fl=2 hz=0.0234375, 31:ds=92 fs=18 fl=3 hz=0.02394526795895097, 5:ds=82 fs=18 fl=2 hz=0.022446689113355782, 33:ds=68 fs=12 fl=1 hz=0.017361111111111112, 27:ds=65 fs=18 fl=1 hz=0.02358490566037736, 1:ds=57 fs=4 fl=4 hz=0.00909090909090909

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=75 flags=purple
- S24: ds=66 flags=purple
- S18: ds=51 flags=red+purple
- S23: ds=46 flags=blue+purple
- S16: ds=41 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=RS
  - 039: score=2 tags=RS
  - 048: score=2 tags=RS
  - 057: score=2 tags=RS
  - 129: score=2 tags=RS
  - 138: score=2 tags=RS
  - 147: score=2 tags=RS
  - 156: score=2 tags=RS
  - 237: score=2 tags=RS
  - 246: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 259 -> combined:683(B); evening:737(B)
- 447 -> combined:982(B); midday:739(B)
- 555 -> evening:855(B); midday:850(B)
- 888 -> evening:763(B); midday:815(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:39(blue); evening:38(blue)
- 11 -> combined:46(purple); midday:55(purple)
- 22 -> combined:62(purple); evening:31(purple); midday:79(blue)
- 23 -> combined:45(blue); evening:29(purple)
- 24 -> combined:84(red); evening:42(blue); midday:58(red)
- 25 -> combined:59(red); evening:99(red); midday:29(purple)
- 44 -> combined:47(purple); evening:139(red)
- 47 -> combined:170(red); evening:85(red); midday:112(red)
- 48 -> combined:48(blue); midday:32(purple)
- 55 -> combined:27(purple); evening:143(red)
- 56 -> combined:41(blue); evening:38(blue)
- 59 -> combined:41(blue); evening:55(blue)
- 77 -> combined:61(purple); evening:41(purple); midday:30(purple)
- 99 -> combined:52(purple); evening:26(purple); midday:39(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.831714285714286)[R1,XVAR-Cons(CEM)], 3(5.593571428571428)[R3,XVAR-Cons(CEM)], 1(3.3666)[R2,XVAR-Cons(CE)], 5(0.3687142857142857)[R3,Swap]
- P2: 2(3.7194)[R2,XVAR-Cons(CE)], 3(2.813507142857143)[R1,XVAR-Cons(CM)], 1(1.4464285714285714)[R1,Double-Pressure], 4(1.1806999999999999)[R2,Double-Pressure], 5(1.145)[R1,Swap]
- P3: 9(8.184171428571428)[R1,Mirror-Echo], 4(7.119942857142856)[R2,Mirror-Echo], 6(5.828357142857143)[R3,XVAR-Cons(CEM)]
