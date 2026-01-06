# Aux Summary — PuertoRico4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2026-01-03/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=917, 144, 913, 451, 643
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2026-01-03/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=144, 451, 098, 875, 793
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2026-01-03/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=917, 913, 643, 785, 490

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=3 last_repeat_gap=7 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=60), P2:3 (gap=20), P3:9 (gap=35)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=60)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.587912857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=47.34522178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=47.05128178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=45.808590714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 329: score=45.72003464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 339: score=41.80638571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 326: score=41.550785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 336: score=40.33975 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 269: score=40.02285178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 219: score=39.69710714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=993 sev=B
- 447: ds=984 sev=B
- 000: ds=732 sev=B
- 039: ds=720 sev=B
- 466: ds=716 sev=B
- 677: ds=694 sev=B
- 259: ds=685 sev=B
- 577: ds=675 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=64 sev=purple
  - 77: ds=63 sev=purple
  - 99: ds=54 sev=purple
  - 11: ds=48 sev=purple
  - 55: ds=29 sev=purple
  - 33: ds=24 sev=-
  - 66: ds=23 sev=-
  - 88: ds=16 sev=-
  - 00: ds=14 sev=-
  - 44: ds=1 sev=-
- non_repeating:
  - 47: ds=172 sev=red
  - 24: ds=86 sev=red
  - 25: ds=61 sev=red
  - 48: ds=50 sev=blue
  - 23: ds=47 sev=blue
  - 56: ds=43 sev=blue
  - 59: ds=43 sev=blue
  - 05: ds=41 sev=blue
  - 28: ds=36 sev=purple
  - 35: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:191, 27:132, 5:95, 32:89, 26:84, 31:81, 28:63, 18:55, 34:54, 33:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=191 fs=18 fl=1 hz=0.025477707006369428, 27:ds=132 fs=24 fl=1 hz=0.029868578255675033, 5:ds=95 fs=27 fl=1 hz=0.0343980343980344, 32:ds=89 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=84 fs=4 fl=2 hz=0.01020408163265306, 31:ds=81 fs=14 fl=3 hz=0.018619934282584887, 28:ds=63 fs=26 fl=0 hz=0.0278372591006424, 18:ds=55 fs=20 fl=0 hz=0.022727272727272728, 34:ds=54 fs=26 fl=0 hz=0.02857142857142857, 33:ds=51 fs=10 fl=0 hz=0.016516516516516516

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=81 flags=purple
- S23: ds=63 flags=blue+purple
- S26: ds=54 flags=blue+purple
- S8: ds=48 flags=purple
- S6: ds=44 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '8'], 'pairs': {'remaining_count': 1}}
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
- current_index=25 streak=1 max=3 last_repeat_gap=60 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=30), P2:1 (gap=26), P3:9 (gap=17)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.587912857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=47.34522178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=47.05128178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=45.808590714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 329: score=45.72003464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 339: score=41.80638571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 326: score=41.550785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 336: score=40.33975 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 269: score=40.02285178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 219: score=39.69710714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=960 sev=B
- 299: ds=951 sev=B
- 003: ds=942 sev=B
- 077: ds=928 sev=B
- 333: ds=877 sev=B
- 555: ds=851 sev=B
- 088: ds=822 sev=B
- 888: ds=816 sev=B
- 666: ds=801 sev=B
- 447: ds=740 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=107 sev=red
  - 22: ds=80 sev=blue
  - 11: ds=56 sev=purple
  - 99: ds=40 sev=purple
  - 77: ds=31 sev=purple
  - 33: ds=25 sev=purple
  - 88: ds=22 sev=-
  - 55: ds=14 sev=-
  - 66: ds=11 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 47: ds=113 sev=red
  - 24: ds=59 sev=red
  - 38: ds=44 sev=blue
  - 03: ds=43 sev=blue
  - 04: ds=43 sev=blue
  - 35: ds=41 sev=blue
  - 48: ds=33 sev=purple
  - 19: ds=32 sev=purple
  - 25: ds=30 sev=purple
  - 18: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 29:97, 10:95, 27:94, 26:91, 3:84, 16:56, 23:51, 15:49, 5:47, 32:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 29:ds=97 fs=16 fl=2 hz=0.020809248554913295, 10:ds=95 fs=20 fl=3 hz=0.026376146788990827, 27:ds=94 fs=19 fl=1 hz=0.024721878862793572, 26:ds=91 fs=7 fl=2 hz=0.011682242990654207, 3:ds=84 fs=31 fl=0 hz=0.03506787330316742, 16:ds=56 fs=4 fl=2 hz=0.009695290858725763, 23:ds=51 fs=31 fl=1 hz=0.034782608695652174, 15:ds=49 fs=25 fl=0 hz=0.026939655172413795, 5:ds=47 fs=28 fl=0 hz=0.03181818181818182, 32:ds=44 fs=2 fl=1 hz=0.006112469437652812

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=43 flags=purple
- S25: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 036: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=22 streak=1 max=2 last_repeat_gap=2 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=30), P2:5 (gap=46), P3:6 (gap=22)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CEM)), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=46)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 229: score=48.587912857142854 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 239: score=47.34522178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 226: score=47.05128178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 236: score=45.808590714285714 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=lane
- 329: score=45.72003464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 339: score=41.80638571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 326: score=41.550785714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 336: score=40.33975 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 269: score=40.02285178571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 219: score=39.69710714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=992 sev=B
- 579: ds=973 sev=B
- 114: ds=917 sev=B
- 555: ds=856 sev=B
- 888: ds=764 sev=B
- 067: ds=753 sev=B
- 446: ds=740 sev=B
- 259: ds=738 sev=B
- 224: ds=724 sev=B
- 449: ds=696 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=144 sev=red
  - 44: ds=140 sev=red
  - 77: ds=42 sev=purple
  - 66: ds=33 sev=purple
  - 22: ds=32 sev=purple
  - 99: ds=27 sev=purple
  - 11: ds=24 sev=-
  - 33: ds=12 sev=-
  - 88: ds=8 sev=-
  - 00: ds=7 sev=-
- non_repeating:
  - 25: ds=100 sev=red
  - 47: ds=86 sev=red
  - 45: ds=70 sev=red
  - 26: ds=63 sev=red
  - 59: ds=56 sev=red
  - 24: ds=43 sev=blue
  - 05: ds=39 sev=blue
  - 56: ds=39 sev=blue
  - 23: ds=30 sev=purple
  - 89: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:449, 32:164, 4:118, 10:105, 31:93, 5:83, 33:69, 27:66, 1:58, 14:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=449 fs=5 fl=1 hz=0.01662049861495845, 32:ds=164 fs=6 fl=1 hz=0.009987515605493134, 4:ds=118 fs=23 fl=2 hz=0.03071253071253071, 10:ds=105 fs=16 fl=2 hz=0.0234375, 31:ds=93 fs=18 fl=3 hz=0.02394526795895097, 5:ds=83 fs=18 fl=2 hz=0.022446689113355782, 33:ds=69 fs=12 fl=1 hz=0.017361111111111112, 27:ds=66 fs=18 fl=1 hz=0.02358490566037736, 1:ds=58 fs=4 fl=4 hz=0.00909090909090909, 14:ds=48 fs=37 fl=1 hz=0.04171240395170143

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=76 flags=purple
- S24: ds=67 flags=purple
- S18: ds=52 flags=red+purple
- S23: ds=47 flags=blue+purple
- S16: ds=42 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=3 tags=FLT,RS
  - 129: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 039: score=2 tags=RS
  - 048: score=2 tags=RS
  - 057: score=2 tags=RS
  - 138: score=2 tags=RS
  - 147: score=2 tags=RS
  - 156: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 259 -> combined:685(B); evening:738(B)
- 447 -> combined:984(B); midday:740(B)
- 555 -> evening:856(B); midday:851(B)
- 888 -> evening:764(B); midday:816(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:41(blue); evening:39(blue)
- 11 -> combined:48(purple); midday:56(purple)
- 22 -> combined:64(purple); evening:32(purple); midday:80(blue)
- 23 -> combined:47(blue); evening:30(purple)
- 24 -> combined:86(red); evening:43(blue); midday:59(red)
- 25 -> combined:61(red); evening:100(red); midday:30(purple)
- 47 -> combined:172(red); evening:86(red); midday:113(red)
- 48 -> combined:50(blue); evening:25(purple); midday:33(purple)
- 55 -> combined:29(purple); evening:144(red)
- 56 -> combined:43(blue); evening:39(blue)
- 59 -> combined:43(blue); evening:56(red)
- 77 -> combined:63(purple); evening:42(purple); midday:31(purple)
- 99 -> combined:54(purple); evening:27(purple); midday:40(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.891428571428571)[R1,XVAR-Cons(CEM)], 3(6.397621428571428)[R2,XVAR-Cons(CEM)], 5(1.9518642857142858)[R3,XVAR-Cons(CM)], 1(1.0135)[R2,Double-Pressure]
- P2: 2(3.790407142857143)[R2,XVAR-Cons(CE)], 3(3.5793714285714286)[R1,XVAR-Cons(CM)], 1(1.4762857142857142)[R1,Double-Pressure], 5(1.145)[R1,Swap], 7(0.5755357142857142)[R3,Mirror-Echo]
- P3: 9(7.829392857142857)[R1,XVAR-Cons(CEM)], 6(7.362757142857143)[R2,XVAR-Cons(CEM)], 4(0.4184071428571428)[R3,Mirror-Echo], 2(0.2414285714285714)[R3,Swap], 0(0.20435714285714285)[R3,Swap]
