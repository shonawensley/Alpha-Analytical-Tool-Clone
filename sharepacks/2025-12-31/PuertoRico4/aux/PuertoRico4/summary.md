# Aux Summary — PuertoRico4 — 2025-12-31

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-31/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_30.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2025-12-31/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=643, 098, 785, 875, 490
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2025-12-31/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=098, 875, 793, 962, 087
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2025-12-31/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=643, 785, 490, 902, 517

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=3 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=56), P2:5 (gap=25), P3:9 (gap=31)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:2 (ds=56)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 259: score=53.79019821428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 254: score=51.935921785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 229: score=47.54072285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 359: score=45.132807142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=44.58527 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 354: score=43.52039285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 224: score=42.988214285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 219: score=39.555235714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 329: score=39.50282857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 249: score=39.29846428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=989 sev=B
- 447: ds=980 sev=B
- 000: ds=728 sev=B
- 039: ds=716 sev=B
- 466: ds=712 sev=B
- 677: ds=690 sev=B
- 259: ds=681 sev=B
- 577: ds=671 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=60 sev=purple
  - 77: ds=59 sev=purple
  - 99: ds=50 sev=purple
  - 44: ds=45 sev=purple
  - 11: ds=44 sev=purple
  - 55: ds=25 sev=purple
  - 33: ds=20 sev=-
  - 66: ds=19 sev=-
  - 88: ds=12 sev=-
  - 00: ds=10 sev=-
- non_repeating:
  - 47: ds=168 sev=red
  - 24: ds=82 sev=red
  - 45: ds=79 sev=red
  - 25: ds=57 sev=red
  - 48: ds=46 sev=blue
  - 23: ds=43 sev=blue
  - 56: ds=39 sev=blue
  - 59: ds=39 sev=blue
  - 05: ds=37 sev=blue
  - 19: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:187, 27:128, 5:91, 32:85, 26:80, 31:77, 28:59, 18:51, 34:50, 33:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=187 fs=18 fl=1 hz=0.025477707006369428, 27:ds=128 fs=24 fl=1 hz=0.029868578255675033, 5:ds=91 fs=27 fl=1 hz=0.0343980343980344, 32:ds=85 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=80 fs=4 fl=2 hz=0.01020408163265306, 31:ds=77 fs=14 fl=3 hz=0.018619934282584887, 28:ds=59 fs=26 fl=0 hz=0.0278372591006424, 18:ds=51 fs=20 fl=0 hz=0.022727272727272728, 34:ds=50 fs=26 fl=0 hz=0.02857142857142857, 33:ds=47 fs=10 fl=0 hz=0.016516516516516516

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=77 flags=purple
- S23: ds=59 flags=blue+purple
- S26: ds=50 flags=blue+purple
- S8: ds=44 flags=purple
- S6: ds=40 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2'], 'pairs': {'remaining_count': 1}}
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
- current_index=14 streak=1 max=3 last_repeat_gap=58 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=28), P2:1 (gap=24), P3:1 (gap=17)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 259: score=53.79019821428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 254: score=51.935921785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 229: score=47.54072285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 359: score=45.132807142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=44.58527 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 354: score=43.52039285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 224: score=42.988214285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 219: score=39.555235714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 329: score=39.50282857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 249: score=39.29846428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=958 sev=B
- 299: ds=949 sev=B
- 003: ds=940 sev=B
- 077: ds=926 sev=B
- 333: ds=875 sev=B
- 555: ds=849 sev=B
- 088: ds=820 sev=B
- 888: ds=814 sev=B
- 666: ds=799 sev=B
- 447: ds=738 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=105 sev=blue
  - 22: ds=78 sev=blue
  - 11: ds=54 sev=purple
  - 99: ds=38 sev=purple
  - 77: ds=29 sev=purple
  - 33: ds=23 sev=-
  - 44: ds=22 sev=-
  - 88: ds=20 sev=-
  - 55: ds=12 sev=-
  - 66: ds=9 sev=-
- non_repeating:
  - 47: ds=111 sev=red
  - 24: ds=57 sev=red
  - 38: ds=42 sev=blue
  - 03: ds=41 sev=blue
  - 04: ds=41 sev=blue
  - 35: ds=39 sev=blue
  - 45: ds=39 sev=blue
  - 48: ds=31 sev=purple
  - 19: ds=30 sev=purple
  - 25: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 25:137, 29:95, 10:93, 27:92, 26:89, 3:82, 16:54, 23:49, 15:47, 5:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 25:ds=137 fs=18 fl=0 hz=0.02211874272409779, 29:ds=95 fs=16 fl=2 hz=0.020809248554913295, 10:ds=93 fs=20 fl=3 hz=0.026376146788990827, 27:ds=92 fs=19 fl=1 hz=0.024721878862793572, 26:ds=89 fs=7 fl=2 hz=0.011682242990654207, 3:ds=82 fs=31 fl=0 hz=0.03506787330316742, 16:ds=54 fs=4 fl=2 hz=0.009695290858725763, 23:ds=49 fs=31 fl=1 hz=0.034782608695652174, 15:ds=47 fs=25 fl=0 hz=0.026939655172413795, 5:ds=45 fs=28 fl=0 hz=0.03181818181818182

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=41 flags=purple
- S25: ds=38 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=7 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=28), P2:5 (gap=44), P3:6 (gap=20)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=44)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 259: score=53.79019821428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 254: score=51.935921785714285 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 229: score=47.54072285714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 359: score=45.132807142857146 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=44.58527 tags=Double-Pressure,Lane-C,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=lane
- 354: score=43.52039285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 224: score=42.988214285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 219: score=39.555235714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 329: score=39.50282857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 249: score=39.29846428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=990 sev=B
- 579: ds=971 sev=B
- 114: ds=915 sev=B
- 555: ds=854 sev=B
- 888: ds=762 sev=B
- 067: ds=751 sev=B
- 446: ds=738 sev=B
- 259: ds=736 sev=B
- 224: ds=722 sev=B
- 449: ds=694 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=142 sev=red
  - 44: ds=138 sev=red
  - 77: ds=40 sev=purple
  - 66: ds=31 sev=purple
  - 22: ds=30 sev=purple
  - 99: ds=25 sev=purple
  - 11: ds=22 sev=-
  - 33: ds=10 sev=-
  - 88: ds=6 sev=-
  - 00: ds=5 sev=-
- non_repeating:
  - 25: ds=98 sev=red
  - 47: ds=84 sev=red
  - 45: ds=68 sev=red
  - 26: ds=61 sev=red
  - 39: ds=54 sev=blue
  - 59: ds=54 sev=blue
  - 79: ds=45 sev=blue
  - 24: ds=41 sev=blue
  - 05: ds=37 sev=blue
  - 56: ds=37 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:447, 32:162, 4:116, 22:115, 10:103, 31:91, 5:81, 33:67, 27:64, 1:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=447 fs=5 fl=1 hz=0.01662049861495845, 32:ds=162 fs=6 fl=1 hz=0.009987515605493134, 4:ds=116 fs=23 fl=2 hz=0.03071253071253071, 22:ds=115 fs=34 fl=0 hz=0.04, 10:ds=103 fs=16 fl=2 hz=0.0234375, 31:ds=91 fs=18 fl=3 hz=0.02394526795895097, 5:ds=81 fs=18 fl=2 hz=0.022446689113355782, 33:ds=67 fs=12 fl=1 hz=0.017361111111111112, 27:ds=64 fs=18 fl=1 hz=0.02358490566037736, 1:ds=56 fs=4 fl=4 hz=0.00909090909090909

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=74 flags=purple
- S24: ds=65 flags=purple
- S18: ds=50 flags=red+purple
- S23: ds=45 flags=blue+purple
- S16: ds=40 flags=red+purple

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
- 259 -> combined:681(B); evening:736(B)
- 447 -> combined:980(B); midday:738(B)
- 555 -> evening:854(B); midday:849(B)
- 888 -> evening:762(B); midday:814(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:37(blue); evening:37(blue)
- 11 -> combined:44(purple); midday:54(purple)
- 19 -> combined:36(purple); midday:30(purple)
- 22 -> combined:60(purple); evening:30(purple); midday:78(blue)
- 23 -> combined:43(blue); evening:28(purple)
- 24 -> combined:82(red); evening:41(blue); midday:57(red)
- 25 -> combined:57(red); evening:98(red); midday:28(purple)
- 44 -> combined:45(purple); evening:138(red)
- 45 -> combined:79(red); evening:68(red); midday:39(blue)
- 47 -> combined:168(red); evening:84(red); midday:111(red)
- 48 -> combined:46(blue); midday:31(purple)
- 55 -> combined:25(purple); evening:142(red)
- 56 -> combined:39(blue); evening:37(blue)
- 59 -> combined:39(blue); evening:54(blue)
- 77 -> combined:59(purple); evening:40(purple); midday:29(purple)
- 99 -> combined:50(purple); evening:25(purple); midday:38(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.772)[R1,XVAR-Cons(CEM)], 3(4.674200000000001)[R3,XVAR-Cons(CEM)], 1(3.3017)[R2,XVAR-Cons(CE)], 4(1.0597999999999999)[R2,Double-Pressure]
- P2: 5(7.0919428571428575)[R1,XVAR-Cons(CEM)], 2(2.9619642857142856)[R3,XVAR-Cons(CE)], 1(1.4165714285714284)[R1,Double-Pressure], 4(1.1598)[R2,Double-Pressure], 7(0.5296642857142857)[R3,Mirror-Echo]
- P3: 9(7.866664285714286)[R1,Mirror-Echo], 4(6.254250000000001)[R2,Mirror-Echo], 6(2.9058571428571427)[R3,XVAR-Cons(CE)], 1(1.1075714285714284)[R1,Double-Pressure]
