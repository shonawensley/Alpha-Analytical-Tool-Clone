# Aux Summary — PuertoRico4 — 2025-12-30

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-12-30/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-12-29.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2025-12-30/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=785, 875, 490, 793, 902
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2025-12-30/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=875, 793, 962, 087, 627
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2025-12-30/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=785, 490, 902, 517, 007

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=2 max=3 last_repeat_gap=1 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=54), P2:4 (gap=34), P3:9 (gap=29)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 249: score=52.70676678571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 259: score=48.95140714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 244: score=43.030049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 254: score=42.69296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=42.48018571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 159: score=42.143100000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 246: score=41.59587857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=41.258792857142865 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 219: score=38.53932857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 229: score=38.45871428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 668: ds=998 sev=B
- 001: ds=987 sev=B
- 447: ds=978 sev=B
- 000: ds=726 sev=B
- 039: ds=714 sev=B
- 466: ds=710 sev=B
- 677: ds=688 sev=B
- 259: ds=679 sev=B
- 577: ds=669 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=58 sev=purple
  - 77: ds=57 sev=purple
  - 99: ds=48 sev=purple
  - 44: ds=43 sev=purple
  - 11: ds=42 sev=purple
  - 55: ds=23 sev=-
  - 33: ds=18 sev=-
  - 66: ds=17 sev=-
  - 88: ds=10 sev=-
  - 00: ds=8 sev=-
- non_repeating:
  - 47: ds=166 sev=red
  - 24: ds=80 sev=red
  - 45: ds=77 sev=red
  - 25: ds=55 sev=blue
  - 89: ds=48 sev=blue
  - 48: ds=44 sev=blue
  - 23: ds=41 sev=blue
  - 56: ds=37 sev=blue
  - 59: ds=37 sev=blue
  - 05: ds=35 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 10:185, 27:126, 5:89, 32:83, 26:78, 14:77, 31:75, 28:57, 18:49, 34:48

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 10:ds=185 fs=18 fl=1 hz=0.025477707006369428, 27:ds=126 fs=24 fl=1 hz=0.029868578255675033, 5:ds=89 fs=27 fl=1 hz=0.0343980343980344, 32:ds=83 fs=2 fl=2 hz=0.0071633237822349575, 26:ds=78 fs=4 fl=2 hz=0.01020408163265306, 14:ds=77 fs=44 fl=1 hz=0.049723756906077346, 31:ds=75 fs=14 fl=3 hz=0.018619934282584887, 28:ds=57 fs=26 fl=0 hz=0.0278372591006424, 18:ds=49 fs=21 fl=0 hz=0.023182297154899896, 34:ds=48 fs=26 fl=0 hz=0.02857142857142857

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=75 flags=purple
- S23: ds=57 flags=blue+purple
- S26: ds=48 flags=blue+purple
- S8: ds=42 flags=purple
- S6: ds=38 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '6'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 036: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=3 last_repeat_gap=57 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=27), P2:1 (gap=23), P3:1 (gap=16)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 249: score=52.70676678571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 259: score=48.95140714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 244: score=43.030049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 254: score=42.69296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=42.48018571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 159: score=42.143100000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 246: score=41.59587857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=41.258792857142865 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 219: score=38.53932857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 229: score=38.45871428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 111: ds=957 sev=B
- 299: ds=948 sev=B
- 003: ds=939 sev=B
- 077: ds=925 sev=B
- 333: ds=874 sev=B
- 555: ds=848 sev=B
- 088: ds=819 sev=B
- 888: ds=813 sev=B
- 666: ds=798 sev=B
- 447: ds=737 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=104 sev=blue
  - 22: ds=77 sev=blue
  - 11: ds=53 sev=purple
  - 99: ds=37 sev=purple
  - 77: ds=28 sev=purple
  - 33: ds=22 sev=-
  - 44: ds=21 sev=-
  - 88: ds=19 sev=-
  - 55: ds=11 sev=-
  - 66: ds=8 sev=-
- non_repeating:
  - 47: ds=110 sev=red
  - 24: ds=56 sev=red
  - 38: ds=41 sev=blue
  - 03: ds=40 sev=blue
  - 04: ds=40 sev=blue
  - 35: ds=38 sev=blue
  - 45: ds=38 sev=blue
  - 48: ds=30 sev=purple
  - 89: ds=30 sev=purple
  - 19: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 25:136, 29:94, 10:92, 27:91, 26:88, 3:81, 16:53, 23:48, 15:46, 5:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 25:ds=136 fs=18 fl=0 hz=0.02211874272409779, 29:ds=94 fs=16 fl=2 hz=0.020809248554913295, 10:ds=92 fs=20 fl=3 hz=0.026376146788990827, 27:ds=91 fs=19 fl=1 hz=0.024721878862793572, 26:ds=88 fs=7 fl=2 hz=0.011682242990654207, 3:ds=81 fs=31 fl=0 hz=0.03506787330316742, 16:ds=53 fs=4 fl=2 hz=0.009695290858725763, 23:ds=48 fs=31 fl=1 hz=0.034782608695652174, 15:ds=46 fs=25 fl=0 hz=0.026939655172413795, 5:ds=44 fs=28 fl=0 hz=0.03181818181818182

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S7: ds=40 flags=purple
- S25: ds=37 flags=purple

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
- current_index=11 streak=1 max=2 last_repeat_gap=6 last_repeat_index=23

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=27), P2:5 (gap=43), P3:6 (gap=19)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P1 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P2:5 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 249: score=52.70676678571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 259: score=48.95140714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 244: score=43.030049999999996 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 254: score=42.69296428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 149: score=42.48018571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 159: score=42.143100000000004 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 246: score=41.59587857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 256: score=41.258792857142865 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 219: score=38.53932857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 229: score=38.45871428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=989 sev=B
- 579: ds=970 sev=B
- 114: ds=914 sev=B
- 555: ds=853 sev=B
- 888: ds=761 sev=B
- 067: ds=750 sev=B
- 446: ds=737 sev=B
- 259: ds=735 sev=B
- 224: ds=721 sev=B
- 449: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=141 sev=red
  - 44: ds=137 sev=red
  - 77: ds=39 sev=purple
  - 66: ds=30 sev=purple
  - 22: ds=29 sev=purple
  - 99: ds=24 sev=-
  - 11: ds=21 sev=-
  - 33: ds=9 sev=-
  - 88: ds=5 sev=-
  - 00: ds=4 sev=-
- non_repeating:
  - 25: ds=97 sev=red
  - 47: ds=83 sev=red
  - 45: ds=67 sev=red
  - 26: ds=60 sev=red
  - 39: ds=53 sev=blue
  - 59: ds=53 sev=blue
  - 79: ds=44 sev=blue
  - 24: ds=40 sev=blue
  - 34: ds=40 sev=blue
  - 05: ds=36 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:446, 32:161, 4:115, 22:114, 10:102, 31:90, 5:80, 33:66, 27:63, 1:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=446 fs=5 fl=1 hz=0.01662049861495845, 32:ds=161 fs=6 fl=1 hz=0.009987515605493134, 4:ds=115 fs=23 fl=2 hz=0.03071253071253071, 22:ds=114 fs=34 fl=0 hz=0.04, 10:ds=102 fs=16 fl=2 hz=0.0234375, 31:ds=90 fs=18 fl=3 hz=0.02394526795895097, 5:ds=80 fs=18 fl=2 hz=0.022446689113355782, 33:ds=66 fs=12 fl=1 hz=0.017361111111111112, 27:ds=63 fs=18 fl=1 hz=0.02358490566037736, 1:ds=55 fs=4 fl=4 hz=0.00909090909090909

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S2: ds=73 flags=purple
- S24: ds=64 flags=purple
- S18: ds=49 flags=red+purple
- S23: ds=44 flags=blue+purple
- S16: ds=39 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [3], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 039: score=3 tags=FLT,RS
  - 138: score=3 tags=FLT,RS
  - 156: score=3 tags=FLT,RS
  - 237: score=3 tags=FLT,RS
  - 246: score=3 tags=FLT,RS
  - 345: score=3 tags=FLT,RS
  - 678: score=3 tags=FLT,RS
  - 012: score=2 tags=RS
  - 048: score=2 tags=RS
  - 057: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 259 -> combined:679(B); evening:735(B)
- 447 -> combined:978(B); midday:737(B)
- 555 -> evening:853(B); midday:848(B)
- 888 -> evening:761(B); midday:813(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 05 -> combined:35(purple); evening:36(purple)
- 11 -> combined:42(purple); midday:53(purple)
- 19 -> combined:34(purple); midday:29(purple)
- 22 -> combined:58(purple); evening:29(purple); midday:77(blue)
- 23 -> combined:41(blue); evening:27(purple)
- 24 -> combined:80(red); evening:40(blue); midday:56(red)
- 25 -> combined:55(blue); evening:97(red); midday:27(purple)
- 44 -> combined:43(purple); evening:137(red)
- 45 -> combined:77(red); evening:67(red); midday:38(blue)
- 47 -> combined:166(red); evening:83(red); midday:110(red)
- 48 -> combined:44(blue); midday:30(purple)
- 56 -> combined:37(blue); evening:36(purple)
- 59 -> combined:37(blue); evening:53(blue)
- 77 -> combined:57(purple); evening:39(purple); midday:28(purple)
- 89 -> combined:48(blue); midday:30(purple)
- 99 -> combined:48(purple); midday:37(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(8.612285714285715)[R1,XVAR-Cons(CEM)], 1(3.3039785714285714)[R2,XVAR-Cons(CE)], 3(1.8384285714285715)[R3,XVAR-Cons(CM)], 4(1.1389)[R2,Double-Pressure], 6(0.3317928571428571)[R3,Mirror-Echo]
- P2: 4(7.135878571428571)[R1,XVAR-Cons(CEM)], 5(6.798792857142857)[R2,XVAR-Cons(CEM)], 1(1.3867142857142856)[R1,Double-Pressure], 2(1.3060999999999998)[R2,Double-Pressure], 3(0.29800000000000004)[R3,Swap]
- P3: 9(7.040328571428572)[R1,Mirror-Echo], 4(3.281885714285714)[R2,Mirror-Echo], 6(2.847714285714286)[R3,XVAR-Cons(CE)], 1(1.0777142857142856)[R1,Double-Pressure], 8(0.38349999999999995)[R2,Swap]
